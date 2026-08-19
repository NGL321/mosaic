---
ticket: 47
map: 1
date: 2026-08-03
kind: verification
tier: T3
session: unrecorded
sources: 4
debt: [155, 156]
supersedes: null
---

# Damrich et al.'s failure thresholds, reproduced: the collapse is real, the d ≳ 30 number is not, and the detector fires on nothing

**Provenance.** Machine-produced, unverified. The paper was read directly (arXiv), and
[its released code](https://github.com/berenslab/eff-ph) was read function by function and
re-run — not cited. The numbers below are computed here, on this machine, from a
[script committed alongside this document](2026-08-03-damrich-thresholds-reproduction.py);
they are not read off the paper's figures, which is the whole point of
[#47](https://github.com/NGL321/mosaic/issues/47). What was *not* done is checking that a
detected feature is the planted loop — see [#155](https://github.com/NGL321/mosaic/issues/155).
None of this has been verified by Noah unaided.

## 0. Verdict

> **The failure is real and the threshold is not.** Euclidean VR-PH does collapse on a
> noisy circle in high ambient dimension, and it collapses at Mosaic's sample sizes too —
> but not at d ≳ 30, where the loop is still recovered comfortably. The survey's sharper
> claim, that DTM "collapsed at σ ≈ 0.15" and did worse than Euclidean, is true of one
> DTM family and **false of another the paper's own script enumerates.** And the paper's
> detection criterion fires on **pure noise with no circle underneath** in 30–80% of
> seeds, which means every binary threshold quoted from this literature — the survey's
> included — has an unstated false-positive rate.

| § | Sub-question | Verdict | One-line reason |
|---|---|---|---|
| §2 | Is *"for d ≳ 30 no persistent loop is found at all"* reproducible? | **Refuted** | At d = 30 the loop is recovered in 9/10 seeds with a relative persistence of **1.36**, well clear of the noise floor. Degradation is smooth, and the margin enters the noise floor between d = 40 and d = 50. |
| §2 | Is *"at d = 50 detection fails completely"* reproducible? | **Supported** | Margin 1.10 at d = 50 and 1.05 at d = 100, against a null band of 1.03–1.15. The signal is gone. |
| §3 | Did DTM *"collapse at σ ≈ 0.15"* and do worse than Euclidean? | **Loose** | Exactly right for the `p_radius = ∞` family — 1/10 at σ = 0.15 where Euclidean is 10/10 at σ = 0.20. Wrong for `p_radius = 1`, which holds 10/10 through σ = 0.20 and beats Euclidean at every σ tested. |
| §4 | Did Fermat distances *"not have any effect"*? | **Supported** | Margins 4.26–10.24 against Euclidean's 7.46 at σ = 0.10 — no consistent direction — and ≤ 1.10 at σ = 0.25, indistinguishable from Euclidean. |
| §5 | Do the thresholds hold at the n a Mosaic ECA study would have? | **Supported** | At d = 50, σ = 0.25 the margin is 1.02–1.22 across n = 100 … 2000, inside the null band at every n. Small n does not rescue it. |
| §6 | Is the paper's detection criterion a detector? | **Refuted** | On isotropic Gaussian noise with no circle at all, `wide_gap_score` reports a detection in 30–80% of seeds. It counts features above a gap; it does not test for a loop. |

---

## 1. What was run, and why not the paper's own harness

[The released code](https://github.com/berenslab/eff-ph) is the specification here, and it is
used as one — read function by function, transcribed with source line numbers, and re-run.
It is not imported, for two reasons that are worth stating because they bound what this
document establishes:

- `utils/dist_utils.py` imports `umap`, `openTSNE` and the authors' own
  [`vis_utils`](https://github.com/sdamrich/vis_utils) at module scope, for spectral and
  neighbour-embedding distances this reproduction does not need. The three distances it
  *does* need — Euclidean, Fermat, DTM — are pure `numpy`/`scipy` and are transcribed
  verbatim.
- `utils/utils.py` shells out to a **modified** Ripser build (the interval-matching fork)
  that emits representative cocycles. Persistence *diagrams* are build-independent, so the
  `ripser` PyPI package computes the same thing; representatives are not available, and
  §6 is where that bites.

One detail was checked rather than assumed, because getting it wrong would have silently
changed every DTM number: `vis_utils`'s `kNN_dists` takes `Kmin(K=k+1)[:, 1:]`, i.e. it
**excludes the point itself** from its own k nearest neighbours. The transcription matches.

Hyperparameters are `scripts/compute_ph.py`'s defaults — `toy_circle`, n = 1000, a random
orthonormal embedding into the ambient dimension, isotropic Gaussian noise in all d
dimensions, `max_dim = 1`. Ten seeds rather than the script's three, because several of the
claims below turn on rates rather than on single runs.

**Two numbers are reported per cell, not one.** `detected` is the paper's own
`wide_gap_score` — 1 iff exactly one H1 feature sits above the largest gap in life times.
`rel` is the longest life time divided by the second longest: the *margin*. The margin is
reported because §6 shows the binary alone cannot distinguish a recovered loop from an
empty diagram with one lucky feature in it.

## 2. The dimension threshold — **the survey's number is wrong, its conclusion is not**

Euclidean, σ = 0.25, n = 1000, 10 seeds:

| d | detected | margin |
|---|---|---|
| 2 | 10/10 | 5.07 |
| 5 | 10/10 | 3.43 |
| 10 | 10/10 | 2.43 |
| 20 | 10/10 | 1.57 |
| **30** | **9/10** | **1.36** |
| 40 | 8/10 | 1.19 |
| **50** | **7/10** | **1.10** |
| 100 | 5/10 | 1.05 |

The [#4 survey](https://github.com/NGL321/mosaic/issues/4) states, quoting the paper's prose:
*"for d ≳ 30 no persistent loop is found at all using Euclidean distances."*

**That does not reproduce.** At d = 30 the loop is recovered in nine seeds out of ten, with
a margin of 1.36 — against a null band of 1.03–1.15 established in §6. It is a weakened
signal, not an absent one. The survey's second number, *"at d = 50 detection fails
completely,"* **does** reproduce: 1.10 at d = 50 and 1.05 at d = 100 are inside the null band,
which is what "the loop is gone" looks like.

So the shape of the finding survives and the threshold moves: the collapse is somewhere
between d = 40 and d = 50, not at d ≳ 30. Note also that the **binary is not monotone** —
5/10 at d = 100 is not meaningfully worse than 7/10 at d = 50 — while the **margin is
monotone throughout**. That is the first sign of §6's problem.

## 3. DTM — **true of one family, false of another**

d = 50, n = 1000, 10 seeds. [The paper's script](https://github.com/berenslab/eff-ph/blob/main/scripts/compute_ph.py)
enumerates eighteen DTM configurations; five are run here, spanning both `p_radius` regimes.

| distance | σ=0.05 | σ=0.10 | σ=0.15 | σ=0.20 | σ=0.25 |
|---|---|---|---|---|---|
| euclidean | 10/10 | 10/10 | 10/10 | 10/10 (1.79) | 7/10 (1.10) |
| dtm k=4, p_radius=∞ | 10/10 | 10/10 | **3/10** | 0/10 | 0/10 |
| dtm k=15, p_radius=∞ | 10/10 | 10/10 | **1/10** | 0/10 | 0/10 |
| dtm k=100, p_radius=∞ | 10/10 | 7/10 | **0/10** | 0/10 | 0/10 |
| dtm k=15, p_dtm=2, p_radius=1 | 10/10 | 10/10 | 10/10 (4.04) | 10/10 (1.92) | 6/10 (1.13) |
| dtm k=100, p_dtm=2, p_radius=1 | 10/10 | 10/10 | 10/10 (4.00) | 10/10 (2.07) | 8/10 (1.14) |

The survey's claim is that DTM *"collapsed at σ ≈ 0.15"* and performed *worse* than plain
Euclidean on the ℝ⁵⁰ noisy circle.

For `p_radius = ∞` — the max-aggregated DTM — that is **exactly right**, and sharper than the
prose suggests: collapse is total at σ = 0.15 for k = 100 and near-total for k = 15, in a
regime where plain Euclidean is still at 10/10 with σ a third larger. The diagrams do not
weaken; they empty.

For `p_radius = 1` it is **wrong in both halves.** That family does not collapse at σ = 0.15,
and it is not worse than Euclidean — it is slightly *better* at every σ tested, holding a
margin of ~2.0 at σ = 0.20 where Euclidean is at 1.79.

This is the reproduction's most consequential correction. *"The standard robustness fixes
also fail"* is doing load-bearing work in the survey's argument that a Mosaic study would sit
inside a proven failure regime, and for DTM it is a claim about a hyperparameter family
rather than about DTM. That does not rescue DTM at σ = 0.25, where `p_radius = 1` is at 1.13
— inside the null band — but it does mean the collapse-at-0.15 threshold should not be quoted
unqualified.

## 4. Fermat — **no effect, confirmed**

d = 50, n = 1000, 10 seeds. Fermat is
[`utils/dist_utils.py:177`](https://github.com/berenslab/eff-ph/blob/main/utils/dist_utils.py):
the shortest path under the p-th power of the Euclidean distance.

| distance | σ = 0.10 | σ = 0.25 |
|---|---|---|
| euclidean | 10/10 (7.46) | 7/10 (1.10) |
| fermat p=1 | 10/10 (**7.46**) | 7/10 (**1.10**) |
| fermat p=2 | 10/10 (10.24) | 6/10 (1.09) |
| fermat p=3 | 10/10 (8.75) | 4/10 (1.06) |
| fermat p=5 | 10/10 (5.77) | 4/10 (1.05) |
| fermat p=7 | 10/10 (4.26) | 4/10 (1.05) |

The survey's *"Fermat distances did not have any effect"* holds. At σ = 0.10 the margins
straddle Euclidean's in both directions with no consistent gain; at σ = 0.25 every one is
inside the null band, indistinguishable from Euclidean and from each other.

**A sanity check fell out of this and is worth recording:** Fermat at p = 1 reproduces
Euclidean to the digit — 7.46 and 1.10, both cells. It must, since the p = 1 Fermat distance
is the shortest path on a complete graph of Euclidean distances, and the Euclidean metric
already satisfies the triangle inequality. That the transcription reproduces a known
identity it was not built to reproduce is the cheapest evidence available that the
transcription is right.

## 5. Mosaic's sample size — **the failure is not an artifact of n = 1000**

[#47](https://github.com/NGL321/mosaic/issues/47) asks the question the paper does not:
whether the thresholds hold at the n a Mosaic ECA study would have — O(10²)–O(10³) points —
rather than at the paper's n. Euclidean, σ = 0.25, 10 seeds:

| n | d = 20 | d = 30 | d = 50 |
|---|---|---|---|
| 100 | 9/10 (1.79) | 9/10 (1.39) | 6/10 (**1.12**) |
| 200 | 10/10 (1.59) | 6/10 (1.26) | 7/10 (**1.22**) |
| 500 | 10/10 (1.72) | 9/10 (1.44) | 1/10 (**1.06**) |
| 1000 | 10/10 (1.57) | 9/10 (1.36) | 7/10 (**1.10**) |
| 2000 | 10/10 (1.59) | 9/10 (1.32) | 4/10 (**1.02**) |

**The d = 50 margin is inside the null band at every n**, and the binary detection rate
wanders between 1/10 and 7/10 without a trend. Small n does not rescue the collapse, and it
does not deepen it either — the failure is a property of the ambient dimension and the noise
level, not of the sample size, over the range Mosaic would occupy.

The survey's §4.1(ii) — *"the measurement regime is inside two proven failure regimes"* — is
therefore **strengthened** by this check rather than weakened, which is the opposite of what
one might expect from a threshold that turned out to be wrong in §2. The d ≳ 30 number was
too aggressive; the conclusion drawn from it was not.

## 6. The detector fires on nothing

This was not in [#47](https://github.com/NGL321/mosaic/issues/47)'s brief. It is the reason
§2–§5 report margins.

`wide_gap_score` ([`utils/pd_utils.py:479`](https://github.com/berenslab/eff-ph)) returns 1
iff the number of H1 features above the largest gap in life times equals the ground truth —
here, one. **It never asks whether that feature is the planted loop.** So: run it on
isotropic Gaussian noise, at the same σ, with no circle underneath at all.

| n | d = 20 | d = 30 | d = 50 |
|---|---|---|---|
| 100 | 5/10 (1.09) | 3/10 (1.07) | **8/10** (1.15) |
| 200 | 5/10 (1.08) | 7/10 (1.13) | 3/10 (1.04) |
| 500 | 5/10 (1.05) | 0/10 (1.03) | 5/10 (1.06) |
| 1000 | 8/10 (1.09) | 7/10 (1.10) | 7/10 (1.09) |

**The criterion reports a loop in pure noise 30–80% of the time**, and at n = 100, d = 50 it
does so *more often* (8/10) than it does on the actual circle at the same n and d (6/10).

The margins tell the story the binary cannot. Noise sits at **1.03–1.15**. The circle at
d = 20 sits at 1.57–1.79 and at d = 30 at 1.26–1.44 — outside the band, recoverable. The
circle at d = 50 sits at 1.02–1.22 — **inside the band**, which is what §2 and §5 are
actually reporting.

None of this contradicts Damrich et al.: their paper's contribution is that spectral
distances succeed where these fail, and a criterion with a high false-positive rate makes
that comparison *harder* to win, not easier. What it contradicts is the way the threshold
travels into a survey as a bare number. *"No persistent loop is found at all"* reads as a
statement about topology; the quantity behind it is a statement about the shape of a
diagram, with an uncontrolled error rate.

---

## What this does not establish

### Sources not reached

Everything this document relies on was reached and opened: the paper (arXiv), the `eff-ph`
repository at its current head, `sdamrich/vis_utils` at the `eff-ph-arxiv-v1` tag, and the
`ripser` package. There is no paywall or dead link behind any claim here.

**Two things were reachable and deliberately not run**, which is a different fact and should
not hide inside the sentence above. The interval-matching Ripser fork was not built, so
representative cocycles were never computed
([#155](https://github.com/NGL321/mosaic/issues/155)). And thirteen of the paper's eighteen
DTM configurations were not run — the five in §3 span both `p_radius` regimes, which is what
the claim under test needed, but the grid is not exhausted.

The **paper's own figures were not re-derived**. This reproduces the numbers the survey
quoted from the prose; it does not check that the figures show what the prose says.

### Open gaps

- **Where exactly the collapse sits between d = 40 and d = 50** is not resolved. The sweep jumps from 1.19 to 1.10 and the null band's ceiling is 1.15, so the crossing is inside that interval and was not bracketed.
- **Why the `p_radius = 1` DTM family behaves so differently** from `p_radius = ∞` is not explained here, only measured. The max-aggregation empties the diagram entirely at σ = 0.15 while the sum-aggregation degrades smoothly; that is a large qualitative difference between two rows of the same table in the paper's own script.
- **Whether the low-margin binary detections are the planted loop or an artifact** is exactly what [#155](https://github.com/NGL321/mosaic/issues/155) asks, and it decides how §5 should be read. If they are artifacts, the d = 50 row is worse than reported rather than merely uninformative.
- **The null control uses one null.** Isotropic Gaussian is the natural null for this experiment because it is the noise the experiment adds, but an activation point cloud is not isotropic Gaussian, and the false-positive rate on a realistic null is unmeasured.

### Load-bearing ifs

- **If `wide_gap_score` is not the criterion behind the paper's quoted thresholds**, §2's refutation is aimed at the wrong target. It is the criterion `utils/pd_utils.py` exposes for exactly this experiment and the one the figure notebooks call, but the mapping from figure to function was inferred from the code rather than stated by the authors.
- **If the transcribed distances differ from the originals in any way that matters**, everything here moves. Three independent checks say they do not: the `kNN_dists` self-exclusion was verified against `vis_utils` source, Fermat p = 1 reproduces Euclidean to the digit (§4), and the Euclidean d-sweep is monotone in the margin as the paper's figures are.
- **If the margin statistic is a bad summary**, §6's null band is the wrong yardstick and the conclusions that lean on it — §2's refutation and §5's *strengthened* — weaken with it. The margin was chosen because it separates signal from noise where the binary does not, which is an honest description of an ad-hoc choice and is why [#156](https://github.com/NGL321/mosaic/issues/156) is filed.
- **If Mosaic's activation clouds are far from the (n, d, σ) regime simulated here**, §5 does not transfer. The n range was chosen from the survey's own O(10²)–O(10³) estimate; the ambient dimension and noise level are the paper's, not Mosaic's.

---

## Verification Debt

Two items, both filed, and both created by this document rather than inherited.

1. **The reproduction never checks that the detected feature is the planted loop** — [#155](https://github.com/NGL321/mosaic/issues/155). Persistence diagrams are build-independent, so the `ripser` package computes the same diagrams; representative cocycles are not available from it, and `eff-ph`'s own `all_cohom_correct` / `winding_numbers` machinery was therefore not run. *What would settle it:* build the interval-matching fork and check the winding number of the top feature against the planted circle.
2. **Mosaic has no calibrated statistic for deciding that a loop was recovered** — [#156](https://github.com/NGL321/mosaic/issues/156). §6 is the finding that produced it: the criterion the literature reports thresholds against has an uncontrolled false-positive rate, and the margin used here to work around that has no calibration either. *What would settle it:* choose a statistic, characterise its null by simulation at the (n, d, σ) an actual Inquiry would occupy, and state a threshold with a false-positive rate attached.

**Item 2 is the one that outlives this ticket.** [#47](https://github.com/NGL321/mosaic/issues/47)
is a question about somebody else's numbers; #156 is a question about whether Mosaic can
report a loop at all, and it is the same shape as
[#147](https://github.com/NGL321/mosaic/issues/147) — an estimator nobody has characterised
on finite samples — arriving from a third direction.

---

## Proposals

**None.** No authored file changes on the strength of this document.

Two things follow for other tickets and are recorded here rather than acted on:

- **The [#4 survey](https://github.com/NGL321/mosaic/issues/4)'s §3.2(c) and §4.1(ii) quote the d ≳ 30 threshold**, which §2 refutes. The survey is a record file, so amending it is not a custody question — but it lands under [#51](https://github.com/NGL321/mosaic/issues/51), and editing the text of a document in the same breath as landing it would make the "every line is the original's" check that #51 rests on untrue. The correction belongs in a follow-up commit against the landed document, with this document cited.
- **Any Inquiry proposing persistent homology as an instrument** inherits [#156](https://github.com/NGL321/mosaic/issues/156) as an Adequacy Criterion problem: an instrument whose false-positive rate is unstated cannot pass a machine-decidable test of fitness.

---

## Appendix: primary sources

- Damrich, S., Berens, P. & Kobak, D. (2024). *Persistent Homology for High-dimensional Data Based on Spectral Methods.* NeurIPS 2024. https://arxiv.org/abs/2311.03087
- `berenslab/eff-ph` — the paper's released code, read at the current head of `main` and transcribed with line numbers in [the script](2026-08-03-damrich-thresholds-reproduction.py). https://github.com/berenslab/eff-ph
- `sdamrich/vis_utils`, branch `eff-ph-arxiv-v1` — `kNN_dists`, which fixes whether a point is its own nearest neighbour and so fixes every DTM number. https://github.com/sdamrich/vis_utils
- `ripser` 0.6.15 (PyPI) — the persistence computation used here in place of the paper's modified Ripser build. https://pypi.org/project/ripser/
