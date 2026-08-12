"""PROTOTYPE — the register check: confirmatory or exploratory, by ancestry.

Ticket #63. Throwaway. Nothing depends on this and nothing runs it in CI.

The question: *how is a result's register established mechanically, so that no argument
can move it?* The map bars exploratory results from the Protective Belt, and that
guarantee is only as good as the check behind it — which must be ancestry, not
persuasion, because the argument "this metric was obvious in advance, we just forgot to
write it down" will be made, by an agent, persuasively.

**The ticket's own rule does not hold, and finding that is the point of building this.**
It says the config SHA must be an ancestor of the commit recording the output sha256.
Ancestry orders *commits*. It does not order a commit against *the data*:

    1. run the training script against a candidate under configs/, read the number
    2. liking it, commit that candidate to config.yaml     <- the freeze
    3. commit the run manifest carrying the number from step 1

The freeze is a genuine ancestor of the manifest. Every ancestry check passes. The
result is exploratory, and the check calls it confirmatory. This is #26 R6's failure in
a new dress: not a rule satisfiable by writing a word, but one satisfiable by committing
in a convenient order.

Two things close it, both ruled on #63:

- **The run set is DECLARED before any of it produces a number** — because the leak that
  ancestry structurally cannot see is not the result, it is the siblings that were never
  committed. Twenty seeds run, one manifest published: every ancestry check passes, and
  the data chose the result.
- **The dispatch is witnessed** — the run was launched from the declaration commit, and
  the runner's record of what it checked out is written by the party outside, the same
  trust root #64 rests the environment block on. The attestation is COPIED into the
  manifest at publish, never referenced: GitHub expires logs, and a register derivable
  only until a retention window closes is not derivable.

**Nothing here is asserted and nothing here is stored.** The register is a pure function
of committed text — declaration, manifests, attestations — computed on demand and
rendered into the coverage report and the notebook entry, which are projections rather
than sources (#90's argument, applied one level down). There is no `register:` field
anywhere in `inquiries/`, and a declaration carrying one is refused outright.

Run the driver, not this file:

    python docs/prototypes/register-check/prototype_tui.py
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# Two kinds of finding, and the difference is the whole design.
#
# A REFUSAL means the register cannot be derived at all — the record is malformed, and
# the check must say so rather than fall through to a verdict. #53 is the precedent: a
# green run that could cover nothing is worse than a red one, so "no declaration present"
# is exit 2, never a quiet pass.
#
# A DOWNGRADE means the register derives, and derives to `exploratory`. This is not an
# error. Exploratory results are first-class in the record (premise 3) — they are barred
# from the Protective Belt, and their route in is to become the preregistered hypothesis
# of a new confirmatory Inquiry. The check is not stopping work. It is naming what kind
# of evidence the work produced.
# --------------------------------------------------------------------------

REFUSALS = {
    "SET_UNDECLARED": (
        "A manifest cites no run-set declaration. Under #63 the declaration is what makes "
        "the set of runs a commitment rather than a selection, so its absence is not a "
        "malformed field — there is nothing to derive a register from. The result is in "
        "the record; it simply has no register yet."
    ),
    "DECLARATION_ASSERTS_REGISTER": (
        "The declaration carries a `register:` field. #56 derives Register from ancestry "
        "and never accepts it declared; #60 refuses the same field on the charter. A "
        "declared register is a register an argument can move, which is the one thing "
        "this check exists to prevent."
    ),
    "SEEDS_NOT_DERIVABLE": (
        "The declaration lists seeds literally instead of deriving them from a master "
        "seed and a rule. A literal list is honest for the runs it names and says nothing "
        "about a replacement, so the attrition policy has no arithmetic to fall back on "
        "and 'the next seed' becomes whatever someone picks after seeing the last one."
    ),
    "NO_ATTRITION_POLICY": (
        "The declaration states no attrition policy. A set with no declared response to a "
        "failed run has to improvise one after the failure, which is a judgement made with "
        "the data in view. Declared in advance, attrition is arithmetic."
    ),
    "DATASET_UNPINNED": (
        "The declaration names a pre-existing dataset with no checksum. An unpinned "
        "dataset is a tag rather than a digest, one layer up from #64's BASE_BY_TAG: the "
        "bytes the hold-out was computed over can be repointed underneath the result."
    ),
}

DOWNGRADES = {
    # ---- ancestry ---------------------------------------------------------
    "CHARTER_NOT_ANCESTOR": (
        "The charter commit carrying the metric and the decision rule is not an ancestor "
        "of the declaration. The number was given its meaning after the set that would "
        "produce it was named — a metric fixed late is a metric fixed to fit."
    ),
    "FREEZE_NOT_ANCESTOR": (
        "The freeze commit — the appearance of config.yaml, per #60 — is not an ancestor "
        "of the declaration. Runs were declared against an instrument still being searched "
        "over, so the apparatus and the measurement were free at the same time."
    ),
    "DECLARATION_NOT_ANCESTOR": (
        "The declaration is not an ancestor of the commit recording this run's output. "
        "The set was named after the record it is supposed to have constrained."
    ),
    "DISPATCH_NOT_FROM_DECLARATION": (
        "The attested run checked out a commit that is not the declaration or a descendant "
        "of it. THIS IS THE REFUSAL THE TICKET'S OWN RULE COULD NOT MAKE: ancestry between "
        "commits is satisfiable by committing in a convenient order, and only the witness "
        "of what the runner actually checked out orders the commit against the data."
    ),
    "DISPATCH_UNATTESTED": (
        "The run carries no runner attestation, so nothing outside the agent's own writing "
        "says when the data came into existence relative to the declaration. #64 accepts a "
        "hand-entered environment block and marks it; the register is stricter, because "
        "here the attestation IS the ordering evidence rather than a description of it."
    ),

    # ---- the declared set -------------------------------------------------
    "SET_INCOMPLETE": (
        "A declared run is neither a result nor an attested non-completion. Absence is the "
        "leak declaring the set exists to expose: before #63 a run that produced nothing "
        "left no trace, so twenty runs and one published manifest was invisible. It is "
        "visible now, and an unaccounted run means the set did not constrain anything."
    ),
    "UNDECLARED_RUN": (
        "A manifest cites this set with a seed the declaration's draw rule never produces. "
        "The seed sequence is derivable from the master seed in a clone, so a seed outside "
        "it was chosen rather than drawn — which is the reroll the whole mechanism is "
        "aimed at."
    ),
    "ATTRITION_EXCEEDED": (
        "More runs were replaced than the declared attrition policy allows. Past the "
        "declared bound, replacement stops being arithmetic and becomes a search over "
        "seeds conducted after the data is in view."
    ),
    "ATTRITION_UNATTESTED": (
        "A run is accounted for as attrition with no runner attestation. Attrition is "
        "attested by the runner and never claimed by an agent: the workflow record — run "
        "id, conclusion, exit code — is written outside the job, which is exactly what an "
        "agent's own account of its own failure is not."
    ),
    "NULL_REPORTED_AS_ATTRITION": (
        "A run with an output sha256 is accounted for as a failure. A run that completes "
        "and misses the threshold is a RESULT — a null, first-class in the record, and #61 "
        "has nulls sorting themselves. Bytes exist, so the account is contradicted by the "
        "output it claims not to have."
    ),

    # ---- pre-existing data (the kind-(1) second form) ---------------------
    "NO_HOLDOUT": (
        "The declaration names a pre-existing dataset and no hold-out. Nothing in this "
        "repository can precede a dataset released in 2019, so ancestry against the data "
        "is not weak here, it is meaningless. You cannot make old data new — you can only "
        "manufacture a portion that has not been seen."
    ),
    "SPLIT_NOT_DERIVABLE": (
        "The hold-out is enumerated rather than derived from a committed rule and salt. An "
        "enumerated split is a choice, and a choice made by someone who has already seen "
        "the data is the exploratory move wearing a confirmatory label."
    ),
    "HOLDOUT_TOUCHED": (
        "A run predating the declaration read records inside the hold-out. The portion is "
        "no longer unseen, so the ordering the hold-out was constructed to restore is gone "
        "— and unlike a seed, it cannot be redrawn."
    ),
}

# A hazard is not a downgrade. #9: an untestable hazard is declared and attaches
# permanently to every leg the Inquiry earns. #64 established the pattern of the gate
# appending one itself, so it cannot be omitted by the party with a motive to omit it.
HAZARDS = {
    "cancellation_peek": (
        "One or more runs in this set were cancelled rather than completed. Logs stream, "
        "so a party watching a run can read the metric before the job writes output and "
        "cancel; the run then legitimately has no output, is honestly attested as "
        "cancelled, and the attrition policy replaces it with the next derivable seed. "
        "One peek per cancellation — visible and countable, because every cancellation is "
        "in the run record with the party that fired it. Marked rather than prevented, the "
        "same posture #64 took on the hand-entered manifest."
    ),
}


# --------------------------------------------------------------------------
# The two derivations. Both are pure functions of committed text, which is what lets a
# stranger recompute the register in a clone rather than being asked to trust a field.
# --------------------------------------------------------------------------

def seed_sequence(master_seed: str, rule: str, count: int) -> list[int]:
    """The seeds this declaration draws, in order.

    Deliberately boring. The property that matters is not the quality of the stream, it
    is that index i is a function of committed text alone — so 'the next seed' after a
    failure is arithmetic rather than a decision taken with the data in view.
    """
    if rule != "sha256-stream":
        raise ValueError(f"unknown draw rule: {rule}")
    out = []
    for i in range(count):
        h = hashlib.sha256(f"{master_seed}:{i}".encode()).hexdigest()
        out.append(int(h[:8], 16))
    return out


def holdout(record_ids: list[str], salt: str, fraction: float) -> set[str]:
    """The portion of a pre-existing dataset no run may read before the freeze.

    Same trick as the seed draw, pointed at records instead of runs: the split is a
    function of the salt, so it is recomputable by anyone and choosable by nobody.
    """
    cut = int(fraction * 10_000)
    return {
        r for r in record_ids
        if int(hashlib.sha256(f"{salt}:{r}".encode()).hexdigest()[:8], 16) % 10_000 < cut
    }


# --------------------------------------------------------------------------
# A toy commit graph. The real check calls `git merge-base --is-ancestor`; this exists so
# the driver can build a history that is wrong in one specific way.
# --------------------------------------------------------------------------

@dataclass
class Graph:
    parents: dict[str, tuple[str, ...]] = field(default_factory=dict)

    def commit(self, sha: str, *parents: str) -> str:
        self.parents[sha] = parents
        return sha

    def is_ancestor(self, a: str, b: str) -> bool:
        if a == b:
            return True
        seen, stack = set(), [b]
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            if cur == a:
                return True
            stack.extend(self.parents.get(cur, ()))
        return False


@dataclass
class Verdict:
    refusals: list[tuple[str, str]] = field(default_factory=list)
    downgrades: list[tuple[str, str]] = field(default_factory=list)
    hazards: list[str] = field(default_factory=list)

    @property
    def derivable(self) -> bool:
        return not self.refusals

    @property
    def register(self) -> str | None:
        if not self.derivable:
            return None
        return "exploratory" if self.downgrades else "confirmatory"

    @property
    def exit_code(self) -> int:
        """0 confirmatory, 1 exploratory, 2 underivable.

        The third code is the #53 lesson made structural: a check with nothing to measure
        must not report the same thing as a check that measured and found nothing wrong.
        """
        return {None: 2, "exploratory": 1, "confirmatory": 0}[self.register]

    def refuse(self, code: str, detail: str = "") -> None:
        self.refusals.append((code, detail))

    def downgrade(self, code: str, detail: str = "") -> None:
        self.downgrades.append((code, detail))

    def hazard(self, name: str) -> None:
        self.hazards.append(name)


# --------------------------------------------------------------------------
# The check.
# --------------------------------------------------------------------------

def derive(
    graph: Graph,
    *,
    charter_commit: str,
    freeze_commit: str,
    declaration: dict | None,
    declaration_commit: str | None,
    accounts: list[dict],
    prior_reads: list[str] | None = None,
) -> Verdict:
    """Derive the register of the result a declared set produced.

    `accounts` is one entry per run the record holds: its manifest fields, the commit
    that recorded it, and the runner's copied-in attestation. `prior_reads` is the record
    ids read by runs predating the declaration — only meaningful for pre-existing data.
    """
    v = Verdict()

    # -- is there anything to derive from? ----------------------------------
    if not declaration or not declaration_commit:
        v.refuse("SET_UNDECLARED", f"{len(accounts)} manifest(s) citing no declaration")
        return v

    if "register" in declaration or "register_policy" in declaration:
        v.refuse("DECLARATION_ASSERTS_REGISTER")

    draw = declaration.get("draw") or {}
    if not draw.get("master_seed") or not draw.get("rule"):
        v.refuse("SEEDS_NOT_DERIVABLE", f"seeds: {declaration.get('seeds', 'absent')}")

    attrition = declaration.get("attrition") or {}
    if "max_replacements" not in attrition:
        v.refuse("NO_ATTRITION_POLICY")

    dataset = declaration.get("dataset") or {}
    if dataset and not dataset.get("checksum"):
        v.refuse("DATASET_UNPINNED", f"source: {dataset.get('source', '?')}")

    if not v.derivable:
        return v

    # -- ancestry, over the graph -------------------------------------------
    if not graph.is_ancestor(charter_commit, declaration_commit):
        v.downgrade("CHARTER_NOT_ANCESTOR", f"{charter_commit} !< {declaration_commit}")
    if not graph.is_ancestor(freeze_commit, declaration_commit):
        v.downgrade("FREEZE_NOT_ANCESTOR", f"{freeze_commit} !< {declaration_commit}")

    # -- the seeds this declaration is allowed to have drawn -----------------
    count = int(draw.get("count", 0))
    allowed = seed_sequence(
        draw["master_seed"], draw["rule"], count + int(attrition["max_replacements"]))
    planned, replacements = allowed[:count], allowed[count:]

    seen: set[int] = set()
    used_replacements = 0

    for a in accounts:
        run = a.get("run_id", "?")
        seed = a.get("seed")

        if seed not in allowed:
            v.downgrade("UNDECLARED_RUN", f"{run}: seed {seed} is not in the draw")
            continue
        seen.add(seed)
        if seed in replacements:
            used_replacements += 1

        att = a.get("attestation") or {}
        has_output = bool(a.get("output_sha256"))

        # -- ordering: the run happened at or after the declaration ----------
        if not att:
            v.downgrade("DISPATCH_UNATTESTED", f"{run}: no workflow record copied in")
        elif not graph.is_ancestor(declaration_commit, att.get("checked_out", "")):
            v.downgrade(
                "DISPATCH_NOT_FROM_DECLARATION",
                f"{run}: ran from {att.get('checked_out')}, declared at {declaration_commit}")

        if has_output and not graph.is_ancestor(declaration_commit, a.get("commit", "")):
            v.downgrade("DECLARATION_NOT_ANCESTOR", f"{run}: recorded at {a.get('commit')}")

        # -- results and attrition are different things ----------------------
        if a.get("accounted_as") == "attrition":
            if has_output:
                v.downgrade("NULL_REPORTED_AS_ATTRITION", f"{run}: output exists")
            elif att.get("conclusion") in (None, "success"):
                v.downgrade("ATTRITION_UNATTESTED", f"{run}: conclusion={att.get('conclusion')}")
            if att.get("conclusion") == "cancelled":
                v.hazard("cancellation_peek")
        elif not has_output:
            v.downgrade("SET_INCOMPLETE", f"{run}: neither a result nor an attested failure")

    # -- every declared run is accounted for --------------------------------
    unaccounted = [s for s in planned if s not in seen]
    if unaccounted:
        # A planned seed may be legitimately absent only if a replacement stood in for it.
        if len(unaccounted) > used_replacements:
            v.downgrade(
                "SET_INCOMPLETE",
                f"{len(unaccounted)} declared seed(s) unaccounted, "
                f"{used_replacements} replacement(s) used")

    if used_replacements > int(attrition["max_replacements"]):
        v.downgrade(
            "ATTRITION_EXCEEDED",
            f"{used_replacements} used, {attrition['max_replacements']} declared")

    # -- the kind-(1) second form -------------------------------------------
    if dataset:
        split = dataset.get("split") or {}
        if not split:
            v.downgrade("NO_HOLDOUT", f"dataset: {dataset.get('source')}")
        elif not split.get("salt") or not split.get("fraction"):
            v.downgrade("SPLIT_NOT_DERIVABLE", f"rule: {split.get('rule', 'absent')}")
        else:
            held = holdout(
                dataset.get("record_ids") or [], split["salt"], float(split["fraction"]))
            touched = sorted(held & set(prior_reads or []))
            if touched:
                v.downgrade(
                    "HOLDOUT_TOUCHED",
                    f"{len(touched)} held-out record(s) already read: {', '.join(touched[:3])}…")

    # dedupe, preserving order: one code fires once however many runs tripped it
    for bucket in (v.downgrades,):
        first: dict[str, tuple[str, str]] = {}
        for code, detail in bucket:
            first.setdefault(code, (code, detail))
        bucket[:] = list(first.values())
    v.hazards[:] = list(dict.fromkeys(v.hazards))

    return v


# --------------------------------------------------------------------------
# Emission. Ruled on #63: the register is never a field in `inquiries/`. It renders into
# the coverage report and the notebook entry — artifacts that are already projections, so
# a copy there cannot be mistaken for a source the way a stamped field could.
# --------------------------------------------------------------------------

def render(v: Verdict, *, subject: str) -> str:
    if not v.derivable:
        lines = [
            f"NO REGISTER — {subject}",
            "  The register cannot be derived. This is not 'exploratory': it is the check",
            "  declining to report a verdict it did not compute.",
            "",
        ]
        for code, detail in v.refusals:
            lines.append(f"  [{code}]{(' ' + detail) if detail else ''}")
            lines.append(f"      {REFUSALS[code]}")
            lines.append("")
        return "\n".join(lines)

    lines = [f"{v.register.upper()} — {subject}"]
    if v.register == "confirmatory":
        lines.append("  Metric and decision rule preceded the set; the set preceded the data.")
        lines.append("  Eligible for the Protective Belt, by a separate human act.")
    else:
        lines.append(f"  {len(v.downgrades)} reason(s). First-class in the record, and")
        lines.append("  barred from the Belt: its route in is to become the preregistered")
        lines.append("  hypothesis of a new confirmatory Inquiry. That transition is Noah's.")
        lines.append("")
        for code, detail in v.downgrades:
            lines.append(f"  [{code}]{(' ' + detail) if detail else ''}")
            lines.append(f"      {DOWNGRADES[code]}")
            lines.append("")
    for name in v.hazards:
        lines.append("")
        lines.append(f"  + untestable hazard appended to the Inquiry: {name}")
        lines.append(f"      {HAZARDS[name]}")
    return "\n".join(lines)
