"""PROTOTYPE — drive the dispatch gate over a real charter.

    python docs/prototypes/inquiry-charter/prototype_tui.py

Loads the worked charter in `example/README.md`, then breaks it one field at a time so
you can watch what the gate emits. Every defect below is one somebody will actually
commit: the plausible mistake, not the absurd one.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import gate  # noqa: E402

HERE = Path(__file__).parent
CHARTER = HERE / "example" / "README.md"


def drop_adequacy(c):
    """The charter that reads well and cannot be delegated."""
    c.pop("adequacy", None)
    return c


def prose_adequacy(c):
    """Adequacy as a sentence — the most likely real mistake."""
    c["adequacy"] = {
        "rationale": "The instrument should reliably detect topological structure.",
        "reduction_check": {"against": ["probes/baseline_weight_norm.py"]},
        "hazards": {"untestable": []},
    }
    return c


def leak_hypothesis(c):
    """Tuning the apparatus against the thing being measured. The reason for the freeze."""
    c["adequacy"]["probe"] = "probes/h1_lifetime_trajectory.py"
    return c


def drop_reduction_check(c):
    """A novel measure with no confound set. #9's clause, and easy to omit."""
    c["adequacy"].pop("reduction_check", None)
    return c


def drop_hazards(c):
    """Silence is not 'no hazards' — it has to be written as a claim."""
    c["adequacy"].pop("hazards", None)
    return c


def drop_conjecture(c):
    """An Inquiry serving nothing: unaimed, and nobody's budget pays for it."""
    c.pop("conjectures", None)
    return c


def question_targets_core(c):
    c["question"] = "Does Least Action hold for schema-level inference?"
    return c


def drop_decision_rule(c):
    c["discriminating"].pop("decision_rule", None)
    return c


def declare_register(c):
    """Helpful-looking, and it destroys the register guarantee."""
    c["register"] = "confirmatory"
    return c


def declare_budget(c):
    """The pre-#164 charter. This is what the format used to say, and it is now a refusal."""
    c["budget"] = {"experiments": 40, "gpu_hours": 25}
    c["stall_tolerance"] = "3 Inquiries with no gap movement"
    return c


def declare_rule(c):
    c["continue_return_retire"] = {
        "continue": "While instruments remain untried and the budget holds.",
        "retire": "On budget exhaustion with nothing passing adequacy.",
    }
    return c


def name_a_tier(c):
    c["environment_requirement"] = {"runs_on": "self-hosted, local-only"}
    return c


def identity(c):
    return c


CASES = [
    ("0", "the charter as written", identity, {}),
    ("1", "no Adequacy Criterion", drop_adequacy, {}),
    ("2", "Adequacy Criterion is prose", prose_adequacy, {}),
    ("3", "adequacy probe = the discriminating metric", leak_hypothesis, {}),
    ("4", "no reduction check", drop_reduction_check, {}),
    ("5", "hazards not declared at all", drop_hazards, {}),
    ("6", "serves no Conjecture", drop_conjecture, {}),
    ("7", "the Question aims at the Hard Core", question_targets_core, {}),
    ("8", "metric with no decision rule", drop_decision_rule, {}),
    ("9", "register declared in the charter", declare_register, {}),
    ("b", "budget + stall tolerance declared (the pre-#164 charter)", declare_budget, {}),
    ("c", "continue/return/retire declared", declare_rule, {}),
    ("t", "environment names a tier", name_a_tier, {}),
    ("m", "a frozen field amended after open", identity, {"amended_after_open": True}),
]


def run(base: dict, key: str) -> None:
    label, mutate, flags = next((c[1], c[2], c[3]) for c in CASES if c[0] == key)
    charter = mutate(copy.deepcopy(base))
    verdict = gate.check(charter, **flags)
    print("\n" + "=" * 74)
    print(f"CASE {key} — {label}")
    print("=" * 74)
    print(gate.render(verdict, slug=f"{base['inquiry']}-{base['slug']}"))


def main() -> None:
    base = gate.parse(CHARTER.read_text(encoding="utf-8"))
    print(__doc__)
    while True:
        print("\n" + "-" * 74)
        for k, label, _, _ in CASES:
            print(f"  {k}  {label}")
        print("  all  run every case      q  quit")
        choice = input("\n> ").strip().lower()
        if choice in ("q", "quit", ""):
            return
        if choice == "all":
            for k, *_ in CASES:
                run(base, k)
            continue
        if choice in {c[0] for c in CASES}:
            run(base, choice)
        else:
            print("  ?")


if __name__ == "__main__":
    main()
