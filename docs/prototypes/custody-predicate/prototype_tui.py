"""
PROTOTYPE (ticket #23) — throwaway TUI shell over custody.py.

Run:  python docs/prototypes/custody-predicate/prototype_tui.py

Flip through cases with [n]/[p], mutate the current case with the toggles at the
bottom, and watch which of §5's three candidate readings convicts it. Real cases
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
    POLICIES,
    STRANGER_CHECK,
    Commit,
    Endorsement,
    FileClass,
    Identity,
    Session,
    Verdict,
)

sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # § and ─ on Windows

B, D, R = "\x1b[1m", "\x1b[2m", "\x1b[0m"
COLOUR = {
    Verdict.PASS: "\x1b[32m",
    Verdict.VIOLATION: "\x1b[31m",
    Verdict.UNDECIDABLE: "\x1b[33m",
    Verdict.VACUOUS: "\x1b[2m",
}


# ---------------------------------------------------------------- real history

def real_cases() -> list[Commit]:
    """Every commit that has ever touched CONTEXT.md, as the checker would see
    it *today* — human name, agent trailer or not, no attendance signal."""
    repo = Path(__file__).resolve().parents[3]
    fmt = "%h%x1f%s%x1f%(trailers:key=Co-Authored-By,valueonly,separator=%x2C)"
    out = subprocess.run(
        ["git", "log", f"--format={fmt}", "--", "CONTEXT.md"],
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
            sha=sha,
        ))
    return cases


# ------------------------------------------------------------ synthetic cases

SYNTHETIC = [
    Commit("the case everyone agrees is a breach: unattended agent edits the vocabulary",
           "record:", FileClass.AUTHORED, Identity.AGENT_BOT, True,
           Session.UNATTENDED, Endorsement.ABSENT),
    Commit("the two record: commits, replayed post-#24 as they actually happened",
           "record:", FileClass.AUTHORED, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.PRESENT),
    Commit("§6 de minimis: human fixes a typo in CONTEXT.md, no agent involved",
           "record:", FileClass.AUTHORED, Identity.HUMAN, False,
           Session.ATTENDED, Endorsement.UNKNOWN),
    Commit("human types the vocabulary unaided but could not defend a word of it",
           "record:", FileClass.AUTHORED, Identity.HUMAN, False,
           Session.ATTENDED, Endorsement.ABSENT),
    Commit("agent writes a research document — custody follows the file, not the topic",
           "evidence:", FileClass.RECORD, Identity.AGENT_BOT, True,
           Session.UNATTENDED, Endorsement.ABSENT),
    Commit("a belt rung with no falsifier drafted",
           "belt:", FileClass.RECORD, Identity.HUMAN, True,
           Session.ATTENDED, Endorsement.ABSENT),
    Commit("agent commits the charter from an attended session, under its own identity",
           "core:", FileClass.AUTHORED, Identity.AGENT_BOT, True,
           Session.ATTENDED, Endorsement.PRESENT),
]


# ------------------------------------------------------------------ rendering

def cycle(seq, current, step=1):
    items = list(seq)
    return items[(items.index(current) + step) % len(items)]


def tally(policy, cases):
    counts = {v: 0 for v in Verdict}
    for c in cases:
        counts[policy(c).verdict] += 1
    return counts


def render(cases, idx, current, history):
    os.system("")  # enable ANSI on Windows terminals
    print("\x1b[2J\x1b[H", end="")
    c = current
    origin = f"real {c.sha}" if c.sha else "synthetic"

    print(f"{B}PROTOTYPE #23{R} {D}— what does §5 custody claim, and what checks it?{R}"
          f"{D}   case {idx + 1}/{len(cases)}{R}")
    print(D + "─" * 92 + R)
    print(f"{B}CASE{R}  {c.subject}  {D}[{origin}]{R}")
    for label, value, note in (
        ("file class", c.file_class.value, "CONTEXT.md / the charter"
            if c.file_class is FileClass.AUTHORED else ""),
        ("commit type", c.ctype, ""),
        ("author identity", c.identity.value,
            "agent worktrees inherit NGL321 (pre-#24)"
            if c.identity is Identity.HUMAN_UNVERIFIED else ""),
        ("agent co-author", "present" if c.agent_co_author else "absent", ""),
        ("session", c.session.value,
            "git carries no attendance signal" if c.session is Session.UNKNOWN else ""),
        ("endorsement", c.endorsement.value,
            "lives on the PR, not the commit" if c.endorsement is Endorsement.UNKNOWN else ""),
    ):
        print(f"      {label:<17}{B}{value:<20}{R}{D}{note}{R}")

    print(f"\n{B}VERDICTS{R}")
    for key, name, policy in POLICIES:
        r = policy(c)
        col = COLOUR[r.verdict]
        print(f"  {B}{key}{R} {name:<12}{col}{r.verdict.value:<14}{R}{D}{r.reason}{R}")

    print(f"\n{B}REAL HISTORY{R} {D}— every commit that has touched CONTEXT.md "
          f"({len(history)}){R}")
    for key, name, policy in POLICIES:
        counts = tally(policy, history)
        line = "  ".join(
            f"{COLOUR[v]}{counts[v]} {v.value.lower()}{R}"
            for v in Verdict if counts[v]
        )
        print(f"  {B}{key}{R} {name:<12}{line}")

    print(f"\n{B}CHECKABLE BY A STRANGER IN ONE COMMAND{R}")
    for _, name, _ in POLICIES:
        print(f"  {name:<12}{D}{STRANGER_CHECK[name]}{R}")

    print(f"\n{D}[n/p] case  [f] file  [c] type  [i] identity  [t] trailer  "
          f"[s] session  [e] endorsement  [r] reset  [q] quit{R}")


# --------------------------------------------------------------------- driver

def getkey() -> str:
    if os.name == "nt":
        import msvcrt
        return msvcrt.getwch().lower()
    import termios
    import tty
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1).lower()
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
        if k == "q":
            print()
            return
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
        elif k == "e":
            current = current.with_(endorsement=cycle(Endorsement, current.endorsement))


if __name__ == "__main__":
    main()
