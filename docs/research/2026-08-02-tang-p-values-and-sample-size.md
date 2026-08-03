---
ticket: 111
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 4
debt: []
supersedes: null
---

# No sample size reconciles Tang et al.'s bolding: the p-values are not merely unstated, they are unreconstructable

The preprint was reached and read directly in both first-party renderings of v1 — the
[arXiv HTML](https://arxiv.org/html/2605.06352v1) and the
[PDF](https://arxiv.org/pdf/2605.06352v1) — and the training schedule of §3, the two correlation
tables, and their captions were transcribed from the HTML and then re-read cell for cell against the
PDF text layer, which agrees on every value. The per-cell **bold** markers that carry the paper's
significance claim were recovered from the HTML's `ltx_font_bold` spans, because bold does not
survive PDF text extraction; individual spans were spot-checked against the raw markup. Nothing was
retrieved from an abstract, a search result, or recollection. The critical values in §2 were
**computed here**, not looked up: exactly, by enumerating the full null permutation distribution of
Spearman's ρ for n ≤ 10, and by the standard t-approximation above that. The script is
[`2026-08-02-tang-p-value-reconstruction.py`](./2026-08-02-tang-p-value-reconstruction.py) beside
this file; every number below is its output. I did not contact the authors, and I did not read the
plots themselves — only their captions and axes as rendered in text.

## 0. Verdict

| Sub-question | Verdict | Where argued |
|---|---|---|
| n — the checkpoints entering each Spearman ρ — can be recovered from the reported schedule | **Refuted** | §1 |
| The schedule nonetheless bounds n from above, at 121 checkpoints per run | **Established** | §1 |
| Some single n makes Table 1's bolding self-consistent | **Refuted** | §2 |
| Some single n makes Table 2's bolding self-consistent | **Refuted** | §2 |
| The ticket's pair — bolded `+0.14 ± 0.51` beside unbolded `+0.33 ± 0.16` — is reconcilable at some n | **Refuted** | §2 |
| `+0.14 ± 0.51` could be significant at *any* n the reported schedule permits | **Refuted** | §2 |
| A one-sample t-test on the five per-seed ρ values explains the bolding instead | **Refuted** | §3 |
| Some sign-blind per-seed rule could have produced the pattern | **Open** | §3 |
| The bolding tracks \|ρ\| approximately, at an effective n near 28 | **Loose** | §4 |
| The [#49](https://github.com/NGL321/mosaic/issues/49) document's counts of bolded cells (48, and 89 of 140) are right | **Refuted** | §4 |
| [#111](https://github.com/NGL321/mosaic/issues/111) is discharged — the p-values cannot be reconstructed, and the bound that fact places on the paper is stated | **Supported** | §5 |

> **Refuted** on the only reading that would have saved the tables: there is no sample size that
> makes the bolding consistent. Table 1's weakest bolded cell needs n ≥ 197 to reach p < 0.05 while
> its strongest unbolded cell needs n ≤ 35 to miss it; Table 2's needs n ≥ 44 against n ≤ 10. Both
> brackets are empty, and 121 checkpoints is the ceiling the schedule allows, so `+0.14 ± 0.51`
> cannot be significant at any n the paper's own design permits. Across the two tables 31 pairs are
> ordered the wrong way: 19 distinct bolded cells are weaker than some unbolded cell beside them.
> The unstated n is therefore not a
> reporting omission that a reader could patch by guessing; the significance marking on 86 of 140
> cells is unreconstructable in principle, and it should be read as decoration, not as a test result.

## 1. What n could be, and the ceiling the schedule puts on it

§3 of the paper is unusually complete about training and silent about exactly one thing.
[The setup](https://arxiv.org/html/2605.06352v1) states, verbatim: "Models are trained for 6×10⁴
gradient steps with a fixed batch size of 512. Model weights, optimizer states, and train/test
metrics are checkpointed every 500 steps." Five seeds (46–50) per configuration. That fixes the
grid of available checkpoints at **121** — steps 0, 500, …, 60,000 — or 120 if step 0 is not
analysed.

But the persistent homology is not computed on all of them. The same section says: "At selected
checkpoints we construct point clouds from (i) the rows of the token embedding matrix … and (ii) the
second-token hidden states after each encoder layer on the test set." *Selected* is the whole
problem. The paper never says which checkpoints, never says how many, and never states a sample size
anywhere: the string does not occur in either rendering, and no table note, caption, or appendix
supplies it. Nor is any test named — §4 of the [#49 document](./2026-08-02-tang-topological-signatures-recheck.md)
established that already, and re-reading confirms it.

So n is unknown, and the candidates are the regular coarsenings of a 500-step cadence: 121, 61, 31,
25, 13, 7. Two pieces of the paper's own evidence push toward the fine end. The persistence diagrams
of Figure 1 are drawn at steps 1, 20,000, 30,000 and 50,000, which tells us only that PH was computed
at more than a handful of moments. The stronger constraint is the cross-correlation result: §4.3
reports "a consistent temporal lag centered around 1,000 training steps" between first differences of
test accuracy and first differences of the PH statistics, with the panels in Figure 12. A CCF over a
sampled series can only resolve lags that are integer multiples of the sampling interval, and the PH
series is one of the two inputs — so a lag of about 1,000 steps requires the PH cadence to be 1,000
steps or finer, i.e. **n ∈ {61, 121}**. That is an inference from a reported result rather than a
statement by the authors, and §2 does not depend on it; it matters only because it points the
opposite way from where the bolding would need n to be.

## 2. No n works, and one cell works at no n at all

For a Spearman ρ at fixed n, every standard two-sided test at α = 0.05 — the t-approximation, the
Fisher-z approximation, and the exact permutation distribution alike — rejects exactly when |ρ|
exceeds a critical value ρ*(n) that falls as n grows. Nothing about the choice of test changes the
*shape* of the rule. So under any single n, the bolded cells must be upward-closed in |ρ|: **no
bolded cell may be weaker than any unbolded cell in the same table.** That gives a bracket needing no
assumption about which test was used, and [the script](./2026-08-02-tang-p-value-reconstruction.py)
computes it.

The critical values, at α = 0.05, two-sided (exact by enumeration for n ≤ 10, t-approximation above):

| n | 7 | 8 | 9 | 10 | 13 | 25 | 31 | 61 | 121 |
|---|---|---|---|---|---|---|---|---|---|
| ρ*(n) | 0.786 | 0.738 | 0.700 | 0.649 | 0.553 | 0.396 | 0.355 | 0.252 | 0.179 |

**Table 1 (Transformer), 60 cells, 45 bolded.** The weakest bolded cell is H₁ Total / Embed / 10%,
`+0.14 ± 0.51`. The strongest unbolded cell is H₁ Total / Layer 1 / 0%, `+0.33 ± 0.16`. These are
exactly the pair [the ticket](https://github.com/NGL321/mosaic/issues/111) names, and they are the
extremes of the table, so checking them checks everything.

- For `+0.14` to be significant: ρ*(n) ≤ 0.14, i.e. **n ≥ 197**.
- For `+0.33` to be insignificant: ρ*(n) > 0.33, i.e. **n ≤ 35**.

The requirements are disjoint by a factor of about 5.6. And 197 is not merely larger than 35 — it is
larger than 121, the total number of checkpoints that exist. **`+0.14 ± 0.51` is the one cell in the
paper that cannot be significant at any n the reported training schedule permits**, even if every
checkpoint were used and even allowing n to vary from cell to cell. One further bolded cell —
H₁ Total / Embed / 5%, `+0.24 ± 0.49` — is likewise weaker than an unbolded one, for 4 inversion
pairs in total.

**Table 2 (MLP), 80 cells, 41 bolded.** The same test, worse. The weakest bolded cell is H₁ Total /
Embed (L0) / 20%, `−0.30 ± 0.09`, needing **n ≥ 44**. The strongest unbolded cell is H₀ Total /
Hidden 1 / 0%, `−0.61 ± 0.36`, needing **n ≤ 10** — and at n ≤ 10 the exact permutation critical value
is used, which is the conservative choice and the one that gives the bolding the most room. Empty
bracket again, and this time **27 inversion pairs across 17 distinct bolded cells**. The `−0.61` cell is doing something odd on its
own account: the row above it, H₀ Max / Hidden 1 / 0%, is `−0.55 ± 0.39` and *is* bolded. A weaker
correlation with a larger seed spread is marked significant while the stronger, tighter one beside it
is not.

Neither table is internally consistent, and they are not consistent with each other either: the n
that minimises disagreement for Table 1 is anywhere in 25–73 (2 cells still wrong), for Table 2 it is
17 (4 still wrong), and the best single n for both at once is 28–30, leaving **7 of 140 cells
contradicted**.

## 3. The alternatives that could have rescued it

Three readings could in principle explain a table where |ρ| does not order the bolding. Two fail on
the paper's own printed numbers; the third survives only by being uncheckable.

**A one-sample t-test across the five seeds — Refuted.** The natural alternative uses the printed SD
rather than n: treat the five per-seed ρ values as a sample and test their mean against zero, so a
cell is significant when |ρ| / SD ≥ t₀.₉₇₅,₄ / √5 = 1.2417. This is testable directly from the tables,
and it does not work. It orders the ticket's pair the *same* wrong way — `+0.14 ± 0.51` gives 0.27,
`+0.33 ± 0.16` gives 2.06 — and it disagrees with the printed bolding on 11 of 140 cells (4 in
Table 1, 7 in Table 2). Ranked by |ρ| / SD there are 22 inversions in Table 1 and 28 in Table 2, more
than under |ρ|. So the bolding is not a monotone function of the seed-level t statistic either.

**A per-cell n that varies — Refuted where it matters.** If different runs contributed different
numbers of analysed checkpoints, the bracket argument weakens to a per-cell one. It does not rescue
anything, because the binding constraint in §2 is the ceiling: no run has more than 121 checkpoints,
ρ*(121) = 0.179, and `+0.14` is below it. Varying n also cannot help Table 2's `−0.61`/`−0.55` pair
without asserting that the MLP embedding-layer runs at the same permutation level were analysed at
wildly different cadences, which the paper's uniform description of the pipeline contradicts.

**A sign-blind per-seed rule — Open, and worse if true.** One family of rules does reproduce
inversions: computing a p-value per seed at the full n and then combining without regard to sign —
"bold if all five seeds are individually significant", or a Fisher combination of two-sided p-values.
Under such a rule `+0.14 ± 0.51` could be bolded if its five seeds were, say, +0.8, +0.7, −0.6, −0.5
and +0.3, all individually beyond ρ*(121) = 0.179 but disagreeing in sign, while `+0.33 ± 0.16` could
be unbolded because one seed of five landed at 0.15. This is consistent with the pattern, and it is
**not checkable from the paper**, because the per-seed ρ values are not printed and
[no code or data is released](https://arxiv.org/abs/2605.06352) ([#112](https://github.com/NGL321/mosaic/issues/112)).
It is also the reading under which the bolding means least: a cell marked *significant* under it is
one whose seeds each departed from zero in *some* direction, which is compatible with the reported
mean ρ being near zero and the effect having no consistent sign. That is precisely the situation the
bolded `+0.14 ± 0.51` describes. A reader who takes the bold to mean "this correlation differs from
zero" would be reading it wrong in exactly the cell the ticket flagged.

## 4. What the bolding does track, and two counts to correct

The pattern is not random — it is roughly a threshold on |ρ| near 0.37, which is ρ*(28). Ninety-five
percent of cells (133 of 140) are consistent with that single cut. What that says is that the bolding
behaves like a threshold applied at an effective n of about 28, which is neither the 121 checkpoints
the schedule provides nor the 61 the cross-correlation result of
[§4.3](https://arxiv.org/html/2605.06352v1) implies, and which no sentence in the paper licenses. At
the n the paper's own CCF analysis points to, the *unbolded* cells become the anomalies: at n = 61,
ρ*(61) = 0.252, so `+0.33`, `−0.61`, `−0.42`, `−0.30` and several others ought all to be significant
and are not. Whichever end of the range is right, the table disagrees with itself somewhere.

Two incidental corrections to the [#49 document](./2026-08-02-tang-topological-signatures-recheck.md),
both from a direct recount of the `ltx_font_bold` spans. It reports "48 of Table 1's 60 cells and 41
of Table 2's 80 cells marked significant" and "89 of 140". Table 2's 41 is right; Table 1's is **45**,
not 48, so the total is **86 of 140**, not 89. Table 1's fifteen unbolded cells are the whole of the
20% permutation column (twelve) plus H₀ Total / Layer 2 / 0%, H₁ Max / Layer 2 / 0% and H₁ Total /
Layer 1 / 0%. Nothing in §3 of that document turns on the difference — its argument is that a paper
tagging most of 140 cells has run *some* test, which stands — but the number is quoted and should be
right. Separately, and smaller: Figure 12's cross-correlation panels are labelled
P_frac ∈ {1%, 2%, 5%, 10%}, and 2% is not a column of Table 1, whose columns are {0, 1, 5, 10, 20}%.
The ablation grid in the figures and the ablation grid in the tables are not the same grid.

## 5. What this bounds

[#111](https://github.com/NGL321/mosaic/issues/111) asked for one of three outcomes: recover n from
the authors, establish it from the schedule and show the bolding consistent with it, or record that
it cannot be recovered. The third has happened, and in a stronger form than the ticket anticipated.
It is not that n is missing and the significance claims are therefore unverified-but-plausible; it is
that **no value of n exists** under which the printed table is a correct rendering of a Spearman test
at p < 0.05. One of three things is true, and the paper does not let a reader tell which: the
significance test is not the one every reader will assume, the bolding was applied by hand or by a
script with a bug, or the tables were assembled from runs with denominators that vary in an unstated
way. All three are reasons to stop treating the bold as evidence.

The practical bound. The paper's headline claim is a *trajectory* claim — H₁ maximum and total
persistence rise sharply at the grokking step while local intrinsic dimension falls — and that claim
is carried by figures, not by these tables. It is untouched by this document. What is touched is the
Appendix C correlation evidence and the label-permutation ablation resting on it, which is exactly the
evidence [#49](https://github.com/NGL321/mosaic/issues/49) found the survey to have been leaning on
when it wrongly said there was no null model. The permutation *control* survives — the 20% and 100%
columns collapse toward zero, and that is visible in the point estimates without reference to any
p-value. The *significance marking* does not survive. Any use of Tang et al. downstream should cite
the collapse of the correlation magnitudes under label permutation and should not cite "significant
at p < 0.05", because that phrase in this paper cannot be given a denominator.

## What this does not establish

### Sources not reached

I did not contact the authors, who are the one party who could say what n is and what test produced
the p-values; the ticket names that as the other discharge route and it remains available, and an
answer from them would replace §2's negative result with a positive one only if it also explained the
inversions. I did not look for the per-seed ρ values in any form outside the preprint — there are
none in it, and §5 of the [#49 document](./2026-08-02-tang-topological-signatures-recheck.md)
established that no code or data is released — so §3's sign-blind rule is untested rather than
rejected. I read the figure *captions* and the axis descriptions as rendered in text, but not the
plotted images themselves; a checkpoint count legible only as tick marks in Figure 11 or 13 would
supply the n, and would not change §2, because §2's contradiction holds for every n simultaneously.

### Open gaps

Which of the three explanations in §5 is true is open and is answerable only by the authors or by
released code. Whether the same inconsistency extends to the paper's other quantitative claims — the
LID numbers, the Fourier restricted/excluded accuracies, the trajectory magnitudes in §4.1 — is
untested; this document audited two tables, and a table-generation fault is the kind of thing that
does not stay in one table. Whether the grid mismatch noted in §4 (Figure 12's 2% panel against
Table 1's columns) reflects runs that exist but are untabulated, or a mislabelled figure, is open.
And the substantive question underneath all of it is still the one
[#113](https://github.com/NGL321/mosaic/issues/113) holds: even a correctly computed p would not tell
you that persistent homology beats any other quantity that steps at the grokking step.

### Load-bearing ifs

The whole of §2 rests on the premise that the paper's bolding is meant as a per-cell test of the
reported ρ against zero at a common n — which is what both captions say and what any reader will
take them to mean. If instead the bold marks something else entirely that the paper failed to
describe (a per-seed conjunction, as in §3; a significance transferred from a different statistic; a
manual emphasis of "results we consider notable"), then the tables are not wrong, they are
undocumented, and the verdict softens from *inconsistent* to *uninterpretable* — which bounds the
paper's usability just as tightly but blames it differently. §2 also depends on the transcription of
140 cells and their bold flags being correct; the values were checked against two renderings, and the
bold flags against one, so a bold marker lost in the LaTeX-to-HTML conversion would be undetected
here — though it would have to be a marker *added* to `+0.33` and *removed* from `+0.14` to rescue
the ticket's pair. §1's inference bounding the PH cadence at 1,000 steps assumes the CCF was computed
on the PH sampling grid rather than on some finer interpolation, and nothing in §2 depends on it.

## Verification Debt

None. This document discharges [#111](https://github.com/NGL321/mosaic/issues/111) by the third of
the three routes the ticket allowed — recording that the sample size cannot be recovered — and it
files nothing new, because what it found is not a new gap but a harder version of the gap already
tracked. The two live siblings absorb the residue without needing to be restated as fresh tickets:
[#112](https://github.com/NGL321/mosaic/issues/112) already holds that nothing was released, which is
why §3's sign-blind hypothesis cannot be tested, and
[#113](https://github.com/NGL321/mosaic/issues/113) already holds the deeper objection that the
label-permutation control cannot discriminate persistent homology from anything else that moves at the
grokking step. Filing a fourth ticket for "the bolding is also internally inconsistent" would add a
number to the tracker without adding a question anyone could work on: the only action it could name —
ask the authors — is already named on #111 itself and does not become more available by being
re-filed.

## Proposals

Two, both for files this agent should not edit unilaterally.

For `docs/research/2026-08-02-tang-topological-signatures-recheck.md` §3, replace *"recovering the
bold spans from the HTML shows 48 of Table 1's 60 cells and 41 of Table 2's 80 cells marked
significant"* and the following *"tags 89 of 140 cells"* with — *"recovering the bold spans from the
HTML shows 45 of Table 1's 60 cells and 41 of Table 2's 80 cells marked significant, with the
unmarked ones concentrated exactly where the control predicts — the high-permutation columns. A paper
that tags 86 of 140 cells at p < 0.05 has run a significance test."* The correction does not move that
document's verdict; it is a recount.

For the [#4](https://github.com/NGL321/mosaic/issues/4) survey, extending the replacement text that
document already proposes, append — *"and the significance marking cannot be taken at face value: no
sample size makes it self-consistent. Table 1 bolds ρ = +0.14 as p < 0.05, which would require at
least 197 checkpoints, while leaving ρ = +0.33 unbolded, which requires at most 35; the training
schedule provides at most 121. Across both tables 19 bolded cells are weaker than some unbolded cell
beside them.
What survives is the point estimates, which do collapse toward zero under label permutation."*

## Appendix: primary sources

All four retrieved 2026-08-02. The first three are one paper in three first-party renderings, listed
separately because the audit turns on comparing them: the values sit in a LaTeX table, so the HTML
conversion was checked against the PDF text layer cell by cell, and the significance bolding is
legible only in the HTML.

1. Yifan Tang, Qiquan Wang, Inés García-Redondo, Anthea Monod, *Topological Signatures of Grokking*, arXiv:2605.06352v1 [cs.LG], submitted 7 May 2026 — abstract and publisher record; used for the single-version history and to confirm no code or data link exists: https://arxiv.org/abs/2605.06352
2. The same, full text, arXiv HTML rendering of v1 — source of the §3 training schedule and "at selected checkpoints" wording, of all 140 Table 1 and Table 2 cell values, of both table captions, of the §4.3 cross-correlation lag, and of the `ltx_font_bold` markers from which the significance flags were recovered: https://arxiv.org/html/2605.06352v1
3. The same, full text, PDF of v1, 19 pages — read as an independent rendering; used to confirm the HTML conversion altered no tabulated value and that §3 states "checkpointed every 500 steps", "6×10⁴ gradient steps" and "at selected checkpoints" in the typeset paper: https://arxiv.org/pdf/2605.06352v1
4. SciPy, `scipy.stats.spearmanr` — first-party documentation for the test the tables' p-values would ordinarily come from; quoted for its own caveat that the asymptotic p-value "is only accurate for very large samples (>500 observations)" and that "for smaller sample sizes, consider a permutation test", which is why §2 enumerates the exact null distribution for n ≤ 10: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html
