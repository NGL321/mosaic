---
ticket: 98
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 5
debt: [123, 124]
supersedes: null
---

# Pesin's identity is true and does not reach the systems Mosaic searches — the Order axis has one estimator, not four

Five primary sources were opened and read in full: Pesin (1977) from the Math-Net.Ru English full text, Ruelle (1978) from the author's own copy at IHÉS, Mitchell/Hraber/Crutchfield (1993) from the first author's copy of the *Complex Systems* paper, Beggs & Plenz (2003) from a capture of the publisher's PDF, and Tisseur (2000) from the arXiv deposit of the *Nonlinearity* paper. Every quotation below is transcribed from one of those five documents; where a scan's OCR mangles a symbol the mangling is silently repaired and the symbol named in words. Nothing here is recalled. Packard (1988) — the origin of the spreading rate Γ — was **not** reached, and Shereshevsky (1991) was reached only through Tisseur's restatement of it; both are recorded under *Sources not reached*, and no verdict below rests on either. None of this has been checked by Noah unaided.

---

## 0. Verdict

| Sub-question | Verdict | Argued in |
|---|---|---|
| **1** What does Pesin's identity state, and under what hypotheses? | **Established** — equality between entropy and the integrated sum of positive exponents, for a C² diffeomorphism of a compact smooth Riemannian manifold preserving a measure *equivalent to the Riemannian volume* | §1 |
| **2** Is the hypothesis "SRB / absolutely continuous invariant measure", as the ticket assumed? | **Refuted** — Pesin (1977) never mentions SRB; his hypothesis is the strictly stronger "equivalent to the Riemannian volume" | §1 |
| **3** What does Ruelle's inequality state, and how much weaker are its hypotheses? | **Established** — h(p) ≤ p(λ⁺) for *any* invariant probability measure of *any* C¹ map of a compact manifold, not necessarily invertible | §2 |
| **4** Does h_μ > 0 ⟹ λ_max > 0 survive in the smooth setting? | **Supported** — this direction is Ruelle's, and needs none of Pesin's extra hypotheses | §2 |
| **5** Does the converse, λ_max > 0 ⟹ h_μ > 0, hold in general? | **Refuted** — Ruelle himself poses it as an open question in 1978, and it fails outright off the manifold | §2, §3 |
| **6** Does h_μ > 0 ⟺ λ_max > 0 hold for the systems Mosaic intends to search? | **Refuted** — a published cellular automaton has λ⁻ = 2 and h_μ = 0 under the uniform measure | §3 |
| **7** Does any source state that Γ is the Lyapunov exponent? | **Refuted** — the cited source states the opposite, twice, in one paragraph | §4 |
| **8** Does any source state a σ ↔ λ_max or σ ↔ h_μ correspondence? | **Unresolved** — none was reached; Beggs & Plenz do not, and the claim's provenance is untraced | §5 |
| **9** What does σ = 1 mark in Beggs & Plenz, and is it claimed to be the Edge of Chaos? | **Established** — the critical point of a branching process, "the edge of stability"; no claim about chaos, entropy rate or exponents appears in the paper | §5 |
| **10** Are the four quantities estimators of one Order axis? | **Refuted** — they are four different measurements, related where at all by strict inequalities | §6 |
| **11** Is narrowing the axis to a single named estimator the correct discharge? | **Supported** — h_μ is the only one of the four that is defined on every system the Bound must place | §6 |

### The one-line verdict

> **Pesin's identity is exactly true and almost entirely out of reach.** It holds for C² diffeomorphisms of compact Riemannian manifolds preserving a measure equivalent to the volume; a cellular automaton, a Boolean network and a spiking cortex are none of those. Ruelle's inequality survives the loss of every extra hypothesis but gives only one direction, h_μ > 0 ⟹ λ_max > 0. Off the manifold even that has to be rebuilt by hand, and the rebuilt version has a published counterexample in which the exponent is positive and the entropy rate is zero. The four estimators are not one axis; **Order should be narrowed to h_μ**, and λ_max, Γ and σ demoted to separately named diagnostics.

