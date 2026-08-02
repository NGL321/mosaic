"""
PROTOTYPE (ticket #90) — throwaway TUI over graph.py.

Run:  python docs/prototypes/belt-graph/prototype_tui.py

[s] cycles the store renderer (issues / files / hybrid).
[1..7] steps the programme forward through events the record actually implies.
[m] fires a MAJOR. [h] attaches a retroactive hazard. [r] resets.

Everything is in memory; nothing touches GitHub, git, or disk.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from graph import (  # noqa: E402
    Condition,
    Graph,
    Hazard,
    Leg,
    LegKind,
    Node,
    Relevance,
    Release,
    as_files,
    as_hybrid,
    as_issues,
    chart,
    config_sha,
    seed,
)

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

B, D, R = "\x1b[1m", "\x1b[2m", "\x1b[0m"
RED, YEL, GRN, CYA, MAG = ("\x1b[31m", "\x1b[33m", "\x1b[32m", "\x1b[36m", "\x1b[35m")

COND_COLOUR = {
    Condition.CONJECTURE: D,
    Condition.ELIGIBLE: CYA,
    Condition.BELT: GRN,
}
STORES = [("issues", as_issues), ("files", as_files), ("hybrid", as_hybrid)]


def getkey() -> str:
    try:
        import msvcrt

        return msvcrt.getch().decode(errors="ignore").lower()
    except ImportError:
        import termios
        import tty

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


# -- the scripted future ----------------------------------------------------
# Not predictions. Each step is the *cheapest* event that exercises one rule #9
# fixed, so the store gets asked the question the store has to answer.


def step_1(g: Graph) -> str:
    g.releases.append(
        Release("0.6.0", "PATCH", "evidence: individuation stability sweep",
                evidence_for="individuation")
    )
    g.earn(
        "individuation",
        Leg(
            LegKind.SURVIVAL,
            domain="synthetic",
            inquiry="I-1",
            hazards=[],
        ),
    )
    g.snapshot()
    return "I-1 measured; individuation survived its falsifier on synthetic data"


def step_2(g: Graph) -> str:
    return g.admit("individuation", Relevance.CONNECTIVE, "0.7.0")


def step_3(g: Graph) -> str:
    g.releases.append(
        Release("0.8.0", "PATCH", "evidence: individuation on Allen Institute data",
                evidence_for="individuation")
    )
    g.earn(
        "individuation",
        Leg(
            LegKind.SURVIVAL,
            domain="neuro",
            inquiry="I-2",
            hazards=[
                Hazard(
                    "Recording coverage is a fraction of the population; "
                    "unobserved units cannot be excluded as schema members.",
                    source="I-2 charter",
                )
            ],
        ),
    )
    g.snapshot()
    return "second survival leg, in a second domain — this is cross-domain "\
           "robustness with no new vocabulary, and it carries a hazard"


def step_4(g: Graph) -> str:
    g.post(
        Node(
            "no-topological-signature",
            "Persistent homology on grokking representations carries no "
            "predictive content beyond effective rank.",
            Condition.CONJECTURE,
            posted_in="#4 → I-3",
            falsifier="A filtration whose residual beats effective rank at "
            "matched compute.",
            supports=["individuation"],
        )
    )
    g.releases.append(
        Release("0.9.0", "PATCH", "evidence: reduction check, null result",
                evidence_for="no-topological-signature")
    )
    g.earn(
        "no-topological-signature",
        Leg(LegKind.SURVIVAL, domain="ml", inquiry="I-3"),
    )
    g.snapshot()
    return "a negative result earns a leg — the eliminative clause is what "\
           "keeps it admissible instead of buried in a branch state"


def step_5(g: Graph) -> str:
    return g.admit("no-topological-signature", Relevance.ELIMINATIVE, "0.10.0")


def step_6(g: Graph) -> str:
    g.earn(
        "individuation",
        Leg(
            LegKind.DERIVATION,
            domain="mathematics",
            inquiry=None,
            through="core.schema-thesis",
        ),
    )
    g.snapshot()
    return "a derivation leg closes a path to the core — the disjunction is "\
           "now load-bearing on this node"


def step_7(g: Graph) -> str:
    g.releases.append(Release("0.11.0", "MINOR", "demote individuation's neuro leg"))
    out = g.kill_leg("individuation", 1, "replication failed on a second session")
    g.snapshot()
    return out


STEPS = [step_1, step_2, step_3, step_4, step_5, step_6, step_7]


def history(g: Graph) -> list[tuple[str, float | None]]:
    return g.snapshots


def render(g: Graph, store: int, msg: str, done: int) -> None:
    print("\x1b[2J\x1b[H", end="")
    print(f"{B}PROTOTYPE #90 — where the Protective Belt graph lives{R}")
    print(f"{D}store renderer: {B}{STORES[store][0]}{R}{D}   "
          f"content sha: {config_sha(g)}   steps taken: {done}/{len(STEPS)}{R}")
    print()

    print(f"{B}The graph{R}")
    for node in g.nodes.values():
        colour = COND_COLOUR[node.condition]
        legs = "".join(
            ("!" if leg.hazardous else "|") if leg.alive else "x" for leg in node.legs
        )
        bar = node.barred and f" {RED}barred{R}" or ""
        print(
            f"  {colour}{node.condition.value:<10}{R} {node.id:<26} "
            f"{MAG}{legs:<4}{R} {D}{node.statement[:52]}{R}{bar}"
        )
    print()

    print(chart(g, history(g)))
    print()

    if msg:
        print(f"{YEL}» {msg}{R}")
        print()

    print(STORES[store][1](g)[:1600])
    print()
    print(f"{D}[s] store  [1-7] step  [m] MAJOR  [h] late hazard  [r] reset  [q] quit{R}")


def main() -> None:
    g, store, msg, done = seed(), 1, "", 0
    while True:
        render(g, store, msg, done)
        key = getkey()
        msg = ""
        if key == "q":
            print()
            return
        if key == "s":
            store = (store + 1) % len(STORES)
        elif key == "r":
            g, done = seed(), 0
        elif key == "m":
            msg = g.major("1.0.0", "the schema thesis is abandoned")
        elif key == "h":
            if g.nodes["individuation"].legs:
                msg = g.attach_hazard(
                    "individuation",
                    0,
                    Hazard(
                        "The synthetic generator's ground truth is itself a "
                        "schema decomposition — the instrument may be scoring "
                        "its own prior.",
                        source="post-freeze review",
                        retroactive=True,
                    ),
                )
            else:
                msg = "no leg to hazard yet — take step 1 first"
        elif key.isdigit() and 1 <= int(key) <= len(STEPS):
            n = int(key)
            if n != done + 1:
                msg = f"steps are ordered; take {done + 1} next"
            else:
                msg = STEPS[n - 1](g)
                done = n


if __name__ == "__main__":
    main()
