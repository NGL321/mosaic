# The research-output document contract — proposal for #26

**PROTOTYPE.** Throwaway. This file is the candidate contract; `contract.py` is the same
thing as a predicate; `rewrite-2026-07-25-grokking-eca-tda-survey.md` is the #4 survey
rewritten into it, which is the test #26 asked for. Read `VERDICT.md` for what survived.

A research-track document lives at `docs/research/YYYY-MM-DD-slug.md` and is `evidence:`
(PATCH). It is **record**, so it is agent-writable under [`PROTOCOL.md` §5]. It is not a
notebook entry — that is the narrative layer and belongs to #11.

---

## 1. Front matter

YAML, fenced, before the title. This is the only machine-readable part of the document and
it exists so that #24's dispatch pipeline can route on it without reading prose.

```yaml
---
ticket: 4                    # the issue this resolves
map: 1                       # the map ticket it hangs from
date: 2026-07-25             # the document's date; revisions add `revised:`
kind: survey                 # survey | verification | question | revision
tier: T3                     # the document's floor — see §4
session: sha256:9f2c…        # Transcript Archive session id, or `unrecorded`
sources: 47                  # primary sources in the appendix; must match the count
debt: [29, 30]               # issues this document opened; [] if none
supersedes: null             # path of the document this replaces, if any
---
```

`session:` accepts the literal `unrecorded`. A document that cannot cite its transcript
should say so rather than omit the key, because an absent key and an unrecordable session
are different facts and only one of them is anybody's fault.

The **human** provenance paragraph stays, immediately under the title, and is not
replaced by the YAML. It states the *scope* of the tier — which sources were read in full,
which were reached by abstract, what was derived rather than retrieved. `tier: T3` cannot
carry that, and it is the sentence a reviewer actually reads.

## 2. Required sections, in order

| | Section | Contains |
|---|---|---|
| 1 | `# Title` + provenance paragraph | the question, answered in the title where possible |
| 2 | `## 0. Verdict` | a verdict table — one row per sub-question, each naming the section that argues it — and a one-line verdict as a blockquote |
| 3 | `## 1..N` evidence | the argument. Each top-level section carries at least one **verdict token** |
| 4 | `## What this does not establish` | three subsections: **sources not reached**, **open gaps**, **load-bearing ifs** |
| 5 | `## Verification Debt` | itemised; each item names its `debt:open` issue or is marked `unfiled` |
| 6 | `## Proposals` | exact replacement text for authored files, or the single word `None.` |
| 7 | `## Appendix: primary sources` | every source, every source linked, retrieval dates where facts rot |

`kind: revision` adds `## 0.1 What this revision changed` — additive, naming what moved and
what did not. Nothing else in the contract varies by kind.

**Section 4 is the one addition that is not already common practice**, and it is the one the
ticket asked for by name. Three subsections, because "what we didn't establish" collapses
into hand-waving without them:

- **Sources not reached** — what was wanted and could not be got, and why. #13's *Limnaea*
  paper is the model.
- **Open gaps** — questions this document opened and did not close, stated so someone could
  pick one up. The survey's §4.4 is the best example in the corpus and is why this is required.
- **Load-bearing ifs** — the claims whose falsity would move the verdict. This is the
  document writing its own falsifier, and it is what makes a later reader able to attack it
  cheaply instead of re-reading everything.

## 3. Citation form

**Inline at the claim site, plus a full appendix.** Both, not either:

- Inline, because the map's standing preference is that borrowed frames are cited where they
  are borrowed, and because a reader checking one paragraph should not have to bounce.
- Appendix, because a verifier discharging debt works down a list, and because it is the
  artifact #13 was handed.

A **primary source** is the thing itself, read directly: the paper, the publisher record, the
first-party documentation page, the scan of the original edition. Not an abstract, not a
survey's description of it, not a model's recollection. #13 is the standing precedent —
where a primary source could not be reached, the verdict is **Unresolved** and says so.

Footnotes are not used. They put the citation one jump away from the claim while looking
like they didn't.

## 4. Tiers inside a document

**One tier, in the front matter, for the whole document. No per-claim badges.**

This inverts what #26 assumed, and the reason is #5's ruling: *an agent's reading is evidence
attached to a claim; it does not move the tier.* An agent-written document is therefore T3 in
every claim it contains, by construction — a per-claim badge would be the same three
characters on every line, which is not a tiering, it is a watermark.

What varies claim to claim, and therefore what the contract requires per claim, is the
**verdict**: `Supported`, `Refuted`, `Loose`, `Unresolved`, `Established`, `Contested`,
`Open`. That vocabulary is already in use across all four existing documents; the contract
only fixes it as a closed set and makes it mandatory per section.

The tier badge `⟦T3 · #33⟧` belongs at the **destination** — the `CONTEXT.md` line where the
claim lands, typed by Noah, per #5. The research document is where a claim is *argued*; the
badge records what the researcher can *defend*. Different questions, different files.

## 5. Acceptance criteria

Fifteen checks. Thirteen are mechanical and belong in CI; two are not, and are listed anyway
so the checklist does not imply CI covers them.

| | Check | Severity | By |
|---|---|---|---|
| R1 | Front matter present and complete, `kind` in the closed set | blocking | CI |
| R2 | `session:` is `sha256:<digest>` or `unrecorded` | blocking | CI |
| R3 | First section is the verdict, with a table or a stated one-liner | blocking | CI |
| R4 | Every evidence section carries a verdict token | blocking | CI |
| R5 | `What this does not establish`, with all three subsections | blocking | CI |
| R6 | Every debt item names an issue or is marked `unfiled` | blocking | CI |
| R7 | No debt/tier/provenance content inside HTML comments | blocking | CI |
| R8 | `Proposals` section present, `None.` if empty | blocking | CI |
| R9 | Appendix present, count matches front matter, every entry linked | blocking | CI |
| R10 | Volatile sources carry a retrieval date | advisory | CI |
| R11 | No inline tier badges | advisory | CI |
| R12 | Every verdict row names the section that argues it | advisory | CI |
| R13 | No substantial evidence section without an inline citation | advisory | CI |
| R14 | The argument survives an adversarial read | blocking | human |
| R15 | The recommendation is actionable | blocking | human |

R14 and R15 are where the merge decision actually lives. R1–R13 exist to make sure a reviewer
spends their attention there instead of on shape.

## 6. What this contract covers

**All four kinds**, on one template. Verification (#13), a resolved question (#14), a survey
(#4) and an infrastructure question (#27) were checked against it and differ only in `kind:`
and in whether §0.1 is present. Splitting the template per kind would have produced four
templates differing in one field.

It does **not** cover notebook entries (#11), ADRs (`docs/adr/`), or prototype write-ups
like this one. Those are different artifacts with different readers.

[`PROTOCOL.md` §5]: https://github.com/NGL321/mosaic/blob/main/PROTOCOL.md
