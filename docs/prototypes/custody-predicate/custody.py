"""
PROTOTYPE (ticket #23) — the portable bit.

QUESTION BEING PROTOTYPED
-------------------------
PROTOCOL.md §5 claims custody of authored files (CONTEXT.md, the charter) is
"human only", and offers `git log --format='%an' -- CONTEXT.md → one name` as its
mechanical check. That command does not work today, and #24 will make it *work*
without deciding *what it should say*. The ticket's three readings:

  A  TYPED       the human typed the text; an agent co-author trailer on an
                 authored file is a violation.
  B  AMANUENSIS  the human authored it with an agent as amanuensis; the trailer
                 is expected, and the violation is an *unattended* session.
  C  ENDORSED    the human understood and endorsed it; custody collapses into
                 warrant and the file-level rule is dropped.

  D  AMANUENSIS + WARRANT   the workshopped fourth, drafted after driving A–C.

D exists because A and B share a failure the ticket did not name: **a human can
type every character and still only be reciting.** Attendance and typing are both
proxies for a thing neither of them checks. So D keeps custody answering the only
question custody can answer — *whose hand* — and hands *whose understanding* back
to warrant, at file scope rather than commit-type scope:

  1. IDENTITY (kept from A) — an authored file is committed under a human
     identity. One git command, adversarially meaningful, survives #24.
  2. CITATION (kept from B) — an agent co-author on an authored file obliges a
     `Session:` trailer resolving in the Transcript Archive. The trailer stops
     being a verdict and becomes a *routing signal*: it triggers obligations
     rather than convicting the commit.
  3. DEFENCE (borrowed from C, rescoped) — a meaning-changing commit to an
     authored file obliges a defence artifact, agent trailer or not. §6's de
     minimis exception carries over unchanged.

TERMINATION
-----------
"Defend" is unbounded until the repository says where defence bottoms out. FLOOR
below models that: with no declared competence floor, D's defence obligation is
UNDECIDABLE rather than satisfied — the deficiency reports itself instead of
being papered over. This is the root baseline assertion the programme lacks, and
it is the thing Verification Debt has always presupposed without stating.

Drive it by hand with prototype_tui.py.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum

# The competence floor: a declared statement of what Noah can defend unaided,
# below which a derivation's dependencies are Verification Debt rather than a
# custody failure. Toggle it in the TUI to see what D is worth without one.
FLOOR = {"declared": False}


class FileClass(Enum):
    """§5's custody categories. Custody follows the file, never the topic."""

    AUTHORED = "AUTHORED"  # CONTEXT.md, the charter
    RECORD = "RECORD"  # research docs, notebook, ledger, experiment output
    TOOLING = "TOOLING"  # PROTOCOL.md, README.md, CI, config


class Identity(Enum):
    """Who the commit's author field actually identifies."""

    HUMAN = "HUMAN"  # post-#24: a human identity means a human
    AGENT_BOT = "AGENT_BOT"  # post-#24: agents commit under a bot identity
    HUMAN_UNVERIFIED = "HUMAN_UNVERIFIED"  # today: agent worktrees inherit NGL321


class Session(Enum):
    """Whether a human was present when the commit was made."""

    ATTENDED = "ATTENDED"
    UNATTENDED = "UNATTENDED"
    UNKNOWN = "UNKNOWN"  # today's state: git carries no attendance signal


class Endorsement(Enum):
    """Whether a §5-warrant-style artifact accompanies the commit."""

    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    UNKNOWN = "UNKNOWN"


class Defence(Enum):
    """What the human produced about the diff, and how it fared under grilling.
    CI can check presence; only the checker agent separates the middle two."""

    DEFENDED = "DEFENDED"  # survived grilling, down to the floor
    RECITED = "RECITED"  # words on the page, hollow under grilling
    ABSENT = "ABSENT"
    UNKNOWN = "UNKNOWN"


class Verdict(Enum):
    PASS = "PASS"
    VIOLATION = "VIOLATION"
    UNDECIDABLE = "UNDECIDABLE"  # the policy needs a fact the record lacks
    VACUOUS = "VACUOUS"  # the policy applies but demands nothing


@dataclass(frozen=True)
class Commit:
    subject: str
    ctype: str  # record | evidence | belt | core | feat | fix | chore
    file_class: FileClass
    identity: Identity
    agent_co_author: bool
    session: Session = Session.UNKNOWN
    endorsement: Endorsement = Endorsement.UNKNOWN
    defence: Defence = Defence.UNKNOWN
    session_cited: bool = False  # a Session: trailer that resolves in the archive
    de_minimis: bool = False  # §6: cannot alter meaning
    # --- ground truth: what actually happened, as against what the record says.
    # No checker can read these. They exist so a policy's verdict can be scored
    # against reality, which is how ceremony-satisfiability becomes visible.
    truly_attended: bool = True
    truly_defensible: bool = True
    sha: str | None = None  # set when the case came from real history

    def with_(self, **kw) -> Commit:
        return replace(self, **kw)

    @property
    def legitimate(self) -> bool:
        """What a truthful custody rule ought to conclude. Both conjuncts are
        load-bearing: dropping the second is what makes A and B ceremony."""
        return self.truly_attended and self.truly_defensible


@dataclass(frozen=True)
class Ruling:
    verdict: Verdict
    reason: str


# --------------------------------------------------------------------------
# A — TYPED
# --------------------------------------------------------------------------

