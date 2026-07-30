"""
PROTOTYPE (ticket #26) — throwaway TUI shell over contract.py.

Run:   python docs/prototypes/research-contract/prototype_tui.py
Dump:  python docs/prototypes/research-contract/prototype_tui.py --dump

The question: what must a research-track document contain to be mergeable?

The corpus is the four documents that actually exist — the #4 survey, the #13 citation
verification, the #14 individuation question, the #27 cost basis — plus the #4 survey
rewritten into the proposed contract. Toggling a rule off with [1]-[9]/[a]-[f] and
watching which documents flip is how you find out whether a constraint bites or is
ceremony: a rule every document already passes is describing the corpus, and a rule
every document fails is either the finding or the overreach.

Nothing is written anywhere.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from contract import RULES, census, evaluate, parse  # noqa: E402

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

HERE = Path(__file__).parent
REPO = HERE.parents[2]

W = 88
BAR = "=" * W
DASH = "-" * W

CORPUS = [
    ("#4  survey (as written)", HERE / "inputs" / "2026-07-25-grokking-eca-tda-survey.md"),
    ("#4  survey (REWRITTEN)", HERE / "rewrite-2026-07-25-grokking-eca-tda-survey.md"),
    ("#13 citation verification", REPO / "docs/research/2026-07-28-verifying-cited-influences.md"),
    ("#14 individuation question", REPO / "docs/research/2026-07-28-markov-blanket-individuation.md"),
    ("#27 cost and quota basis", REPO / "docs/research/2026-07-29-automation-cost-and-quota-basis.md"),
]

KEYS = "123456789abcdef"  # one per rule, in order


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def load():
    docs = []
    for name, path in CORPUS:
        if not path.exists():
            docs.append(parse(name + "  [MISSING]", ""))
            continue
        docs.append(parse(name, path.read_text(encoding="utf-8")))
    return docs


def mark(passed: bool, severity: str, checked_by: str = "ci") -> str:
    if checked_by == "human":
        return " hum"
    if passed:
        return " ok "
    return "FAIL" if severity == "blocking" else "warn"


def grid(docs) -> str:
    """Every rule against every document. The whole state, one screen."""
    reports = [evaluate(d) for d in docs]
    head = f"{'':<38}" + "".join(f"{i + 1:>8}" for i in range(len(docs)))
    lines = [head, f"{'':<38}" + "".join(f"{d.name.split()[0]:>8}" for d in docs), DASH]
    for i, rule in enumerate(RULES):
        if not rule.enabled:
            label = f"[{KEYS[i]}] {rule.id} {rule.title[:28]}"
            lines.append(f"\x1b[2m{label:<38}" + "".join(f"{'  off':>8}" for _ in docs) + "\x1b[0m")
            continue
        label = f"[{KEYS[i]}] {rule.id} {rule.title[:28]}"
        cells = ""
        for rep in reports:
            r = next(x for x in rep.results if x.rule.id == rule.id)
            cells += f"{mark(r.passed, rule.severity, rule.checked_by):>8}"
        lines.append(f"{label:<38}{cells}")
    lines.append(DASH)
    verdict = ""
    for rep in reports:
        verdict += f"{('pass' if rep.passes_ci else 'BLOCK'):>8}"
    lines.append(f"{'CI GATE':<38}{verdict}")
    lines.append(f"{'HUMAN GATE (R14, R15)':<38}" + "".join(f"{'open':>8}" for _ in reports))
    lines.append("")
    lines.append("  1 " + docs[0].name + "        2 " + docs[1].name)
    for i, d in enumerate(docs[2:], start=3):
        lines.append(f"  {i} {d.name}")
    return "\n".join(lines)


def detail(doc) -> str:
    rep = evaluate(doc)
    out = [f"{doc.name}", DASH, ""]
    out.append("FRONT MATTER")
    out.append("  " + (", ".join(f"{k}={v}" for k, v in doc.front.items()) if doc.front else "(none)"))
    out.append("")
    out.append("CENSUS")
    for k, v in census(doc).items():
        out.append(f"  {k:<20} {v}")
    out.append("")
    out.append("SECTIONS (##)")
    for s in doc.top_sections:
        vs = ",".join(sorted(set(s.verdicts))) or "-"
        out.append(f"  {s.title[:56]:<58} verdicts={vs[:20]:<20} links={len(s.links)}")
    out.append("")
    out.append("RULES")
    for r in rep.results:
        out.append(f"  {mark(r.passed, r.rule.severity, r.rule.checked_by)}  {r.rule.id:<4} "
                   f"{r.rule.title[:34]:<36} {r.rule.checked_by:<6} {r.evidence[:60]}")
    out.append("")
    out.append(f"  -> CI GATE {'PASS' if rep.passes_ci else 'BLOCK'}  "
               f"({len(rep.ci_failures)} blocking, {len(rep.advisory_failures)} advisory); "
               f"human gate always open")
    return "\n".join(out)


def rule_book() -> str:
    out = ["WHY EACH RULE EXISTS", DASH]
    for i, r in enumerate(RULES):
        state = "" if r.enabled else "  (disabled)"
        out.append(f"[{KEYS[i]}] {r.id} {r.title}  [{r.severity}/{r.checked_by}]{state}")
        out.append(f"     {r.why}")
    return "\n".join(out)


def bite(docs) -> str:
    """
    Which rules earn their place. A rule nothing fails is describing the corpus; a rule
    everything fails is either the finding or the overreach. Only the middle discriminates.
    """
    reports = [evaluate(d) for d in docs]
    out = ["DOES THE CONSTRAINT BITE?", DASH,
           f"{'rule':<38}{'fails':>7}{'of':>4}   reading", ""]
    n = len(docs)
    for rule in RULES:
        if not rule.enabled:
            out.append(f"{rule.id + ' ' + rule.title[:32]:<38}{'-':>7}{n:>4}   toggled off")
            continue
        if rule.checked_by == "human":
            out.append(f"{rule.id + ' ' + rule.title[:32]:<38}{'-':>7}{n:>4}   "
                       "human — no predicate, listed so CI is not mistaken for the gate")
            continue
        fails = sum(1 for rep in reports
                    if not next(x for x in rep.results if x.rule.id == rule.id).passed)
        if fails == 0:
            reading = "already universal — codifies practice"
        elif fails == n:
            reading = "nothing passes — the finding, or overreach"
        elif fails == n - 1:
            reading = "only the rewrite passes — the contract's content"
        else:
            reading = "discriminates within the corpus"
        out.append(f"{rule.id + ' ' + rule.title[:32]:<38}{fails:>7}{n:>4}   {reading}")
    return "\n".join(out)


def dump(docs) -> None:
    print(BAR)
    print(" RESEARCH-OUTPUT DOCUMENT CONTRACT — PROTOTYPE FOR #26")
    print(BAR)
    print()
    print(grid(docs))
    print()
    print(bite(docs))
    print()
    for d in docs:
        print()
        print(BAR)
        print(detail(d))


def main() -> None:
    docs = load()
    if "--dump" in sys.argv:
        dump(docs)
        return
    view, sel = "grid", 0
    while True:
        clear()
        print(BAR)
        print(" RESEARCH-OUTPUT DOCUMENT CONTRACT — PROTOTYPE FOR #26")
        print(" the four real research documents, plus the #4 survey rewritten into the contract")
        print(BAR)
        print()
        if view == "grid":
            print(grid(docs))
        elif view == "detail":
            print(detail(docs[sel]))
        elif view == "why":
            print(rule_book())
        else:
            print(bite(docs))
        print()
        print(DASH)
        print(" [g]rid  [d]etail <n>  [w]hy  [b]ite  [1-9a-f] toggle rule  [r]eset  [q]uit")
        try:
            k = input(" > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if k == "q":
            return
        if k == "g":
            view = "grid"
        elif k == "w":
            view = "why"
        elif k == "b":
            view = "bite"
        elif k == "r":
            for r in RULES:
                r.enabled = True
        elif k.startswith("d"):
            rest = k[1:].strip()
            if rest.isdigit() and 1 <= int(rest) <= len(docs):
                sel = int(rest) - 1
            view = "detail"
        elif len(k) == 1 and k in KEYS[: len(RULES)]:
            r = RULES[KEYS.index(k)]
            r.enabled = not r.enabled


if __name__ == "__main__":
    main()
