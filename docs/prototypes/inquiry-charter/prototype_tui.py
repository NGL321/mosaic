"""PROTOTYPE — drive the dispatch gate over a real charter.

    python docs/prototypes/inquiry-charter/prototype_tui.py

Loads the worked charter in `example/README.md`, then lets you break it one field at
a time and watch what the gate emits. Every defect below is one somebody will
actually commit: the plausible mistake, not the absurd one.
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
    c["adequacy"] = {"rationale": "The instrument should be able to detect topological structure reliably."}
    return c


def leak_hypothesis(c):
    """Tuning the apparatus against the thing being measured. The whole reason for the freeze."""
    c["adequacy"]["probe"] = "probes/h1_lifetime_trajectory.py"
    return c


def drop_falsifier(c):
    c["hypothesis"].pop("falsified_by", None)
    return c


def drop_decision_rule(c):
    c["discriminating"].pop("decision_rule", None)
    return c


def declare_register(c):
    """Helpful-looking, and it destroys the register guarantee."""
    c["register"] = "confirmatory"
    return c


def name_a_tier(c):
    c["environment_requirement"] = {"runs_on": "self-hosted, local-only"}
    return c


def rule_reasons_about_axioms(c):
    c["continue_return_retire"]["return"] = (
        "Return to Noah if a result appears to bear on the Least Action axiom."
    )
    return c


def unsigned(c):
    return c


CASES = [
    ("0", "the charter as written", lambda c: c, {}),
    ("1", "no Adequacy Criterion", drop_adequacy, {}),
    ("2", "Adequacy Criterion is prose", prose_adequacy, {}),
    ("3", "adequacy probe = the discriminating metric", leak_hypothesis, {}),
    ("4", "hypothesis with no falsifier", drop_falsifier, {}),
    ("5", "metric with no decision rule", drop_decision_rule, {}),
    ("6", "register declared in the charter", declare_register, {}),
    ("7", "environment names a tier", name_a_tier, {}),
    ("8", "rule reasons about the Hard Core", rule_reasons_about_axioms, {}),
    ("9", "last commit authored by the App", unsigned, {"signed_by_human": False}),
    ("a", "agent commit touched a frozen field", unsigned, {"agent_touched_frozen": True}),
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
        print("  a l l  run every case      q  quit")
        choice = input("\n> ").strip().lower()
        if choice in ("q", "quit", ""):
            return
        if choice in ("all", "l"):
            for k, *_ in CASES:
                run(base, k)
            continue
        if choice in {c[0] for c in CASES}:
            run(base, choice)
        else:
            print("  ?")


if __name__ == "__main__":
    main()
