---
ticket: 49
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 3
debt: [111, 112, 113]
supersedes: null
---

# Tang et al. do report a null: the survey's "no null model at all" is wrong, and its three quoted numbers are right

The preprint was reached and read end to end, twice and in two renderings: the arXiv HTML of
[v1](https://arxiv.org/html/2605.06352v1) and the [PDF of the same version](https://arxiv.org/pdf/2605.06352v1),
nineteen pages, fourteen figures, two tables — matching the page and figure counts on the
[arXiv abstract record](https://arxiv.org/abs/2605.06352), which is how I satisfied myself that neither
rendering was truncated. The three disputed correlations live in a LaTeX table, so I did not trust the
HTML conversion alone: every value quoted below was read in the HTML and then re-read in the PDF text
layer, and the per-cell **bold** markers that carry the paper's significance claim were recovered from the
HTML's `ltx_font_bold` spans, because bold does not survive PDF text extraction. Nothing here was derived
from an abstract, a search-engine summary, or recollection. Nothing here was recomputed: no code was run,
because there is none to run (§5). The `#4` survey document itself is on another branch and was not read;
the quotes audited here are the ones restated on
[ticket #49](https://github.com/NGL321/mosaic/issues/49), which is a real limit on what this document can
say about the survey's wording (§4 subsections).

## 0. Verdict

| Sub-question | Verdict | Where argued |
|---|---|---|
| ρ = +0.77 ± 0.03 on H₁ max is in the paper verbatim, at the layer and condition claimed | **Supported** | §2 |
| "up to 0.81 at layer 1" is in the paper verbatim | **Supported** | §2 |
| H₀ total at −0.75 ± 0.03 is in the paper verbatim, at the layer and condition claimed | **Supported** | §2 |
| The survey's framing — these as the paper's headline correlations — is faithful to their place in it | **Loose** | §2 |
| "The authors report no null model at all" | **Refuted** | §3 |
| No bootstrap, no confidence interval, no named test, and no multiple-comparison correction anywhere | **Supported** | §4 |
| The sample size behind each reported p < 0.05 can be recovered from the paper | **Refuted** | §4 |
| Code or artifacts are released such that the correlations could be recomputed | **Refuted** | §5 |
| The paper specifies enough for a cheap independent reimplementation | **Supported** | §5 |
| The correlations have been recomputed, so #49 is fully discharged by this document | **Open** | §5 |
| Tang et al. survives as the survey's positive precedent on the shape of its evidence | **Contested** | §6 |

> **Refuted** on the claim that matters: the paper runs an explicit label-permutation control that it
> introduces in so many words as a test "that the observed signals are not artifacts", marks per-cell
> significance at p < 0.05 across 140 correlation cells, and shades ±1 standard deviation over five
> seeds. The three quoted numbers are verbatim and correctly located. The survey's real complaint
> survives only in a much narrower form — no bootstrap, no confidence interval, no named test, no
> correction for multiplicity, and no reported sample size — and that narrower form is worth keeping.

## 1. What the disputed numbers are measurements of

The paper's headline result is not a correlation at all. Sections 4.1 and 4.2 of
[the preprint](https://arxiv.org/html/2605.06352v1) report a *trajectory* claim: applying Vietoris–Rips
persistent homology (via Ripser) to the token-embedding matrix of transformers and MLPs trained on
modular addition for p ∈ {113, 149, 197}, the maximum persistence of H₁ rises from a baseline of ≈0.075–0.08
to 0.20–0.25 at the grokking step, and total H₁ persistence from ≈20 to 30–50, while local intrinsic
dimension inverts, falling from ≈20–25 to ≈5. Those are the numbers the abstract is about.

The Spearman correlations the survey quotes come from somewhere else: §4.3, the label-permutation
ablation, tabulated in Appendix C. The design is that training labels are permuted at a fraction
*P*<sub>frac</sub> ∈ {0%, 1%, 5%, 10%, 20%} (Transformer, Table 1) or {0%, 10%, 20%, 50%, 100%} (MLP,
Table 2), the model is trained for the same fixed 60,000-step budget, and a Spearman rank correlation is
taken between a persistent-homology statistic and test accuracy *across training checkpoints*, then
averaged over five seeds (46–50) with a standard deviation. So each quoted ρ is a within-run,
across-training-time rank correlation, summarised across seeds — not a correlation across models, tasks,
or runs. That is the object being audited, and §2 checks the numbers against it.

## 2. The three numbers, checked cell by cell

All three are in [Table 1](https://arxiv.org/html/2605.06352v1) of the preprint, verbatim, at the layer
and permutation level the survey implies.

**ρ = +0.77 ± 0.03 on H₁ max — Supported.** Table 1, row *H₁ Max*, sub-row *Embed*, column *0%*, reads
`+0.77 ± 0.03`, bolded. The layer is the token-embedding layer and the condition is the unpermuted run.
The `± 0.03` is a standard deviation across the five seeds, not a confidence interval on ρ; the survey's
notation does not say otherwise, but a reader could take it for one.

**"up to 0.81 at layer 1" — Supported.** Both the running text of §4.3 — "maximum H₁ persistence
exhibited strong positive correlation with test accuracy, reaching ρ = 0.81 in layer 1" — and Table 1
carry it. In the table it is row *H₁ Max*, sub-row *Layer 1*, column *5%*: `+0.81 ± 0.05`. Two things a
careless read would miss. First, 0.81 is the maximum over that sub-row and occurs at 5% label
permutation, not in the clean run: at *0%* the same cell is `+0.49 ± 0.08`. Second, "up to 0.81 at layer 1"
therefore does not license the natural inference that the signal strengthens with depth in the
unperturbed model — in the clean Transformer run the embedding layer (0.77) beats layer 1 (0.49) and
layer 2 is `−0.23 ± 0.23`, unbolded, i.e. not significant and the wrong sign.

**H₀ total at −0.75 ± 0.03 — Supported.** Table 1, row *H₀ Total*, sub-row *Embed*, column *0%*, reads
`−0.75 ± 0.03`, bolded. Same layer and same clean condition as the +0.77.

**The framing is Loose.** Three qualifications, none of which makes any quoted digit wrong. (i) These
figures are an appendix table supporting an ablation, not the paper's headline evidence — §1 above. (ii)
They are Transformer-only; Table 2's MLP numbers are visibly weaker and more dispersed in early layers
(embedding-layer H₀ max is `−0.49 ± 0.45` at 0%, i.e. an SD nearly as large as the estimate) and the paper
says so. (iii) The paper's own prose is very slightly generous to itself here: §4.3 says H₀ statistics
remain "consistently below −0.49 across all grokking permutation levels", but H₀ Total at Layer 1, 0% is
exactly −0.49 and the Layer 2 column runs −0.06 and −0.47, above that bound; the sentence is scoped to
"the embedding layer and first layer", so it is defensible, and it is the sort of scoping a quoting
survey drops.

## 3. The central question: the paper reports a null, in three distinct forms

The survey's claim that **the authors report no null model at all** is **Refuted**. I searched the full
text of [both renderings](https://arxiv.org/pdf/2605.06352v1) for `null`, `permutation test`, `bootstrap`,
`confidence`, `resampl`, `surrogate`, `shuffl`, `monte carlo`, `significan`, `p <`, `error bar`, and
`standard deviation`, and read the whole paper besides. Three things are present.

**A control condition, framed as such.** §3, Experimental Setup, in the paragraph on task and data: "To
test that the observed signals are not artifacts, as a control setting we additionally run experiments
where training labels are independently permuted at random while the test set retains the original
labels." This is the paper's null, and §4.3 is where it is exercised: label permutation is swept from 0%
to 100%, and the paper reports that at *P*<sub>frac</sub> ≥ 20% the model fails to generalise within the
budget and "the previously observed correlations between test accuracy and PH measures largely
disappeared". Table 1 bears this out numerically — the entire 20% column collapses to values between
−0.20 and +0.10, none of them bolded — and Table 2's 100% column collapses likewise. Whatever else is
true, a randomised-label control that is stated as an artifact test, run at five corruption levels, and
shown to null out the effect is a null model.

**Per-cell significance marking.** The caption of Table 1 reads "Spearman Rank Correlation (ρ) between PH
measures and test accuracy (mean ± SD). Bolded values indicate p < 0.05"; Table 2's reads "Bold values
indicate statistical significance (p < 0.05)". These are not decorative: recovering the bold spans from
the HTML shows 48 of Table 1's 60 cells and 41 of Table 2's 80 cells marked significant, with the
unmarked ones concentrated exactly where the control predicts — the high-permutation columns. A paper
that tags 89 of 140 cells at p < 0.05 has run a significance test.

**Dispersion bands.** Every trajectory figure is "averaged across seeds (±1 std. shaded)" (Figure 3
caption and throughout), and every table cell carries mean ± SD over the five fixed seeds. Not a
confidence interval — see §4 — but it is a reported band, and the survey's phrasing denies even that.

There is also a fourth thing the survey seems not to have noticed, which is evidence about the *direction*
of the effect rather than its existence: §4.3 and Appendix C.1 report a cross-correlation analysis on the
first differences of test accuracy and the PH statistics, and find for the Transformer a consistent lag of
about 1,000 steps in which "changes in test accuracy consistently preceded shifts in the PH statistics".
For the MLP (Appendix C.2, Figure 14) the peak is near zero lag. This is a real, and slightly awkward,
result: it makes the topological signature a lagging descriptor of grokking rather than a leading
indicator of it.

## 4. What the paper genuinely does not report

The survey's instinct was right; the sentence it wrote overshot. Narrowed, the complaint holds and is
worth keeping. Against [the full text](https://arxiv.org/html/2605.06352v1):

**No bootstrap and no confidence interval — Supported.** The strings `bootstrap`, `confidence`,
`resampl`, and `monte carlo` do not occur anywhere in the paper. Every dispersion reported is a standard
deviation over five seeds. Five is a small enough n that an SD is a weak summary, and an SD across seeds
answers "how much does ρ move if I reseed?" — not "how far is ρ from zero?", which is the question a
correlation claim needs answered.

**No named significance test — Supported.** The tables assert p < 0.05 and the paper never says what
produced the p. For a Spearman ρ the obvious candidates (the asymptotic t-approximation, an exact
permutation distribution, a Fisher-z interval) disagree materially at small n, and the paper does not
choose one in print.

**No sample size — Refuted that it can be recovered.** This is the sharper version of the same problem.
The p-value for a rank correlation is a function of ρ and n. Checkpoints are saved every 500 steps over
60,000 steps, which would be 120, but §3 says persistent homology is computed only "at selected
checkpoints" and never says how many or which. So n is unstated, and no reported p < 0.05 in either table
can be reconstructed, checked, or reproduced from the paper as printed. Table 1 also contains at least one
pair that looks hard to reconcile under any single n: `+0.14 ± 0.51` (H₁ Total, Embed, 10%) is bolded
significant while `+0.33 ± 0.16` (H₁ Total, Layer 1, 0%) is not.

**No correction for multiplicity — Supported.** `bonferroni`, `fdr`, and `multiple comparison` do not
appear. 140 correlation cells are tested at a nominal 0.05 with no adjustment mentioned.

**No null distribution for ρ itself — Supported, and this is the deepest gap.** The label-permutation
control tests a different hypothesis than it is being asked to carry. It establishes that the PH–accuracy
association vanishes when generalisation is destroyed. It cannot establish that the association is
specific to persistent homology, because at high permutation test accuracy is flat, so *nothing* correlates
with it and the control is uninformative about discrimination. Meanwhile in the clean run both series are
indexed by training step and both undergo a single sharp change at the grokking step, which is exactly the
condition under which any two such series rank-correlate strongly, and under which the i.i.d. assumption
behind a Spearman p-value fails. The paper's own §4.1 supplies the counter-candidate: local intrinsic
dimension inverts at the same step, so it would presumably correlate about as well. A time-series
surrogate null — say, phase-randomised or block-permuted accuracy trajectories — is the missing object,
and no such thing is in the paper.

## 5. Artifacts: nothing released, and a cheap reimplementation instead

**No code or data is released — Refuted that the correlations could be recomputed.** There is no code- or
data-availability statement, no supplementary material, and no repository link anywhere in the nineteen
pages; `github`, `zenodo`, `availab`, and `available` return nothing in the body of either rendering (the
only `github` hits in the HTML are arXiv's own "Report GitHub Issue" page furniture). The
[arXiv record](https://arxiv.org/abs/2605.06352) carries a single version, v1 of 7 May 2026, comments
"19 pages, 14 figures, 2 tables", and no code link. The correlations therefore cannot be recomputed from
released artifacts. By the survey's own stated standard — an unreleased TDA result is what should not be
believed — this is the finding that bites, and it bites harder than the no-null-model claim it replaces.

**But the paper is unusually reimplementable — Supported.** §3 gives, without hedging: both architectures
in full (2-layer pre-LN encoder, d_model 128, 4 heads, d_attn 32, d_ff 256, GELU, no dropout; and a
3×512 MLP over concatenated 128-d embeddings), AdamW with β = (0.9, 0.98), ε = 1e−6, weight decay 0.1,
lr 3e−3, 10-step linear warm-up then constant, batch 512, 60,000 steps, checkpoints every 500; the exact
seeds (46–50); the primes and training fractions; Ripser for Vietoris–Rips PH in degrees 0 and 1 on the
centred, normalised token-embedding rows; and TwoNN via `skdim` for LID on 2,000 subsampled points. It
even gives the cost: 8–10 minutes to train one model on a single RTX 3070 laptop GPU, plus about 2
minutes of CPU for PH and 6 for LID. The full grid is a few tens of GPU-hours at most; a single
ablation column is under an hour. The one thing a reimplementation would have to guess is the checkpoint
subset entering each ρ, which is the same gap as §4's missing n.

**So #49 is not fully discharged — Open.** This document closes the "re-read the preprint for a null
model" half decisively and closes the artifact question decisively. It does not close the "recompute the
correlations" half, and cannot, because recomputation is now a reimplementation and was not run here.

## 6. What this does to the survey's use of Tang et al.

**Contested**, in the specific sense that the survey's conclusion may well stand but its stated reason for
it does not. The survey's verdict "turns on the shape of its evidence", and the shape it asserted —
strong correlations with no null at all — is not the shape the paper has. The paper is better than the
survey said on nulls and controls, and its actual weaknesses are different ones: an unstated n behind
every p, no multiplicity correction, five-seed SDs standing in for intervals, a control that cannot
discriminate persistent homology from the other quantities that move at the same step, a cross-correlation
result showing accuracy leads topology rather than the reverse, and no released code. A survey that cited
those weaknesses would reach a similar level of caution on firmer ground. Until the survey line is
rewritten, it asserts an absence that
[§3 of this document](https://arxiv.org/html/2605.06352v1) refutes from the paper's own §3 and §4.3, which
is the failure mode the ticket predicted — an absence claim is the easiest thing to get wrong — landing on
the party that made it.

## What this does not establish

### Sources not reached

The `#4` survey document itself was not read: it lives on `research/grokking-eca-tda-survey`, not on this
branch, so §6 and the "framing is Loose" row audit the four quotes as
[ticket #49](https://github.com/NGL321/mosaic/issues/49) restates them, not the survey's own sentences in
their own context. If the survey qualifies the "no null model" claim in prose that the ticket compressed,
§6 is aimed at the ticket rather than the survey, and the correction needed is smaller than stated. I also
did not search the authors' personal or institutional pages, or any third-party mirror, for code released
outside the preprint; §5's finding is scoped to the preprint and its arXiv record, which are the primary
sources, and an unlinked repository existing somewhere would not change the fact that the paper does not
point to one.

### Open gaps

Four, all live. Whether an n exists that makes Table 1's bold pattern self-consistent — `+0.14 ± 0.51`
significant beside `+0.33 ± 0.16` not — is answerable by arithmetic once n is known and is not answerable
now. Whether local intrinsic dimension, or weight norm, or any other quantity that steps at the grokking
step correlates with test accuracy as strongly as H₁ max does, which is the discrimination the paper's
control does not perform and the one that decides whether topology is doing work. What a proper
time-series surrogate null does to these ρ values. And whether a reimplementation reproduces the
trajectory result of §4.1 at all — the trajectory claim, not the correlations, is what the abstract sells
and what the survey would actually be leaning on.

### Load-bearing ifs

The whole of §3 rests on the claim that the label-permutation sweep counts as a null model. If a reader
holds that "null model" means specifically a null *distribution for the test statistic* — a permutation or
surrogate distribution of ρ — then the paper has none, §4's last item is the right finding, and the
survey's sentence is defensible under a stricter reading of its own words than I have given it; I have
read "no null model at all" as the broad claim its "at all" implies, and that reading is the one the
verdict depends on. §2's verdicts rest on the arXiv HTML and PDF of v1 being faithful renderings of what
the authors submitted; they agree with each other cell for cell, which is most of what I can check
without the source. §4's "no sample size" rests on there being no statement of the PH checkpoint count
anywhere, including inside a figure image — I read every caption but I did not read the plots
themselves, and a checkpoint count visible only as an axis in Figure 11 or 12 would weaken that item
without touching §3.

## Verification Debt

Three items, all filed, all open. They are the residue of a correction: [#49](https://github.com/NGL321/mosaic/issues/49)
found the survey's headline objection to this paper to be **wrong**, and what replaces it is three
narrower objections that are right.

- **[#111](https://github.com/NGL321/mosaic/issues/111)** — no p-value in either table can be
  reconstructed, because the number of checkpoints entering each Spearman ρ is never stated. Table 1
  bolds `+0.14 ± 0.51` as significant beside an unbolded `+0.33 ± 0.16`, which is hard to reconcile
  under any single n. Argued in §4.
- **[#112](https://github.com/NGL321/mosaic/issues/112)** — no artifacts were released, so the
  correlations can only ever be *reimplemented*, never recomputed. This discharged
  [#49](https://github.com/NGL321/mosaic/issues/49)'s conditional rather than evading it — the ticket
  asked to recompute *if the artifacts exist*, and they do not — but the number stays unverified
  outside the author group, and the [#4](https://github.com/NGL321/mosaic/issues/4) survey's own rule
  about unreleased TDA results lands on its only positive precedent. Argued in §5.
- **[#113](https://github.com/NGL321/mosaic/issues/113)** — the label-permutation control cannot
  discriminate persistent homology from any other quantity that steps at the grokking step, because
  permuting labels destroys grokking and flattens everything. The paper reports such a quantity itself.
  Argued in §4.

[#49](https://github.com/NGL321/mosaic/issues/49) is discharged by this document. Its recomputation half
was conditional on artifacts existing and they do not; what survives of it is
[#112](https://github.com/NGL321/mosaic/issues/112), which states the residue as the reimplementation it
has now become, rather than leaving the original ticket open under a quietly changed meaning.

## Proposals

Two, both for authored files this agent may not edit.

For the `#4` survey, wherever it says the authors report no null model: replace with — *"Tang et al.
report a label-permutation control, per-cell significance marking at p < 0.05 across 140 cells, and ±1 SD
seed bands. What they do not report is any confidence interval or bootstrap, the test that produced the
p-values, the sample size those p-values depend on, any correction for 140 comparisons, or any surrogate
null for a rank correlation between two series that both step once at the same training step. The
correlations cannot be recomputed: no code or data is released."*

For the badge at the claim site, if the claim survives rewriting: `⟦T3 · #49⟧`.

## Appendix: primary sources

All three retrieved 2026-08-02. They are one paper in three first-party renderings, listed separately
because the audit turned on comparing them: the disputed values sit in a LaTeX table, so the HTML
conversion was checked against the PDF text layer cell by cell, and the significance bolding is legible
only in the HTML.

1. Yifan Tang, Qiquan Wang, Inés García-Redondo, Anthea Monod, *Topological Signatures of Grokking*, arXiv:2605.06352v1 [cs.LG], 7 May 2026 — abstract and publisher record, used for version history, page/figure/table counts, and the absence of any code link: https://arxiv.org/abs/2605.06352
2. The same, full text, arXiv HTML rendering of v1 — read end to end; source of §§1–5 quotations, of Table 1 and Table 2 cell values, and of the `ltx_font_bold` significance markers: https://arxiv.org/html/2605.06352v1
3. The same, full text, PDF of v1, 19 pages — read end to end as an independent rendering; used to confirm the HTML conversion had not altered or dropped any tabulated value and that no code-availability statement exists in the typeset paper: https://arxiv.org/pdf/2605.06352v1
