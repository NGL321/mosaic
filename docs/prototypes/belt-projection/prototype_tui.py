"""
PROTOTYPE (ticket #90) — driven TUI over projection.py.

Run:  python docs/prototypes/belt-projection/prototype_tui.py

[1-5] inject an event  [m] MAJOR  [r] reset  [q] quit

Every event is a write to something that already exists — an `axiom.md` line, or a
`CHARTER.md` edit in Noah's hand. Nothing writes to a belt-graph store, because there
isn't one. That is the thing being tested.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from projection import Condition, build, chart  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

B, D, R = "\x1b[1m", "\x1b[2m", "\x1b[0m"
RED, YEL, GRN, CYA, MAG = "\x1b[31m", "\x1b[33m", "\x1b[32m", "\x1b[36m", "\x1b[35m"
COND = {Condition.CONJECTURE: D, Condition.ELIGIBLE: CYA, Condition.BELT: GRN}

I172 = "inquiries/172-formation-signature-grokking"
I178 = "inquiries/178-trajectory-invariance"
I181 = "inquiries/181-schema-count-stability"
C051 = "conjectures/051-topology-carries-no-content"


def initial_state() -> dict:
    """Ledgers as the fixture's committed axiom.md files have them, plus the set of
    rungs currently in CHARTER.md. Both are real files in the real thing."""
    return {
        "ledgers": {
            I172: [{"event": "carried", "at": "2026-08-20"}],
            I178: [{"event": "carried", "at": "2026-08-22"}],
            I181: [],
        },
        "retired_rungs": set(),
        "series": [("v0.7.0", None), ("v0.10.0", None)],
    }


def project(state: dict):
    p = build(ledgers=state["ledgers"])
    for node in p.nodes.values():
        if node.id in state["retired_rungs"]:
            node.rung = None
    return p


# -- the events -------------------------------------------------------------


def ev_1(s: dict) -> str:
    s["ledgers"][I172].append(
        {
            "event": "retracted",
            "route": "rule-dictated",
            "why": "replication run failed the frozen decision_rule (6 of 10 seeds)",
        }
    )
    return (
        "ONE line appended to inquiries/172/axiom.md. It killed legs on TWO "
        "conjectures — 043 survives on 178, 051 has nothing left."
    )


def ev_2(s: dict) -> str:
    s["retired_rungs"].add(C051)
    return (
        "Noah edits CHARTER.md and retires 051's rung. Until this commit the rung "
        "stood with no live leg — the cascade stopped at the projection."
    )


def ev_3(s: dict) -> str:
    s["ledgers"][I178].append(
        {
            "event": "hazard",
            "name": "architecture_pair_is_not_a_sample",
            "late": True,
        }
    )
    return (
        "A late untestable hazard, appended to 178's ledger — the charter is frozen "
        "at open and cannot take it. #9: obliges a corroboration Inquiry, retires "
        "nothing."
    )


def ev_4(s: dict) -> str:
    s["ledgers"][I181] = [{"event": "carried", "at": "2026-09-02"}]
    return "181 carries. 043 gains a third leg, in a second domain (synthetic)."


def ev_5(s: dict) -> str:
    s["ledgers"][I178].append(
        {
            "event": "retracted",
            "route": "discretionary",
            "why": "the declared hazard bit: the architecture pair was the effect",
        }
    )
    return "Discretionary retraction of 178. Noah's, and it owes a full defence."


EVENTS = [ev_1, ev_2, ev_3, ev_4, ev_5]
LABELS = [
    "172's axiom retracted (rule-dictated: replication failed)",
    "Noah retires 051's rung in CHARTER.md",
    "late untestable hazard on 178",
    "181 carries — 043 gains a third leg",
    "178's axiom retracted (discretionary: the hazard bit)",
]


def ev_major(s: dict) -> str:
    s["retired_rungs"] |= {n for n in build(ledgers=s["ledgers"]).nodes}
    return (
        "MAJOR. Every rung leaves CHARTER.md, blanket. NOT ONE axiom.md line "
        "changes — every leg is retained, which is what makes the rebuild a "
        "re-validation rather than a re-run."
    )


# -- render -----------------------------------------------------------------


def render(state: dict, msg: str, done: set) -> None:
    p = project(state)
    print("\x1b[2J\x1b[H", end="")
    print(f"{B}PROTOTYPE #90 — the belt graph as a projection{R}")
    print(f"{D}no belt-graph store exists; everything below is computed{R}\n")

    print(f"{B}Nodes{R}  {D}(condition derived: rung → belt, live leg → eligible){R}")
    for node in p.nodes.values():
        legs = "".join(
            ("!" if leg.hazardous else "|") if leg.alive else "x" for leg in node.legs
        )
        tags = []
        if node.dead:
            tags.append(f"{RED}dead{R}")
        if node.barred:
            tags.append(f"{YEL}barred{R}")
        if node.rung:
            tags.append(f"{GRN}rung/{node.rung['relevance']}{R}")
        print(
            f"  {COND[node.condition]}{node.condition.value:<10}{R} "
            f"{Path(node.id).name:<34} {MAG}{legs:<4}{R} "
            f"{D}{node.statement[:44]}{R} {' '.join(tags)}"
        )

    print(f"\n{B}Legs{R}  {D}(derived from axiom.md × the charter's conjectures: list){R}")
    for node in p.nodes.values():
        for leg in node.legs:
            state_s = f"{GRN}live{R}" if leg.alive else f"{RED}dead{R}"
            extra = f" {D}{leg.route}: {leg.died}{R}" if not leg.alive else ""
            haz = f" {YEL}⚠{len(leg.hazards)}{R}" if leg.hazards else ""
            print(
                f"  {state_s}  {Path(leg.inquiry).name:<32} → "
                f"{Path(leg.conjecture).name:<34} {D}{leg.domain}{R}{haz}{extra}"
            )

    print(f"\n{B}Readings{R}")
    for name, reading in p.readings().items():
        colour = D if reading.value is None else ""
        note = f"  {RED}← {reading.blocked[:64]}{R}" if reading.blocked else ""
        print(f"  {colour}{name:<26} {str(reading):>12}{R}{note}")
    idx = p.index()
    print(f"  {B}{'INDEX':<26} {('—' if idx is None else f'{idx:+.2f}'):>12}{R}")

    print()
    print(chart(state["series"]))
    print()
    for i, label in enumerate(LABELS, 1):
        mark = f"{GRN}✓{R}" if i in done else " "
        print(f"  {mark} [{i}] {D}{label}{R}")
    if msg:
        print(f"\n{YEL}» {msg}{R}")
    print(f"\n{D}[1-5] event  [m] MAJOR  [r] reset  [q] quit{R}")


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


def main() -> None:
    state, msg, done = initial_state(), "", set()
    while True:
        render(state, msg, done)
        key = getkey()
        msg = ""
        if key == "q":
            print()
            return
        if key == "r":
            state, done = initial_state(), set()
        elif key == "m":
            msg = ev_major(state)
        elif key.isdigit() and 1 <= int(key) <= len(EVENTS):
            n = int(key)
            msg = EVENTS[n - 1](state)
            done.add(n)


if __name__ == "__main__":
    main()
