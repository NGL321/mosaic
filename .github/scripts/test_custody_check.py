"""
Tests for .github/scripts/custody_check.py.

The bug this file exists for: the first draft matched the trailer key `session`
while every real commit in the repository carries `Claude-Session:`, so the check
convicted correctly cited commits and produced two wrong issues before anyone
noticed. Every failure mode here is of that shape — a check that reports
confidently while measuring the wrong thing.

Run:  python -m pytest .github/scripts/test_custody_check.py
  or: python .github/scripts/test_custody_check.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import custody_check as cc  # noqa: E402


# --- session_citations -----------------------------------------------------


def test_bare_session_key_is_a_citation() -> None:
    assert cc.session_citations({"session": ["https://example/s/1"]}) == ["https://example/s/1"]


def test_tool_prefixed_session_key_is_a_citation() -> None:
    """The regression. `Claude-Session:` is what the tools actually emit."""
    tr = {"co-authored-by": ["Claude Opus 5 <noreply@anthropic.com>"],
          "claude-session": ["https://claude.ai/code/session_01KJ"]}
    assert cc.session_citations(tr) == ["https://claude.ai/code/session_01KJ"]


def test_an_unrelated_key_ending_in_session_is_not_invented() -> None:
    assert cc.session_citations({"co-authored-by": ["someone"]}) == []


def test_a_key_merely_containing_session_does_not_count() -> None:
    """`Sessionish:` is not a citation; only `Session:` and `<Tool>-Session:`."""
    assert cc.session_citations({"sessionish": ["x"], "session-notes": ["y"]}) == []


# --- workflow_paths --------------------------------------------------------


WORKFLOW_SNIPPET = """\
on:
  pull_request:
    paths:
      - CONTEXT.md
      - CHARTER.md

permissions:
  contents: read
"""


def test_workflow_paths_reads_the_filter() -> None:
    assert cc.workflow_paths(WORKFLOW_SNIPPET) == {"CONTEXT.md", "CHARTER.md"}


def test_workflow_paths_stops_at_the_next_key() -> None:
    """`contents: read` must not be swallowed into the paths list."""
    assert "contents: read" not in cc.workflow_paths(WORKFLOW_SNIPPET)


def test_the_shipped_workflow_agrees_with_the_authored_set() -> None:
    """The drift the script exits 2 on — asserted here so it fails in review, not in CI."""
    text = cc.WORKFLOW.read_text(encoding="utf-8")
    assert cc.workflow_paths(text) == set(cc.AUTHORED)


# --- validate_authored_set -------------------------------------------------


def test_the_authored_set_is_not_vacuous_in_this_repository() -> None:
    notes = cc.validate_authored_set()
    # CHARTER.md is not written yet, so the run says what it covers.
    assert any("CHARTER.md" in n for n in notes)


def test_a_vacuous_authored_set_is_a_tool_failure(monkeypatch) -> None:
    """A green run over nothing is the failure §5 argues against. It must not be green."""
    monkeypatch.setattr(cc, "AUTHORED", frozenset({"NOT-A-FILE.md"}))
    try:
        cc.validate_authored_set()
    except cc.GitError as e:
        assert "covering nothing" in str(e)
    else:  # pragma: no cover
        raise AssertionError("a vacuous authored set passed validation")


def test_drift_between_script_and_workflow_is_a_tool_failure(monkeypatch) -> None:
    monkeypatch.setattr(cc, "AUTHORED", frozenset({"CONTEXT.md"}))
    try:
        cc.validate_authored_set()
    except cc.GitError as e:
        assert "disagree" in str(e)
    else:  # pragma: no cover
        raise AssertionError("drifted paths passed validation")


# --- trailers, against real git --------------------------------------------


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          encoding="utf-8", cwd=cc.ROOT).stdout.strip()


def test_trailers_ignores_a_session_line_in_prose() -> None:
    """A loose `key: value` scan would let prose satisfy CITATION. Real trailers
    are the contiguous final block, which is what git knows and we do not."""
    body = ("record: something\n\n"
            "The body mentions Session: https://not-a-trailer/1 in passing.\n\n"
            "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>\n"
            "Claude-Session: https://claude.ai/code/session_real\n")
    parsed = cc.git("interpret-trailers", "--parse", stdin=body)
    keys = {ln.partition(":")[0].strip().lower() for ln in parsed.splitlines() if ln.strip()}
    assert keys == {"co-authored-by", "claude-session"}


def test_the_repositorys_own_vocabulary_commits_are_cited(monkeypatch) -> None:
    """The two commits the first draft wrongly convicted. Skipped if unreachable."""
    for sha in ("2ec5194", "1889b61"):
        if not _git("cat-file", "-t", sha) == "commit":
            return
        tr = cc.trailers(sha)
        assert tr.get("co-authored-by"), f"{sha} should carry an agent co-author"
        assert cc.session_citations(tr), f"{sha} is cited; the check must not convict it"


if __name__ == "__main__":
    sys.exit(subprocess.call([sys.executable, "-m", "pytest", __file__, "-q"]))
