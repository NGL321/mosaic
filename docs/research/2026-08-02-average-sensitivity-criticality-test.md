---
ticket: 122
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 5
debt: [128, 129]
supersedes: null
---

# Average sensitivity is a real per-instance quantity and a weak per-instance test — the criterion is exact for one step and borrows the annealed limit for everything after it

**Provenance.** Machine-produced, unverified. Four sources were opened and read directly: Shmulevich & Kauffman (2004) in full, from the PubMed Central deposit of the *Phys. Rev. Lett.* text — **not** from the APS typesetting, which returned HTTP 403 and is recorded under *Sources not reached*; Schober & Bossert (2007) from the ar5iv rendering of the arXiv deposit, read for its definitions and theorem statements rather than cover to cover; Manicka, Marques-Pita & Rocha (2022) from the PubMed Central deposit of the *J. R. Soc. Interface* article together with the ar5iv rendering of its arXiv preprint; and Costa, Rozum, Marcus & Rocha (2023) from the PubMed Central deposit of the *Entropy* article. Derrida & Pomeau (1986) is cited here but was **not re-opened in this session** — its equations (14) and (15) are taken from the transcription in [`2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md`](2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md) §3, which read them off a page scan, and this document inherits whatever risk that transcription carries. **Two results here were derived, not retrieved**: the exact one-step identity in §2, and the heterogeneous-bias correction in §4. Both are shown in full so a reader can attack them. Lynch (1995), the theorem Schober & Bossert extend, was reached only through their restatement. None of this has been checked by Noah unaided.

## 0. Verdict

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | What is the exact definition of average sensitivity for a realised Boolean network? | **Established** — the sum of the per-input activities of each node's truth table, averaged over nodes; activity is the fraction of the 2^k input rows on which toggling that input flips the output | §1 |
| 2 | Is it a genuine *per-instance* quantity — computable from a given network with no ensemble, no trajectory and no estimated limit? | **Supported** | §1 |
| 3 | Is the criterion `s̄ = 1`? | **Established** — stated and used as such by the primary source, and by every follow-up read here | §2 |
| 4 | Is `s̄` *exactly* the one-step damage amplification factor of a given network, with no approximation? | **Supported** — derived here, in three lines | §2 |
| 5 | Does the criterion nonetheless require the annealed approximation, an ensemble average, or N → ∞? | **Supported** — not to *define* `s̄`, but to get from one step to the asymptotic regime, which is the whole content of the test | §3 |
| 6 | Do Shmulevich & Kauffman themselves claim per-instance applicability? | **Established** — explicitly, in their closing paragraph, without proof or error bound | §1, §3 |
| 7 | Is the rigorous version — Lynch's theorem as extended by Schober & Bossert — a per-instance statement? | **Refuted** — its λ is an *expectation over the function ensemble*, and its conclusion holds as N → ∞ with probability tending to one | §3 |
| 8 | Does `s̄ = 1` actually decide the regime of realised networks? | **Refuted** — MCC 0.44 and AUC 0.54 against measured Derrida coefficients on 63 empirical models | §5 |
| 9 | Is there a repaired per-instance criterion that does work on realised networks? | **Supported** — effective connectivity, at MCC 0.96, but with a fitted constant | §5 |
| 10 | Does any of this constrain the Informational Capacity axis? | **Refuted** — no source read here computes an entropy rate, a mutual information or a channel capacity | §6 |
| 11 | What does it cost to compute for a given network? | **Established** — exact in Σᵢ kᵢ·2^kᵢ function evaluations; no data, no trajectory, no limit | §6 |
| 12 | Does any primary source compose Derrida & Pomeau's (14) and (15) into `⟨K⟩ · 2p(1−p) = 1`? | **Supported** — Schober & Bossert (2007) with a theorem, Costa et al. (2023) as a standing form | §4 |
| 13 | Is the composed form correct as the secondary literature quotes it? | **Refuted** — it is the product of means where the true quantity is the mean of a product, and the gap is `2⟨K⟩·Var(p)` | §4 |
| 14 | Net: is a cheap per-instance criticality test on discrete-state systems recoverable? | **Supported**, with a qualification that is the whole finding | §7 |

> **The per-instance object exists and the per-instance *theorem* does not.** Average sensitivity `s̄` is computed from a realised network's truth tables alone — no generator, no ensemble parameters, no trajectory, no estimated limit — and it is *exactly*, with no approximation whatsoever, the expected number of nodes flipped one step after a single-bit perturbation. That much is a clean repair of what [#100](https://github.com/NGL321/mosaic/issues/100) found missing. But comparing that number to 1 is a criticality test only if the one-step multiplier extrapolates, and extrapolating it is precisely the annealed approximation in the N → ∞ limit that made `K · 2p(1−p) = 1` non-per-instance in the first place. The extrapolation is not innocent: against measured Derrida coefficients on 63 empirical biological networks the test scores AUC 0.54, which its own authors call "only marginally better than a random toss".

