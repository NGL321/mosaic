---
ticket: 46
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 3
debt: [47]
supersedes: null
---

# The HDLSS curse-of-dimensionality theorems hold n fixed and send d to infinity, which is not the regime a Mosaic ECA study would occupy

Provenance: the paper under verification ([Hiraoka, Imoto, Kanazawa & Liu, *Curse of Dimensionality on Persistence Diagrams*, arXiv:2404.18194](https://arxiv.org/abs/2404.18194)) was read **in full**, in its author-source rendering, including §1.4 Settings, every numbered statement in §2 and §3, the proofs of Propositions 3.1–3.2, Theorem 3.4, Theorems 3.13–3.17 and 3.19, the §4 normalised-PCA results and their hypotheses, and §5 Discussion. Theorem 4.11's proof was read in statement and in outline only; its Appendix A gamma-function computation was skimmed and is named under *sources not reached*. The claim under verification — that the theorems place a Mosaic ECA study "inside a proven failure regime" — was read at its own source, the [#4 survey](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md) §3.2(c) and §4.1(ii). The (n, d) arithmetic for a Mosaic ECA study in §4 below is **derived here**, not retrieved: no source states it, which is precisely why [#46](https://github.com/NGL321/mosaic/issues/46) exists.

## 0. Verdict

| Sub-question | Verdict | Argued in |
|---|---|---|
| Do the theorems state HDLSS as *n fixed, d → ∞*, with 3 < n < d and essential dimension s fixed? | **Established** | §1 |
| What drives the asymptotics — is it low n, or something else? | **Established** — it is the signal-to-noise collapse, not n | §2 |
| Does the paper supply a finite-d threshold at which diagrams "stop being reliable"? | **Refuted** — it supplies none | §3 |
| Does the HDLSS regime reach the (n, d) a Mosaic ECA study would have? | **Refuted** | §4 |
| Does the paper's noise model transfer to ECA activation point clouds? | **Open** | §4 |
| Does the survey's §4.1(ii) conclusion survive the loss of this step? | **Loose** | §5 |

> **Refuted.** The HDLSS theorems are asymptotics in *d* with *n* held fixed and required to satisfy 3 < n < d; a Mosaic ECA study has n freely growable into the thousands at an ambient dimension fixed by architecture in the low hundreds, so it sits at n ≳ d — outside the theorems' standing hypothesis, not inside the proven failure regime. The survey's citation of Hiraoka et al. at §4.1(ii) does not carry the weight put on it, though the survey's *conclusion* may survive on the separate, empirical Damrich et al. evidence and on a mechanism the paper describes but does not prove in this regime.

## 1. The exact hypotheses: what is fixed and what goes to infinity

The whole of the paper's setting is fixed in [§1.4](https://arxiv.org/abs/2404.18194), and it is narrower than the phrase "high-dimensional data" suggests.

- **The original point cloud.** P = {x₁, …, xₙ} ⊂ ℝᵈ, with each xᵢ = (x₁ᵢ, …, x_{sᵢ}, 0, …, 0)ᵀ. The signal lives in the first **s** coordinates only. The paper: "*n* is called the sample size (3 < n < d), *d* is called the dimension, and *s* is called the essential dimension… The essential dimension *s* is set to be independent of *d* and less than *n*."
- **The noise point cloud.** E = {e₁, …, eₙ} ⊂ ℝᵈ, i.i.d. across points, drawn from a continuous (Lebesgue-absolutely-continuous) distribution with mean zero and covariance **ν·I_d**, ν > 0. The paper additionally assumes "the coordinates of every point in E are i.i.d. as well." Per-coordinate variance ν is a **constant, not a function of d**.
- **The observed point cloud.** P′ = P + E, i.e. x′ᵢ = xᵢ + eᵢ.
- **The asymptotic regime, stated verbatim.** "The terminology HDLSS used in this paper means we consider the asymptotic behavior in the setting where **d tends to infinity but n is fixed**."

Three constraints therefore bind simultaneously and are easy to lose when only theorem statements are read: **n is fixed**, **n < d**, and **s < n with s independent of d**. Every result in §3 and §4 inherits all three. §4 adds a fourth for the normalised-PCA results: eᵢ ~ 𝒩_d(0, I_d), standard Gaussian.

The results themselves, for the record:

- **Theorem 3.13** (Rips): d_B(D̄_N(P), D̄_N(P′)) = √(2νd)/4 + O_ℙ(1) if N = 0, and O_ℙ(1) if N > 0, as d → ∞.
- **Theorem 3.14** (Rips): if D_N(P) ≠ ∅, that bottleneck distance does **not** converge to zero in probability.
- **Theorem 3.15** (Rips): if D_N(P) ≠ ∅, the Hausdorff distance d_H(D_N(P), D_N(P′)) is *eventually unbounded in probability*.
- **Theorem 3.16 / 3.17** (Čech): d_B = O_ℙ(√d), and is eventually unbounded in probability, for every N.
- **Theorem 3.19** classifies the above as *bottleneck inconsistency, sub-class III* (Rips, N > 0), *strong bottleneck inconsistency* (Rips N = 0, and Čech all N), per Definition 3.18.
- **Theorems 4.19 / 4.20**: after normalised PCA onto the first s principal components, both d_B and d_H return to O_ℙ(1) — the partial mitigation.

Note what "unreliable" means technically. In the Rips case the bottleneck distance stays *bounded* (Theorem 3.13, N > 0); what blows up is the Hausdorff distance (Theorem 3.15), i.e. the diagram's birth–death pairs march off to infinity along the diagonal while remaining a bounded matching-distance away from it. The Čech case is worse: the bottleneck distance itself is unbounded. "Persistence diagrams cease to be reliable descriptors" in the abstract is these statements, not a claim that features are randomised.

## 2. What drives it, and what would break it

The engine is [Proposition 3.1](https://arxiv.org/abs/2404.18194), which is a two-line consequence of the paper's own generalisation (Theorem 2.20) of the [Hall–Marron–Neeman geometric representation theorem](https://arxiv.org/abs/2404.18194):

‖x′ᵢ‖ = √(νd) + O_ℙ(1),  ‖x′ᵢ − x′ⱼ‖ = √(2νd) + O_ℙ(1),  ⟨x′ᵢ, x′ⱼ⟩ / (‖x′ᵢ‖‖x′ⱼ‖) = O_ℙ(d^{−1/2}).

The proof of Theorem 2.20 is Chebyshev on ‖z − μ‖² = Σᵢ(zᵢ − ε)²: the mean is νd and the variance is d·𝕍[(z₁ − ε)²], so the standard deviation is O(√d) against a mean of order d, giving ‖z − μ‖² = νd + O_ℙ(√d) and hence ‖z − μ‖ = √(νd) + O_ℙ(1). Nothing deeper than the law of large numbers over coordinates is needed. In Proposition 3.1 the signal terms ‖xᵢ‖², (xᵢ − xⱼ)ᵀ(eᵢ − eⱼ) "only depend on s", which is fixed, so they are swallowed by the O_ℙ(√d) noise fluctuation.

The consequence is that P′ converges in shape to the vertex set of a **regular simplex Δ^{n−1} with scalar √(νd)** — every pairwise distance the same, every pair of vectors asymptotically orthogonal. Lemma 3.3 computes that simplex's Rips diagram exactly: D₀ = {(0, √(2νd)/2)} with multiplicity n−1, and D_N = ∅ for N > 0. The stability theorem (Theorem 2.7, from Chazal et al.) then transfers the closeness of point clouds to closeness of diagrams (Theorem 3.4), and the blow-up follows because that simplex's diagram itself runs away like √d while D(P) stays put.

**So the driver is a signal-to-noise collapse, not a small sample.** Per-coordinate noise variance ν is held constant while the number of coordinates grows, so total noise energy νd → ∞ while the signal, confined to s fixed coordinates, stays O(1). The SNR falls like d^{−1/2}. Every √d in the results traces to this.

**Where n actually enters the proof** is narrow and worth naming precisely: Proposition 2.18 (max and min of *finitely many* O_ℙ(1) sequences are O_ℙ(1)) is what lets the O_ℙ(1) fluctuation in Proposition 3.1 survive the maximum over the n(n−1)/2 pairs in dis(𝒞′) in Theorem 3.4, and again at (22). Theorem 4.11's eigengap divergence is likewise stated "as d → ∞ but m is fixed". Fixed n is used as *finiteness*, so that a max over a constant number of terms costs nothing — not because low n is the source of the pathology.

Four things would break the result, in descending order of relevance:

1. **ν shrinking with d.** If noise energy is budgeted rather than per-coordinate — νd held constant, i.e. ν ∝ 1/d — every √(νd) term is O(1) and the curse vanishes. The theorems say nothing about a fixed total perturbation spread over more coordinates.
2. **Non-isotropic, non-independent noise.** Covariance ν·I_d and i.i.d. coordinates are what make Chebyshev's variance computation d·𝕍[(z₁−ε)²]. Noise with rapidly decaying spectrum — effective rank ≪ d — does not concentrate at √(νd).
3. **s growing with d.** "s independent of d and less than n" is what makes the signal terms negligible. A signal whose dimension grows with the ambient dimension is outside the setting.
4. **n growing with d.** The paper is explicit that it does not cover this — §5(5): "Our work treats the setting where d tends to infinity but n is fixed. This framework also involves the setting where both d and n = n(d) diverge with the ratio d/n → ∞. Since the sample size n varies with d, discussions in this scenario become even more complex." That sentence is the paper telling a reader exactly what it has not proved.

## 3. The paper supplies no finite-d threshold

This matters for any attempt to apply the result to a concrete experiment. Every statement in [the paper](https://arxiv.org/abs/2404.18194) is in the O_ℙ / o_ℙ calculus of Definitions 2.9 and 2.11: "*there exist* a constant C_(ε) and a positive integer M_(ε) such that ℙ(|X_m| ≤ C_(ε)) ≥ 1 − ε holds for every m > M_(ε)". The constants are existential and never exhibited. There is no explicit C, no explicit M, no concentration inequality with numbers in it, and consequently **no d above which the paper certifies that a diagram is unreliable**.

The numerical experiment in §3.2.1 is an illustration, not a threshold: n = 500 points sampled uniformly from [−1,1]², Gaussian noise with ν = 1×10⁻⁵, at d = 1000, 5000, 10000. Note that even the paper's own demonstration uses ν five orders of magnitude below unity to keep the effect visible at a legible scale, and n = 500 < d = 1000 to stay inside its hypothesis.

The operational rule of thumb the survey pairs this with — "no persistent loop is found at all at d ≳ 30" — is [Damrich et al.'s](https://arxiv.org/abs/2311.03087) empirical finding on a planted noisy circle, not Hiraoka et al.'s theorem. The two are doing different work and only one of them yields a number. Any argument that a specific (n, d) is "inside the failure regime" is drawing on the empirical paper while borrowing the authority of the proved one.

## 4. The load-bearing step: what (n, d) a Mosaic ECA study actually has

The [#4 survey](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md) §4.1(ii) reads: "Activation point clouds from a small ECA model would be O(10²–10³) points in O(10²) dimensions. … [Hiraoka et al.](https://arxiv.org/abs/2404.18194) prove persistence diagrams stop being reliable descriptors in exactly the HDLSS regime this study would occupy." The second clause is the inference the paper does not make. Take the two parameters in turn.

**d is fixed by design and modest.** In an ECA study, the ambient dimension is one of: the hidden width of the model whose activations are embedded (the survey's own figure, O(10²); Tang et al.'s comparator is 128), or the lattice width W if the point cloud is built from CA states directly (typically 10¹–10²). Either way d is an architecture or experiment-design constant, chosen once. It is not a quantity the study wants to send to infinity, and there is no scientific pressure to widen it.

**n is essentially free and wants to be large.** Every initial condition of the automaton is a sample. For lattice width W there are 2^W of them — at W = 20, over a million — and the rule can be run to generate as many trajectories, and as many time slices per trajectory, as wanted. The binding constraint on n is not availability but Vietoris–Rips cost, which the survey's own §3.2(f) puts at "a few thousand points with H₀/H₁ is routine" (Tang et al. subsample hidden states to 2,000 precisely for this reason). So the attainable working range is roughly **n ∈ [10³, 10⁴] at d ∈ [10¹, 10²·⁷]**, and n can be pushed further with landmarking or subsampling schemes.

Set that against the hypotheses of §1:

| | Hiraoka et al. require | A Mosaic ECA study has |
|---|---|---|
| relation of n to d | 3 < n < d | n ≳ d, and n ≫ d at any comfortable sample size |
| n as d varies | fixed | free, and increasing n is the cheapest quality improvement available |
| what → ∞ | d | nothing; d is a design constant |
| ratio | d/n → ∞ | d/n → 0 |

**The theorems do not reach it.** The mismatch is not marginal, and it is not one of degree — it is a sign flip. To land inside the paper's setting a Mosaic study would have to deliberately hold its sample count *below* its hidden width and then widen the network without collecting more samples, which is the opposite of what an ECA study is free to do and has no reason to do. Even at the survey's own stated numbers, most of the range O(10²–10³) points at O(10²) dimensions already has n ≥ d, violating the standing hypothesis 3 < n < d outright.

Two further mismatches are independent of the n-versus-d one and would each be enough on their own:

- **The noise model is not the ECA study's noise model.** The paper's E is exogenous, isotropic (covariance ν·I_d), full-rank, i.i.d. across coordinates, and added to a signal confined to s ≪ d fixed coordinates. Variability in a trained network's activation vectors is none of these: coordinates are strongly correlated, the effective rank is far below the width, and there is no clean signal-plus-independent-noise decomposition to point at. Whether an ECA activation cloud exhibits the concentration of Proposition 3.1 is an **empirical question about that cloud**, cheaply answerable by plotting the pairwise-distance histogram, and it is not settled either way by this paper.
- **An asymptotic statement does not evaluate at a point.** As §3 established, there is no finite-d claim to instantiate at (n = 500, d = 128). "This study is inside the regime" treats a limit theorem as though it were a bound.

## 5. What survives of §4.1(ii)

Not nothing, and the distinction is the useful output here.

**What does not survive:** the specific sentence that Hiraoka et al. *prove* the study's regime to be a failure regime. That is a misapplication of the theorem's hypotheses, and a reviewer who reads §1.4 of the paper will find it in under a minute. The claim should be withdrawn rather than softened.

**What does survive, on other evidence:** the mechanism the paper analyses — Euclidean pairwise distances concentrating so that a Rips filtration sweeps a compressed range — is a real hazard that does not require n < d. [Damrich et al. (NeurIPS 2024)](https://arxiv.org/abs/2311.03087), as reported in the survey's §3.2(c), is the load-bearing citation for this, and it is empirical, is at n in the thousands, and is at d ≈ 20–50 — a regime that a Mosaic ECA study genuinely could occupy. The survey's §4.1(ii) conclusion is therefore **Loose**: right for a reason it half-cites and wrong for the reason it emphasises.

**What is now cheap to do.** Because the theorems do not apply, the question of whether distance concentration actually bites is a measurement, not a literature question. Compute the pairwise-distance histogram of the actual activation cloud and report the ratio of its spread to its mean; if that ratio is not small, the Hiraoka mechanism is not operating and the objection is answered directly rather than argued about. This is strictly better than the survey's current mitigation ("apply normalised PCA as recommended by Hiraoka et al."), which imports a fix designed for a regime the study is not in and which the paper itself says is only partial (§5(1): normalised PCA "can not enhance the asymptotic similarity level to the bottleneck consistency level").

## What this does not establish

### Sources not reached

Appendix A of Hiraoka et al. — the gamma-function recurrence and Legendre-duplication computation establishing Theorem A.5/A.6, which underwrites the Wishart eigengap divergence of Theorem 4.11 — was read in statement and outline, not verified line by line. This affects only §4 of the paper, the normalised-PCA mitigation, which none of this document's verdicts depend on. [Damrich et al. (arXiv:2311.03087)](https://arxiv.org/abs/2311.03087) was **not** read for this ticket; §3 and §5 above describe its role only as the survey reports it, and the parenthetical figures ("d ≳ 30", "σ = 0.25") are the survey's, unverified here. Nothing else wanted was unavailable: the paper was reached in full from its author source and every quotation above is from that text.

### Open gaps

Four are open. (1) Whether an ECA activation point cloud *empirically* shows Proposition 3.1-style distance concentration is unmeasured, and §5 proposes the measurement. (2) The regime the paper explicitly leaves open — n = n(d) → ∞ with d/n → ∞ (§5(5)) — is unresolved in the literature as far as this reading goes, and it is the regime an intermediate design would sit in. (3) Nothing here checks whether the survey's *other* HDLSS-adjacent claim, that Tang et al.'s 113–197 points in 128 dimensions is "the exact intersection of both failure regimes", survives the same scrutiny; at n ≈ d it too fails the 3 < n < d hypothesis, but that claim is about a third party's study and was not the ticket. (4) Whether the natural ECA-state point cloud (rather than activations) has any low-dimensional signal structure at all — the paper's s — is untouched.

### Load-bearing ifs

The Refuted verdict on the central sub-question rests on one factual claim about Mosaic and one about the paper. **If** a Mosaic ECA study were in fact constrained to n < d — for instance if the point cloud had to be one point per *rule* (256 elementary rules) or per *neighbourhood* (8), against a hidden width of 512 — then n < d would hold and the objection would need re-examining, though "n fixed while d → ∞" would still not describe it. **If** the paper carried a non-asymptotic bound somewhere this reading missed, §3's Refuted verdict would fall and with it the "an asymptotic does not evaluate at a point" argument in §4; the reading found none, and the O_ℙ definitions in §2.2 are purely existential, but a missed corollary is the shape of error that would matter. The Loose verdict on §4.1(ii) depends on the survey's characterisation of Damrich et al. being accurate, which this document did not check.

## Verification Debt

One item, and it was already on the tracker before this document existed.

- **[#47](https://github.com/NGL321/mosaic/issues/47)** — Damrich et al. (2024), whose failure
  thresholds are read off figures and never reproduced. That ticket was filed against the survey's use
  of the paper; this document **raises its price**. §5 concludes that what actually transfers to a
  Mosaic ECA study is the empirical distance-concentration mechanism, which Damrich carries and
  Hiraoka does not — so Damrich has gone from one of two supports for survey §4.1(ii) to the only
  one. It is now load-bearing alone, and deserves reading at the depth this ticket got.

The second item found here is **not** debt. Survey §3.2(c) calls Tang et al.'s "~113–197 points in 128
dimensions" the exact intersection of both failure regimes; at n ≈ d that violates Hiraoka's standing
`3 < n < d` hypothesis, so half that sentence carries the same defect this document found. It is a
known error in a draft with the correction already written — a task for
[#51](https://github.com/NGL321/mosaic/issues/51), which owns landing that survey, not a step the
programme cannot defend.

## Proposals

Replacement text for the [#4 survey](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md), for whoever owns `research/grokking-eca-tda-survey` to apply.

§4.1(ii), second sentence — replace:

> [Hiraoka et al. (2026)](https://arxiv.org/abs/2404.18194) prove persistence diagrams stop being reliable descriptors in exactly the HDLSS regime this study would occupy.

with:

> [Hiraoka et al. (2026)](https://arxiv.org/abs/2404.18194) prove diagram unreliability in a regime this study would *not* occupy — their HDLSS asymptotic holds the sample size n fixed with 3 < n < d and sends d → ∞, whereas an ECA study has n freely growable into the thousands at an ambient dimension fixed in the low hundreds. What transfers from them is not the theorem but the mechanism: Euclidean pairwise distances concentrating around a common value, which compresses the range a Rips filtration sweeps. Whether that is happening is directly measurable on the actual point cloud (pairwise-distance spread over mean), and the design should report it.

§3.2(c), the Hiraoka paragraph — append:

> Their HDLSS setting is stated precisely: sample size n fixed with 3 < n < d, signal confined to s fixed coordinates with s < n, and i.i.d. isotropic noise of covariance ν·I_d with ν constant in d. The blow-up is a signal-to-noise collapse — noise energy νd grows while an O(1) signal does not — and every result is asymptotic in d with no finite-d threshold. See [`docs/research/2026-08-02-hdlss-persistence-and-eca.md`](https://github.com/NGL321/mosaic/blob/main/docs/research/2026-08-02-hdlss-persistence-and-eca.md).

No amendment to `CONTEXT.md` is proposed: the claim this discharges lives in an unmerged survey, and the tier promotion at the claim site belongs with that survey's landing.

## Appendix: primary sources, all retrieved 2026-08-02

1. Hiraoka, Y., Imoto, Y., Kanazawa, S. & Liu, E., *Curse of Dimensionality on Persistence Diagrams*, **Foundations of Data Science** (2026), arXiv:2404.18194 — record and abstract at [arxiv.org/abs/2404.18194](https://arxiv.org/abs/2404.18194); full text read in the author-source HTML rendering at [ar5iv.labs.arxiv.org/html/2404.18194](https://ar5iv.labs.arxiv.org/html/2404.18194). All quotations in §1, §2, §3 and §5 above are verbatim from that text.
2. NGL321/mosaic, *Grokking, ECA and TDA: survey* (`docs/research/2026-07-25-grokking-eca-tda-survey.md`, branch `research/grokking-eca-tda-survey`), §3.2(c), §3.2(f), §4.1(ii) and §4.2 — the claim under verification, read at source: [github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md).
3. NGL321/mosaic issue #46, *[debt] Hiraoka et al. (2026) HDLSS asymptotics were read at theorem-statement depth* — the ticket, including its statement of the load-bearing step: [github.com/NGL321/mosaic/issues/46](https://github.com/NGL321/mosaic/issues/46).
