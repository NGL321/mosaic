"""PROTOTYPE — the dispatch gate.

Ticket #60. Throwaway. Nothing depends on this and nothing runs it in CI.

The question it exists to answer: *is the refusal mechanical?* The map's premise 2
says an Inquiry with no hypothesis-blind Adequacy Criterion cannot be dispatched
AFK — "a visible refusal, and itself a finding about the Inquiry". A rule satisfiable
by writing a word is not a rule (#26 R6), so every check below is either structural
or checked against git, and none of them reads prose for meaning.

**Nothing here checks a signature.** After #164 the Inquiry charter carries no human
hand: the Question is agent-drafted, the Adequacy Criterion is apparatus, and the
freeze is ancestry. Noah's hand is on the Conjecture, one level up. Three refusals
below exist precisely to keep it there — a charter that declares a budget, a stall
tolerance or a continue/return/retire rule is claiming authority that is not its own.

Run the driver, not this file:

    python docs/prototypes/inquiry-charter/prototype_tui.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import yaml

# --------------------------------------------------------------------------
# Refusals. Each is a named, emittable finding — never a bare exit code.
# --------------------------------------------------------------------------

REFUSALS = {
    "NO_QUESTION": "No frozen Question. There is nothing for agents to search against.",
    "NO_CONJECTURE": (
        "The charter names no Conjecture. #164: an Inquiry is opened under a posted "
        "conjecture's authority and its budget, and the axioms it contributes are "
        "meaningless outside that system. An Inquiry serving nothing is unpayable and "
        "unaimed."
    ),
    "QUESTION_TARGETS_CORE": (
        "The Question occupies the goal position over a Hard Core member. #61's typing "
        "rule: core sentences may appear as premises and never as a goal. This is #9's "
        "'no Hard Core member may be an Inquiry's Question' as a well-formedness "
        "condition rather than a prohibition someone has to remember."
    ),
    "NO_ADEQUACY": (
        "No Adequacy Criterion. Premise 2: this Inquiry cannot be delegated AFK. "
        "The refusal is a finding — the Inquiry is not ready, and saying so is research output."
    ),
    "ADEQUACY_NOT_DECIDABLE": (
        "The Adequacy Criterion is prose. It needs an executable probe, the name it "
        "decides, and a threshold, or no agent can tell when the search has ended."
    ),
    "ADEQUACY_NOT_BLIND": (
        "The Adequacy Criterion references a name declared under `hypothesis`, "
        "`axiom_if_carried` or `discriminating`. Blindness is enforced by scope, not by "
        "reading: the two namespaces are disjoint or the charter is refused."
    ),
    "NO_REDUCTION_CHECK": (
        "No reduction check. #9, via #61: a novel measure must show predictive content "
        "the cheapest available measure does not already carry, with the confound set "
        "named before the data exists. An Inquiry proposing a novel measure with no "
        "statable confound set refuses itself."
    ),
    "HAZARDS_UNDECLARED": (
        "No hazard declaration. #9 splits them: testable hazards become further adequacy "
        "clauses, untestable ones are named and travel onto every leg this Inquiry earns. "
        "An empty declaration is a claim that there are none, and must be written as one."
    ),
    "NO_DECISION_RULE": (
        "A discriminating metric with no decision rule. A number that means nothing "
        "in advance means whatever is convenient afterwards."
    ),
    "REGISTER_DECLARED": (
        "The charter declares a register. #56: Register is a property of a result and "
        "is derived from ancestry, never asserted. A declared register is a register "
        "an argument can move."
    ),
    "GOVERNOR_DECLARED": (
        "The charter declares a budget, a spend ceiling or a stall tolerance. #164 moved "
        "the governor to the Conjecture, which is what authorises and pays for this "
        "Inquiry. A local budget is an Inquiry writing its own cheque."
    ),
    "RULE_DECLARED": (
        "The charter declares a continue/return/retire rule. #61: those verbs only mean "
        "anything at the Conjecture. What the Inquiry keeps is mechanical and needs no "
        "signature — adequacy met, freeze; allocation spent, Exhausted; inadmissible "
        "result, return."
    ),
    "TIER_NAMED": (
        "The environment names a tier rather than stating a requirement. Premise 11: "
        "the charter declares what it needs; the loop decides what satisfies it. An "
        "agent may never widen a tier, and it cannot widen what it cannot name."
    ),
    "NO_ENVIRONMENT": (
        "No environment requirement. The loop cannot route a job it cannot describe, "
        "and silence would be routed to whatever is cheapest."
    ),
    "NO_PLACEMENT": (
        "No placement constraint. Premise 7: every dataset an Inquiry touches carries "
        "a declared constraint, and absence is not permission."
    ),
    "POST_OPEN_AMENDMENT": (
        "A frozen field was modified after the Inquiry opened. #61: agents may propose "
        "and may never amend. The freeze is git ancestry, which is what makes it "
        "checkable in a clone rather than promised in a document. An unsatisfiable "
        "Adequacy Criterion ends the Inquiry Exhausted; it does not get edited."
    ),
}

HARD_CORE_TERMS = ("least action", "scale corollary")

# A tier is a place. A requirement is a capability. The gate knows the place-names.
TIER_NAMES = (
    "self-hosted",
    "local-only",
    "github-hosted",
    "ubuntu-latest",
    "modal",
    "runpod",
    "cloud",
    "desktop",
    "the pi",
    "raspberry",
)

MISSING_REFUSAL = {
    "question": "NO_QUESTION",
    "conjectures": "NO_CONJECTURE",
    "adequacy": "NO_ADEQUACY",
    "placement": "NO_PLACEMENT",
    "environment_requirement": "NO_ENVIRONMENT",
}

# Fields that belong to the Conjecture. Their presence here is the refusal.
GOVERNOR_FIELDS = ("budget", "spend_ceiling", "stall_tolerance", "token_allocation")
RULE_FIELDS = ("continue_return_retire", "continue", "retire")


@dataclass
class Verdict:
    refusals: list[tuple[str, str]] = field(default_factory=list)

    @property
    def dispatchable(self) -> bool:
        return not self.refusals

    def refuse(self, code: str, detail: str = "") -> None:
        self.refusals.append((code, detail))


def _names_in(node) -> set[str]:
    """Every identifier-ish token reachable from a subtree.

    Deliberately crude: file paths and snake_case names. The point is that blindness is
    decided over a *name set*, so an agent cannot argue its way across the boundary — it
    can only rename, and renaming is visible in the diff of a file frozen at open.
    """
    out: set[str] = set()
    if isinstance(node, dict):
        for v in node.values():
            out |= _names_in(v)
    elif isinstance(node, list):
        for v in node:
            out |= _names_in(v)
    elif isinstance(node, str):
        for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_./-]*", node):
            if "/" in tok or "_" in tok:
                out.add(tok.strip("./"))
    return out


def _strip_prose(node):
    """Drop the fields written for a human. The gate never reads them for meaning."""
    prose = {"rationale", "statement", "requires", "basis", "notes", "over"}
    if isinstance(node, dict):
        return {k: _strip_prose(v) for k, v in node.items() if k not in prose}
    if isinstance(node, list):
        return [_strip_prose(v) for v in node]
    return node


def parse(text: str) -> dict:
    parts = re.split(r"(?m)^---[ \t]*$\n?", text, maxsplit=2)
    if len(parts) < 3 or parts[0].strip():
        raise ValueError("charter has no front matter")
    return yaml.safe_load(parts[1]) or {}


def check(charter: dict, *, amended_after_open: bool = False) -> Verdict:
    v = Verdict()

    for key, code in MISSING_REFUSAL.items():
        if not charter.get(key):
            v.refuse(code, f"missing: {key}")

    adequacy = charter.get("adequacy") or {}
    hypothesis = charter.get("hypothesis") or {}
    discriminating = charter.get("discriminating") or {}

    # -- the Question may not aim at the core ------------------------------
    hits = [t for t in HARD_CORE_TERMS if t in str(charter.get("question", "")).lower()]
    if hits:
        v.refuse("QUESTION_TARGETS_CORE", f"in goal position: {', '.join(hits)}")

    if adequacy:
        # -- adequacy is machine-decidable ---------------------------------
        missing = [k for k in ("probe", "decides", "threshold") if not adequacy.get(k)]
        if missing:
            v.refuse("ADEQUACY_NOT_DECIDABLE", f"missing: {', '.join(missing)}")

        # -- #9's two mandatory clauses ------------------------------------
        if not adequacy.get("reduction_check"):
            v.refuse("NO_REDUCTION_CHECK")
        hazards = adequacy.get("hazards")
        if hazards is None or not isinstance(hazards, dict) or (
            "testable" not in hazards and "untestable" not in hazards
        ):
            v.refuse("HAZARDS_UNDECLARED")

        # -- adequacy is hypothesis-blind, by scope -------------------------
        adequacy_names = _names_in(_strip_prose(adequacy))
        hypothesis_names = _names_in(_strip_prose(
            {"h": hypothesis, "d": discriminating, "a": charter.get("axiom_if_carried")}))
        leaked = sorted(adequacy_names & hypothesis_names)
        if leaked:
            v.refuse("ADEQUACY_NOT_BLIND", f"shared names: {', '.join(leaked)}")

    # -- a metric without a rule --------------------------------------------
    if discriminating.get("metric") and not discriminating.get("decision_rule"):
        v.refuse("NO_DECISION_RULE")

    # -- three things that live one level up ---------------------------------
    if "register" in charter or "register_policy" in charter:
        v.refuse("REGISTER_DECLARED")
    named = [f for f in GOVERNOR_FIELDS if f in charter]
    if named:
        v.refuse("GOVERNOR_DECLARED", f"declared: {', '.join(named)}")
    named = [f for f in RULE_FIELDS if f in charter]
    if named:
        v.refuse("RULE_DECLARED", f"declared: {', '.join(named)}")

    # -- requirement, not tier ----------------------------------------------
    env_text = yaml.safe_dump(charter.get("environment_requirement") or "").lower()
    named = [t for t in TIER_NAMES if t in env_text]
    if named:
        v.refuse("TIER_NAMED", f"named: {', '.join(named)}")

    # -- the git-checked one -------------------------------------------------
    if amended_after_open:
        v.refuse("POST_OPEN_AMENDMENT")

    return v


def render(v: Verdict, *, slug: str) -> str:
    """What the gate emits. A refusal is a comment on the Inquiry's issue, not a log line."""
    if v.dispatchable:
        return f"DISPATCHABLE — {slug}\n  The Question is frozen. Searching may begin."
    lines = [
        f"REFUSED — {slug}",
        f"  {len(v.refusals)} refusal(s). The Inquiry does not enter Searching.",
        "",
    ]
    for code, detail in v.refusals:
        lines.append(f"  [{code}]{(' ' + detail) if detail else ''}")
        lines.append(f"      {REFUSALS[code]}")
        lines.append("")
    return "\n".join(lines)