---

## 1. What Pesin (1977) states, and the hypotheses it states it under

The paper is [*Characteristic Lyapunov exponents and smooth ergodic theory*, Russian Math. Surveys **32**:4 (1977), 55–114](https://www.mathnet.ru/eng/rm3219), read in full from the English full text. The standing hypotheses are set in §1.1 and are not weakened anywhere later. Verbatim:

> "The smooth ergodic theory studies the ergodic properties of smooth dynamical systems on smooth compact Riemannian manifolds, preserving a given normalized measure, denoted by ν, which is compatible with the smoothness (that is, equivalent to the Riemannian volume)."

Three separable conditions live in that sentence: the phase space is a **smooth compact Riemannian manifold**; the map is a **diffeomorphism** of it; and the invariant measure is **equivalent to the Riemannian volume**. §5.1 adds the smoothness class: "Let *f* be a C²-diffeomorphism of *M* preserving the measure ν."

The identity itself is Theorem 5.1, on p. 81:

> "THEOREM 5.1. The entropy h(f) of the diffeomorphism f satisfies the equality
> h(f) = −∫_M Σ_{i=1}^{k(x)} q_i(x) χ_i(x) dν"

with k(x) "the number of negative values of χ⁺ at x", q_i the multiplicities, and "for k(x) = 0 the empty sum is taken to be zero". §1.6 gives the same result in the form the phrase "Pesin's identity" usually carries: "the entropy is equal to the integral of the sum of the positive characteristic Lyapunov exponents."

**Two findings here that the ticket's framing did not anticipate.**

*First, the smoothness class is not incidental and Pesin flags it himself.* §1.6, verbatim: "We emphasize one interesting (not to say odd) fact: Margulis's result is true for dynamical systems of class C¹, whereas the lower estimate is obtained for systems of class C² (it can be proved for class C^{1+ε})." So the two halves of the identity have *different* hypotheses. The upper bound — what became Ruelle's inequality — is C¹. The lower bound, the half that turns an inequality into an identity, is C² in this paper and C^{1+ε} at best. The ticket's "C^{1+alpha}" is right about the floor and wrong about which half needs it.

*Second, "SRB" is not Pesin's hypothesis.* The string does not occur in the paper, in any spelling. Pesin requires ν **equivalent to the Riemannian volume** — mutual absolute continuity with volume on the whole manifold. An SRB measure is a strictly weaker object: absolutely continuous *conditionals on unstable manifolds*, typically singular with respect to volume, and the extension of the identity to that class is later work by other people that this document did not read. The ticket's parenthetical "SRB / absolutely continuous invariant measure" collapses two different conditions, and the difference is load-bearing: a dissipative attractor carries an SRB measure and does not carry a measure equivalent to volume, so it is outside Theorem 5.1 as stated.

**The biconditional the ticket wants is in the paper, but it is stated about a different quantity.** §1.6, verbatim: "We emphasize that the entropy being positive and the condition (1.7) are equivalent." And (1.7) is:

> "the set A = {x ∈ M: there is a vector v ∈ T_xM for which χ⁺(x, v) < 0} has positive measure."

That is positive entropy if and only if a **negative** exponent exists on a positive-measure set. Getting from there to λ_max > 0 requires the exponents to be symmetric enough that a negative one forces a positive one — which is true when ν is equivalent to volume, and is exactly the hypothesis being spent. The step is not written out in the paper and is not verified here; it is listed under *Load-bearing ifs*.

## 2. Ruelle (1978): weaker hypotheses, one direction, and an open question

[*An inequality for the entropy of differentiable maps*, Bol. Soc. Bras. Mat. **9** (1978), 83–87](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B51%5D.pdf) is five pages and was read in full from the author's copy at IHÉS. Theorem 2 opens:

> "Let M be a C^∞ compact manifold and f : M → M a C¹ map."

and concludes, with λ⁺(x) defined as the sum of the positive exponents counted with multiplicity:

> "Then, for every p ∈ I the entropy h(p) satisfies h(p) ≤ p(λ⁺) [where p(λ⁺) = ∫ p(dx) λ⁺(x)]."

I is "the set of f-invariant probability measures on M". Compare the hypotheses line by line against §1: **C¹ rather than C²**, **a map rather than a diffeomorphism** — Ruelle notes that Oseledec's theorem as published "assumes τ and T invertible" and that his Theorem 1 drops that — and, decisively, **every invariant probability measure rather than one equivalent to volume**. Ruelle's inequality is the general fact; Pesin's identity is the special case bought with three extra hypotheses.

**One direction survives the generalisation and the other does not.** h_μ > 0 forces p(λ⁺) > 0, hence a positive exponent on a positive-measure set. That is the direction Mosaic can have for free wherever a compact manifold and a C¹ map exist. The converse — a positive exponent forcing positive entropy — is not available, and Ruelle says so in the last paragraph of the paper. §3, *Remark*, verbatim:

> "The inequality h(p) ≤ p(λ⁺) was known for axiom A diffeomorphisms and for the time one map of axiom A flows [5], [6]. It is also obvious for quasi-periodic maps of the m-torus. A related result was proved for certain diffeomorphisms preserving a smooth measure by Margulis and Pesin [3]. In all those cases one has sup_ρ [h(p) − p(λ⁺)] = 0.
> Question. Is this "variational principle" true in general?"

The author of the inequality, writing in 1978 with Pesin's paper in his bibliography, treats *equality in general* as an open question and marks it with the word "Question". Any document that treats h_μ > 0 ⟺ λ_max > 0 as a standing fact is claiming something the primary literature explicitly declined to claim at the point where both halves were established.

## 3. Off the manifold: the cellular-automaton counterexample

This is the decisive finding, and it is not a hypothesis-counting argument — it is a published counterexample.

A cellular automaton has no tangent bundle. Its configuration space is A^ℤ for a finite alphabet A, a Cantor set, not a smooth compact Riemannian manifold; its transition map is continuous but not differentiable, because there is nothing to differentiate. Neither Pesin's Theorem 5.1 nor Ruelle's Theorem 2 has a hypothesis that a CA satisfies. Both are silent, not false, and silence is what a search programme cannot use.

The CA literature responded by *building* an analogue rather than borrowing one, which is itself evidence that the borrowing does not work. Tisseur's [*Cellular automata and Lyapunov exponents*, Nonlinearity **13** (2000) 1547–1560](https://arxiv.org/abs/math/0312136) opens its introduction with the history: "For differential systems, the Lyapunov exponents are essentially local properties and it is natural to introduce a corresponding definition in the discrete frame of a cellular automaton, defined by a local rule." Wolfram "call Lyapunov exponents the speed of these propagations and suspect that there exists relations between the spatial and temporal entropies and these exponents"; Shereshevsky supplied a definition in 1991 and proved, in Tisseur's transcription:

> "Shereshevsky establishes an inequality presumed by Wolfram and similar to the Pesin one ([15] or [16]) in the differentiable case:
> h_μ(F) ≤ h_μ(σ)(λ⁺_μ + λ⁻_μ)"

Note the shape. What the CA setting supports is an **inequality**, analogous to Ruelle's, with an extra factor of the shift's entropy — not an identity. And Tisseur's abstract states the strictness outright: the examples are "both proving that average exponents provide a better bound for the entropy, and one showing that the inequalities are strict in general."

**Example 6.1 is the counterexample the ticket needs.** Tisseur takes a Coven aperiodic CA of radius 2 with aperiodic word B = 10, and μ the uniform measure on {0,1}^ℤ — a measure that is shift-ergodic and F-invariant, the natural choice, not a pathological one. Verbatim:

> "If μ is the uniform measure I⁺_μ + I⁻_μ = 0 by Proposition 5.2 and h_μ(F) = 0. On the contrary the sum of the maximum Lyapunov exponents is strictly positive."

He then computes λ⁺_μ = 0 and λ⁻_μ = 2 and concludes: "From Theorem 5.1 we get h_μ(σ)(λ⁺_μ + λ⁻_μ) = 2 log 2 > h_μ(F) = 0." A strictly positive maximal Lyapunov exponent, an entropy rate of exactly zero, in the same system under the same measure. Tisseur states the general moral himself in Remark 6: "The condition h_μ(σ)(I⁺_μ + I⁻_μ) > 0 does not imply that h_μ(F) > 0."

**So the biconditional does not merely lose its warrant off the manifold; it is false there.** A system Mosaic would classify as "chaotic, Order low" by reading its exponent is classified "perfectly ordered, Order maximal" by reading its entropy rate. The two estimators do not disagree at the margin — on this example they return opposite ends of the axis.

## 4. Γ is not the Lyapunov exponent, and the source says so twice

The ticket asked for the Mitchell/Crutchfield/Hraber quotation to be verified against the original. It is verified, and the sentence *after* it matters more than the sentence quoted.

From [*Revisiting the Edge of Chaos: Evolving Cellular Automata to Perform Computations*, Complex Systems **7**:89–130 (1993)](https://melaniemitchell.me/PapersContent/rev-edge.pdf), §3, discussing Packard's location of λ_c, verbatim — the paper writes the spreading rate as lower-case γ, not Γ:

> "The spreading rate γ is a measure of unpredictability in spatio-temporal patterns and so is one possible measure of chaotic behavior [22, 31]. It is analogous to, but not the same as, the Lyapunov exponent for continuous-state dynamical systems. In the case of CA it indicates the average propagation speed of information through space-time, though not the rate of production of local information."

The quoted disclaimer is exact. The clause the ticket did not carry — "the average propagation speed of information through space-time, though not the rate of production of local information" — is the stronger finding, because *the rate of production of local information is precisely h_μ*. In one sentence the authors deny that γ is λ and deny that γ is the entropy rate. Two of the four claimed equivalences are refused in the same breath by the paper the operationalisation cites for γ.

The paper also undercuts γ as an estimator of anything at the system level: "While not shown in Figure 2, for most λ values γ's variance is high… That is, the behavior of any particular rule at a given λ might be very different from the average behavior at that value. Thus, the interpretations of these averages is somewhat problematic." γ is reported there as a Monte-Carlo average over sampled rules, and Figure 2 is reproduced from Packard with the note "No vertical scale was provided there."

## 5. σ = 1 marks the edge of stability, and Beggs & Plenz never mention chaos

[*Neuronal avalanches in neocortical circuits*, J. Neurosci. **23**(35):11167–11177 (2003)](https://web.archive.org/web/2020/https://www.jneurosci.org/content/jneuro/23/35/11167.full.pdf) was read in full from a capture of the publisher's PDF; the live publisher URL is behind a bot challenge, recorded under *Sources not reached* for what that costs.

The definition, from *Materials and Methods*, verbatim:

> "By definition, σ is the average number of descendants from one ancestor (de Carvalho and Prado, 2000) and, intuitively, was defined in our system as the average number of electrodes activated in the next time bin, given a single electrode being active in the current time bin."

And what σ = 1 marks, from *Results*, verbatim:

> "According to theory, σ > 1 would represent a supercritical state in which an increasing number of electrodes would be activated at each step, eventually leading to an unstable runaway activation of the network (Fig. 7B). If σ < 1 (subcritical state), activity would decrease over successive steps. If σ = 1 (critical state), activity at one electrode would lead to activity in one other electrode on average, keeping the network at the edge of stability (Harris, 1989)."

That is a **branching-process criticality**: the boundary between an activity cascade that dies out and one that runs away. It is a statement about the expected size of a descendant population, and the reference for it is Harris's branching-processes monograph.

**The paper contains no claim that this is the same boundary as λ = 0 or h_μ = 0.** Searching the full text: the word "Lyapunov" occurs **zero** times. "Chaos" occurs once, inside the title of a cited reference (Van Vreeswijk & Sompolinsky 1996) and never in the authors' own prose. "Edge of chaos" does not occur; the phrase they use is "the edge of stability". "Entropy" occurs twice, both in *Materials and Methods*, and both times it is the Shannon entropy of a stimulus/response set inside a mutual-information calculation — "I(S; R) = H(R) − H(R/S), where H(R) was the entropy of the response set" — not a dynamical entropy rate of the network.

The authors also caution against reading σ as a property of the dynamics rather than of a statistical model fitted to them: "It should be noted that the branching parameter used to characterize the critical state is a statistical measure and does not say anything about the specific biological processes that could produce a particular value of σ." And they warn against the naive reading of σ = 1 as one-neuron-activates-one-neuron: "Because the branching parameter reflects a statistical average, it gives only the expected number of descendants after many branching events… In fact, the most common outcome in the critical state will be that no other neurons are activated."

So the σ side of the correspondence rests on nothing in the source. **No primary source stating a σ ↔ λ_max or σ ↔ h_μ correspondence was reached** — the searches returned model-specific claims in the recurrent-network literature and secondary summaries, none of them opened, so row 8 is **Unresolved** rather than **Refuted**. What can be said definitively is that the paper Mosaic cites for σ makes no such claim, and that σ = 1 is defined by a *stability* threshold on a cascade, not by an *information-production* rate — the same distinction that §4 shows separates γ from h_μ.

## 6. What survives, and the narrowing that follows

Assembling the four:

| Quantity | Defined on | Relation to h_μ established by a source read here |
|---|---|---|
| h_μ | any measure-preserving system on any measurable space | it is h_μ |
| λ_max | compact manifold, C¹ map, invariant measure | h_μ ≤ ∫λ⁺, Ruelle Thm 2; equality only under Pesin's three extra hypotheses; **converse false** off the manifold (§3) |
| γ (Γ) | cellular automata with a rule table | "not the rate of production of local information" — the source denies the relation (§4) |
| σ | systems admitting an avalanche/ancestor–descendant decomposition | none; the source does not discuss entropy rate or exponents (§5) |

They are not four estimators of one quantity. They are four measurements of four things, related where at all by inequalities that are known to be strict, and in one direction by a counterexample. The ticket's alternative discharge — "narrowing the Order axis to a single named estimator" — is the one the evidence supports.

**The estimator to keep is h_μ**, for a reason that is about Mosaic's search space rather than about elegance. The Bound has to place a diamond, a thunderstorm, a cortex, a transformer and a cellular automaton on the same axis. h_μ is defined for all of them: it needs a measure-preserving transformation and a partition, and nothing else — no tangent bundle, no rule table, no resting state, no avalanche. λ_max needs a differentiable structure that three of those five do not have, and the discrete surrogate is a different object with a strict inequality between them ([Tisseur](https://arxiv.org/abs/math/0312136), §3). γ needs a rule table, which is the objection [Mitchell/Hraber/Crutchfield](https://melaniemitchell.me/PapersContent/rev-edge.pdf) already made to λ and which the 2026-08-01 survey already accepted against Langton's λ; it is odd to refuse λ on that ground and then admit γ, which is measured on the same objects. σ needs an ancestor–descendant decomposition and a quiescent background, which a diamond does not have.

This is not a loss. The Order entry already drafted for `CONTEXT.md` is *already* h_μ and only h_μ — `1 − h_μ / log₂|A|`. What this document removes is the surrounding prose that treats readings of λ_max, γ and σ as substitutable evidence about that number. The concrete casualty is the cortex placement: a σ of 1.04 is not a measurement of h_μ, and the sentence deriving "Order strictly interior" from "σ ≈ 1" via "the discrete analogue of a zero Lyapunov exponent" has no source behind either step. Cortex may well be in-region; nothing read here places it there.

**One relation is worth keeping as a one-way falsifier.** Where a system *is* a C¹ map of a compact manifold, Ruelle's inequality gives h_μ > 0 ⟹ λ_max > 0 with no further hypotheses. So a measured λ_max = 0 refutes a claim of positive entropy rate for such a system. That is a usable check in one direction and never a substitute for measuring h_μ.

---

## What this does not establish

### Sources not reached

**Packard (1988)**, *Adaptation toward the edge of chaos*, in *Dynamic Patterns in Complex Systems*, 293–301 — the origin of the spreading rate γ. No accessible copy of the chapter was located; it is a 1988 book chapter with no repository deposit. γ is therefore known here only through Mitchell/Hraber/Crutchfield's description of it, which is the same second-hand position [#87](https://github.com/NGL321/mosaic/issues/87) already occupied and which §4's verdict does not depend on, because the denial being verified is *theirs*, not Packard's. **Shereshevsky (1991)**, the original CA Lyapunov-exponent definition and the inequality h_μ(F) ≤ h_μ(σ)(λ⁺+λ⁻), was read only through Tisseur's restatement in the introduction of a paper that extends it; the counterexample in §3 is Tisseur's own and was read directly, so the verdict does not rest on the restatement, but the inequality's exact hypotheses in the original are unverified. **Beggs & Plenz's live publisher page** returned an HTTP 403 bot challenge on every attempt; the text quoted in §5 is from an Internet Archive capture of the publisher's own PDF, `jneurosci.org/content/jneuro/23/35/11167.full.pdf`, which is the article as typeset and paginated (11167–11177) but is a capture rather than a live retrieval. **Ledrappier–Strelcyn and Ledrappier–Young**, which extend the entropy formula from Pesin's volume-equivalent measures to SRB measures, were not attempted; §1's finding is only that Pesin (1977) does not cover SRB, not that nobody does.

### Open gaps

**Where the σ ↔ λ claim actually comes from is untraced.** Row 8 is Unresolved, not Refuted, and the honest form of that is: somebody may have proved a correspondence in a specific model class — the recurrent-network and random-Boolean-network literatures both look likely — and this document did not open any of it. Until someone does, "σ = 1 is the discrete analogue of λ = 0" should be treated as an unsourced intuition. **Whether a CA counterexample runs the other way is unknown.** Tisseur gives λ > 0 with h_μ = 0; whether h_μ > 0 with all CA exponents zero is possible was not established, and it would matter, because it decides whether the CA inequality is at least a one-way falsifier the way Ruelle's is. **How Pesin's negative-exponent biconditional becomes a positive-exponent one** is asserted in §1 and not proved. **What h_μ costs to estimate on the systems Mosaic searches** is untouched here and is the substance of [#99](https://github.com/NGL321/mosaic/issues/99); narrowing the axis to one estimator makes that ticket more urgent, not less, because there is now no fallback quantity to read instead. **Whether the Bound needs the exponent at all** — if h_μ is the axis, λ_max may have no role beyond the one-way falsifier of §6, and that is a simplification nobody has proposed yet.

### Load-bearing ifs

**If Pesin's (1.7) biconditional does not transfer from negative to positive exponents**, then §1's reading is too generous and even the smooth-case biconditional is weaker than stated — this would strengthen the verdict, not weaken it, but it is the step in §1 most likely to be wrong. **If Tisseur's Example 6.1 is arithmetically wrong, or if his λ is not the quantity Mosaic would compute for a CA**, §3's counterexample evaporates and row 6 falls back to Unresolved; his λ is Shereshevsky's maximum-speed-of-perturbation definition, and a different reasonable CA exponent might behave differently. This is the single claim on which the headline verdict rests, and it is the cheapest thing for a later reader to attack. **If γ as Packard actually defined it in 1988 differs from what Mitchell/Hraber/Crutchfield describe**, §4 verifies a quotation about the wrong object; the disclaimer is theirs and stands, but its target might not be Packard's γ. **If the Beggs & Plenz text used here differs from the published article**, §5's negative findings — zero occurrences of "Lyapunov" — are findings about a capture rather than about the paper. **If a source does state the σ ↔ λ correspondence with a proof**, row 8 flips from Unresolved to Established and §6's narrowing loses one of its four legs, though not the CA counterexample that carries it.

---

## Verification Debt

Two items, both filed, both open.

- **[#123](https://github.com/NGL321/mosaic/issues/123)** — the σ ↔ λ correspondence has **untraced
  provenance**. §5 shows Beggs & Plenz do not claim it — zero occurrences of "Lyapunov", and "chaos"
  only inside a reference title — but cannot show nobody does; the recurrent-network and
  random-Boolean-network literatures were not searched to exhaustion. Recorded as Unresolved rather
  than Refuted, because the other three legs *were* refuted on evidence and the difference is worth
  keeping.
- **[#124](https://github.com/NGL321/mosaic/issues/124)** — **cortex's placement inside the region is
  underived.** `2026-08-01-informational-capacity-and-order.md` §5 reaches it from σ ≈ 1 via "the
  discrete analogue of a zero Lyapunov exponent", in two unsourced steps, and §3 here shows the second
  fails off a manifold: Tisseur's Coven automaton has λ⁻ = 2 with `h_μ = 0`. *Proposals* §2 drafts
  wording that withdraws the placement pending an `h_μ` estimate.

**The narrowing raises [#99](https://github.com/NGL321/mosaic/issues/99)'s urgency rather than easing
it.** Order is now `h_μ` and only `h_μ`, so there is no fallback quantity left to read instead of the
one nobody has yet estimated on any system Mosaic intends to search.

## Proposals

### 1. Narrow the Order axis to one estimator, in the pending `CONTEXT.md` entry

The **Order** entry drafted in `docs/research/2026-08-01-informational-capacity-and-order.md` §Proposals-1 has not yet landed in `CONTEXT.md`. Its definition line is already correct and should not change. Proposed replacement for its `_Departs_` paragraph in full:

```markdown
_Departs_: **Not** Langton's λ, which parameterises a cellular automaton's rule table.
Mitchell, Crutchfield & Hraber (1993) object that "behaviors in state space cannot be
adequately parameterized by any function of the equations of motion, such as λ"; Mosaic takes
that objection and measures the dynamics instead — which also gives the axis an argument for
systems that have no rule table, including every system the Bound's own examples name.
**Order is h_μ and only h_μ.** The maximal Lyapunov exponent λ_max, the difference-pattern
spreading rate Γ and the branching parameter σ are *not* alternative estimators of it and may
not be substituted for it. Pesin's identity equates entropy with the integrated positive
exponents only for a C² diffeomorphism of a compact Riemannian manifold preserving a measure
equivalent to the volume; Ruelle's inequality holds far more generally but only in the
direction h_μ > 0 ⟹ λ_max > 0, and Ruelle poses equality-in-general as an open question.
Off the manifold the converse is false outright: Tisseur (2000) exhibits a cellular automaton
with λ⁻ = 2 and h_μ = 0 under the uniform measure. Mitchell, Crutchfield & Hraber say of Γ
that it is "analogous to, but not the same as, the Lyapunov exponent" and that it measures
"the average propagation speed of information through space-time, though not the rate of
production of local information". Beggs & Plenz's σ = 1 marks the critical point of a
branching process — "the edge of stability" — and their paper makes no claim about exponents,
chaos, or entropy rate. Where a candidate system happens to be a C¹ map of a compact
manifold, λ_max = 0 may be used as a one-way falsifier of a claim that h_μ > 0; nowhere else,
and never as a reading of Order.
```

The badge for the added material is `⟦T3 · #98⟧`, drafted here and Noah's to apply.

### 2. Withdraw the cortex placement, or re-derive it

`docs/research/2026-08-01-informational-capacity-and-order.md` §5 currently reads, of Beggs & Plenz: *"A branching parameter of one is the neutral point of a branching process: activity neither dies out nor explodes, which is the discrete analogue of a zero Lyapunov exponent, which is Order strictly interior. Cortex is inside."* Neither step is sourced — §5 above shows the paper never mentions Lyapunov exponents, and §3 shows the exponent-to-entropy-rate step fails in discrete systems anyway. Proposed replacement for that clause:

> A branching parameter of one is the neutral point of a branching process: activity neither dies out nor explodes, which Beggs & Plenz call "the edge of stability". Whether that is the same boundary as an intermediate entropy rate is **not** established — their paper makes no claim about exponents or entropy rate, and the exponent-to-entropy-rate bridge fails for discrete-state systems (`docs/research/2026-08-02-pesin-and-the-order-axis.md` §3, §5). Cortex is a plausible candidate and is **not** placed.

### 3. Nothing to change in the Bound's own text

The Edge of Chaos Bound as settled does not name any of the four estimators, so nothing in it is falsified by this document. No amendment is proposed to `CHARTER.md`.

---

## Appendix: primary sources, all retrieved 2026-08-02

1. Ya. B. Pesin (1977), *Characteristic Lyapunov exponents and smooth ergodic theory*, **Russian Math. Surveys 32**:4, 55–114; from *Uspekhi Mat. Nauk* 32:4, 55–112. Read in full, English full text, 60 pages: [mathnet.ru/eng/rm3219](https://www.mathnet.ru/eng/rm3219) (DOI [10.1070/RM1977v032n04ABEH001639](https://doi.org/10.1070/RM1977v032n04ABEH001639)). §1.1 for the standing hypotheses, §1.6 for the C²/C^{1+ε} remark and the positive-entropy ⟺ (1.7) equivalence, Theorem 5.1 on p. 81 for the identity.
2. David Ruelle (1978), *An inequality for the entropy of differentiable maps*, **Bol. Soc. Bras. Mat. 9**, 83–87. Read in full, 5 pages, from the author's copy: [ihes.fr/~ruelle/PUBLICATIONS/\[51\].pdf](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B51%5D.pdf) (DOI [10.1007/BF02584795](https://doi.org/10.1007/BF02584795)). Theorem 2 for the inequality and its hypotheses; §3 *Remark* for the "Question" on equality in general.
3. Melanie Mitchell, Peter T. Hraber & James P. Crutchfield (1993), *Revisiting the Edge of Chaos: Evolving Cellular Automata to Perform Computations*, **Complex Systems 7**:89–130; SFI Working Paper 93-03-014. Read in full, 39 pages: [melaniemitchell.me/PapersContent/rev-edge.pdf](https://melaniemitchell.me/PapersContent/rev-edge.pdf); deposit record at [arXiv:adap-org/9303003](https://arxiv.org/abs/adap-org/9303003). §3 for the γ paragraph and Figure 2.
4. John M. Beggs & Dietmar Plenz (2003), *Neuronal Avalanches in Neocortical Circuits*, **J. Neurosci. 23**(35):11167–11177 (DOI [10.1523/JNEUROSCI.23-35-11167.2003](https://doi.org/10.1523/JNEUROSCI.23-35-11167.2003)). Read in full, 11 pages, from an Internet Archive capture of the publisher's PDF because the live host returns 403: [web.archive.org/web/2020/jneurosci.org/content/jneuro/23/35/11167.full.pdf](https://web.archive.org/web/2020/https://www.jneurosci.org/content/jneuro/23/35/11167.full.pdf). *Materials and Methods* Eq. (1) for σ; *Results* p. 11173 for the sub/super/critical reading; *Discussion*, "Features of the critical state", for the statistical-measure caveat.
5. Pierre Tisseur (2000), *Cellular automata and Lyapunov exponents*, **Nonlinearity 13**, 1547–1560. Read in full, 21 pages, from the author's arXiv deposit: [arXiv:math/0312136](https://arxiv.org/abs/math/0312136). §1 for Shereshevsky's inequality and its relation to "the Pesin one… in the differentiable case"; §6.1 for the Coven CA with λ⁻_μ = 2 and h_μ(F) = 0; Remark 6 for the general statement.
