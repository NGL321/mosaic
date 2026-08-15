# Research documents

The **evidence** layer: what a research ticket produces. A research document is a piece of
work; a [notebook entry](../../notebook/README.md) is the narrative of work happening. An
entry may cite a document; they are not the same artifact and do not share this template.

One file per ticket, `YYYY-MM-DD-slug.md`, flat. Documents are **record** files and so are
agent-writable under [`PROTOCOL.md` §5](../../PROTOCOL.md); they land as `evidence:` (PATCH).

Check one before opening a pull request:

```console
python tools/check_research_doc.py
```

Settled in [#26](https://github.com/NGL321/mosaic/issues/26). The contract exists to remove a
revision tax: the first three documents were each invented from scratch, shaped differently,
and one needed a follow-up commit to apply review feedback. An agent that knows the required
shape before it starts produces work that lands in one pass.

---

## 1. Front matter

YAML, fenced, before the title. The only machine-readable part of the document, and it exists
so that a dispatch pipeline ([#24](https://github.com/NGL321/mosaic/issues/24)) can route on
it without reading prose.

```yaml
---
ticket: 4                    # the issue this resolves
map: 1                       # the map ticket it hangs from
date: 2026-07-25             # the document's date; revisions add `revised:`
kind: survey                 # survey | verification | question | revision
tier: T3                     # the document's floor — see §4
session: unrecorded          # Transcript Archive session id — see below — or `unrecorded`
sources: 44                  # primary sources in the appendix; must match the count
debt_source: [45, 46]        # `debt:source` issues this document filed; [] if none
debt_verification: []        # `debt:verification` issues it *proposes*; [] if none
supersedes: null             # path of the document this replaces, if any
---
```

**The two debt keys mirror the tracker and never add to it.** Every number is an open issue
that already exists, carrying the matching kind label, and the same numbers appear in the
*Debt* section; the checker requires the two to agree.

**The keys are split because the custody rules differ, not because the schema is tidier.**
[#189](https://github.com/NGL321/mosaic/issues/189) separated the ledger into **Source Debt**
(debtor: an agent; discharged by producing a Source) and **Verification Debt** (debtor: Noah;
discharged by learning). An agent may **file** a Source Debt outright — that the record has
not sourced an assertion is a fact about the record. It may only **propose** a Verification
Debt, because asserting what Noah cannot defend unaided is a claim about the researcher, and
[`PROTOCOL.md` §5](../../PROTOCOL.md) reserves root assertions about Noah to Noah. A proposed
Verification Debt therefore goes in *Proposals* alongside the tier badge it would hold down,
on the same rail the badge already travels, and is decidable only against the **competence
floor** ([#40](https://github.com/NGL321/mosaic/issues/40)) — undeclared as of this writing,
which §5 rules makes the obligation *undecidable rather than satisfied*. [#5](https://github.com/NGL321/mosaic/issues/5) settled
that the ledger *is* the issue tracker, and this key does not reopen that — it is there so the
debt a document created is greppable from a clone without an API call, the same read-through
cache argument that justifies [`curriculum/open.md`](../../curriculum/open.md). If the two ever
disagree, the tracker is right.

**`session:` is `sha256:` and a whole 64-character digest, in either case — or the literal
`unrecorded`.** A document that cannot cite its transcript should say so rather than omit the
key: an absent key and an unrecordable session are different facts, and only one of them is
anybody's fault. The digest is not truncated, because the archive identifies a session the way
[`DATA-PROTOCOL.md` §2](../DATA-PROTOCOL.md) identifies every other object — by content hash —
and a prefix a reader cannot resolve against the archive is a citation in appearance only.

The keys carry `#` comments here for the reader. They are stripped before checking, so this
block can be copied as it stands; every value still has to be replaced with a true one.

The **human provenance paragraph** goes immediately under the title and is not replaced by
the YAML. It states the *scope* of the tier — which sources were read in full, which were
reached by abstract, what was derived rather than retrieved. `tier: T3` cannot carry that,
and it is the sentence a reviewer actually reads.

## 2. Sections, in order

| | Section | Contains |
|---|---|---|
| 1 | `# Title` + provenance paragraph | the question, answered in the title where possible |
| 2 | `## 0. Verdict` | a verdict table — one row per sub-question, each carrying a verdict and naming the section that argues it — and a one-line verdict as a blockquote |
| 3 | `## 1..N` evidence | the argument |
| 4 | `## What this does not establish` | three `###` subsections: **sources not reached**, **open gaps**, **load-bearing ifs**, a sentence under each |
| 5 | `## Debt` | itemised; each item names its issue **and its kind** — Source or Verification |
| 6 | `## Proposals` | exact replacement text for authored files, or the single word `None.` |
| 7 | `## Appendix: primary sources` | every source, every one linked, retrieval dates where facts rot |

`kind: revision` adds `## 0.1 What this revision changed` — additive, naming what moved and
what did not. Nothing else varies by kind: verification, a resolved question, a survey and an
infrastructure question all fit this, and four templates differing in one field would have
been four templates.

**§4 is the section that was not already common practice**, and it is the one worth the most:

- **Sources not reached** — what was wanted and could not be got, and why. Writing this
  against the [#4](https://github.com/NGL321/mosaic/issues/4) survey is what surfaced that its
  headline refutation rested on a proof reached through a search-engine record and never
  opened ([#45](https://github.com/NGL321/mosaic/issues/45)).
- **Open gaps** — questions the document opened and did not close, stated so someone could
  pick one up. Often the most valuable thing a survey produces.
- **Load-bearing ifs** — the claims whose falsity would move the verdict. This is the document
  writing its own falsifier, and it is what lets a later reader attack it cheaply instead of
  re-deriving the whole argument first.

Each is its own `###` heading with prose under it, and the checker reads the headings rather
than searching the section for words. The first version searched for needles as loose as `gap`,
which the single sentence *"we could not reach the original; that gap is open, and if false it
would change the verdict"* satisfies three times over — the gate satisfiable by ceremony that
[`PROTOCOL.md` §5](../../PROTOCOL.md) argues is worse than none. Where a subsection is
genuinely empty it says so in a sentence — *"every source in the appendix was opened"* — not in
a word: `None.` is what a document writes when it has not looked.

## 3. Citations

**Inline at the claim site, and a full appendix.** Both, not either: inline because borrowed
frames are cited where they are borrowed and a reader checking one paragraph should not have
to bounce; the appendix because a verifier discharging debt works down a list. Footnotes are
not used — they put the citation one jump away while looking like they didn't.

A **primary source** is the thing itself, read directly: the paper, the publisher record, the
first-party documentation page, the scan of the original edition. Not an abstract, not another
survey's description of it, not a model's recollection. Where a primary source cannot be
reached, the verdict is **Unresolved** and says so — the precedent is
[#13](https://github.com/NGL321/mosaic/issues/13).

## 4. Verdicts, and why there are no tier badges here

A claim's verdict comes from a closed set: **Supported**, **Refuted**, **Loose**,
**Unresolved**, **Established**, **Contested**, **Open**.

**One tier, in the front matter, for the whole document. No per-claim tier badges.**
[#5](https://github.com/NGL321/mosaic/issues/5) settled that an agent's reading is evidence
attached to a claim and does not move its tier. An agent-written document is therefore T3 in
every claim it contains, by construction — a per-claim badge would be the same three
characters on every line, which is not a tiering but a watermark. What varies claim to claim,
and so what is annotated claim by claim, is the **verdict**.

The badge `⟦T3 · #33⟧` belongs at the **destination**: the `CONTEXT.md` line where the claim
lands. A research document is where a claim is *argued*; the badge records what the researcher
can *defend*. An agent may draft the exact badge text in *Proposals*, and Noah applies it —
§5 is explicit that custody is over the decision, not the keystrokes, so what the rule requires
is that he has read and accepted the badge, not that he composed its wording.

## 5. Acceptance

Fourteen checks. Twelve are in `tools/check_research_doc.py`; two are not, and are listed here
anyway so that a green run is not mistaken for a merge decision.

| | Check | Severity | By |
|---|---|---|---|
| R1 | Front matter present and complete, `kind` in the closed set | blocking | CI |
| R2 | `session:` is `sha256:` + a 64-character digest, or `unrecorded` | blocking | CI |
| R3 | First section is the verdict, with a table or a stated one-liner | blocking | CI |
| R4 | Every verdict-table row carries a verdict from the closed set | blocking | CI |
| R5 | `What this does not establish`, three `###` subsections, each with a body | blocking | CI |
| R6 | Every debt item names an issue other than this document's own ticket **and declares its kind**, mirrored in the matching front-matter key | blocking | CI |
| R7 | No debt/tier/provenance content inside HTML comments | blocking | CI |
| R8 | `Proposals` section present, `None.` if empty | blocking | CI |
| R9 | Appendix present, count matches front matter, every entry linked | blocking | CI |
| R12 | Every verdict row names the section that argues it | blocking | CI |
| R10 | An appendix entry citing a source that moves carries a retrieval date | advisory | CI |
| R13 | No substantial evidence section without an inline citation | advisory | CI |
| R14 | **The argument survives an adversarial read** | blocking | human |
| R15 | **The recommendation is actionable** | blocking | human |

R14 and R15 are where the merge decision lives. Everything above them exists so a reviewer
spends their attention there instead of on shape. A document that concludes *"more research is
needed"* passes every mechanical check on this list.

**Two of these are narrower than they read, and the gap is the reviewer's.** R6 checks that a
debt item names *some* issue that is not this document's own ticket, that it declares a kind
from the closed set, and that the front matter mirrors the same numbers under the matching
key; that the number is an issue at all, that it is open, and that its **label agrees with the
declared kind** are not checkable offline and are not checked. The kind is therefore
self-declared and a mislabelled item passes — which is the exact leak #189 named: *if the
filing rule cannot tell the kinds apart at filing time, the split leaks back the moment it is
made*. What stops it is not this check but the custody asymmetry above — an agent cannot file
a Verification Debt at all, so the kind that matters is the one CI never has to adjudicate. R10 decides which sources
move by reading the link — pricing, quotas, rate limits, `latest` docs — so it is a reminder
with false negatives, not a guarantee; it is advisory for that reason. Both were written into
this table as though CI settled them, which is the specific way a gate comes to certify less
than it advertises ([#53](https://github.com/NGL321/mosaic/issues/53)).

Numbering is the prototype's and is not contiguous: R11 forbade inline tier badges and was
retired for having nothing to bite on — no document had ever carried one — and its reasoning
survives as §4 above. The ids are kept stable so the reasoning on
[#26](https://github.com/NGL321/mosaic/issues/26) still refers to something.

## The three documents here predate this

All three used to fail the contract, mostly on §4 and on debt filed only in prose. They were
retrofitted under [#50](https://github.com/NGL321/mosaic/issues/50) and all three now pass;
`0.x` is where process mistakes are allowed to accumulate and be swept once, rather than fixed
one at a time as they appear ([`PROTOCOL.md` §2](../../PROTOCOL.md)).

**What the sweep cost, recorded because it is the argument for doing it:** eighteen
Verification Debt items that three documents had itemised in prose and never filed
([#135](https://github.com/NGL321/mosaic/issues/135)–[#152](https://github.com/NGL321/mosaic/issues/152)),
against five already on the tracker. The ledger was carrying a fifth of the debt these three
documents had already found and written down.

`What this does not establish` is retrofitted honestly rather than completely. #50 is explicit
that only whoever did the reading knows which sources they failed to reach, and none of the
three sessions is reachable — so each document's *sources not reached* subsection says what is
recoverable from its own text and says that it is incomplete. The
[individuation document](2026-07-28-markov-blanket-individuation.md) is the thin one, and says
so in the subsection itself.

The checker was **not** wired into CI by that sweep, and the reason has changed: the repository
is no longer in permanent red, but CI wiring belongs with the other gates in
[#24](https://github.com/NGL321/mosaic/issues/24) rather than arriving on its own.
