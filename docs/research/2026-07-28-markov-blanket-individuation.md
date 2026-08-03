---
ticket: 14
map: 1
date: 2026-07-28
revised: 2026-07-29
kind: question
tier: T3
session: unrecorded
sources: 28
debt: [139, 140, 141, 142, 143, 144, 145, 146, 147]
supersedes: null
---

# Can a Markov blanket carry individuation, or should causal states?

**Ticket:** [#14 — Can a Markov blanket carry individuation, or should causal states?](https://github.com/NGL321/mosaic/issues/14)
**Map:** [#1 — Founding charter for Mosaic](https://github.com/NGL321/mosaic/issues/1)
**Date:** 2026-07-28. **Revised 2026-07-29** against `main` at `e3ac60a`, after [#19](https://github.com/NGL321/mosaic/pull/19) (`PROTOCOL.md`), [#20](https://github.com/NGL321/mosaic/pull/20) (citation audit) and [#21](https://github.com/NGL321/mosaic/pull/21) (research substance) landed. Changes are listed in §0 and are additive — the recommendation did not move.
**Provenance Tier:** machine-produced, unverified. Every claim below is sourced to a primary document (paper, publisher record, or author-hosted PDF) and linked, and the load-bearing papers were read in full rather than by abstract; but none of the derivations have been checked by Noah unaided. Discharging this is Verification Debt, itemised in §9 and logged against the Curriculum.

---

## 0. What this document concluded

> **No. The Markov blanket cannot carry the individuation load, and neither can causal
> states on their own.** Individuation and qualification collapse into **one criterion
> applied at two levels** — the partition search of Krakauer et al. — which is a
> simplification of the `Inference Engine` definition rather than an addition to it.

| § | Sub-question | Verdict | One-line reason |
|---|---|---|---|
| §2 | Does instantaneous conditional independence give trajectory independence? | **Refuted** | Biehl, Pollock & Kanai (2021), Observation 1: an explicit Ornstein–Uhlenbeck counterexample proves the two are logically independent *in either direction*. |
| §3 | Does the free-energy side's own defence preserve the blanket as an individuating construct? | **Refuted** | Ramstead's reply states the formal ontology is *"not an a priori attempt to find or draw boundaries in nature"* but instrumentalist model-building. That is the rebuttal, not a critic's characterisation. |
| §4 | Do causal states individuate? | **Refuted** | Computational mechanics is *handed* a process: Shalizi & Crutchfield Def. 1 starts from a fixed alphabet, and Crutchfield & Feldman frame the apparatus as a measurement channel with the observable partition already chosen. |
| §5.1 | Do Markov blankets survive nesting? | **Loose** | Nesting is constructed, not proved. |
| §5.2 | Do causal states survive nesting? | **Supported** | Shalizi (2003), Lemma 2 (Patch Composition) *proves* that local causal states compose losslessly. |
| §6 | Is there a candidate neither thread named? | **Supported** | Krakauer, Bertschinger, Olbrich, Flack & Ay: an individual is *"a system partition that is a sufficient predictor of its own future"*, found by searching over candidate partitions. |
| §6.1 | Are `Closure` and the proposed individuation criterion one apparatus at two levels? | **Open** | The same formalism by three of the same authors already sits under `Closure`, adopted independently. Whether that is identity or resemblance is unsettled, and over-claiming it would do the most damage of anything here. |
| §7 | Can the entry keep the blanket as stated? | **Refuted** | Options 1, 2 and 4 each fail for a stated reason; option 3 — demote the blanket to intuition-and-citation — is what survives. |
| §7.7 | Has anyone related blankets and causal states formally? | **Open** | Searched for and not found. A well-posed, apparently unasked question squarely inside Mosaic's territory, and a candidate belt rung in its own right. |

**Inference Engine** currently reads: *a system delineated by a Markov blanket whose internal state carries predictive information about states beyond that blanket*. The blanket individuates; predictive information qualifies. This document asks whether the blanket can carry the individuation load.

**It cannot, and the recommendation is option 3: demote the blanket to intuition-and-citation, and put the formal weight on the computational-mechanics apparatus.** Three findings drive this, and the third is the one that matters most because it is a concession rather than an attack:

1. **The instantaneous and path formulations are logically independent, and this is proved.** [Biehl, Pollock & Kanai (2021), Observation 1](https://arxiv.org/abs/2001.06408) prove by explicit Ornstein–Uhlenbeck counterexample that sparse coupling of the flow and conditional independence in the ergodic density *neither implies the other, in either direction*. So the answer to Thread A's crux is: no, instantaneous conditional independence does not give you trajectory independence, and neither does trajectory-level sparse coupling give you the instantaneous version. [Friston et al. (2023)](https://arxiv.org/abs/2210.12761) do state the blanket over paths — "internal paths are conditionally independent of external paths, given blanket paths" — but they do not concede the earlier version was insufficient; they relocate the definition without remarking on it. Mosaic's criterion is about futures, so it needs the path version, and the path version is a different claim from the one Pearl is cited for.

2. **The FEP side's own defence concedes exactly the point Mosaic needs.** Answering [Bruineberg, Dołęga, Dewhurst & Baltieri (2022)](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/emperors-new-markov-blankets/715C589A73DDF861DCF8997271DE0B8C), [Ramstead's reply](https://arxiv.org/abs/2112.15528) states that the formal ontology "is **not an a priori attempt to find or draw boundaries in nature**. Rather, it is an attempt to construct scientific models of these boundaries, in an instrumentalist fashion." A construct whose defenders describe it instrumentally cannot be the thing that says where an engine stops. That is not a critic's characterisation; it is the rebuttal.

3. **Causal states do not individuate either — and admitting that is what makes the recommendation survivable.** Computational mechanics is handed a process. [Shalizi & Crutchfield (2001), Definition 1](https://arxiv.org/abs/cond-mat/9907176) starts from a countable alphabet A and a bi-infinite sequence over it; [Crutchfield & Feldman (2003)](https://arxiv.org/abs/cond-mat/0102181) frame the whole apparatus as a *measurement channel* with the observable partition already fixed. So the ε-machine machinery buys qualification and capacity, not individuation, and swapping the blanket for causal states straight across would smuggle the modeller's choice back in under a new name.

The resolution is that **individuation and qualification collapse into one criterion applied at two levels**. [Krakauer, Bertschinger, Olbrich, Flack & Ay](https://link.springer.com/article/10.1007/s12064-020-00313-7) already do this: they search over candidate system/environment partitions and keep the one that maximises propagated information from past to future, defining an individual as "a system partition that is a sufficient predictor of its own future." That is *Mosaic's existing qualifying criterion used as the individuation criterion*, which is a simplification of the definition rather than an addition to it. It buys the nesting property too — [Shalizi (2003), Lemma 2 (Patch Composition)](https://arxiv.org/abs/math/0305160) *proves* that local causal states compose losslessly, where blanket nesting is asserted by construction and not proved.

The honest cost: this still requires the modeller to declare an observable. It does not escape the map/territory problem; it makes the choice explicit and falsifiable instead of hiding it inside a word that sounds ontological. Full argument in §7. Sections 1–6 are the evidence. Proposed replacement text for `CONTEXT.md` is in §8 — **as a proposal, not an edit**, which under [`PROTOCOL.md`](https://github.com/NGL321/mosaic/blob/main/PROTOCOL.md) §5 is the only form an agent may deliver it in.

### 0.1 What the 2026-07-29 revision changed

Three merges landed between this document being written and being opened for review. None disturbed the recommendation; two improved its standing and one corrected it.

- **Strengthened — §6.1 is new, and is the most useful thing in the revision.** [#21](https://github.com/NGL321/mosaic/pull/21) added a **Closure** entry to `CONTEXT.md` whose `_After_` line credits informational closure to Bertschinger, Olbrich, Ay & Jost. That is the same formalism, by three of the same authors, that Krakauer et al. build the recommended individuation criterion on. Mosaic had therefore already adopted this apparatus at the *schema* level, independently and on its own reasons, before this document recommended its parent at the *engine* level. The recommendation is one apparatus at two levels of an existing nesting, not an import — which answers the "degenerating problemshift" objection with a fact rather than an argument. The tempting over-claim is flagged and refused in §6.1, and logged as debt item 6a.
- **Corrected — §1.1.** An earlier draft said the `_After_` line over-credits Pearl by attributing temporal granularity to him. The [#13/#20 citation audit](https://github.com/NGL321/mosaic/blob/main/docs/research/2026-07-28-verifying-cited-influences.md) reached Pearl's Definition (3.12), p. 97 in the scanned first edition and found the line **Supported** as written. The corrected version keeps the load-bearing point — Pearl's construct is atemporal, so Friston's temporal form is a substantive addition and not inherited authority — and drops the claim against the line. §1.1 now also quotes Pearl verbatim from the audit rather than leaning on a secondary reconstruction, and notes that Pearl's *minimal* shielding set is a **boundary**, not a blanket.
- **Retargeted — §8.** The proposed replacement text was written against the pre-#21 entry. That entry has since gained an **Extraction** cross-reference and the not-a-scalar clause that resolved [#15](https://github.com/NGL321/mosaic/issues/15). Both are now preserved verbatim in the proposal, which otherwise changes only the individuation half. Applying the old text would have reverted #15 silently. §8 also now records **Extraction** and **Closure** among the entries the recommendation touches: Extraction gains a formal ceiling it currently lacks — the excess entropy of the observed process.

---

## 1. What a Markov blanket is, and at what temporal granularity

### 1.1 Pearl's blanket has no time in it (established)

The terms *Markov blanket* and *Markov boundary* are Pearl's, from [*Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference* (Morgan Kaufmann, 1988)](https://dl.acm.org/doi/book/10.5555/534975). [#13/#20's citation audit](https://github.com/NGL321/mosaic/blob/main/docs/research/2026-07-28-verifying-cited-influences.md) reached the scanned first edition and gives the definition verbatim — Definition (3.12), p. 97, §3.3 *Markov networks*:

> "A **Markov blanket** BL_I(a) of an element a ∈ U is any subset S of elements for which I(a, S, U − S − a) and a ∉ S. (3.12) A set is called a **Markov boundary** of a, denoted B_I(a), if it is a minimal Markov blanket of a…"

`I(a, S, U − S − a)` is Pearl's conditional-independence relation. Two features of the primary text matter here. First, in Pearl a Markov blanket is *any* shielding set; the **minimal** one is the Markov **boundary**. Secondary reconstructions routinely collapse this — [Bruineberg et al.](https://philsci-archive.pitt.edu/19726/7/The%20Emperor's%20New%20Markov%20Blankets_updated.pdf) render the blanket as "the minimal set of nodes that renders a particular node conditionally independent of all other nodes in a Bayesian graph," which is Pearl's *boundary*. Nothing in this document turns on the distinction, but §8's replacement text avoids the word "blanket" for a minimal object for that reason.

Second, and this is the point that matters for Thread A: **Pearl's definition carries no time index whatsoever.** U is a set of elements; nothing indexes them. It is not instantaneous — it is atemporal. So "the blanket is stated at an instant" is not a fact about Pearl's construct; it is a fact about how the free-energy literature instantiated it.

**A correction to an earlier draft of this document, on the strength of the #13/#20 audit.** That draft said the current `CONTEXT.md` `_After_` line over-credits Pearl by attributing temporal granularity to him. That is wrong as stated: the line reads "Pearl (1988) for the blanket as conditional independence," which is exactly what Definition (3.12) supplies and no more, and the audit's verdict on it — **Supported**, no change needed to the attribution — stands. The real observation is narrower and belongs to the *reader*, not to the line: because the entry cites Pearl and Friston in one breath, it invites the inference that the temporal form of Friston's blanket is inherited from Pearl's authority. It is not. Friston's is a substantive additional commitment, and §2 shows it is not even a single commitment.

### 1.2 Friston's blanket, first at steady state (established)

[Friston (2013), "Life as we know it," *J. R. Soc. Interface* 10:20130475](https://royalsocietypublishing.org/doi/10.1098/rsif.2013.0475) and then at length in [Friston (2019), "A free energy principle for a particular physics," arXiv:1906.10184](https://arxiv.org/abs/1906.10184) instantiate the blanket in the *density* of a random dynamical system at non-equilibrium steady state. Friston's monograph states the move plainly: "we assume that for something to exist it must possess (internal or intrinsic) states that can be separated statistically from (external or extrinsic) states that do not constitute the thing. This separation implies the existence of a Markov blanket; namely, a set of states that render the internal and external states conditionally independent." The blanket is then partitioned into active and sensory states, and this is described as "the minimal set of conditional independencies — and implicit partition of states — that licenses talk about things (that possess states)."

[Biehl, Pollock & Kanai (2021)](https://arxiv.org/abs/2001.06408) formalise the two versions actually in circulation as:

- **Condition 1** — sparse coupling of the *flow*: the vector field factorises so external states influence only themselves and sensory states, internal states only themselves and active states.
- **Condition 2** — conditional independence in the *ergodic density*: `p*(ψ,s,a,λ) = p*(ψ|s,a) p*(λ|s,a) p*(s,a)`.

They note flatly that "we have two different formal expressions of what constitutes a Markov blanket in these publications, and their relationship has not previously been established."

### 1.3 Friston's blanket, later over paths (established)

[Friston, Da Costa, Sakthivadivel, Heins, Pavliotis, Ramstead & Parr (2023), "Path integrals, particular kinds, and strange things," *Physics of Life Reviews* 47:35–62](https://www.sciencedirect.com/science/article/pii/S1571064523001094) ([arXiv:2210.12761](https://arxiv.org/abs/2210.12761)) states the blanket over trajectories. From its narrative summary of the derivation:

> "A particle is constituted by internal and blanket states. The blanket states constitute the boundary between the states internal and external to the particle. Mathematically, this means that internal paths are conditionally independent of external paths, given blanket paths."

And in the body, deriving it from coupling structure rather than from a density:

> "The particular states are partitioned into sensory, active and internal states with particular flow dependencies; namely, external states can only influence themselves and sensory states, while internal states can only influence themselves and active states. From (4), these coupling constraints mean that external and internal paths are independent, when conditioned on blanket paths. […] This is because there are no flows that depend on both internal and external states (and fluctuations are independent)."

Note what this is and is not. It **is** the path version, and it is arrived at from Biehl's Condition 1 (sparse coupling of the flow), not from Condition 2. It is **not** a concession. The paper offers no passage acknowledging that the instantaneous/density formulation was insufficient, and no passage acknowledging that the two are inequivalent. The issue's phrasing — "Friston's later path-integral work appears to concede this" — is half right: the later work *supplies* the path version but does not *concede* anything about the earlier one. Where the paper does address why conditional independence is the starting point at all, the justification is epistemic rather than ontological: "the only thing we have at hand is a probabilistic description of the system […] and the only way to separate the states of something from its boundary states is in terms of probabilistic independencies."

---

## 2. Thread A: does instantaneous conditional independence give you trajectories?

**No, and this is proved rather than argued.**

The decisive result is [Biehl, Pollock & Kanai (2021), Observation 1](https://arxiv.org/abs/2001.06408). The two conditions it concerns are, in the paper's own statement, a claim about the **flow** and a claim about the **density** respectively:

> **Condition 1** — the vector field factorises as f(x) = (f_ψ(ψ,s,a), f_s(ψ,s,a), f_a(s,a,λ), f_λ(s,a,λ))ᵀ.
>
> **Condition 2** — the ergodic density factorises as p\*(ψ,s,a,λ) = p\*(ψ|s,a) p\*(λ|s,a) p\*(s,a).

Observation 1 then states, and the two displayed relations are reproduced here **exactly as the paper sets them** — as its Equations (11) and (12), both written with Condition 1 on the left and the arrow carrying the direction:

> "Neither one of Condition 1 (the vector field dependency structure) or Condition 2 (conditional independence in the ergodic distribution) implies the other:
>
> Condition 1 ⇏ Condition 2  (11)
>
> Condition 1 ⇍ Condition 2. (12)"

Read the arrows, not the operand order: **⇏** is "does not imply," so (11) says the flow condition does not give you the density condition; **⇍** is "is not implied by," so (12) says the density condition does not give you the flow condition. The paper keeps Condition 1 on the left in both lines rather than transposing to "Condition 2 ⇏ Condition 1", which is why the pair reads oddly when quoted inline. Both directions fail, and that is the whole content of the observation.

The proof is by explicit counterexample in their Appendix A, constructed within the class of Ornstein–Uhlenbeck processes — where the drift matrix M and the inverse covariance U are both constant, so Condition 1 reduces to vanishing blocks of M and Condition 2 to vanishing blocks of U, and the two can be independently arranged. Restricting to the best-behaved possible class is what makes the result strong: if the implication fails for linear Gaussian systems with constant diffusion and solenoidal matrices, it fails generally.

This settles the technical question Thread A poses, in a slightly different shape than the ticket anticipated. It is not merely that the instantaneous version is *weaker*; the two are **logically independent in both directions**. A system can have a perfectly good blanket in its steady-state density and no sparse coupling in its flow, and vice versa. So:

- A definition that says "delineated by a Markov blanket" and cites Pearl is ambiguous between two inequivalent conditions.
- Mosaic's criterion — *carries predictive information about states beyond that blanket* — is a claim about futures given a present, so it needs the trajectory-level object. The density-level blanket does not supply it.

[Aguilera, Millidge, Tschantz & Buckley (2022)](https://arxiv.org/abs/2105.11203) make the same gap visible graphically rather than algebraically. Their Figure 2 contrasts a directed acyclic graph, where the blanket is read straight off the structure, with a cyclic causal model where it is not: "nodes that meet the local Markov condition (grey nodes) do not guarantee the conditional independence required for a Markov blanket, as new couplings might emerge." Since any system with feedback — which is every system Mosaic cares about — is cyclic, this is the normal case, not a pathology.

**Established:** instantaneous and path blankets are inequivalent, by counterexample in the simplest possible system class.
**Established:** the FEP literature contains both, uses the same name for both, and did not establish their relationship until it was pointed out externally.
**Not established:** any claim that the later path-integral work retracts the earlier formulation.

---

## 3. Thread B: the Pearl/Friston distinction, the technical critiques, and the replies

### 3.1 Bruineberg, Dołęga, Dewhurst & Baltieri (2022) — what they actually argue

Target article: ["The Emperor's New Markov Blankets," *Behavioral and Brain Sciences* 45:e183](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/emperors-new-markov-blankets/715C589A73DDF861DCF8997271DE0B8C); the full pre-print text is at [PhilSci-Archive](https://philsci-archive.pitt.edu/19726/7/The%20Emperor's%20New%20Markov%20Blankets_updated.pdf). Their abstract states the distinction:

> "We propose to distinguish between instrumental Pearl blankets and realist Friston blankets. Pearl blankets are substantiated by the empirical literature but can do limited philosophical work. Friston blankets can do philosophical work, but require strong theoretical assumptions. Both are conflated in the current literature on the free-energy principle."

And the map/territory framing:

> "While Pearl blankets are unambiguously part of the map, Friston blankets are best understood as part of the territory. Since these are different formal constructs with different metaphysical implications, the scientific credibility of Pearl blankets should not automatically be extended to Friston blankets."

The passage that lands hardest on Mosaic, because Mosaic is doing exactly the thing described:

> "Simply put, where Friston blankets are located in a model depends (at least partially) on modeling choices, i.e., Friston blankets cannot simply be 'detected' in some objective way and then used to determine the boundary of a system. This can be easily seen by the fact that Markov blankets are defined only in relation to a set of conditional (in)dependencies, or the equivalent graphical models […] The choice of a particular graphical model is then usually enforced by Bayesian model selection, which is in turn dependent on the data used."

Their conclusion is a dilemma, stated in the introduction:

> "those wishing to use Markov blankets for these purposes are faced with a dilemma: either they stick to the original innocuous-but-metaphysically-uninteresting formulation; or they bolster it with novel metaphysical premises. However, in the latter case it is the additional premises and not the mathematical construct itself that carries out most of the theoretical work leading to novel conclusions, undermining any claim that these conclusions simply follow from the original Markov blanket formalism."

This is a philosophy paper and it is not making a mathematical claim, so it can be answered — but Mosaic inherits the dilemma exactly as stated. Using the blanket to *individuate* is the second horn.

### 3.2 The BBS peer commentary and the authors' reply

BBS target articles ship with open peer commentary. This one drew 35 commentaries, answered in [Bruineberg, Dołęga, Dewhurst & Baltieri, "The Emperor Is Naked: Replies to commentaries on the target article," *BBS* 45:e219](https://pubmed.ncbi.nlm.nih.gov/36172792/), organised around three questions: "Are Friston blankets just Pearl blankets? What ontological and metaphysical commitments are implied by the use of Friston blankets? What kind of explanatory work are Friston blankets capable of?"

Commentaries span the range, including [Bramley and colleagues, "Redressing the emperor in causal clothing"](https://www.research.ed.ac.uk/en/publications/redressing-the-emperor-in-causal-clothing-commentary-on-the-emper), ["Scientific realism about Friston blankets without literalism"](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/scientific-realism-about-friston-blankets-without-literalism/E9DCE9EEA26AF82CE4977311B4973561), ["Markov blankets do not demarcate the boundaries of the mind"](https://pubmed.ncbi.nlm.nih.gov/36172779/), ["The emperor has no blanket!"](https://pubmed.ncbi.nlm.nih.gov/36172752/), and ["Life, mind, agency: Why Markov blankets fail the test of evolution"](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/life-mind-agency-why-markov-blankets-fail-the-test-of-evolution/FDC150120C65F6AE5B8E1F2202C68D48). *I read the target article and the authors' reply abstract in full; the individual commentaries I reached as titles and publisher abstracts only, not full text.* That is a stated limit on this section.

### 3.3 The first-party rebuttal, and why it concedes the point

The FEP-side commentary is [Ramstead, "The empire strikes back: Some responses to Bruineberg and colleagues," *BBS* 45](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/empire-strikes-back-some-responses-to-bruineberg-and-colleagues/EAD6092F39E09AE0BABA34012E54CA08) ([full text, arXiv:2112.15528](https://arxiv.org/abs/2112.15528)), whose acknowledgements credit discussions with Da Costa, Friston, Heins, Kiefer, Sakthivadivel and Parr — so it is fair to read it as the group's position.

It makes two moves.

**Move one: Pearl blankets and Friston blankets are the same object in different categories.**

> "FBs and PBs just are MBs—in different mathematical contexts. […] The fundamental distinction is that PBs are the kind of MB that arises in the context of static statistical inference within a Bayes network, while FBs arise when considering the interdependencies between dynamics."

The analogy offered is the natural numbers reinterpreted in the reals: same objects, different properties. **This move does not survive contact with §2.** Biehl et al. proved that the two formal conditions in circulation are logically independent in both directions. That is not one object viewed in two categories; it is two conditions, either of which can hold without the other. The Peano analogy would require the two to be the same set of constraints under different ambient structure, and they are not.

**Move two: the FEP is instrumentalist anyway.** This is the move that matters for Mosaic, and it is a concession dressed as a defence:

> "The formal ontology that flows from the Bayesian mechanics is not an a priori attempt to find or draw boundaries in nature. Rather, it is an attempt to construct scientific models of these boundaries, in an instrumentalist fashion. The formal ontology only entails that we create empirically evaluable, formal models of organism boundaries."

And earlier:

> "there is nothing about the FEP that commits us to realism about scientific models. In fact, we have argued that precisely the opposite is the case."

If the framework's own defenders say the blanket does not draw boundaries in nature but models them instrumentally, then **the blanket cannot be what individuates a Mosaic engine.** Mosaic is not asking the blanket to be a convenient partition; it is asking it to say what a thing *is*. The defence and the requirement are incompatible. This is the single most decisive item in the whole document, and it comes from the defence rather than the attack, which is why it is hard to argue with.

### 3.4 Biehl, Pollock & Kanai (2021): what is broken and what survives

[Published in *Entropy* 23(3):293](https://www.mdpi.com/1099-4300/23/3/293); [arXiv:2001.06408](https://arxiv.org/abs/2001.06408). Abstract, verbatim in relevant part:

> "we reveal that various definitions of the 'Markov blanket' proposed in different works are not equivalent. We show that crucial steps in the free energy argument which involve rewriting the equations of motion of systems with Markov blankets, are not generally correct without additional (previously unstated) assumptions. We prove by counterexample that the original free energy lemma, when taken at face value, is wrong. We show further that this free energy lemma, when it does hold, implies equality of variational density and ergodic conditional density. The interpretation in terms of Bayesian inference hinges on this point, and we hence conclude that it is not sufficiently justified."

Itemised, with their own labels:

| Result | Status | What it kills |
|---|---|---|
| Observation 1 | Proved by counterexample (App. A) | Condition 1 ⇎ Condition 2. The blanket has two inequivalent definitions. |
| Observation 2 | Proved by counterexample (App. B) | The simplified flow equations (their Eqs. 19–22) do not follow even when *both* conditions hold. Getting them requires removing solenoidal terms "by fiat," i.e. assuming R_as = R_λs = 0. |
| Observation 3 | Proved | Further inconsistency when Condition 1 and Condition 3 are assumed jointly, as in later work. |
| Free Energy Lemma | Proved false at face value (App. C) | The existence of a variational density q(Ψ\|λ) with the required gradient properties is not implied. |
| Vanishing gradients ⇒ q = p* | Proved false (App. D) | Even where the gradients of the KL divergence vanish, the divergence itself "can be arbitrarily large." The Bayesian reading does not follow. |

**What survives, in their own words:** "Note that we only highlight some specific problems in the discussed publications. These problems do not rule out conclusively that the general ideas behind the free energy principle are worth pursuing." And: "the technical issues presented here do not affect the validity of approaches where an (expected) free energy minimizing agent is assumed" — i.e. active inference as a *modelling* method is untouched. This is a critique of the derivation of the FEP from the blanket, not of active inference as engineering.

**Relevance to Mosaic, stated precisely.** Mosaic's Inference Engine definition does *not* depend on the Free Energy Lemma — the `_Departs_` line already refuses the Friston qualification and substitutes a thermodynamic one. So most of Biehl et al. misses Mosaic. Observation 1 does not miss: it is the whole of Thread A.

### 3.5 Aguilera, Millidge, Tschantz & Buckley (2022): how restrictive is "having a blanket"?

[*Physics of Life Reviews* 40:24–50](https://ui.adsabs.harvard.edu/abs/2022PhLRv..40...24A/abstract); [arXiv:2105.11203](https://arxiv.org/abs/2105.11203). They analyse the simplest non-trivial class — weakly-coupled non-equilibrium *linear* stochastic systems, i.e. multivariate Ornstein–Uhlenbeck processes whose NESS is a zero-mean multivariate Gaussian obtained by solving a continuous Lyapunov equation. Their reasoning for choosing that class is worth recording: "if the assumptions and steps of the FEP do not hold in such simple systems, we consider it unlikely that they hold in more complex nonlinear systems where the dynamics are expected to be more deeply intertwined."

Three results:

1. **Blanket existence is a fine-tuning condition.** "we can conclude that Markov blankets will emerge only for particular combinations of parameters, as cycles in the system will in general introduce couplings preventing their existence." Their listed exceptions — weak couplings under circular loops, or two layers of blanket states — hold "because cycles generating conditional couplings between x, y are of order higher than 2," and "in general these cases will not display a Markov blanket for stronger couplings […] except for perfectly symmetric couplings."

2. **The solenoidal restriction is severe.** The FEP requires no solenoidal coupling between external and other states (their Assumption 1, `Q` block-diagonal). Since solenoidal flow is precisely what breaks detailed balance and drives a system out of equilibrium, and since non-equilibrium is "a fundamental aspect of living entities," this excludes the asymmetric organism–environment interactions and oscillatory biorhythms that motivated the theory. Their abstract: "Suitable systems require an absence of perception-action asymmetries that is highly unusual for living systems interacting with an environment."

3. **The most serious problem is not about blankets at all.** The step connecting system behaviour to variational inference "relies on an implicit equivalence between the dynamics of the average states of a system with the average of the dynamics of those states. This equivalence does not hold in general even for linear systems, since it requires an effective decoupling from the system's history of interactions." They spell out the consequence: substituting the true flow by an average flow at fixed blanket state "decouples the trajectory of y from its previous state, which in most dynamical systems will result in an impoverished description, not capturing its real, history-dependent, behaviour."

Point 3 is worth flagging for Mosaic even though it targets the FEP's inference reading rather than the blanket: it is a *history-dependence* objection, and Mosaic's engines are defined by what their internal state carries about futures given pasts. Any formalism that averages away trajectory dependence is the wrong tool for this programme regardless of the blanket question.

### 3.6 The FEP-side technical reply, and its honesty

[Heins & Da Costa, "Sparse coupling and Markov blankets," arXiv:2205.10190](https://arxiv.org/abs/2205.10190) — both authors are FEP-side, Heins a co-author on the 2023 path-integral paper. Their abstract:

> "The authors demonstrate that in general, Markov blankets are not guaranteed to follow from sparse coupling. The current commentary explains the relationship between sparse coupling and Markov blankets in the case of Gaussian steady-state densities. We precisely derive conditions under which causal coupling leads—or does not lead—to Markov blankets."

This is a good reply and should be reported as such. It **grants** Aguilera et al.'s central negative result rather than disputing it, then supplies a sufficient condition: a *locality* constraint on the state-dependence of the solenoidal flow, "whereby the coupling between any two pairs of states does not depend on other states besides the two that are interacting." They argue this may hold for spatially-localised short-range interactions, e.g. neighbouring particles in a collective.

Two things follow. The objection is answered *conditionally*, not dissolved — and the authors say so themselves in their closing line: "Future work should focus on verifying whether these sorts of constraints are satisfied in realistic models of sparsely coupled systems." As of this survey I found no such verification. And the condition that rescues blankets is *spatial locality of interaction*, which is a strange fit for Mosaic, whose engines are individuated by informational rather than spatial relations and whose Schema Dynamics are explicitly about coupling across a heterogeneous network.

### 3.7 Thread B summary

| Claim | Status |
|---|---|
| The FEP literature uses two inequivalent formal definitions of "Markov blanket" | **Established.** [Biehl et al., Observation 1](https://arxiv.org/abs/2001.06408) — proved by counterexample. |
| The original Free Energy Lemma is wrong at face value | **Established.** [Biehl et al., App. C](https://arxiv.org/abs/2001.06408). Does not bear on Mosaic, which does not use it. |
| Markov blankets fail to emerge generically from sparse coupling in cyclic systems | **Established, and conceded by the other side.** [Aguilera et al.](https://arxiv.org/abs/2105.11203); [Heins & Da Costa](https://arxiv.org/abs/2205.10190). |
| Sufficient conditions for blanket emergence exist | **Established but unverified in practice.** [Heins & Da Costa](https://arxiv.org/abs/2205.10190) supply a locality-of-solenoidal-coupling condition and explicitly leave its realism to future work. |
| Blanket placement depends on modelling choices rather than being detected | **Established, and conceded.** [Bruineberg et al.](https://philsci-archive.pitt.edu/19726/7/The%20Emperor's%20New%20Markov%20Blankets_updated.pdf) assert it; [Ramstead](https://arxiv.org/abs/2112.15528) concedes it in instrumentalist terms. |
| "Friston blankets are just Pearl blankets in another category" | **Contested, and I judge it fails.** [Ramstead](https://arxiv.org/abs/2112.15528) asserts it; [Biehl et al.'s Observation 1](https://arxiv.org/abs/2001.06408) contradicts it. |
| The whole FEP programme is thereby refuted | **No, and this document does not claim it.** Biehl et al. explicitly decline to conclude this. |

---

## 4. Thread C: what computational mechanics actually offers, and what it does not

### 4.1 The construction (established)

Origin: [Crutchfield & Young (1989), "Inferring Statistical Complexity," *Phys. Rev. Lett.* 63:105–108](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.63.105). Full formal development: [Shalizi & Crutchfield (2001), "Computational Mechanics: Pattern and Prediction, Structure and Simplicity," *J. Stat. Phys.* 104:817–879](https://link.springer.com/article/10.1023/A:1010388907793) ([arXiv:cond-mat/9907176](https://arxiv.org/abs/cond-mat/9907176)). Review: [Crutchfield (2012), "Between order and chaos," *Nature Physics* 8:17–24](https://www.nature.com/articles/nphys2190) ([PDF](https://csc.ucdavis.edu/~chaos/papers/Crutchfield.NaturePhysics2012.pdf)).

The **causal states** are the equivalence classes of pasts inducing the same distribution over futures. [Shalizi & Crutchfield, Definition 5](https://arxiv.org/abs/cond-mat/9907176):

> ε(s⃖) ≡ { s⃖′ | P(S⃗ = s⃗ | S⃖ = s⃖) = P(S⃗ = s⃗ | S⃖ = s⃖′), for all s⃗ ∈ S⃗, s⃖′ ∈ S⃖ }

The **ε-machine** is this state set plus the induced labelled transition structure (their Definitions 8 and 4; [Crutchfield 2012](https://www.nature.com/articles/nphys2190) gives the compact version). **Statistical complexity** is C_μ(R) ≡ H[R], the Shannon entropy of the state distribution — "the average amount of memory (in bits) that the process appears to retain about the past" ([Definition 4](https://arxiv.org/abs/cond-mat/9907176)).

### 4.2 The theorems, by number (established)

All from [Shalizi & Crutchfield (2001)](https://arxiv.org/abs/cond-mat/9907176). "Prescient rivals" are alternative partitions of pasts that predict as well as the causal states.

| # | Statement | Content |
|---|---|---|
| Lemma 1 | Old Country Lemma: H[S⃗^L\|R] ≥ H[S⃗^L\|S⃖] | No effective state beats the whole past. |
| Lemma 2 | Past and future are conditionally independent given the causal state | The causal state *is* a screening variable — the property a blanket is asked for, obtained rather than assumed. |
| Lemma 3 | Causal states are the largest strictly homogeneous subsets of histories w.r.t. futures of all lengths | Maximal coarse-graining consistent with prediction. |
| Lemma 5 | ε-machines are deterministic (unifilar) | Current state plus next symbol fixes next state. |
| Lemma 7 | Refinement Lemma | Any prescient rival is, up to measure zero, a refinement of the causal states. The engine of Theorems 2 and 3. |
| **Theorem 1** | **Causal states are maximally prescient**: H[S⃗^L\|R] ≥ H[S⃗^L\|S] for all R, all L | No rival predicts better. |
| **Corollary 1** | **Causal states are sufficient statistics** for prediction: I[S⃗^L; S] = I[S⃗^L; S⃖] | They lose nothing about the future. |
| **Theorem 2** | **Causal states are minimal**: C_μ(R̂) ≥ C_μ(S) for all prescient rivals | No equally-predictive rival is simpler. |
| **Theorem 3** | **Causal states are unique**: any prescient rival with C_μ(R̂) = C_μ(S) is related to S by an invertible function, a.e. | The minimal sufficient statistic is essentially unique. |
| **Theorem 4** | **ε-machines are minimally stochastic**: H[R̂′\|R̂] ≥ H[S′\|S] | Least residual uncertainty in state transitions. |
| **Theorem 5** | **The Bounds of Excess**: E ≤ C_μ, with equality iff H[S\|S⃗] = 0 | See §4.3. |
| Theorem 6 | Control Theorem: H[S] − h[S⃗\|R̂] ≤ C_μ | Bounds how much fixing the state buys you. |

Together Theorems 1–3 are the statement that the causal states are **the** minimal sufficient statistic for prediction, unique up to measure zero. This is a genuinely stronger foundation than anything the blanket literature offers: it is proved, the proofs are short and checkable, and there is no competing formulation of the same object in circulation.

### 4.3 The two quantities Mosaic wants, and the relation between them (established)

- **Excess entropy** E = I[S⃖ ; S⃗], the mutual information between the whole past and the whole future. Independently and near-simultaneously introduced as **predictive information** I_pred by [Bialek, Nemenman & Tishby (2001), "Predictability, Complexity, and Learning," *Neural Computation* 13:2409–2463](https://direct.mit.edu/neco/article/13/11/2409/6521) ([arXiv:physics/0007070](https://arxiv.org/abs/physics/0007070)), who prove it is the *subextensive* part of the entropy — S(T) ≈ S₀T + S₁(T), with I_pred(T) = S₁(T) — and is therefore always finite-or-subextensive, growing at most sublinearly. They classify processes by whether I_pred stays bounded, grows logarithmically (finite-parameter models, with the coefficient counting model dimension), or grows as a power law (nonparametric), and argue "the divergent part of I_pred(T) provides the unique measure for the complexity of dynamics underlying a time series."
- **Statistical complexity** C_μ = H[S], the memory the process must store to predict optimally. Entropy convergence and the E/C_μ/h_μ relationships are laid out in [Crutchfield & Feldman (2003), "Regularities unseen, randomness observed: Levels of entropy convergence," *Chaos* 13:25–54](https://pubs.aip.org/aip/cha/article/13/1/25/135236) ([arXiv:cond-mat/0102181](https://arxiv.org/abs/cond-mat/0102181)).

**Theorem 5** relates them: **E ≤ C_μ**, with equality if and only if H[S|S⃗] = 0, i.e. the future determines the current causal state. The interpretation is exactly what Mosaic needs: *E is what the past tells you about the future; C_μ is what the system must store to tell you it.* The gap C_μ − E is stored structure that is not visible as past-future correlation — memory that has to be maintained without appearing in the observable mutual information.

This is a **matched pair, and the match is a theorem, not an analogy.** Mosaic's qualifying criterion (predictive information) and any capacity proxy (statistical complexity) are not two independent measurements bolted together; they are two functionals of the same object with a proved inequality between them. That is a stronger position than the current definition occupies.

### 4.4 The counter-objection: do causal states individuate? (**No.**)

This is the question the recommendation must not hand-wave, and the honest answer is unfavourable.

Computational mechanics is **handed a process**. [Shalizi & Crutchfield, Definition 1](https://arxiv.org/abs/cond-mat/9907176):

> "We restrict ourselves to discrete-valued, discrete-time stationary stochastic processes. […] Let A be a countable set. Let Ω = A^Z be the set of bi-infinite sequences composed from A […] A process is a sequence of random variables S_i = T_i(S⃡), i ∈ Z."

The alphabet A is given. The time series is given. The equivalence relation ∼_ε then partitions *pasts of that series* — it does not partition the world into system and environment. Every optimality theorem in §4.2 is conditional on a fixed A.

[Crutchfield & Feldman (2003)](https://arxiv.org/abs/cond-mat/0102181) are explicit that this is a **measurement channel**, with the observer's instrument upstream of everything:

> "We assume that there is a process (source) that produces a data stream (message) — an infinite string of symbols drawn from some finite alphabet. The task for the observer (receiver) is to estimate the probability distribution of sequences […] Since the observer does not have direct access to the source's internal, hidden states, we picture instead that the observer can estimate to arbitrary accuracy the probability of measurement sequences."

And the warning that the representation itself is a choice: "one should consider the histogram to be a particular class of representation for the source's internal structure — one that may or may not correctly capture that structure."

[Crutchfield (2012)](https://www.nature.com/articles/nphys2190) says the same in the review's framing — the problem is "to understand a system's randomness and organization, **given only the available, indirect measurements that an instrument provides**," and "the system to which we refer is simply the entity we seek to understand by way of making observations." The entity is presupposed; the theory characterises the process it generates.

**So the obvious counter-objection lands.** Swapping "Markov blanket" for "causal states" in the individuation slot would replace a modeller's choice of partition with a modeller's choice of observable, and would be a lateral move dressed up as a fix.

There is one important qualification in computational mechanics' favour, and it should be stated because it is real. [Crutchfield (2012)](https://www.nature.com/articles/nphys2190) argues that C_μ has "an essential kind of representational independence": "The causal equivalence relation, in effect, extracts the representation from a process's behaviour. […] Independence from selecting a representation achieves the intuitive goal of using UTMs in algorithmic information theory — the choice that, in the end, was the latter's undoing." That is a genuine advantage *over Kolmogorov complexity*, whose value depends on an arbitrary universal machine. It is **not** independence from the choice of observable. Two distinct claims; only the first is established.

### 4.5 Thread C summary

| Claim | Status |
|---|---|
| Causal states are the minimal sufficient statistic for prediction, unique a.e. | **Established.** Theorems 1–3, [Shalizi & Crutchfield (2001)](https://arxiv.org/abs/cond-mat/9907176). |
| Past and future are conditionally independent given the causal state | **Established.** Lemma 2, same. Screening is *derived*, not stipulated. |
| E ≤ C_μ, equality iff H[S\|S⃗] = 0 | **Established.** Theorem 5, same. |
| Predictive information is the subextensive part of the entropy and is the unique complexity measure for a time series | **Established** for the first clause; the uniqueness claim is an argument from axioms in [Bialek et al. (2001)](https://arxiv.org/abs/physics/0007070), not a theorem in the Theorem-5 sense. |
| Causal states individuate a system from its environment | **No. Refuted by the framework's own setup.** [Def. 1](https://arxiv.org/abs/cond-mat/9907176); [measurement channel](https://arxiv.org/abs/cond-mat/0102181); [Crutchfield 2012](https://www.nature.com/articles/nphys2190). |
| C_μ is representation-independent | **Established in the narrow sense** (independent of a chosen computational representation), **false in the broad sense** (independent of the chosen observable). |
| There is a literature explicitly relating Markov blankets to causal states | **No such literature found.** This is an open gap; see §7.4. |

---

## 5. Thread D: does either candidate survive nesting?

Mosaic's constraint: an engine holds many **Schemas**, each carrying its own metric space, so "an engine holding several schemas is itself a small network." Whatever individuates an engine must compose.

### 5.1 Blankets: nesting is constructed, not proved

Friston's nesting claim is prominent and long-standing. [Friston (2019)](https://arxiv.org/abs/1906.10184) frames it via the *Siphonaptera* rhyme — "big fleas have little fleas" — and states the recursion directly: "the states of things are constituted by their Markov blanket, while the Markov blanket comprises the states of smaller things with Markov blankets within them – and so on ad infinitum. This appeal to blankets 'all the way' down offers a recursive definition of everything."

The mechanism is spelled out in [Friston, Fagerholm, Zarghami, Parr, Hipólito, Magrou & Razi, "Parcels and particles: Markov blankets in the brain," *Network Neuroscience*](https://direct.mit.edu/netn/article/5/1/211/97539) ([arXiv:2007.09704](https://arxiv.org/abs/2007.09704)):

> "if we start with some states at any level, we can partition these states into a set of particles – based upon how the states are coupled to each other. We can then take the principal eigenstates of each particle's blanket states to form new states at the scale above – and start again. This recursive application of a grouping or partition operator (G) – followed by a dimension reduction (R) – leads to the renormalisation group based upon two operators, R and G."

The dimension reduction eliminates internal states and the fast-decaying eigenmodes, "leaving us with the slow unstable eigenstates picked out by the dimension reduction, which we can now see as an adiabatic approximation." The application to neural architecture at multiple scales is in [Hipólito, Ramstead, Convertino, Bhat, Friston & Parr, "Markov blankets in the brain," *Neuroscience & Biobehavioral Reviews*](https://www.sciencedirect.com/science/article/pii/S0149763421000579) ([arXiv:2006.02741](https://arxiv.org/abs/2006.02741)), which partitions "into single neurons, brain regions, and brain-wide networks."

**Assessment.** This is a *procedure* that produces a hierarchy, not a theorem that blankets compose. It assumes an eigen-decomposition-based coarse-graining, a spectral gap for the adiabatic separation, and — critically — that a blanket exists at each level. Given §3.5, that last assumption is precisely what is not generically true: if blankets emerge "only for particular combinations of parameters" at one scale, the RG scheme has no guarantee that the coarse-grained states at the scale above admit one. The nesting claim inherits every weakness of Thread B and adds a spectral assumption of its own. It is a construction that will always return *something*; whether what it returns is a blanket at every level is unestablished.

### 5.2 Causal states: composition is proved

Computational mechanics has a localised version. [Shalizi (2003), "Optimal Nonlinear Prediction of Random Fields on Networks," *DMTCS*](https://arxiv.org/abs/math/0305160) shows optimal nonlinear prediction on a network-indexed random field "is formally identical to the problem of finding minimal local sufficient statistics," derives their properties, and — the point for Thread D — "show[s] that they can be composed into global predictors." The result is stated as:

> **"Lemma 2 (Patch Composition)** The causal state of a patch at one time is uniquely determined by the composition of all the local causal states within the patch at that time."

The proof shows the composition of local causal states within the patch is a sufficient statistic of the patch and then applies minimality. This is exactly the property the blanket literature asserts and does not prove: **local structure composes into global structure with no loss.**

The spatiotemporal machinery is developed in [Rupe & Crutchfield, "Local causal states and discrete coherent structures," *Chaos* 28:075312 (2018)](https://arxiv.org/abs/1801.00515), which defines the local causal states via past and future *lightcones* —

> L⁻(r,t) ≡ { X^{r′}_{t′} : t′ ≤ t and ‖r′ − r‖ ≤ c(t′ − t) }, L⁺(r,t) ≡ { X^{r′}_{t′} : t′ > t and ‖r′ − r‖ ≤ c(t − t′) }

with c the finite speed of information propagation — and equates two past lightcones when they induce the same distribution over future lightcones. Their notable result for Mosaic is that **coherent structures fall out as spatially-localised deviations from the symmetries of the local causal state field**, in an approach that is "behavior-driven in the sense that it does not rely on directly analyzing spatiotemporal equations of motion, rather it considers only the spatiotemporal fields a system generates." They validate it against the older domain–particle–interaction decomposition on elementary cellular automata. The precursor result — using optimal predictors to detect self-organisation — is [Shalizi, Shalizi & Haslinger (2004), "Quantifying Self-Organization with Optimal Predictors," *Phys. Rev. Lett.* 93:118701](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.93.118701).

Two caveats, stated plainly. First, the lightcone construction assumes a lattice or network with a finite propagation speed c, and Rupe & Crutchfield concede the choice is "ultimately a weak-causality argument" — it is a modelling assumption, not a derivation. Second, coherent-structure detection localises structure *within a given field*; it still does not tell you where the field came from. Composition is solved; individuation is not.

The channel-composition apparatus that would extend this to input–output coupling between engines is begun in [Barnett & Crutchfield, "Computational Mechanics of Input-Output Processes: Structured transformations and the ε-transducer," *J. Stat. Phys.*](https://arxiv.org/abs/1412.2690), explicitly announced as "the first in a series on the structural information theory of memoryful channels, channel composition, and allied conditional information measures." **The composition instalments of that series I did not locate, and I flag that as an unverified assumption rather than a supporting citation.**

### 5.3 Thread D summary

| Question | Blankets | Causal states |
|---|---|---|
| Do they nest? | Asserted via an RG scheme ([Friston 2019](https://arxiv.org/abs/1906.10184); [Parcels and particles](https://arxiv.org/abs/2007.09704)) that presupposes a blanket at each scale plus a spectral gap. | **Proved.** [Shalizi (2003), Lemma 2](https://arxiv.org/abs/math/0305160). |
| Is there a spatially local version? | Blanket-of-blankets, per the above. | Yes: local causal states over lightcones ([Rupe & Crutchfield 2018](https://arxiv.org/abs/1801.00515)). |
| Does the local version detect structure without being told where it is? | n/a | **Yes, within a given field** — coherent structures as symmetry deviations. |
| Do they compose across coupled systems? | Not established. | Begun via ε-transducers ([Barnett & Crutchfield](https://arxiv.org/abs/1412.2690)); **composition results not verified here.** |

Thread D favours causal states clearly, and it is the only thread where the advantage is a proved theorem against an assumed construction.

---

## 6. The candidate nobody named: information-theoretic individuality

Neither of the two candidates in the ticket individuates. A third does, and it does so using the criterion Mosaic has already chosen.

[Krakauer, Bertschinger, Olbrich, Flack & Ay, "The information theory of individuality," *Theory in Biosciences* 139:209–223 (2020)](https://link.springer.com/article/10.1007/s12064-020-00313-7) ([arXiv:1412.2447](https://arxiv.org/abs/1412.2447)). Their abstract:

> "Our purpose is to extract through an algorithmic decomposition system-environment boundaries supporting individuality. We infer or detect evolved individuals rather than assume that they exist. Given a set of consistent measurements over time, we discover a coarse-grained or quantized description on a system, inducing partitions (which can be nested). Legitimate individual partitions will propagate information from the past into the future, whereas spurious aggregations will not. Individuals are therefore defined in terms of ongoing, bounded information processing units rather than lists of static features."

The procedure is a search over partitions:

> "The basic idea is to systematically increase the number of variables that we assign to the target system and determine whether this procedure leads to an increase in the quantity representing autonomy. If the expansion of the boundary of the system does not lead to an increase in autonomy, then we have incorporated an environmental variable needlessly. In this way individuals represent mechanism for aggregating dynamical processes in such a way as to maximize their knowledge of the future."

And the criterion, in their own words, is *the causal-state condition applied to a partition*:

> "We can think about an individual as a system partition that is a sufficient predictor of its own future. This means in particular that S_{n−1} does not add any information about S_{n+1} besides the one already contained in S_n. Formally this reads as I(S_{n+1}; S_{n−1} | S_n) = 0."

They derive graded forms — autonomy A* = I(S_{n+1}; S_n), non-closure nC = I(S_{n+1}; E_n | S_n), and the identity A* − A = NTIC (non-trivial informational closure) — and prove that closure implies sufficiency, "informational closure is therefore a stronger notion than sufficiency." Individuality comes in degrees and at multiple nested levels by construction: "we wish to allow for a hierarchy of such partitions in order to capture biological examples such as organelles within cells, and cells within bodies within populations."

**Why this is the right fit for Mosaic, in four points.**

1. It individuates by **optimisation over partitions**, not by stipulating one. It answers Bruineberg et al.'s objection head-on: the modeller does not place the boundary, the criterion selects it. Compare their explicit contrast — "We infer or detect evolved individuals rather than assume that they exist."
2. The criterion is **the one Mosaic already uses**. Mosaic's Inference Engine entry qualifies engines by whether internal state carries predictive information. Krakauer et al. individuate by whether a partition propagates information from past to future. These are the same quantity. The definition gets *shorter*, not longer.
3. It is **graded by construction**, which matches `CONTEXT.md`'s existing "Being an engine is a matter of degree, and many blanketed systems are not one at all."
4. It **nests explicitly**, satisfying Thread D at the individuation level, where §5.2 satisfies it at the structural level.

**Its weakness, stated in full.** It begins from "a set of consistent measurements over time" — a vector of chemical concentrations, cell-type abundances, behavioural probabilities. Same presupposition as computational mechanics. The observable is chosen; only the partition of it is derived. This is not a solution to the map/territory problem and must not be presented as one. What it *is*: a reduction of the modeller's discretion from "where is the boundary" to "what is being measured," where the latter is an explicit, reportable, criticisable experimental choice, and the former was a hidden ontological assertion.

### 6.1 The vocabulary already went there — **Closure and the individuation criterion share an apparatus**

This subsection was added when the document was reconciled against `main` at `e3ac60a`, and it is the strongest new finding in the revision.

While this research was running, [#21](https://github.com/NGL321/mosaic/pull/21) landed a new `CONTEXT.md` entry, **Closure**: *"how much of the environment's influence on what a schema observes is accounted for by those observations themselves."* Its `_After_` line credits **informational closure — Bertschinger, Olbrich, Ay & Jost** ([*Autonomy: an information theoretic perspective*, BioSystems 91:331–345, 2008](https://www.sciencedirect.com/science/article/abs/pii/S0303264707001037); [*Information and closure in systems theory*](https://www.semanticscholar.org/paper/Information-and-closure-in-systems-theory-Bertschinger-Olbrich/846a8c33af45d6175643627b4df8fb0a9b63d423)) — and lumpability as the degenerate case.

That is the same apparatus, by three of the same authors, as the individuation criterion recommended in §6. [Krakauer, Bertschinger, Olbrich, Flack & Ay (2020)](https://link.springer.com/article/10.1007/s12064-020-00313-7) build individuality directly on it: their non-closure term is **nC = I(S_{n+1}; E_n | S_n)** — the information the environment carries about the system's next state beyond what the system's own present state carries — and their central identity is **A\* − A = NTIC**, non-trivial informational closure. The 2020 paper is the 2008 autonomy measure turned into a partition search.

**Why this matters for the recommendation.** The objection most likely to be raised against §6 is that it imports a foreign formalism to patch a definition — a degenerating move, accommodation rather than prediction. It does not. Mosaic independently adopted the informational-closure apparatus at the *schema* level, on its own reasons, before this document recommended its parent at the *engine* level. The recommendation is therefore **one apparatus used at two levels of an existing nesting**, not two apparatuses glued at a seam. That is a considerably better position than the one this document occupied when it was first written, and it was not available to be argued then.

**What is not established, stated precisely.** Mosaic's **Closure** is a property of a *schema* — of which variables were carved together. Krakauer et al.'s non-closure is a property of the *individuated system partition*. These are cognate quantities from one formalism at two levels of the hierarchy; they are **not shown here to be the same quantity**, and nothing in this document proves the schema-level and engine-level applications compose. Two things follow, both recorded rather than resolved:

1. It is an **open question**, and a well-posed one, whether an engine's Extraction and its schemas' Closures are functionals of a single partition-search objective evaluated at two levels of nesting. If they are, the not-a-scalar clause from [#15](https://github.com/NGL321/mosaic/issues/15) acquires a formal statement rather than a stipulation. This is a candidate Protective Belt rung and is listed alongside the §7.7 gap.
2. The identification is **Verification Debt**, added as item 6a in §9. Nobody should write it into `CONTEXT.md` as though it were proved — the `_After_` lines proposed in §8 credit the two sources separately, which is the honest form until it is.

---

## 7. The argument

### 7.1 Why option 1 (keep the blanket as stated) fails

Three independent reasons, any one sufficient.

The definition is **formally ambiguous**: "delineated by a Markov blanket" picks out one of two provably inequivalent conditions ([Biehl et al., Observation 1](https://arxiv.org/abs/2001.06408)) and the entry does not say which. The `_After_` line credits Pearl for "the blanket as conditional independence," but Pearl's construct is atemporal and neither condition is his.

The individuation move is **conceded by its own defenders** to be instrumental rather than ontological ([Ramstead](https://arxiv.org/abs/2112.15528)). Mosaic needs it to be ontological or it is not doing individuation.

Blanket existence is **not generic** in exactly the systems Mosaic studies — cyclic, feedback-coupled, far from equilibrium ([Aguilera et al.](https://arxiv.org/abs/2105.11203), conceded by [Heins & Da Costa](https://arxiv.org/abs/2205.10190)). A definition whose central term is a fine-tuning condition on parameters will not survive a referee.

### 7.2 Why option 2 (require the path version) is better but still fails

Requiring paths fixes the ambiguity and is the correct reading of Mosaic's own criterion. [Friston et al. (2023)](https://arxiv.org/abs/2210.12761) supply a formulation that can be cited exactly. So option 2 is a real improvement on option 1.

It does not fix the other two. The path blanket in that paper is *derived from* sparse coupling of the flow — Biehl's Condition 1 — and §3.5 is precisely the result that sparse coupling does not generically deliver conditional independence in cyclic systems. Nor does going to paths touch the instrumentalist concession, which is about what the construct is *for*, not about its temporal index. Option 2 buys precision and buys nothing else.

### 7.3 Why option 4 (replace outright) overshoots

The blanket picture is doing real work in Mosaic that is not formal. It supplies the intuition that a thing is what it is by virtue of how it is coupled, that the coupling has a sensory and an active face, and that this is what makes the interior/exterior distinction non-arbitrary. That intuition is correct and it is the reason the programme started here. It is also the shared vocabulary of the field Mosaic is writing into; deleting it costs legibility for no gain. The problem is not the picture, it is the picture being asked to carry a proof.

### 7.4 Why option 3, and what "option 3" has to mean

**Recommendation: option 3 — demote the blanket to intuition-and-citation, and put the formal weight on the computational-mechanics apparatus.** With one correction that the ticket's phrasing of option 3 does not anticipate, and which §4.4 forces:

**Causal states carry the qualification and capacity weight. They do not carry individuation, and nothing should say they do.** Individuation is carried by *selecting the partition under the same predictive-sufficiency criterion* — the [Krakauer et al.](https://link.springer.com/article/10.1007/s12064-020-00313-7) construction — with the observable declared rather than derived.

The resulting structure:

| Load | Carried by | Warrant |
|---|---|---|
| Individuation | Partition selected to maximise propagated past→future information; the engine is the partition that is a sufficient predictor of its own future | [Krakauer et al. (2020)](https://link.springer.com/article/10.1007/s12064-020-00313-7); reduces to I(S_{n+1}; S_{n−1} \| S_n) = 0 |
| Qualification | Excess entropy / predictive information above threshold | [Bialek et al. (2001)](https://arxiv.org/abs/physics/0007070); Theorem 5 of [Shalizi & Crutchfield](https://arxiv.org/abs/cond-mat/9907176) |
| Capacity | Statistical complexity C_μ | Theorems 1–4, same |
| Internal structure | ε-machine over causal states | Definitions 5, 8, same |
| Nesting | Local causal states composing to patch causal states | [Shalizi (2003), Lemma 2](https://arxiv.org/abs/math/0305160) |
| Intuition, and the field's vocabulary | Markov blanket | [Pearl (1988)](https://dl.acm.org/doi/book/10.5555/534975); [Friston (2013)](https://royalsocietypublishing.org/doi/10.1098/rsif.2013.0475) |

### 7.5 The strongest counter-argument to this recommendation, and the answer

**The counter-argument.** *You rejected the blanket because it smuggles in a modeller's choice, and you have replaced it with something that smuggles in a modeller's choice. Krakauer et al. need "a set of consistent measurements over time"; Crutchfield needs an alphabet and an instrument. You have moved the arbitrariness one step upstream and declared victory.*

This is correct as far as it goes, and any version of this document that denied it would be worthless.

**The answer is that the two choices are not of the same kind, and the difference is the whole point.**

Choosing a *boundary* and calling it discovered is an ontological claim disguised as a formal result — the precise thing [Bruineberg et al.](https://philsci-archive.pitt.edu/19726/7/The%20Emperor's%20New%20Markov%20Blankets_updated.pdf) object to and [Ramstead](https://arxiv.org/abs/2112.15528) declines to defend. Choosing an *observable* is an ordinary experimental commitment. Every measurement in every science makes one. It is stated in the methods section, it is contestable by anyone who thinks you measured the wrong thing, and it can be varied as a designed factor to test robustness. It is honest in a way the other is not.

Three further asymmetries make the trade favourable rather than lateral:

1. **Given the observable, everything downstream is forced.** Theorems 1–3 make the causal states the unique minimal sufficient statistic. There is no second choice. With the blanket, choosing the partition is the *first* of an open-ended sequence of choices, and Biehl et al. show even the definition is not settled.
2. **The individuation criterion becomes the qualification criterion.** Mosaic currently uses two unrelated notions — a blanket for the boundary, predictive information for the qualification — glued together. Under this recommendation they are one quantity applied at two levels. That is a *simplification* of the Hard Core, and by the Positive Heuristic a definition that does more with fewer primitives is the better one.
3. **Screening is derived, not assumed.** [Lemma 2 of Shalizi & Crutchfield](https://arxiv.org/abs/cond-mat/9907176) gives conditional independence of past and future given the causal state, as a *consequence* of the equivalence relation. This is the property the blanket is imported to provide. Mosaic gets it for free, without needing any system in the world to satisfy a fine-tuning condition.

That said, one honest cost remains uncancelled and should be logged rather than argued away: **Mosaic will no longer be able to say that an engine's boundary is a fact about the world independent of measurement.** It will say that, relative to a declared set of observables, there is a unique best partition and a unique minimal predictor. That is a weaker metaphysical claim. It is also the strongest one anything in this literature can currently support, and the recommendation is that Mosaic say the true weaker thing rather than the false stronger thing.

### 7.6 Whether this is a progressive Problemshift

By Lakatos's test, a Problemshift is progressive if it predicts novel facts and degenerating if it only accommodates known ones. This one predicts: under the amended definition, *whether a given subsystem is an engine becomes a computable quantity with a threshold*, so the claim "X is an engine and Y is not" becomes falsifiable against data rather than settled by where the modeller drew a line. It also opens a measurement programme — searching partitions of a network's activity for maximal informational closure — that the blanket definition did not license. **Progressive.**

The revision strengthens this verdict on a point that was not available when it was first written. The standard objection to a move like this one is that it is accommodation dressed as progress — reaching for a new formalism because the old one broke. §6.1 shows it is not: Mosaic had already adopted the informational-closure apparatus at the schema level, independently, in [#21](https://github.com/NGL321/mosaic/pull/21). The engine-level recommendation converges on a formalism the vocabulary had arrived at by another route, which is the shape of a progressive shift rather than a patch.

### 7.7 The open gap, worth recording

**Nobody has related Markov blankets and causal states formally.** I searched for such work and found none: no theorem stating when a Friston blanket's internal states are (or refine, or are refined by) the causal states of the blanket-conditioned process; no result connecting the C_μ of a particle's internal dynamics to the conditions under which its blanket exists. Given that Lemma 2 of [Shalizi & Crutchfield](https://arxiv.org/abs/cond-mat/9907176) delivers exactly the screening property the blanket is imported to provide, the question "when is the causal-state partition a Markov blanket, and vice versa?" is well-posed, apparently unasked, and squarely inside Mosaic's territory. It is a candidate Protective Belt rung in its own right.

A **second** well-posed gap was opened by the revision, stated in §6.1: whether an engine's **Extraction** and its schemas' **Closures** are functionals of one partition-search objective evaluated at two levels of nesting. If they are, the not-a-scalar clause from [#15](https://github.com/NGL321/mosaic/issues/15) stops being a stipulation and becomes a result. Both gaps are recorded here rather than pursued.

---

## 8. Proposed amendment to `CONTEXT.md` (a proposal, not an edit)

`CONTEXT.md` has **not** been modified, and under [`PROTOCOL.md`](https://github.com/NGL321/mosaic/blob/main/PROTOCOL.md) §5 it cannot be: authored files are human-only custody, and an agent's job is to propose exact replacement text. This is that text.

**Written against `CONTEXT.md` at `e3ac60a`**, i.e. after [#21](https://github.com/NGL321/mosaic/pull/21) filled the research substance section. The entry acquired two clauses in that merge — the **Extraction** cross-reference and the not-a-scalar clause resolving [#15](https://github.com/NGL321/mosaic/issues/15) — and both are **preserved verbatim below**. Only the individuation half changes. If this text is applied against an older copy of the entry it will silently revert #15, so check the base first.

> **Inference Engine**:
> A partition of a measured system whose internal state is a sufficient predictor of its own future — no earlier state adds information about later ones — and which carries predictive information about states outside the partition over and above what its boundary state carries. The partition is selected, not stipulated: among candidate partitions of a declared set of observables, an engine is one that maximises information propagated from past to future. Its internal structure is the ε-machine over its causal states, and the memory that structure costs is their statistical complexity. Being an engine is a matter of degree — measured by **Extraction**, below — and most partitions are not one at all. The degree is **not a scalar**: an engine's Extraction is one number, but the **Closure** of each of its schemas is another, and the two move independently.
> _Avoid_: Agent, model, module, particle, node, blanketed system
> _After_: Shalizi & Crutchfield (2001) for causal states as the minimal sufficient statistic for prediction, and for statistical complexity; Bialek, Nemenman & Tishby (2001) for predictive information; Krakauer, Bertschinger, Olbrich, Flack & Ay (2020) for individuation by choosing the partition that maximises propagated information. Pearl (1988) and Friston (2013) for the Markov blanket, which supplies the **intuition** — a thing is what it is by how it is coupled, with a sensory and an active face — and is cited for that and not relied on formally.
> _Departs_: The blanket **no longer individuates**. It was doing so in an earlier version of this entry; it cannot. The instantaneous and path formulations are provably inequivalent (Biehl, Pollock & Kanai 2021), blanket existence is a fine-tuning condition in cyclic systems (Aguilera, Millidge, Tschantz & Buckley 2022), and the framework's own defenders describe it instrumentally rather than as drawing boundaries in nature (Ramstead 2022). Individuation and qualification are therefore **one criterion at two levels** rather than two criteria glued together. Departs from computational mechanics in turn: causal states characterise a process whose observable is already given and do not individuate on their own, so the partition search is Mosaic's addition, after Krakauer et al. The observable is **declared, not discovered** — the boundary is a fact relative to a stated measurement, not independent of it.

> **Provenance of the proposed entry.** **T3** — machine-produced and unverified. Every
> source behind it was read directly and is in the appendix, which is *evidence, not
> warrant*: the Shalizi–Crutchfield theorems, the Biehl–Pollock–Kanai counterexample and the
> Krakauer construction are all Verification Debt, itemised below and filed. Promoted from an
> HTML comment under [#50](https://github.com/NGL321/mosaic/issues/50) — debt logged inside a
> comment is logged nowhere ([#5](https://github.com/NGL321/mosaic/issues/5)).

Consequential edits implied elsewhere, flagged but not drafted:

- **Least Action** — unaffected. Its `_After_` line already cites [Still, Sivak, Bell & Crooks (2012)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.109.120604) for retained non-predictive information as dissipated work, which is the same currency as C_μ − E. Worth noting that Theorem 5's gap now has a thermodynamic reading; that is a Protective Belt claim, not a definitional change.
- **Representation** — unaffected in content. Its "carrying predictive information the engine's inference actually uses" now names the same quantity the engine definition uses, which is a tightening.
- **Schema** — the "an engine holding several schemas is itself a small network" clause is now *supported* rather than merely asserted, via [Shalizi (2003), Lemma 2](https://arxiv.org/abs/math/0305160).
- **Extraction** — unaffected in content, and **given a formal ceiling it currently lacks**. Extraction is "achieved predictive information as a fraction of the ceiling set by the observed process itself." Under this recommendation that ceiling has a name and a theorem: it is the excess entropy E of the observed process (§4.3), which is by construction the most any predictor can extract. The entry's own worry — that a ratio needs a well-defined denominator to compare across environments — is answered by an existing quantity rather than a new one.
- **Closure** — unaffected in content, and **the same lineage as the proposed individuation criterion**. See §6.1; this is the strongest coherence finding in the revision and is set out there rather than here.

---

## What this does not establish

Retrofitted under [#50](https://github.com/NGL321/mosaic/issues/50) against the [output
contract](README.md), which postdates this document. **Open gaps** is recoverable in full —
§7.7 was already written as one, and is the strongest thing here. **Sources not reached** is
the subsection [#50](https://github.com/NGL321/mosaic/issues/50) says an agent cannot honestly
retrofit, and it is thin below for exactly that reason: it is reconstructed from the
document's own text, not from the session that produced it.

### Sources not reached

**Thin, and the thinness is the finding.** Every source this document *cites* is in the
appendix and was read; what cannot be recovered from the document alone is what was *wanted
and not got*. The original session is not reachable, so the honest answer is that this
subsection is incomplete rather than empty, and a reader should not read its shortness as a
clean bill.

Two are recoverable from the text:

- **Nothing formally relating Markov blankets and causal states.** Searched for and not found (§7.7). This is a genuine absence in the literature rather than an access failure — which is why it is recorded as an open gap below and not only here.
- **The Bertschinger, Olbrich, Ay & Jost (2008) paper is behind a publisher paywall.** It is load-bearing for §6.1 and appears in the appendix as a publisher landing page. [#33](https://github.com/NGL321/mosaic/issues/33) independently records that the same paper is cited from **recall, not warrant**, on `Closure` — so the one source both halves of §6.1's identification rest on is the one nobody has opened.

### Open gaps

- **Nobody has related Markov blankets and causal states formally** (§7.7). No theorem states when a Friston blanket's internal states are, refine, or are refined by the causal states of the blanket-conditioned process; nothing connects a particle's C_μ to the conditions under which its blanket exists. Given that Lemma 2 delivers exactly the screening property the blanket is imported to provide, *"when is the causal-state partition a Markov blanket, and vice versa?"* is well-posed, apparently unasked, and a candidate Protective Belt rung.
- **Whether an engine's Extraction and its schemas' Closures are one partition-search objective at two levels of nesting** (§6.1). If they are, [#15](https://github.com/NGL321/mosaic/issues/15)'s not-a-scalar clause stops being a stipulation and becomes a result. Filed as [#145](https://github.com/NGL321/mosaic/issues/145).
- **The recommendation still requires the modeller to declare an observable.** It does not escape the map/territory problem; it makes the choice explicit and falsifiable instead of hiding it inside a word that sounds ontological. Whether an observable can be *chosen well* — by what criterion, against what — is not addressed anywhere.

### Load-bearing ifs

- **If the Biehl–Pollock–Kanai Ornstein–Uhlenbeck counterexample does not hold, the whole recommendation loses its sharpest argument.** §2's **Refuted** is the finding everything downstream leans on, and it is taken on the paper's authority — nobody here reconstructed it. [#141](https://github.com/NGL321/mosaic/issues/141), and the one item the document itself says must be reconstructible on a whiteboard.
- **If Shalizi (2003) Lemma 2 does not compose in the form §5.2 reads it as composing**, the nesting advantage of causal states over blankets disappears and Thread D's asymmetry goes with it — [#146](https://github.com/NGL321/mosaic/issues/146).
- **If §6.1's identification is over-claimed**, the "one apparatus at two levels" answer to the degenerating-problemshift objection becomes a resemblance argument rather than a fact, and the recommendation has to be defended on its merits alone. The document flags and refuses the over-claim; it does not settle it — [#145](https://github.com/NGL321/mosaic/issues/145).
- **If the quantities cannot be estimated from finite samples at the volumes Mosaic can collect**, every theorem above is true and unusable. This is the largest hidden risk in the document and it is not a reading gap — [#147](https://github.com/NGL321/mosaic/issues/147).

---

## Verification Debt

Nine items, all filed. Mathematics Noah would need to defend the amended entry unaided,
**ordered by dependency**, which is the order the Curriculum should schedule them in.

1. **Information theory to the data-processing inequality and sufficient statistics** — [#139](https://github.com/NGL321/mosaic/issues/139). Required to read *any* of Theorems 1–5. The proofs use only the chain rule, H[f(X)] ≤ H[X], and conditioning-reduces-entropy — genuinely elementary, and they must be owned rather than recognised. [Cover & Thomas, 2nd ed.](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X), ch. 2.
2. **Shalizi & Crutchfield Theorems 1, 2, 3 and 5, reproved from the paper** — [#140](https://github.com/NGL321/mosaic/issues/140). Theorem 2 depends on the Refinement Lemma (Lemma 7), the only non-trivial step; there is an alternative proof in Appendix E and both should be worked.
3. **The Biehl–Pollock–Kanai Ornstein–Uhlenbeck counterexample (Appendix A)** — [#141](https://github.com/NGL321/mosaic/issues/141). Requires linear SDEs, the stationary Fokker–Planck equation, the Helmholtz decomposition f = (Γ + R)∇ ln p*, and the continuous Lyapunov equation JΣ* + Σ*Jᵀ + 2Γ = 0. **The single item that must be reconstructible on a whiteboard**, because it is the technical claim the demotion of the blanket rests on.
4. **Excess entropy and entropy convergence** — [#142](https://github.com/NGL321/mosaic/issues/142). [Crutchfield & Feldman (2003)](https://arxiv.org/abs/cond-mat/0102181) §III–V: block entropy H(L), its discrete derivatives, and E as the L→∞ intercept. Needed to say what E *is* without hand-waving, and to know its finite-data estimate is biased.
5. **Subextensivity of predictive information** — [#143](https://github.com/NGL321/mosaic/issues/143). [Bialek et al. (2001)](https://arxiv.org/abs/physics/0007070) §II: why I_pred(T) = S₁(T) and why it cannot grow linearly. Modest, and it is what makes the qualification criterion defensible against *"isn't that just mutual information?"*
6. **The Krakauer identity A* − A = NTIC and the closure ⇒ sufficiency implication** — [#144](https://github.com/NGL321/mosaic/issues/144). Half a page, and elementary once item 1 is done. Must be reproduced because it **is** the individuation criterion.
7. **The informational-closure family, and whether `Closure` and non-closure are one quantity at two levels** — [#145](https://github.com/NGL321/mosaic/issues/145). [Bertschinger, Olbrich, Ay & Jost (2008)](https://www.sciencedirect.com/science/article/abs/pii/S0303264707001037), then the derivation of nC and NTIC in Krakauer et al. Settles §6.1 — the one place this recommendation touches vocabulary that landed independently, and so the place an unearned identification would do the most damage. Cheap relative to its value, since item 6 covers most of the machinery.
8. **Shalizi (2003), Lemma 2 (Patch Composition), and the lightcone construction** — [#146](https://github.com/NGL321/mosaic/issues/146). Needed for `Schema`'s nesting claim. More notation than mathematics — a judgement that is itself untested until someone reads it.
9. **Estimation, not just theory** — [#147](https://github.com/NGL321/mosaic/issues/147), and **the largest hidden debt.** Every quantity above is defined on an infinite stationary process and must be estimated from finite samples. Causal-state reconstruction (CSSR and its descendants), entropy-rate estimator bias, and the sample complexity of C_μ are live problems, and none of the theorems in §4.2 says anything about them. Any empirical Mosaic claim will be attacked here first. Its own Curriculum block, not folded into the others.

**Debt discharged by the recommendation, recorded as a credit:** the non-equilibrium
steady-state machinery, the Helmholtz/solenoidal decomposition, and the information geometry
of Bayesian mechanics are no longer load-bearing for the `Inference Engine` definition. Item 3
needs the SDE apparatus **once**, to verify a counterexample — not to build on.

**A note on scope, added by the retrofit.** These nine were written as *"new Verification Debt
created by this recommendation"*, and §8's proposed entry has not been applied to `CONTEXT.md`.
They are filed anyway, and unconditionally: [#14](https://github.com/NGL321/mosaic/issues/14)
is closed as decided, so the argument is in the record and the record is what the debt holds
down. Item 9 in particular does not wait on any amendment — it is a fact about the quantities,
not about the entry. Where an item's phrasing names the amended entry, read it as naming the
claim the entry would carry.

---

## Appendix: primary sources cited

**Markov blankets — origin and free-energy formulations**
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference.* Morgan Kaufmann. https://dl.acm.org/doi/book/10.5555/534975
- Friston, K. (2013). *Life as we know it.* J. R. Soc. Interface 10:20130475. https://royalsocietypublishing.org/doi/10.1098/rsif.2013.0475
- Friston, K. (2019). *A free energy principle for a particular physics.* arXiv:1906.10184. https://arxiv.org/abs/1906.10184
- Friston, K., Fagerholm, E. D., Zarghami, T. S., Parr, T., Hipólito, I., Magrou, L. & Razi, A. (2021). *Parcels and particles: Markov blankets in the brain.* Network Neuroscience 5(1):211–251. https://arxiv.org/abs/2007.09704
- Hipólito, I., Ramstead, M. J. D., Convertino, L., Bhat, A., Friston, K. & Parr, T. (2021). *Markov blankets in the brain.* Neurosci. Biobehav. Rev. https://www.sciencedirect.com/science/article/pii/S0149763421000579
- Friston, K., Da Costa, L., Sakthivadivel, D. A. R., Heins, C., Pavliotis, G. A., Ramstead, M. & Parr, T. (2023). *Path integrals, particular kinds, and strange things.* Physics of Life Reviews 47:35–62. https://www.sciencedirect.com/science/article/pii/S1571064523001094 · https://arxiv.org/abs/2210.12761

**Critiques and replies**
- Biehl, M., Pollock, F. A. & Kanai, R. (2021). *A technical critique of some parts of the free energy principle.* Entropy 23(3):293. https://www.mdpi.com/1099-4300/23/3/293 · https://arxiv.org/abs/2001.06408
- Aguilera, M., Millidge, B., Tschantz, A. & Buckley, C. L. (2022). *How particular is the physics of the free energy principle?* Physics of Life Reviews 40:24–50. https://arxiv.org/abs/2105.11203
- Heins, C. & Da Costa, L. (2022). *Sparse coupling and Markov blankets: A comment on "How particular is the physics of the Free Energy Principle?"* arXiv:2205.10190. https://arxiv.org/abs/2205.10190
- Bruineberg, J., Dołęga, K., Dewhurst, J. & Baltieri, M. (2022). *The Emperor's New Markov Blankets.* Behavioral and Brain Sciences 45:e183. https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/emperors-new-markov-blankets/715C589A73DDF861DCF8997271DE0B8C · https://philsci-archive.pitt.edu/19726/7/The%20Emperor's%20New%20Markov%20Blankets_updated.pdf
- Bruineberg, J., Dołęga, K., Dewhurst, J. & Baltieri, M. (2022). *The Emperor Is Naked: Replies to commentaries on the target article.* Behavioral and Brain Sciences 45:e219. https://pubmed.ncbi.nlm.nih.gov/36172792/
- Ramstead, M. J. D. (2022). *The empire strikes back: Some responses to Bruineberg and colleagues.* Behavioral and Brain Sciences 45. https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/empire-strikes-back-some-responses-to-bruineberg-and-colleagues/EAD6092F39E09AE0BABA34012E54CA08 · https://arxiv.org/abs/2112.15528

**Computational mechanics**
- Crutchfield, J. P. & Young, K. (1989). *Inferring statistical complexity.* Phys. Rev. Lett. 63:105–108. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.63.105
- Shalizi, C. R. & Crutchfield, J. P. (2001). *Computational mechanics: Pattern and prediction, structure and simplicity.* J. Stat. Phys. 104:817–879. https://link.springer.com/article/10.1023/A:1010388907793 · https://arxiv.org/abs/cond-mat/9907176
- Crutchfield, J. P. & Feldman, D. P. (2003). *Regularities unseen, randomness observed: Levels of entropy convergence.* Chaos 13:25–54. https://pubs.aip.org/aip/cha/article/13/1/25/135236 · https://arxiv.org/abs/cond-mat/0102181
- Crutchfield, J. P. (2012). *Between order and chaos.* Nature Physics 8:17–24. https://www.nature.com/articles/nphys2190 · https://csc.ucdavis.edu/~chaos/papers/Crutchfield.NaturePhysics2012.pdf
- Shalizi, C. R. (2003). *Optimal nonlinear prediction of random fields on networks.* Discrete Mathematics and Theoretical Computer Science. https://arxiv.org/abs/math/0305160
- Shalizi, C. R., Shalizi, K. L. & Haslinger, R. (2004). *Quantifying self-organization with optimal predictors.* Phys. Rev. Lett. 93:118701. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.93.118701
- Barnett, N. & Crutchfield, J. P. (2015). *Computational mechanics of input-output processes: Structured transformations and the ε-transducer.* J. Stat. Phys. https://arxiv.org/abs/1412.2690
- Rupe, A. & Crutchfield, J. P. (2018). *Local causal states and discrete coherent structures.* Chaos 28:075312. https://arxiv.org/abs/1801.00515

**Predictive information and individuality**
- Bialek, W., Nemenman, I. & Tishby, N. (2001). *Predictability, complexity, and learning.* Neural Computation 13:2409–2463. https://direct.mit.edu/neco/article/13/11/2409/6521 · https://arxiv.org/abs/physics/0007070
- Krakauer, D., Bertschinger, N., Olbrich, E., Flack, J. C. & Ay, N. (2020). *The information theory of individuality.* Theory in Biosciences 139:209–223. https://link.springer.com/article/10.1007/s12064-020-00313-7 · https://arxiv.org/abs/1412.2447
- Still, S., Sivak, D. A., Bell, A. J. & Crooks, G. E. (2012). *Thermodynamics of prediction.* Phys. Rev. Lett. 109:120604. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.109.120604
- Bertschinger, N., Olbrich, E., Ay, N. & Jost, J. (2008). *Autonomy: An information theoretic perspective.* BioSystems 91:331–345. https://www.sciencedirect.com/science/article/abs/pii/S0303264707001037
- Bertschinger, N., Olbrich, E., Ay, N. & Jost, J. (2006). *Information and closure in systems theory.* In *Explorations in the Complexity of Possible Life: Proceedings of the 7th German Workshop on Artificial Life*, pp. 9–21. IOS Press, Amsterdam. Workshop chapter with no DOI-stable publisher page; author-hosted copy on Olbrich's profile: https://www.researchgate.net/profile/Eckehard-Olbrich/publication/41832496_Information_and_closure_in_systems_theory/links/5805d79208aee314f68e3137/Information-and-closure-in-systems-theory.pdf
- Cover, T. M. & Thomas, J. A. *Elements of Information Theory*, 2nd ed. Wiley. https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X — cited in §9 as Curriculum reading, not as evidence.

**Mosaic documents cross-referenced**
- `PROTOCOL.md` — working protocol (custody, commit types, merges). https://github.com/NGL321/mosaic/blob/main/PROTOCOL.md
- `docs/research/2026-07-28-verifying-cited-influences.md` — the #13/#20 citation audit, whose §4 verifies the Pearl and Friston attributions this document reasons about. https://github.com/NGL321/mosaic/blob/main/docs/research/2026-07-28-verifying-cited-influences.md
