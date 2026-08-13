"""PROTOTYPE — drive the declaration gate over the commit that adds a declaration.

    python docs/prototypes/declaration-gate/prototype_tui.py

Every case is one commit: a `.declared.yaml` appearing under `inquiries/NNN-slug/runs/`,
against whatever declarations are already in that directory. No git history, no manifests,
no runner — if a case needs any of those, it is by construction not this gate's.

CASE `p` IS THE ONE THE TICKET EXISTS FOR: #182's `NO_PREDECESSOR`, refused at the commit
that declares the set rather than at the register read after the set has run.

CASE `h` IS THE ONE THAT DRAWS THE LINE. A kind-(1) declaration with no hold-out at all is
ACCEPTED. `NO_HOLDOUT` is a #63 downgrade, not a refusal — the set derives `exploratory`,
which is first-class in the record — so a gate that refused it would forbid legitimate
work in the name of protecting it.

CASE `B` IS THE POSTURE QUESTION, priced. The same defect, bypassed, arriving at set close
as #63's exit 2 with a set's budget already spent.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import gate  # noqa: E402
import yaml  # noqa: E402

HERE = Path(__file__).parent


def load(name: str) -> dict:
    return yaml.safe_load((HERE / "example" / name).read_text(encoding="utf-8"))


FIRST = "2026-08-14-s3f9c1.declared.yaml"       # kind (2), the first set in the Inquiry
SUCCESSOR = "2026-08-21-w4a1d8.declared.yaml"   # kind (2), the second attempt
DATASET = "2026-08-14-p7b2e4.declared.yaml"     # kind (1), over a 2019 release

SLUGS = {172: "formation-signature-grokking", 181: "visual-coding-holdout"}


# The directory as the successor finds it: one closed predecessor.
CLOSED_PREDECESSOR = [{"set_id": "s3f9c1", "closed": True, "salt": None}]
OPEN_PREDECESSOR = [{"set_id": "s3f9c1", "closed": False, "salt": None}]
TWO_CLOSED = [
    {"set_id": "s3f9c1", "closed": True, "salt": None},
    {"set_id": "w4a1d8", "closed": True, "salt": None},
]
CLOSED_DATASET_SET = [
    {"set_id": "p7b2e4", "closed": True, "salt": "181:p7b2e4:holdout"},
]


# ---------------------------------------------------------------------------
# Cases. (key, label, file, siblings, mutate, mode)
#
# `mutate` breaks exactly one thing in the declaration. Every one of them is a mistake an
# agent produces on its own; none requires anyone to be dishonest.
# ---------------------------------------------------------------------------

def declared_register(d):
    d["register"] = "confirmatory"


def literal_seeds(d):
    d["draw"] = {"seeds": [17, 23, 42, 108, 271, 314]}


def no_attrition(d):
    d.pop("attrition")


def unpinned(d):
    d["dataset"].pop("checksum")


def no_follows(d):
    d.pop("follows")


def follows_older(d):
    d["follows"] = "s3f9c1"  # against TWO_CLOSED, the most recent is w4a1d8


def no_holdout(d):
    d["dataset"].pop("split")


def reused_salt(d):
    d["follows"] = "p7b2e4"
    d["set_id"] = "q8c3f0"
    d["dataset"]["split"]["salt"] = "181:p7b2e4:holdout"


def fresh_salt(d):
    d["follows"] = "p7b2e4"
    d["set_id"] = "q8c3f0"
    d["dataset"]["split"]["salt"] = "181:q8c3f0:holdout"


def stale_config(d):
    d["config_sha"] = "sha256:" + "0" * 64


def two_at_once(d):
    d.pop("attrition")
    d["register"] = "exploratory"


CASES = [
    ("0", "the first set in an empty runs/ — nothing to follow", FIRST, [], None, "add"),
    ("1", "the successor, naming its closed predecessor", SUCCESSOR, CLOSED_PREDECESSOR, None, "add"),
    ("g", "the declaration asserts a register", FIRST, [], declared_register, "add"),
    ("l", "seeds listed literally", FIRST, [], literal_seeds, "add"),
    ("a", "no attrition policy declared", FIRST, [], no_attrition, "add"),
    ("P", "kind (1): the dataset unpinned", DATASET, [], unpinned, "add"),
    ("p", "a second set that names no predecessor", SUCCESSOR, CLOSED_PREDECESSOR, no_follows, "add"),
    ("o", "a second set declared while the first is still open", SUCCESSOR, OPEN_PREDECESSOR, None, "add"),
    ("j", "a third set that follows the first, not the second", SUCCESSOR, TWO_CLOSED, follows_older, "add"),
    ("d", "a predecessor declared and then abandoned, unrun", SUCCESSOR, OPEN_PREDECESSOR, None, "add"),
    ("A", "an existing declaration, edited", FIRST, CLOSED_PREDECESSOR, None, "modify"),
    ("S", "kind (1): a successor reusing the same hold-out salt", DATASET, CLOSED_DATASET_SET, reused_salt, "add"),
    ("F", "kind (1): a successor with a fresh salt", DATASET, CLOSED_DATASET_SET, fresh_salt, "add"),
    ("h", "kind (1): no hold-out at all — ACCEPTED, and why", DATASET, [], no_holdout, "add"),
    ("c", "a config_sha that is not the frozen one — ACCEPTED, and why", FIRST, [], stale_config, "add"),
    ("2", "two defects in one commit", FIRST, [], two_at_once, "add"),
]


def run(key: str) -> None:
    label, name, siblings, mutate, mode = next(
        (c[1], c[2], c[3], c[4], c[5]) for c in CASES if c[0] == key)

    decl = copy.deepcopy(load(name))
    if mutate:
        mutate(decl)

    print("\n" + "=" * 76)
    print(f"CASE {key} — {label}")
    print("=" * 76)
    path = f"inquiries/{decl['inquiry']}-{SLUGS[decl['inquiry']]}/runs/{name}"
    print(f"  commit {mode}s  {path}")
    print(f"  runs/ already holds  {[s['set_id'] for s in siblings] or 'nothing'}")
    print()

    v = gate.check_declaration(decl, siblings, mode)
    print(gate.render(v, subject=f"set {decl['set_id']}"))
    print(f"\n  exit {v.exit_code}")

    if key == "h":
        print(
            "\n  Why accepted: NO_HOLDOUT is a #63 DOWNGRADE. This set will derive\n"
            "  `exploratory` at close, and exploratory results are first-class in the\n"
            "  record — barred from the Belt, with a route in via premise 3. Refusing it\n"
            "  here would be the gate deciding what kind of evidence the programme is\n"
            "  allowed to gather. The partition is what keeps that from happening by\n"
            "  accident: press `?`."
        )
    if key == "c":
        print(
            "\n  Why accepted: FREEZE_NOT_ANCESTOR is a downgrade too, and it reads git\n"
            "  history the gate does not have. Both reasons are independent and both\n"
            "  point the same way."
        )
    if key == "S":
        print(
            "\n  #182 ruled this exit 2 and did not hand it to #181. It reads two\n"
            "  committed files and nothing else, so the partition claims it. Six of the\n"
            "  seven the gate fires were named somewhere; this one was named and misfiled."
        )
    if key == "d":
        print(
            "\n  Mechanically identical to case `o`, and a different problem. s3f9c1 was\n"
            "  declared and then abandoned — the config was wrong, the Inquiry moved on,\n"
            "  nothing ever ran. #182 requires the predecessor to have CLOSED, and nothing\n"
            "  closes a set with no runs: SET_INCOMPLETE is a downgrade over manifests\n"
            "  that will never exist. So the Inquiry's runs/ is a dead end, and the only\n"
            "  exits are to delete the declaration — which the gate would refuse as an\n"
            "  amendment, and which erases the sequence #182 exists to record — or to run\n"
            "  a set nobody wants in order to close it.\n"
            "\n  THE GATE DID NOT CAUSE THIS. #182's line has no termination rule and the\n"
            "  gate is only where it becomes visible: before the gate, the dead end is\n"
            "  found at set close, after the successor has run. Open question, on the\n"
            "  ticket."
        )
    if key == "A":
        print(
            "\n  The gate never looks at the content. #60 needs git history to tell a\n"
            "  legitimate pre-open charter edit from an illegitimate post-open one; a\n"
            "  declaration has no legitimate edit, so the diff mode settles it alone.\n"
            "  Nothing downstream can see this: #63 derives from the declaration's text\n"
            "  as it stands, so an edited master_seed retroactively draws whichever seed\n"
            "  was published."
        )


def bypass() -> None:
    """CASE B — the posture question, priced rather than argued."""
    decl = copy.deepcopy(load(SUCCESSOR))
    no_follows(decl)

    print("\n" + "=" * 76)
    print("CASE B — the same defect, with the gate bypassed")
    print("=" * 76)
    print(
        "  The declaration is committed to a branch nobody opened a pull request for.\n"
        "  The gate does not run. Six runs execute against it.\n"
    )
    v = gate.check_declaration(decl, CLOSED_PREDECESSOR, "add")
    for name, _, _c in v.refusals:
        print(f"    at the declaring commit   {name}   exit 2   [not run]")
    print("    ... 6 runs, ~4 GPU-hours, ~$2.40 at #57's Modal rate ...")
    for name, _, _c in v.refusals:
        print(f"    at set close (#63)        {name}   exit 2   [run]")
    print(
        "\n  Same finding, same name, same exit code, same function over the same text.\n"
        "  The gate is not a new authority and cannot disagree with the backstop — it is\n"
        "  #63's own refusal, fired at the first commit that could have carried it.\n"
        "\n  So what the gate buys is not correctness. Correctness was never at risk: the\n"
        "  register still refuses at close, and a set whose register cannot derive is not\n"
        "  evidence. What it buys is the budget, and the difference between a refusal that\n"
        "  arrives before the declaring party has moved on and one that arrives after.\n"
        "\n  And what it costs, if it reads as load-bearing when it is not, is #53's\n"
        "  failure exactly. Which is why the gate says ACCEPTED rather than CONFIRMATORY,\n"
        "  and why nothing in it can pronounce on a register."
    )


def main() -> None:
    print(__doc__)
    while True:
        print("\n" + "-" * 76)
        for k, label, *_ in CASES:
            print(f"  {k}  {label}")
        print("  B  the same defect, bypassed — what the gate actually buys")
        print("  ?  the partition: every #63/#182 finding, by what it reads")
        print("  all  run every case      q  quit")
        choice = input("\n> ").strip()
        if choice.lower() in ("q", "quit", ""):
            return
        if choice == "?":
            print("\n" + gate.partition_table())
            continue
        if choice == "B":
            bypass()
            continue
        if choice.lower() == "all":
            for k, *_ in CASES:
                run(k)
            bypass()
            continue
        if choice in {c[0] for c in CASES}:
            run(choice)
        else:
            print("  ?")


if __name__ == "__main__":
    main()
