"""
Tests for tools/check_research_doc.py.

The checks that matter are the ones with a way to pass falsely: a section that exists but
says nothing, a debt item that names a number that is not an issue, a front matter that
disagrees with the document under it. A shape checker whose checks can be satisfied without
doing the work is the gate PROTOCOL.md §5 argues is worse than none, so those are what is
covered here rather than the happy path.

Run:  python -m pytest tools/test_check_research_doc.py
  or: python tools/test_check_research_doc.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import check_research_doc as crd  # noqa: E402

GOOD_FRONT = """\
---
ticket: 4
map: 1
date: 2026-07-25
kind: survey
tier: T3
session: unrecorded
sources: 1
debt: [45]
supersedes: null
---
"""


def doc(body: str, front: str = GOOD_FRONT) -> crd.Doc:
    return crd.parse(Path("test.md"), front + body)


# --- parsing ---------------------------------------------------------------


def test_a_section_owns_its_subsections() -> None:
    d = doc("# T\n\n## 1. One\n\n### 1.1 Sub\n\n[a](https://x.invalid)\n\n## 2. Two\n\nx\n")
    one = d.top_sections[0]
    assert one.title == "1. One"
    assert len(one.links) == 1, "a `##` section must include its `###` subsections"


def test_slug_strips_the_section_number() -> None:
    d = doc("# T\n\n## 4.2 Implications For The Rung\n\nx\n")
    assert d.top_sections[0].slug == "implications for the rung"


def test_front_matter_is_optional_and_its_absence_is_not_a_crash() -> None:
    d = crd.parse(Path("test.md"), "# T\n\n## 0. Verdict\n\nx\n")
    assert d.front == {}
    assert d.top_sections[0].title == "0. Verdict"


# --- front matter ----------------------------------------------------------


def test_front_matter_rejects_a_kind_outside_the_closed_set() -> None:
    d = doc("# T\n", GOOD_FRONT.replace("kind: survey", "kind: memo"))
    ok, why = crd._front_matter(d)
    assert not ok and "memo" in why


def test_front_matter_rejects_a_present_but_empty_key() -> None:
    d = doc("# T\n", GOOD_FRONT.replace("tier: T3", "tier:"))
    ok, why = crd._front_matter(d)
    assert not ok and "tier" in why


def test_session_accepts_unrecorded_but_not_a_freeform_excuse() -> None:
    assert crd._session(doc("# T\n"))[0]
    d = doc("# T\n", GOOD_FRONT.replace("session: unrecorded", "session: lost, sorry"))
    assert not crd._session(d)[0]


# --- the negative-space section -------------------------------------------


NEGATIVE = """\
# T

## What this does not establish

### Sources not reached
The original could not be reached.

### Open gaps
An open gap worth naming.

### Load-bearing ifs
If this were false it would change the verdict.
"""


def test_negative_space_wants_all_three_subsections() -> None:
    assert crd._negative_space(doc(NEGATIVE))[0]


def test_negative_space_rejects_a_heading_with_nothing_under_it() -> None:
    ok, why = crd._negative_space(doc("# T\n\n## What this does not establish\n\nNone.\n"))
    assert not ok
    assert "sources not reached" in why


# --- debt ------------------------------------------------------------------


def test_debt_requires_an_issue_number_not_a_word() -> None:
    body = "# T\n\n## Verification Debt\n\n1. **Unfiled.** Someone should read the original.\n"
    ok, why = crd._debt_filed(doc(body))
    assert not ok
    assert "file them first" in why, "`unfiled` must not be an escape hatch"


def test_debt_front_matter_must_mirror_the_section() -> None:
    body = "# T\n\n## Verification Debt\n\n1. [#46](u) — read the proof.\n"
    ok, why = crd._debt_filed(doc(body))  # front matter says [45]
    assert not ok and "mirror" in why


def test_debt_passes_when_the_two_agree() -> None:
    body = "# T\n\n## Verification Debt\n\n1. [#45](u) — read the proof.\n"
    assert crd._debt_filed(doc(body))[0]


def test_a_document_may_declare_no_debt() -> None:
    front = GOOD_FRONT.replace("debt: [45]", "debt: []")
    ok, _ = crd._debt_filed(doc("# T\n\n## Verification Debt\n\nNone.\n", front))
    assert ok


# --- the #5 failure, mechanised -------------------------------------------


def test_record_content_in_an_html_comment_is_caught() -> None:
    ok, why = crd._no_hidden_record(doc("# T\n\n<!-- Provenance Tier: T3, unverified -->\n"))
    assert not ok and "comment" in why


def test_an_ordinary_comment_is_not_caught() -> None:
    assert crd._no_hidden_record(doc("# T\n\n<!-- prettier-ignore -->\n"))[0]


# --- verdicts and traceability --------------------------------------------


TABLE = """\
# T

## 0. Verdict

| Sub-question | Verdict | Argued in |
|---|---|---|
| Does it hold? | **Refuted** | §2.3 |
"""


def test_a_verdict_row_needs_a_verdict_from_the_closed_set() -> None:
    assert crd._sub_question_verdicts(doc(TABLE))[0]
    weakened = TABLE.replace("**Refuted**", "**Probably not**")
    ok, why = crd._sub_question_verdicts(doc(weakened))
    assert not ok and "closed-set" in why


def test_a_verdict_row_must_name_its_section() -> None:
    assert crd._claims_traceable(doc(TABLE))[0]
    ok, _ = crd._claims_traceable(doc(TABLE.replace("§2.3", "see above")))
    assert not ok


def test_a_leading_section_number_counts_as_naming_it() -> None:
    """#27 writes `**1.1** Does a Google…`, which names its section perfectly well."""
    t = TABLE.replace("| Does it hold? | **Refuted** | §2.3 |",
                      "| **1.1** Does it hold? | **Refuted** | quoted |")
    assert crd._claims_traceable(doc(t))[0]


# --- appendix --------------------------------------------------------------


def test_appendix_count_must_match_the_front_matter() -> None:
    body = "# T\n\n## Appendix: primary sources\n\n- A. https://x.invalid\n- B. https://y.invalid\n"
    ok, why = crd._appendix_sources(doc(body))  # front matter says sources: 1
    assert not ok and "sources=1" in why


def test_appendix_entries_must_be_linked() -> None:
    body = "# T\n\n## Appendix: primary sources\n\n- Culík & Yu (1988). Complex Systems 2.\n"
    ok, why = crd._appendix_sources(doc(body))
    assert not ok and "no link" in why


def test_surveys_are_exempt_from_the_retrieval_date() -> None:
    """A paper does not move. A pricing page does."""
    body = "# T\n\n## Appendix: primary sources\n\n- A. https://x.invalid\n"
    assert crd._volatile_dated(doc(body))[0]
    front = GOOD_FRONT.replace("kind: survey", "kind: verification")
    assert not crd._volatile_dated(doc(body, front))[0]


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ok   {name}")
            except AssertionError as e:
                failures += 1
                print(f"  FAIL {name}  {e}")
    print(f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
