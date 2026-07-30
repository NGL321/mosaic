#!/usr/bin/env python3
"""Check §5's custody obligations over the commits a pull request adds.

Two of the three obligations are mechanical, and only those are checked here:

  IDENTITY  an authored file is committed under a human identity.
  CITATION  an agent co-author on an authored file carries a `Session:` trailer.

The third — DEFENCE — is not CI's to judge. A defence artifact is grilled by a
checker agent on the pull request thread (§6), so this script reports the
obligation and does not pretend to verify it.

Only commits the pull request *adds* are checked, which is what implements §2's
pre-charter grace correctly: history that predates a mechanism is deferred, not
re-litigated on every run. Nothing here reaches backwards.

Usage:  custody_check.py <base-sha> <head-sha>
"""

from __future__ import annotations

import subprocess
import sys

# §5's authored files. Custody follows the file, never the topic.
AUTHORED = {"CONTEXT.md", "CHARTER.md"}

# Identities that are agents. Empty until #24 gives agents their own identity —
# until then the IDENTITY obligation is undecidable rather than satisfied, and
# this script says so instead of passing silently.
AGENT_IDENTITIES: set[str] = set()

AGENT_CO_AUTHOR_MARKERS = ("claude", "gpt-", "copilot", "gemini", "[bot]")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          check=True).stdout.strip()


def commits(base: str, head: str) -> list[str]:
    out = git("rev-list", "--no-merges", f"{base}..{head}")
    return out.splitlines() if out else []


def authored_files_touched(sha: str) -> list[str]:
    files = git("show", "--name-only", "--format=", sha).splitlines()
    return [f for f in files if f in AUTHORED]


def trailers(sha: str) -> dict[str, list[str]]:
    body = git("show", "-s", "--format=%B", sha)
    found: dict[str, list[str]] = {}
    for line in body.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            if key and " " not in key.strip():
                found.setdefault(key.strip().lower(), []).append(value.strip())
    return found


def main() -> int:
    base, head = sys.argv[1], sys.argv[2]
    problems: list[str] = []
    obligations: list[str] = []
    undecidable: list[str] = []

    for sha in commits(base, head):
        touched = authored_files_touched(sha)
        if not touched:
            continue

        short = git("show", "-s", "--format=%h %s", sha)
        author = git("show", "-s", "--format=%an", sha)
        tr = trailers(sha)
        co_authors = tr.get("co-authored-by", [])
        agent_co = [c for c in co_authors
                    if any(m in c.lower() for m in AGENT_CO_AUTHOR_MARKERS)]

        # 1. IDENTITY
        if author in AGENT_IDENTITIES:
            problems.append(f"{short}\n    an agent identity ({author}) committed "
                            f"{', '.join(touched)} — no era excuses this (§5)")
        elif not AGENT_IDENTITIES:
            undecidable.append(f"{short}\n    identity not distinguishable until agents "
                               f"commit under their own identity (#24)")

        # 2. CITATION
        if agent_co and not tr.get("session"):
            problems.append(
                f"{short}\n    agent co-author ({agent_co[0]}) on {', '.join(touched)} "
                f"with no Session: trailer — the influence is untraceable (§5)")

        # 3. DEFENCE — reported, never judged here.
        obligations.append(f"{short}\n    owes a defence artifact on this pull request, "
                           f"grilled by an agent that did not draft the text (§5, §6)")

    if undecidable:
        print("UNDECIDABLE — recorded, not failed:")
        print("\n".join(f"  {u}" for u in undecidable), "\n")
    if obligations:
        print("OBLIGATIONS — for the reviewer, not for CI:")
        print("\n".join(f"  {o}" for o in obligations), "\n")
    if problems:
        print("CUSTODY VIOLATIONS:")
        print("\n".join(f"  {p}" for p in problems))
        return 1

    print("No custody violations in the added commits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
