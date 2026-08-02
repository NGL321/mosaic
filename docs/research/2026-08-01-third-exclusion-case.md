---
ticket: 103
map: 1
date: 2026-08-01
kind: question
tier: T3
session: unrecorded
sources: 6
debt: [105, 106, 107]
supersedes: null
---

# The third exclusion case is the memoryless system — a biased coin, a (p, 1−p) Bernoulli map, an untrained feed-forward network on noise — and it is the case that makes the second axis load-bearing

**Provenance.** Machine-produced, unverified. Four sources were read in full from a primary document, all of them this session and all by converting the publisher's or the author's own PDF to text rather than by reading a landing page: Crutchfield & Feldman (2001), from the arXiv PDF; Feldman, McTague & Crutchfield (2008), from the authors' UC Davis copy; Li (1991), from the *Complex Systems* page scan, which carries an OCR layer; and Mitchell, Crutchfield & Hraber (1993), §2 only, from the arXiv PDF, to re-verify the one quotation this document leans on. Two are carried from [#87](https://github.com/NGL321/mosaic/issues/87) and were **not** re-opened here — Crutchfield & Young (1989) and Schoenholz et al. (2017) — and are marked as such at every claim that rests on them.

Three things in this document were **derived, not retrieved**, and each is filed as debt rather than asserted: that exact `E = 0` forces an i.i.d. process ([#105](https://github.com/NGL321/mosaic/issues/105)); that the (p, 1−p) Bernoulli map's natural partition is generating, so that its coordinates are the map's and not the partition's ([#106](https://github.com/NGL321/mosaic/issues/106)); and the placement of a paramagnet on the `E = 0` axis, which is worked from Feldman/McTague/Crutchfield's own Hamiltonian rather than read off their figure.

Four `(h_μ, E)` pairs in §3 were **computed here, on running systems** — a simulated interval map and three randomly-initialised neural networks. So far as the record shows this is the first time Mosaic has measured either axis on anything. The estimator is a naive plug-in with no bias correction and no confidence interval, it returns positive excess entropy for processes whose true excess entropy is exactly zero, and that is [#107](https://github.com/NGL321/mosaic/issues/107). None of these readings has been checked by Noah unaided.

---

## 0. Verdict

> **Yes — and it is not one system but a line: the memoryless processes, which occupy the entire lower boundary `E = 0` of the accessible region at every intermediate Order, and which a one-dimensional Order axis would admit. The Bound's second axis is now load-bearing in evidence. It takes one further case to make it load-bearing in both directions.**

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | A system intermediate on Order and excluded on Capacity exists mathematically | **Established** — the lower boundary is `E = 0` across the whole range `0 < h_μ < log₂|A|`, attained by biased i.i.d. sources | §1 |
| 2 | Exact `E = 0` forces an i.i.d. process, so the honest criterion is *small* E and not *zero* E | **Supported** — derived here from monotonicity of past–future mutual information; corroborated but not stated by Feldman/McTague/Crutchfield | §1 |
| 3 | A case characterised by its **dynamics** rather than by a rule table | **Supported** — memorylessness is a dynamical property; the (p, 1−p) Bernoulli map is a deterministic realisation with no rule table | §2 |
| 4 | A case drawn from something Mosaic might **actually search** | **Supported** — an untrained feed-forward network on i.i.d. input, measured at (Order 0.500, Ê ≈ 0.001 bits) | §3 |
| 5 | The falsifier branch: does intermediate Order entail non-negligible Capacity, arguing for collapsing the Bound to one dimension? | **Refuted** — it does not; the axes are independent by construction and by two primary sources that say so in as many words | §1, §6 |
| 6 | The case discriminates [#87](https://github.com/NGL321/mosaic/issues/87)'s pair from an **Order-only** operationalisation | **Supported** — Order alone admits it; the pair excludes it | §4 |
| 7 | The case *alone* discriminates the pair from **every** one-dimensional operationalisation | **Refuted** — a Capacity-only or `C_μ`-only rule still passes all three cases; a **fourth** datum is needed, and §4 supplies it | §4 |
| 8 | The case fares the same under both readings of [#102](https://github.com/NGL321/mosaic/issues/102) | **Refuted** — an exclusion under the system-dynamics reading, fragile under the observed-process reading; which is itself an argument for the former | §5 |
| 9 | "Excluded on Capacity" is decidable on measured data today | **Open** — the plug-in estimator's noise floor is the same order as the excess entropy of processes that genuinely have some | §3 |

---

## 1. The accessible region, and why its floor is exactly the memoryless line

The question the ticket asks first is whether the wanted case is possible at all: is the lower boundary of the `(h_μ, E)` plane at `E = 0` across the whole intermediate range of entropy rate, or does an intermediate entropy rate force positive excess entropy?

**It is `E = 0`, across the whole range, and the sources say so before any construction is needed.** [Feldman, McTague & Crutchfield](https://csc.ucdavis.edu/~cmg/papers/oic.pdf) put the geometry plainly in their §II D, verbatim:

> "The excess entropy E and the entropy rate hμ are exactly the two quantities that specify the large-L asymptotic form for the block entropy Eq. (13). The set of all (hμ, E) pairs is thus geometrically equivalent to the set of all straight lines with non-negative slope and intercept. Clearly, a line's slope and intercept are independent quantities. Thus, there is no a priori reason to anticipate any relationship between hμ and E, a point emphasized early on by Li."

That is the entire falsifier branch settled in one paragraph, and by the same authors whose plane [#87](https://github.com/NGL321/mosaic/issues/87) adopted. `h_μ` is the slope of the asymptote of `H(L)`; `E` is its intercept; slope and intercept of a line are free of each other. The reference is to [Li (1991)](https://content.wolfram.com/sites/13/2018/02/05-4-3.pdf), whose abstract states the point as his own headline, verbatim:

> "It is emphasized that, given an entropy value, there are many possible complexity values, and vice versa; that is, the relationship between complexity and entropy is not one-to-one, but rather many-to-one or one-to-many."

and whose §1 closes:

> "The conclusion from this study seems to be that there is no universal relationship between complexity and entropy independent of the underlying sequences."

Li's "complexity" is the excess entropy under another name — his Eq. (2) defines it as the past–future mutual information and his Eq. (6) as `C = lim_N [H(S_N) − hN]`, which is Crutchfield & Feldman's Prop. 7 verbatim.

**The upper boundary is a real constraint; the lower boundary is not.** Feldman/McTague/Crutchfield give one bound in closed form, their Eq. (15): for a binary order-R Markov process, `E ≤ R(1 − h_μ)`. Their derivation is worth quoting because it is the reason the *lower* boundary is free, verbatim:

> "The second term on the right hand side is minimized by assuming that the conditional entropy of the two blocks is given simply by Rhμ--i.e., R times the per-symbol entropy rate hμ. In other words, we obtain a lower bound by assuming that the process is independent, identically distributed over R-blocks."

Independence is what *saturates* the bound in the direction that makes `E` small. There is no matching lower envelope, and the reason is trivially constructive.

**The construction.** A biased binary i.i.d. source has `h_μ = H(p)` and `E = 0` exactly. [Crutchfield & Feldman](https://arxiv.org/abs/cond-mat/0102181) work exactly this case in their §VI A, verbatim:

> "The fair coin has an hμ of 1 bit per symbol, while the biased coin, being less unpredictable, has hμ ≈ .8813."

and

> "Each coin flip does not depend on past flips, and so there is no mutual information between the past and the future. Thus, E = 0. Similarly, no information is needed to synchronize to the source -- H(L) assumes its asymptotic form at L = 1 -- and so T = 0. That is, the statistics of isolated flips are all that is required to optimally predict both processes. Historical information does not improve predictability."

The last sentence is the Bound's exclusion criterion stated by the source. `H(p)` sweeps `(0, 1)` as `p` sweeps `(0, ½)`, so the entire segment `{(h_μ, 0) : 0 < h_μ < 1}` is occupied. Their own Table III lists the biased coin at `p = 0.7` as `h_μ = 0.881`, `G = 0.119`, `E = 0`, `T = 0` — Order 0.119, Capacity zero. Tune `p` to 0.110028 and Order is exactly 0.500.

**And this is the sharpest thing in the document: `E = 0` exactly is *only* the memoryless line.** Derived here, and filed as [#105](https://github.com/NGL321/mosaic/issues/105) because no source was found that states it. Take `E = lim_L I[X_{−L..−1} ; X_{0..L−1}]`, Crutchfield & Feldman's Prop. 8. The finite-L mutual informations are non-negative and non-decreasing in `L`, so `E = 0` forces every one of them to vanish. Fix `k` and take `L = k`: `(X_{−k},…,X_{−1})` is independent of `X_0`; by stationarity that is `X_k ⊥ (X_0,…,X_{k−1})` for every `k`, which is precisely the statement that the process is i.i.d. The corroborating remark from Feldman/McTague/Crutchfield's ε-machine enumeration is verbatim:

> "The minimum complexity, E = 0, corresponds to machines with only a single state."

— true of *topological* ε-machines under a uniform measure, so it points the same way without closing the general case.

Three consequences, all load-bearing.

- **The third exclusion case is not a system; it is a one-parameter family.** Any process at exactly zero Capacity and non-zero Order is a biased i.i.d. source. There is no other candidate to look for.
- **"Excluded on Capacity" cannot mean `E = 0`.** No physical system will measure exactly zero, and the exact-zero locus is a measure-zero set. The criterion has to be a **threshold** — `E` below some `ε` — which turns the third case from a point into a neighbourhood of the memoryless line. By Pinsker's inequality small past–future mutual information means the past–future joint is close to the product of its marginals, so the neighbourhood is exactly "approximately memoryless", which is the right shape for a Bound. Where `ε` sits is [#107](https://github.com/NGL321/mosaic/issues/107) and is not settled here.
- **Small `E` does not mean "no structure".** Crutchfield & Feldman's simple nondeterministic source sits at `h_μ ≈ 0.6778` (Order 0.3222) with `E ≈ 0.147` bits — verbatim, "there is not much mutual information between the past and future" — and yet, verbatim, "the number of effective states seen by an observer that attempts to reconstruct the hidden process is infinite, even though the internal process is a simple, three-state Markov chain." A system can have unbounded statistical complexity and near-zero Informational Capacity. The Bound excludes it anyway, and should: whatever structure it has, its past tells you almost nothing about its future, so there is nothing for an `Extraction` measurement to be a fraction of.

**The vertical spread at fixed Order is what the ticket wanted to see, and it is in the source's own table.** Crutchfield & Feldman's Table III lists the golden mean process, the even process and the random-random-XOR process at *identical* `h_μ = 2/3` — Order = 1/3 in every case — with `E = 0.252`, `E ≈ 0.902` and `E = 2` bits respectively. Add the biased coin at `p = 0.173952`, for which `H(p) = 2/3` to six places, and there is a fourth process at the same Order with `E = 0`. Four systems, one Order coordinate, Capacity ranging over `[0, 2]` bits. Crutchfield & Feldman draw the moral themselves, twice, verbatim: "the entropy rate is not sufficient to distinguish the structural properties of a source", and "again emphasizing the poverty of hμ as a structural measure."

## 2. Characterised by its dynamics, not by a rule table

[#87](https://github.com/NGL321/mosaic/issues/87) §1 killed Langton's λ on a structural objection, re-verified from [Mitchell, Crutchfield & Hraber](https://arxiv.org/pdf/adap-org/9306003) §2 this session, verbatim:

> "in the global view of CA space, CA rule tables themselves are the appropriate loci of dynamical behavior. This is in stark contrast with the state space and the attractor-basin portrait approach of dynamical systems theory. The latter approach acknowledges the fact that behaviors in state space cannot be adequately parameterized by any function of the equations of motion, such as λ."

The ticket rightly binds the third case by the same rule, and warns that a biased coin might satisfy the mathematics and fail the test. It does not fail it — but the reason is worth stating precisely, because the naive reading ("a coin is a toy, therefore it is a rule table") gets it backwards.

**Memorylessness is a property of the dynamics, and of nothing else.** The exclusion criterion here is not "the system's specification is short" and not "the system has few states". It is: *the conditional distribution of the next observation given the entire history equals its distribution given nothing.* That is a statement in state space, about the process's own trajectory statistics, and it is exactly the kind of statement Mitchell/Crutchfield/Hraber were asking for in place of λ. It is total over every system that emits a symbolisable time series — including a diamond, a thunderstorm, a cortex and a transformer — which is the property λ lacked. It never touches an equation of motion.

**And it has a deterministic realisation with no rule table at all: the (p, 1−p) Bernoulli map.** Take the two-branch piecewise-linear map of the unit interval

    T(x) = x / p            for x ∈ [0, p)
    T(x) = (x − p) / (1 − p) for x ∈ [p, 1]

with the partition at the kink, `s = 0` iff `x < p`. Each branch maps its interval *onto* the whole unit interval with constant slope, so Lebesgue measure is invariant and the state after any observed symbol is uniform on `[0,1]` again. The symbol sequence is therefore i.i.d. Bernoulli(p): `h_μ = H(p)` and `E = 0`, exactly, at any Order in `(0,1)`. This is a **deterministic chaotic dynamical system** — positive Lyapunov exponent, sensitive dependence, an attractor filling the interval — squarely inside the apparatus Mosaic's *dynamical-systems modelability* Bound has already bought. It has a state space, an equation of motion, and no transition table. Whether the partition is *generating*, and so whether `h_μ` here is the map's Kolmogorov–Sinai entropy rather than an artefact of the coarse-graining, is asserted and not read: [#106](https://github.com/NGL321/mosaic/issues/106).

**The near-miss that shows this is not free.** Feldman/McTague/Crutchfield's own one-parameter *symmetric* tent family does **not** contain the case. They report, verbatim, that "in sharp contrast to the logistic map, for the tent map it does appear as if the excess entropy takes on only a single value for each value of the entropy rate hμ", and give the relation at band-mergings as their Eq. (21), `E = −log₂ h_μ`. On that family, `E = 0` only at `h_μ = 1` — the thunderstorm corner — and an intermediate entropy rate *does* force positive excess entropy: at `h_μ = ½` the family sits at `E = 1` bit. Had one asked the question inside that family alone, the falsifier branch would have fired and the honest report would have been "collapse the Bound to one dimension." It is the asymmetry of the branches, not the chaos, that empties the memory; the symmetric family cannot express it. That is the strongest reason in this document to distrust family-level surveys of the plane, and it is why §1's argument is made from the geometry rather than from a scatter plot.

## 3. Measured, on systems, including one Mosaic might actually search

Everything above is analytic. This section reports numbers computed here, on running systems, with a naive plug-in block-entropy estimator (`Ĥ(L)` from empirical L-block frequencies; `ĥ_μ` taken as `Ĥ(L_max) − Ĥ(L_max − 1)`; `Ê(L) = Ĥ(L) − L·ĥ_μ`). No bias correction, no confidence interval — [#107](https://github.com/NGL321/mosaic/issues/107).

| system | samples | Order = 1 − ĥ_μ | Ê at L_max | true E |
|---|---|---|---|---|
| (p, 1−p) Bernoulli map, p = 0.110028 | 4 × 10⁶ | 0.4994 | +0.0029 bits (L = 12) | 0 |
| untrained feed-forward tanh net, i.i.d. input | 2 × 10⁶ | 0.5003 | +0.0014 bits (L = 10) | 0 |
| untrained recurrent net, gain 1.5, i.i.d. input | 2 × 10⁶ | 0.5072 | +0.0223 bits (L = 10) | > 0 |
| untrained leaky recurrent net, α = 0.12 | 2 × 10⁶ | 0.7530 | +0.302 bits (L = 12) | > 0 |

**The Bernoulli map behaves exactly as §2 predicts.** `Ĥ(L)` came out linear in `L` to five decimal places — 0.50090, 1.00180, 1.50270, 2.00359, … — which is the signature of `E = 0`: a block entropy with no intercept. `ĥ_μ(L)` held at 0.50090 from `L = 1` to `L = 8`.

**The network is the case Mosaic might actually search, and it is the one worth the ticket.** The feed-forward system is a randomly-initialised two-hidden-layer `tanh` network (30 → 64 → 64 → 1) driven by i.i.d. Gaussian input, its scalar output thresholded at the 89th percentile so that the output stream's marginal is biased and Order lands at ½. Its Order coordinate is squarely intermediate — it is not a crystal and it is not a fair coin — and its Capacity is zero, for a reason that is a property of the architecture's *dynamics*: a feed-forward map has no state carried between time steps, so it cannot introduce temporal dependence that its input did not already have. Under an i.i.d. drive the output stream is i.i.d., whatever the network's internal complexity. A large network is a complicated object; on this axis it holds nothing.

This is the exclusion the Bound needs to be able to make and could not make before. An Order-only Bound looks at that system, reads 0.50, and admits it for search. The pair reads (0.50, ≈0) and refuses it. Nothing about the refusal depends on the network being untrained, small, or synthetic — it depends only on the map from input stream to output stream being memoryless.

**The recurrent contrast is the control, and it is honest about how thin the margin is.** Give the same network recurrent state and drive it identically, and Capacity becomes positive at matched Order: 0.0223 bits against the feed-forward system's 0.0014 at Order ≈ 0.50. That is a factor of sixteen and it is in the right direction, but 0.0223 bits is not much larger than the numbers an estimator with no bias correction produces from nothing, which is exactly why [#107](https://github.com/NGL321/mosaic/issues/107) is filed rather than waved at. Slowing the recurrence (a leaky integrator, α = 0.12) makes the separation unambiguous — `Ê = 0.302` bits, an `Ĥ(L)` curve with a visible intercept — but it also drags Order to 0.75, so it is a different point in the plane and not a matched control.

**A physical realisation, worked rather than measured.** Feldman/McTague/Crutchfield's Eq. (22) Hamiltonian for a one-dimensional spin chain, `H = −J₁ Σ_nn S_iS_j − J₂ Σ_nnn S_iS_j − B Σ S_i`, sits at `J₁ = J₂ = 0` on the edge of their own sampled parameter range. There the Boltzmann weight factorises over sites, the configuration is i.i.d. with `p = 1/(1 + e^{−2B/T})`, and the chain is a **paramagnet in an applied field**: `E = 0` exactly, `h_μ = H(p)` anywhere in `(0,1)`. At `B/T ≈ 1.045` the chain sits at Order 0.500, Capacity 0. This is an equilibrium physical system, with a temperature, in a model class the same authors chart. It is derived from their Hamiltonian, not read off their figure, and is offered as evidence that the case is not an artefact of digital constructions.

## 4. Does it discriminate? Against one axis yes, against every one axis no — and the fix is a fourth case

This is the ticket's whole purpose, so it gets a direct answer in both directions.

**Against an Order-only Bound: yes, decisively.** Run the three cases against a one-dimensional operationalisation that keeps only `Order = 1 − h_μ/log₂|A|` and excludes the extremes:

| case | Order | Capacity `E` | Order-only rule | the (Order, E) pair |
|---|---|---|---|---|
| diamond (period-p crystal) | 1 | log₂ p (4 bits at p = 16) | excluded | excluded |
| thunderstorm (fair coin) | 0 | 0 | excluded | excluded |
| **memoryless system** (biased coin, Bernoulli map, feed-forward net) | 0.500 | 0 | **admitted** | **excluded** |

That is an identification test where [#87](https://github.com/NGL321/mosaic/issues/87) had only a non-exclusion test. A later reader who wants to attack the two-dimensional proposal now has something cheap to attack: show that a memoryless system at middling Order *ought* to be searched, and the Capacity axis loses its warrant.

**Against a Capacity-only or `C_μ`-only Bound: no, and this is the honest half.** A one-dimensional rule of the form "`E` (or `C_μ`) must lie strictly between a floor and a ceiling" excludes the diamond by its ceiling and both coins by its floor. It passes all three cases. The third case therefore does not, by itself, establish that Order is load-bearing — only that Capacity is.

**What closes it is a fourth datum, and Feldman/McTague/Crutchfield hand it over in closed form.** Their family `F_{p,b}` of p-cyclic ε-machines with `b` branchings between successive states satisfies their Eqs. (25) and (26): `E(F_{p,b}) = log₂ p` and `h_μ(F_{p,b}) = b/p`. Take `p = 5`, `b = 3`. Then:

| case | Order | `E` | `C_μ` |
|---|---|---|---|
| period-5 crystal | **1** | log₂ 5 = 2.3219 bits | log₂ 5 |
| `F₅,₃` (period-5 cycle, 3 branchings) | **0.4** | log₂ 5 = 2.3219 bits | log₂ 5 |

The diamond and a positive-entropy structured process are **exactly equal** on both Capacity measures — both ε-machines are five-state cycles — and are separated only by Order. A Capacity-only rule that excludes the crystal excludes `F₅,₃` too, and `F₅,₃` is the sort of thing a Bound must admit: it produces information at 0.6 bits per symbol and carries 2.32 bits of it from its past into its future.

So the test data, extended, reads: **the memoryless line kills Order-alone; the `F_{p,b}` coincidence kills Capacity-alone and `C_μ`-alone; the pair survives both.** That is what makes the Bound two-dimensional in evidence. It took two new cases, not one, and the ticket's framing — that one case would do it — is half right.

A note on `C_μ`, which [#87](https://github.com/NGL321/mosaic/issues/87) rated **Loose** on computability grounds: the simple nondeterministic source (§1) is a second, independent reason to prefer `E`. It has `C_μ = ∞` and `E ≈ 0.147` bits. A `C_μ`-based Bound would rank it maximally complex; an `E`-based Bound places it just above the exclusion line. Whichever is right, the two axes disagree sharply on a three-state Markov chain, so `C_μ` is not a refinement of `E` that can be reached for casually. The Crutchfield & Young result that `C_μ` "vanishes for trivially periodic and for purely random data sets" is carried from [#87](https://github.com/NGL321/mosaic/issues/87) and was not re-opened here.

## 5. Under [#102](https://github.com/NGL321/mosaic/issues/102)'s two readings the case comes apart — which is an argument for one of them

[#102](https://github.com/NGL321/mosaic/issues/102) asks whether Informational Capacity is the excess entropy of the **candidate system's own dynamics** or of **what an engine observes**. The third case behaves differently under the two, and the difference is not a detail.

**Reading A — the candidate system's own dynamics. A clean, unconditional exclusion.** The Bernoulli map's symbolic dynamics under its generating partition is i.i.d.; the feed-forward network's input-to-output stream map carries no state; the paramagnet's configuration measure factorises over sites. In each case `E = 0` is a fact about the system, evaluable before any engine is identified in it, which is what makes the Bound a search restriction. The case is an exclusion, full stop.

**Reading B — what an engine observes. The exclusion is fragile in both directions.** An engine observing a memoryless source through a sensor that itself has memory — a leaky integrator, a sliding window, any temporal filter — sees a process with `E > 0`. §3's recurrent control is precisely this experiment performed on the system side: identical i.i.d. drive, memory added downstream, Capacity rises from 0.0014 to 0.0223 bits at matched Order. Move that memory from the system into the observer and the arithmetic is unchanged. So under Reading B the *same* candidate is excluded for an engine with an instantaneous sensor and admitted for an engine with a filter, and the Bound stops being a property of the search space and becomes a property of the searcher's instrument. Conversely, [#102](https://github.com/NGL321/mosaic/issues/102)'s own example runs the other way — a low-bandwidth sensor onto a high-capacity world reads `E ≈ 0` and would exclude a system that Reading A admits.

**The case therefore bears on [#102](https://github.com/NGL321/mosaic/issues/102), and the direction is Reading A.** A Bound whose verdict on a fixed candidate changes when you swap the observing instrument cannot bound a search, because the search has not yet chosen an instrument. That is a structural argument, not a measurement, and it does not touch [#102](https://github.com/NGL321/mosaic/issues/102)'s third option — that both quantities are wanted, the Bound's axis on the system and `Extraction`'s ceiling on the observation — which this document takes to be the likeliest resolution and does not attempt to settle.

**And on the third option, the cost is visible here.** If Informational Capacity is read on the system, then [#87](https://github.com/NGL321/mosaic/issues/87)'s headline reuse — that Informational Capacity was already in `CONTEXT.md` as `Extraction`'s unnamed denominator — does not survive, because `Extraction`'s ceiling is explicitly "the ceiling set by the observed process itself". The third case does not decide that; it makes the price of each option concrete. Under Reading A the Bound works and the reuse fails; under Reading B the reuse holds and the Bound becomes engine-relative.

## 6. The falsifier branch, considered and not taken

The ticket is explicit that "I found a case" is not the required answer, and that if intermediate Order entailed non-negligible Capacity the finding would argue for collapsing the Bound to one dimension. That branch was live and it did not fire. The evidence against it is of three kinds, and they are independent:

1. **Geometric.** `h_μ` and `E` are the slope and the intercept of the asymptote of `H(L)`; free parameters of a line. Feldman/McTague/Crutchfield, §II D.
2. **Analytic.** Biased i.i.d. sources realise `E = 0` at every `h_μ ∈ (0, log₂|A|)`, and — [#105](https://github.com/NGL321/mosaic/issues/105) — they are the *only* processes that do so exactly. Crutchfield & Feldman §VI A, plus a derivation.
3. **Ensemble.** Li's survey of one-step two-symbol Markov chains finds the relationship "many-to-one or one-to-many", with "no universal relationship between complexity and entropy independent of the underlying sequences". Confirmed here numerically: scanning order-1 binary chains at `h_μ = 0.500 ± 0.002`, Capacity ranges from `E = 0.00000` bits (at `P(1|0) = 0.11`, `P(1|1) = 0.11` — the independent chain) to `E = 0.5013` bits, which is the `R = 1` case of Feldman/McTague/Crutchfield's Eq. (15) bound `E ≤ R(1 − h_μ) = 0.5` saturated. The whole vertical interval is occupied.

Where the branch *would* have fired is worth recording, because it is the honest form of the near-miss: inside a single one-parameter family, an intermediate entropy rate can perfectly well force positive excess entropy. §2 gives the case — the symmetric tent map, where `E = −log₂ h_μ` and the only zero-Capacity point is the fair coin. A survey that had sampled the plane through that family and stopped would have reported the falsifier. The reason it is wrong is that the family is a curve in a plane, not the plane, which is the same objection Mitchell/Crutchfield/Hraber made to λ and [#87](https://github.com/NGL321/mosaic/issues/87) §8 made to reading coverage of the plane as coverage of the region. Three appearances of one error in one Bound is enough to name it: **a parameterisation of some systems is not the space of systems**, and no result about a family transfers to the region without an argument.

---

## What this does not establish

### Sources not reached

**Crutchfield & Young (1989) and Schoenholz et al. (2017) were not re-opened in this session.** Both are in the appendix because claims here lean on them, and both are carried at the depth [#87](https://github.com/NGL321/mosaic/issues/87) reached them — full text for the former, abstract only for the latter. The `C_μ` "vanishes for trivially periodic and for purely random data sets" quotation in §4 is therefore second-hand within Mosaic's own record, which is better than recall and worse than reading.

**Kolmogorov (1958), Sinai (1959) and Rokhlin on generating partitions** were not attempted, and they are what would turn §2's Bernoulli-map construction from a claim about a symbol stream into a claim about a map. [#106](https://github.com/NGL321/mosaic/issues/106). **Cover & Thomas, or any measure-theoretic text stating past–future independence implies full independence**, was likewise not reached, so §1's central equivalence stands on a four-line derivation ([#105](https://github.com/NGL321/mosaic/issues/105)). **Grassberger's and Nemenman–Shafee–Bialek's entropy estimators** were not read, which is why §3's numbers carry no error bars ([#107](https://github.com/NGL321/mosaic/issues/107)). **Kauffman** remains unreached from [#87](https://github.com/NGL321/mosaic/issues/87), and it matters here too: random Boolean networks are the obvious place to look for a memoryless system with a closed-form membership test, and [#100](https://github.com/NGL321/mosaic/issues/100) is still open. **Shaw (1984)**, whom Li credits with the past–future mutual information and the block-entropy geometry, was not attempted; **Grassberger (1986)** on effective measure complexity likewise. Neither is load-bearing, because Crutchfield & Feldman and Li were both read directly.

### Open gaps

**The threshold is unnamed.** §1 establishes that "excluded on Capacity" has to mean `E < ε` and not `E = 0`, and this document does not propose an `ε`. It cannot, honestly, until [#107](https://github.com/NGL321/mosaic/issues/107) says what the estimator's noise floor is: at 2 × 10⁶ samples the plug-in estimator returned +0.0014 bits from a process with exactly none, and a genuinely weakly-correlated recurrent network sixteen times that. Those are the same order of magnitude, and a threshold between them would be a coin flip dressed as a decision procedure. The same gap sits on the Order axis, where [#87](https://github.com/NGL321/mosaic/issues/87) already recorded that the region's boundaries are unnamed.

**Nothing was measured on a system Mosaic actually cares about.** §3's networks are *randomly initialised*, which is the same limit [#87](https://github.com/NGL321/mosaic/issues/87) §5 flagged on the Schoenholz and Poole results. Whether a *trained* transformer's output stream carries measurable excess entropy is unmeasured and is a far more interesting question than anything in this document — it is the one case where the Bound would say something the programme could act on.

**The `F_{p,b}` fourth case was taken from a formula, not computed.** §4's identification argument leans on `E(F_{p,b}) = log₂ p` and `h_μ(F_{p,b}) = b/p`. Both are Feldman/McTague/Crutchfield's Eqs. (25) and (26), read directly, but the coincidence with the period-5 crystal's coordinates was not independently verified, and it is doing real work: it is the entire case against a Capacity-only Bound.

**Whether a memoryless system can be an Inference Engine at all is not asked here.** `CONTEXT.md` requires an engine's internal state to carry predictive information about states beyond its blanket. If a memoryless environment makes that impossible by construction, then §3's feed-forward network is excluded twice over and the Bound is doing work the vocabulary already did — which would be a pleasing convergence and might also mean the third case is less independent evidence than §4 claims. Not investigated.

### Load-bearing ifs

**If exact `E = 0` does not force i.i.d.** — if some stationary process with memory nonetheless has zero past–future mutual information — then §1's characterisation is wrong, the third case is not the memoryless line but merely *contains* it, and rows 1 and 2 both move. The derivation is four lines and rests entirely on `I[past_L ; future_L]` being non-decreasing in `L`; if that monotonicity fails for some pathological process the argument fails with it. [#105](https://github.com/NGL321/mosaic/issues/105).

**If the (p, 1−p) map's partition is not generating**, §2's deterministic realisation evaporates and the case retreats to stochastic sources — a biased coin and a paramagnet — which still satisfy §1 and §3 but are much weaker answers to the ticket's demand for a *dynamical* characterisation, because a coin has no state space to speak of. The network case in §3 would then be doing all the work alone. [#106](https://github.com/NGL321/mosaic/issues/106).

**If Informational Capacity is read on the observed process rather than on the system** — [#102](https://github.com/NGL321/mosaic/issues/102)'s Reading B — then the third case is not an exclusion at all, only an exclusion *for engines with memoryless sensors*, and row 6's discrimination weakens accordingly: an Order-only Bound and the pair would disagree about the biased coin only for some observers. §5 argues this is a reason to reject Reading B, but that argument is structural and someone could reasonably take the other branch and keep [#87](https://github.com/NGL321/mosaic/issues/87)'s `Extraction`-ceiling reuse instead.

**If a Bound is allowed to be a conjunction of one-dimensional rules on `C_μ` alone**, §4's identification collapses. The `F_{p,b}` argument against `C_μ`-alone assumes the rule is a single interval; a rule that also conditions on something else — the ε-machine's topology, say — could separate the crystal from `F₅,₃` without an entropy-rate axis. Nothing here rules that out; what it rules out is the *simple* one-dimensional rival, which is the one a later reader would actually propose.

**If §3's feed-forward network is not the kind of thing Mosaic searches**, row 4 flips to Unresolved and the case is synthetic after all. The claim that it is searchable rests on the computational window Bound — that Mosaic investigates the computational-stochastic fraction of cognition on the evidence of deep learning — and on nothing else.

---

## Verification Debt

Three items, all newly filed, all `debt:open`. None was dischargeable within this session; each names what would discharge it.

1. **[#105](https://github.com/NGL321/mosaic/issues/105) — `E = 0` implies i.i.d. is derived here, never read in a source.** The structural claim that fixes the shape of the whole answer — that the exact-zero-Capacity locus is precisely the memoryless line — is a four-line derivation from the monotonicity of past–future mutual information. Feldman/McTague/Crutchfield's single-state ε-machine remark corroborates it for topological machines under a uniform measure and no further. Discharged by a measure-theoretic statement of the equivalence, or by a counterexample.
2. **[#106](https://github.com/NGL321/mosaic/issues/106) — the skew Bernoulli map's generating partition and Kolmogorov–Sinai entropy are asserted, not read.** §2's deterministic realisation needs the partition at the kink to be generating, or its `h_μ` is a property of the coarse-graining rather than of the map. This is the specific, sharpest instance of the symbolisation worry the previous survey recorded in general — that both axes are defined on a symbol sequence and the answer moves with the partition. Discharged by reading Kolmogorov–Sinai and the generating-partition theorem, or by recomputing the coordinates under a deliberately non-generating partition and reporting the movement.
3. **[#107](https://github.com/NGL321/mosaic/issues/107) — "excluded on Capacity" has no measured noise floor, so the threshold cannot be set.** §3's plug-in estimator returns +0.0014 to +0.0029 bits on processes whose true excess entropy is exactly zero, which is the same order as the excess entropy of the recurrent control that genuinely has some. Narrower and newer than the standing "no validated estimator, nothing measured" debt: something has now been measured, and the measurement is what exposes the gap. Discharged by a bias-corrected estimator with a confidence interval, run on a process of known `E`, reporting a minimum detectable `E` at declared sample size.

---

## Proposals

Two items. `CONTEXT.md` and the charter are human-only custody under [`PROTOCOL.md` §5](../../PROTOCOL.md); these are exact text for Noah to apply, reject or rewrite.

### 1. A third case in the Edge of Chaos Bound's text

The Bound as settled in [#6](https://github.com/NGL321/mosaic/issues/6) reads:

> Mosaic searches only systems balancing **Informational Capacity** against **Order** — excluding the over-ordered (a diamond: enormous capacity, far too much order, and no one says it thinks) and the under-ordered (a thunderstorm), while allowing that **incidental cognition may exist outside the region**.

Proposed replacement, incorporating [#87](https://github.com/NGL321/mosaic/issues/87)'s correction to the diamond gloss so the two proposals do not collide:

> Mosaic searches only systems balancing **Informational Capacity** against **Order** — excluding the over-ordered (a diamond: an astronomical number of configurations, almost none of that structure carried from its past into its future, and no one says it thinks), the under-ordered (a thunderstorm), and the **memoryless** (a biased coin, or an untrained feed-forward network fed noise: middling order, and still nothing of its past held in its future) — while allowing that **incidental cognition may exist outside the region**.

The third case is the one that earns the second axis. A diamond and a thunderstorm sit at opposite corners and are refused by either coordinate alone, so they cannot tell this Bound from a one-dimensional one; a memoryless system at middling Order is refused only by Capacity. Companion note, if the charter carries reasoning alongside its commitments: the crystal is refused only by Order, since a period-5 cycle and a period-5 cycle with branchings carry identical Informational Capacity and differ only in entropy rate.

### 2. A sentence for the `Informational Capacity` entry [#87](https://github.com/NGL321/mosaic/issues/87) proposed

[#87](https://github.com/NGL321/mosaic/issues/87)'s draft `CONTEXT.md` entry for `Informational Capacity` should not be landed with an exclusion criterion of `E = 0`, because §1 shows that locus is exactly the i.i.d. processes and nothing physical will measure it. Proposed addition to that entry's `_Departs_` line:

```markdown
Exclusion on this axis is a **threshold and not a zero test**: excess entropy vanishes
exactly only for memoryless processes, so the Bound refuses systems whose past–future
mutual information is *small*, not systems where it is nil. Where the threshold sits is
open, and is bounded below by what an entropy-rate estimator can distinguish from zero.
```

No proposal is made on [#102](https://github.com/NGL321/mosaic/issues/102). §5 argues for the system-dynamics reading and states the price; the decision is that ticket's.

---

## Appendix: primary sources

1. James P. Crutchfield & David P. Feldman (2001), *Regularities Unseen, Randomness Observed: Levels of Entropy Convergence*, SFI Working Paper 01-02-012; **Chaos 13**:25–54 (2003). Read in full this session from the arXiv PDF, converted to text: [arXiv:cond-mat/0102181](https://arxiv.org/abs/cond-mat/0102181). §VI A for the fair and biased coins and the "Historical information does not improve predictability" passage; §VI D for the golden mean process (`h_μ = 2/3`, `E ≈ 0.2516`); §VI E for the even process (`h_μ = 2/3`, `E ≈ 0.902`) and RRXOR (`h_μ = 2/3`, `E = 2`); §VI F for the simple nondeterministic source (`h_μ ≈ 0.6778`, `E ≈ 0.147`, infinitely many causal states); Table III for the summary; Props. 7 and 8 for the subextensive and mutual-information readings of `E`; Defs. 1–2 for finitary/infinitary.
2. David P. Feldman, Carl S. McTague & James P. Crutchfield (2008), *The Organization of Intrinsic Computation: Complexity-Entropy Diagrams and the Diversity of Natural Information Processing*, **Chaos 18**:043106. Read in full this session from the authors' copy, converted to text: [csc.ucdavis.edu/~cmg/papers/oic.pdf](https://csc.ucdavis.edu/~cmg/papers/oic.pdf) (also [arXiv:0806.4789](https://arxiv.org/abs/0806.4789)). §II D for the slope-and-intercept independence argument and Eq. (15) `E ≤ R(1 − h_μ)`; §III A 2 and Eq. (21) for the tent map's `E = −log₂ h_μ`; Eq. (22) for the Ising Hamiltonian used in §3's paramagnet derivation; §III D for the ε-machine enumeration, the single-state `E = 0` remark, and Eqs. (25)–(26) for the `F_{p,b}` family.
3. Wentian Li (1991), *On the Relationship between Complexity and Entropy for Markov Chains and Regular Languages*, **Complex Systems 5**:381–399. Read in full this session from the journal's page scan, which carries an OCR layer: [content.wolfram.com/sites/13/2018/02/05-4-3.pdf](https://content.wolfram.com/sites/13/2018/02/05-4-3.pdf). Abstract and §1 for the many-to-one relationship and "no universal relationship between complexity and entropy"; §2, Eqs. (2) and (6), for past–future mutual information and the block-entropy intercept; §3, Eqs. (10)–(15) and Fig. 4, for the one-step two-symbol Markov chain scatter.
4. Melanie Mitchell, James P. Crutchfield & Peter T. Hraber (1993), *Dynamics, Computation, and the "Edge of Chaos": A Re-Examination*. §2 re-read this session from the arXiv PDF, converted to text: [arXiv:adap-org/9306003](https://arxiv.org/pdf/adap-org/9306003). Cited only for the rule-table objection quoted in §2, which is the constraint the third case had to satisfy.
5. James P. Crutchfield & Karl Young (1989), *Inferring Statistical Complexity*, **Phys. Rev. Lett. 63**:105–108. **Not re-opened this session**; read in full for [#87](https://github.com/NGL321/mosaic/issues/87) from the [APS full text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.63.105/fulltext). The only claim resting on it here is that `C_μ` vanishes for trivially periodic and purely random data, used in §4.
6. Samuel S. Schoenholz, Justin Gilmer, Surya Ganguli & Jascha Sohl-Dickstein (2017), *Deep Information Propagation*, ICLR 2017. **Not re-opened this session**; abstract read for [#87](https://github.com/NGL321/mosaic/issues/87): [arXiv:1611.01232](https://arxiv.org/abs/1611.01232). Cited only for the ordered/chaotic phase framing of randomly-initialised networks that §3's controls sit inside.
