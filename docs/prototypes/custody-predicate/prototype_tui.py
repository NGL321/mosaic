"""
PROTOTYPE (ticket #23) — throwaway TUI shell over custody.py.

Run:  python docs/prototypes/custody-predicate/prototype_tui.py

Flip through cases with [n]/[p], mutate the current case with the toggles at the
bottom, and watch which of §5's candidate readings convicts it — and, in the
right-hand column, whether that verdict actually tracks what happened. Real cases
are loaded from this repository's own CONTEXT.md history at startup (read-only);
everything else is in memory and nothing is written anywhere.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from custody import (  # noqa: E402
    FLOOR,
    POLICIES,
    PROGRAMME,
    STRANGER_CHECK,
    Commit,
    Defence,
    Endorsement,
    FileClass,
    Identity,
    Session,
    Verdict,
    may_ratify,
    soundness,
)

sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # § and ─ on Windows

B, D, R = "\x1b[1m", "\x1b[2m", "\x1b[0m"
COLOUR = {
    Verdict.PASS: "\x1b[32m",
    Verdict.VIOLATION: "\x1b[31m",
    Verdict.UNDECIDABLE: "\x1b[33m",
    Verdict.VACUOUS: "\x1b[2m",
    Verdict.DEFERRED: "\x1b[36m",
}
SCORE_COLOUR = {
    "SOUND": "\x1b[32m",
    "FOOLED": "\x1b[31;1m",
    "OVERSTRICT": "\x1b[35m",
    "SILENT": "\x1b[2m",
    "DEFERRED": "\x1b[36m",
}


# ---------------------------------------------------------------- real history

def real_cases() -> list[Commit]:
    """Every commit that has touched CONTEXT.md, as a checker sees it today —
    human name, agent trailer or not, no attendance signal, no defence on file.

    `--all`, not `main`: the two record: commits that landed the vocabulary are
    still on grilling/research-vocabulary, and they are the cases in question."""
    repo = Path(__file__).resolve().parents[3]
    fmt = "%h%x1f%s%x1f%(trailers:key=Co-Authored-By,valueonly,separator=%x2C)"
    out = subprocess.run(
        ["git", "log", "--all", f"--format={fmt}", "--", "CONTEXT.md"],
        cwd=repo, capture_output=True, text=True, check=True,
    ).stdout
    cases = []
    for line in reversed([l for l in out.splitlines() if l.strip()]):
        sha, subject, trailers = line.split("\x1f")
        cases.append(Commit(
            subject=subject,
            ctype=subject.split(":")[0] + ":",
            file_class=FileClass.AUTHORED,
            identity=Identity.HUMAN_UNVERIFIED,
            agent_co_author=bool(trailers.strip()),
            mechanism_available=False,  # pre-#24, pre-archive-citation: unrecordable
            sha=sha,
        ))
    return cases


# ------------------------------------------------------------ synthetic cases

SYNTHETIC = [
    Commit("the case everyone agrees is a breach: unattended agent edits the vocabulary",
           "record:", FileClass.AUTHORED, Identity.AGENT_BOT, True,
           Session.UNATTENDED, Endorsement.ABSENT, Defence.ABSENT,
           truly_attended=False, truly_defensible=False),

    Commit("THE ONE TO PROTECT: convoluted idea made concrete, monitored, cited, defended",
           "record:", FileClass.AUTHORED, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.PRESENT, Defence.DEFENDED,
           session_cited=True),

    Commit("THE ONE TO CATCH: human typed every character and can only recite it",
           "record:", FileClass.AUTHORED, Identity.HUMAN, False,
           Session.ATTENDED, Endorsement.UNKNOWN, Defence.RECITED,
           truly_defensible=False),

    Commit("same, but co-authored — identical hollowness, different trailer",
           "record:", FileClass.AUTHORED, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.UNKNOWN, Defence.RECITED,
           session_cited=True, truly_defensible=False),

    Commit("Extraction / Closure: landed with Verification Debt logged against them",
           "record:", FileClass.AUTHORED, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.UNKNOWN, Defence.UNKNOWN,
           session_cited=True, truly_defensible=False),

    Commit("the ceremony test: 'attended' asserted by the one party whose attendance is at issue",
           "record:", FileClass.AUTHORED, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.PRESENT, Defence.DEFENDED,
           session_cited=True, truly_attended=False),

    Commit("§6 de minimis: human fixes a misspelt name in CONTEXT.md",
           "record:", FileClass.AUTHORED, Identity.HUMAN, False,
           Session.ATTENDED, Endorsement.UNKNOWN, Defence.ABSENT,
           de_minimis=True),

    Commit("agent writes a research document — custody follows the file, not the topic",
           "evidence:", FileClass.RECORD, Identity.AGENT_BOT, True,
           Session.UNATTENDED, Endorsement.ABSENT, Defence.ABSENT),

    Commit("a belt rung with no falsifier drafted",
           "belt:", FileClass.RECORD, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.ABSENT, Defence.ABSENT,
           truly_defensible=False),

    Commit("amanuensis edit with no Session: trailer — nothing to trace the influence to",
           "record:", FileClass.AUTHORED, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.PRESENT, Defence.DEFENDED,
           session_cited=False),
]


# ------------------------------------------------------------------ rendering

def cycle(seq, current, step=1):
    items = list(seq)
    return items[(items.index(current) + step) % len(items)]


def clip(s, n):
    return s if len(s) <= n else s[: n - 1] + "…"


def tally(policy, cases):
    counts = {v: 0 for v in Verdict}
    for c in cases:
        counts[policy(c).verdict] += 1
    return counts


def render(cases, idx, c, history):
    os.system("")  # enable ANSI on Windows terminals
    print("\x1b[2J\x1b[H", end="")
    origin = f"real {c.sha}" if c.sha else "synthetic"

    print(f"{B}PROTOTYPE #23{R} {D}— what does §5 custody claim, and what checks it?{R}"
          f"{D}   case {idx + 1}/{len(cases)}{R}")
    print(D + "─" * 96 + R)
    print(f"{B}CASE{R} {clip(c.subject, 78)} {D}[{origin}]{R}")

    left = [
        ("file class", c.file_class.value),
        ("commit type", c.ctype),
        ("identity", c.identity.value),
        ("agent co-author", "present" if c.agent_co_author else "absent"),
    ]
    right = [
        ("session", c.session.value),
        ("session cited", "yes" if c.session_cited else "no"),
        ("defence", c.defence.value),
        ("de minimis / mech", f"{'yes' if c.de_minimis else 'no'}"
            f" / {'available' if c.mechanism_available else 'ABSENT'}"),
    ]
    for (ll, lv), (rl, rv) in zip(left, right):
        print(f"     {ll:<16}{B}{lv:<19}{R}{ll and ''}{rl:<18}{B}{rv}{R}")

    verdict = "LEGITIMATE" if c.legitimate else "ILLEGITIMATE"
    col = "\x1b[32m" if c.legitimate else "\x1b[31m"
    print(f"     {D}ground truth     {R}attended {B}{'yes' if c.truly_attended else 'no':<4}{R}"
          f" defensible {B}{'yes' if c.truly_defensible else 'no':<4}{R} → {col}{verdict}{R}"
          f" {D}(unreadable by any checker){R}")

    print(f"\n{B}VERDICTS{R}{D}{'vs ground truth':>88}{R}")
    for key, name, policy in POLICIES:
        r = policy(c)
        score, _ = soundness(policy, c)
        print(f"  {B}{key}{R} {name:<14}{COLOUR[r.verdict]}{r.verdict.value:<13}{R}"
              f"{D}{clip(r.reason, 55):<56}{R}{SCORE_COLOUR[score]}{score}{R}")

    print(f"{B}REAL HISTORY{R} {D}— every commit that has touched CONTEXT.md "
          f"({len(history)}){R}")
    for key, name, policy in POLICIES:
        counts = tally(policy, history)
        line = "  ".join(f"{COLOUR[v]}{counts[v]} {v.value.lower()}{R}"
                         for v in Verdict if counts[v])
        print(f"  {B}{key}{R} {name:<14}{line}")

    floor = (f"{B}declared{R}" if FLOOR["declared"]
             else "\x1b[33mnot declared — D cannot rule until it is\x1b[0m")
    era = ("\x1b[36mpre-charter (0.x) — grace live\x1b[0m" if PROGRAMME["pre_charter"]
           else f"{B}charter ratified — grace spent{R}")
    print(f"{B}FLOOR{R} {floor}   {B}ERA{R} {era}")

    gate = may_ratify(cases)
    print(f"{B}CHARTER GATE{R} may tag research-v1.0.0? "
          f"{COLOUR[gate.verdict]}{'yes' if gate.verdict is Verdict.PASS else 'no'}{R}"
          f" {D}— {gate.reason}{R}")

    print(f"\n{B}CHECKABLE BY A STRANGER{R}")
    for _, name, _ in POLICIES:
        print(f"  {name:<14}{D}{clip(STRANGER_CHECK[name], 88)}{R}")

    print(f"\n{D}[n/p] case  [f] file  [c] type  [i] identity  [t] trailer  [s] session"
          f"  [x] citation  [d] defence  [m] de minimis  [e] endorsement{R}")
    print(f"{D}[1] attended  [2] defensible  [3] mechanism  [F] floor  [G] ratify charter"
          f"  [r] reset  [q] quit{R}")


# --------------------------------------------------------------------- driver

def getkey() -> str:
    if os.name == "nt":
        import msvcrt
        return msvcrt.getwch()
    import termios
    import tty
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


TYPES = ("record:", "evidence:", "belt:", "core:", "feat:", "fix:", "chore:")


def main() -> None:
    history = real_cases()
    cases = history + SYNTHETIC
    idx, current = 0, cases[0]

    while True:
        render(cases, idx, current, history)
        k = getkey()
        if k in "qQ":
            print()
            return
        if k == "F":
            FLOOR["declared"] = not FLOOR["declared"]
            continue
        if k == "G":
            PROGRAMME["pre_charter"] = not PROGRAMME["pre_charter"]
            continue
        k = k.lower()
        if k in "np":
            idx = (idx + (1 if k == "n" else -1)) % len(cases)
            current = cases[idx]
        elif k == "r":
            current = cases[idx]
        elif k == "f":
            current = current.with_(file_class=cycle(FileClass, current.file_class))
        elif k == "c":
            current = current.with_(ctype=cycle(TYPES, current.ctype))
        elif k == "i":
            current = current.with_(identity=cycle(Identity, current.identity))
        elif k == "t":
            current = current.with_(agent_co_author=not current.agent_co_author)
        elif k == "s":
            current = current.with_(session=cycle(Session, current.session))
        elif k == "x":
            current = current.with_(session_cited=not current.session_cited)
        elif k == "d":
            current = current.with_(defence=cycle(Defence, current.defence))
        elif k == "m":
            current = current.with_(de_minimis=not current.de_minimis)
        elif k == "e":
            current = current.with_(endorsement=cycle(Endorsement, current.endorsement))
        elif k == "1":
            current = current.with_(truly_attended=not current.truly_attended)
        elif k == "2":
            current = current.with_(truly_defensible=not current.truly_defensible)
        elif k == "3":
            current = current.with_(mechanism_available=not current.mechanism_available)


if __name__ == "__main__":
    main()
