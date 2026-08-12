"""PROTOTYPE — drive the register check over a real declaration and a real set of runs.

    python docs/prototypes/register-check/prototype_tui.py

Builds an honest history — charter, freeze, declaration, six runs — and then breaks it one
way at a time. Every defect below is one an agent would plausibly produce on its own; none
of them requires anyone to be dishonest, which is the point.

CASE `t` IS THE ONE THE TICKET EXISTS FOR. It is the ticket's own rule, satisfied: the
config SHA is a genuine ancestor of the commit recording the output. It passes ancestry
and the result is exploratory, because the runs happened before the declaration and the
graph cannot see that. Only the runner's witness of what it checked out can.

CASE `s` is the one nothing before this ticket could see at all: twenty seeds run, one
manifest published. Perfect ancestry on the published result, and the data chose it.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import register  # noqa: E402
import yaml  # noqa: E402

HERE = Path(__file__).parent


# ---------------------------------------------------------------------------
# The honest history. Linear, because the shape that matters is the order.
#
#   c_charter  README.md — the Question, the metric, the decision rule. Frozen at open.
#   c_freeze   config.yaml appears. #60: this commit IS the freeze.
#   c_declare  the run-set declaration appears. This commit is the data freeze.
#   c_run_*    one commit per run, recording its manifest at publish.
# ---------------------------------------------------------------------------

def honest_world(decl_path: str = "2026-08-14-s3f9c1.declared.yaml"):
    g = register.Graph()
    g.commit("c_charter")
    g.commit("c_freeze", "c_charter")
    g.commit("c_declare", "c_freeze")

    decl = yaml.safe_load((HERE / "example" / decl_path).read_text(encoding="utf-8"))
    seeds = register.seed_sequence(
        decl["draw"]["master_seed"], decl["draw"]["rule"], decl["draw"]["count"])

    accounts = []
    prev = "c_declare"
    for i, seed in enumerate(seeds):
        commit = f"c_run{i}"
        g.commit(commit, prev)
        prev = commit
        accounts.append({
            "run_id": f"2026-08-14-r{i}",
            "set_id": decl["set_id"],
            "seed": seed,
            "commit": commit,
            "output_sha256": "sha256:" + f"{i}" * 64,
            "accounted_as": "result",
            # Copied into the manifest at publish by the runner, never referenced live:
            # GitHub expires logs, and a register derivable only until a retention window
            # closes is not derivable. Same author and same moment as #64's `env:` block.
            "attestation": {
                "workflow_run_id": 9_100_000 + i,
                "checked_out": commit,
                "conclusion": "success",
                "reported_by": "app",
            },
        })
    return g, decl, accounts


# ---------------------------------------------------------------------------
# Mutations. Each takes (graph, declaration, accounts) and breaks exactly one thing.
# ---------------------------------------------------------------------------

def identity(g, d, a):
    return g, d, a, None


def ticket_rule_satisfied(g, d, a):
    """THE case. The ticket's rule holds and the result is exploratory anyway.

    Ran the sweep first, liked a number, then committed the declaration. Every commit is
    in the right order — the freeze precedes the declaration, the declaration precedes
    every manifest — and the runner's record says each job checked out a commit that
    predates the declaration. That witness is the only thing in the record that knows.
    """
    for i, acct in enumerate(a):
        acct["attestation"]["checked_out"] = "c_freeze"
    return g, d, a, None


def seed_shopping(g, d, a):
    """Six declared, one published. Invisible before this ticket; a hole now."""
    return g, d, a[:1], None


def reroll(g, d, a):
    """A seed nobody's rule draws. The commonest honest-looking mistake: hard-coding 42."""
    a[3]["seed"] = 42
    return g, d, a, None


def null_as_attrition(g, d, a):
    """The number came out wrong, so the run is filed as a failure. Bytes say otherwise."""
    a[2]["accounted_as"] = "attrition"
    return g, d, a, None


def agent_claimed_failure(g, d, a):
    """An agent's own account of its own failure, with the runner reporting success."""
    a[2]["accounted_as"] = "attrition"
    a[2]["output_sha256"] = None
    return g, d, a, None


def honest_attrition(g, d, a):
    """A run OOMs and is replaced by the next seed in the stream. Stays confirmatory."""
    a[2]["accounted_as"] = "attrition"
    a[2]["output_sha256"] = None
    a[2]["attestation"]["conclusion"] = "failure"
    replacement = register.seed_sequence(
        d["draw"]["master_seed"], d["draw"]["rule"], d["draw"]["count"] + 1)[-1]
    g.commit("c_run_r", "c_run5")
    a.append({
        "run_id": "2026-08-15-rr", "set_id": d["set_id"], "seed": replacement,
        "commit": "c_run_r", "output_sha256": "sha256:" + "a" * 64,
        "accounted_as": "result",
        "attestation": {"workflow_run_id": 9_100_099, "checked_out": "c_run_r",
                        "conclusion": "success", "reported_by": "app"},
    })
    return g, d, a, None


def cancelled(g, d, a):
    """Cancelled, not crashed. Honest, replaceable — and it earns a hazard, because logs
    stream and whoever cancelled may have read the metric first."""
    g, d, a, _ = honest_attrition(g, d, a)
    a[2]["attestation"]["conclusion"] = "cancelled"
    return g, d, a, None


