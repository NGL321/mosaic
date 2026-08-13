"""
Tests for tools/snapshot_debt.py.

The parsing helpers fail *quietly* — a malformed issue body yields a plausible
looking row rather than an error — which is the worst failure mode for a file
whose whole job is being an auditable artifact. These cover that surface.

Run:  python -m pytest tools/test_snapshot_debt.py
  or: python tools/test_snapshot_debt.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import snapshot_debt as sd  # noqa: E402


def setup_function(_fn=None) -> None:
    sd._problems.clear()


# --- field -----------------------------------------------------------------


def test_field_extracts_a_one_line_marker() -> None:
    body = "intro\n**Holds down.** `Schema` — CONTEXT.md\n\n## Next"
    assert sd.field(body, "**Holds down.**") == "`Schema` — CONTEXT.md"


def test_field_warns_and_falls_back_when_missing() -> None:
    setup_function()
    assert sd.field("nothing here", "**Holds down.**", where="#9") == "—"
    assert len(sd._problems) == 1
    assert "#9" in sd._problems[0]


# --- section ---------------------------------------------------------------


def test_section_preserves_line_structure() -> None:
    body = "## Discharged by\n\n- read it\n- rederive it\n\n## Curriculum\nInfo theory."
    assert sd.section(body, "Discharged by") == "- read it\n- rederive it"


def test_section_does_not_collapse_bullets_into_one_line() -> None:
    body = "## Discharged by\n- a\n- b\n"
    assert "- a - b" not in sd.section(body, "Discharged by")


def test_section_is_case_insensitive_on_the_heading() -> None:
    assert sd.section("## curriculum\nTopology.", "Curriculum") == "Topology."


def test_section_stops_at_the_next_heading() -> None:
    body = "## Curriculum\nInfo theory.\n## Elsewhere\nnot this"
    assert sd.section(body, "Curriculum") == "Info theory."


def test_section_warns_when_empty() -> None:
    setup_function()
    assert sd.section("## Curriculum\n\n## Next\nx", "Curriculum", where="#9") == "—"
    assert len(sd._problems) == 1


# --- cell ------------------------------------------------------------------


def test_cell_escapes_pipes_so_the_table_survives() -> None:
    assert sd.cell("a | b") == "a \\| b"


def test_cell_flattens_multiline_for_table_use() -> None:
    assert sd.cell("- a\n- b") == "- a - b"


# --- link_text -------------------------------------------------------------


def test_link_text_escapes_brackets_in_debt_titles() -> None:
    assert sd.link_text("[debt] Mountcastle unread") == "\\[debt\\] Mountcastle unread"


# --- partition -------------------------------------------------------------


def _issue(number: int, state: str, *labels: str) -> dict:
    return {
        "number": number,
        "state": state,
        "title": f"[debt] item {number}",
        "body": "",
        "url": f"https://example.invalid/{number}",
        "labels": [{"name": n} for n in labels],
    }


def test_partition_splits_on_kind_label_not_state() -> None:
    setup_function()
    live, done = sd.partition(
        [
            _issue(1, "CLOSED", sd.VERIFICATION_LABEL),
            _issue(2, "OPEN", sd.SOURCE_LABEL, sd.DONE_LABEL),
        ]
    )
    # The label is authoritative, so a closed-but-undischarged issue is still open debt.
    assert [i["number"] for i in live[sd.VERIFICATION_LABEL]] == [1]
    assert [i["number"] for i in done] == [2]
    assert len(sd._problems) == 2  # both disagreements reported, neither hidden


def test_partition_files_a_both_kinds_issue_under_each() -> None:
    setup_function()
    live, done = sd.partition(
        [_issue(1, "OPEN", sd.SOURCE_LABEL, sd.VERIFICATION_LABEL)]
    )
    # An assertion may be unsourced *and* undefended; #189 made the kinds non-exclusive,
    # so neither wins arbitrarily and no warning is due.
    assert [i["number"] for i in live[sd.SOURCE_LABEL]] == [1]
    assert [i["number"] for i in live[sd.VERIFICATION_LABEL]] == [1]
    assert done == []
    assert sd._problems == []


def test_partition_reports_the_retired_open_label() -> None:
    setup_function()
    live, done = sd.partition(
        [_issue(1, "OPEN", sd.LEGACY_LABEL, sd.SOURCE_LABEL)]
    )
    # Retired by #189. It still files correctly on its kind, but it is never silent.
    assert [i["number"] for i in live[sd.SOURCE_LABEL]] == [1]
    assert any(sd.LEGACY_LABEL in problem for problem in sd._problems)


def test_partition_skips_and_warns_on_an_issue_with_no_kind() -> None:
    setup_function()
    live, done = sd.partition([_issue(1, "OPEN")])
    assert (all(not g for g in live.values()), done) == (True, [])
    assert len(sd._problems) == 1


def test_partition_is_quiet_when_labels_and_state_agree() -> None:
    setup_function()
    live, done = sd.partition(
        [
            _issue(1, "OPEN", sd.VERIFICATION_LABEL),
            _issue(2, "CLOSED", sd.SOURCE_LABEL, sd.DONE_LABEL),
        ]
    )
    assert [i["number"] for i in live[sd.VERIFICATION_LABEL]] == [1]
    assert [i["number"] for i in done] == [2]
    assert sd._problems == []


# --- render ----------------------------------------------------------------


def test_render_does_not_duplicate_an_issue_present_twice() -> None:
    setup_function()
    i = _issue(1, "OPEN", sd.SOURCE_LABEL)
    out = sd.render([i])
    assert out.count("https://example.invalid/1") == 2  # table row + detail heading


def test_comparable_ignores_the_snapshot_date() -> None:
    a = "x\nSnapshot of [`x`](y) taken 2026-01-01.\nz"
    b = "x\nSnapshot of [`x`](y) taken 2099-12-31.\nz"
    assert sd._comparable(a) == sd._comparable(b)


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            setup_function()
            try:
                fn()
                print(f"  ok   {name}")
            except AssertionError:
                failures += 1
                print(f"  FAIL {name}")
    print(f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
