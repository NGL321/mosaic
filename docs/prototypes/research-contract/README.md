# PROTOTYPE — the research-output document contract (#26)

**Throwaway.** Nothing here is meant to merge to `main` as-is. The validated decision lands
as a template plus a checker; this directory is the primary source that produced it, kept on
`prototype/research-output-contract` per the prototype skill.

## The question

> What must a research-track document contain to be mergeable, and what template does an
> agent write it into?

Three tickets had produced documents, each invented from scratch, at least one needing a
follow-up commit to apply review feedback. That revision tax is what #26 exists to remove.

## Run it

```console
python docs/prototypes/research-contract/prototype_tui.py
```

`--dump` prints every pane at once, which is the AFK-readable form.

Keys: `[g]rid` every rule against every document · `[d]<n>` one document in detail ·
`[w]hy` the rationale for each rule · `[b]ite` which constraints discriminate ·
`[1-9a-e]` toggle a rule off and watch which documents flip · `[r]eset` · `[q]uit`.

The toggle is the point. A rule no document fails is describing the corpus rather than
constraining it; a rule every document fails is either the finding or an overreach. Only
the ones in between are doing work, and the `[b]ite` pane labels each one.

## What's here

| | |
|---|---|
| `TEMPLATE.md` | the candidate contract — front matter, section order, citation form, tiering, acceptance criteria |
| `contract.py` | the same contract as a predicate. Pure; the part that would lift into `tools/check_research_doc.py` |
| `prototype_tui.py` | throwaway shell. Not for production |
| `rewrite-2026-07-25-grokking-eca-tda-survey.md` | the #4 survey rewritten into the contract — the test #26 asked for |
| `inputs/2026-07-25-grokking-eca-tda-survey.md` | the survey as written, vendored because it lives on `research/grokking-eca-tda-survey` and never reached `main` |
| `VERDICT.md` | did the template earn its constraints |

The corpus is all four documents that actually exist — #4, #13, #14, #27 — not invented
examples. Rules were written against what the corpus already did, then the survey was
rewritten and the rules re-run. Any rule that only the rewrite passes is content the
contract is *adding*, and has to justify itself in `VERDICT.md`.

## No persistence

Documents are read; nothing is written. Toggled rules live in memory and reset on exit.
