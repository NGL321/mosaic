# Damrich, Berens & Kobak (2024) — Persistent homology for high-dimensional data based on spectral methods

Admitted 2026-08-13 by [#199](https://github.com/NGL321/mosaic/issues/199), which split
[#47](https://github.com/NGL321/mosaic/issues/47) into this Source and its reproduction.

**Reading debt: [#210](https://github.com/NGL321/mosaic/issues/210), open.** While it is open the
reading below is **T3** — machine-produced and unverified. The tier is derived from that issue's
state and is stored nowhere, here included.

**This is the one of the three whose reproduction has already been run.** See
[Reproduction](#reproduction) — it is recorded, not deferred, and it did not come back clean.

## Citation

Damrich, S., Berens, P. & Kobak, D. (2024). *Persistent Homology for High-dimensional Data Based on
Spectral Methods.* **Advances in Neural Information Processing Systems 37 (NeurIPS 2024).**
arXiv [2311.03087](https://arxiv.org/abs/2311.03087), DOI
[10.48550/arXiv.2311.03087](https://doi.org/10.48550/arXiv.2311.03087). Comments: 54 pages, 44
figures.

**The fixed version is arXiv:2311.03087v3, 31 October 2024** — the last of three (v1 6 November 2023,
v2 8 May 2024, v3 31 October 2024) and the one contemporaneous with the NeurIPS 2024 proceedings.
Every locator below is v3's.

**A gap in the record, stated rather than papered over.** Neither
`docs/research/2026-07-25-grokking-eca-tda-survey.md` (read 2026-07-25) nor
`docs/research/2026-08-03-damrich-thresholds-reproduction.md` (read 2026-08-03) names the version it
read. Both postdate v3 by well over a year and both cite the bare `abs/` URL, which serves the
latest version, so v3 is near-certain — but it is an inference, and the two documents' quotes are
matched to v3 here rather than assumed identical to what they saw.

**Retrieval route.** Full text at `https://arxiv.org/html/2311.03087v3`, **status: 200, read**,
2026-08-13; every claim below was located in it this session and is not carried over on trust.
Abstract and version history at `https://arxiv.org/abs/2311.03087`, **status: 200**. Released code at
[`berenslab/eff-ph`](https://github.com/berenslab/eff-ph), **status: 200**, read function by function
and re-run by the reproduction below — this Source's artifacts exist, which is the whole difference
between it and [Tang et al.](../tang-2026-topological-signatures/README.md).

## Claims

The four claims Mosaic actually took, all from `#4`'s survey §3.2(c). Persistence statistics are
Vietoris–Rips H₁ on a noisy circle embedded in ℝ^d with isotropic Gaussian noise in all d dimensions.

### claim-1 — traditional PH fails under high-dimensional noise, and so do its refinements

**Quoted** — §1, Introduction:

> "If data points are sampled from a low-dimensional manifold embedded in a high-dimensional ambient
> space (manifold hypothesis), then the measurement noise typically affects all ambient dimensions.
> In this setting, traditional persistent homology is not robust against even low levels of noise."

and, abstract:

> "The same holds true for existing refinements of persistent homology."

**Rendered** — Where a point cloud's intrinsic dimension is far below its ambient dimension and noise
is isotropic in the ambient space, Vietoris–Rips persistent homology under the Euclidean metric is
not a reliable detector of the manifold's topology, and the published robustness variants of it do
not repair this. **The metric is constitutive of the measurement, not incidental to it** — which is
why an Inquiry proposing PH as an instrument must declare and vary its metric as a designed factor.

### claim-2 — the dimension threshold

**Quoted** — §7.1, *Results on synthetic data*:

> "Using the circle data in ℝ<sup>d</sup>, we found that if the noise level was fixed at σ = 0.25, no
> persistent loop was found using Euclidean distances for d ≳ 30 (Figure 8)."

**Rendered** — At a fixed noise level of σ = 0.25, Euclidean VR-PH recovers no persistent loop from a
planted circle once the ambient dimension reaches roughly 30.

**Refuted by reproduction. See [Reproduction](#reproduction) — the collapse is real, the number is
not.** The claim is not edited here and never will be: it is what the paper says, and the
reproduction is a separate node.

### claim-3 — the robustness fixes that do not work

**Quoted** — §7.1, *Results on synthetic data*:

> "Most other distances outperformed the Euclidean distance, at least in the low noise regime. Fermat
> distance did not have any effect, and neither did DTM distance, which collapsed at σ≈0.15 due to
> our thresholding (Figure 6a)."

**Rendered** — Fermat distances leave the detection of a planted loop essentially unchanged relative
to Euclidean. Distance-to-Measure fails from σ ≈ 0.15, and **the authors attribute that failure to
their own thresholding rather than to DTM**.

**The qualifier is load-bearing and Mosaic dropped it.** The survey quotes *"collapsed at σ ≈ 0.15"*
and omits *"due to our thresholding"*, which converts a statement about one configuration into a
statement about a method. The reproduction found exactly the fault line that qualifier points at: the
collapse is a property of the `p_radius = ∞` DTM family and false of `p_radius = 1`, both of which
are in the paper's own script. A future correction to the survey's sentence is a **new claim** if it
re-quotes the paper, and this one stands.

### claim-4 — the fixes that partly work

**Quoted** — §7.1, *Results on synthetic data*:

> "Geodesics, UMAP/t-SNE graph, and core distance offered only a modest improvement"

**Rendered** — Graph-geodesic and neighbour-embedding-graph distances, and core distance, improve
loop recovery over Euclidean but not enough to restore it. Only the spectral distances the paper
introduces do that.

**Not reproduced.** The reproduction ran Euclidean, Fermat and DTM only.

### Not claimed here

The survey also states that DTM *"performed worse than plain Euclidean on the ℝ⁵⁰ noisy circle"*.
That comparison was **not located in the paper's prose** this session, and it is the survey's gloss
on Figure 6a until someone finds the sentence. It is therefore not admitted as a claim. The
reproduction measured it directly and found it true of one DTM family and false of the other, so
nothing is lost by leaving it out — but it must not be cited as Damrich et al.'s assertion.

The paper's own positive contribution — that diffusion distance and effective resistance *do* recover
the topology, and the closed-form formula for effective resistance — is deliberately not admitted.
Mosaic has taken no premise from it. Admitting a claim nothing steers by is the growth surface
`literature/README.md` warns about.

## Corroboration

Append-only.

- **2026-08-13** — **Hiraoka, Imoto, Kanazawa & Liu**, *Curse of dimensionality on persistence
  diagrams* ([arXiv:2404.18194](https://arxiv.org/abs/2404.18194), Foundations of Data Science 2026),
  was cited by survey §4.1(ii) alongside this paper as the second proof that a Mosaic ECA study sits
  in a failure regime. **It has been withdrawn as support**:
  [#46](https://github.com/NGL321/mosaic/issues/46) found its HDLSS theorems require `d/n → ∞` under
  a standing `3 < n < d`, while an ECA study has `d/n → 0` — the paper closes the door itself at
  §5(5). This Source is now the *sole* support for §4.1(ii). Recorded here because a corroboration
  that was retracted is exactly the thing a reader needs to know and the hardest thing to notice
  later.

## Reproduction

Append-only. **Not an Inquiry**, and the distinction is not pedantry: what follows was a research
task with no posted Conjecture, no frozen Question and no Adequacy Criterion, so it generates **no
confirmatory axiom in either direction** and may not be offered as a leg. It steers, like everything
else on this shelf.

- **2026-08-03** — [#47](https://github.com/NGL321/mosaic/issues/47), on
  [PR #157](https://github.com/NGL321/mosaic/pull/157), document
  `docs/research/2026-08-03-damrich-thresholds-reproduction.md`. Machine-produced, unverified. The
  released code was read function by function, the three needed distances transcribed with source
  line numbers, and the experiment re-run at ten seeds. Per claim:

  | claim | verdict | what came back |
  |---|---|---|
  | claim-2, `d ≳ 30` | **Refuted** | At d = 30 the loop is recovered 9/10 seeds at a margin of 1.36, against a 1.03–1.15 noise floor. The collapse sits between d = 40 and d = 50. |
  | claim-2, "at d = 50 detection fails" | **Corroborated** | Margin 1.10 at d = 50, 1.05 at d = 100 — inside the noise floor. |
  | claim-3, Fermat | **Corroborated** | Margins straddle Euclidean's in both directions at σ = 0.10 and are indistinguishable from it at σ = 0.25. |
  | claim-3, DTM | **Split** | Exactly right for `p_radius = ∞`; false for `p_radius = 1`, which beats Euclidean at every σ tested. The paper's own qualifier — *"due to our thresholding"* — points at this. |
  | claim-4 | not run | — |

  **An unbriefed finding that outlives the ticket.** The paper's detection criterion,
  `wide_gap_score`, reports a loop on isotropic Gaussian noise with no circle underneath in 30–80% of
  seeds. It counts features above a gap; it never asks whether the feature is the planted loop. Every
  binary threshold quoted from this literature therefore carries an unstated false-positive rate.
  Filed as [#156](https://github.com/NGL321/mosaic/issues/156), with
  [#155](https://github.com/NGL321/mosaic/issues/155) for the representative-cocycle check that was
  not run.

  **The refutation does not weaken the use Mosaic made of this paper.** Survey §4.1(ii)'s claim is
  that a Mosaic ECA study's measurement regime sits inside a proven failure regime, and the
  reproduction's §5 checked that at the sample sizes such a study would actually have — the margin is
  inside the noise floor at every n from 100 to 2000. The threshold moved; the conclusion drawn from
  it is **strengthened**. What is refuted is the bare number, and that number is quoted in survey
  §3.2(c) and §4.1(ii) and needs correcting there.

  **This entry is provisional in one respect only.** PR #157 is open. Until it merges there is no
  commit in `main`'s history holding the document this row summarises.
