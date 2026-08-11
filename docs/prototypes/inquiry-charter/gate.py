"""PROTOTYPE — the dispatch gate.

Ticket #60. Throwaway. Nothing depends on this and nothing runs it in CI.

The question it exists to answer: *is the refusal mechanical?* The map's premise 2
says an Inquiry with no hypothesis-blind Adequacy Criterion cannot be dispatched
AFK — "a visible refusal, and itself a finding about the Inquiry". A rule satisfiable
by writing a word is not a rule (#26 R6), so every check below is either structural
or checked against git, and none of them reads prose for meaning.

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
    "NO_ADEQUACY": (
        "No Adequacy Criterion. Premise 2: this Inquiry cannot be delegated AFK. "
        "The refusal is a finding — the Inquiry is not ready, and saying so is research output."
    ),
    "ADEQUACY_NOT_DECIDABLE": (
        "The Adequacy Criterion is prose. It needs an executable probe, the name it "
        "decides, and a threshold, or no agent can tell when the search has ended."
    ),
    "ADEQUACY_NOT_BLIND": (
        "The Adequacy Criterion references a name declared under `hypothesis` or "
        "`discriminating`. Blindness is enforced by scope, not by reading: the two "
        "namespaces are disjoint or the charter is refused."
    ),
    "NO_FALSIFIER": (
        "The hypothesis states no falsifier. inquiries/README.md: an Inquiry that "
        "cannot say what would falsify the claim it serves is not ready to run."
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
    "TIER_NAMED": (
        "The environment names a tier rather than stating a requirement. Premise 11: "
        "the charter declares what it needs; the loop decides what satisfies it. An "
        "agent may never widen a tier, and it cannot widen what it cannot name."
    ),
    "NO_PLACEMENT": (
        "No placement constraint. Premise 7: every dataset an Inquiry touches carries "
        "a declared constraint, and absence is not permission."
    ),
    "NO_BUDGET": "No search budget. There is no terminator, so Exhausted is unreachable.",
    "NO_ENVIRONMENT": (
        "No environment requirement. The loop cannot route a job it cannot describe, "
        "and silence would be routed to whatever is cheapest."
    ),
    "RULE_NAMES_HARD_CORE": (
        "The continue/return/retire rule references the Hard Core. #61: the Negative "
        "Heuristic mechanises as a refusal — an agent may never record a result as "
        "bearing on the axioms, so its rule may never reason about them."
    ),
    "UNSIGNED": (
        "The charter's last commit was not authored by the human. §5 custody: "
        "falsification criteria are human-authored outright. Under a GitHub App "
        "identity (#24) this is checkable, not a matter of trust."
    ),
    "FROZEN_FIELD_TOUCHED": (
        "An agent commit modified a frozen field. The freeze is git ancestry, and this "
        "is what makes it checkable in a clone rather than promised in a document."
    ),
}

HARD_CORE_TERMS = ("hard core", "least action", "scale corollary", "axiom")

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
    "adequacy": "NO_ADEQUACY",
    "budget": "NO_BUDGET",
    "placement": "NO_PLACEMENT",
    "environment_requirement": "NO_ENVIRONMENT",
}


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

    Deliberately crude: file paths, snake_case names, and quoted symbols. The point
    is that blindness is decided over a *name set*, so an agent cannot argue its way
    across the boundary — it can only rename, and renaming is visible in the diff.
    """
    out: set[str] = set()
    if isinstance(node, dict):
        for k, v in node.items():
            out |= _names_in(v)
    elif isinstance(node, list):
        for v in node:
            out |= _names_in(v)
    elif isinstance(node, str):
        for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_./-]*", node):
            if "/" in tok or "_" in tok:
                out.add(tok.strip("./"))
    return out


def parse(text: str) -> dict:
    parts = re.split(r"(?m)^---[ \t]*$\n?", text, maxsplit=2)
    if len(parts) < 3 or parts[0].strip():
        raise ValueError("charter has no front matter")
    return yaml.safe_load(parts[1]) or {}


def check(charter: dict, *, signed_by_human: bool = True,
          agent_touched_frozen: bool = False) -> Verdict:
    v = Verdict()

    # -- presence -----------------------------------------------------------
    for key, code in MISSING_REFUSAL.items():
        if not charter.get(key):
            v.refuse(code, f"missing: {key}")

    adequacy = charter.get("adequacy") or {}
    hypothesis = charter.get("hypothesis") or {}
    discriminating = charter.get("discriminating") or {}

    # -- adequacy is machine-decidable --------------------------------------
    if adequacy:
        missing = [k for k in ("probe", "decides", "threshold") if not adequacy.get(k)]
        if missing:
            v.refuse("ADEQUACY_NOT_DECIDABLE", f"missing: {', '.join(missing)}")

        # -- adequacy is hypothesis-blind, by scope --------------------------
        adequacy_names = _names_in(
            {k: val for k, val in adequacy.items() if k != "rationale"})
        hypothesis_names = _names_in(hypothesis) | _names_in(discriminating)
        leaked = sorted(adequacy_names & hypothesis_names)
        if leaked:
            v.refuse("ADEQUACY_NOT_BLIND", f"shared names: {', '.join(leaked)}")

    # -- a hypothesis, if present, states its falsifier ----------------------
    if hypothesis and not hypothesis.get("falsified_by"):
        v.refuse("NO_FALSIFIER")

    # -- a metric without a rule --------------------------------------------
    if discriminating.get("metric") and not discriminating.get("decision_rule"):
        v.refuse("NO_DECISION_RULE")

    # -- the register is derived, never declared -----------------------------
    if "register" in charter or "register_policy" in charter:
        v.refuse("REGISTER_DECLARED")

    # -- requirement, not tier ----------------------------------------------
    env_text = yaml.safe_dump(charter.get("environment_requirement") or "").lower()
    named = [t for t in TIER_NAMES if t in env_text]
    if named:
        v.refuse("TIER_NAMED", f"named: {', '.join(named)}")

    # -- the rule may not reason about the Hard Core -------------------------
    rule_text = yaml.safe_dump(charter.get("continue_return_retire") or "").lower()
    hits = [t for t in HARD_CORE_TERMS if t in rule_text]
    if hits:
        v.refuse("RULE_NAMES_HARD_CORE", f"named: {', '.join(hits)}")

    # -- the two git-checked ones -------------------------------------------
    if not signed_by_human:
        v.refuse("UNSIGNED")
    if agent_touched_frozen:
        v.refuse("FROZEN_FIELD_TOUCHED")

    return v


def render(v: Verdict, *, slug: str) -> str:
    """What the gate emits. A refusal is a comment on the Inquiry's issue, not a log line."""
    if v.dispatchable:
        return f"DISPATCHABLE — {slug}\n  The Question is frozen. Searching may begin."
    lines = [f"REFUSED — {slug}", f"  {len(v.refusals)} refusal(s). The Inquiry does not enter Searching.", ""]
    for code, detail in v.refusals:
        lines.append(f"  [{code}]{(' ' + detail) if detail else ''}")
        lines.append(f"      {REFUSALS[code]}")
        lines.append("")
    return "\n".join(lines)
