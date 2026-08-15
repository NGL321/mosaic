"""PROTOTYPE — the declaration gate: refusing a malformed run-set declaration where it
is committed, rather than where its register is read.

Ticket #181. Throwaway. Nothing depends on this and nothing runs it in CI.

The question: *does the run-set declaration want a gate of its own?* #60's dispatch gate
refuses a malformed charter before Searching begins; #64's publish gate refuses a
malformed manifest before a run enters the record. The declaration #63 introduced has no
gate: a malformed one is discovered when the register comes out as **exit 2**, by which
point the whole set has been run and its budget spent.

**The gate introduces no refusal of its own, and that is the finding.** Every name below
is already a refusal in #63's `register.py` or #182's ruling. What this file does is
partition those findings by *what they read*, and fire the ones that read only text
already committed at the declaring commit. So the third-gate question is not answered by
symmetry with #60 and #64 — it is answered by a partition anyone can recompute:

    a finding whose inputs are all present at the declaring commit
    can fire at the declaring commit.

Two consequences fall out of the partition rather than out of anyone's judgement:

- **A downgrade may never move.** `exploratory` is a first-class outcome (premise 3), so
  a check that refused a declaration destined to derive `exploratory` would forbid work
  the programme permits. The gate is a subset of the REFUSALS and never touches the
  DOWNGRADES. `NO_HOLDOUT` is the case that shows the line falls somewhere non-obvious.
- **The partition finds defects the ticket did not list.** #181 named five. The criterion
  yields seven: `DECLARATION_AMENDED`, which the natural path trigger hands over free,
  and `HOLDOUT_SALT_REUSED`, which #182 ruled a refusal without noticing it reads nothing
  but two committed files.

Run the driver, not this file:

    python docs/prototypes/declaration-gate/prototype_tui.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# What the gate fires on.
#
# A path, not a workflow event — #60's shape rather than #64's. The declaration appears
# in `inquiries/NNN-slug/runs/`, and the appearance IS the second freeze event, exactly
# as `config.yaml`'s appearance is the first.
#
# `mode` matters as much as the path. #60's gate had to reconstruct POST_OPEN_AMENDMENT
# out of git history because the charter is edited legitimately before it opens. A
# declaration is never edited at all, so `modify` on this path is a refusal with no case
# analysis behind it — the cheapest check in the whole loop, and one only a commit-time
# gate is positioned to make.
# --------------------------------------------------------------------------

TRIGGER = re.compile(r"^inquiries/(\d+)-[a-z0-9-]+/runs/[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9]+\.declared\.yaml$")


# --------------------------------------------------------------------------
# The partition. This is the argument, written as data.
#
# Each of #63's and #182's findings, tagged with what it has to read. The gate fires
# exactly those tagged `declaration` or `siblings` — both are committed text present in
# the tree at the moment the declaration lands.
# --------------------------------------------------------------------------

READS = {
    # ---- refusals that read the declaration alone -------------------------
    "DECLARATION_ASSERTS_REGISTER": "declaration",
    "SEEDS_NOT_DERIVABLE": "declaration",
    "NO_ATTRITION_POLICY": "declaration",
    "DATASET_UNPINNED": "declaration",
    # ---- refusals that read the declaration and its siblings in runs/ -----
    #
    # #182's NO_PREDECESSOR is SPLIT INTO THREE, on Noah's ruling that naming is cheap and
    # an intuitive name heads off the case analysis a single name pushes onto whoever
    # reads the refusal. Driving the gate is what showed the three were unlike: a missing
    # line, a wrong line, and a declaration that is not defective at all but early.
    "NO_PREDECESSOR_NAMED": "siblings",
    "PREDECESSOR_NOT_MOST_RECENT": "siblings",
    "PREDECESSOR_NOT_CLOSED": "siblings",
    "HOLDOUT_SALT_REUSED": "siblings",
    "DECLARATION_AMENDED": "siblings",
    # ---- the withdrawal, and the two ways it is misused --------------------
    "WITHDRAWAL_AFTER_RUN": "siblings",
    "WITHDRAWAL_UNMATCHED": "siblings",
    # ---- refusals that cannot fire until runs exist ------------------------
    "SET_UNDECLARED": "manifests",
    # ---- downgrades: the register DERIVES, to exploratory. Never movable, --
    #      whatever they read, because refusing them would forbid legitimate work.
    "CHARTER_NOT_ANCESTOR": "downgrade",
    "FREEZE_NOT_ANCESTOR": "downgrade",
    "DECLARATION_NOT_ANCESTOR": "downgrade",
    "DISPATCH_NOT_FROM_DECLARATION": "downgrade",
    "DISPATCH_UNATTESTED": "downgrade",
    "SET_INCOMPLETE": "downgrade",
    "UNDECLARED_RUN": "downgrade",
    "ATTRITION_EXCEEDED": "downgrade",
    "ATTRITION_UNATTESTED": "downgrade",
    "NULL_REPORTED_AS_ATTRITION": "downgrade",
    "NO_HOLDOUT": "downgrade",
    "SPLIT_NOT_DERIVABLE": "downgrade",
    "HOLDOUT_TOUCHED": "downgrade",
}

MOVABLE = ("declaration", "siblings")


# --------------------------------------------------------------------------
# Refusals. Each is a named, emittable finding — never a bare exit code. The wording is
# #63's and #182's; nothing is restated in this file's own voice, because a second copy
# of a refusal is a second thing that can drift.
# --------------------------------------------------------------------------

REFUSALS = {
    "DECLARATION_ASSERTS_REGISTER": (
        "The declaration carries a `register:` field. #56 derives Register from ancestry "
        "and never accepts it declared; #60 refuses the same field on the charter. A "
        "declared register is a register an argument can move."
    ),
    "SEEDS_NOT_DERIVABLE": (
        "The declaration lists seeds literally instead of deriving them from a master "
        "seed and a rule. A literal list is honest for the runs it names and says nothing "
        "about a replacement, so the attrition policy has no arithmetic to fall back on."
    ),
    "NO_ATTRITION_POLICY": (
        "The declaration states no attrition policy. A set with no declared response to a "
        "failed run improvises one after the failure, which is a judgement made with the "
        "data in view."
    ),
    "DATASET_UNPINNED": (
        "The declaration names a pre-existing dataset with no checksum. Unpinned, it is a "
        "tag rather than a digest — one layer up from #64's BASE_BY_TAG — and the bytes "
        "the hold-out was computed over can be repointed underneath the result."
    ),
    "NO_PREDECESSOR_NAMED": (
        "A declaration in a non-empty `runs/` carries no `follows:` field. #182: the "
        "declaring party commits to being the *n*th attempt in advance, exactly as #63's "
        "declaration commits to the set in advance. Add the field naming the most recent "
        "declaration in this Inquiry."
    ),
    "PREDECESSOR_NOT_MOST_RECENT": (
        "`follows:` names a declaration that is not the most recent in this Inquiry. #182: "
        "a line, never a tree — a branch point lets sets be declared in parallel, which is "
        "#63's leak exactly, since everything declared in advance and one thing reported "
        "stops meaning anything."
    ),
    "PREDECESSOR_NOT_CLOSED": (
        "The predecessor named has not closed. NOTHING IS WRONG WITH THIS DECLARATION — it "
        "is early, and waiting fixes it. The exception is a predecessor that can never "
        "close because it has no Runs at all; see WITHDRAWAL below, which is the exit."
    ),
    "HOLDOUT_SALT_REUSED": (
        "A successor declaration reuses its predecessor's byte-identical hold-out salt. "
        "#182 refuses this outright: the successor's data had already been read before the "
        "declaration meant to judge it existed. Not a sequence defect — a hold-out defect, "
        "and unlike a seed a hold-out cannot be redrawn."
    ),
    "WITHDRAWAL_AFTER_RUN": (
        "A withdrawal names a set that has already recorded an account — a result or an "
        "attested non-completion. A set that has run closes the ordinary way, through its "
        "own accounts. Withdrawal is the exit for a set that never dispatched, and letting "
        "it reach a set that did would make it an undo on a measurement in progress."
    ),
    "WITHDRAWAL_UNMATCHED": (
        "A withdrawal names no declaration in this Inquiry's `runs/`. It is a link in the "
        "Run-Set Sequence and a link needs both ends."
    ),
    "DECLARATION_AMENDED": (
        "An existing declaration was modified. The declaration is a commitment, and a "
        "commitment that can be edited after the runs is the seed sequence chosen with the "
        "data in view — the whole mechanism, reversed by a text editor. #60's "
        "POST_OPEN_AMENDMENT, one level down, and cheaper: a charter is legitimately "
        "edited before it opens, so #60 needs history to tell the cases apart, while a "
        "declaration is never edited at all and `modify` on this path settles it."
    ),
}


# A hazard is not a refusal. #9: an untestable hazard is declared and attaches permanently
# to every leg the Inquiry earns. #64 and #63 both established the gate appending one
# itself, so it cannot be omitted by the party with a motive to omit it.
HAZARDS = {
    "withdrawn_unrun": (
        "A declared set in this Inquiry was withdrawn with no account recorded against it. "
        "This is `cancellation_peek` one level up: logs stream, so a party can read a "
        "number and then record nothing at all — the whole set abandoned rather than one "
        "run cancelled. The hazard attaches to EVERY withdrawal and asks no questions, "
        "because the alternative is exempting a set on a claim that nothing ran, and a "
        "claim of absence is exactly what #63 established cannot be verified. Marked "
        "rather than prevented; countable, because every withdrawal is a committed link."
    ),
}


@dataclass
class Verdict:
    # (name, why, which condition tripped)
    refusals: list[tuple[str, str, str]] = field(default_factory=list)
    hazards: list[tuple[str, str]] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def exit_code(self) -> int:
        # 0 clean, 2 refused. NEVER 1.
        #
        # The gate's refusal is #63's exit 2 arriving early — the same condition, found by
        # the same predicate over the same text — so it carries the same code. Exit 1 in
        # the register check means `exploratory`, which is not an error and is not the
        # gate's to pronounce: no run has produced a number yet, and the declaration in
        # front of it may be a perfectly good exploratory one.
        return 2 if self.refusals else 0


# --------------------------------------------------------------------------
# The check. A pure function of the declaration text and the sibling declarations already
# in `runs/` — no git history, no manifests, no network, no runner.
#
# `siblings` is the directory listing at the parent commit, in commit order, each entry:
#     {"set_id", "closed": bool, "salt": str | None, "accounts": int, "withdrawn": bool}
# All of it is committed text; `closed` is derivable from the predecessor's own manifests
# and attestations (#182 ruling 2), and is passed in resolved here to keep the prototype
# free of a manifest reader it does not need.
# --------------------------------------------------------------------------

def check_declaration(decl: dict, siblings: list[dict], mode: str = "add") -> Verdict:
    v = Verdict()

    def refuse(name: str, condition: str = "") -> None:
        v.refusals.append((name, REFUSALS[name], condition))

    if mode == "modify":
        # Nothing else is worth saying about this commit. The content may be immaculate.
        refuse("DECLARATION_AMENDED")
        return v

    # ---- reads the declaration alone --------------------------------------
    if "register" in decl:
        refuse("DECLARATION_ASSERTS_REGISTER")

    draw = decl.get("draw") or {}
    if "seeds" in draw or not draw.get("rule") or not draw.get("master_seed"):
        refuse("SEEDS_NOT_DERIVABLE")

    attrition = decl.get("attrition") or {}
    if not attrition.get("policy"):
        refuse("NO_ATTRITION_POLICY")

    dataset = decl.get("dataset")
    if dataset is not None and not dataset.get("checksum"):
        refuse("DATASET_UNPINNED")

    # ---- reads the declaration and its siblings ---------------------------
    if siblings:
        # THREE CONDITIONS UNDER ONE NAME, and driving this is what showed it. #182 minted
        # NO_PREDECESSOR for the absent field, the wrong predecessor and the open one, and
        # the three are not fixed the same way: one is a missing line, one is a wrong line,
        # and the third is not a defect in the declaration at all — it is a declaration
        # arriving too early, which is fixed by waiting rather than by editing. A party
        # reading the bare name has to guess which, so the gate emits the condition.
        follows = decl.get("follows")
        most_recent = siblings[-1]
        if follows is None:
            refuse("NO_PREDECESSOR_NAMED", f"runs/ already holds {len(siblings)}")
        elif follows != most_recent["set_id"]:
            refuse("PREDECESSOR_NOT_MOST_RECENT",
                   f"follows `{follows}`; the most recent is `{most_recent['set_id']}`")
        elif not most_recent["closed"]:
            hint = " — it has no accounts and cannot close; withdraw it" \
                if not most_recent.get("accounts") else ""
            refuse("PREDECESSOR_NOT_CLOSED", f"`{most_recent['set_id']}` is still open{hint}")

        if any(s.get("withdrawn") for s in siblings):
            v.hazards.append(("withdrawn_unrun", HAZARDS["withdrawn_unrun"]))

        salt = ((dataset or {}).get("split") or {}).get("salt")
        if salt is not None and any(s.get("salt") == salt for s in siblings):
            refuse("HOLDOUT_SALT_REUSED")
    elif decl.get("follows"):
        v.notes.append(
            "`follows:` names a predecessor in an empty runs/. Harmless, and not a "
            "refusal anyone has ruled — noted so the driver does not have to guess."
        )

    return v


# --------------------------------------------------------------------------
# The withdrawal — the exit for a declared set that never dispatched.
#
# #182 requires a declaration's predecessor to have CLOSED, and nothing closes a set with
# no Runs: the honest account is SET_INCOMPLETE, a downgrade over manifests that will never
# exist. Without an exit the Inquiry's runs/ is a dead end.
#
# THREE THINGS IT IS NOT, and each one is a rule already on the books:
#
#   - not an edit to the declaration      (a declaration is never edited once committed)
#   - not a deletion                      (that erases the Run-Set Sequence #182 exists to
#                                          record — absence is not a record)
#   - not a waiver                        (Noah's ruling on this ticket, and inert anyway:
#                                          the register still refuses at close)
#
# So it is a NEW COMMITTED FILE beside the declaration, and a LINK IN THE SEQUENCE rather
# than an escape from it. #182 already defines link shapes and already attaches a hazard to
# a search-shaped one; a withdrawal is the fourth shape and needs no new machinery.
#
# It carries no `reason:`, on #182's ruling that prose is an argument's front door.
# --------------------------------------------------------------------------

def check_withdrawal(withdrawal: dict, siblings: list[dict]) -> Verdict:
    v = Verdict()

    def refuse(name: str, condition: str = "") -> None:
        v.refusals.append((name, REFUSALS[name], condition))

    target = withdrawal.get("withdraws")
    match = next((s for s in siblings if s["set_id"] == target), None)

    if match is None:
        refuse("WITHDRAWAL_UNMATCHED", f"no declaration `{target}` in runs/")
        return v

    if match.get("accounts"):
        refuse("WITHDRAWAL_AFTER_RUN",
               f"`{target}` has {match['accounts']} account(s) recorded")
        return v

    # Accepted. The set closes, the successor is admitted, and the hazard travels.
    v.hazards.append(("withdrawn_unrun", HAZARDS["withdrawn_unrun"]))
    v.notes.append(
        f"`{target}` closes as WITHDRAWN. It stays in the Run-Set Sequence permanently as "
        "a link of that shape, so the next declaration follows it rather than replacing it."
    )
    return v


def render(v: Verdict, subject: str) -> str:
    lines = []
    if not v.refusals:
        lines.append(f"  ACCEPTED — {subject} may be committed.")
        if not v.hazards:
            lines.append(
                "  The gate says nothing about the register. It will derive to confirmatory "
                "or exploratory\n  at set close, from runs that do not exist yet."
            )
        lines.append("")
    else:
        lines.append(f"  REFUSED — {subject} does not enter the tree.")
        lines.append("")
        for name, why, condition in v.refusals:
            lines.append(f"  {name}  [reads: {READS[name]}]")
            if condition:
                lines.append(f"      -> {condition}")
            for chunk in _wrap(why):
                lines.append(f"      {chunk}")
            lines.append("")
    for name, why in v.hazards:
        lines.append(f"  HAZARD  {name}   [attached by the gate, not declared by anyone]")
        for chunk in _wrap(why):
            lines.append(f"      {chunk}")
        lines.append("")
    for note in v.notes:
        for chunk in _wrap("note: " + note):
            lines.append("  " + chunk)
    return "\n".join(lines)


def _wrap(text: str, width: int = 68) -> list[str]:
    out, line = [], ""
    for word in text.split():
        if len(line) + len(word) + 1 > width:
            out.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        out.append(line)
    return out


def partition_table() -> str:
    """The third-gate argument, printed. Derived from READS, not asserted."""
    buckets: dict[str, list[str]] = {}
    for name, reads in READS.items():
        buckets.setdefault(reads, []).append(name)
    lines = [
        "  Every finding #63 and #182 defined, by what it reads:",
        "",
    ]
    for reads in ("declaration", "siblings", "manifests", "downgrade"):
        verdict = "FIRES AT THE DECLARING COMMIT" if reads in MOVABLE else "cannot move"
        if reads == "downgrade":
            verdict = "must not move — exploratory is a legitimate outcome"
        lines.append(f"  {reads:<14} {verdict}")
        for name in buckets.get(reads, []):
            lines.append(f"                   {name}")
        lines.append("")
    movable = sum(len(buckets.get(r, [])) for r in MOVABLE)
    lines.append(
        f"  {movable} of {len(READS)} fire at the declaring commit. Counted as #63 and #182"
    )
    lines.append(
        "  left them — before NO_PREDECESSOR split three ways and before the withdrawal —"
    )
    lines.append("  seven of twenty-one move, and #181 named five of those.")
    return "\n".join(lines)
