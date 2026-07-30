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


def test_an_inline_comment_is_not_part_of_the_value() -> None:
    """The §1 template comments every key, so a document copying it carried the comments."""
    d = doc("# T\n", GOOD_FRONT.replace("sources: 1", "sources: 1   # must match the count"))
    assert d.front["sources"] == "1"
    assert crd._session(doc("# T\n", GOOD_FRONT.replace(
        "session: unrecorded", "session: unrecorded          # no transcript")))[0]


def test_a_hash_inside_a_value_survives() -> None:
    """`#` only opens a comment after whitespace; a path anchor is not a comment."""
    d = doc("# T\n", GOOD_FRONT.replace("supersedes: null", "supersedes: docs/x.md#section"))
    assert d.front["supersedes"] == "docs/x.md#section"


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


DIGEST = "9f2c" + "0" * 60


def test_session_wants_a_whole_digest_in_either_case() -> None:
    """Half a hash does not identify a session; hex case does not change what it identifies."""
    def sessions(v: str) -> bool:
        return crd._session(doc("# T\n", GOOD_FRONT.replace("session: unrecorded", f"session: {v}")))[0]

    assert sessions(f"sha256:{DIGEST}")
    assert sessions(f"sha256:{DIGEST.upper()}")
    assert not sessions("sha256:9f2c1234")


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


def test_negative_space_is_not_satisfiable_by_one_sentence() -> None:
    """
    The keyword version passed on this sentence, which is the ceremony the section exists to
    prevent: needles as loose as `gap` over the lowercased body, all three hit at once.
    """
    body = ("# T\n\n## What this does not establish\n\nWe could not reach the original; that "
            "gap is open, and if false it would change the verdict.\n")
    ok, why = crd._negative_space(doc(body))
    assert not ok
    assert "open gaps" in why and "load-bearing ifs" in why


def test_negative_space_rejects_a_subsection_with_a_token_under_it() -> None:
    thin = NEGATIVE.replace("An open gap worth naming.", "None.")
    ok, why = crd._negative_space(doc(thin))
    assert not ok and "open gaps" in why


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


def test_a_documents_own_ticket_does_not_count_as_filed_debt() -> None:
    """`unfiled` closed one hatch; `#4` in a document resolving #4 was the same hatch open."""
    body = "# T\n\n## Verification Debt\n\n1. Someone should re-read the #4 survey.\n"
    front = GOOD_FRONT.replace("debt: [45]", "debt: [4]")  # ticket: 4
    ok, why = crd._debt_filed(doc(body, front))
    assert not ok and "own ticket" in why


def test_a_sub_bullet_is_not_a_second_debt_item() -> None:
    body = ("# T\n\n## Verification Debt\n\n1. [#45](u) — read the proof.\n"
            "   - it is paywalled\n   - the preprint differs\n")
    ok, why = crd._debt_filed(doc(body))
    assert ok, why


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


def test_a_comment_quoted_in_a_fenced_block_is_not_a_finding() -> None:
    """A document documenting R7 was flagging itself; only `README.md` being name-excluded hid it."""
    body = "# T\n\nR7 catches this:\n\n```markdown\n<!-- debt: unverified, see later -->\n```\n"
    assert crd._no_hidden_record(doc(body))[0]


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


def test_a_sub_question_may_contain_a_triple_dash() -> None:
    """Shedding rows that contain `---` shed the content rows too, and the table with them."""
    t = TABLE.replace("Does it hold?", "Is A --- B?")
    ok, why = crd._sub_question_verdicts(doc(t))
    assert ok, why


def test_the_verdict_column_may_be_called_something_else() -> None:
    """The header is the first row. It is not the row with the word `Verdict` in it."""
    t = TABLE.replace("| Sub-question | Verdict | Argued in |", "| Sub-question | Finding | Where |")
    ok, why = crd._sub_question_verdicts(doc(t))
    assert ok, why


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


def test_a_numbered_appendix_is_an_appendix() -> None:
    """`_debt_filed` accepted both markers; this one accepted only dashes and read `1.` as empty."""
    body = "# T\n\n## Appendix: primary sources\n\n1. A. https://x.invalid\n"
    ok, why = crd._appendix_sources(doc(body))
    assert ok, why


def test_an_unreadable_source_count_fails_rather_than_skipping_the_comparison() -> None:
    body = "# T\n\n## Appendix: primary sources\n\n- A. https://x.invalid\n"
    ok, why = crd._appendix_sources(doc(body, GOOD_FRONT.replace("sources: 1", "sources: many")))
    assert not ok and "not a count" in why


def test_the_retrieval_date_follows_the_source_not_the_kind() -> None:
    """A paper does not move. A pricing page does, and a survey may cite one — #27 does."""
    paper = "# T\n\n## Appendix: primary sources\n\n- Culík & Yu. https://doi.invalid/10.1\n"
    assert crd._volatile_dated(doc(paper))[0], "a survey citing a paper needs no date"
    for kind in ("survey", "verification"):
        front = GOOD_FRONT.replace("kind: survey", f"kind: {kind}")
        live = "# T\n\n## Appendix: primary sources\n\n- Gemini API pricing — https://x.invalid/docs/pricing\n"
        ok, why = crd._volatile_dated(doc(live, front))
        assert not ok, f"kind: {kind} — {why}"
        dated = live.rstrip("\n") + " (retrieved 2026-07-29)\n"
        assert crd._volatile_dated(doc(dated, front))[0]


def test_one_date_on_the_appendix_heading_covers_it() -> None:
    """How #27 writes it, and it is not worse for being written once."""
    body = ("# T\n\n## Appendix: primary sources, all retrieved 2026-07-29\n\n"
            "- Gemini API pricing — https://x.invalid/docs/pricing\n")
    assert crd._volatile_dated(doc(body))[0]


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
            except Exception as e:  # noqa: BLE001 — one broken test must not eat the summary
                failures += 1
                print(f"  ERROR {name}  {type(e).__name__}: {e}")
    print(f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
