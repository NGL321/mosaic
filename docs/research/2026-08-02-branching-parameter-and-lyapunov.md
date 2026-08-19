---
ticket: 123
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 11
debt: [131]
supersedes: null
---

# The branching parameter's Lyapunov ancestor exists, and it is not a Lyapunov exponent

Eleven primary sources were opened and read directly, nine of them in full: the two random-Boolean-network papers that define a "Lyapunov exponent" for a discrete network (Luque & Solé 2000, Shmulevich & Kauffman 2004), the edge-of-chaos recurrent-network paper that defines the critical line (Natschläger, Bertschinger & Legenstein 2004), four papers from the avalanche-criticality line that use the branching parameter σ (Kinouchi & Copelli 2006, Larremore/Shew/Restrepo 2011, Beggs & Timme 2012, Cayco Gajic & Shea-Brown 2012), one review that draws the edge-of-chaos link in words (Hesse & Gross 2014), one preprint that carries the claim in the exact form the ticket describes (Dasgupta 2014), and the two papers by Kanders, Lorimer and Stoop that measure avalanche criticality and the Lyapunov spectrum in the same network. Text was extracted from the authors' own deposits — arXiv, NeurIPS proceedings, PubMed Central author manuscripts, Frontiers, the ETH Research Collection — and every word count reported below (`Lyapunov`, `branching`, `chaos`, `entropy`) was run by this agent over the extracted text of the document named, not recalled. Where a PDF's text layer drops a Greek glyph the symbol is restored in brackets and named in words. Three papers named by the ticket or by the citation chain could **not** be opened — Bertschinger & Natschläger (2004), Beggs (2008) and Haldeman & Beggs (2005) — and are recorded under *Sources not reached*; the last two are filed as [#131](https://github.com/NGL321/mosaic/issues/131). None of this has been checked by Noah unaided.

---

## 0. Verdict

| Sub-question | Verdict | Argued in |
|---|---|---|
| **1** Does any primary source state a correspondence between a branching-type mean-offspring number and a quantity it calls a Lyapunov exponent? | **Established** — the RBN literature does, explicitly: λ = log[2p(1−p)K], and 2p(1−p)K is the mean number of descendant bit-flips | §2 |
| **2** Is that λ the maximal Lyapunov exponent of a smooth flow? | **Refuted** — it is a Hamming-distance damage-expansion rate, and Luque & Solé say in the same paper that deterministic chaos "is not possible in these systems" | §2 |
| **3** Does that identity have the status of a theorem? | **Refuted** — λ is *defined* as the time-average of log of the expansion rate whose annealed mean is the branching number; σ = 1 ⟺ λ = 0 is a tautology composed with a mean-field approximation | §2 |
| **4** Is the RBN branching number the same object as Beggs & Plenz's σ? | **Refuted** — one counts descendants of a *difference* against a reference trajectory, the other descendants of *activity* against a quiescent background | §3 |
| **5** Does the neuronal-avalanche literature connect σ to a dynamical exponent? | **Refuted** — four papers in that line, opened in full, contain zero occurrences of "Lyapunov"; the criticality condition they state is a linear-stability multiplier λ_A = 1, not an exponent λ = 0 | §3 |
| **6** Does the edge-of-chaos recurrent-network literature identify its critical point with σ = 1? | **Refuted** — its critical line is the slope α = 1 of an annealed Hamming-distance map; the paper contains zero occurrences of "branching", "avalanche" and "Lyapunov" | §4 |
| **7** Where does the σ ↔ λ claim come from? | **Established** — from verbal identification in reviews and from citation drift, both traced to specific sentences | §5 |
| **8** When both quantities are measured in one model, do they co-occur? | **Refuted** — Kanders, Lorimer & Stoop measure both and find λ₁ > 0 at sub-, at critical, and at supercritical avalanche behaviour | §6 |
| **9** Does any source state a σ ↔ h_μ correspondence? | **Refuted** — none was found, and the one measurement of both rises monotonically with coupling and peaks *supercritically* | §6 |
| **10** Does the cortical placement question reopen with a usable instrument? | **Refuted** — σ is what Beggs & Plenz said it was, a branching-process statistic; nothing licenses reading Order off it | §7 |

### The one-line verdict

> **The claim has a real ancestor, and the ancestor is not the claim.** In the random-Boolean-network literature a quantity called the Lyapunov exponent is *defined* as the logarithm of the mean number of descendant bit-flips, so "σ = 1 ⟺ λ = 0" is true there by construction — but that λ is a Hamming-distance damage-expansion rate in a system whose own authors say deterministic chaos is impossible, and that σ counts descendants of a *perturbation*, not of *activity*. Beggs & Plenz's σ is the second object, and the four avalanche-criticality papers opened here contain the word "Lyapunov" zero times between them; what they state is a linear-stability condition on the quiescent fixed point, λ_A = 1, which is a multiplier equal to one and not an exponent equal to zero. The identification in the neural literature is made in reviews, in words, with "therefore" carrying the weight a theorem would carry, and it degrades by citation into "the Lyapunov exponent is nearly zero at the critical point" attributed to a paper whose own abstract says "neutral". The one study that measures avalanche criticality and the Lyapunov spectrum in the same network finds them decoupled. **The cortical placement question does not reopen.**

---

## 1. Search scope, stated before the findings

A null result is worth exactly what its scope statement is worth, so the scope is stated first and in full.

**Literatures searched.** Three, as the ticket names them: (a) the neuronal-avalanche line descending from Beggs & Plenz (2003); (b) the edge-of-chaos recurrent-network and reservoir-computing line; (c) the random-Boolean-network line descending from [Derrida & Pomeau (1986)](https://doi.org/10.1209/0295-5075/1/2/001), whose annealed approximation `2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md` established is the actual source of the ordered/chaotic dichotomy. A fourth was added when the RBN thread turned up branching-process language: (d) the perturbation-avalanche treatment of RBNs.

**Queries run.** Fifteen, all through WebSearch: `Luque Solé "Lyapunov exponents in random Boolean networks" annealed approximation`; `branching parameter sigma "Lyapunov exponent" neuronal avalanches criticality correspondence`; `Bertschinger Natschläger "Real-time computation at the edge of chaos in recurrent neural networks" critical line Lyapunov`; `Shmulevich Kauffman "Activities and sensitivities in Boolean network models"`; `Rämö Kesseli Yli-Harja "perturbation avalanches" Boolean networks branching process criticality`; `"branching ratio" OR "branching parameter" equals "average sensitivity" Boolean network "Lyapunov exponent" logarithm`; `Kinouchi Copelli "Optimal dynamical range of excitable networks at criticality" branching ratio largest eigenvalue`; `Larremore Shew Restrepo "Predicting criticality and dynamic range in complex networks" largest eigenvalue`; `Boedecker Obst Lizier Mayer Asada "Information processing in echo state networks at the edge of chaos" Lyapunov exponent`; `Haldeman Beggs 2005 "Critical branching captures activity in living neural networks…"`; `Beggs 2008 "criticality hypothesis" review "branching parameter" "edge of chaos" Lyapunov`; `Kanders Toyoizumi Stoop "Avalanche and edge-of-chaos criticality do not necessarily co-occur in neural networks"`; `"branching parameter" "Kolmogorov-Sinai entropy" neural avalanches critical sigma=1 entropy rate relation`; `theorem "branching process" criticality "maximal Lyapunov exponent" equivalence proof dynamical systems mean offspring`; `Rämö Kauffman Kesseli Yli-Harja "Measures for information propagation in Boolean networks"`.

**Sources opened.** The eleven in the appendix. **Sources named and not opened:** six, itemised under *Sources not reached*.

**Method for the negative claims.** Every "zero occurrences of X" below was produced by extracting the document's text with `pypdf` (for PDFs) or by tag-stripping the publisher's HTML, then running a case-insensitive regular expression over the result. The extraction files are working artifacts and are not committed. Two consequences worth stating: a word rendered entirely as a figure would be missed, and a word in a reference title counts as an occurrence unless said otherwise — which is why the counts below distinguish body prose from bibliography.

## 2. The RBN literature does state it, in a form the ticket did not anticipate

The ticket's guess that the random-Boolean-network literature is a likely home is **correct**, and the thing found there is not what was expected.

[Luque & Solé, *Lyapunov exponents in random Boolean networks*, Physica A **284** (2000) 33–45](https://arxiv.org/abs/adap-org/9907001) was read in full, sixteen pages, from the arXiv deposit. They define a damage expansion rate, their equation (18):

> "η(t) = |d(t + 1)| / |d(t)|"

where d(t) is the Hamming-distance vector between a trajectory and a perturbed copy, and then, equation (19):

> "This allows us to define a Lyapunov exponent: λ(T) = (1/T) Σ_{t=1}^{T} log η(t)"

Under the annealed (Derrida–Pomeau) approximation they compute the mean expansion rate as their equation (24), `η̄ ≈ 2p(1 − p)K`, and conclude with equation (27):

> "λ = log[2p(1 − p)K] … which determine the two classical regimes: λ < 0 (order) and λ > 0 (chaos) with the marginal case λ = 0."

**2p(1 − p)K is the mean number of descendants of a single bit-flip.** [Shmulevich & Kauffman, *Activities and sensitivities in Boolean network models*, Phys. Rev. Lett. **93** (2004) 048701](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/), read in full from the PubMed Central author manuscript, derives exactly that quantity from first principles as the expected *average sensitivity* — "the number of Hamming neighbors of x on which the function value is different than on x" — obtaining `E[s_f] = K·2p(1−p)`, and then states the identity outright:

> "It is interesting to note that in the context of random Boolean networks with connectivity K, the expected average sensitivity determines the well-known critical transition curve with the Lyapunov exponent [11] being the logarithm of the expected average sensitivity: λ = log E[s_f]."

Their reference [11] is Luque & Solé (2000). So there is a real, traceable, two-paper chain in which **a mean number of descendants and a quantity named "the Lyapunov exponent" are related by a logarithm**, and the critical point of the one is the zero of the other. This is the closest thing in the searched literatures to what the ticket asked for, and it is worth being precise about what it is and is not.

**It is not a theorem.** λ is *defined* by equation (19) as the long-run average of log η, and η is *defined* by (18) as the one-step expansion factor of the Hamming distance. That log of a mean-offspring number is zero exactly when the number is one is arithmetic. The only substantive content is the annealed step from η(t) to `2p(1−p)K`, which is a mean-field approximation, not an identity — Luque & Solé present it as one ("assuming that, on mean field grounds, F′(x(t)) can be replaced by a random matrix Ω"). Shmulevich & Kauffman contain **zero** occurrences of "branching" and zero of "entropy"; Luque & Solé contain **zero** occurrences of "branching".

**It is not a smooth-manifold exponent, and the authors say so.** Luque & Solé are explicit that the object they are constructing is an analogy, in the paragraph that introduces it:

> "A RBN is by definition a discrete (N cells) deterministic system with a finite number of states ({0, 1}), and therefore periodic patterns are expected after a maximum of 2^N steps. Thus, if we follow strictly the standard definition of low-dimensional deterministic chaos, chaotic behavior is not possible in these systems. Taking this into account, we will define chaotic behavior here through damage spreading […] Thus our disordered phase will be called chaotic phase, analogously to continuous systems."

That is the same move [Tisseur (2000)](https://arxiv.org/abs/math/0312136) documents for cellular automata and that `docs/research/2026-08-02-pesin-and-the-order-axis.md` §3 already established has a published counterexample: an exponent built from Hamming-distance divergence in a discrete-state system is a *different object* from λ_max of a smooth flow, and the entropy correspondence that holds for the second fails for the first. A source that conflates them would be the finding; these two sources do not conflate them — they announce the substitution in plain words and then use the word "Lyapunov" for the substitute anyway. The conflation happens downstream, in readers.

## 3. Beggs & Plenz's σ is a different quantity, and the avalanche literature never names an exponent

The RBN branching number counts descendants of a **difference** — one flipped bit, propagating against a reference copy of the same network. Beggs & Plenz's σ counts descendants of **activity** — one active electrode, propagating against a quiescent background. These coincide only where the background is silent, so that "active" and "differs from the reference" name the same event. That is a modelling assumption, not an identity, and it is exactly the assumption that fails in a network whose neurons fire on their own (§6).

The avalanche-criticality line keeps σ in the first sense throughout and never reaches for an exponent. [Kinouchi & Copelli, *Optimal dynamical range of excitable networks at criticality*, Nature Physics **2** (2006) 348–351](https://arxiv.org/abs/q-bio/0601037), read in full from the arXiv deposit, defines it as a pure offspring count:

> "The local branching ratio σ_j = Σ_i^{K_j} p_ij corresponds to the average number of excitations created in the next time step by the j-th element […] The average branching ratio σ is the relevant control parameter."

Word counts over the full extracted text: **"Lyapunov" 0, "chaos" 0, "chaotic" 0, "entropy" 0**, "branching" 9.

[Larremore, Shew & Restrepo, *Predicting criticality and dynamic range in complex networks*, Phys. Rev. Lett. **106** (2011) 058101](https://arxiv.org/abs/1008.0022), read in full, generalises σ to arbitrary topology and in doing so states the actual mathematical content of "criticality" in this literature:

> "To examine the linear stability of this fixed point, we set η = 0 and linearize around p_i^t = 0 […] Thus, the stability of the solution p⃗ = 0 is governed by the largest eigenvalue of the network adjacency matrix, λ, with λ < 1 being stable and λ > 1 being unstable. Therefore, the critical state described in previous literature, occurring at various values of ⟨d⟩, should universally occur at λ = 1."

Word counts: **"Lyapunov" 0, "chaos" 0, "chaotic" 0, "entropy" 0**.

**This paper is the likeliest single source of the confusion, and it is worth stating why.** It calls the largest eigenvalue of the adjacency matrix λ, and its criticality condition is **λ = 1**. A Lyapunov exponent is also written λ, and its criticality condition is **λ = 0**. The two are related — log of a linear multiplier is a growth exponent — but the multiplier here is the linearisation of a mean-field map *about the quiescent fixed point*, whereas λ_max is an average along a typical trajectory of the attractor the system actually occupies. Those agree only when the system sits at the quiescent fixed point, which is the one state in which nothing is happening. A reader carrying "criticality at λ = 1" and "edge of chaos at λ = 0" in the same head, without carrying which λ each is, gets the ticket's claim for free and without evidence.

Two more from the same line confirm the pattern. [Beggs & Timme, *Being critical of criticality in the brain*, Front. Physiol. **3** (2012) 163](https://pmc.ncbi.nlm.nih.gov/articles/PMC3369250/) — Beggs' own later review, read in full — has **"Lyapunov" 0** and "edge of chaos" once, inside the title of a cited reference, which is the same pattern §5 of `docs/research/2026-08-02-pesin-and-the-order-axis.md` found in Beggs & Plenz (2003) itself. [Cayco Gajic & Shea-Brown, *Neutral stability, rate propagation, and critical branching in feedforward networks*](https://arxiv.org/abs/1210.8406), read in full, takes σ directly from Beggs & Plenz and glosses σ = 1 as *stability*, not chaos:

> "To avoid decay or growth of activity, the system must produce firing rate dynamics which are neutrally stable, satisfying σ ≈ 1; such networks are labeled critical."

**"Lyapunov" 0** in thirty-one pages, against twenty-seven occurrences of "branching". And their result is itself a decoupling: the connectivity γ_obs at which σ ≈ 1 and the connectivity γ_eig at which the mean-field transition matrix has the eigenstructure supporting broad responses "do coincide in the noisy case" but not for high spike thresholds — two fingerprints that come apart under a parameter change.

## 4. The edge-of-chaos recurrent-network literature does not use σ either

The ticket's second guess is that the reservoir-computing line, which does compute Lyapunov exponents, might identify its critical point with a branching parameter. It does not, and the check is clean.

Bertschinger & Natschläger's *Neural Computation* paper is paywalled and was not reached (see below), but the same three authors' companion paper — [Natschläger, Bertschinger & Legenstein, *At the Edge of Chaos: Real-time Computations and Self-Organized Criticality in Recurrent Neural Networks*, NIPS 17 (2004) 142–152](https://proceedings.neurips.cc/paper_files/paper/2004/file/f8da71e562ff44a2bc7edf3578c593da-Paper.pdf) — is open, and was read in full. Word counts over the whole eight pages: **"Lyapunov" 0, "branching" 0, "avalanche" 0, "entropy" 0**. "Critical line" occurs twelve times, and it is defined the way Luque & Solé define theirs — as the marginal slope of an annealed Hamming-distance map (the glyph α is dropped by the PDF's text layer and is restored in brackets):

> "To define the chaotic and ordered phase of an input driven network we use an approach which is similar to that proposed by Derrida and Pomeau [2] for autonomous systems: consider two (initial) network states with a certain (normalized) Hamming distance […] Whether d* = 0 or d* ≠ 0 can be decided by looking at the slope of the function f(·,·,·) at its fixed point d* = 0 […] Accordingly we say that the network is in the ordered, critical or chaotic regime if [α] < 1, [α] = 1 or [α] > 1 respectively."

and the critical line itself is written as a condition on the **expected number of downstream bits flipped by one flip**: `K · P_bf = 1`, where P_bf "denotes the probability (averaged over the inputs and the network activity) that a node will change its output if a single out of its K input bits is flipped".

**So the two literatures compute the same mean-field quantity and give it four names.** Luque & Solé call it the damage expansion rate η̄; Shmulevich & Kauffman call it the expected average sensitivity E[s_f]; Natschläger, Bertschinger & Legenstein call it K·P_bf and its marginal value the critical line; Kinouchi & Copelli and the avalanche line call something *structurally analogous but referentially different* the branching ratio σ. Only the first two attach the word "Lyapunov" to its logarithm. None of the three that define it as a perturbation count calls it σ; the one line that calls it σ counts activity instead. That is the whole finding, and it is why the ticket's search did not converge: the correspondence exists between names, not between the two objects Mosaic was relating.

## 5. Where the neural-side claim comes from: a "therefore", and a citation that drifts

The claim does have a home in the neural literature. It is not a theorem, a model result, or a measurement; it is an assertion in review prose, and it degrades as it is cited.

[Hesse & Gross, *Self-organized criticality as a fundamental property of neural systems*, Front. Syst. Neurosci. **8** (2014) 166](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2014.00166/full) — one of the two references Kanders, Lorimer & Stoop name as having "drawn links between edge-of-chaos and avalanche criticality" — was read in full. It contains **"Lyapunov" 0** times and "edge of chaos" four times, of which two are in the bibliography. The two in the body are these:

> "Because phase transitions usually break certain symmetries of the system, they often separate an ordered state from a less ordered state. Critical states are therefore said to be on the edge of chaos."

> "In the quiescent phase, the system is completely static, whereas in the active phase, the individual nodes are activated stochastically, and seemingly chaotically. The phase transition point therefore marks the edge of chaos."

Both sentences turn on "therefore", and in both the antecedent is a statement about symmetry or about a quiescent-to-active transition. Neither mentions an exponent, an entropy rate, or a differentiable structure. The second is candid about what is doing the work: activity in the active phase is "*seemingly* chaotically" distributed. This is the identification, and it is verbal.

**One citation-generation later it is a numerical claim.** [Dasgupta, *Cognitive Aging as Interplay between Hebbian Learning and Criticality*, arXiv:1402.0836 (2014)](https://arxiv.org/abs/1402.0836), a fifty-six page thesis-format preprint reached because it is the top search return for the conjunction of the two terms, states it in the exact shape the ticket describes:

> "Analysis of the information transmission shows that critical branching optimizes information throughput [2]. Furthermore the Lyapunov exponent is nearly zero at the critical point, signifying stable neural dynamics, capable of exploring all possible LFP configuration, and yet is not random [21]."

Its reference [21] is Haldeman & Beggs (2005). That paper's own abstract, read from the [PubMed record](https://pubmed.ncbi.nlm.nih.gov/15783702/), does not use the word:

> "When we tune the branching parameter to the critical point, we find that metastable states are most numerous and that network dynamics are not attracting, but neutral."

**"Neutral" has become "the Lyapunov exponent is nearly zero".** That is a real strengthening — "neutral" is a statement about the absence of attraction among metastable states, whereas a near-zero maximal Lyapunov exponent is a claim about the asymptotic separation rate of nearby trajectories on the attractor. The full text of Haldeman & Beggs could not be opened (APS-closed; no open copy in OpenAlex or Semantic Scholar), so this document cannot say that the paper never computes an exponent — only that its abstract does not, and that its abstract is what the strengthened sentence is attached to. That gap is filed as [#131](https://github.com/NGL321/mosaic/issues/131), and no verdict here rests on it.

## 6. Measured together in one model, the two fingerprints come apart

The decisive evidence is not a word count. Kanders, Lorimer and Stoop built a recurrent spiking network specifically to test whether avalanche criticality and edge-of-chaos criticality are the same critical point, and measured both.

[*Avalanche and edge-of-chaos criticality do not necessarily co-occur in neural networks*, Chaos **27** (2017) 047408](https://www.research-collection.ethz.ch/server/api/core/bitstreams/ef6eb5a7-3a0e-4bbc-93a4-6debf5a560cb/content) was read in full, ten pages, from the ETH Research Collection deposit of the AIP version. The premise is stated as an open question, not as settled doctrine:

> "Despite the links that have been drawn between edge-of-chaos and avalanche criticality [18,19] previously, the precise relationship between avalanche and edge-of-chaos criticality is still not settled."

References 18 and 19 are Beggs (2008) and Hesse & Gross (2014) — the two review-prose sources of §5. The result:

> "Based on a realistic paradigm of neural networks, we show that a positive largest Lyapunov exponent—indicating chaotic dynamics of the network—is conserved as we tune the network from subcritical to critical and to supercritical avalanche behavior. This demonstrates that avalanche criticality does not necessarily co-occur with edge-of-chaos criticality."

The network is 128 Rulkov map neurons, 4% connectivity, 80/20 excitatory/inhibitory, tuned across avalanche regimes by a single synaptic scaling parameter W. Avalanche criticality is established to the field's own standard — a power-law size distribution passing a Kolmogorov–Smirnov goodness-of-fit test, collapse of rescaled avalanche shapes, and the exponent relation (τ−1)/(α−1) = γ satisfied. The exponents are computed the careful way, from the Jacobian along the trajectory rather than from a finite perturbation, and the paper says explicitly why that matters:

> "Moreover, such perturbations may be far away from the perturbation limit δ₀ → 0 inherent to the definition of Lyapunov exponents, so that it cannot be excluded that the largest Lyapunov exponent obtained following such approaches, depends on the size of the perturbation."

The [companion conference paper](https://services.ini.uzh.ch/admin/extras/doc_get.php?id=64626), *Neural avalanches at the edge-of-chaos?* (NOLTA2016, 493–496), read in full, gives the numbers in physical units: λ₁ ≈ 18 s⁻¹ for the subcritical **and** the critical network, and λ₁ ≈ 16.5 s⁻¹ for the supercritical one. Every regime is chaotic, and the largest exponent is very slightly *smaller* on the supercritical side — the opposite of the monotone relation the folk claim implies.

**The same paper closes the h_μ half of the question.** Its Lyapunov spectra give the Kolmogorov–Sinai entropy upper bound H = Σ_{λᵢ>0} λᵢ as 28, 46 and 88 s⁻¹ for the subcritical, critical and supercritical networks respectively, and the authors draw the conclusion themselves: "although the supercritical case has a slightly smaller largest Lyapunov exponent, it loses information about a past state at a faster rate." The entropy-rate bound is **monotone increasing in coupling and maximal supercritically**. σ = 1 is not where it turns over, is not where it is maximised, and is not where it vanishes. No source found in this search states a σ ↔ h_μ correspondence, and this measurement is against one.

**Why they come apart is diagnosable, and it is the §3 distinction.** Kanders and Stoop trace the chaos to a source: "the largest Lyapunov exponent of the network essentially captures the dynamics of the intrinsically spiking neuron", the one unit they made fire on its own to seed spontaneous activity. Their networks have a non-quiescent background — and a non-quiescent background is precisely the condition under which "descendant of an activation" and "descendant of a perturbation" stop naming the same event. The two σ's of §3 are the same number only in the silent-background limit, and cortex is not in it.

## 7. What this leaves, and what it does not reopen

Assembling the four ways σ and λ have been related in the sources actually opened:

| Relation claimed | Where | What it actually is |
|---|---|---|
| λ = log[2p(1−p)K], zero at criticality | [Luque & Solé 2000](https://arxiv.org/abs/adap-org/9907001), [Shmulevich & Kauffman 2004](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) | a definition composed with an annealed approximation; λ is a Hamming-distance damage rate for a system the authors say cannot be chaotic in the standard sense |
| criticality at λ = 1 | [Larremore, Shew & Restrepo 2011](https://arxiv.org/abs/1008.0022) | the largest eigenvalue of the adjacency matrix — a linear multiplier at the quiescent fixed point, not an exponent, and equal to one rather than zero |
| σ ≈ 1 is "neutral stability" | [Cayco Gajic & Shea-Brown 2012](https://arxiv.org/abs/1210.8406), Haldeman & Beggs 2005 (abstract) | a statement about non-attraction of the mean-field rate map; no exponent computed |
| "critical states are therefore on the edge of chaos" | [Hesse & Gross 2014](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2014.00166/full) | review prose, zero occurrences of "Lyapunov" |

None of the four is what row 8 of `docs/research/2026-08-02-pesin-and-the-order-axis.md` asked for, and the fourth is what the ticket suspected: *a source that says "σ = 1 is the edge of chaos" without a theorem, which is not a discharge.*

**#123 is therefore discharged as a negative, with the provenance traced.** The correspondence Mosaic borrowed has an ancestor — the RBN identity λ = log s — and the borrowing broke on two joints at once: it swapped a perturbation-descendant count for an activity-descendant count, and it swapped a Hamming-distance divergence rate for the maximal exponent of a smooth flow. `2026-08-02-pesin-and-the-order-axis.md` §3 had already shown, via [Tisseur (2000)](https://arxiv.org/abs/math/0312136) §6.1, that the second swap is not merely unwarranted but false in a published example. This document adds that the first swap is also unwarranted, and that the only direct test of the conjunction in a neural model refutes it.

**The cortical placement question does not reopen.** The ticket's reason for keeping #123 alive was that σ = 1 "remains the only cheap, well-established criticality signature available for neural recordings, and if the correspondence has a real source, the cortical placement question reopens with a usable instrument." The correspondence does not have a real source, so σ is not an instrument for Order. It remains an excellent instrument for what Beggs & Plenz built it to measure — whether a cascade of activity is poised between dying out and running away — and Mosaic should keep it under that description and no other. The withdrawal of the cortex placement drafted in `2026-08-02-pesin-and-the-order-axis.md` *Proposals* §2 stands unchanged; this document adds a sentence naming why σ cannot be repaired into an Order reading, so that the question is not reopened a third time by the same intuition.

---

## What this does not establish

### Sources not reached

Six, and the first three matter. **Haldeman & Beggs (2005)**, Phys. Rev. Lett. 94, 058101, is APS-closed with no open copy reported by OpenAlex or Semantic Scholar; it was reached **by abstract only** through PubMed, and it is the node at which the "Lyapunov exponent is nearly zero" citation chain of §5 terminates. **Beggs (2008)**, Phil. Trans. R. Soc. A 366, 329–343, returns a bot challenge at the publisher and a 404 at the Semantic Scholar "bronze" URL; it is one of the two sources Kanders, Lorimer & Stoop name as drawing the link, and it is unread. Both are filed as [#131](https://github.com/NGL321/mosaic/issues/131), and §5's verdict is stated as a claim about the abstract and about the citing paper, not about either full text. **Bertschinger & Natschläger (2004)**, *Neural Computation* 16, 1413–1436, is behind the MIT Press paywall; §4 substitutes the same three authors' open NIPS companion paper, which shares the model, the mean-field method and the critical-line definition but is not the paper the ticket named, and the substitution is why §4's verdict is about the reservoir line rather than about that article specifically. **Legenstein & Maass (2007)**, *Neural Networks* 20, 323–334, and **Boedecker, Obst, Lizier, Mayer & Asada (2012)**, *Theory in Biosciences* 131, 205–213 — the two reservoir papers that do compute Lyapunov exponents — are both paywalled and were not opened; no verdict rests on either, but neither is ruled out as containing a σ = 1 claim, and the balance of evidence from their own literature (§4) is that they would not. **Rämö, Kesseli & Yli-Harja (2006)**, *J. Theor. Biol.* 242, 164–170, and its 2007 *Physica D* successor, which treat RBN damage spreading explicitly as a branching process, are Elsevier-paywalled; they are the most likely place for someone to have written "σ" and "λ" on the same page in the RBN setting, and this document did not check.

### Open gaps

**Whether Haldeman & Beggs (2005) computes an exponent** is the single unresolved historical question, and it is [#131](https://github.com/NGL321/mosaic/issues/131). **Whether the RBN branching-process papers name the mean-offspring number σ** is untested; if Rämö et al. do, then the two σ's of §3 have been written with the same letter in print, which would explain the confusion more economically than §3's account and would not change any verdict. **Whether σ has any usable relation to h_μ under a stated modelling assumption** — for instance, in the silent-background limit where the two σ's coincide and the network is a Markov chain with a known transition matrix — was not attempted, and is the only route by which σ could become an Order instrument; it would be a derivation, not a citation. **What the entropy rate of a critical branching process actually is** is a classical question this search touched only through Kanders et al.'s numerical KS bound; the branching-process literature proper (Harris, Athreya–Ney) was not searched. **Whether the avalanche and edge-of-chaos transitions coincide in models with quiescent nodes** is left open by Kanders et al. themselves, who note that studies exhibiting both used "rather simple network models, with nodes having no intrinsic dynamics" — which is consistent with §6's diagnosis and is testable.

### Load-bearing ifs

**If the full text of Haldeman & Beggs (2005) does compute a Lyapunov exponent and report it near zero at σ = 1**, then §5's account of the chain is wrong at its last link and the neural side of the correspondence has a real primary source; row 7 would flip and rows 1–3's RBN findings would stand unchanged, but §6's direct measurement would still decouple the two in a network with intrinsic node dynamics. This is the cheapest attack on this document and is why it is filed rather than argued around. **If the word counts are wrong** — if a PDF text layer dropped a section, or "Lyapunov" appears in a figure caption rendered as an image — then every "zero occurrences" claim in §3 and §4 is a claim about an extraction rather than about a paper; the extractions covered the stated page counts and the counts of other words in the same documents came out plausible, but none was checked against a human read of the typeset page. **If Kanders, Lorimer & Stoop's network is not avalanche-critical**, §6 collapses; their evidence is a KS-tested power law, a shape collapse the paper itself calls "rather noisy", and the exponent relation, and the shape collapse is the weak leg. **If "the mean number of descendant bit-flips" and "the mean number of descendant activations" do in fact coincide under conditions cortex satisfies**, then §3's central distinction is idle and σ would be an Order instrument after all; §6 is evidence against, but from one model at N = 128. **If some source outside the four literatures listed in §1 states the correspondence with a proof**, this document's null result is scoped too narrowly to have found it, and §1 is where that scope can be checked.

---

## Verification Debt

One item, filed and open.

- **[#131](https://github.com/NGL321/mosaic/issues/131)** — the two closed-access nodes of the σ-to-Lyapunov citation chain are **unread**. Haldeman & Beggs (2005) was reached by abstract only, and Beggs (2008) not at all; both are APS/Royal-Society closed with no open deposit. §5 traces the numerical claim "the Lyapunov exponent is nearly zero at the critical point" to a citation of the first, whose abstract says "neutral" instead, and Kanders, Lorimer & Stoop name both as places where the link was drawn. The verdicts in this document are stated so as not to depend on either — §2's identity is read from Luque & Solé and Shmulevich & Kauffman directly, and §6's decoupling from a paper opened in full — but the *historical* claim about where the neural-side identification originates is unverified at exactly those two nodes.

This document files no debt against the Order axis itself. [#124](https://github.com/NGL321/mosaic/issues/124), the cortex placement, is **strengthened** rather than reopened by §7: the instrument that might have re-derived it does not exist.

## Proposals

### 1. Add one sentence to the pending `CONTEXT.md` Order entry

The `_Departs_` paragraph proposed in `docs/research/2026-08-02-pesin-and-the-order-axis.md` *Proposals* §1 has not yet landed. It currently ends with the σ sentence: *"Beggs & Plenz's σ = 1 marks the critical point of a branching process — 'the edge of stability' — and their paper makes no claim about exponents, chaos, or entropy rate."* Proposed addition immediately after that sentence:

```markdown
Nor does anyone else's: a deliberate search of the neuronal-avalanche,
reservoir-computing and random-Boolean-network literatures found no source
relating σ to λ_max or to h_μ. The nearest thing is an RBN identity,
λ = log[2p(1−p)K] (Luque & Solé 2000; Shmulevich & Kauffman 2004), in which
"λ" is *defined* as the log of the mean number of descendant bit-flips — a
Hamming-distance damage rate, for a system whose authors state that
deterministic chaos "is not possible", and counting descendants of a
*perturbation* rather than of *activity*. Where both quantities are measured
in one model they come apart: Kanders, Lorimer & Stoop (2017) find a positive
largest Lyapunov exponent conserved across sub-, at- and supercritical
avalanche behaviour, with the Kolmogorov–Sinai entropy bound rising
monotonically with coupling and peaking *supercritically*.
```

The badge for the added material is `⟦T3 · #123⟧`, drafted here and Noah's to apply.

### 2. No change to the cortex withdrawal

`docs/research/2026-08-02-pesin-and-the-order-axis.md` *Proposals* §2 withdraws the cortex placement pending an `h_μ` estimate. That text stands exactly as drafted; this document supplies the reason the withdrawal is not provisional-pending-a-source, because the source was searched for and is not there. No new wording is proposed.

### 3. Nothing to change in the Bound's own text

As with [#98](https://github.com/NGL321/mosaic/issues/98): the Edge of Chaos Bound names none of these estimators, so nothing in it is touched. No amendment to `CHARTER.md`.

---

## Appendix: primary sources, all retrieved 2026-08-02

1. Bartolo Luque & Ricard V. Solé (2000), *Lyapunov exponents in random Boolean networks*, **Physica A 284**, 33–45. Read in full, 16 pages, from the authors' arXiv deposit: [arXiv:adap-org/9907001](https://arxiv.org/abs/adap-org/9907001) (DOI [10.1016/S0378-4371(00)00184-9](https://doi.org/10.1016/S0378-4371%2800%2900184-9)). §2 for the damage-spreading definition of "chaotic"; equations (18), (19), (24) and (27) for the exponent.
2. Ilya Shmulevich & Stuart A. Kauffman (2004), *Activities and Sensitivities in Boolean Network Models*, **Phys. Rev. Lett. 93**, 048701. Read in full from the PubMed Central author manuscript: [PMC1490311](https://pmc.ncbi.nlm.nih.gov/articles/PMC1490311/) (DOI [10.1103/PhysRevLett.93.048701](https://doi.org/10.1103/PhysRevLett.93.048701)). For E[s_f] = K·2p(1−p) and for λ = log E[s_f], citing Luque & Solé as reference [11].
3. Thomas Natschläger, Nils Bertschinger & Robert Legenstein (2004), *At the Edge of Chaos: Real-time Computations and Self-Organized Criticality in Recurrent Neural Networks*, **Advances in Neural Information Processing Systems 17**, 142–152. Read in full, 8 pages, from the NeurIPS proceedings: [proceedings.neurips.cc/paper/2004/hash/f8da71e562ff44a2bc7edf3578c593da](https://proceedings.neurips.cc/paper_files/paper/2004/file/f8da71e562ff44a2bc7edf3578c593da-Paper.pdf). §3 for the critical-line definition and equation (1).
4. Osame Kinouchi & Mauro Copelli (2006), *Optimal dynamical range of excitable networks at criticality*, **Nature Physics 2**, 348–351. Read in full, 6 pages, from the arXiv deposit: [arXiv:q-bio/0601037](https://arxiv.org/abs/q-bio/0601037) (DOI [10.1038/nphys289](https://doi.org/10.1038/nphys289)). For the local branching ratio σ_j and the σ = 1 critical point.
5. Daniel B. Larremore, Woodrow L. Shew & Juan G. Restrepo (2011), *Predicting Criticality and Dynamic Range in Complex Networks: Effects of Topology*, **Phys. Rev. Lett. 106**, 058101. Read in full, 4 pages, from the arXiv deposit: [arXiv:1008.0022](https://arxiv.org/abs/1008.0022) (DOI [10.1103/PhysRevLett.106.058101](https://doi.org/10.1103/PhysRevLett.106.058101)). Equation (2) and the paragraph after it, for criticality as largest eigenvalue λ = 1.
6. John M. Beggs & Nicholas Timme (2012), *Being critical of criticality in the brain*, **Front. Physiol. 3**, 163. Read in full: [PMC3369250](https://pmc.ncbi.nlm.nih.gov/articles/PMC3369250/) (DOI [10.3389/fphys.2012.00163](https://doi.org/10.3389/fphys.2012.00163)). Zero occurrences of "Lyapunov"; "edge of chaos" only inside a cited reference title.
7. Natasha Cayco Gajic & Eric Shea-Brown (2012), *Neutral stability, rate propagation, and critical branching in feedforward networks*. Read in full, 31 pages: [arXiv:1210.8406](https://arxiv.org/abs/1210.8406); published as **Neural Computation 25** (2013), 1768–1806 (DOI [10.1162/NECO_a_00461](https://doi.org/10.1162/NECO_a_00461)). §3 for σ and the "neutrally stable" gloss; §§6–8 for γ_obs against γ_eig.
8. Janina Hesse & Thilo Gross (2014), *Self-organized criticality as a fundamental property of neural systems*, **Front. Syst. Neurosci. 8**, 166. Read in full: [frontiersin.org/articles/10.3389/fnsys.2014.00166/full](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2014.00166/full) (DOI [10.3389/fnsys.2014.00166](https://doi.org/10.3389/fnsys.2014.00166)). The two "therefore … edge of chaos" sentences; zero occurrences of "Lyapunov".
9. Sakyasingha Dasgupta (2014), *Cognitive Aging as Interplay between Hebbian Learning and Criticality*. Read in full, 56 pages: [arXiv:1402.0836](https://arxiv.org/abs/1402.0836). §2.2 for the sentence "the Lyapunov exponent is nearly zero at the critical point", and its reference [21], Haldeman & Beggs (2005). Cited here as the specimen of the claim in circulation, not as an authority for it.
10. Karlis Kanders & Ruedi Stoop (2016), *Neural avalanches at the edge-of-chaos?*, **Proc. NOLTA2016** (Yugawara, Japan), 493–496. Read in full, 4 pages, from the Institute of Neuroinformatics, UZH/ETH: [services.ini.uzh.ch/admin/extras/doc_get.php?id=64626](https://services.ini.uzh.ch/admin/extras/doc_get.php?id=64626). §4 for λ₁ ≈ 18 s⁻¹ across subcritical and critical networks and the KS-entropy bounds of 28/46/88 s⁻¹.
11. Karlis Kanders, Tom Lorimer & Ruedi Stoop (2017), *Avalanche and edge-of-chaos criticality do not necessarily co-occur in neural networks*, **Chaos 27**, 047408. Read in full, 10 pages, from the ETH Zurich Research Collection deposit of the published version: [research-collection.ethz.ch bitstream ef6eb5a7-3a0e-4bbc-93a4-6debf5a560cb](https://www.research-collection.ethz.ch/server/api/core/bitstreams/ef6eb5a7-3a0e-4bbc-93a4-6debf5a560cb/content) (DOI [10.1063/1.4978998](https://doi.org/10.1063/1.4978998)). §I for the "still not settled" framing and references 18–19; §V for the Lyapunov spectra and the entropy bound; the appendix for the Jacobian-based computation.