## 1. The definition, and the fact that it is per-instance

[Shmulevich & Kauffman (2004)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) build the quantity in two steps, and the first step is what makes it usable on a realised system.

**Activity.** For a Boolean function `f : {0,1}^K → {0,1}`, the partial derivative with respect to input `j` is

```
∂f(x)/∂x_j  =  f(x^(j,0)) ⊕ f(x^(j,1))
```

with `⊕` addition modulo 2 and `x^(j,k)` the vector `x` with its `j`-th component forced to `k`. The derivative is itself a Boolean function, and "specifies whether a change in the jth input causes a change in the original function f". The **activity** of `x_j` in `f` is its mean over the hypercube:

```
α_j^f  =  2^(−K) · Σ_{x ∈ {0,1}^K}  ∂f(x)/∂x_j
```

which the authors gloss as "a probability that toggling the jth input bit changes the function value, when the input vectors x are distributed uniformly over {0,1}^K". They note that under a non-uniform distribution the same quantity "is referred to as the influence of variable x_j on the function f" — the Kahn–Kalai–Linial object. Mosaic needs the definition only to this depth, and the harmonic-analysis machinery behind it ("much of the discussion in this Letter can be formulated in terms of spectral methods or harmonic analysis on the n cube") is not load-bearing for anything below.

**Sensitivity.** The sensitivity of `f` at a point is the number of its Hamming neighbours that disagree with it:

```
s^f(x)  =  |{ i ∈ [1,…,K] : f(x ⊕ e_i) ≠ f(x) }|
```

and the **average sensitivity** `s^f` is the expectation of that over `x`. Under the uniform distribution the two definitions collapse into each other, which is the paper's key algebraic step, quoted verbatim: "the average sensitivity is equal to the sum of the activities: s^f = E[s^f(x)] = Σᵢ E[χ[f(x ⊕ eᵢ) ≠ f(x)]] = Σᵢ αᵢ^f". So `s^f` is a number in `[0, K]`.

