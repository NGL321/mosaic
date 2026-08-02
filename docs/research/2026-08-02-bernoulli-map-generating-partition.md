---
ticket: 106
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 6
debt: [126, 127]
supersedes: null
---

# The (p, 1−p) Bernoulli map's kink partition is generating, and its `E = 0` is the fragile half of the claim

**Ticket:** [#106 — The skew Bernoulli map's generating partition and Kolmogorov–Sinai entropy are asserted, not read](https://github.com/NGL321/mosaic/issues/106)
**Map:** [#1 — Founding charter for Mosaic](https://github.com/NGL321/mosaic/issues/1)
**Date:** 2026-08-02
**Provenance:** machine-produced, unverified by Noah. Six primary sources were opened and read directly, five of them in full: Barrionuevo–Burton–Dajani–Kraaikamp's 1996 *Acta Arithmetica* paper (17 pp., publisher's scan), Kolmogorov's 1958 *Doklady* note (4 pp., Russian original, Math-Net.Ru scan), Rokhlin's 1967 *Uspekhi* lecture course (54 pp., Russian original, Math-Net.Ru scan — §§3, 9, 10 read closely, the rest skimmed), Sinai's own four-page exposition *Metric Entropy of Dynamical System* from his Princeton page, Sarig's *Lecture Notes on Ergodic Theory* (ch. 4 read closely), and Crutchfield & Feldman's 2003 entropy-convergence paper (definitions and the IID example read closely). Nothing here is recalled; every theorem is quoted from the text named beside it. Sinai's 1959 *Doklady* note itself was **not** reached — see *Sources not reached*. The numerical half is this session's own computation, run once, and its script is in the repository beside this file.

---

## 0. Verdict

| | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1.1 | Is there a theorem, with stated hypotheses, giving `h(T) = h(T, ξ)` for generating `ξ`? | **Established** | §1 |
| 1.2 | Does its one-sided form cover this map, which is non-invertible? | **Established** | §1 |
| 1.3 | Is Kolmogorov (1958) the citation for that theorem? | **Refuted** | §1 |
| 2.1 | Is Lebesgue measure invariant for the (p, 1−p) map? | **Established** | §2 |
| 2.2 | Is the partition at the kink generating for it? | **Established** | §2 |
| 2.3 | Is the symbol stream under that partition exactly i.i.d. Bernoulli(p)? | **Established** | §2 |
| 3.1 | Does `h_μ = H(p)` follow by citation rather than by derivation? | **Supported** | §3 |
| 3.2 | Does `E = 0` follow by citation rather than by derivation? | **Supported** | §3 |
| 4.1 | Do the measured coordinates match the cited values under the kink partition? | **Supported** | §4 |
| 4.2 | Does `h_μ` move under a deliberately wrong threshold partition? | **Supported** | §4 |
| 4.3 | Does `E = 0` survive a deliberately wrong threshold partition? | **Refuted** | §4 |
| 4.4 | Was the ticket's premise — that a wrong partition is a *coarse-graining* worry — the right worry? | **Contested** | §4 |

### The one-line verdict

> **The claim holds, and the ticket's two unread steps are both single-sentence quotations from one 1996 paper — but the audit inverts which half of `h_μ = H(p), E = 0` was in danger.** `h_μ` is the robust coordinate: it is pinned to the map by the generating-partition theorem and, measured, it moves by at most 0.077 bits across four deliberately wrong partitions. `E = 0` is the fragile one: it is a property of *this* partition, not of the map, and it moves from 0.004 to **0.867 bits** — from "nothing remembered" to "nearly two symbols' worth" — under a threshold moved from `x = p` to `x = 0.5`.

---

## 1. The theorem, its hypotheses, and who actually proved it

The step the ticket calls unread is the inference *"the symbol stream's `h_μ` is the map's Kolmogorov–Sinai entropy, not an artefact of a fortunate coarse-graining."* The licence for that inference is the **generating-partition theorem**, and it is stated three times in the sources reached, in increasing order of directness for this application.

**Sinai states it himself**, in [*Metric Entropy of Dynamical System*](https://web.math.princeton.edu/facultypapers/Sinai/MetricEntropy2.pdf), a four-page exposition on his Princeton faculty page. He first defines the quantity the theorem is about:

> "**Definition 1.** Entropy of dynamical system `h(T) = sup_ξ h(T, ξ)` where sup is taken over all finite partitions `ξ`."

then the hypothesis:

> "**Definition 2.** A partition `ξ` is called generating partition (or generator) of the dynamical system `(M, M, µ, T)` if the smallest σ-algebra containing all `T^n C_j`, `−∞ < n < ∞`, `1 ≤ j ≤ r`, is `M`."

and then the conclusion, in one line:

> "**Theorem 1.** If `ξ` is a generating partition then `h(T) = h(T, ξ)`."

That is exactly the licence the Mosaic claim needs: without it, `h(T, ξ)` for one chosen `ξ` is a lower bound on `h(T)` and nothing more, since `h(T)` is a supremum over *all* partitions.

**Sinai's own version of the definition is two-sided**, quantified over `−∞ < n < ∞`, which presumes `T` invertible. The (p, 1−p) map is not: it is two-to-one. This gap is not cosmetic and it is where the audit could have failed. It does not, because both other sources state the one-sided form explicitly.

[Rokhlin's 1967 lecture course](https://www.mathnet.ru/eng/rm5788) — read in the Russian original, *Успехи математических наук* 22:5, 3–56 — defines the one-sided generator in §3.5:

> "Измеримое разбиение ξ называется **образующей эндоморфизма** T, если ξ⁻ = ε."

(*"A measurable partition ξ is called a generator of the endomorphism T if ξ⁻ = ε"*, where §3.5 defines `ξ⁻ = ⋁_{i≥0} T^{−i}ξ` and `ε` is the partition into single points.) The theorem is §9.4, after §9.1 defines `h(T) = sup_ξ h(T, ξ)`:

> "**9.4.** Если ξ ∈ Z — образующая эндоморфизма T или двусторонняя образующая автоморфизма T (см. 3.5), то `h(T, ξ) = h(T)`."

(*"If ξ ∈ Z is a generator of the endomorphism T, or a two-sided generator of the automorphism T, then h(T, ξ) = h(T)."*) `Z` is Rokhlin's class of measurable partitions of finite entropy; a two-cell partition trivially qualifies. **This is the form that covers the (p, 1−p) map**, and it is the one to cite.

[Sarig's lecture notes](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/ergodicnotes.pdf) give the same content in modern English, and name the distinction (Definition 4.4, p. 111):

> "A countable measurable partition `α` is called a **generator** for an invertible `(X, B, µ, T)` if `⋁_{i=−∞}^{∞} T^{−i}α = B mod µ`, and a **strong generator**, if `⋁_{i=0}^{∞} T^{−i}α = B mod µ`. (This latter definition makes sense in the non-invertible case as well)"

> "**Theorem 4.4 (Sinai's Generator Theorem).** Let `(X, B, µ, T)` be an invertible ppt. If `α` is a generator of finite entropy, then `h_µ(T) = h_µ(T, α)`. A similar statement holds for non-invertible ppt assuming that `α` is a strong generator."

**The hypotheses, assembled, are exactly four:** `(X, B, µ, T)` is a measure-preserving system on a Lebesgue space; `µ` is `T`-invariant; `α` is a measurable partition of finite entropy; and `⋁_{i≥0} T^{−i}α = B mod µ`. The conclusion is `h_µ(T) = h_µ(T, α)` — the entropy computed from *this one* partition is the supremum over all of them. §2 checks all four against the map.

**Sub-question 1.3 — Refuted, and this is the one genuine correction the audit produces.** The ticket names "Kolmogorov (1958), Sinai (1959) and Rokhlin's generating-partition theory" as the unreached sources. [Kolmogorov's 1958 *Doklady* note](http://www.mathnet.ru/eng/dan22922) was reached and read in the Russian original, and **it does not contain the generating-partition theorem**. It defines `h` for a *quasi-regular* flow via a filtration `𝔊_t = S_t 𝔊_0` satisfying three conditions — monotone, exhausting, trivial intersection — and its Theorems 1 and 2 establish that `M H(𝔊_{t+Δ} | 𝔊_t) = Δh` and that `h` does not depend on which `𝔊_0` is chosen. That is the K-system construction, not a statement about partitions. Sinai's own account says as much: the theorem "was proven by Kolmogorov in his lecture for Bernoulli partitions", and "the proof of this theorem for general case was given in [S1]" — Sinai (1959). **Citing Kolmogorov (1958) for `h(T) = h(T, ξ)` would be citing the wrong paper.** The citations to use are Rokhlin §9.4 and Sinai's Theorem 1.

## 2. The map is a generalized Lüroth series map, and one 1996 paper settles all three steps

The ticket's two unread steps — that the natural partition is generating, and that Lebesgue is invariant with successive symbols independent — are not two separate research problems. They are Lemma 1 and Theorem 1 of a single paper: Barrionuevo, Burton, Dajani and Kraaikamp, ["Ergodic properties of generalized Lüroth series", *Acta Arithmetica* 74 (1996) 311–327](http://matwbn.icm.edu.pl/ksiazki/aa/aa74/aa7442.pdf), read here in the publisher's scan.

**The identification.** §1.2 of that paper defines, for a digit set `D` and disjoint intervals `I_n = (l_n, r_n]` of length `L_n` with `Σ L_n = 1` and `0 < L_i ≤ L_j < 1` for `i > j`, the operator

> "`Tx := (x − l_n)/(r_n − l_n)`, `x ∈ I_n`, `n ∈ D`"

Take `D = {0, 1}`, `I_0 = (p, 1]`, `I_1 = (0, p]`, so `L_0 = 1 − p` and `L_1 = p`. With `p < 1/2` the ordering condition holds. Then `Tx = (x − p)/(1 − p)` on `I_0` and `Tx = x/p` on `I_1`: **this is the (p, 1−p) Bernoulli map**, with `I_∞ = {0}`, a Lebesgue-null set, and with the digit `a_n(x)` being precisely the symbol of `T^{n−1}x` under the partition at the kink. The interval-ordering condition is a labelling convention on which digit is called `0`, not a restriction; the endpoint convention (half-open on the left rather than the right) differs from the Mosaic statement of the map on a countable set, hence `mod 0`.

**Step 1 of the ticket — that the partition is generating.** Lemma 1 (p. 315), last sentence:

> "Furthermore, `(I_n)_{n∈D}` is a generating partition."

with the proof's mechanism given on the same page: the *fundamental interval* `Δ_{k_1…k_n} = {x : a_1(x) = k_1, …, a_n(x) = k_n}` "is an interval with `p_n/q_n` as one endpoint, and having length `1/(s_1…s_n)`", i.e. `∏ L_{k_i}`, which tends to zero. So the `n`-fold refinement of the kink partition consists of intervals of length at most `(1−p)^n → 0`, which generates the Borel σ-algebra. This is the same argument Sarig uses for expanding Markov maps generally (Theorem 4.5, p. 115): *"One checks that the elements of `α_0^{n−1}` are all intervals of length `O(λ^{−n})`. Therefore `α` is a strong generator."* The refinement being **intervals**, and not unions of intervals, is the whole content — §4.3 shows what goes wrong when it fails.

**Step 2 of the ticket — Lebesgue invariance and independence of successive symbols.** Theorem 1 (p. 316):

> "The `(I, ε)`-GLS operator `T_ε` from (8) is measure preserving with respect to Lebesgue measure and Bernoulli."

and Lemma 1's first sentence (p. 315):

> "The stochastic variables `a_1(x), a_2(x), …` corresponding to the `(I, ε)`-GLS operator `T_ε` from (8) are i.i.d. with respect to the Lebesgue measure `λ`, and `λ(a_n = k) = L_k` for `k ∈ D ∪ {∞}`."

With `L_0 = 1 − p`, `L_1 = p`, that says in terms: **the symbol stream under the kink partition is i.i.d. Bernoulli(p)**, and it says it as a theorem, not as a derivation from the map's construction. The proof is the computation `λ(Δ_{k_1…k_n}) = ∏_{i=1}^n L_{k_i}` — the cylinder measures factorise exactly, which is the "each branch is onto" argument the Mosaic document made, now with a citation under it.

The isomorphism the ticket asks for is Theorem 1's second clause. The paper's Theorem 2 (p. 317) additionally identifies the natural extension `T̄_ε` on `[0,1]²` with `λ × λ` and shows it too is Bernoulli, which matters because the paper's entropy statement (§3) is made about `T̄_ε`.

## 3. `h_μ = H(p)` and `E = 0`, with a citation for each step

**`h_μ = H(p)`.** The 1996 paper writes the conclusion out on p. 319, invoking the theorem of §1 by name:

> "The partition `ξ = {I_k × [0,1]}_{k∈D}` is a generator for `T̄_ε`, which implies that the entropy `h(T̄_ε)` of `T̄_ε` equals `h(T̄_ε, ξ)` (see also [W], p. 96). Therefore, `h(T̄_ε) = − Σ_{k∈D} L_k log L_k`."

For `D = {0,1}`, `L_0 = 1−p`, `L_1 = p`, that is `−p log p − (1−p) log(1−p) = H(p)` exactly, which is the asserted value. Two hypotheses are being carried silently here and both are discharged elsewhere in the sources read. First, the statement is about the *natural extension* `T̄_ε`, not `T_ε`; [Rokhlin §9.9](https://www.mathnet.ru/eng/rm5788) closes that — *"Энтропия эндоморфизма равна энтропии его естественного расширения"* (*"the entropy of an endomorphism equals the entropy of its natural extension"*). Second, the value `−Σ L_k log L_k` for a Bernoulli system is itself a theorem, not arithmetic: Rokhlin §9.10 (*"если T — автоморфизм или эндоморфизм Бернулли с пространством состояний X, то энтропия h(T) равна энтропии пространства X"*), and, with the proof shown, [Sarig Proposition 4.6, p. 113](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/ergodicnotes.pdf): *"The entropy of the Bernoulli shift with probability vector p is `− Σ p_i log p_i`."*

**A second, independent route to the same number** is available and worth recording, because it does not pass through the symbolic coding at all. Sarig's Theorem 4.5 (Rokhlin formula, p. 115) applies to any `T : [0,1] → [0,1]` with a Markov partition into intervals on which `T` is `C¹`, monotone, and `|T'| > λ > 1`, and with an invariant measure `µ`; it gives `h_µ(T) = −∫ log (dµ/dµ∘T) dµ`. The (p, 1−p) map satisfies all three: the kink partition is Markov because each branch is onto, both slopes `1/p` and `1/(1−p)` exceed 1 (at `p = 0.110028`, they are 9.089 and 1.1236, so `λ = 1.1236`), and Lebesgue is invariant by §2. With `µ` Lebesgue the density ratio is `L_A` on branch `A`, giving `h_µ = −Σ L_A log L_A = H(p)` again. **`h_μ = H(p)` is therefore doubly cited, and the second route never mentions a partition's symbols.**

**`E = 0`.** The excess entropy is defined by Crutchfield and Feldman, ["Regularities Unseen, Randomness Observed: Levels of Entropy Convergence"](https://arxiv.org/abs/cond-mat/0102181) (arXiv:cond-mat/0102181; *Chaos* 13 (2003) 25–54), Eq. (48):

> "`E ≡ I_1 = Σ_{L=1}^{∞} [h_µ(L) − h_µ]`"

equivalently, by their Prop. 7 / Eq. (A24), `E = lim_{L→∞}[H(L) − L h_µ]` — the intercept of the asymptote in their Fig. 2, which is exactly what §4's script fits. Their §VI.A settles the value for an i.i.d. source directly:

> "For both coins `H(L)` grows linearly. Hence, `ΔH(L)` is constant for these and all other IID processes."

`ΔH(L) = h_µ(L)` constant means `h_µ(L) = h_µ` for every `L`, so every term of Eq. (48) is zero and `E = 0` **exactly**, not asymptotically. Chaining: the symbol stream is i.i.d. by the 1996 paper's Lemma 1; an i.i.d. source has `E = 0` by Crutchfield & Feldman §VI.A. That is a citation at each step, which is what the ticket asked for.

One further quotation from the same paper is load-bearing for §4 and is recorded here: their Lemma 1 (App. A 8) proves `h_µ(L) ≥ h_µ` and that *"the `h_µ(L)`'s are nonincreasing as `L` increases"*. So a *measured* `h_µ(L) = H(L) − H(L−1)` is an **upper bound** on the true entropy rate. That converts §4's finite-`L` estimates from suggestive into decisive: a measured `h_14` below `H(p)` proves the true rate is below `H(p)`.

## 4. The measurement: how far the coordinates actually move

The ticket offers a second, independent discharge — *"computing the coordinates under a second, deliberately non-generating partition and reporting how far they move"* — and this section does it. The script is [`2026-08-02-bernoulli-map-partitions.py`](https://github.com/NGL321/mosaic/blob/main/docs/research/2026-08-02-bernoulli-map-partitions.py), numpy only, deterministic, in this directory; it was run once and the numbers below are its output verbatim. It iterates the map at `p = 0.110028` for 4 × 10⁶ kept iterates after a 10⁵ burn-in from `x₀ = 0.31415926535897932`, symbolises under five two-cell threshold partitions `ξ_c = {[0,c), [c,1)}` plus the one-cell trivial partition, and estimates `H(L)` for `L = 1…14` by plug-in. Here `H(p) = 0.50000041` bits.

### 4.1 The invariant measure, checked

Before any entropy: the orbit's time average of `x` is **0.500000** against a uniform density's 0.5; the fraction of time in `[0, p)` is **0.110130** against `p = 0.110028`; and the largest deviation of a 1000-bin histogram from flat is **5.00%**, consistent with the ±5.2% that Poisson counting noise on 4000 expected counts produces at three standard deviations over 1000 bins. Lebesgue invariance (§2, Theorem 1 of the [1996 paper](http://matwbn.icm.edu.pl/ksiazki/aa/aa74/aa7442.pdf)) is what the orbit shows.

### 4.2 The coordinates, per partition

`h_L = H(14) − H(13)`; `h_MM` applies the Miller–Madow correction `(m_L − m_{L−1})/(2N ln 2)` for the plug-in estimator's downward bias, with `m_L` the number of occupied `L`-blocks; `E_fit` is the intercept of a five-point least-squares fit of `H(L) = E + hL` over `L = 10…14`. By [Crutchfield & Feldman's Lemma 1](https://arxiv.org/abs/cond-mat/0102181), `h_L` — and `h_MM` up to the correction's own error — is an **upper bound** on that partition's true `h_μ`.

| Partition | `P(sym=1)` | `H(1)` | `h_L` | `h_MM` | `E_fit` | `h_MM − H(p)` | `m₁₄` |
|---|---|---|---|---|---|---|---|
| kink, `c = p` | 0.88987 | 0.50031 | 0.49952 | **0.50003** | **0.00422** | **+0.00003** | 7506 |
| midpoint, `c = 0.5` | 0.50009 | 1.00000 | 0.42297 | 0.42299 | **0.86675** | −0.07701 | 353 |
| quarter, `c = 0.25` | 0.74985 | 0.81151 | 0.48635 | 0.48646 | **0.64138** | −0.01354 | 1691 |
| near-kink, `c = 0.15` | 0.84979 | 0.61037 | 0.49681 | 0.49717 | **0.36610** | −0.00283 | 4715 |
| far, `c = 0.90` | 0.10004 | 0.46913 | 0.13310 | 0.13311 | **0.34838** | −0.36689 | 106 |
| trivial, one cell | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | −0.50000 | 1 |
| *asserted* | — | — | — | *0.50000* | *0* | *0* | — |

**The kink partition reproduces the cited values.** `h_MM = 0.50003` against `H(p) = 0.50000` — three parts in 10⁵. `H(L) − L·H(p)` never exceeds **0.00307** bits over the whole range `L = 1…14`, so the growth curve is a straight line through the origin of slope `H(p)`, which is the signature of exact i.i.d. And the residual `E_fit = 0.00422` is estimator bias, not structure: on the first quarter of the orbit it is **0.01373**, i.e. it falls by a factor of 3.3 when the sample grows fourfold, the roughly-`1/N` behaviour a plug-in bias has and a real `E` does not. Under the same quartering the other partitions' `E_fit` move by at most 0.0070 (midpoint −0.0015, quarter +0.0026, near-kink +0.0070, far −0.0021). **`E = 0` for the kink partition is confirmed; `E ≈ 0.87` for the midpoint partition is confirmed as real.**

**`h_μ` is the robust coordinate.** Every wrong threshold's `h_MM` sits *below* `H(p)`, which by the monotonicity result is proof that its true `h_μ` is below `H(p)` — that is, each of these partitions is **not generating**, and each destroys some entropy. But the amounts are small for three of the four: 0.077 bits at `c = 0.5`, 0.014 at `c = 0.25`, 0.003 at `c = 0.15` against a total of 0.500. Only the extreme `c = 0.90` — where the rarer cell has measure 0.1, capping `h_μ` at `H(0.1) = 0.469` before the dynamics is consulted at all — loses most of it.

**`E` is the fragile coordinate.** It moves from 0.004 to **0.867**, 0.641, 0.366 and 0.348 bits. An observer who moved the threshold from `x = p` to `x = 0.5` and reported the Order-axis coordinates would report an entropy rate 15% low and an excess entropy that had gone from *nothing remembered* to *nearly two symbols' worth of memory in an i.i.d. process*. The `H(L) − L·H(p)` column for `c = 0.5` makes the mechanism visible: it rises to 0.500 at `L = 1`, holds near 0.49 through `L = 3`, then falls through zero at `L ≈ 11.4` and reaches −0.198 at `L = 14`. There is no `L` at which a naive reading of that curve returns the map's coordinates.

### 4.3 A direct test of generation, and the correction to the ticket's premise

The entropy argument shows *that* the wrong partitions are not generating. The script also shows it directly, by measuring the thing the definition is about: the measure-weighted mean **diameter** of the atoms of `ξ ∨ T^{−1}ξ ∨ … ∨ T^{−(L−1)}ξ`, estimated as the spread of orbit points sharing a length-`L` block. A partition is generating exactly when this goes to zero.

| `L` | kink | midpoint | quarter | near-kink | far | trivial | kink, predicted |
|---|---|---|---|---|---|---|---|
| 2 | 0.64660 | 0.42658 | 0.50097 | 0.59809 | 0.80823 | 0.99999 | 0.64667 |
| 8 | 0.17490 | 0.23604 | 0.15683 | 0.16412 | 0.76906 | 0.99999 | 0.17487 |
| 14 | **0.04729** | **0.19112** | 0.06607 | 0.04906 | **0.75430** | 0.99999 | **0.04729** |

The kink column matches `(p² + (1−p)²)^L` — the exact mean cylinder length implied by the [1996 paper's](http://matwbn.icm.edu.pl/ksiazki/aa/aa74/aa7442.pdf) `λ(Δ_{k_1…k_n}) = ∏ L_{k_i}` — to five decimal places at every `L`. That is the generating property measured, not assumed, and it is an independent confirmation of Lemma 1. The `c = 0.90` column is flat at ≈0.755 from `L = 2` to `L = 14`: fourteen observations of that system reduce a reader's uncertainty about `x` by essentially nothing, which is what "not generating" means operationally. The midpoint column is the interesting middle case — still falling at `L = 14` but decisively flattening, 0.214 → 0.200 → 0.191 across `L = 10, 12, 14` while the kink column halves over the same span.

**Sub-question 4.4 — Contested.** The ticket frames the risk as "a fortunate coarse-graining", i.e. that a *coarser* observation might accidentally look simple. That is not what the measurement found, and the mechanism is worth stating because it is the general lesson. `ξ_{0.5}` is not coarser than `ξ_p`: both are two-cell partitions, and by information content `H(1) = 1.000` bits against the kink's `0.500`, `ξ_{0.5}` is the *more* informative single measurement. What it lacks is not resolution but **alignment with the map's discontinuity**. The refinement of `ξ_c` is cut by the preimages of `c` *and* by the preimages of the kink, so its boundary set is dense for any `c` — but its **atoms are unions of the resulting intervals**, one union per itinerary, and only about `2^{h L}` itineraries occur where `2^L` intervals do. Distinct points therefore share an itinerary forever, and the partition fails to generate for a reason that has nothing to do with how coarse it is. **The right warning to carry forward is not "do not coarse-grain" but "symbolise at the map's own discontinuities."** This is the specific, mechanised form of the general worry recorded as [#87](https://github.com/NGL321/mosaic/issues/87) §7.2, and it sharpens it: the free choice in symbolisation costs little in `h_μ` and can cost everything in `E`.

## What this does not establish

### Sources not reached

Three. **Sinai (1959)**, *Dokl. Akad. Nauk SSSR* **124**, 768–771 — the paper that actually proves the generating-partition theorem in general — was not reached: no Math-Net.Ru identifier for it could be located from this session, and the two searches that would have found it returned only secondary accounts. Its content is reached here only through Sinai's own later exposition and Rokhlin §9.4, both of which state the theorem but neither of which is the 1959 note. **Walters, *An Introduction to Ergodic Theory*, p. 96** is the citation the 1996 paper itself hangs the entropy formula on, and it was not opened; the Internet Archive copy is lending-restricted and no first-party text was found. Rokhlin §9.4 and Sarig Theorem 4.4 are used as substitutes, and both state the same result, but the *specific* proposition on Walters p. 96 has not been read. **Ornstein's isomorphism theorem** in the original is likewise unread; it is invoked on p. 319 of the 1996 paper, but nothing in this document's verdict depends on it — the isomorphism used here is the explicit one in that paper's Theorem 1, proved from the cylinder measures.

### Open gaps

Four, in decreasing order of how much they would matter. **First**, `E` under a wrong partition was measured but not predicted: nothing here says what `E(ξ_c)` *should* be as a function of `c`, and the observed non-monotonicity — 0.867 at `c = 0.5`, 0.641 at 0.25, 0.366 at 0.15, but 0.348 at 0.90 — is unexplained. **Second**, whether any threshold `c ≠ p` is generating for this map is left open; the measurement proves the four tested are not, at the resolution available, but `c = 0.15` sits only 0.0028 bits below `H(p)` and the general question is untouched. **Third**, the numerical orbit is a float64 trajectory of a chaotic map whose Lyapunov exponent is `H(p) ln 2 ≈ 0.347` nats, so the computed orbit decorrelates from the true orbit of `x₀` within about 106 iterations; the results are defended by uniform hyperbolicity and shadowing, and by the orbit's measured flatness, but no shadowing bound was computed and no arbitrary-precision run was done as a control. **Fourth**, `E` is estimated at `L ≤ 14` for processes that plainly have not converged by `L = 14`; the reported `E_fit` for the wrong partitions are therefore *lower* bounds on their true `E`, which makes the headline gap conservative but leaves the true values unknown.

### Load-bearing ifs

Three. **If the (p, 1−p) map is not the `(I, ε)`-GLS map of §1.2 of the 1996 paper** — if the interval-ordering condition (5) is a real restriction rather than a labelling convention, or if the half-open endpoint convention matters — then Lemma 1 and Theorem 1 do not apply and §2 collapses to the derivation the ticket rejected. This was checked by substituting the definitions and the identification is exact `mod 0`, but it is an identification made by this session, not one stated in the paper. **If the entropy statement on p. 319 of that paper cannot be transferred from the natural extension `T̄_ε` to `T_ε`**, §3's first route fails; it is transferred using Rokhlin §9.9, and if that citation is misread the second route through Sarig's Rokhlin formula still stands, so this if is load-bearing for one argument and not for the verdict. **If the Miller–Madow correction understates the plug-in bias at `L = 14`**, the `near-kink, c = 0.15` row's conclusion — that it is not generating — is not safe: its margin is 0.0028 bits and the correction it received was 0.0004. The other three rows' margins are 10× to 130× larger and are safe against any plausible mis-correction.

## Verification Debt

Two items, both filed, both open. Both come from the numerical half, and the first is the more
important finding of this whole reading.

- **[#126](https://github.com/NGL321/mosaic/issues/126)** — **no prediction for `E(ξ_c)`.** §4 measured
  it at four wrong thresholds and it is **non-monotonic in `|c − p|`**: 0.867 (c = 0.5), 0.641 (0.25),
  0.366 (0.15), 0.348 (0.90). Four data points saying a bad partition does a lot to `E`, and no model
  for what. Carries a second open question: whether *any* `c ≠ p` is generating — `c = 0.15` sits only
  0.0028 bits below `H(p)`, close enough that the numerical argument alone does not settle it.
- **[#127](https://github.com/NGL321/mosaic/issues/127)** — the float64 orbit has **no shadowing bound
  and no arbitrary-precision control**. At λ ≈ 0.347 nats the computed orbit decorrelates from the true
  orbit of its stated `x₀` within ~106 iterations. Uniform hyperbolicity plus the measured density
  flatness defends the statistics in outline, but the load-bearing claim is a *residual* shrinking at
  the right rate — which is what a systematic numerical artefact would imitate.

A third item is folded into [#126](https://github.com/NGL321/mosaic/issues/126) rather than filed
separately: `E_fit` at `L ≤ 14` is a **lower** bound for the unconverged wrong partitions, which makes
the headline gap conservative. It sharpens #126's question without being a separate debt.

## Proposals

Two, both for whoever holds the pen on the document that #106 audits (`docs/research/2026-08-01-third-exclusion-case.md`), and neither applied here.

1. Replace the assertion that the kink partition is generating and that the symbols are i.i.d. with the citation: Barrionuevo, Burton, Dajani & Kraaikamp, *Ergodic properties of generalized Lüroth series*, Acta Arith. 74 (1996) 311–327, **Lemma 1** (i.i.d. digits with `λ(a_n = k) = L_k`; the partition is generating) and **Theorem 1** (Lebesgue-preserving and Bernoulli), taking `D = {0,1}`, `I_0 = (p,1]`, `I_1 = (0,p]`. Cite **Rokhlin (1967) §9.4** — *not* Kolmogorov (1958) — for `h(T, ξ) = h(T)` when `ξ` generates an endomorphism.

2. Add a sentence distinguishing the two coordinates' robustness, in these terms: *"`h_μ = H(p)` is a property of the map, pinned by the generating-partition theorem. `E = 0` is a property of the map read through this partition: measured under a threshold at `x = 0.5` rather than at the kink, `h_μ` falls 0.077 bits while `E` rises from 0.004 to 0.867 bits."*

The `⟦T3 · #106⟧` badge, if any of this lands in `CONTEXT.md`, is Noah's to apply.

## Appendix: primary sources

All six were opened and read directly in the form linked. Retrieval date for all: **retrieved 2026-08-02**.

1. J. Barrionuevo, R. M. Burton, K. Dajani, C. Kraaikamp, "Ergodic properties of generalized Lüroth series", *Acta Arithmetica* **74** (1996), 311–327 — publisher's scan, [matwbn.icm.edu.pl/ksiazki/aa/aa74/aa7442.pdf](http://matwbn.icm.edu.pl/ksiazki/aa/aa74/aa7442.pdf), record at [eudml.org/doc/206855](https://eudml.org/doc/206855). Read in full. §1.2 (the GLS operator), Lemma 1 and Theorem 1 (pp. 315–317), Theorem 2 (p. 317), the entropy statement (p. 319).
2. V. A. Rokhlin, "Лекции по энтропийной теории преобразований с инвариантной мерой", *Успехи математических наук* **22**:5 (1967), 3–56; English translation *Russian Math. Surveys* **22**:5, 1–52, [doi:10.1070/RM1967v022n05ABEH001224](https://doi.org/10.1070/RM1967v022n05ABEH001224) — full text via [www.mathnet.ru/eng/rm5788](https://www.mathnet.ru/eng/rm5788). Russian original read; §3.5 (generator of an endomorphism), §9.1, §9.4, §9.9, §9.10, §10.1 read closely.
3. A. N. Kolmogorov, "Новый метрический инвариант транзитивных динамических систем и автоморфизмов пространств Лебега", *Doklady Akad. Nauk SSSR* **119**:5 (1958), 861–864 — full text via [www.mathnet.ru/eng/dan22922](http://www.mathnet.ru/eng/dan22922). Read in full (4 pp.). Establishes the negative finding in §1.3: this note contains the K-system construction and Theorems 1–2 on the invariance of `h`, and does not contain the generating-partition theorem.
4. Ya. G. Sinai, "Metric Entropy of Dynamical System", Mathematics Department, Princeton University — [web.math.princeton.edu/facultypapers/Sinai/MetricEntropy2.pdf](https://web.math.princeton.edu/facultypapers/Sinai/MetricEntropy2.pdf). Read in full (4 pp.). Definitions 1–2 and Theorem 1, and Sinai's own attribution of the general proof to his 1959 note.
5. O. Sarig, *Lecture Notes on Ergodic Theory*, Weizmann Institute of Science, version dated 3 April 2023 — [weizmann.ac.il/math/sarigo/…/ergodicnotes.pdf](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/ergodicnotes.pdf). Chapter 4 read closely: Definition 4.4 and Theorem 4.4 (Sinai's Generator Theorem, p. 111), Proposition 4.5 (p. 112), Proposition 4.6 (Bernoulli entropy, p. 113), Theorem 4.5 (Rokhlin formula for expanding Markov interval maps, p. 115).
6. J. P. Crutchfield, D. P. Feldman, "Regularities Unseen, Randomness Observed: Levels of Entropy Convergence", *Chaos* **13** (2003), 25–54; SFI Working Paper 01-02-012 — [arxiv.org/abs/cond-mat/0102181](https://arxiv.org/abs/cond-mat/0102181), full text read from the arXiv PDF. Eq. (11) (`H(L)`), Eq. (48) and Prop. 7 / Eq. (A24) (the excess entropy), Lemma 1 of App. A 8 (`h_µ(L)` non-increasing, `h_µ(L) ≥ h_µ`), §VI.A (IID sources).
