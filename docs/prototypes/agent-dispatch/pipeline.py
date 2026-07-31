"""
PROTOTYPE (ticket #24) — the portable half: what decides that an agent runs.

The question this module answers: a GitHub event arrives (a comment, a label, a
review, an agent's own report). What decides whether an agent dispatches, what
identity its commits carry, what it is allowed to read and write, whose money it
spends, and whether the thing it posts when it finishes triggers another one?

Three runner options are modelled side by side, because #24 recommends one on
non-cost grounds and Noah has since proposed a second:

  A  ACTION      anthropics/claude-code-action, GitHub-hosted runner
  B  SANDCASTLE  @ai-hero/sandcastle driven from a workflow, GitHub-hosted runner
  C  SANDCASTLE_PI  the same harness on a self-hosted runner (the Pi 5 of #3 §6)

And two trigger models, because the ticket assumes one of them:

  COMMENT  a comment body is the command  — what #24's title says
  LABEL    a label transition is the command — what Sandcastle's own repo does

Pure. No I/O, no network, no terminal codes, no GitHub. `prototype_tui.py`
drives it; nothing flows back into here.

**Settled by Noah, 2026-07-31**, after driving this:

1. **The depth cap goes in the workflow, not here.** `World.max_depth` stays in this
   module because the module is what runs, but the ruling is that a guard belongs
   wherever it is most effective — and a cap the workflow cannot see stops being
   enforced the first time somebody adds a second workflow.
2. **`agent:blocked` is an ordinary label in the standard workflow**, cleared by
   whichever agent or human clears the block, with the reason on the comment.
   Recovery belongs in the same traffic as the work. The third *identical* block
   opens an issue rather than retrying, because a label cannot count and #24
   requires an unsatisfiable check to become visible rather than routed around.

Not settled, and the reason this module stops where it does: **every guard below is
per-thread.** The generative research loop — documents emitting debt issues emitting
documents — passes all of them cleanly and is bounded by nothing here.

Two things are load-bearing and are the bits worth lifting out if the design holds:

1. `dispatch()` returns a `Decision` carrying a *reason* in every branch, including
   the branches that dispatch. A pipeline whose refusals are silent is a pipeline
   nobody can audit, and "why did nothing happen?" is the question this design will
   be asked most often.
2. `findings()` is separate from `dispatch()`. Whether a run is *authorised* and
   whether it is *safe* are different questions, and collapsing them is how
   `pull_request_target` gets shipped: the label gate authorises the human, and
   says nothing at all about the code being checked out.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum

# ---------------------------------------------------------------- vocabulary

#: Skills #24 lists as AFK — the ones whose whole interface is a document and a
#: ticket comment. Grilling is deliberately absent: its output is a decision that
#: did not exist before the conversation, so there is nothing to dispatch.
DISPATCHABLE = {
    "research": ("agent:research", "/research", 2.55),
    "verify": ("agent:verify", "/verify", 0.90),
    "survey": ("agent:survey", "/survey", 3.40),
    "review": ("agent:review", "/review", 0.60),
    "revise": ("agent:revise", "/revise", 1.20),
}

#: Applied when a run starts, removed when it ends. Also the concurrency guard
#: that does not depend on GitHub's `concurrency:` block being right.
IN_PROGRESS = "agent:in-progress"
BLOCKED = "agent:blocked"

#: What a finished run asks for next. This is the reason a pipeline exists at
#: all — research that has to be labelled by hand before it is reviewed is a
#: pipeline with a human in the middle of it — and it is also where the loop is:
#: review and revise want each other, forever.
HANDOFF = {
    "research": "review",
    "survey": "review",
    "review": "revise",
    "revise": "review",
    "verify": None,
}

WRITE_ASSOCIATIONS = {"OWNER", "MEMBER", "COLLABORATOR"}


class Trigger(str, Enum):
    COMMENT = "comment-triggered"
    LABEL = "label-triggered"


class Runner(str, Enum):
    ACTION = "claude-code-action"
    SANDCASTLE = "sandcastle (GitHub-hosted)"
    SANDCASTLE_PI = "sandcastle (self-hosted Pi)"


class Identity(str, Enum):
    #: Today: agents inherit the researcher's git config. #23's complaint.
    INHERITED = "researcher's git config"
    #: Sandcastle's own workflows: `git config user.name sandcastle-agent[bot]`.
    #: Author field is a bot; the push is still GITHUB_TOKEN.
    GIT_CONFIG_BOT = "git config bot name"
    #: A GitHub App installation token. Author and pusher are both the App.
    APP = "GitHub App"


class Verdict(str, Enum):
    DISPATCH = "dispatch"
    REFUSE = "refuse"
    IGNORE = "ignore"
    QUEUE = "queue"


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"


class Channel(str, Enum):
    """How untrusted text reaches the agent. The three differ by a lot."""

    #: `${{ github.event.comment.body }}` inside a `run:` block. The comment is
    #: shell on the runner before it is ever a prompt.
    INTERPOLATED = "interpolated into the workflow"
    #: Sandcastle `promptArgs`. Substituted on the host before shell expansion,
    #: and `!`…`` inside an argument value is inert text by construction.
    PROMPT_ARG = "promptArgs (shell-inert)"
    #: The agent runs `gh issue view` itself. Data, arriving as prompt.
    TOOL_FETCHED = "fetched by the agent's own tools"


# ------------------------------------------------------------------- the world


@dataclass(frozen=True)
class Event:
    kind: str  # "comment" | "label" | "review" | "push"
    actor: str
    association: str  # OWNER | MEMBER | COLLABORATOR | CONTRIBUTOR | NONE | BOT
    target: int
    body: str = ""
    label: str | None = None
    #: Set when this event was produced by a run rather than by a person.
    machine: bool = False

    @property
    def is_bot(self) -> bool:
        return self.association == "BOT" or self.machine


@dataclass
class Thread:
    number: int
    title: str
    is_pr: bool = False
    from_fork: bool = False
    open: bool = True
    labels: set[str] = field(default_factory=set)
    #: Set to the actor when someone without write access has commented here.
    #: Their text is in the thread, so it is in the agent's context, whoever
    #: eventually presses the button.
    third_party_text: str | None = None


@dataclass(frozen=True)
class Untrusted:
    """A span of text nobody vouched for, and how it gets in."""

    origin: str
    channel: Channel
    #: True when nobody with a write bit put this text there.
    third_party: bool = False


@dataclass(frozen=True)
class Job:
    skill: str
    runner: Runner
    #: What the runner checks out. `head` on a fork PR is somebody else's code.
    checkout: str
    #: Secrets present in the job's environment while that code runs.
    secrets: tuple[str, ...]
    untrusted: tuple[Untrusted, ...]
    #: The name that lands in `%an` on the commits this run makes.
    author: str
    #: Whether that name is a machine's. §5's check reads this, not the intent.
    author_is_machine: bool
    write_scope: tuple[str, ...]
    cost: float
    concurrency_group: str
    #: True when the runner's filesystem outlives the run.
    persistent_host: bool


@dataclass(frozen=True)
class Decision:
    verdict: Verdict
    reason: str
    job: Job | None = None
    #: Label transitions this decision performs, applied by `apply()`.
    add_labels: tuple[str, ...] = ()
    remove_labels: tuple[str, ...] = ()


@dataclass(frozen=True)
class Finding:
    severity: Severity
    title: str
    detail: str


@dataclass
class Config:
    trigger: Trigger = Trigger.LABEL
    runner: Runner = Runner.SANDCASTLE
    identity: Identity = Identity.GIT_CONFIG_BOT
    #: `pull_request_target` — the footgun #24 names by name. Needed to hand a
    #: fork PR run any secret at all; sufficient to hand a fork PR every secret.
    pr_target: bool = True
    #: The hand-rolled-workflow mistake: pasting the comment body into a `run:`.
    #: Off for ACTION and SANDCASTLE, which never do this; available as a toggle
    #: because a workflow written by hand can always reintroduce it.
    naive_interpolation: bool = False
    #: Whether runs draw metered API credit rather than subscription quota.
    #: All three runners currently draw a `CLAUDE_CODE_OAUTH_TOKEN`, so this is
    #: false — see #27. It exists because #27 also records that Anthropic
    #: *paused*, rather than withdrew, the change that would move Action usage
    #: onto separate credit. Turn it on to see what a ceiling is for.
    metered: bool = False
    daily_ceiling: float = 12.00
    #: Whether a finished run may ask for the next one. Off means every stage is
    #: hand-started, which is a human in the middle of the thing #24 built to
    #: get the human out of the middle of.
    chain_handoff: bool = True
    #: Whether a dispatch request from a machine is honoured at all.
    allow_machine_dispatch: bool = True


@dataclass
class World:
    threads: dict[int, Thread]
    config: Config = field(default_factory=Config)
    running: set[str] = field(default_factory=set)
    day_spend: float = 0.0
    #: (event, decision) in order. The audit trail the whole design is for.
    ledger: list[tuple[Event, Decision]] = field(default_factory=list)
    #: How many machine-triggered events deep the current chain is.
    depth: int = 0
    max_depth: int = 6


# --------------------------------------------------------------- the decision


def _requested_skill(cfg: Config, ev: Event) -> str | None:
    """Which skill, if any, this event is asking for."""
    if cfg.trigger is Trigger.COMMENT:
        if ev.kind != "comment":
            return None
        head = ev.body.strip().split()[0] if ev.body.strip() else ""
        for skill, (_label, command, _cost) in DISPATCHABLE.items():
            if head == command:
                return skill
        return None

    if ev.kind != "label":
        return None
    for skill, (label, _command, _cost) in DISPATCHABLE.items():
        if ev.label == label:
            return skill
    return None


def dispatch(world: World, ev: Event) -> Decision:
    """The whole gate. Pure: reads the world, returns what should happen."""
    cfg = world.config
    skill = _requested_skill(cfg, ev)

    if skill is None:
        return Decision(Verdict.IGNORE, "no command in this event")

    thread = world.threads.get(ev.target)
    if thread is None:
        return Decision(Verdict.IGNORE, f"#{ev.target} does not exist")
    if not thread.open:
        return Decision(Verdict.REFUSE, f"#{thread.number} is closed")

    # --- recursion -------------------------------------------------------
    #
    # Actions declines to re-trigger on events raised by the `github-actions`
    # actor. That guard is a property of the *token*, not of the idea, and it is
    # exactly what an App identity gives up in exchange for a name worth having.
    if ev.is_bot:
        if cfg.identity is not Identity.APP and cfg.trigger is Trigger.COMMENT:
            return Decision(
                Verdict.IGNORE,
                "github-actions actor — the platform's own recursion guard, "
                "which also drops every legitimate handoff",
            )
        if not cfg.allow_machine_dispatch:
            return Decision(
                Verdict.IGNORE,
                "machine dispatch is off — the handoff dies with the loop"
                if cfg.trigger is Trigger.COMMENT
                else "machine dispatch is off — reports were never commands here, "
                "so this rule costs only the handoff",
            )
        if world.depth >= world.max_depth:
            return Decision(
                Verdict.REFUSE,
                f"chain depth {world.depth} hit the cap — nothing else was "
                "going to stop this",
            )

    # --- authorisation ---------------------------------------------------
    #
    # Under LABEL this is not a check at all: GitHub will not let a drive-by
    # apply a label. Under COMMENT it is a check somebody has to write, keep
    # right, and keep right again when GitHub adds an association value.
    if not ev.is_bot and ev.association not in WRITE_ASSOCIATIONS:
        if cfg.trigger is Trigger.COMMENT:
            return Decision(
                Verdict.REFUSE,
                f"@{ev.actor} is {ev.association} — no write bit, no dispatch. "
                "A check this file has to get right, and keep right.",
            )
        return Decision(
            Verdict.REFUSE,
            f"@{ev.actor} labelled without write access — GitHub does not permit "
            "this, so the check below is the platform's, not ours",
        )

    # --- concurrency -----------------------------------------------------
    group = f"agent-mutate-{thread.number}"
    if group in world.running or IN_PROGRESS in thread.labels:
        return Decision(
            Verdict.QUEUE,
            f"{group} is occupied — a second agent on one thread races the first",
        )

    # --- money -----------------------------------------------------------
    cost = DISPATCHABLE[skill][2] if cfg.metered else 0.0
    if world.day_spend + cost > cfg.daily_ceiling:
        return Decision(
            Verdict.REFUSE,
            f"${world.day_spend:.2f} + ${cost:.2f} exceeds the "
            f"${cfg.daily_ceiling:.2f} daily ceiling",
        )

    job = _plan(world, ev, thread, skill, cost)
    reason = (
        f"{skill} requested by @{ev.actor} ({ev.association}) on "
        f"#{thread.number} via {cfg.trigger.value}"
    )
    consumed = (DISPATCHABLE[skill][0],) if cfg.trigger is Trigger.LABEL else ()
    return Decision(
        Verdict.DISPATCH,
        reason,
        job=job,
        add_labels=(IN_PROGRESS,),
        remove_labels=consumed + (BLOCKED,),
    )


def _plan(world: World, ev: Event, thread: Thread, skill: str, cost: float) -> Job:
    cfg = world.config

    # What lands on the commit.
    author, machine = {
        Identity.INHERITED: ("Noah Litov", False),
        Identity.GIT_CONFIG_BOT: ("mosaic-agent[bot]", True),
        Identity.APP: ("mosaic-agent[bot]", True),
    }[cfg.identity]

    # Where the untrusted text goes.
    untrusted: list[Untrusted] = []
    if thread.third_party_text:
        origin = f"@{thread.third_party_text}'s comment on #{thread.number}"
    else:
        origin = f"#{thread.number} thread text"
    third_party = thread.third_party_text is not None
    if cfg.naive_interpolation:
        untrusted.append(Untrusted(origin, Channel.INTERPOLATED, third_party))
    elif cfg.runner in (Runner.SANDCASTLE, Runner.SANDCASTLE_PI):
        untrusted.append(Untrusted(origin, Channel.PROMPT_ARG, third_party))
    else:
        untrusted.append(Untrusted(origin, Channel.TOOL_FETCHED, third_party))
    if thread.is_pr and thread.from_fork:
        untrusted.append(
            Untrusted(f"#{thread.number}'s diff, from a fork", Channel.TOOL_FETCHED, True)
        )

    # What is checked out, and what is in the environment while it runs.
    if thread.is_pr and thread.from_fork:
        checkout = "head (fork, untrusted)" if cfg.pr_target else "base (fork head unread)"
    else:
        checkout = "head"

    secrets: tuple[str, ...] = ("CLAUDE_CODE_OAUTH_TOKEN", "GITHUB_TOKEN")
    if cfg.identity is Identity.APP:
        secrets = ("CLAUDE_CODE_OAUTH_TOKEN", "APP_PRIVATE_KEY")
    scope = ("contents:write", "pull-requests:write", "issues:write")

    # Plain `pull_request` on a fork: read-only token, no secrets, and no way
    # for the run to say anything when it is done.
    if thread.from_fork and not cfg.pr_target:
        secrets = ()
        scope = ("contents:read",)

    return Job(
        skill=skill,
        runner=cfg.runner,
        checkout=checkout,
        secrets=secrets,
        untrusted=tuple(untrusted),
        author=author,
        author_is_machine=machine,
        write_scope=scope,
        cost=cost,
        concurrency_group=f"agent-mutate-{thread.number}",
        persistent_host=cfg.runner is Runner.SANDCASTLE_PI,
    )


# ---------------------------------------------------------------- the hazards


def findings(world: World, job: Job) -> list[Finding]:
    """What is wrong with a run that was authorised anyway.

    Deliberately not consulted by `dispatch()`. Authorisation and safety are
    different questions and the design should be able to say a run is legitimate
    and dangerous in the same breath.
    """
    cfg = world.config
    out: list[Finding] = []

    if "fork, untrusted" in job.checkout and job.secrets:
        out.append(
            Finding(
                Severity.CRITICAL,
                "pull_request_target checks out fork code with secrets in env",
                "The label gate authorised the *maintainer*. It said nothing about "
                f"the code. Install/build steps run before the agent does, and "
                f"{', '.join(job.secrets)} are readable from any of them.",
            )
        )

    if "fork head unread" in job.checkout:
        out.append(
            Finding(
                Severity.MEDIUM,
                "the run is safe and mute",
                "A plain `pull_request` on a fork gets a read-only token and no "
                "secrets — so the agent cannot post its own result. Reporting needs "
                "a second, privileged `workflow_run` job, which is where the "
                "privilege comes back. Safety here is a choice about where the "
                "trust boundary sits, not a way to avoid having one.",
            )
        )

    if job.persistent_host and "fork, untrusted" in job.checkout:
        out.append(
            Finding(
                Severity.CRITICAL,
                "untrusted code on a non-ephemeral self-hosted runner",
                "A GitHub-hosted runner is destroyed after the job. The Pi is a "
                "machine in the house that also holds the Transcript Archive "
                "backup. Compromise persists across runs.",
            )
        )

    for u in job.untrusted:
        if u.channel is Channel.INTERPOLATED:
            out.append(
                Finding(
                    Severity.CRITICAL,
                    f"{u.origin} is interpolated into the workflow",
                    "The text is shell on the runner before it is ever a prompt. "
                    "No agent behaviour is involved and no model refusal helps.",
                )
            )
        else:
            out.append(
                Finding(
                    Severity.HIGH if u.third_party else Severity.MEDIUM,
                    f"{u.origin} reaches the agent as prompt text ({u.channel.value})",
                    "It cannot execute, but the agent holds "
                    f"{', '.join(job.write_scope)} and may still be talked into "
                    "using them. "
                    + (
                        "Nobody with a write bit put this text there: a stranger "
                        "plants it, a maintainer starts the run, and the gate that "
                        "checks who pressed the button never looks at what it reads."
                        if u.third_party
                        else "Irreducible while agents read issues; the fix is that "
                        "what it writes is reviewable, not that it is obedient."
                    ),
                )
            )

    if not job.author_is_machine:
        out.append(
            Finding(
                Severity.HIGH,
                "commits will carry the researcher's name",
                "PROTOCOL §5's check `git log --format='%an'` returns one name "
                "regardless of who wrote the text. This is #23, unfixed.",
            )
        )
    elif cfg.identity is Identity.GIT_CONFIG_BOT:
        out.append(
            Finding(
                Severity.MEDIUM,
                "the bot name is a git config value, not an identity",
                "`git config user.name mosaic-agent[bot]` makes %an true and is "
                "unverifiable — any workflow, and any human, can set the same "
                "string. The push is still GITHUB_TOKEN. An App makes it checkable.",
            )
        )

    if cfg.trigger is Trigger.COMMENT:
        if cfg.allow_machine_dispatch:
            out.append(
                Finding(
                    Severity.HIGH,
                    "report and command are the same channel",
                    "An agent that says what it did and an agent that asks for the "
                    "next run both post a comment. Any rule strong enough to stop "
                    "the loop stops the handoff too. Under an App identity the "
                    "platform's own guard is gone as well — it keys on the "
                    "`github-actions` actor, which is the thing an App is not.",
                )
            )
        else:
            out.append(
                Finding(
                    Severity.MEDIUM,
                    "no handoff — every stage is hand-started",
                    "The loop is closed by refusing machine dispatch, which also "
                    "refuses research→review. A human is back in the middle of "
                    "the pipeline built to take the human out of the middle.",
                )
            )
    elif cfg.allow_machine_dispatch:
        out.append(
            Finding(
                Severity.MEDIUM,
                "machine handoff is on; the cap is the only thing stopping it",
                "Under labels a report cannot command — but review→revise→review "
                f"still runs until depth {world.max_depth}. The cap is load-bearing "
                "and belongs in the workflow, not in a comment about the workflow.",
            )
        )

    return out


# ------------------------------------------------------------------ the world


def apply(world: World, ev: Event, dec: Decision) -> World:
    """Fold a decision back in. Mutates the world in place and returns it."""
    world.ledger.append((ev, dec))
    thread = world.threads.get(ev.target)

    # Text from someone with no write bit stays in the thread whether or not it
    # dispatched anything — and the thread is what the next agent reads.
    if (
        thread is not None
        and ev.kind == "comment"
        and not ev.is_bot
        and ev.association not in WRITE_ASSOCIATIONS
    ):
        thread.third_party_text = ev.actor

    if dec.verdict is not Verdict.DISPATCH or thread is None:
        if dec.verdict is Verdict.REFUSE and thread is not None:
            thread.labels.add(BLOCKED)
        return world

    thread.labels -= set(dec.remove_labels)
    thread.labels |= set(dec.add_labels)
    if dec.job:
        world.running.add(dec.job.concurrency_group)
        world.day_spend += dec.job.cost
        world.depth = world.depth + 1 if ev.is_bot else 0
    return world


def finish(world: World, thread_no: int, job: Job) -> list[Event]:
    """A run ends: labels come off, it says what it did, and it asks for the next.

    Returns the events reporting *raises*. Feeding these back into `dispatch()`
    is the whole loop question, and the reason this returns them rather than
    swallowing them. Note that there are two of them, and that under
    `Trigger.LABEL` they arrive on two different channels.
    """
    cfg = world.config
    thread = world.threads[thread_no]
    thread.labels.discard(IN_PROGRESS)
    world.running.discard(job.concurrency_group)

    raised = [
        Event(
            kind="comment",
            actor=job.author,
            association="BOT",
            target=thread_no,
            body=f"`{job.skill}` complete on #{thread_no}. Wrote the document, "
            f"opened a PR, and logged the run.",
            machine=True,
        )
    ]

    nxt = HANDOFF.get(job.skill)
    if nxt and cfg.chain_handoff:
        if cfg.trigger is Trigger.COMMENT:
            raised.append(
                Event(
                    kind="comment",
                    actor=job.author,
                    association="BOT",
                    target=thread_no,
                    body=f"{DISPATCHABLE[nxt][1]} — handing off from {job.skill}.",
                    machine=True,
                )
            )
        else:
            raised.append(
                Event(
                    kind="label",
                    actor=job.author,
                    association="BOT",
                    target=thread_no,
                    label=DISPATCHABLE[nxt][0],
                    machine=True,
                )
            )
    return raised


def seed() -> World:
    """A small world resembling the real tracker."""
    return World(
        threads={
            26: Thread(26, "Settle the research-output document contract"),
            51: Thread(51, "Land the #4 survey", is_pr=True),
            60: Thread(
                60,
                "Drive-by fix from a stranger",
                is_pr=True,
                from_fork=True,
                third_party_text="drive-by",
            ),
            12: Thread(12, "Assemble the founding charter", open=False),
        }
    )
