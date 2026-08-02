---
ticket: 87
map: 1
date: 2026-08-01
kind: survey
tier: T3
session: unrecorded
sources: 13
debt: [98, 99, 100]
supersedes: null
---

# Informational Capacity and Order are excess entropy and normalised entropy rate — and that still does not fire the Bound's escape hatch

**Provenance.** Machine-produced, unverified. Five sources were read in full from a primary document: Langton (1990), from a page scan of *Physica D* **42**:12–37; Mitchell, Crutchfield & Hraber (1993), from the arXiv PDF; Crutchfield & Feldman (2001), from the arXiv PDF; Crutchfield & Young (1989), from the APS full text of *Phys. Rev. Lett.* **63**:105; and Beggs & Plenz (2003) and Priesemann et al. (2014), from open full texts. Six were reached at abstract or publisher-record depth only and are marked as such at every claim that rests on them. **Kauffman was not reached at all** — named in the ticket, refused by every route tried, and filed as [#100](https://github.com/NGL321/mosaic/issues/100). Every placement of the diamond, the thunderstorm and the cortex below is *analytic on an idealised model* or *read off someone else's measurement*; nothing here was computed on a system. That gap is [#99](https://github.com/NGL321/mosaic/issues/99), and it is the largest thing wrong with this document. None of these readings has been checked by Noah unaided.

---

## 0. Verdict

> **The axes are Crutchfield & Feldman's entropy rate and excess entropy — Informational Capacity is already in `CONTEXT.md` as the unnamed denominator of `Extraction`, Order is genuinely new — and operationalising them makes region *membership* decidable while leaving "searched without yield" as unfireable as it was.**

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | Langton's λ as the **Order** axis | **Refuted** — parameterises a rule table, not a dynamics; undefined for a diamond | §1 |
| 2 | Mitchell, Hraber & Crutchfield's pushback, carried in-line in the Bound | **Established** — it stands, and it *selects* the surviving pair rather than blocking it | §1 |
| 3 | A measurable pair of axes exists | **Supported** — entropy rate \(h_\mu\) and excess entropy \(\mathbf{E}\) | §2 |
| 4 | **Informational Capacity** is expressible in existing Mosaic vocabulary | **Supported** — it is the ceiling in `Extraction`'s ratio, already presupposed and unnamed | §3 |
| 5 | **Order** is expressible in existing Mosaic vocabulary | **Refuted** — neither `Extraction` nor `Closure` reaches it; it is new machinery | §3 |
| 6 | The diamond falls outside the region | **Supported** — Order = 1, \(\mathbf{E}=\log_2 p\); excluded on both axes | §4 |
| 7 | The thunderstorm falls outside the region | **Supported** — Order → 0, \(\mathbf{E}\to 0\); excluded on both axes | §4 |
| 8 | The Bound's gloss *"a diamond: enormous capacity"* | **Refuted** — a crystal's capacity is near zero on this axis; the gloss reads the other one | §4 |
| 9 | An uncontroversially cognitive system falls inside | **Contested** — cortex is inside on Order, unmeasured on Capacity, and the criticality evidence is itself disputed | §5 |
| 10 | Tononi's Φ as either axis | **Refuted** — exponential in node count, ~10–12 nodes in practice | §6 |
| 11 | Statistical complexity \(C_\mu\) as the Capacity axis | **Loose** — sharper than \(\mathbf{E}\) and bounds it, but needs ε-machine reconstruction | §6 |
| 12 | Both axes are measurable on real candidate systems today | **Open** — no estimator chosen, no symbolisation policy, nothing measured | §7 |
| 13 | Region **membership** becomes decidable | **Supported** — a candidate can now be refused, which it could not be before | §8 |
| 14 | *"The region was searched without yield"* becomes fireable from the axes | **Refuted** — the axes give a membership predicate, not an exhaustion predicate | §8 |

---

## 1. λ is the wrong shape, and the Bound's own objection says why

Langton's parameter is defined on the rule table and nowhere else. From the [scan of *Physica D* **42**:12–37, §2.1](https://shinyverse.org/al4ai/papers/Langton.EdgeOfChaos.pdf), verbatim:

> "The λ parameter is defined as follows. We pick an arbitrary state s ∈ Σ, and call it the quiescent state s_q. Let there be n transitions to this special quiescent state in a transition function Δ. Let the remaining K^S − n transitions in Δ be filled by picking randomly and uniformly over the other K − 1 states"

giving λ = (K^S − n)/K^S, with λ = 0 the most homogeneous table and λ = 1 − 1/K the most heterogeneous. Langton is candid in §2.4 that "λ is not necessarily the best parameter," and his own claim is about *average* behaviour over an ensemble of rules sampled at fixed λ, not about any particular rule.

Two things follow immediately for Mosaic, and neither depends on the empirical dispute.

**λ has no argument for most of the search space.** A diamond has no rule table. Neither does a thunderstorm, a cortex, or a transformer. λ is a coordinate on the space of cellular-automaton transition functions; the Bound quantifies over physical systems. There is no total function from "system" to λ, so λ cannot be the Order axis of a Bound that must place a crystal.

**And the Bound's in-line objection is stronger than a replication failure.** The Bound's text carries Mitchell, Hraber & Crutchfield's (1993) pushback deliberately. [Their abstract](https://arxiv.org/abs/adap-org/9303003) reports the negative replication:

> "Our experiment produced very different results, and we suggest that the interpretation of the original results is not correct."

But the load-bearing objection is in the companion re-examination, and it is structural rather than experimental. From [*Dynamics, Computation, and the "Edge of Chaos": A Re-Examination*](https://arxiv.org/pdf/adap-org/9306003) §2, verbatim (de-hyphenated):

> "One assumption is that in the global view of CA space, CA rule tables themselves are the appropriate loci of dynamical behavior. This is in stark contrast with the state space and the attractor-basin portrait approach of dynamical systems theory. The latter approach acknowledges the fact that behaviors in state space cannot be adequately parameterized by any function of the equations of motion, such as λ."

They add that the correlation between λ and behaviour "is quite good for very low and very high λ values" but that "for intermediate λ values in finite-state CA, there is a large degree of variation in behavior" — the variance is worst exactly in the region the Bound cares about. And in their conclusion they note that both the Game of Life and Langton's own universal-computation construction sit at λ ≈ λ_c while these constructions "do not establish any necessary correlation between λ_c and the ability for complex, or even universal, computation."

**This does not undercut the Bound; it selects its instrument.** The objection's positive content is a recommendation: measure the *dynamics*, in state space, not the equations of motion. Mosaic's second Bound — dynamical-systems modelability — has already bought that apparatus. What the pushback kills is λ, and the same authors' other work supplies the replacement. That is why §2 is not a workaround.

One further detail from the same paper is worth carrying: Packard located λ_c using "the difference-pattern spreading rate Γ", which the authors describe as "analogous to, but not the same as, the Lyapunov exponent for continuous-state dynamical systems." So a dynamical order parameter was already doing the real work under λ, and λ was a proxy for it. Also: Γ's "variance, like that of the statistics used by Langton, is high."

## 2. The pair that survives: entropy rate and excess entropy

The measure-theoretic version of the ordered/chaotic axis, and of the quantity that peaks between the extremes, is fully worked out in [Crutchfield & Feldman, *Regularities Unseen, Randomness Observed*](https://arxiv.org/pdf/cond-mat/0102181) (SFI 01-02-012; *Chaos* **13**:25). Both quantities are defined on the block entropy \(H(L)\) of length-\(L\) observations, their Eq. (11).

**Order axis — the source entropy rate**, their Eq. (13), verbatim:

> "The source entropy rate hμ is the rate of increase with respect to L of the total Shannon entropy in the large L limit: hμ ≡ lim_{L→∞} H(L)/L"

with the ceiling supplied by their Eq. (12), \(H(L) \le L\log_2|A|\). They then define, at Eq. (46), a **total predictability** \(G = \log_2|A| - h_\mu\) — used verbatim in their worked example: "the total predictability G = log₂|A| − hμ = 0 bits for the fair coin and 0.1187 bits for the biased coin." Normalising that by its own ceiling gives a quantity on \([0,1]\), which is exactly the shape [#15](https://github.com/NGL321/mosaic/issues/15) fixed for `Extraction` and `Closure`. That normalised predictability is **Order**.

**Capacity axis — the excess entropy**, their Eq. (48), with three equivalent readings they prove as propositions:

- Prop. 7, Eq. (51): \(\mathbf{E} = \lim_{L\to\infty}[H(L) - h_\mu L]\) — "The excess entropy is the subextensive part of H(L)".
- Prop. 8, Eq. (53): \(\mathbf{E}\) is "the mutual information between the left and right (past and future) semi-infinite halves of the chain".
- Prop. 6, Eq. (50): \(\mathbf{E}\) is the source's intrinsic redundancy, \(\sum_L r(L)\).

And, decisively for §3, Crutchfield & Feldman name the synonym themselves in the same section: "References [5,6] refer to the excess entropy as *predictive information*" — references 5 and 6 being [Bialek, Nemenman & Tishby](https://arxiv.org/abs/physics/0007070), whose abstract defines "*predictive information* I_pred(T) as the mutual information between the past and the future of a time series" (*Neural Computation* **13**:2409–2463).

**Why two axes and not one.** \(\mathbf{E}\) alone is already a "complexity" that is small at both extremes — which is the standard reason it is used. But small-at-both-ends is precisely why it cannot stand alone in a Bound whose text distinguishes *over-ordered* from *under-ordered*: a single low reading does not say which side you fell off. \(h_\mu\) says which side. The pair is a plane, and it is the complexity–entropy plane the same authors have used since 1989.

That 1989 paper states the whole two-axis picture in its opening paragraph. From [Crutchfield & Young, *Inferring Statistical Complexity*, *Phys. Rev. Lett.* **63**:105 (1989)](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.63.105/fulltext), verbatim:

> "Prior to the discovery of chaos, physical processes were broadly described in terms of two extreme models of behavior: periodic and random. Both are simple, but in distinct senses… Information-theoretic descriptions of this spectrum, (say) using the dynamical entropies, measure the raw diversity of temporal patterns: Periodic behavior has low information content; random, high content. What this misses, however, is the statistical simplicity of random behavior."

and, of their statistical complexity \(C_\mu\):

> "It vanishes for trivially periodic and for purely random data sets. A reconstructed ε-machine reflects a balanced utilization of deterministic and random information processing."

That is the Bound's diamond and the Bound's thunderstorm, stated as a physics result thirty-seven years before the Bound was written.

## 3. Against Mosaic's own quantities: one axis is already here, one is not

[#15](https://github.com/NGL321/mosaic/issues/15) settled that `Extraction` and `Closure` are **ratios against ceilings**, and `CONTEXT.md` defines `Extraction` as "achieved predictive information as a fraction of the ceiling set by the observed process itself."

**That ceiling is the excess entropy.** The predictive information available in an observed process — the most any engine could extract, given what it observes — is the mutual information between that process's past and its future, which is \(\mathbf{E}\) by Crutchfield & Feldman's Prop. 8, and is Bialek, Nemenman & Tishby's \(I_\mathrm{pred}\) under a second name. So:

\[ \texttt{Extraction} \;=\; \frac{I_\mathrm{pred}^{\text{achieved}}}{\mathbf{E}} \]

**Informational Capacity is the denominator Mosaic has been writing since [#2](https://github.com/NGL321/mosaic/issues/2) without naming.** This is the strongest single result here, and it is a reuse rather than an invention: the Bound's capacity axis and the vocabulary's central ratio turn out to be the same quantity used twice — once as a coordinate on the search space, once as a normaliser.

Two consequences fall straight out, and both are load-bearing.

**The region is where `Extraction` is well-conditioned.** \(\mathbf{E} = 0\) makes `Extraction` the ratio \(0/0\). A perfect crystal has no defined `Extraction`; neither does a fair coin. As \(\mathbf{E}\) falls toward zero the ratio's denominator vanishes and the quantity Mosaic measures engines by stops meaning anything. The Edge of Chaos Bound, read this way, is not an extra commitment bolted onto the vocabulary — it is *the region in which Mosaic's own primary quantity is defined*. That is a much better reason to hold it than an intuition about diamonds.

**Informational Capacity breaks the ratio convention, and should say so.** \(\mathbf{E}\) is a raw quantity in bits with no environment-independent ceiling — Crutchfield & Feldman are explicit that for "infinitary" processes the sum in Eq. (48) does not converge at all. `Extraction` and `Closure` are ratios; Informational Capacity cannot be, because it *is* a ceiling. Nothing is wrong with that, but the `CONTEXT.md` comment asserting that the ratio property is load-bearing and "should not be traded away" now has a sibling term that is not a ratio, and the entry must not read as though it were.

**Order is not in the vocabulary.** `Closure` asks how much of the environment's influence on a schema's observations those observations account for; `Extraction` asks how much of the available structure an engine captures. Both are about an engine or schema's relation to structure. \(h_\mu\) is a property of the candidate system's dynamics *before any engine has been identified in it* — it is what makes the Bound a search restriction rather than a measurement on something already admitted. There is no expressing it in existing terms; it is new, and it is the only new machinery this document proposes.

## 4. The test data, actually run

The Bound's two exclusions are worked below on idealised models. This is not measurement, and §7 says so at length.

**The diamond.** Model: a perfect crystal at equilibrium — a spatially periodic configuration, temporally at a fixed point. [Crutchfield & Feldman's](https://arxiv.org/pdf/cond-mat/0102181) periodic-process example (§VI B) gives both coordinates in closed form. Verbatim: "As for all period processes, the entropy rate hμ for the period-16 process is zero," and "The excess entropy E for the period-16 process is log₂16 = 4 bits; the sequence's past carries 4 bits of phase information about the future."

So a period-\(p\) source sits at **Order = 1** (maximum) and **Informational Capacity = \(\log_2 p\)** — four bits for a period-16 process; a few tens of bits for any crystal one cares to name. Excluded, at the boundary, on **both** axes.

**This refutes the Bound's own gloss.** The Bound [as settled in #6](https://github.com/NGL321/mosaic/issues/6) says the diamond has "enormous capacity, far too much order." On this axis a diamond's capacity is *negligible*, and the exclusion is over-determined rather than a trade-off. What is enormous about a diamond is the number of configurations its ~10²³ atoms could in principle be in — a ceiling on \(H\), not the mutual information between its past and its future. The gloss reads Informational Capacity as state-space size. Under that reading the axis does no work at all: the thunderstorm's state space is enormous too, so *both* exclusions would fall to Order alone and the Bound would be one-dimensional. The realised reading is the one that makes the pair non-degenerate, and the Bound's parenthetical has to change. Proposed wording is in *Proposals*.

**The thunderstorm.** Model: a maximum-entropy source over its observable alphabet — the idealisation of a turbulent, sensitively-dependent flow whose symbol sequence is near-incompressible. Crutchfield & Feldman's IID example, verbatim: "The fair coin has an hμ of 1 bit per symbol… for both processes the excess entropy E and the transient information T are zero… Each coin flip does not depend on past flips, and so there is no mutual information between the past and the future. Thus, E = 0."

**Order → 0**, **Informational Capacity → 0**. Excluded, at the opposite corner, again on both axes.

**What the test data does and does not prove.** Both cases land at *corners*, and both are excluded by either axis alone. So the diamond and the thunderstorm do not discriminate between candidate pairs — almost any monotone order parameter passes this test, including λ where it is defined. The test data is weaker evidence for the specific pair than it looks. What it does establish is the thing the Bound needs: the pair does not exclude anything it must admit, and it excludes the two named cases decisively. It is a non-exclusion test, not an identification test.

**The region over-admits, and that is correct.** A logistic map at the period-doubling accumulation point has intermediate Order and, per Crutchfield & Young, "infinite graph complexity" — it is squarely inside. No one says it thinks. This is not a defect: a Bound restricts where Mosaic *looks*, and asserts nothing about what it will *find*. Over-admission costs search budget; over-exclusion would cost the programme its object. The asymmetry is the right one. It does, however, make §8's problem worse.

## 5. Something uncontroversially cognitive, inside

Two independent lines put cortex and trained-scale networks in the interior. Neither is clean.

**Cortex, on the Order axis.** [Beggs & Plenz, *J. Neurosci.* **23**:11167–11177 (2003)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6741045/) report, verbatim: "As predicted by theory for a critical branching process, the propagation obeys a power law with an exponent of −3/2 for event sizes, with a branching parameter close to the critical value of one" — with "the power law exponent α was observed to be −1.50 ± 0.008 for electrode number" and "σ = 1.04 ± 0.19". A branching parameter of one is the neutral point of a branching process: activity neither dies out nor explodes, which is the discrete analogue of a zero Lyapunov exponent, which is Order strictly interior. Cortex is inside.

**And the evidence is disputed, on two fronts.** [Priesemann et al., *Front. Syst. Neurosci.* **8**:108 (2014)](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2014.00108/full) analysed *in vivo* spiking and concluded, verbatim, that "neural activity does not reflect a SOC state but a slightly sub-critical regime without a separation of time scales," with "one spike on average triggers a little less than one spike in the next step." Separately, [Touboul & Destexhe, *Phys. Rev. E* **95**:012413 (2017)](https://arxiv.org/abs/1503.08033) show that power-law statistics "naturally emerge from networks in self-sustained irregular regimes away from criticality" — so the avalanche exponent is not sufficient evidence of criticality at all.

Read carefully, both *help* the Bound rather than hurting it. A Bound needs a **region**, not a critical line; "slightly subcritical" is inside a band and outside a line. And Touboul & Destexhe's objection is against inferring criticality from a power law, which is an argument for measuring \(h_\mu\) directly rather than reading it off avalanche statistics. But they mean the reading is worth less than it looks, and that is why row 9 is **Contested** rather than **Supported**.

**The computational window, on the same axis.** [Schoenholz, Gilmer, Ganguli & Sohl-Dickstein, *Deep Information Propagation*](https://arxiv.org/abs/1611.01232) state, verbatim: "in networks at the edge of chaos, one of these depth scales diverges. Thus arbitrarily deep networks may be trained only sufficiently close to criticality," and that "the ordered and chaotic phases correspond to regions of vanishing and exploding gradient respectively." [Poole et al.](https://arxiv.org/abs/1606.05340) find the matching expressivity statement: "an order-to-chaos expressivity phase transition, with networks in the chaotic phase computing nonlinear functions whose global curvature grows exponentially with depth."

This is the strongest form of the Bound available anywhere: for deep networks, being in the interior is *necessary for trainability at depth*, not merely correlated with capability. Its limit is exact and must be stated — both results are mean-field theory of **randomly initialised** networks. Nobody has measured where a trained network sits, and the claim does not transfer to one without argument.

**Cortex's Capacity coordinate is not measured here at all.** The Order coordinate has published numbers; \(\mathbf{E}\) for cortical spiking does not appear in anything reached for this document. Row 9 is Contested for that reason as much as for the criticality dispute.

## 6. What was rejected, and why

**Tononi's Φ — Refuted, on computability.** Φ is a candidate for neither axis on content (it measures integration, not order), but it is worth killing explicitly because it is the obvious thing to reach for. [Oizumi, Albantakis & Tononi (2014)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003588) define integrated information via minimum-information partitions over the system's mechanisms. The authors' own reference implementation settles the cost: [Mayner et al., PyPhi (2018)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006343) state verbatim that "the algorithm is exponential time in the number of nodes, O(n5^3n)" and that this "limits the size of systems that can be practically analyzed to ~10–12 nodes" — with a seven-node system taking "~2.75 h". A Bound whose membership predicate cannot be evaluated on twelve nodes cannot bound a search over minds. Refuted, plainly, on the ticket's own criterion that computability matters more than elegance.

**Statistical complexity \(C_\mu\) — Loose.** \(C_\mu\) is sharper than \(\mathbf{E}\): it is the entropy of the ε-machine's causal states, and Crutchfield & Young's "It vanishes for trivially periodic and for purely random data sets" is stated of \(C_\mu\), not of \(\mathbf{E}\). It also bounds it. But obtaining it requires ε-machine reconstruction — building the subtree-equivalence classes their paper describes — which is practical for low-dimensional symbolic sources and not for a cortex. \(\mathbf{E}\) is estimable from block entropies without reconstructing a machine, so \(\mathbf{E}\) is the axis and \(C_\mu\) is a refinement to reach for when reconstruction is feasible.

**Lempel–Ziv complexity — not a rival, an estimator.** LZ compressibility is a consistent estimator of the entropy rate, so it is a practical route to the Order axis on a symbol stream, not a competing definition. The primary source (Lempel & Ziv 1976) was not reached; this is asserted, not verified, and is part of [#99](https://github.com/NGL321/mosaic/issues/99).

**Langton's λ — Refuted**, per §1.

**Kauffman — Unreached**, and the one genuinely regrettable gap. The random-Boolean-network critical condition is the closest thing in the prior art to a *closed-form* membership test on discrete-state systems, which would sidestep §7's estimation problem entirely for a useful class. Filed as [#100](https://github.com/NGL321/mosaic/issues/100).

## 7. Where this is uncomputable in practice, stated plainly

Both axes are limits over block length. Crutchfield & Feldman's own headline finding, from [their abstract](https://arxiv.org/abs/cond-mat/0102181), is about exactly this: "One consequence of ignoring these structural properties is that the missed regularities are converted to apparent randomness. We demonstrate that this problem arises particularly for small data sets; e.g., in settings where one has access only to short measurement sequences."

Four specific problems, none solved here:

1. **Estimator bias.** Block-entropy estimators overestimate \(h_\mu\) at finite \(L\) — that overestimate is literally what \(\mathbf{E}\) sums (their Prop. 6). A short record therefore reports a system as more chaotic and less capacious than it is, pushing candidates toward the thunderstorm corner. The bias has the sign that causes false exclusions.
2. **Symbolisation is a free choice.** Both quantities are defined on a symbol sequence. Crutchfield & Young are explicit that their ε-machines are named for "their dependence on the measuring instrument," and work from a specified generating partition. Mosaic has no partition policy, and the answer moves with the partition.
3. **Convergence is not guaranteed.** For infinitary processes \(\mathbf{E}\) diverges. A divergent capacity is not obviously a disqualification, but the region's upper edge is undefined and no candidate has forced the question.
4. **Nothing has been measured.** Diamond, thunderstorm and logistic map are analytic. Cortex is someone else's branching parameter, not an entropy rate. No system Mosaic intends to search has had either coordinate computed.

The honest summary: the axes are computable *in principle* for any system that emits a symbolisable time series, which is a strictly larger and more useful class than λ's, and computable *in practice* today for exactly nothing in Mosaic's search space. That is [#99](https://github.com/NGL321/mosaic/issues/99).

## 8. The escape hatch: half of it moves

The Bound's stratum-default hatch, from the [#6](https://github.com/NGL321/mosaic/issues/6) resolution, is *"the perspective stops paying — the region is searched without yield, or the apparatus stops producing tractable problems."* The ticket asks whether operationalising the axes makes the first clause fireable. It does not, and the reason is worth stating precisely, because it is not the reason the ticket anticipated.

**What does become available: a membership predicate.** Before this, "is system X in the region?" had no answer of any kind, so the Bound could not refuse a candidate and could not be cited in a decision. With \((h_\mu, \mathbf{E})\) it can — subject to §7. That is the half of the Bound that actually does work: a Bound's job is bounding a search, and refusing a candidate is what bounding means. Row 13.

**What does not: an exhaustion predicate.** "Searched without yield" requires a notion of the region having been *covered*. Two obstacles, and neither is an estimation problem that §7 could dissolve:

- The region is a subset of \(\mathbb{R}^2\) and is uncountable. There is no enumeration to complete.
- More seriously, **the axes are a projection, not a parameterisation**. The search space is systems; \((h_\mu,\mathbf{E})\) is a two-number summary of one. Two systems with identical coordinates are not interchangeable candidates — a Boolean network and a cortical slice can agree on both numbers and share nothing else. Covering the plane is not covering the region. This is the *same* objection Mitchell, Crutchfield & Hraber made to λ, one level up: a coordinate on a space is not the space, and it would be inconsistent to accept the objection in §1 and ignore it here.

So the hatch remains unfireable, and the ticket's framing — that operationalising the axes discharges it — turns out to be wrong. The commitment that can never be discharged is not caused by the axes being undefined; it is caused by *"searched"* being a predicate over an uncountable space of systems with no exhaustion criterion attached. Defining the axes was necessary and is not sufficient.

**What would fire it.** A coverage rule stated in units the programme already counts, rather than over the plane. [#9](https://github.com/NGL321/mosaic/issues/9) supplies them: an Inquiry is "the unit in which the programme buys evidence," it terminates in `Answered`, `Exhausted` or `Retired`, and the health index is already charted against releases. A fireable clause looks like: *the Bound is exhausted when N Inquiries whose systems were verified in-region reach `Exhausted`, or `Answered` with a negative result, at declared budget.* That is countable, it fires on a schedule the programme can actually meet, and it needs no new machinery. It is a change to the **Bound's own text**, not to the axes — which is why it appears in *Proposals* alongside them.

Note that §4's over-admission makes this worse, not better: a region that correctly admits the logistic map is a region in which a great many fruitless Inquiries can be run without ever amounting to evidence of exhaustion. The budget rule is what stops that from being an infinite bill.

---

## What this does not establish

### Sources not reached

**Kauffman, in every form** — the 1969 *J. Theor. Biol.* paper (ScienceDirect returned HTTP 403), *The Origins of Order* (1993, no accessible scan located), and Derrida & Pomeau (1986) on the annealed approximation. He is named on the Bound's `_After_` line and in the ticket, and this survey did not read a word of him; [#100](https://github.com/NGL321/mosaic/issues/100). **Packard (1988)**, the experiment whose refutation the Bound carries, was read only through Mitchell/Crutchfield/Hraber's description of it — so the pushback is verified and the thing pushed back against is not. **Bertschinger & Natschläger (2004)**, *Neural Computation* **16**:1413–1436, on the critical line in recurrent networks: MIT Press returned 403 and no repository copy was found; the abstract was seen only in search-result summaries, which are not a primary source, so nothing in §5 rests on it. **Boedecker et al. (2012)**, *Theory in Biosciences* **131**:205–213 — Springer redirected to an authentication endpoint; this matters because their reported result is that information storage and transfer peak *near but not exactly at* the transition, which is evidence about the region's width that this document therefore lacks. **Palmer, Marre, Berry & Bialek (2015)**, PNAS — 403; this is the paper most likely to supply a measured Informational Capacity for a biological system, and its absence is why row 9 is Contested. **Pesin (1977)** and **Ruelle (1978)**, for the entropy-rate/Lyapunov identity ([#98](https://github.com/NGL321/mosaic/issues/98)). **Lempel & Ziv (1976)**, IEEE, not attempted past the paywall. **Lorenz (1963)** — AMS returned 403; the thunderstorm's positive entropy rate is therefore modelled, not cited.

### Open gaps

**The region's boundaries are unnamed.** This document says the region is the interior of the complexity–entropy plane and does not say where the interior starts. Order must exclude 0 and 1, but a diamond is not the only over-ordered thing and no threshold is proposed. A Bound with a shape but no numbers is still not a decision procedure, and picking the numbers honestly probably requires §7 to be discharged first — the thresholds should come from where measurement can actually distinguish, not from taste.

**Whether \(\mathbf{E}\) should be measured on the system or on what an engine observes.** `Extraction`'s ceiling is the excess entropy of the *observed* process; the Bound needs the excess entropy of the *candidate system's own* dynamics. Same functional, different argument, and they are not equal — an engine can observe a low-capacity channel into a high-capacity world. This document has used both readings and has not said which the axis is.

**No third exclusion case.** §4 shows the two named cases are separable by either axis alone, so they cannot distinguish this proposal from a weaker one. A case that is *intermediate* on one axis and excluded on the other is what would actually test the pair, and the Bound does not supply one. Constructing it is the highest-value next piece of work on the Bound itself.

**Whether the four Order estimators are one axis.** \(h_\mu\), \(\lambda_{\max}\), the spreading rate \(\Gamma\) and the branching parameter \(\sigma\) are treated here as reading the same thing; Mitchell/Crutchfield/Hraber say outright that \(\Gamma\) is "not the same as" the Lyapunov exponent. [#98](https://github.com/NGL321/mosaic/issues/98).

**Whether trained networks are critical.** §5's ML evidence is mean-field theory of random initialisation. Whether a trained transformer sits in the region is unmeasured, and it is the single system Mosaic's computational window cares most about.

### Load-bearing ifs

**If the excess entropy is not `Extraction`'s ceiling**, §3's headline reuse collapses and Informational Capacity becomes new machinery rather than a naming of something already present. The chain is: `CONTEXT.md` says the ceiling is "the predictive structure available in what an engine observes"; the mutual information between a process's past and future is that quantity; Crutchfield & Feldman's Prop. 8 and the Bialek/Nemenman/Tishby synonym make that \(\mathbf{E}\). If `Extraction`'s ceiling was meant as something else — a per-symbol rate, or a bound conditioned on the engine's own resources — the identification fails and row 4 flips.

**If the diamond's "enormous capacity" gloss is meant to be kept**, the axis has to be state-space size, and then §4's argument shows the Bound collapses to one dimension. Row 8 and the proposed rewording stand or fall together; one of the two must go.

**If entropy-rate estimation on a real candidate turns out to be infeasible rather than merely undone**, row 13 flips from Supported to Refuted and the membership predicate is decidable only on toy systems — which would leave the Bound roughly where λ left it, with a better pedigree.

**If "searched without yield" is meant as coverage of the *plane* rather than of the space of systems**, §8's second obstacle disappears and the hatch is closer to fireable than argued here. The whole of row 14 rests on reading "the region" as a region of systems, which is how the Bound's own diamond-and-thunderstorm examples read it.

---

## Verification Debt

Three items, all newly filed. None was dischargeable within this session; each names what would discharge it.

1. **[#98](https://github.com/NGL321/mosaic/issues/98) — Pesin's identity and the equivalence of the Order axis's estimators are unread.** \(h_\mu\), \(\lambda_{\max}\), \(\Gamma\) and \(\sigma\) are treated as one axis on standard recall. Pesin (1977) and Ruelle's inequality were not reached, and Mitchell/Crutchfield/Hraber explicitly deny one of the four equivalences. Discharged by reading the originals, or by narrowing the axis to one named estimator.
2. **[#99](https://github.com/NGL321/mosaic/issues/99) — No validated estimator for entropy rate or excess entropy on any system Mosaic intends to search.** No estimator chosen, no finite-data characterisation, no symbolisation policy, nothing measured. This is the gap between §2's definitions and §7's practice, and it is what row 12 records. Discharged by a document selecting an estimator and reporting \((h_\mu, \mathbf{E})\) for one real system.
3. **[#100](https://github.com/NGL321/mosaic/issues/100) — Kauffman's ordered/chaotic regimes, cited on the Bound, were not reached in the original.** Also covers Derrida & Pomeau's critical condition, which is the prior art's best candidate for a closed-form membership test and is absent from this document only because it could not be read.

---

## Proposals

Four items. `CONTEXT.md` is human-only custody under [`PROTOCOL.md` §5](../../PROTOCOL.md); these are exact text for Noah to apply, reject or rewrite.

### 1. Two new entries in `CONTEXT.md`, *Research substance*, after `Closure`

```markdown
**Informational Capacity**:
How much of what a system will do is already written in what it has done — the mutual
information between its past and its future. Formally the **excess entropy**
E = lim_{L→∞} [H(L) − h_μ L], equivalently the mutual information between the two
semi-infinite halves of the observed sequence. It is the **ceiling in Extraction's ratio**:
the predictive structure there is to capture, against which an engine's achieved predictive
information is normalised. One of the two axes of the **Edge of Chaos** Bound; the other is
**Order**.
_Avoid_: Bandwidth, channel capacity, information content, complexity, memory, state-space size
_After_: Crutchfield & Feldman (2001), *Regularities Unseen, Randomness Observed*, for the
excess entropy and the equivalence of its subextensive, redundancy and mutual-information
readings; Bialek, Nemenman & Tishby (2001), whose **predictive information** is the same
quantity — Crutchfield & Feldman say so in as many words.
_Departs_: Named **Informational** Capacity because *capacity* alone collides with "general
cognitive capacity" in `Schema Dynamics`. Unlike **Extraction** and **Closure** it is **not a
ratio against a ceiling** — it *is* a ceiling, in bits, and for infinitary processes it does
not converge at all. And it is not the size of the state space: a crystal's astronomical
configuration count is a bound on H, not mutual information between past and future.

**Order**:
How far a system's dynamics fall short of producing information at the maximum rate its
alphabet allows: 1 − h_μ / log₂|A|, where h_μ = lim_{L→∞} H(L)/L is the source entropy rate.
Order 1 is a perfectly periodic process; Order 0 a fair coin. A property of the candidate
system's dynamics, prior to identifying any engine in it — which is what makes the **Edge of
Chaos** Bound a restriction on where Mosaic looks rather than a measurement on something
already admitted.
_Avoid_: Regularity, structure, stability, determinism, predictability, criticality
_After_: Crutchfield & Feldman (2001), Eq. (13) for h_μ and Eq. (46) for the total
predictability log₂|A| − h_μ that this normalises; Langton (1990) for the ordered/chaotic
framing and for the phrase *edge of chaos*.
_Departs_: **Not** Langton's λ, which parameterises a cellular automaton's rule table.
Mitchell, Crutchfield & Hraber (1993) object that "behaviors in state space cannot be
adequately parameterized by any function of the equations of motion, such as λ"; Mosaic takes
that objection and measures the dynamics instead — which also gives the axis an argument for
systems that have no rule table, including every system the Bound's own examples name.
```

Both entries are `⟦T3 · #87⟧` on their `_After_` and `_Departs_` lines, per [#5](https://github.com/NGL321/mosaic/issues/5)'s rule that the badge attaches there and not to the definition. The badge is drafted here; applying it is Noah's.

Note for the `Extraction` entry, which this makes answerable: its "ceiling set by the observed process itself" now has a name, and the sentence could say so — *"…as a fraction of its **Informational Capacity**, the ceiling set by the observed process itself."* Offered, not urged; it is a meaning-preserving edit to a settled entry.

### 2. A correction to the Edge of Chaos Bound's text

The Bound as settled reads *"excluding the over-ordered (a diamond: enormous capacity, far too much order, and no one says it thinks)."* On the axis proposed above a diamond's Informational Capacity is a few tens of bits, not enormous, and the exclusion is over-determined rather than a trade-off. Proposed replacement for that clause, for the charter ([#12](https://github.com/NGL321/mosaic/issues/12)):

> excluding the over-ordered (a diamond: an astronomical number of configurations, almost none of that structure carried from its past into its future, and no one says it thinks)

### 3. An exhaustion clause for the Bound's escape hatch

§8 argues the axes make membership decidable and leave *"searched without yield"* unfireable, because "the region" is a region of systems and has no enumeration. Proposed addition to the Bound's escape hatch, using [#9](https://github.com/NGL321/mosaic/issues/9)'s existing units:

> *Searched without yield* is discharged when **N Inquiries whose subject systems were verified in-region** terminate `Exhausted`, or `Answered` with a negative result, at declared budget — with N and the budget fixed in the charter before the first is opened. The clause is deliberately about Inquiries and not about coverage of the Informational Capacity × Order plane: two systems agreeing on both coordinates are not interchangeable candidates, so covering the plane is not covering the region.

N is Noah's to set and this document does not propose a value; the point is that the clause needs *a* countable unit, and Mosaic already has one.

### 4. A third exclusion case for the Bound

§4 shows the diamond and the thunderstorm are both corner cases, separable by either axis alone, so they cannot discriminate between candidate operationalisations. The Bound would be materially stronger for a case that is *intermediate on Order and excluded on Capacity*. No proposed case here — constructing one is work, not wording — but it is recommended as the next ticket on the Bound itself, and it is what would let a later reader tell this proposal from a weaker one.

---

## Appendix: primary sources

1. Chris G. Langton (1990), *Computation at the Edge of Chaos: Phase Transitions and Emergent Computation*, **Physica D 42**:12–37. Read in full from a page scan: [shinyverse.org/al4ai/papers/Langton.EdgeOfChaos.pdf](https://shinyverse.org/al4ai/papers/Langton.EdgeOfChaos.pdf). λ definition at §2.1, Eq. (1); the "not necessarily the best parameter" concession at §2.4.
2. Melanie Mitchell, Peter Hraber & James P. Crutchfield (1993), *Revisiting the Edge of Chaos: Evolving Cellular Automata to Perform Computations*, SFI Working Paper 93-03-014, **Complex Systems 7**:89–130. Abstract page read: [arXiv:adap-org/9303003](https://arxiv.org/abs/adap-org/9303003). Full text not opened; the structural objections are cited from entry 3 instead.
3. Melanie Mitchell, James P. Crutchfield & Peter T. Hraber (1993), *Dynamics, Computation, and the "Edge of Chaos": A Re-Examination*. Read in full: [arXiv:adap-org/9306003](https://arxiv.org/pdf/adap-org/9306003). §2 for the rule-table objection and the Γ/Lyapunov remark; §5 for the symmetry-breaking account of Packard's histogram.
4. James P. Crutchfield & Karl Young (1989), *Inferring Statistical Complexity*, **Phys. Rev. Lett. 63**:105–108. Read in full: [APS full text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.63.105/fulltext). Opening paragraph for the periodic/random two-extremes framing; "It vanishes for trivially periodic and for purely random data sets" for \(C_\mu\).
5. James P. Crutchfield & David P. Feldman (2001), *Regularities Unseen, Randomness Observed: Levels of Entropy Convergence*, SFI Working Paper 01-02-012; **Chaos 13**:25–54 (2003). Read in full: [arXiv:cond-mat/0102181](https://arxiv.org/abs/cond-mat/0102181). Eq. (11) H(L), Eq. (12) ceiling, Eq. (13) \(h_\mu\), Eq. (46) predictability, Eq. (48) and Props. 6–8 for \(\mathbf{E}\), §VI A and §VI B for the IID and periodic placements.
6. William Bialek, Ilya Nemenman & Naftali Tishby (2001), *Predictability, Complexity, and Learning*, **Neural Computation 13**:2409–2463. Abstract read: [arXiv:physics/0007070](https://arxiv.org/abs/physics/0007070). Cited only for the definition of predictive information as past–future mutual information.
7. John M. Beggs & Dietmar Plenz (2003), *Neuronal Avalanches in Neocortical Circuits*, **J. Neurosci. 23**(35):11167–11177. Full text read: [PMC6741045](https://pmc.ncbi.nlm.nih.gov/articles/PMC6741045/). Exponent −1.50 ± 0.008; branching parameter σ = 1.04 ± 0.19.
8. Viola Priesemann, Michael Wibral, Mario Valderrama, Robert Pröpper, Michel Le Van Quyen, Theo Geisel, Jochen Triesch, Danko Nikolić & Matthias H. J. Munk (2014), *Spike avalanches in vivo suggest a driven, slightly subcritical brain state*, **Front. Syst. Neurosci. 8**:108. Full text read: [doi:10.3389/fnsys.2014.00108](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2014.00108/full).
9. Jonathan Touboul & Alain Destexhe (2017), *Power-law statistics and universal scaling in the absence of criticality*, **Phys. Rev. E 95**:012413. Abstract read: [arXiv:1503.08033](https://arxiv.org/abs/1503.08033). Cited only for the claim that power laws are insufficient evidence of criticality.
10. Samuel S. Schoenholz, Justin Gilmer, Surya Ganguli & Jascha Sohl-Dickstein (2017), *Deep Information Propagation*, ICLR 2017. Abstract read: [arXiv:1611.01232](https://arxiv.org/abs/1611.01232).
11. Ben Poole, Subhaneil Lahiri, Maithra Raghu, Jascha Sohl-Dickstein & Surya Ganguli (2016), *Exponential expressivity in deep neural networks through transient chaos*, NeurIPS 2016. Abstract read: [arXiv:1606.05340](https://arxiv.org/abs/1606.05340).
12. Masafumi Oizumi, Larissa Albantakis & Giulio Tononi (2014), *From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0*, **PLoS Comput. Biol. 10**(5):e1003588. Publisher full text read: [doi:10.1371/journal.pcbi.1003588](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003588).
13. William G. P. Mayner, William Marshall, Larissa Albantakis, Graham Findlay, Robert Marchman & Giulio Tononi (2018), *PyPhi: A toolbox for integrated information theory*, **PLoS Comput. Biol. 14**(7):e1006343. Publisher full text read: [doi:10.1371/journal.pcbi.1006343](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006343). Source of the O(n5^3n) cost and the ~10–12 node practical limit.