**Nothing in either definition mentions a generator.** Activity is a count over the 2^K rows of a *particular* truth table. This is the whole of the repair [#100](https://github.com/NGL321/mosaic/issues/100) was looking for: `K` and `p` are parameters of the ensemble that drew a network and have nothing to consume when handed one network, whereas `α_j^f` and `s^f` are read directly off the network that was handed over. Two networks drawn from the same `(K, p)` have different average sensitivities, and that is the point — it is what a per-instance quantity is for.

Shmulevich & Kauffman say so themselves, in the last two sentences of the Letter: "we have an analytical method that allows us to determine whether a specific network is ordered or chaotic without having to run computer simulations that construct empirical Derrida curves. For example, given a concrete network, we can compute the average sensitivity of each function and average these to obtain a single number that reflects the regime in which the network operates." That is exactly the claim the ticket asks about. §3 is about what stands behind it, and the answer is less than the sentence implies.

## 2. The criterion is `s̄ = 1`, and for one step it is exact

**The criterion.** [Shmulevich & Kauffman](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) never write "s = 1" as a displayed condition, but they use it as one, unmistakably, in their second worked example. Take a network in which every node computes `f(x₁,…,x₁₈) = (x₁ ∧ x₂) ∨ (x₃ ∧ x₄) ∨ … ∨ (x₁₇ ∧ x₁₈)`. Verbatim: "each of the 18 activities is approximately equal to 0.0501 and the average sensitivity is approximately 0.0501 × 18 = 0.9010 (<1), implying the network is ordered." They then note that a random network with the same `K = 18` and the same normalised Hamming weight `p = 0.9249` gives `K·2p(1−p) = 2.5001 (>1)` and "the network is chaotic", concluding: "we can have two networks with identical connectivity and internal homogeneity that lie on opposite sides of the order-chaos boundary, with the average sensitivity reflecting this difference." The threshold is 1, the parenthesised inequalities are doing the work, and the boundary is named.

They also connect it to the exponent: "in the context of random Boolean networks with connectivity K, the expected average sensitivity determines the well-known critical transition curve with the Lyapunov exponent being the logarithm of the expected average sensitivity: λ = log E[s^f]". So `s̄ = 1` is `λ = 0` in the Boolean damage-spreading sense. That is a *different* λ from the one [#98](https://github.com/NGL321/mosaic/issues/98) refuted as a proxy for `h_μ`, and it does not restore the bridge that document broke — it is a perturbation-spreading rate, and [Tisseur's counterexample](https://arxiv.org/abs/math/0312136) is about exactly that class of quantity. §6 returns to this.

**Why 1, exactly, for one step.** The paper asserts the threshold and does not derive it for a realised network. The derivation is short enough to do here, and doing it is what shows precisely which part of the criterion is free and which part is borrowed.

Take a realised network on `N` nodes: node `i` computes `f_i` of the inputs in `In(i)`, `|In(i)| = k_i`. Draw a state `x` uniformly from `{0,1}^N` and flip one uniformly-chosen bit `j`. The expected Hamming distance between the two successor states is

```
E[d₁]  =  Σ_i  P( f_i(x) ≠ f_i(x ⊕ e_j) )
       =  Σ_i  (1/N) Σ_{j ∈ In(i)}  E_x[ ∂f_i/∂x_j ]        (only inputs of i can matter)
       =  (1/N) Σ_i Σ_{j ∈ In(i)}  α_j^{f_i}
       =  (1/N) Σ_i  s^{f_i}
       =  s̄
```

**The mean average sensitivity of a realised network is exactly the expected one-step damage amplification of that network.** No approximation, no limit, no ensemble: the identity holds at every finite `N` for the one specific network in hand. `s̄ < 1` means a one-bit perturbation is expected to shrink after one step; `s̄ > 1` means it is expected to grow. That is a branching-process threshold of exactly the shape [Beggs & Plenz's σ](https://web.archive.org/web/2020/https://www.jneurosci.org/content/jneuro/23/35/11167.full.pdf) has — `σ` "is the average number of descendants from one ancestor" — and it is worth noticing that Mosaic has now met the same first-moment criterion twice from two literatures. What [#98](https://github.com/NGL321/mosaic/issues/98) said about `σ` transfers verbatim: this is a statement about an *expected descendant count*, not about information production.

**One hypothesis is hiding in the first line and it is not small.** `x` was drawn uniformly. Activity is defined against the uniform measure on the hypercube, and [Shmulevich & Kauffman](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) flag the alternative themselves — under any other distribution the quantity is the *influence*, not the activity. A realised network sitting on an attractor is emphatically not uniformly distributed over its state space, so `s̄` is the amplification factor for a perturbation applied at a uniformly random state, which is not the experiment a system that has already relaxed is running.

## 3. What the criterion borrows: the expectation, the annealed step, and N → ∞

The identity in §2 covers one step. A criticality test is a claim about the *asymptotic* fate of a perturbation, and everything between the two is where the ticket's three suspects reappear.

**The extrapolation is the annealed assumption.** Iterating `d_{t+1} = s̄ · d_t` requires that the damage present at step `t` is distributed the way a fresh uniform perturbation is — uncorrelated with the wiring that produced it, spread over nodes independently. That is precisely what [Derrida & Pomeau (1986)](https://web.archive.org/web/20221221185507/http://www.lps.ens.fr/~derrida/PAPIERS/1986/pomeau-86.pdf) buy by re-randomising the functions and the wiring at each time step, and it is what their own equation (5) records as an inequality rather than an equality. And it requires `N → ∞`, without which the linearisation is invalid the moment damage becomes a non-vanishing fraction of the network — the saturation that produces the fixed point `y*` in their equation (11). Neither condition is weakened by the fact that `s̄` is computed on an instance. **The per-instance quantity is exact; the per-instance dynamical conclusion is not.**

**Shmulevich & Kauffman's own evidence is ensemble evidence.** Their validation method is the Derrida curve, which they define as plotting `ρ(t+1)` against `ρ(t)` "and averaging over many pairs of states and random networks" — an average over an ensemble of networks, in a paper whose headline is an instance-level quantity. Their `λ = log E[s^f]` carries an explicit `E` over the truth-table distribution. And the derivation they give of `E[α_j^f] = 2p(1−p)` runs through "the distribution of the truth table of the function f". The instance-level sentence in their conclusion is asserted, not proved, and it is asserted with no error bound and no statement of how large `N` must be.

**The rigorous version is squarely a theorem about ensembles.** [Schober & Bossert (2007)](https://ar5iv.labs.arxiv.org/html/0704.0197) extend Lynch's proof of Kauffman's freezing conjecture, and the parameter that carries it is

```
λ  =  Σ_i p_i Σ_{w ∈ F₂^{K_i}} γ(f_i, w) · a^{w_H(w)} (1 − a)^{K_i − w_H(w)}
```

where `p_i` weights functions by their probability under the *generator* and `a` is "the long-run probability a random gate outputs 1". Their central identification is `λ = E_F(s_f)` — Lynch's parameter is the **expectation** of average sensitivity over the ensemble of functions, not the average sensitivity of a network. Their Theorem 4 concludes "When λ ≤ 1, r = 1 and when λ > 1, r < 1", where `r` is a limiting probability that gates freeze or become ineffective within `α log N` steps **as N → ∞**. So the one place where `s = 1` is a proved criticality boundary rather than a heuristic is a statement about a random ensemble, in the large-`N` limit, with the conclusion holding in probability. All three of the ticket's suspects are present.

The honest summary is that the literature swapped which of the three it needs least. `K · 2p(1−p) = 1` needs the ensemble to even *state* the quantity. `s̄ = 1` states the quantity without an ensemble and then needs the ensemble and the limit to justify the comparison. That is progress — a computable number is strictly better than an uncomputable one — but it is not the disappearance of the problem.

## 4. The composed form: it exists in a primary source, and it is wrong as quoted

The ticket's second item asks whether anyone composes [Derrida & Pomeau's](https://web.archive.org/web/20221221185507/http://www.lps.ens.fr/~derrida/PAPIERS/1986/pomeau-86.pdf) equation (14) — the in-degree mixture — with their equation (15) — the bias — into `⟨K⟩ · 2p(1−p) = 1`. Two findings, and the second is more interesting than the first.

**Yes, primary sources compose it.** [Schober & Bossert](https://ar5iv.labs.arxiv.org/html/0704.0197) do it structurally: their λ sums over the connectivity distribution `p_i` *and* carries the bias, in one parameter, with `λ = 1` as the proved boundary; their Theorem 5 then evaluates it as `λ = 2Kp(1−p)` for the mean-bias model. Composing the two directions is then one line of linearity of expectation, done here: if a node of in-degree `k` and bias `p` has `E[s] = k·2p(1−p)`, then `λ = Σ_k ρ_k · k · 2p(1−p) = ⟨k⟩ · 2p(1−p)`. [Costa, Rozum, Marcus & Rocha (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955587/) state the composed form directly as the standing criterion, `2KP(1−P) = 1`, describing it as decomposing "the Derrida coefficient into average in-degree (K) and bias-variance P(1−P)". [Manicka, Marques-Pita & Rocha (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8767216/) state it more carefully, and their care is the tell: "if a BN has homogeneous in-degree, k, and fixed bias, p, then the critical boundary between ordered and chaotic network dynamics is given by, 2kp(1−p) = 1" — homogeneous, fixed — and then apply it to heterogeneous empirical networks with `k` read as a mean. Row 12 is **Supported**: the composition is not a secondary-literature invention, it is in the primary literature with a theorem behind it, twenty-one years after Derrida & Pomeau.

**But the form as quoted is the product of means where the true quantity is the mean of a product.** Because average sensitivity is an expectation and expectation is linear, the exact per-network condition is

```
⟨ k · 2p(1−p) ⟩  =  1
```

with the average running over nodes. Collapsing that to `⟨k⟩ · 2p̄(1−p̄)` requires two things nobody states. First, in-degree and bias must be uncorrelated across nodes. Second — and this one bites even when they are — `p ↦ 2p(1−p)` is **strictly concave**, so Jensen's inequality separates the two. Writing `p̄ = ⟨p⟩` and expanding:

```
⟨ 2p(1−p) ⟩  =  2⟨p⟩ − 2⟨p²⟩  =  2p̄ − 2( p̄² + Var(p) )  =  2p̄(1−p̄) − 2·Var(p)
```

so, under independence of `k` and `p`,

```
⟨k⟩ · [ 2p̄(1−p̄) − 2·Var(p) ]  =  1
```

The standard composed form drops the `Var(p)` term and is therefore an **upper bound** on the true one-step amplification: it over-predicts chaos, by `2⟨k⟩·Var(p)`. Heterogeneity in node output bias is stabilising, and the effect is first-order in the variance rather than a correction of a correction. Empirical networks have strongly heterogeneous biases, which makes this a candidate partial explanation for the numbers in §5 — and it is exactly the ground [Costa et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955587/) reoccupy from the other side when they add "bias entropy", a measure of bias heterogeneity, to the criterion and improve prediction. Row 13 is **Refuted**, and this correction is derived here rather than retrieved; the one paper that appears to establish it independently was not reached, which is [#128](https://github.com/NGL321/mosaic/issues/128).

## 5. On realised networks the test scores 0.54, and the repair is calibrated

The question the ticket actually asks — does `s̄ = 1` decide criticality for a given network — has been answered empirically, against ground truth, on real systems, and the answer is bad.

[Manicka, Marques-Pita & Rocha (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8767216/) take 63 experimentally validated systems-biology Boolean models from the Cell Collective repository and, for each, measure the **Derrida coefficient** `ζ` directly: generate 250 random initial configurations, make perturbed copies differing in `m ∈ [1, N/10]` flipped states, advance both one step, average the resulting Hamming distances against `m`, and read `ζ` as "the slope of the Derrida plot at the origin", with `ζ > 1` chaotic and `ζ ≤ 1` ordered or critical. That measured `ζ` is the ground truth. They then ask how well the structural theory predicts it — and they record, verbatim, that "the average *network* sensitivity is equivalent to the ST defined in Eq. 1 for predicting criticality", so the numbers are the numbers for the average-sensitivity criterion.

**The structural theory scores MCC 0.44 and AUC 0.54**, which the paper describes as "only marginally better than a random toss". Row 8 is **Refuted** on that.

**The diagnosis is specific and it is about the definition, not the asymptotics.** Verbatim: "sensitivity independently aggregates the influence (activity) of each individual input to an automaton", and so "does not quantify the nonlinear or collective effects in the canalizing logic of automata". Their sharpest illustration: "even for automata of k = 2, sensitivity does not discriminate between such common Boolean functions as conjunction/disjunction and proposition/negation." Average sensitivity is a *sum of independent per-input activities* — a linear measure — and real regulatory logic is dominated by **collective canalization**, "a very common non-linear phenomenon in automata whereby a subset of inputs jointly determine the state of an automaton, while rendering redundant the complement subset of inputs". A first-moment quantity that treats each input separately cannot see that.

**The repair works and is not closed-form.** Replace in-degree with **effective connectivity** `k_e`, "the expected number of inputs of an automaton that are minimally sufficient to determine its state transitions", and the criterion becomes

```
c₁ · ⟨k_e⟩ · p(1−p)  =  1        with  c₁ = 3.94
```

reported at MCC 0.96 and R² 0.94 against the measured `ζ`, versus 0.44 and 0.54 for the structural form. That is a decisive improvement and it comes with a **fitted constant**. [Costa et al. (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955587/) then need a *further* ingredient — bias entropy alongside `k_e` — to reach 89% accuracy and MCC 0.77 on the same empirical models, against 69% and MCC 0.32 for in-degree-based prediction, and between 93.8% and 97.5% on heterogeneous random Boolean networks, with the fits described as power laws. A criterion with a calibrated constant and a power-law fit is a regression with an excellent score, not a closed form; whether `c₁` has a derivation is [#129](https://github.com/NGL321/mosaic/issues/129). Row 9 is **Supported** for the existence of a working per-instance test and says nothing about its being closed-form.

## 6. The other axis, and the cost

**Informational Capacity is untouched, and it is worth being blunt about how untouched.** Across the [Shmulevich & Kauffman](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) Letter there is no entropy rate, no mutual information, no channel capacity and no excess entropy; the quantities are activities, sensitivities, biases and Hamming distances throughout. [Schober & Bossert](https://ar5iv.labs.arxiv.org/html/0704.0197) count frozen and ineffective gates. [Manicka et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC8767216/) measure a Derrida slope. The one thing in this literature that carries the word *entropy* is [Costa et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955587/)'s **bias entropy**, and it is a Shannon entropy of the *static* distribution of node output biases across a network — a combinatorial property of the truth tables, computed without running the system — not a dynamical entropy rate of a trajectory. It is a better description of the *ensemble of rules*, not a measurement of information production. Row 10 is **Refuted**, on the same footing as [#100](https://github.com/NGL321/mosaic/issues/100) row 9: this whole line of work speaks to Order and is silent on the Bound's second axis.

**The cost is the good news and is why this is worth having at all.** Computing `s^{f_i}` exactly requires evaluating `f_i` on all `2^{k_i}` rows of its truth table, once per input, so the whole network costs `Σᵢ kᵢ · 2^{kᵢ}` function evaluations — and for a Boolean network the truth table is usually the *given*, so the "evaluation" is a table lookup. Against the alternative that [#98](https://github.com/NGL321/mosaic/issues/98) left Mosaic with, this is a different kind of object entirely: no trajectory has to be simulated, no invariant measure sampled, no block-entropy sequence extrapolated, and no limit estimated from finite data. It is a finite exact computation on the specification of the system. Both [Manicka et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC8767216/) and [Costa et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955587/) do flag that the exact computation "becomes computationally challenging at higher in-degrees", which is what `2^k` says; sampling gives an unbiased estimate at the cost of turning an exact quantity into an estimated one, which is the thing this route exists to avoid.

## 7. What this licenses for Mosaic

The ticket set up a clean disjunction: if average sensitivity works, a cheap computable test on discrete-state systems is recoverable and the pressure on [#99](https://github.com/NGL321/mosaic/issues/99) eases; if it does not, `h_μ` estimation is the only route. The evidence does not land on either horn, and the shape of the middle is the finding.

**What is recovered.** A quantity that is genuinely per-instance, genuinely cheap, genuinely exact, and genuinely about the Order axis. `s̄` can be handed a specific wiring diagram and a specific set of truth tables and return a number, which `K · 2p(1−p)` cannot ([#100](https://github.com/NGL321/mosaic/issues/100) §4). That number is exactly the system's one-step damage amplification (§2). For a *specified* discrete-state system — a cellular automaton rule, a Boolean model of a pathway — Mosaic can compute it today with no data collection.

**What is not recovered.** The comparison `s̄ ⋛ 1` is a criticality verdict only under the annealed extrapolation and the large-`N` limit (§3), and on realised networks that verdict is barely better than chance (§5). So the *closed form* did not become per-instance; a *computable proxy* became per-instance, and the proxy is weak exactly where Mosaic would want to use it — on real, structured, canalizing systems rather than on random ones.

**The recommendation.** Use `s̄` as a **screen and a one-way falsifier**, not as a placement. It is cheap enough to compute on every discrete-state candidate, and a value far from 1 in either direction is informative about damage propagation in a way that no estimate of `h_μ` currently exists to contradict. It is not a reading of Order, and it must not be substituted for `h_μ`, for the reason [#98](https://github.com/NGL321/mosaic/issues/98) gives in general and which applies here specifically: `s̄` is a perturbation-spreading rate, [Shmulevich & Kauffman](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) identify `log E[s^f]` as a Lyapunov exponent, and [Tisseur (2000)](https://arxiv.org/abs/math/0312136) exhibits a cellular automaton with a strictly positive exponent and `h_μ = 0`. Substituting `s̄` for `h_μ` would reintroduce, in a new notation, the exact bridge [#98](https://github.com/NGL321/mosaic/issues/98) broke.

**So [#99](https://github.com/NGL321/mosaic/issues/99) is not relieved.** Order is still `h_μ` and only `h_μ`, and nobody has estimated it on any system Mosaic intends to search. What this document adds is a cheap discrete-state diagnostic that sits beside it and a warning label about what it is not.

## What this does not establish

### Sources not reached

**The APS typesetting of Shmulevich & Kauffman** — [link.aps.org/doi/10.1103/PhysRevLett.93.048701](https://link.aps.org/doi/10.1103/PhysRevLett.93.048701) — returned **HTTP 403** on 2026-08-02, so the Letter was read from the [PubMed Central deposit](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) instead. PMC's rendering mangles some sub- and superscripts (the paper's `α_j^f` appears as `αjf`, and `s^f(x)` appears once as `Sf(x)` and once as `sf`), so every symbol quoted in §1 was reconstructed from context rather than read off cleanly; where the reconstruction could be wrong it is flagged under *Load-bearing ifs*. **Lynch (1995)**, *A criterion for stability in random Boolean cellular automata* — the theorem all of §3's rigour rests on — was **not reached** and is known here only through [Schober & Bossert's](https://ar5iv.labs.arxiv.org/html/0704.0197) restatement and extension of it; its exact hypotheses in the original are unverified. **Schober & Bossert itself was not read cover to cover**: the arXiv PDF is password-protected against text extraction (`arxiv.org/pdf/0704.0197` downloads but will not open for reading), so the paper was read through the ar5iv HTML rendering, targeted at the definitions, Theorem 4 and Theorem 5; the intervening proofs were not read, and no verdict here rests on a proof step. **The MDPI live page** for Costa et al. returned **HTTP 403**; the article was read from the [PubMed Central deposit](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955587/). **The Physica A (2026) paper** *Mean-preserving spreads of node output biases suppress damage spreading in random Boolean networks*, [S0378437126003420](https://www.sciencedirect.com/science/article/abs/pii/S0378437126003420), which appears to establish §4's correction independently, returned **HTTP 403** on ScienceDirect and has no locatable preprint; **only its title was seen**, and nothing here rests on it — it is [#128](https://github.com/NGL321/mosaic/issues/128). **Derrida & Pomeau (1986) was not re-opened in this session**; §4 uses equations (14) and (15) as transcribed by [`2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md`](2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md) §3. **Kahn–Kalai–Linial (1988) and Friedgut (1998)** were deliberately not sought: §1 needs the activity/influence definition only, which Shmulevich & Kauffman state in full, and opening the Fourier-analytic originals would have bought nothing the verdicts use.

### Open gaps

**Whether `c₁ = 3.94` has a derivation is unknown**, and it decides whether Mosaic has a closed-form per-instance criterion or a calibrated one; it is [#129](https://github.com/NGL321/mosaic/issues/129), and it is the most valuable single thing anyone could pick up from this document. **The uniform-measure hypothesis is unexamined.** §2's identity holds for a perturbation applied at a uniformly random state, and a realised system on an attractor is not there; what `s̄` becomes when activity is replaced by influence under the invariant measure is not established, and it may be that the attractor-restricted influence is the quantity that actually predicts, which would also explain §5's numbers without appealing to canalization. **Nobody has computed `s̄` for a cellular automaton in this document.** The identity in §2 is stated for a Boolean network with node-local truth tables; a CA is that, with a shared rule and a lattice, so `s̄` should reduce to `k · (fraction of rule-table neighbours that disagree)` — but that reduction was not checked against the CA literature, and a Mosaic that wants to place ECA rules needs it checked. **Whether the `Var(p)` correction of §4 changes the empirical picture** was not tested; it is a testable prediction — the structural theory's AUC should improve on the Cell Collective models when the variance term is included — and testing it is cheap and was not done. **The relation between `s̄` and Beggs & Plenz's `σ`** is noticed in §2 and not pursued; if they are the same first-moment criterion in two literatures, [#123](https://github.com/NGL321/mosaic/issues/123)'s untraced `σ ↔ λ` provenance may have an answer here rather than in the recurrent-network literature.

### Load-bearing ifs

**If §2's three-line identity is wrong, rows 4, 14 and most of §7 fall.** It is the one original derivation carrying the document's positive half. Its weakest step is the interchange in the second line — that only inputs of `i` contribute, which is true because `∂f_i/∂x_j ≡ 0` for `j ∉ In(i)`, and that the uniform draw of `x` makes `E_x[∂f_i/∂x_j]` equal `α_j^{f_i}` by definition. The check that it is not wrong is that it reproduces `E[s̄] = ⟨k⟩·2p(1−p)` on the random ensemble, which is [Shmulevich & Kauffman's](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) own stated result and an independent constraint. **If §4's Jensen expansion is wrong, row 13 flips and [#128](https://github.com/NGL321/mosaic/issues/128) is spurious.** It is three lines of algebra on the definition of variance; the sanity check is that `Var(p) = 0` recovers the quoted form exactly. **If the PMC rendering differs materially from the published Letter**, §1's definitions are definitions of a transcription and not of the paper — the specific risk is the subscript/superscript mangling described above, and the mitigation is that the two independent statements `s^f = Σᵢ αᵢ^f` and `E[s^f] = K·2p(1−p)` are mutually consistent only under the reading given. **If Manicka et al.'s claim that "the average network sensitivity is equivalent to the ST" is false**, then §5's AUC of 0.54 is a number about `⟨k⟩·2p̄(1−p̄)` and not about measured average sensitivity, and row 8 falls back to **Unresolved** — this is the single most attackable link in the document's negative half, because §4 shows the two are *not* algebraically identical under heterogeneous bias, and their equivalence claim may hold only in the homogeneous case they state the ST for. **If Lynch's theorem, as restated by Schober & Bossert, has hypotheses they did not carry over**, §3's account of what is proved is an account of the extension and not of the original.

## Verification Debt

Two items, both filed, both open.

- **[#128](https://github.com/NGL321/mosaic/issues/128)** — the **composed form is wrong under heterogeneous
  bias**. §4 establishes that a primary source does compose `⟨K⟩ · 2p(1−p) = 1` — which was the ticket's
  second item, and it is **Supported** — but composing it correctly gives the mean of a product, and
  collapsing to the product of means drops `2⟨K⟩·Var(p)` by Jensen, so the standard form over-predicts
  chaos. The correction was **derived here, not retrieved**; the Physica A (2026) paper that appears to
  establish it independently returned HTTP 403 and only its title was seen.
- **[#129](https://github.com/NGL321/mosaic/issues/129)** — the **working per-instance test has a fitted
  constant**. §5 records that average sensitivity scores MCC 0.44 / AUC 0.54 against measured Derrida
  coefficients on 63 empirical models, and that effective connectivity recovers MCC 0.96 — via
  `c₁·⟨k_e⟩·p(1−p) = 1` with `c₁ = 3.94` calibrated rather than derived, and with a further bias-entropy
  correction needed on top. Whether `c₁` has a derivation decides whether Mosaic has a closed-form
  per-instance criterion or a regression.

**This does not ease [#99](https://github.com/NGL321/mosaic/issues/99).** §7 is explicit: Order remains `h_μ`
and only `h_μ`, `s̄` is a perturbation-spreading rate that [#98](https://github.com/NGL321/mosaic/issues/98)
already refuted as a substitute for `h_μ`, and nothing here removes the need to estimate `h_μ` on a real system.

## Proposals

**1. Record average sensitivity as a discrete-state screen, not as a reading of Order.** If any note, badge or `CONTEXT.md` line records what [#122](https://github.com/NGL321/mosaic/issues/122) settled, the exact text proposed is:

```
For a discrete-state system given by node-local truth tables, the mean average sensitivity
s̄ — the mean, over nodes, of the sum of that node's per-input activities — is computable
exactly from the specification, with no trajectory and no estimated limit, and is exactly
the expected one-step damage amplification. It is a cheap screen and a one-way falsifier;
it is **not** a reading of Order. Comparing s̄ to 1 is a criticality verdict only under the
annealed extrapolation in the N → ∞ limit, and against measured Derrida coefficients on 63
empirical biological models the criterion scores AUC 0.54 (Manicka, Marques-Pita & Rocha
2022). Order is h_μ and only h_μ (#98); s̄ is a perturbation-spreading rate, and Tisseur
(2000) exhibits a system with a positive spreading rate and h_μ = 0.
```

**2. Where `⟨K⟩ · 2p(1−p) = 1` is used, carry the homogeneity hypothesis.** The composed form is licensed by a primary source (§4) and is an *upper bound* on the true amplification whenever node biases vary. The short form: *`⟨K⟩ · 2p(1−p) = 1` assumes homogeneous bias; with heterogeneous bias the condition is `⟨K · 2p(1−p)⟩ = 1`, which is smaller by `2⟨K⟩·Var(p)`.*

**3. Amend [#100](https://github.com/NGL321/mosaic/issues/100)'s open gap, which this closes and re-opens narrower.** That document's first open gap reads that average sensitivity "is a real object in the later literature … that this document did not read and therefore cannot assert. If it works, Mosaic gets what #100 hoped for; if it does not, the closed form stays confined to ensembles." The resolution is neither: the object exists and is per-instance, the criterion is not. No edit to that document is proposed — it is a record of what was true when written — but any summary that carries its disjunction forward should carry this resolution instead.

**4. Badge text, for Noah to apply if and where any of the above lands:** `⟦T3 · #122⟧`.

## Appendix: primary sources, all retrieved 2026-08-02

1. Ilya Shmulevich & Stuart A. Kauffman (2004), *Activities and Sensitivities in Boolean Network Models*, **Phys. Rev. Lett. 93**(4):048701. Read in full from the PubMed Central deposit, the APS typesetting being unreachable: [pmc.ncbi.nlm.nih.gov/articles/PMC1490311](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/). Publisher record: [doi.org/10.1103/PhysRevLett.93.048701](https://doi.org/10.1103/PhysRevLett.93.048701). *Activities and sensitivities* for the partial derivative, `α_j^f`, `s^f(x)` and `s^f = Σᵢ αᵢ^f`; the same section for `E[α_j^f] = 2p(1−p)`, `E[s^f] = K·2p(1−p)` and `λ = log E[s^f]`; *Dynamics of Boolean networks* for the Derrida-curve method and the `B₁`/`B₂` experiment; the `K = 18` example with `s = 0.9010 (<1)`; *Concluding remarks* for the per-instance claim.
2. Steffen Schober & Martin Bossert (2007), *Analysis of random Boolean networks using the average sensitivity*, arXiv:0704.0197 [nlin.CG]. Read through the ar5iv HTML rendering, targeted at definitions and theorem statements rather than cover to cover, the arXiv PDF being unopenable: [ar5iv.labs.arxiv.org/html/0704.0197](https://ar5iv.labs.arxiv.org/html/0704.0197); deposit record at [arxiv.org/abs/0704.0197](https://arxiv.org/abs/0704.0197). The definition of Lynch's λ over the connectivity distribution; `λ = E_F(s_f)`; Theorem 4 for the `λ ≤ 1` / `λ > 1` dichotomy as `N → ∞`; Theorem 5 for `λ = 2Kp(1−p)` in the mean-bias model and `λ = 2^{K+1}Kp(1−p)/(2^K−1)` in the fixed-bias model.
3. Santosh Manicka, Manuel Marques-Pita & Luis M. Rocha (2022), *Effective connectivity determines the critical dynamics of biochemical networks*, **J. R. Soc. Interface 19**(186):20210659. Read from the PubMed Central deposit together with the ar5iv rendering of the preprint: [pmc.ncbi.nlm.nih.gov/articles/PMC8767216](https://pmc.ncbi.nlm.nih.gov/articles/PMC8767216/) and [ar5iv.labs.arxiv.org/html/2101.08111](https://ar5iv.labs.arxiv.org/html/2101.08111). Publisher record: [doi.org/10.1098/rsif.2021.0659](https://doi.org/10.1098/rsif.2021.0659). The structural theory `2kp(1−p) = 1` stated for homogeneous in-degree and fixed bias and attributed to Derrida & Pomeau; the equivalence of average network sensitivity to it; the Derrida-coefficient measurement protocol; MCC 0.44 and AUC 0.54 for the structural theory on 63 Cell Collective models against MCC 0.96 / R² 0.94 for `c₁·⟨k_e⟩·p(1−p) = 1` with `c₁ = 3.94`; the `k = 2` conjunction/negation non-discrimination example.
4. Felipe Xavier Costa, Jordan C. Rozum, Austin M. Marcus & Luis M. Rocha (2023), *Effective Connectivity and Bias Entropy Improve Prediction of Dynamical Regime in Automata Networks*, **Entropy 25**(2):374. Read from the PubMed Central deposit, the MDPI live page returning 403: [pmc.ncbi.nlm.nih.gov/articles/PMC9955587](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955587/). Publisher record: [doi.org/10.3390/e25020374](https://doi.org/10.3390/e25020374). `2KP(1−P) = 1` stated with `K` as average in-degree and described as decomposing the Derrida coefficient; 89% accuracy and MCC 0.77 for effective connectivity with bias entropy on the Cell Collective models against 69% and MCC 0.32 for in-degree; 93.8–97.5% on heterogeneous random Boolean networks; the acknowledgement that the method is computationally challenging at higher in-degrees.
5. Bernard Derrida & Yves Pomeau (1986), *Random Networks of Automata: A Simple Annealed Approximation*, **Europhys. Lett. 1**(2):45–49. **Not re-opened in this session.** Equations (14) and (15) are used in §4 exactly as transcribed from the page scan by [`2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md`](2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md) §3, whose capture is [web.archive.org/…/pomeau-86.pdf](https://web.archive.org/web/20221221185507/http://www.lps.ens.fr/~derrida/PAPIERS/1986/pomeau-86.pdf); publisher record [doi.org/10.1209/0295-5075/1/2/001](https://doi.org/10.1209/0295-5075/1/2/001). Cited for the in-degree mixture (14), the biased map (15), and the annealed inequality (5) that §3 identifies as the extrapolation's cost.
