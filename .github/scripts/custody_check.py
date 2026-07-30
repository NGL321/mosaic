#!/usr/bin/env python3
"""Check §5's custody obligations over the commits a pull request adds.

Two of the three obligations are mechanical, and only those are checked here:

  IDENTITY  an authored file is committed under a human identity.
  CITATION  an agent co-author on an authored file carries a session trailer.

The third — DEFENCE — is not CI's to judge. A defence artifact is grilled by a
checker agent on the pull request thread (§6), so this script reports the
obligation and does not pretend to verify it. It reports it as *may owe*: §6's
de minimis exception exempts changes that cannot alter meaning, and only a
reader can tell whether a diff did.

Only commits the pull request *adds* are checked, which is what implements §2's
pre-charter grace correctly: history that predates a mechanism is deferred, not
re-litigated on every run. Nothing here reaches backwards.

**A green run must mean something.** A custody check that passes while measuring
nothing is indistinguishable in the record from a working one, which is the
failure §5 argues against at length. So the authored set is validated before any
commit is read: if no authored file exists, or if this script and the workflow
that invokes it disagree about which files are authored, that is exit 2 — the
tool is broken — not a pass.

Usage:  custody_check.py <base-ref> <head-ref>

Exit codes (distinct so CI can tell a violation from a broken tool):
    0  no violations in the added commits
    1  a custody violation
    2  the tool could not run — bad refs, vacuous authored set, drifted config
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# Output carries § and em dashes; a cp1252 console would mangle them.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github" / "workflows" / "custody.yml"

# §5's authored files, at the paths §5 declares. Custody follows the file, never
# the topic. `CHARTER.md` does not exist yet; §5 names that path so that when the
# charter is written it lands where this check and the workflow's `paths:` filter
# can both see it. A charter under any other name would leave this check green
# and covering nothing.
AUTHORED = frozenset({"CONTEXT.md", "CHARTER.md"})

# Identities that are agents. Empty until #24 gives agents their own identity —
# until then the IDENTITY obligation is undecidable rather than satisfied, and
# this script says so instead of passing silently.
AGENT_IDENTITIES: frozenset[str] = frozenset()

AGENT_CO_AUTHOR_MARKERS = ("claude", "gpt-", "copilot", "gemini", "[bot]")

EXIT_OK, EXIT_VIOLATION, EXIT_TOOL = 0, 1, 2


class GitError(RuntimeError):
    """A git command failed. Carries something a reviewer can act on."""


def git(*args: str, stdin: str | None = None) -> str:
    """Run git, raising GitError rather than dying on a raw traceback."""
    try:
        out = subprocess.run(
            ["git", *args],
            input=stdin,
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=ROOT,
        )
    except FileNotFoundError as e:  # pragma: no cover - git is always present in CI
        raise GitError("git is not on PATH") from e
    if out.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout.strip()


# ---------------------------------------------------------------------------
# The authored set — validated before anything is checked against it
# ---------------------------------------------------------------------------


def workflow_paths(text: str) -> set[str]:
    """The `paths:` filter of the workflow that invokes this script.

    A hand-rolled read of one known block, so the check needs no YAML
    dependency. It stops at the first key that ends the list.
    """
    found: set[str] = set()
    inside = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("paths:"):
            inside = True
            continue
        if inside:
            if stripped.startswith("- "):
                found.add(stripped[2:].strip())
            elif stripped and not stripped.startswith("#"):
                break
    return found


def validate_authored_set() -> list[str]:
    """Fail loudly if a pass would mean nothing. Returns notes worth printing."""
    notes: list[str] = []

    present = sorted(p for p in AUTHORED if (ROOT / p).exists())
    absent = sorted(p for p in AUTHORED if not (ROOT / p).exists())

    if not present:
        raise GitError(
            "no authored file exists at any path in AUTHORED "
            f"({', '.join(sorted(AUTHORED))}) — the check would pass while "
            "covering nothing. Fix the paths, or §5's declaration of them."
        )
    if absent:
        notes.append(
            f"not yet written: {', '.join(absent)} — declared in §5 so that it "
            f"lands where this check can see it. Covering {', '.join(present)}."
        )

    if WORKFLOW.exists():
        declared = workflow_paths(WORKFLOW.read_text(encoding="utf-8"))
        if declared and declared != set(AUTHORED):
            raise GitError(
                "the workflow's paths: filter and AUTHORED disagree — "
                f"workflow {sorted(declared)} vs script {sorted(AUTHORED)}. "
                "A file in one but not the other is unchecked or untriggered."
            )
    else:  # pragma: no cover - only if the workflow is renamed
        notes.append(f"cannot cross-check the paths: filter — {WORKFLOW} is missing")

    return notes


# ---------------------------------------------------------------------------
# Reading the commits a pull request adds
# ---------------------------------------------------------------------------


def commits(base: str, head: str) -> list[str]:
    """The commits `head` adds relative to `base`, from their merge base.

    `base..head` is wrong when the base branch has advanced or been force-pushed:
    the raw base sha may not be reachable, and commits that merely arrived on the
    base would be re-litigated here. The merge base is the honest starting point.
    """
    try:
        start = git("merge-base", base, head)
    except GitError as e:
        raise GitError(
            f"cannot find a merge base for {base}..{head} — the base branch may "
            f"have advanced or been force-pushed, or the checkout may be shallow "
            f"(fetch-depth: 0). Underlying error: {e}"
        ) from e
    out = git("rev-list", "--no-merges", f"{start}..{head}")
    return out.splitlines() if out else []


def authored_files_touched(sha: str) -> list[str]:
    files = git("show", "--name-only", "--format=", sha).splitlines()
    return [f for f in files if f in AUTHORED]


def trailers(sha: str) -> dict[str, list[str]]:
    """The commit's real trailers — the contiguous final block, and only that.

    Delegated to `git interpret-trailers --parse`, which knows the rules. A
    hand-rolled `key: value` scan of the whole body would let a `Session:` in
    prose, or inside a quoted diff, satisfy CITATION.
    """
    body = git("show", "-s", "--format=%B", sha)
    parsed = git("interpret-trailers", "--parse", stdin=body)
    found: dict[str, list[str]] = {}
    for line in parsed.splitlines():
        key, sep, value = line.partition(":")
        if sep:
            found.setdefault(key.strip().lower(), []).append(value.strip())
    return found


def session_citations(tr: dict[str, list[str]]) -> list[str]:
    """Session trailers under any tool's spelling.

    §5 pins `Session:` as the canonical key and admits a tool-specific prefix,
    because that is what the tools in fact emit: every agent-co-authored commit
    in this repository carries `Claude-Session:`. Matching only the bare key
    would fail every correctly cited commit in the history — which it did.
    """
    return [v
            for key, values in tr.items()
            if key == "session" or key.endswith("-session")
            for v in values]


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: custody_check.py <base-ref> <head-ref>", file=sys.stderr)
        return EXIT_TOOL

    base, head = sys.argv[1], sys.argv[2]
    problems: list[str] = []
    obligations: list[str] = []
    undecidable: list[str] = []

    try:
        notes = validate_authored_set()
        added = commits(base, head)
    except GitError as e:
        print(f"custody check could not run: {e}", file=sys.stderr)
        return EXIT_TOOL

    if notes:
        print("NOTES — about what this run covers:")
        print("\n".join(f"  {n}" for n in notes), "\n")

    try:
        for sha in added:
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
            if agent_co and not session_citations(tr):
                problems.append(
                    f"{short}\n    agent co-author ({agent_co[0]}) on {', '.join(touched)} "
                    f"with no Session: trailer — the influence is untraceable (§5)")

            # 3. DEFENCE — reported, never judged here.
            obligations.append(
                f"{short}\n    may owe a defence artifact on this pull request, grilled by "
                f"an agent that did not draft the text (§5, §6) — unless §6's de minimis "
                f"exception applies, which only a reader can decide. If the scaffolding era "
                f"defers it, file it as a custody:deferred issue rather than dropping it (§2)")
    except GitError as e:
        print(f"custody check could not run: {e}", file=sys.stderr)
        return EXIT_TOOL

    if undecidable:
        print("UNDECIDABLE — recorded, not failed:")
        print("\n".join(f"  {u}" for u in undecidable), "\n")
    if obligations:
        print("OBLIGATIONS — for the reviewer, not for CI:")
        print("\n".join(f"  {o}" for o in obligations), "\n")
    if problems:
        print("CUSTODY VIOLATIONS:")
        print("\n".join(f"  {p}" for p in problems))
        return EXIT_VIOLATION

    print("No custody violations in the added commits.")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
