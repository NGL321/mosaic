# Tang, Wang, García-Redondo & Monod (2026) — Topological signatures of grokking

Admitted 2026-08-13 by [#199](https://github.com/NGL321/mosaic/issues/199), which split
[#112](https://github.com/NGL321/mosaic/issues/112) into this Source and a reproduction Prospect.

**Reading debt: [#211](https://github.com/NGL321/mosaic/issues/211), open.** While it is open the
reading below is **T3** — machine-produced and unverified. The tier is derived from that issue's
state and is stored nowhere, here included.

**This is the awkward one, and #199 asked whoever worked it to make a judgement rather than follow
the recipe.** The judgement is in [Reproduction](#reproduction): the paper's *correlations* get no
Prospect, because they are unreproducible in principle rather than merely unreproduced; the paper's
*trajectory result* gets one, because it is the claim Mosaic actually leans on and it is fully
specified. A blanket **Refuted** verdict was considered and refused — see there for why.

## Citation

Tang, Y., Wang, Q., García-Redondo, I. & Monod, A. (2026). *Topological Signatures of Grokking.*
Preprint, arXiv [2605.06352](https://arxiv.org/abs/2605.06352) **v1, 7 May 2026** — the only version.
Comments: 19 pages, 14 figures, 2 tables. No journal reference.

**Retrieval route.** arXiv record `https://arxiv.org/abs/2605.06352`, **status: 200**, checked
2026-08-13 and 2026-08-02. Full text at `https://arxiv.org/html/2605.06352v1`, **status: 200, read**;
Table 1's cell values and the §3–§4 sentences below were re-read there this session. The PDF
rendering `https://arxiv.org/pdf/2605.06352v1`, **status: 200**, was read end to end on 2026-08-02 by
`docs/research/2026-08-02-tang-topological-signatures-recheck.md` and agrees with the HTML cell for
cell.

**Two renderings are named because the audit turned on comparing them.** The disputed values sit in a
LaTeX table, and the per-cell **bold** markers that carry the paper's significance claim survive only
in the HTML's `ltx_font_bold` spans — PDF text extraction drops them.

**No artifacts exist, and this is a finding rather than a retrieval failure.** There is no code- or
data-availability statement, no supplementary material, no repository link in the nineteen pages, and
no code link on the arXiv record; `github`, `zenodo`, `availab` and `available` return nothing in the
body of either rendering. The correlations below therefore cannot be *recomputed* by anyone outside
the author group — only reimplemented. That was the whole of
[#112](https://github.com/NGL321/mosaic/issues/112).

## Claims

Persistent homology is Vietoris–Rips (Ripser) in degrees 0 and 1 on point clouds from the token
embedding matrix of transformers and MLPs trained on modular addition.

### claim-1 — the trajectory signature

**Quoted** — abstract:

> "Using persistent homology on point clouds derived from the embedding matrices of a range of models
> trained on modular arithmetic with varying primes, we identify a clear and consistent topological
> signature of grokking: a sharp increase in both the maximum and total persistence of first homology
> (H₁)."

and §4.1, with the numbers:

> "The maximum persistence value of a point in the degree-1 persistence diagram (H1 max persistence,
> bottom-left panel of Figure 3) exhibits a clear and reproducible transition: after remaining near
> its baseline of ≈0.07–0.08 throughout the memorization phase, it rises sharply with generalization
> and stabilizes at 0.20–0.25."
>
> "The sum of the persistences of all points in the degree-1 persistence diagram (total H1
> persistence, bottom-right panel) shows a corresponding increase from a baseline of ≈20 to values in
> the range 30–50."

**Rendered** — In a network that groks modular addition, the H₁ persistence of the embedding point
cloud undergoes a step change at the generalisation transition — roughly threefold in the maximum,
and 1.5–2.5× in the total — where it was flat through memorisation. **This is the claim Mosaic
actually leans on**: it is the paper's headline, it is the reason `#4`'s survey holds Tang et al. up
as its only positive precedent for topology detecting a representational transition, and it is the
target of the reproduction Prospect below.

### claim-2 — H₁ max correlates with test accuracy at the embedding layer

**Quoted** — Table 1 (Transformer), row *H₁ Max*, sub-row *Embed*, column *0%*, printed bold:

> +0.77 ± 0.03

**Rendered** — Across training checkpoints of an unperturbed run, the maximum H₁ persistence of the
token-embedding point cloud rank-correlates with test accuracy at ρ = 0.77, with a standard deviation
of 0.03 across five seeds. **The ± is dispersion across seeds, not a confidence interval on ρ** — it
answers *how much does ρ move if I reseed*, never *how far is ρ from zero*.

### claim-3 — the strongest reported correlation, and where it actually sits

**Quoted** — §4.3:

> "Conversely, maximum H₁ persistence exhibited strong positive correlation with test accuracy,
> reaching ρ=0.81 in layer 1 and remaining consistently positive across the same regimes."

and Table 1, row *H₁ Max*, sub-row *Layer 1*, printed bold at *5%* and at *0%*:

> 5%: +0.81 ± 0.05  ·  0%: +0.49 ± 0.08

**Rendered** — The 0.81 figure occurs at **5% label permutation, not in the clean run**. In the clean
Transformer the embedding layer (0.77) beats layer 1 (0.49), and layer 2 is −0.23 ± 0.23, unbolded —
not significant and the wrong sign. So *"up to 0.81 at layer 1"* does **not** license the natural
inference that the signal strengthens with depth in the unperturbed model, and any Mosaic text
quoting it without the condition is asserting something the table denies.

### claim-4 — H₀ total, same layer and condition

**Quoted** — Table 1, row *H₀ Total*, sub-row *Embed*, column *0%*, printed bold:

> −0.75 ± 0.03

**Rendered** — Total H₀ persistence at the embedding layer rank-correlates *negatively* with test
accuracy at −0.75 over the same checkpoints, i.e. connected components merge as the model
generalises.

### claim-5 — what the significance marking asserts

**Quoted** — Table 1 caption:

> "Spearman Rank Correlation (ρ) between PH measures and test accuracy (mean ± SD). Bolded values
> indicate p<0.05."

**Rendered** — The paper asserts per-cell significance at p < 0.05 across 140 correlation cells by
bolding them.

**This assertion does not survive contact with the paper's own reported schedule, and Mosaic has
established that rather than suspected it.** See [Corroboration](#corroboration): no sample size
makes the bolding self-consistent, in either table. The claim is recorded here as what the paper
says, frozen; what Mosaic concluded about it is a separate result and lives below.

### claim-6 — the control

**Quoted** — §3, Experimental Setup:

> "To test that the observed signals are not artifacts, as a control setting we additionally run
> experiments where training labels are independently permuted at random while the test set retains
> the original labels."

**Rendered** — The paper does run a null: labels are permuted at 0–100%, and at ≥ 20% the
correlations largely vanish. `#4`'s survey asserted the authors *"report no null model at all"*, and
**that is false** — the correction is
[#49](https://github.com/NGL321/mosaic/issues/49)'s and is recorded in
`docs/research/2026-08-02-tang-topological-signatures-recheck.md` §3.

### claim-7 — the schedule, and the number it never states

**Quoted** — §3:

> "Model weights, optimizer states, and train/test metrics are checkpointed every 500 steps."
>
> "At selected checkpoints we construct point clouds from (i) the rows of the token embedding
> matrix …"

**Rendered** — Checkpoints exist on a 500-step grid over 60,000 steps, so at most 121 of them. But
persistent homology is computed only at *selected* checkpoints, and the paper never says which or how
many. **The n behind every reported p-value is therefore unstated and unrecoverable**, which is what
makes claim-5 unreconstructable rather than merely unverified — and, decisively for the Prospect
below, it is a gap that bites the correlations and leaves claim-1 untouched.

### claim-8 — the direction of the effect

**Quoted** — §4.3:

> "Across all grokking runs of the Transformer model, cross-correlation analysis revealed a consistent
> temporal lag centered around 1,000 training steps between changes in predictive performance and the
> corresponding topological transition."

**Rendered** — Changes in test accuracy **precede** the topological shift by about a thousand steps in
the Transformer. The topological signature is therefore a *lagging descriptor* of grokking, not a
leading indicator of it. This is the paper's own result and it is awkward for the use a reader
naturally wants to make of the paper; it is admitted here so that Mosaic cannot quietly forget it.

## Corroboration

Append-only.

- **2026-08-02** — **Contradicts claim-5, from Mosaic's own arithmetic.**
  `docs/research/2026-08-02-tang-p-values-and-sample-size.md`, on
  [#111](https://github.com/NGL321/mosaic/issues/111), enumerated the exact null permutation
  distribution of Spearman's ρ for n ≤ 10 and used the t-approximation above that, against the
  schedule of claim-7. **No single sample size makes the bolding consistent, in either table.** Table
  1's weakest bolded cell needs n ≥ 197 to reach p < 0.05 while its strongest unbolded cell needs
  n ≤ 35 to miss it; Table 2's needs n ≥ 44 against n ≤ 10. Both brackets are empty and 121 is the
  ceiling the schedule allows. Across the two tables **31 pairs are ordered the wrong way**, with 19
  distinct bolded cells weaker than some unbolded cell beside them. The document's conclusion is that
  the marking on 86 of 140 cells "should be read as decoration, not as a test result."
- **2026-08-02** — **Narrows, and does not remove, the survey's methodological complaint.**
  [#49](https://github.com/NGL321/mosaic/issues/49)'s document §4: no bootstrap, no confidence
  interval, no named test, no correction for 140 comparisons, and — the deepest gap —
  [#113](https://github.com/NGL321/mosaic/issues/113), no null distribution for ρ itself. The
  label-permutation control of claim-6 destroys generalisation, so test accuracy goes flat and
  *nothing* correlates with it; the control therefore cannot discriminate persistent homology from
  any other quantity that steps at the grokking step, and the paper reports such a quantity itself
  (local intrinsic dimension inverts at the same step).
- **2026-08-13** — No independent replication of this paper found in the record. Not searched for
  this session; **not investigated**, rather than none known.

## Reproduction

Append-only.

- **2026-08-13** — **None, and the split is deliberate.**
  [#199](https://github.com/NGL321/mosaic/issues/199) left the judgement to whoever worked it, on the
  evidence. Here it is.

  **The correlations get no Prospect.** Claim-5's significance marking is not merely unverified but
  **unreconstructable in principle** — claim-7 shows the n is unstated, and #111 shows no n exists
  that would rescue it. A reimplementation could recover its own ρ point estimates and compare them
  to the paper's, but it could not corroborate or refute what the table actually asserts, because
  the assertion has no denominator to check against. Filing a Prospect to reproduce a statistic whose
  stated uncertainty Mosaic has already shown to be decoration would buy nothing, and would leave a
  standing invitation to spend a Conjecture's budget on it.

  **The trajectory result gets one.** Claim-1 is a different object: it is what the abstract sells,
  it is what survey §3.2 leans on in holding this paper up as its only positive precedent, and it is
  stated as concrete numbers over a fully specified setup. §3 gives both architectures in full, AdamW
  with its hyperparameters, batch 512, 60,000 steps, the exact seeds 46–50, the primes, Ripser for
  VR-PH, `skdim`/TwoNN for intrinsic dimension, and the wall-clock cost — 8–10 minutes per model on
  an RTX 3070 laptop, ~2 minutes CPU for the PH step. **The one thing a reimplementation must guess
  — the checkpoint subset — is exactly the thing claim-1 does not depend on.** So the trajectory is
  reproducible from the paper as printed, at a cost of hours rather than tens of GPU-hours, while the
  correlations are not reproducible at any cost. Filed on the backlog —
  [#109 comment](https://github.com/NGL321/mosaic/issues/109#issuecomment-5286746289).

  **A blanket Refuted verdict was considered and refused.** #199 floated it — *"the honest entry may
  be a Source with a Refuted verdict and no reproduction at all"* — and it overstates what Mosaic
  holds in two directions. Nothing here has been reproduced, so **Refuted** would be a reproduction
  verdict with no reproduction behind it, which is the precise thing
  `literature/README.md` exists to prevent. And the record does not support it on the merits: the
  three quoted correlations are verbatim and correctly located, the survey's headline objection to
  the paper turned out to be **wrong** (claim-6), and what replaces it is a set of narrower
  objections about warrant — an unstated n, no multiplicity correction, five-seed SDs standing in for
  intervals, a control that cannot discriminate, and a lag that runs the wrong way. Those bear on
  what the paper's numbers are *worth*, not on whether the numbers are *there*. Recording that
  distinction is the entire point of holding claims twice.
