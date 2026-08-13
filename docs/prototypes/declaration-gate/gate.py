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
    "NO_PREDECESSOR": "siblings",
    "HOLDOUT_SALT_REUSED": "siblings",
    "DECLARATION_AMENDED": "siblings",
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
    "NO_PREDECESSOR": (
        "A declaration in a non-empty `runs/` names no predecessor, or names one that is "
        "not the most recent declaration in the Inquiry, or names one that has not closed. "
        "#182: the declaring party commits to being the *n*th attempt in advance, exactly "
        "as #63's declaration commits to the set in advance. A line, never a tree."
    ),
    "HOLDOUT_SALT_REUSED": (
        "A successor declaration reuses its predecessor's byte-identical hold-out salt. "
        "#182 refuses this outright: the successor's data had already been read before the "
        "declaration meant to judge it existed. Not a sequence defect — a hold-out defect, "
        "and unlike a seed a hold-out cannot be redrawn."
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


@dataclass
class Verdict:
    # (name, why, which condition tripped — see NO_PREDECESSOR below)
    refusals: list[tuple[str, str, str]] = field(default_factory=list)
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
#     {"set_id", "closed": bool, "salt": str | None}
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
            refuse("NO_PREDECESSOR", f"no `follows:` field; runs/ already holds {len(siblings)}")
        elif follows != most_recent["set_id"]:
            refuse("NO_PREDECESSOR",
                   f"follows `{follows}`; the most recent is `{most_recent['set_id']}`")
        elif not most_recent["closed"]:
            refuse("NO_PREDECESSOR",
                   f"`{most_recent['set_id']}` has not closed — a line, never a tree")

        salt = ((dataset or {}).get("split") or {}).get("salt")
        if salt is not None and any(s.get("salt") == salt for s in siblings):
            refuse("HOLDOUT_SALT_REUSED")
    elif decl.get("follows"):
        v.notes.append(
            "`follows:` names a predecessor in an empty runs/. Harmless, and not a "
            "refusal anyone has ruled — noted so the driver does not have to guess."
        )

    return v


def render(v: Verdict, subject: str) -> str:
    lines = []
    if not v.refusals:
        lines.append(f"  ACCEPTED — {subject} may be committed.")
        lines.append(
            "  The gate says nothing about the register. It will derive to confirmatory "
            "or exploratory\n  at set close, from runs that do not exist yet."
        )
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
    for note in v.notes:
        lines.append("  note: " + note)
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
    lines.append(f"  {movable} of {len(READS)} findings move. #181 named five of them.")
    return "\n".join(lines)
