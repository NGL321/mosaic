"""
PROTOTYPE (ticket #5) — throwaway TUI shell over record_form.py.

Run:  python docs/prototypes/record-form/prototype_tui.py
Dump: python docs/prototypes/record-form/prototype_tui.py --dump

Flip between the three schemes with [n]/[p] and switch pane with [1]-[4]. The
same real claims and the same five real debt items are rendered under each, so
the comparison is concrete. Nothing is written anywhere.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from record_form import (  # noqa: E402
    CLAIMS,
    DEBT,
    SCHEMES,
    Tier,
    tree_for,
)

# Windows consoles default to cp1252 and this prototype is full of box-drawing.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

W = 78
BAR = "═" * W
DASH = "─" * W


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def head(s, pane: str) -> str:
    panes = ["tree", "claim", "ledger", "verdict"]
    tabs = "  ".join(
        f"[{i + 1}]{p.upper()}" if p == pane else f" {i + 1} {p}" for i, p in enumerate(panes)
    )
    return (
        f"{BAR}\n"
        f" SCHEME {s.key} — {s.name}\n"
        f" {s.thesis}\n"
        f" truth lives: {s.truth_lives}\n"
        f"{DASH}\n"
        f" {tabs}\n"
        f"{BAR}"
    )


def pane_tree(s) -> str:
    return tree_for(s)


def pane_claim(s) -> str:
    out = [
        "HOW A TIER AND ITS DEBT APPEAR AT THE CLAIM SITE",
        "(the real Extraction entry, CONTEXT.md:106)",
        "",
        DASH,
        "TODAY:",
        "",
        "**Extraction**:",
        "How much of the predictive structure available in what an engine observes",
        "the engine actually captures ...",
        "",
        "        ...and 65 lines later, invisible in the rendered file:",
        "        <!-- Provenance Tier for Extraction and Closure:",
        "             machine-produced, unverified. ... Verification Debt. -->",
        "",
        DASH,
        f"UNDER SCHEME {s.key}:",
        "",
        s.claim_render,
    ]
    return "\n".join(out)


def pane_ledger(s) -> str:
    return f"WHERE THE FIVE REAL DEBT ITEMS LIVE — SCHEME {s.key}\n{DASH}\n\n{s.ledger_render}"


def pane_verdict(s) -> str:
    out = [f"SCHEME {s.key} — {s.name}", DASH, "", "BUYS"]
    out += [f"  + {b}" for b in s.buys]
    out += ["", "COSTS"]
    out += [f"  - {c}" for c in s.costs]
    out += ["", "ABANDONED BY MONTH TWO IF", f"  ! {s.kills_it}"]
    return "\n".join(out)


PANES = {"tree": pane_tree, "claim": pane_claim, "ledger": pane_ledger, "verdict": pane_verdict}
ORDER = ["tree", "claim", "ledger", "verdict"]


def tier_stress() -> str:
    out = [
        BAR,
        " TIER VOCABULARY — STRESS TEST AGAINST THE RECORD AS IT STANDS",
        BAR,
        "",
        "CONTEXT.md defines exactly three tiers. The record already uses four.",
        "",
    ]
    for t in Tier:
        mark = "  <-- NOT IN THE DEFINITION" if t is Tier.T2_AGENT else ""
        out.append(f"  {t.code:<4} {t.label:<42} {mark}")
    out += [
        "",
        DASH,
        "The fourth was written by hand at CONTEXT.md:232, four days after the",
        "three-tier definition landed:",
        "",
        '    "Provenance Tier: machine-produced, checked against primary sources."',
        "",
        "That is not T3 — it was checked, by #13, against primary documents. It is",
        "not T2 — Noah did not verify it; a different agent did. The vocabulary was",
        "under-specified on contact with its first real case, and the record has",
        "already voted with its feet.",
        "",
        "PROTOCOL.md §5 makes the same distinction load-bearing elsewhere: a checker",
        "agent must not be the producing agent. If agent-verification is good enough",
        "to gate a belt claim there, it is a tier here.",
        "",
        DASH,
        "Current census across the 5 real claims:",
        "",
    ]
    for t in Tier:
        n = sum(1 for c in CLAIMS if c.tier is t)
        out.append(f"  {t.code:<4} {t.label:<42} {n}")
    return "\n".join(out)


def claim_table() -> str:
    out = [
        BAR,
        " THE REAL CLAIMS AND WHERE THEIR TIER IS WRITTEN DOWN TODAY",
        BAR,
        "",
    ]
    for c in CLAIMS:
        out += [
            f"  {c.term}  ({c.site})   {c.tier.code}",
            f"    {c.text}",
            f"    debt: {', '.join(c.debt) or '—'}",
            f"    today: {c.current_form}",
            "",
        ]
    return "\n".join(out)


def debt_table() -> str:
    out = [
        BAR,
        " THE FIVE REAL DEBT ITEMS — ALL CURRENTLY INSIDE HTML COMMENTS",
        BAR,
        "",
    ]
    for d in DEBT:
        out += [
            f"  {d.id}  blocks: {', '.join(d.blocks)}",
            f"    {d.what}",
            f"    discharge:  {d.discharge}",
            f"    curriculum: {d.curriculum}",
            f"    logged at:  {d.source}",
            "",
        ]
    return "\n".join(out)


def dump() -> None:
    print(tier_stress())
    print()
    print(claim_table())
    print(debt_table())
    for s in SCHEMES:
        print(BAR)
        print(f" SCHEME {s.key} — {s.name}")
        print(f" {s.thesis}")
        print(BAR)
        for p in ORDER:
            print(f"\n### {p.upper()}\n")
            print(PANES[p](s))
        print()


def main() -> None:
    if "--dump" in sys.argv:
        dump()
        return
    i, pane = 0, "tree"
    while True:
        s = SCHEMES[i]
        clear()
        print(head(s, pane))
        print()
        print(PANES[pane](s))
        print()
        print(DASH)
        print(" [n]ext scheme  [p]rev  [1-4] pane  [t]ier stress  [c]laims  [d]ebt  [q]uit")
        try:
            k = input(" > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if k == "q":
            return
        if k == "n":
            i = (i + 1) % len(SCHEMES)
        elif k == "p":
            i = (i - 1) % len(SCHEMES)
        elif k in {"1", "2", "3", "4"}:
            pane = ORDER[int(k) - 1]
        elif k in {"t", "c", "d"}:
            clear()
            print({"t": tier_stress, "c": claim_table, "d": debt_table}[k]())
            input("\n [enter] ")


if __name__ == "__main__":
    main()
