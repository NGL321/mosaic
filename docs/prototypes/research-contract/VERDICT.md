# Did the template earn its constraints?

The failure mode #26 named was *a template that makes a good document worse*. The #4 survey
is the test case: 323 lines, a negative result, and the best open-gaps section in the corpus.
Rewritten into the contract it is 396 lines — **+23%, and none of it argument.**

Here is where that 73 lines went, and whether each part paid for itself.

---

## Earned

**R5 — `What this does not establish`.** This is the contract's one real addition and it paid
immediately. Writing the *Sources not reached* subsection forced five admissions the original
survey did not make, and one of them is load-bearing: **Culík & Yu (1988) was reached through
a Semantic Scholar record, not the *Complex Systems* original.** The original document cites
that undecidability proof as the reason Noah's stated belief about the Wolfram taxonomy is
refuted — a headline finding resting on a source nobody opened. That is exactly the class of
thing #13 was commissioned to find, discovered here for free by a section heading.

The *Load-bearing ifs* subsection is the other half. It made the document write its own
falsifiers — *if ECA representations do carry cyclic structure, §4.1(i) collapses* — which
converts a survey a later reader must re-derive to attack into one they can attack in an
afternoon. Both subsections are cheap to write and expensive to omit, which is the shape of a
constraint worth having.

**R7 — no record content in HTML comments.** #5 found Mosaic's entire debt load hidden in
comments in `CONTEXT.md`. This check fires **today, on #14** — a document written four days
*after* that finding, carrying its Provenance Tier inside a comment where the rendered file
does not show it. One regex, one real catch, no false positives across five documents.

**R6 — debt itemised and filed.** The original survey said its debt was "logged against the
Curriculum." There was no Curriculum, and the debt was logged nowhere. Writing the section
out produced five concrete items with their prerequisites named, and one of them (verifying
Damrich et al.'s thresholds against released code) is cheap enough to do this week — a fact
invisible while the debt was a sentence.

**R1/R2 — front matter and session id.** Machine-readability is #24's requirement, not a
style preference: a dispatch pipeline has to route on `kind` and `ticket` without an LLM.
The count check inside R9 caught its own front matter being wrong on the first run
(`sources: 41`, appendix listed 44), which is a check earning its keep within minutes of
existing. `session: unrecorded` is honest for the survey, whose transcript predates the
convention — and an explicit `unrecorded` is a fact, where an absent field is an ambiguity.

**R9 — appendix, all linked.** Fires on the original survey: one of 39 entries carries no
link, and it is Culík & Yu again — the same source the negative-space section independently
flagged. Two rules converging on one weak citation is the checker working.

---

## Not earned

**R11 — "no inline tier badges" is a rule with nothing to bite on.** Zero of five documents
carry one, because nobody was ever going to. It is a note in the template, not a CI check,
and shipping it as a check is the bookkeeping-by-accretion failure #5 warned against.

**R6 is satisfiable by ceremony, and the rewrite proves it.** Every one of the five debt items
is marked `unfiled` — and R6 passes. `PROTOCOL.md` §5 argues at length that a gate satisfiable
by ceremony is *worse than none*, because in the record it is indistinguishable from the real
thing. The fix is not to forbid `unfiled` (the survey genuinely predates the tracker) but to
make it visible: `unfiled` items should be counted in the front matter's `debt:` field so a
document declaring five unfiled items reads as a document with five unfiled items, at the top,
where a reviewer sees it. **Not fixed in this prototype.**

**R4 — the closed verdict vocabulary fits verification and strains on surveys.** `Supported /
Refuted / Loose / Unresolved` was born in #13, where every section adjudicates one attribution,
and it is perfect there. On the survey it produced §3.2(f) *"Computational cost — **Refuted**
as a binding constraint"*, which is a section verdict wrapped around a sub-clause because the
rule demanded a token. Several of the rewrite's section verdicts are that shape — §2.2's
*"**Established**, and thinner than assumed"* is another. The
vocabulary is right; requiring it *per top-level section* rather than *per sub-question in the
verdict table* is the overreach.

---

## Cost the template imposed, honestly

Relocating §4.4 *Where the genuine open gaps are* into `What this does not establish` moved
the survey's most valuable output away from §4, the recommendation it justifies. The original
ordering — recommendation, then the gaps that recommendation leaves — reads better. The
contract's ordering is better for *finding* the gaps in an unfamiliar document, and worse for
*reading* the argument. That trade is real and the contract took the wrong side of it for
surveys; a document should be allowed to argue its gaps in place and cross-reference them
from the required section.

Nothing else in the rewrite lost anything. Every line of §1–§4 survives verbatim or with a
verdict token added.

---

## Answers to the ticket's seven questions

1. **The template.** Verdict → evidence → what this does not establish → debt → proposals →
   appendix. Six sections; three of them (`0. Verdict`, evidence, appendix) are what all four
   existing documents already did unprompted, which is why they are cheap.
2. **Front matter.** YAML, seven required keys, listed in `TEMPLATE.md` §1. The human
   provenance paragraph stays — `tier: T3` cannot carry *which sources were read in full*.
3. **Tier notation per claim — the answer is no, and this is the finding.** #5 settled that an
   agent's reading never promotes a tier. So every claim in an agent-written document is T3 by
   construction, and a per-claim badge is the same three characters on every line. #26 asks for
   per-claim tiering on the premise that a document whose every claim carries the same tier is
   not tiered; the resolution is that **the axis that varies inside an evidence document is the
   verdict, not the tier.** The badge belongs at the destination — the `CONTEXT.md` line, typed
   by Noah. Argued in `TEMPLATE.md` §4.
4. **Citation form.** Inline *and* appendix, both mandatory, no footnotes. Primary source =
   the thing itself, read directly; unreachable → verdict `Unresolved`, per #13's precedent.
5. **Declaring what was not established.** Required section, three subsections. See *Earned*.
6. **Acceptance criteria.** Fifteen checks; thirteen mechanical, two human. The two human ones
   are listed *in the same table* so that a green CI run cannot be mistaken for a merge
   decision — R14 and R15 are where the merge actually lives.
7. **Does one contract cover verification, review and revision?** Yes. All four documents fit
   one template differing only in `kind:` and whether a revision log is present. Four templates
   differing in one field would have been four templates.

## Not settled here

- Whether `unfiled` debt should be counted in the front matter (above).
- Whether R4 should attach to sub-questions rather than sections (above).
- Whether `docs/adr/` and #11's notebook entries share any of this. Assumed not; untested.
- The rewrite is a rewrite, not a re-verification. Its §1–§4 claims carry the original's
  provenance, and this prototype adds no reading of its own.