def typed(c: Commit) -> Ruling:
    if c.file_class is not FileClass.AUTHORED:
        return Ruling(Verdict.VACUOUS, "custody's file rule bites only on authored files")
    if c.identity is Identity.AGENT_BOT:
        return Ruling(Verdict.VIOLATION, "an agent identity committed an authored file")
    if c.agent_co_author:
        return Ruling(Verdict.VIOLATION, "agent co-author trailer on an authored file")
    if c.identity is Identity.HUMAN_UNVERIFIED:
        return Ruling(
            Verdict.UNDECIDABLE,
            "human name, but agent sessions inherit it — nothing distinguishes them (pre-#24)",
        )
    return Ruling(Verdict.PASS, "human identity, no agent trailer")


# --------------------------------------------------------------------------
# B — AMANUENSIS
# --------------------------------------------------------------------------

def amanuensis(c: Commit) -> Ruling:
    if c.file_class is not FileClass.AUTHORED:
        return Ruling(Verdict.VACUOUS, "custody's file rule bites only on authored files")
    if c.identity is Identity.AGENT_BOT:
        return Ruling(Verdict.VIOLATION, "an agent identity committed an authored file")
    if c.session is Session.UNATTENDED:
        return Ruling(Verdict.VIOLATION, "an unattended session committed an authored file")
    if c.session is Session.UNKNOWN:
        return Ruling(
            Verdict.UNDECIDABLE,
            "attendance is the whole claim, and git carries no attendance signal",
        )
    if c.identity is Identity.HUMAN_UNVERIFIED:
        return Ruling(Verdict.UNDECIDABLE, "committing identity not distinguishable (pre-#24)")
    return Ruling(Verdict.PASS, "attended session under a human identity; trailer expected")


# --------------------------------------------------------------------------
# C — ENDORSED
# --------------------------------------------------------------------------

def endorsed(c: Commit) -> Ruling:
    if c.ctype.rstrip(":") not in {"belt", "core"}:
        return Ruling(
            Verdict.VACUOUS,
            f"{c.ctype} demands nothing of the human under the warrant table",
        )
    if c.endorsement is Endorsement.ABSENT:
        return Ruling(Verdict.VIOLATION, "no falsifier / work product accompanies the claim")
    if c.endorsement is Endorsement.UNKNOWN:
        return Ruling(Verdict.UNDECIDABLE, "the artifact lives on a pull request, not the commit")
    return Ruling(Verdict.PASS, "warrant artifact present")


# --------------------------------------------------------------------------
# D — AMANUENSIS + WARRANT  (the workshopped candidate)
# --------------------------------------------------------------------------

def amanuensis_warranted(c: Commit) -> Ruling:
    if c.file_class is not FileClass.AUTHORED:
        return Ruling(Verdict.VACUOUS, "custody's file rule bites only on authored files")

    # 1. identity — the one obligation a stranger checks in a single command.
    if c.identity is Identity.AGENT_BOT:
        return Ruling(Verdict.VIOLATION, "an authored file must be committed by the human")
    if c.identity is Identity.HUMAN_UNVERIFIED:
        return Ruling(Verdict.UNDECIDABLE, "committing identity not distinguishable (pre-#24)")

    # §6's de minimis exception, unchanged: it cannot alter meaning, so it owes
    # nothing further. This is why the defence obligation is affordable.
    if c.de_minimis:
        return Ruling(Verdict.PASS, "§6 de minimis — cannot alter meaning, owes nothing further")

    # 2. citation — the trailer routes rather than convicts.
    if c.agent_co_author and not c.session_cited:
        return Ruling(
            Verdict.VIOLATION,
            "agent co-author with no resolving Session: trailer — influence untraceable",
        )

    # 3. defence — and it must have somewhere to bottom out.
    if not FLOOR["declared"]:
        return Ruling(
            Verdict.UNDECIDABLE,
            "'defend' has no terminus until the repo declares a competence floor",
        )
    if c.defence is Defence.ABSENT:
        return Ruling(Verdict.VIOLATION, "meaning-changing edit to an authored file, no defence")
    if c.defence is Defence.RECITED:
        return Ruling(
            Verdict.VIOLATION,
            "recitation, not defence — the failure typed custody shares and cannot see",
        )
    if c.defence is Defence.UNKNOWN:
        return Ruling(Verdict.UNDECIDABLE, "no grilling has happened on this diff yet")
    return Ruling(
        Verdict.PASS,
        "human hand, session cited, defence survived grilling to the floor",
    )


POLICIES = (
    ("A", "typed", typed),
    ("B", "amanuensis", amanuensis),
    ("C", "endorsed", endorsed),
    ("D", "aman+warrant", amanuensis_warranted),
)


# What the sceptic §5 exists to answer can actually run.
STRANGER_CHECK = {
    "typed": "yes — one git command, once #24 gives agents their own identity",
    "amanuensis": "no — needs an attendance trailer that does not exist yet",
    "endorsed": "no — the artifact is on a PR thread, outside the history",
    "aman+warrant": "partly — CI checks identity and citation; the grilling is on the PR, as §5's gate already is",
}


def soundness(policy, c: Commit) -> tuple[str, str]:
    """Score a verdict against ground truth the checker cannot see."""
    v = policy(c).verdict
    if v in (Verdict.UNDECIDABLE, Verdict.VACUOUS):
        return "SILENT", "declines to rule — no protection either way"
    if v is Verdict.PASS and not c.legitimate:
        return "FOOLED", "passed a commit that should not have passed"
    if v is Verdict.VIOLATION and c.legitimate:
        return "OVERSTRICT", "convicted legitimate work"
    return "SOUND", "verdict tracks what actually happened"