def unattested(g, d, a):
    """Ran bare-metal. #64 accepts a hand-entered environment block and marks it; here the
    attestation IS the ordering evidence, so its absence moves the register."""
    for acct in a:
        acct["attestation"] = None
    return g, d, a, None


def declared_register(g, d, a):
    d["register"] = "confirmatory"
    return g, d, a, None


def literal_seeds(g, d, a):
    d.pop("draw")
    d["seeds"] = [s["seed"] for s in a]
    return g, d, a, None


def no_attrition_policy(g, d, a):
    d.pop("attrition")
    return g, d, a, None


def no_declaration(g, d, a):
    return g, None, a, None


def freeze_after_declaration(g, d, a):
    """Declared the runs while still searching for the instrument."""
    g.parents["c_declare"] = ("c_charter",)
    g.parents["c_freeze"] = ("c_declare",)
    return g, d, a, None


# ---- the kind-(1) cases ---------------------------------------------------

RECORDS = [f"rec-{i:04d}" for i in range(200)]


def dataset_world(mutate=None):
    g, d, a = honest_world("2026-08-14-p7b2e4.declared.yaml")
    d["dataset"]["record_ids"] = RECORDS
    held = register.holdout(RECORDS, d["dataset"]["split"]["salt"],
                            d["dataset"]["split"]["fraction"])
    # What the search phase read: everything outside the hold-out. This is the honest case.
    prior = [r for r in RECORDS if r not in held]
    if mutate:
        g, d, a, prior = mutate(g, d, a, prior, held)
    return g, d, a, prior


def ds_clean(g, d, a, prior, held):
    return g, d, a, prior


def ds_no_holdout(g, d, a, prior, held):
    d["dataset"].pop("split")
    return g, d, a, RECORDS


def ds_enumerated_split(g, d, a, prior, held):
    d["dataset"]["split"] = {"rule": "listed", "records": sorted(held)[:50]}
    return g, d, a, prior


def ds_unpinned(g, d, a, prior, held):
    d["dataset"].pop("checksum")
    return g, d, a, prior


def ds_touched(g, d, a, prior, held):
    """The ordinary way this dies: an exploratory pass read the whole dataset."""
    return g, d, a, RECORDS


CASES = [
    ("0", "the declaration as written — six runs, all accounted", identity, None),
    ("t", "the TICKET'S rule satisfied: ran first, declared after", ticket_rule_satisfied, None),
    ("s", "six declared, one published — seed shopping", seed_shopping, None),
    ("r", "a seed the draw rule never produces", reroll, None),
    ("n", "a null filed as a failure", null_as_attrition, None),
    ("c", "an agent's own account of its own failure", agent_claimed_failure, None),
    ("a", "an OOM, replaced by the next seed in the stream", honest_attrition, None),
    ("x", "a cancelled run, replaced", cancelled, None),
    ("u", "no runner attestation at all", unattested, None),
    ("g", "the declaration asserts a register", declared_register, None),
    ("l", "seeds listed literally", literal_seeds, None),
    ("p", "no attrition policy declared", no_attrition_policy, None),
    ("z", "manifests citing no declaration", no_declaration, None),
    ("f", "runs declared before the instrument froze", freeze_after_declaration, None),
    ("D", "kind (1): a clean hold-out on a 2019 dataset", None, ds_clean),
    ("H", "kind (1): no hold-out at all", None, ds_no_holdout),
    ("E", "kind (1): the split enumerated rather than derived", None, ds_enumerated_split),
    ("P", "kind (1): the dataset unpinned", None, ds_unpinned),
    ("T", "kind (1): the hold-out already read during the search", None, ds_touched),
]


def run(key: str) -> None:
    label, mutate, ds = next((c[1], c[2], c[3]) for c in CASES if c[0] == key)

    if ds is not None:
        g, decl, accounts, prior = dataset_world(ds)
    else:
        g, decl, accounts = honest_world()
        g, decl, accounts, prior = mutate(g, copy.deepcopy(decl), accounts)

    print("\n" + "=" * 76)
    print(f"CASE {key} — {label}")
    print("=" * 76)

    v = register.derive(
        g,
        charter_commit="c_charter",
        freeze_commit="c_freeze",
        declaration=decl,
        declaration_commit="c_declare" if decl else None,
        accounts=accounts,
        prior_reads=prior,
    )
    subject = f"set {decl['set_id']}" if decl else "an undeclared set"
    print(register.render(v, subject=subject))
    print(f"\n  exit {v.exit_code}")


def main() -> None:
    print(__doc__)
    while True:
        print("\n" + "-" * 76)
        for k, label, *_ in CASES:
            print(f"  {k}  {label}")
        print("  all  run every case      q  quit")
        choice = input("\n> ").strip()
        if choice.lower() in ("q", "quit", ""):
            return
        if choice.lower() == "all":
            for k, *_ in CASES:
                run(k)
            continue
        if choice in {c[0] for c in CASES}:
            run(choice)
        else:
            print("  ?")


if __name__ == "__main__":
    main()
