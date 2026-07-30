---
ticket: 4
map: 1
date: 2026-07-25
kind: survey
tier: T3
session: unrecorded
sources: 44
debt: [45, 46, 47, 48, 49]
supersedes: null
---

# Survey: grokking, elementary cellular automata, and topological data analysis on neural representations

**Provenance.** Machine-produced, unverified. Every claim below is sourced to a primary
document — paper, official repository, or publisher record — and linked. The load-bearing
papers (Tang et al. 2026; Damrich et al. 2024; Žunkovič & Ilievski 2024) were read past the
abstract; the remainder of §1's mechanistic accounts were read at abstract-and-results depth
and are marked where that matters. None of the derivations has been checked by Noah unaided.
The debt this creates is itemised in *Verification Debt*, below, and is **unfiled** — the
tracker convention that files it did not exist when this document was written.

---

## 0. Verdict

| Sub-question | Verdict | Argued in | One-line reason |
|---|---|---|---|
| Is grokking a stable enough phenomenon to build a rung on? | **Established** | §1.1 | Reproduces widely, and beyond algorithmic data (Omnigrok, ICLR 2023). |
| Is there a settled *mechanism* for it? | **Contested** | §1.2–1.3 | Circuit efficiency, lazy→rich, weight-norm, softmax collapse and local complexity are all live and not obviously reducible to one another. |
| Does the structured representation *cause* generalisation? | **Open** | §1.3 | Liu et al. (2022) assert it; nobody has isolated it. This is the gap the rung sits in. |
| Is there a real grokking result in ECA rule-learning? | **Established** | §2.1 | Žunkovič & Ilievski, JMLR 2024 — analytic, 52 pages, one rule, one non-standard architecture. |
| Is the Wolfram taxonomy "well-characterised" in the sense a categorisation experiment needs? | **Refuted** | §2.3 | Culík & Yu (1988) prove class membership undecidable; assignment depends on the initial-condition ensemble. |
| Has anyone run the ECA compositionality experiment? | **Open** | §2.3 | Nobe & Yura (2023) supply the algebra; nobody has used it as a network probe. Mosaic-shaped gap. |
| Does persistent homology detect grokking? | **Supported, narrowly** | §3.1 | Tang et al. (2026), ρ ≈ 0.77–0.81 on H₁ persistence — and only where the task has cyclic structure. |
| Is Euclidean VR-PH reliable in the regime a Mosaic study would occupy? | **Refuted** | §3.2(c) | Damrich et al. (NeurIPS 2024): no persistent loop found at all for d ≳ 30 under σ = 0.25, with DTM, Fermat and geodesic fixes also failing. Hiraoka et al. (2026) prove HDLSS unreliability. |
| Is the field's track record on this application good? | **Refuted** | §3.2(g) | Two flagship topological measures deflated by careful follow-ups within five years. |
| **Can PH on ECA-grokking representations currently carry a falsifiable claim about compressed representation formation?** | **Refuted** | §4.1 | The only positive precedent depends on a property ECA lacks, and its authors say so. |

> **No — not as the rung is currently specified.** Not "qualified." No. The recommended
> composite is **circuit-efficiency predictions ([Varma et al., 2023](https://arxiv.org/abs/2309.02390))
> as the falsification target, with local intrinsic dimension and effective rank as the
> compression measures**, an ECA-basis progress measure as the mechanistic layer, and
> PH/RTD carried as preregistered exploratory secondaries. That combination is defensible on
> day one and still contains at least two things nobody has done.

---

## 1. Grokking and its mechanistic accounts — **Established** phenomenon, **Contested** mechanism

### 1.1 The phenomenon — **Established**

The phenomenon originates with **[Power, Burda, Edwards, Babuschkin & Misra (2022), "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets," arXiv:2201.02177](https://arxiv.org/abs/2201.02177)** (ICLR 2022 Workshop on Mathematical Reasoning). Small transformers trained on binary-operation tables over finite sets reach perfect training accuracy early, then sit at chance test accuracy for orders of magnitude more optimisation steps before jumping to perfect generalisation. Smaller training fractions require disproportionately more optimisation to generalise.

What is **Established** across the literature:

- The phenomenon is real and reproduces widely on algorithmic tasks.
- It is **not confined to algorithmic data**. [Liu, Michaud & Tegmark, "Omnigrok: Grokking Beyond Algorithmic Data," arXiv:2210.01117](https://arxiv.org/abs/2210.01117) (ICLR 2023) induce grokking on images, language and molecules by manipulating initialisation scale, arguing that train and test loss as functions of weight norm typically resemble an "L" and a "U" respectively, and grokking is the traversal between them.
- It is **not confined to delayed test accuracy**. [Humayun, Balestriero & Baraniuk, "Deep Networks Always Grok and Here is Why," ICML 2024, arXiv:2402.15555](https://arxiv.org/abs/2402.15555) document *delayed robustness* — adversarial robustness emerging long after generalisation — in CNNs on CIFAR-10, measured via the density of the network's spline partition regions ("local complexity"), which undergoes a migration away from training points toward the decision boundary.
- Something structured *does* form in the representations. This is agreed on; what it is and why it forms is not.

### 1.2 The mechanistic accounts, and where they disagree — **Contested**

**Circuit formation / progress measures.** [Nanda, Chan, Lieberum, Smith & Steinhardt, "Progress measures for grokking via mechanistic interpretability," ICLR 2023, arXiv:2301.05217](https://arxiv.org/abs/2301.05217) reverse-engineer a one-layer transformer on modular addition and find it implements addition via discrete Fourier transforms and trigonometric identities — converting addition to rotation about a circle. They define progress measures (restricted and excluded loss, computed via Fourier-space ablations) that vary smoothly where test accuracy jumps, and split training into three phases: **memorisation → circuit formation → cleanup**. Grokking, on this account, is the *cleanup* phase becoming visible in the test metric; the generalising circuit was already forming underneath. Note the paper's own scope restriction: small transformers, modular addition.

**Analytic solution / the circle was always there.** [Gromov, "Grokking modular arithmetic," arXiv:2301.02679](https://arxiv.org/abs/2301.02679) gives closed-form weights for a two-layer MLP with 100% accuracy on modular addition and shows vanilla GD and AdamW find similar feature maps. This is *compatible* with Nanda et al. but relocates the explanandum: the periodic feature map is a natural solution of the loss landscape, not something a "circuit" assembles.

**Circuit efficiency.** [Varma, Shah, Kenton, Kramár & Kumar, "Explaining grokking through circuit efficiency," arXiv:2309.02390](https://arxiv.org/abs/2309.02390) argue grokking occurs when the task admits both a memorising and a generalising solution, the generalising one being slower to learn but more parameter-efficient (larger logits per unit norm). They predict and confirm a **critical dataset size** where the two are equally efficient, and demonstrate two novel behaviours — *ungrokking* (regression from perfect to low test accuracy) and *semi-grokking* (partial delayed generalisation). This is the strongest falsification-flavoured contribution in the grokking literature: it made predictions and they held.

**Lazy → rich transition.** [Kumar, Bordelon, Gershman & Pehlevan, "Grokking as the Transition from Lazy to Rich Training Dynamics," ICLR 2024, arXiv:2310.06110](https://arxiv.org/abs/2310.06110) exhibit grokking in *vanilla GD on polynomial regression with a two-layer net and no regularisation at all*, driven by initial-feature/target misalignment and the rate of feature learning. This is a direct challenge to any account that makes weight decay or explicit regularisation constitutive.

**Representation quality / effective theory.** [Liu, Kitouni, Nolte, Michaud, Tegmark & Williams, "Towards Understanding Grokking: An Effective Theory of Representation Learning," NeurIPS 2022, arXiv:2205.10343](https://arxiv.org/abs/2205.10343) identify four phases — comprehension, grokking, memorisation, confusion — with representation learning confined to a "Goldilocks zone." They make the explicit causal claim that *generalisation originates from structured representations*. **This is the claim closest to Mosaic's rung, and it is the least settled of the accounts.**

**Phase-transition framing.** [Rubin, Seroussi & Ringel, "Grokking as a First Order Phase Transition in Two Layer Networks," ICLR 2024, arXiv:2310.03789](https://arxiv.org/abs/2310.03789) use an adaptive-kernel treatment to argue the post-grokking state is analogous to the mixed phase after a first-order transition, and that grokking is a beyond-lazy/GP feature-learning phenomenon. [Clauw, Stramaglia & Marinazzo (2024), arXiv:2408.08944](https://arxiv.org/abs/2408.08944) (ICML 2024 workshop) attribute it to an emergent transition driven by *synergistic* higher-order interactions among neurons. [Bi, Zhang, Wang & Calhoun (2026), "Grokking as a Falsifiable Finite-Size Transition," arXiv:2603.24746](https://arxiv.org/abs/2603.24746) treat the modulus p as an extensive variable and report finite-size-scaling evidence disfavouring a smooth-crossover reading (ΔAIC = 16.8) — while explicitly leaving **the order of the transition Unresolved**.

**Numerical stability.** [Prieto, Barsbey, Mediano & Birdal, "Grokking at the Edge of Numerical Stability," arXiv:2501.04697](https://arxiv.org/abs/2501.04697) identify *Softmax Collapse* — floating-point breakdown from naïve loss minimisation scaling logits without changing predictions — as an upper bound on unregularised training. Their StableMax and ⊥Grad interventions produce grokking-free generalisation **without regularisation**, which reframes weight decay's role as preventing a numerical pathology rather than as the mechanism.

### 1.3 What is contested — stated plainly

| Question | Status |
|---|---|
| Does grokking happen, robustly, on algorithmic tasks? | **Established.** |
| Does something structured form in the representation before test accuracy moves? | **Established** for modular arithmetic (Nanda et al. 2023; Gromov 2023). |
| Is weight decay / explicit regularisation necessary? | **Contested.** No (Kumar et al. 2024; Prieto et al. 2025). |
| Is grokking a phase transition in the statistical-mechanics sense? | **Contested.** Framed as first-order (Rubin et al. 2024), as a falsifiable finite-size transition of unresolved order (Bi et al. 2026), and as an artefact of measurement/cleanup rather than a transition in the underlying computation (Nanda et al. 2023). |
| Does the structured representation *cause* generalisation, or co-occur with it? | **Open.** Liu et al. (2022) assert causation; nobody has isolated it. This is the gap Mosaic's rung sits in. |
| Is there a single mechanism? | **Contested.** No consensus. Circuit efficiency, lazy→rich, weight-norm/LU, softmax collapse and local-complexity accounts are all live and are not obviously reducible to one another. |

**Implication for Mosaic:** the *phenomenon* is a stable enough platform to build on. The *mechanism* is not — so any rung must be phrased as a claim about an observable, not as a claim that presupposes one of the competing mechanisms. And the specific claim Mosaic wants (structured/compressed representation formation is *the* thing that happens) is precisely the contested item, which is good news for novelty and bad news for ease.

---

## 2. Grokking and rule-learning in elementary cellular automata — **Established** result, **Refuted** premise

### 2.1 The one real reproduction — **Established**

**[Žunkovič, B. & Ilievski, E. (2024), "Grokking phase transitions in learning local rules with gradient descent," *Journal of Machine Learning Research* 25(199), 1–52](https://www.jmlr.org/papers/v25/22-1228.html)** (arXiv:2210.15435). This is the load-bearing paper for the whole ECA leg, and it is a good one — 52 pages, JMLR, with analytic results.

What it actually does:

- Studies a **solvable rule-learning setup** and derives *exact* analytic expressions for critical exponents, grokking probability, and the grokking-time distribution.
- Introduces a **tensor-network map** connecting the setup to standard statistical learning theory, and argues grokking is a consequence of **locality of the teacher model**.
- The architecture is a **tensor-network attention model** (matrix-product-operator style), *not* a standard transformer or MLP.
- The concrete CA instance is **rule 30**, a single Class-III rule; 2-local and 3-local rules appear in an appendix. Rule 30 is expressible as an MPO with bond dimension 4, which is why it is tractable in this framework.
- They report that **sudden spikes in training loss correspond to structural changes in the latent-space representation of the data** — the closest existing statement to Mosaic's rung, in the ECA setting.

**Robustness assessment.** The analytic results are strong and the numerics validate them, but the empirical footprint is narrow: one canonical rule, one non-standard architecture chosen for analytic tractability, and no cross-architecture replication that could be located — see *Sources not reached*. The "locality of the teacher" mechanism is a claim about the *task*, not about transformers specifically, which is a point in its favour for generalisation, but it has not been tested that way.

### 2.2 What else exists, and what it is not — **Established**, and thinner than assumed

- **[Burtsev, M. (2024), "Learning Elementary Cellular Automata with Transformers," arXiv:2412.01417](https://arxiv.org/abs/2412.01417)** (NeurIPS 2024 workshop). 4-layer, 8-head, d_model=512 encoder; 9.5×10⁵ training / 10⁵ test samples via CellPyLib; lattice W=20, radius **r=2** (so ~4.3×10⁹ Boolean functions, *not* the 256 elementary rules), orbit length T=20, with test rules held out from training. Finds high next-state accuracy but sharp degradation on multi-step planning without intermediate context; adding future-state or rule prediction to the loss improves internal rule representations. **No grokking is reported. No Wolfram classes. No mechanistic interpretability.** This is a capability paper, not a dynamics paper.
- **[Rollier, Daly & Baetens (2024), "Convolutional neural networks for automated cellular automaton classification," arXiv:2409.02740](https://arxiv.org/abs/2409.02740).** CNNs classifying ECA space-time diagrams into **Li–Packard** behavioural classes. Its most useful contribution to Mosaic is a methodological warning: earlier deep-learning work on CA classification was in fact "trained to identify the local update rule, rather than directly focus on the mesoscopic patterns" — i.e. the models were solving a different task than advertised, and this had to be corrected with architecture design and augmentation. Any Mosaic ECA experiment inherits this confound.
- **[Zhang et al. (2025), "Intelligence at the Edge of Chaos," ICLR 2025, arXiv:2410.02536](https://arxiv.org/abs/2410.02536)** ([code](https://github.com/vandijklab/Intelligence_at_the_edge_of_chaos)). LLMs pretrained on ECA sequences from different complexity classes, then evaluated on downstream reasoning and chess move prediction. Models trained on **Class IV** rules perform best — intermediate structured complexity beats both trivial and chaotic. This is the closest thing in the literature to "Wolfram classes used for a categorisation experiment," and it is about *pretraining data complexity → downstream capability*, not about compositionality or category formation inside the representation.
- **[Lžičar, M. (2025), "CellARC: Measuring Intelligence with Cellular Automata," arXiv:2511.07908](https://arxiv.org/abs/2511.07908).** 1D multicolour CA as an ARC-style abstraction benchmark; 95k training episodes, interpolation/extrapolation test splits. Notably, it parameterises difficulty by **alphabet size, radius, rule family, Langton's λ, and cellular entropy — and does not use Wolfram classes at all.** A serious benchmark designer, building precisely the categorisation instrument Noah has in mind, chose a continuous complexity parameter over the Wolfram taxonomy.
- **[Aach, Goebbert & Jitsev (2021), "Generalization over different cellular automata rules learned by a deep feed-forward neural network," arXiv:2103.14886](https://arxiv.org/abs/2103.14886)** (CSCE 2021 / Springer) — deep conv encoder–decoder nets learn CA rules and show partial generalisation to unseen configurations and, to a limited extent, to unseen rule sets and neighbourhood sizes. Also the Neural Cellular Automata line (Mordvintsev et al. and successors) exist but concern learned update rules and morphogenesis, not delayed generalisation.

### 2.3 Testing Noah's belief: is the ECA rule taxonomy uniquely suited? — **Refuted**

The belief under test: *"the well-characterised rule taxonomy makes ECA uniquely suited to compositionality and categorisation experiments."*

**The literature is thinner than expected, and the premise is weaker than stated.** Three findings:

1. **Nobody has done the compositionality experiment — Open.** There is a formal study of ECA composition as an algebraic object — [Nobe & Yura, "A study on the composition of elementary cellular automata," arXiv:2305.02947](https://arxiv.org/abs/2305.02947), which classifies the 256 rules by their behaviour under composition and finds that more complex rules tend to have fewer left/right companions. That is a *mathematical* result about the rule space. No one has used it as a neural-network compositionality probe. This is a genuine gap, and it is Mosaic-shaped.

2. **The Wolfram taxonomy is not decidable, and is therefore not "well-characterised" in the sense a categorisation experiment needs — Refuted.** [Culík & Yu (1988), "Undecidability of CA Classification Schemes," *Complex Systems* 2, 177–190](https://www.semanticscholar.org/paper/Undecidability-of-CA-Classification-Schemes-Cul%C3%ADk-Yu/c754b39540f79fd542f4e067ab7436b720605192) formalise the Wolfram classes and prove that **which class a given CA belongs to is undecidable**. Class IV in particular has no quick test distinguishing it from Class III ([Eppstein, "Wolfram's Classification of Cellular Automata"](https://ics.uci.edu/~eppstein/ca/wolfram.html)); gliders — the supposed Class-IV signature — have been found in rules that would be classified into each of the four classes. Worse for experimental design: **class assignment depends on the set of initial conditions used**, because the classification is defined on evolution from disordered states.

   For the 256 elementary rules specifically, published class assignments *are* conventional and mostly agreed — so an experiment can use them as labels. But they are **conventional labels on a provably undecidable predicate**, not ground truth. A claim of the form "the network forms a compressed representation aligned with Wolfram class" is then partly a claim about the convention. That has to be stated up front or the result is unfalsifiable in a hidden way.

3. **The field has partially moved on — Established.** Li–Packard classes (Rollier et al. 2024), Langton's λ and cellular entropy (Lžičar 2025), and Hamming-distance-based classification ([arXiv:2407.06175](https://arxiv.org/abs/2407.06175)) are all in use as better-behaved alternatives. Wolfram's classes survive as vocabulary, less as a measurement instrument.

**Verdict on the belief:** ECA remains a *good* substrate — small, exhaustively enumerable (256 rules), locally specified, with a genuine complexity gradient and a real grokking result attached to it (Žunkovič & Ilievski 2024). But the specific reason offered — a well-characterised taxonomy — does not hold up. If Mosaic wants a graded categorisation axis, **Langton's λ or the composition-algebra structure of Nobe & Yura (2023) are defensible; the four Wolfram classes are a convention that will draw a referee's first question.**

---

## 3. TDA and persistent homology on neural representations — **Supported** narrowly, **Refuted** in Mosaic's regime

This is the section that decides the rung, so it gets the most space and the most adversarial reading.

### 3.1 What has been done — **Supported**, in the presence of cyclic structure

**Foundational.** [Naitzat, Zhitnikov & Lim, "Topology of Deep Neural Networks," *JMLR* 21(184), 1–40, 2020](https://jmlr.org/papers/v21/20-345.html) show that data manifolds passing through a well-trained network undergo a vast reduction in Betti numbers, nearly always to their lowest possible values — and that reduction is much faster for ReLU (non-homeomorphic, changes topology) than tanh (homeomorphic, preserves it). This is the canonical "networks simplify topology" result and the strongest positive precedent for reading representation formation topologically.

**Complexity and generalisation measures.**
- [Rieck et al., "Neural Persistence," ICLR 2019, arXiv:1812.09764](https://arxiv.org/abs/1812.09764) — a topological complexity measure on the weighted stratified graph of a fully-connected layer, proposed as an early-stopping criterion needing no validation set.
- [Birdal, Lou, Guibas & Şimşekli, "Intrinsic Dimension, Persistent Homology and Generalization in Neural Networks," NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/35a12c43227f217207d4e06ffefe39d3-Abstract.html) ([code](https://github.com/tolgabirdal/PHDimGeneralization)) — bounds generalisation via the PH-dimension of the optimisation trajectory.
- [Corneanu, Escalera & Martinez, "Computing the Testing Error without a Testing Set," CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/html/Corneanu_Computing_the_Testing_Error_Without_a_Testing_Set_CVPR_2020_paper.html) — topological summaries of functional network graphs to estimate the generalisation gap. CVPR best-paper finalist.
- [Pérez-Fernández et al., "Persistent Homology Captures the Generalization of Neural Networks Without A Validation Set," arXiv:2106.00012](https://arxiv.org/abs/2106.00012).

**Representation comparison and interpretability.**
- [Barannikov, Trofimov, Balabin & Burnaev, "Representation Topology Divergence," ICML 2022](https://proceedings.mlr.press/v162/barannikov22a.html) ([code](https://github.com/IlyaTrofimov/RTD)) — multi-scale topological dissimilarity between two point clouds with point correspondence, possibly in different ambient spaces. One of the few TDA methods the authors themselves describe as practical on real ML datasets.
- [Gourgoulias et al., "Estimating class separability of text embeddings with persistent homology," *TMLR* 2024, arXiv:2305.15016](https://arxiv.org/abs/2305.15016) — tracks embedding-manifold evolution during training as an unsupervised separability proxy.
- [Gebhart, Schrater & Hylton (2019), "Characterizing the Shape of Activation Space in Deep Neural Networks," arXiv:1901.09496](https://arxiv.org/abs/1901.09496).
- [Ballester, Casacuberta & Escalera, "Topological Data Analysis for Neural Network Analysis: A Comprehensive Survey," arXiv:2312.05840](https://arxiv.org/abs/2312.05840) — 70pp survey organising the field into architecture characterisation, decision boundaries, internal representations/parameters, and training dynamics. The best single map of the area.

**And the one that matters most here:**

**[Tang, Y., Wang, Q., García-Redondo, I. & Monod, A. (2026), "Topological Signatures of Grokking," arXiv:2605.06352](https://arxiv.org/abs/2605.06352)** (7 May 2026, preprint). This is, essentially, Mosaic's proposed experiment already run on modular arithmetic. Its methods section is worth reading in full because it is the template a Mosaic study would have to beat:

- **Task:** (a+b) mod p, p ∈ {113, 149, 197}; training fraction α ∈ {0.20, 0.25, 0.30}.
- **Architectures:** 2-layer transformer encoder (d_model=128, 4 heads, d_attn=32, d_ff=256) and a 3×512 MLP (d_embed=128, GELU).
- **Point clouds:** rows of the token embedding matrix (p points in 128 dims), and second-token hidden states per encoder layer (subsampled to 2,000 points). Centred and normalised before PH.
- **Filtration:** Vietoris–Rips, Euclidean, via Ripser. H₀ and H₁.
- **Statistics:** 5 seeds (46–50), 60,000 steps, checkpoints every 500, ±1 SD shading, Spearman rank correlations against test accuracy.
- **Result:** a sharp rise in **maximum and total H₁ persistence** at the grokking transition; ρ = +0.77 ± 0.03 (H₁ max, embedding layer), up to ρ = 0.81 at layer 1; H₀ total anti-correlates at ρ = −0.75 ± 0.03. Local intrinsic dimension (TwoNN) shows the inverse pattern — rising during memorisation, dropping at generalisation.
- **Control:** label permutation. Up to P_frac ≤ 10% the model still groks; at P_frac ≥ 20% it does not generalise **and the PH–accuracy correlations largely disappear.** This is a real control and it does the work asked of it.
- **Cost:** ~2 minutes per model for CPU Vietoris–Rips at these sizes.
- **Their stated limitation, verbatim:** *"While the observed topological transitions are clear in modular arithmetic, the behavior on MNIST is substantially more diffuse, suggesting that interpretable global topological structure may depend strongly on the underlying geometry of the task. More broadly, PH provides descriptive geometric summaries rather than mechanistic explanations of learning dynamics."*
- On MNIST specifically: H₁ max rises **gradually with no sharp transition**, **no dominant long-lived H₁ feature emerges**, and H₁ total peaks early then declines. The authors attribute this to the absence of underlying cyclic structure in natural images.

Two things follow immediately. First, the instrument works **where the task has a group structure whose Cayley geometry is a loop**. Second, **the authors report no null model or barcode-significance test at all** — no random-point-cloud baseline, no confidence bands, no bootstrap. Their evidence is a correlation across seeds plus a permutation ablation. That is more than most TDA-on-networks papers do, and still not enough to call a barcode feature statistically real.

### 3.2 The methodological hazards, itemised — **Refuted** as a reliable instrument in this regime

#### (a) Sensitivity to choice of filtration — **Established**

[Turkeš, Montúfar & Otter, "On the Effectiveness of Persistent Homology," NeurIPS 2022, arXiv:2206.10551](https://arxiv.org/abs/2206.10551) is the most careful positive study of PH's capabilities — and its cautions are the useful part. They note that "depending on the task, there are many other filtration functions one could choose, such as rank, height, radial, erosion, dilation" and that "the resulting PH captures completely different information about the cycles." For convexity detection they report the pipeline "makes a wrong prediction when concavity is barely pronounced, or if it is missed by the selected tubular filtration lines," and that PH on a plain distance filtration "is very sensitive to outliers," forcing a switch to Distance-to-Measure. They also flag that "the hyperparameter tuning of the PH pipeline does take time," and scope their conclusions to three problems with no state-of-the-art comparison.

The operational consequence: **filtration choice is a researcher degree of freedom large enough to determine the result.** A study that picks the filtration after seeing the data has produced nothing.

#### (b) Sensitivity to choice of metric on representation space — **Established**, and constitutive for Mosaic

PH is computed from a distance matrix. Everything downstream inherits the metric. In activation space there is no canonical choice: Euclidean, cosine, correlation, Mahalanobis under the empirical covariance, and geodesic distance on a k-NN graph all give different barcodes, and the literature contains defences of several. This is not a solved problem, and it is a live problem for Mosaic specifically, because **the Hard Core claim is that inference engines are constrained to their own metric spaces** — meaning the choice of metric is not a nuisance parameter for this programme, it is *part of the object of study*. Using PH here quietly assumes an answer to the question the programme exists to ask.

[Damrich, Berens & Kobak (NeurIPS 2024)](https://arxiv.org/abs/2311.03087) is the sharpest evidence that the metric is decisive rather than incidental: on the same data, Euclidean VR-PH fails while spectral distances (diffusion distance, effective resistance) succeed.

#### (c) Behaviour under noise and finite sampling — **Refuted**, and this is the decisive hazard

Two independent papers, both post-2023, both damaging.

**[Damrich, S., Berens, P. & Kobak, D., "Persistent Homology for High-dimensional Data Based on Spectral Methods," NeurIPS 2024, arXiv:2311.03087](https://arxiv.org/abs/2311.03087)** ([code](https://github.com/berenslab/eff-ph)). When data lie on a low-dimensional manifold in a high-dimensional ambient space and noise affects all ambient dimensions, traditional PH "is not robust against even low levels of noise." Concretely, for a noisy circle with σ = 0.25: performance degrades noticeably from d ≈ 20, and **for d ≳ 30 no persistent loop is found at all using Euclidean distances**; at d = 50 detection fails completely. Critically, **the standard robustness fixes also fail**: Distance-to-Measure "collapsed at σ ≈ 0.15" and performed *worse* than plain Euclidean on the ℝ⁵⁰ noisy circle; Fermat distances "did not have any effect"; core distance and k-NN geodesics gave "only modest improvement," and a single spurious graph edge across the circle destroys the feature early. The paper states flatly that "the same holds true for existing refinements of persistent homology." Only spectral distances recovered the topology.

**[Hiraoka, Y., Imoto, Y., Kanazawa, S. & Liu, E., "Curse of Dimensionality on Persistence Diagrams," *Foundations of Data Science*, 2026 (arXiv:2404.18194)](https://arxiv.org/abs/2404.18194).** Proves the asymptotic behaviour of persistence diagrams for high-dimensional random data in the HDLSS regime, establishing that persistence diagrams **cease to be reliable descriptors** of low-sample-size data under high-dimensional noise perturbation — notwithstanding the stability theorem. Their partial mitigation is normalised PCA before PH.

Note carefully what this pair implies about the one on-point precedent: **Tang et al. (2026) compute Euclidean Vietoris–Rips PH on ~113–197 points in 128 dimensions.** That is d ≫ 30 and n ≈ d — the exact intersection of both failure regimes. Their signal is strong and their control is real, so the finding is probably not an artefact; but no reader with these two papers in hand can accept the barcode as a reliable topological measurement rather than a useful correlate, absent a null model.

#### (d) Statistical significance of barcodes, and what null models exist — **Established**, and almost never used

- **[Fasy, Lecci, Rinaldo, Wasserman, Balakrishnan & Singh, "Confidence sets for persistence diagrams," *Annals of Statistics* 42(6), 2301–2339, 2014](https://projecteuclid.org/journals/annals-of-statistics/volume-42/issue-6/Confidence-sets-for-persistence-diagrams/10.1214/14-AOS1252.full)** — the canonical construction separating topological signal from topological noise via confidence bands on the diagram.
- **[Chazal, Fasy, Lecci, Michel, Rinaldo & Wasserman, "Subsampling Methods for Persistent Homology," ICML 2015](https://proceedings.mlr.press/v37/chazal15.html)** — subsample, compute, combine; proven to retain stable topological information at a large computational saving.
- **[Bobrowski, O. & Skraba, P., "A universal null-distribution for topological data analysis," *Scientific Reports* 13, 2023](https://www.nature.com/articles/s41598-023-37842-2)** (arXiv:2207.03926) — persistence values from random point clouds appear to follow a universal law, enabling per-feature significance values. The authors are explicit that this is **conjectural**, supported by simulation rather than proof, and that the distribution of persistence diagrams "is largely an open problem."
- **[Vishwanath, Sriperumbudur, Fukumizu & Kuriki, "Adversarially Robust Topological Inference," arXiv:2206.01795](https://arxiv.org/abs/2206.01795)** — establishes that although PH is stable under Hausdorff perturbation, it is "highly sensitive to outliers," so the stability theorem is *not* the practical guarantee it is usually cited as; they propose a median-of-means distance with near-minimax guarantees under contamination.

The gap between what statistical TDA makes available and what applied neural-network TDA papers actually use is the single largest credibility problem in this literature.

#### (e) Curse of dimensionality in activation space — **Established**

Covered above (Hiraoka et al. 2026; Damrich et al. 2024). Two additional notes. Euclidean pairwise distances concentrate in high dimension, compressing the range that PH filtrations sweep. And the "helpful" fix — projecting to low dimension first — is itself a filtration choice that can create or destroy loops. Normalised PCA (Hiraoka et al.) is the only principled mitigation with a supporting analysis, and it is partial.

#### (f) Computational cost at realistic layer widths — **Refuted** as a binding constraint

Cost scales with the number of *points*, not the ambient dimension. Vietoris–Rips complex construction is exponential in the number of points in the worst case; [Bauer, "Ripser: efficient computation of Vietoris–Rips persistence barcodes," *Journal of Applied and Computational Topology*, 2021](https://link.springer.com/article/10.1007/s41468-021-00071-5) achieves large practical speedups via implicit coboundary representation, clearing, emergent pairs and cohomology, but does not change the asymptotics. [giotto-ph (Burella Pérez et al., arXiv:2107.05412)](https://arxiv.org/abs/2107.05412) parallelises it.

Practically: a few thousand points with H₀/H₁ is routine (Tang et al. report ~2 minutes/model, and subsample hidden states to 2,000 points precisely because of this). H₂ and above at those sizes is expensive. **Cost is not the binding constraint for a Mosaic-scale study.** Subsampling to make it cheap, however, reintroduces the finite-sampling hazard in (c), and any subsampling must be reported with a variance estimate across draws.

#### (g) The reproducibility record on this specific application — **Refuted**

This is where the honest answer is worst.

- **Neural persistence was substantially deflated by follow-up work.** [Girrbach, Christensen, Winther, Akata & Akata, "Addressing caveats of neural persistence with deep graph persistence," TMLR 2023, arXiv:2307.10865](https://arxiv.org/abs/2307.10865) ([code](https://github.com/ExplainableML/Deep-Graph-Persistence)) find that "the variance of network weights and spatial concentration of large weights are the main factors that impact neural persistence," that in deeper layers neural persistence is **"roughly equivalent to the variance of weights"**, and that "no relevant spatial structure is present in later layers of deep neural networks." They also fault the cross-layer averaging for ignoring layer interactions. In other words: the flagship topological complexity measure for neural networks turned out, in the regime that matters, to be a re-parameterisation of a weight statistic.
- **PH-dimension as a generalisation measure was substantially deflated by follow-up work.** [Tan, García-Redondo, Wang, Bronstein & Monod, "On the Limitations of Fractal Dimension as a Measure of Generalization," NeurIPS 2024, arXiv:2406.02234](https://arxiv.org/abs/2406.02234) report confounding between the observed generalisation–topology correlation and hyperparameter variation; failure to predict generalisation for models trained from poor initialisations; and **model-wise double descent in the topological measures themselves**. They call explicitly for investigation of causal rather than correlational relationships before these measures are trusted.

Note who wrote that last paper: García-Redondo, Wang and Monod — three of the four authors of *Topological Signatures of Grokking*. The group best positioned to run the TDA-on-grokking experiment is also the group that published the strongest negative result on TDA generalisation measures. That is a good sign about *their* work and a bad sign about the field's prior track record.

There is **no negative-results or replication literature** on TDA-for-neural-representations comparable to what exists in, say, the saliency-map literature. What exists instead is a pattern: enthusiastic measure → adopted → deflated by one careful follow-up two to five years later. Two data points is not a law, but it is the base rate a Mosaic study is arguing against.

Positive counterweight, for fairness: [Turkeš et al. (NeurIPS 2022)](https://arxiv.org/abs/2206.10551) show PH genuinely outperforming strong baselines including PointNet on hole-counting, curvature and convexity, and remaining effective under limited compute, limited training data, and out-of-distribution test data. When the task really is about shape, and the filtration is chosen for that shape, PH earns its place.

---

## 4. Implications for the first rung — **Refuted** as specified

### 4.1 Can PH on ECA-grokking representations currently support a falsifiable claim about compressed representation formation?

**No — not as the rung is currently specified.** Not "qualified." No.

Three reasons, in order of severity:

**(i) The positive precedent does not transfer, and its authors say so.** The entire evidential basis for "PH detects grokking" is [Tang et al. (2026)](https://arxiv.org/abs/2605.06352), whose signal is a sharp rise in H₁ persistence — a *loop* — reflecting the cyclic structure of Z_p. In the same paper, on MNIST, the signature becomes diffuse, no dominant long-lived H₁ feature emerges, and the sharp transition disappears. Their stated diagnosis is that "interpretable global topological structure may depend strongly on the underlying geometry of the task."

ECA rule-learning has no cyclic structure. The learned object is a Boolean function on a neighbourhood — points live on or near a hypercube, and the natural representational geometry is combinatorial, not circular. There is no published reason to expect a long-lived H₁ class, and one published reason (the MNIST result) to expect none. **A Mosaic study would therefore be predicting a signal whose only known instance depends on a property its task lacks.** If the study runs and finds nothing, that outcome is uninformative — it is consistent with "no compressed representation formed" and equally consistent with "PH cannot see this kind of compression." An experiment whose null result has two incompatible readings is not falsifying anything.

**(ii) The measurement regime is inside two proven failure regimes.** Activation point clouds from a small ECA model would be O(10²–10³) points in O(10²) dimensions. [Damrich et al. (NeurIPS 2024)](https://arxiv.org/abs/2311.03087) show Euclidean VR-PH failing to find a *known, planted* loop at d ≳ 30 under modest noise, with DTM, Fermat and geodesic refinements all failing too. [Hiraoka et al. (2026)](https://arxiv.org/abs/2404.18194) prove persistence diagrams stop being reliable descriptors in exactly the HDLSS regime this study would occupy. Any barcode Mosaic produces will be attackable on these grounds unless the design pre-empts them.

**(iii) The field's track record on this exact application is two-for-two against.** Neural persistence reduced to weight variance ([Girrbach et al., 2023](https://arxiv.org/abs/2307.10865)); PH-dimension-as-generalisation-measure shown to be confounded and to exhibit double descent ([Tan et al., NeurIPS 2024](https://arxiv.org/abs/2406.02234)). A newcomer proposing a third topological measure of a training phenomenon is, correctly, going to be asked which weight statistic it reduces to. **That question must be answered in the design, not in the discussion.**

**What *is* currently supportable.** A weaker, genuinely falsifiable claim is available: *"in ECA rule-learning, a specified representational statistic changes discontinuously at the grokking transition, and this change is absent under label permutation and absent in matched non-grokking runs."* That claim is defensible today. Whether the statistic should be a barcode summary is the open question — and on current evidence, it should not be the *primary* one.

### 4.2 Methodological commitments a defensible study would have to make up front

Non-negotiable, all pre-registered before any data is seen:

1. **Preregistration.** Analysis plan, filtration, metric, homology dimensions, summary statistic, null model, and decision rule frozen and timestamped (OSF or a signed commit in this repo) before training runs. This is the single highest-leverage commitment available, because the dominant threat is researcher degrees of freedom, not compute.
2. **Filtration: declared and justified in advance.** Vietoris–Rips on H₀/H₁ is the default; if chosen, state that it is chosen for comparability with [Tang et al. (2026)](https://arxiv.org/abs/2605.06352) and not because it worked. Any post-hoc filtration change is a new experiment with a new preregistration.
3. **Metric: declared, and *varied as a designed factor*.** At minimum Euclidean, cosine, and a spectral distance (diffusion distance or effective resistance per [Damrich et al. 2024](https://github.com/berenslab/eff-ph)). Because the Hard Core treats the metric as constitutive of an inference engine, metric-dependence of the result is a *finding*, not a robustness check to bury. Report all three.
4. **Dimensionality control.** Apply normalised PCA before PH as recommended by [Hiraoka et al. (2026)](https://arxiv.org/abs/2404.18194), and report results with and without. State the ambient dimension and sample size explicitly next to every diagram.
5. **Null model — mandatory, and the thing that most distinguishes a defensible study from the existing literature.** At least two of:
   - per-feature significance under the universal null of [Bobrowski & Skraba (2023)](https://www.nature.com/articles/s41598-023-37842-2), flagged as conjectural;
   - confidence bands per [Fasy et al. (2014)](https://projecteuclid.org/journals/annals-of-statistics/volume-42/issue-6/Confidence-sets-for-persistence-diagrams/10.1214/14-AOS1252.full);
   - a matched random-point-cloud baseline (same n, same d, same empirical covariance) and a shuffled-activation baseline.

   Points near the diagonal are not automatically noise and must not be discarded by unstated thresholding.
6. **The reduction check.** Regress the topological statistic on the obvious scalar confounds — weight norm, weight variance, activation variance, local intrinsic dimension, and effective rank — and report the residual predictive content. If the barcode summary is a re-parameterisation of weight variance, say so. This is the check that [Girrbach et al. (2023)](https://arxiv.org/abs/2307.10865) applied *to someone else's measure*; applying it to your own is cheap insurance and a credibility signal.
7. **Sample size and variance.** ≥ 10 seeds per condition (Tang et al. used 5, which is thin), full checkpoint traces, bootstrap CIs across seeds, and subsampling variance reported wherever point clouds are subsampled ([Chazal et al., ICML 2015](https://proceedings.mlr.press/v37/chazal15.html)).
8. **Controls.** Label permutation at graded levels (following Tang et al.'s P_frac design), plus non-grokking matched runs, plus at least one rule the model fails to learn.
9. **Task-confound control specific to ECA.** [Rollier et al. (2024)](https://arxiv.org/abs/2409.02740) showed that CA models can be secretly solving rule-identification rather than the advertised task. Hold out rules from training as [Burtsev (2024)](https://arxiv.org/abs/2412.01417) does, and verify what the model is actually keying on.
10. **Vocabulary honesty on Wolfram classes.** If class labels are used, state that class membership is undecidable in general ([Culík & Yu, 1988](https://www.semanticscholar.org/paper/Undecidability-of-CA-Classification-Schemes-Cul%C3%ADk-Yu/c754b39540f79fd542f4e067ab7436b720605192)), that the labels for the 256 elementary rules are conventional, and that they depend on the initial-condition ensemble. Prefer Langton's λ or the composition algebra of [Nobe & Yura (2023)](https://arxiv.org/abs/2305.02947) as the continuous axis.
11. **Full artefact release.** Seeds, checkpoints, distance matrices, barcodes, and analysis code. Given the field's record, an unreleased TDA result should not be believed, including Mosaic's.

### 4.3 Alternative and complementary instruments for the same rung — **Supported**

Ranked on defensibility versus novelty.

| Instrument | Defensibility | Novelty | Notes |
|---|---|---|---|
| **Restricted / excluded loss (Fourier-style progress measures)** — [Nanda et al., ICLR 2023](https://arxiv.org/abs/2301.05217) | **High.** Established, ablation-validated, mechanistically interpretable. | **Low** on modular arithmetic; **moderate** if the analogue is constructed for a Boolean/ECA basis, which nobody has done. | The right *primary* instrument. Constructing the ECA analogue — a basis in which the generalising ECA circuit is sparse, then ablating everything else — is real work and a real contribution. |
| **Circuit-efficiency predictions: critical dataset size, ungrokking, semi-grokking** — [Varma et al., 2023](https://arxiv.org/abs/2309.02390) | **High.** These are *predictions*, and testing whether they hold in ECA rule-learning is a clean falsification target. | **Moderate–high.** Untested outside algorithmic arithmetic. | Cheapest genuinely falsifiable rung available. Strongly recommended as the *first* experiment regardless of what else is run. |
| **Local intrinsic dimension (TwoNN / MLE)** | **High.** Cheap, standard, well-understood estimators. | **Low–moderate.** | [Tang et al. (2026)](https://arxiv.org/abs/2605.06352) find LID moves *inversely* to H₁ persistence across grokking. This is the most direct available operationalisation of "compression," and it is far more defensible than a barcode. Should be in any design as the baseline the topological measure must beat. |
| **Effective rank / participation ratio of activations** | **High.** Trivial to compute, hard to argue with. | **Low.** | The confound any topological claim must be regressed against (see §4.2.6). |
| **Local complexity / spline-partition density** — [Humayun et al., ICML 2024](https://arxiv.org/abs/2402.15555) | **Moderate–high.** Published, ICML, works on real CNNs. | **High** in ECA — untried. | Measures compression of the input–output map rather than of the representation. Different, complementary claim. |
| **Information-theoretic: synergy / redundancy, transfer entropy, O-information** — [Clauw et al., 2024](https://arxiv.org/abs/2408.08944); [Pomarico et al., 2025](https://arxiv.org/abs/2507.23346) | **Moderate.** Estimator bias in high dimensions is a serious, well-known problem. | **High.** | Conceptually closest to Mosaic's Hard Core (a *network* of inference engines, so inter-engine information flow is the natural observable). Worth a rung of its own later. |
| **Representation Topology Divergence** — [Barannikov et al., ICML 2022](https://proceedings.mlr.press/v162/barannikov22a.html) | **Moderate.** Peer-reviewed, coded, comparative rather than absolute. | **Moderate.** | Better-behaved than raw barcodes because it compares two point clouds with correspondence rather than asserting absolute topology. If TDA is used at all, **this is the more defensible form of it.** |
| **Persistent homology of activation point clouds (the proposed rung)** | **Low, currently.** See §4.1. | **High.** | Keep it as a *secondary, exploratory* measure with preregistered nulls. Do not make the rung depend on it. |
| **Tensor-network / MPS analysis of the ECA learner** — [Žunkovič & Ilievski, JMLR 2024](https://www.jmlr.org/papers/v25/22-1228.html) | **High** for ECA specifically — it is the one analytically solved account of grokking in rule-learning. | **Moderate.** | Entanglement entropy across the chain is a principled compression measure with an exact theory behind it. Underexploited, and directly aimed at the "locality of the teacher" mechanism. |

---

## What this does not establish

### Sources not reached

- **Cross-architecture replication of Žunkovič & Ilievski (2024).** Searched and not found; the claim in §2.1 is that none *could be located*, which is weaker than none existing. A reader who finds one falsifies §2.1's robustness assessment, not its analytic content.
- **Culík & Yu (1988) was reached through a Semantic Scholar record, not the *Complex Systems* original.** The undecidability result is stated in the record and is uncontroversially cited elsewhere, but the proof was not read. §2.3's second finding rests on a secondary reading and is the weakest-sourced load-bearing claim in the document.
- **Eppstein's course page** is a lecture note, not a primary source. It is cited in §2.3 for the Class-III/IV indistinguishability remark, which is corroborated by Culík & Yu but is not independently sourced here.
- **The Li–Packard classification's original paper** was not reached; §2.3's third finding uses Rollier et al. (2024) as its source for what Li–Packard classes are.
- **Hiraoka et al. (2026) was read at theorem-statement depth.** The asymptotic proof was not followed. Whether the HDLSS regime the theorems describe is exactly the regime a Mosaic ECA study would occupy is an inference made here, not a claim the paper makes about this application.

### Open gaps

These are places a careful newcomer could contribute something real. They are the most valuable output of this survey, and the first is more valuable than the recommendation it sits under.

1. **A progress-measure basis for Boolean/local-rule learning.** Nanda et al.'s method depends on knowing the right basis (Fourier, for Z_p). The analogue for ECA — presumably Walsh–Hadamard over the neighbourhood, or the composition algebra of [Nobe & Yura (2023)](https://arxiv.org/abs/2305.02947) — has not been constructed. Doing so would make the mechanistic-interpretability toolkit usable on an entire second task family. **This is the highest-value gap identified in this survey.**
2. **Testing the circuit-efficiency predictions outside modular arithmetic.** Critical dataset size, ungrokking and semi-grokking ([Varma et al., 2023](https://arxiv.org/abs/2309.02390)) have not been tested on ECA rule-learning. Clean, cheap, genuinely falsifiable, and interesting whichever way it comes out.
3. **Neural compositionality over the ECA composition algebra.** [Nobe & Yura (2023)](https://arxiv.org/abs/2305.02947) give the mathematical structure; nobody has asked whether a network that has learned rules A and B represents A∘B compositionally. This is directly a *compressed-representation-of-a-concept* question and it is wide open.
4. **Does the Žunkovič–Ilievski locality mechanism survive a change of architecture?** Their result is analytic on a tensor-network attention model. Whether standard transformers on the same task show the same critical exponents and grokking-time distribution is an unanswered, well-posed replication question with a quantitative prediction attached.
5. **A null-model-equipped TDA study of neural representations.** Nobody in this application area is using [Fasy et al. (2014)](https://projecteuclid.org/journals/annals-of-statistics/volume-42/issue-6/Confidence-sets-for-persistence-diagrams/10.1214/14-AOS1252.full) confidence bands or [Bobrowski & Skraba (2023)](https://www.nature.com/articles/s41598-023-37842-2) per-feature significance. A paper whose contribution is *"here is what survives when you apply proper statistical TDA to the existing claims"* would be valuable, is squarely within a returning undergraduate's reach, and fits Mosaic's warrant discipline exactly. It would also very likely be a negative result — which, per the Positive Heuristic, is fine.
6. **Metric-dependence as an object of study rather than a nuisance.** Recomputing the [Tang et al. (2026)](https://arxiv.org/abs/2605.06352) grokking signature under Euclidean, cosine, and spectral distances, and reporting where it survives, is a small paper that speaks directly to Mosaic's Hard Core claim about representation-constrained metric spaces. Very few people have both the motivation and the framing to care about this; Noah does.
7. **Whether the H₁ grokking signature is a re-parameterisation of a scalar.** Nobody has regressed it against weight variance, effective rank and LID. Given the precedent of [Girrbach et al. (2023)](https://arxiv.org/abs/2307.10865), someone should, and it takes days rather than months.

### Load-bearing ifs

The claims whose falsity would move the verdict. Each is cheap for a later reader to attack, which is the point of listing them.

- **If ECA rule-learning representations do carry a cyclic structure** — from the periodicity of the rule table under some natural group action, say — then §4.1(i) collapses and PH becomes a live primary instrument again. Nothing here rules this out; the claim is that no published reason to expect it exists.
- **If a spectral distance recovers loops reliably in the O(10²) points / O(10²) dims regime**, §4.1(ii)'s force drops from "inside two proven failure regimes" to "inside one, with a known mitigation." Damrich et al. show spectral distances succeeding where Euclidean fails, but not at Mosaic's n.
- **If Tang et al. (2026) survives peer review with a null model added**, the "not enough to call a barcode feature statistically real" judgement in §3.1 weakens. It is a preprint as retrieved.
- **If the two deflation results (§3.2(g)) are the base rate of a young field rather than of TDA specifically**, the track-record argument in §4.1(iii) is a rhetorical point rather than evidence. Two data points is explicitly not a law, and this document says so while still leaning on them.

---

## Verification Debt

Filed as `debt:open` issues, mirrored in the front matter's `debt:` key. None was filed when this
document was first written — the tracker convention was settled by
[#5](https://github.com/NGL321/mosaic/issues/5) four days later, and the original said only that
its debt was "logged against the Curriculum", which did not exist. That is the failure #5 named:
debt asserted in prose and logged nowhere. **These five must be discharged before this document
merges**; they are the reason it has not.

1. **[#45](https://github.com/NGL321/mosaic/issues/45) — Culík & Yu (1988) undecidability proof.** Read the *Complex Systems* original and follow the reduction. §2.3's second finding depends on it and it was reached only through a secondary record. Requires: computability theory to the level of reductions from the halting problem.
2. **[#46](https://github.com/NGL321/mosaic/issues/46) — Hiraoka et al. (2026) HDLSS asymptotics.** Follow the proof, and check that the regime it describes is the regime a Mosaic ECA study occupies. §3.2(c) makes that inference; the paper does not. Requires: high-dimensional probability, persistence-diagram stability.
3. **[#47](https://github.com/NGL321/mosaic/issues/47) — Damrich et al. (2024) failure thresholds.** The d ≳ 30 / σ = 0.25 numbers are read off the paper's figures as reported. Verify against the released code. Requires: only running the code, so this is the cheapest item here.
4. **[#48](https://github.com/NGL321/mosaic/issues/48) — Žunkovič & Ilievski (2024) critical exponents.** The analytic claims in §2.1 are taken on the paper's authority. Requires: tensor networks, MPO representations, finite-size scaling. This is the most expensive item and the one that would schedule real Curriculum work.
5. **[#49](https://github.com/NGL321/mosaic/issues/49) — the Spearman correlations in §3.1.** ρ = 0.77 ± 0.03 etc. are quoted, not recomputed, and the "no null model" claim is an absence, which is what a careless reading misses. Verifiable from the paper's released artifacts if they exist; if they do not, that is itself worth recording.

---

## Proposals

**None.** This document recommends an experimental design; it proposes no edit to `CONTEXT.md`
or the charter. If the recommendation in §0 is accepted, the belt rung it implies is a `belt:`
commit and goes through the §5 warrant gate with a falsifier in Noah's own words — which is a
separate act by a different hand, not something this document can carry.

---

## Appendix: primary sources

Papers, not volatile pages; no retrieval date is given because a published paper does not move.
Where only a preprint exists, the version cited is the one on arXiv as of 2026-07-25.

**Grokking**
- Power, Burda, Edwards, Babuschkin & Misra (2022). *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets.* arXiv:2201.02177. https://arxiv.org/abs/2201.02177
- Liu, Kitouni, Nolte, Michaud, Tegmark & Williams (2022). *Towards Understanding Grokking: An Effective Theory of Representation Learning.* NeurIPS 2022. https://arxiv.org/abs/2205.10343
- Liu, Michaud & Tegmark (2023). *Omnigrok: Grokking Beyond Algorithmic Data.* ICLR 2023. https://arxiv.org/abs/2210.01117
- Nanda, Chan, Lieberum, Smith & Steinhardt (2023). *Progress measures for grokking via mechanistic interpretability.* ICLR 2023. https://arxiv.org/abs/2301.05217
- Gromov (2023). *Grokking modular arithmetic.* arXiv:2301.02679. https://arxiv.org/abs/2301.02679
- Varma, Shah, Kenton, Kramár & Kumar (2023). *Explaining grokking through circuit efficiency.* arXiv:2309.02390. https://arxiv.org/abs/2309.02390
- Rubin, Seroussi & Ringel (2024). *Grokking as a First Order Phase Transition in Two Layer Networks.* ICLR 2024. https://arxiv.org/abs/2310.03789
- Kumar, Bordelon, Gershman & Pehlevan (2024). *Grokking as the Transition from Lazy to Rich Training Dynamics.* ICLR 2024. https://arxiv.org/abs/2310.06110
- Humayun, Balestriero & Baraniuk (2024). *Deep Networks Always Grok and Here is Why.* ICML 2024. https://arxiv.org/abs/2402.15555
- Clauw, Stramaglia & Marinazzo (2024). *Information-Theoretic Progress Measures reveal Grokking is an Emergent Phase Transition.* ICML 2024 workshop. https://arxiv.org/abs/2408.08944
- Prieto, Barsbey, Mediano & Birdal (2025). *Grokking at the Edge of Numerical Stability.* arXiv:2501.04697. https://arxiv.org/abs/2501.04697
- Pomarico et al. (2025). *Transfer entropy and O-information to detect grokking in tensor network multi-class classification problems.* arXiv:2507.23346. https://arxiv.org/abs/2507.23346
- Bi, Zhang, Wang & Calhoun (2026). *Grokking as a Falsifiable Finite-Size Transition.* arXiv:2603.24746. https://arxiv.org/abs/2603.24746

**Cellular automata**
- Culík & Yu (1988). *Undecidability of CA Classification Schemes.* Complex Systems 2, 177–190. https://www.semanticscholar.org/paper/Undecidability-of-CA-Classification-Schemes-Cul%C3%ADk-Yu/c754b39540f79fd542f4e067ab7436b720605192
- Aach, Goebbert & Jitsev (2021). *Generalization over different cellular automata rules learned by a deep feed-forward neural network.* CSCE 2021. https://arxiv.org/abs/2103.14886
- Nobe & Yura (2023). *A study on the composition of elementary cellular automata.* arXiv:2305.02947. https://arxiv.org/abs/2305.02947
- Žunkovič & Ilievski (2024). *Grokking phase transitions in learning local rules with gradient descent.* JMLR 25(199), 1–52. https://www.jmlr.org/papers/v25/22-1228.html
- Rollier, Daly & Baetens (2024). *Convolutional neural networks for automated cellular automaton classification.* arXiv:2409.02740. https://arxiv.org/abs/2409.02740
- Burtsev (2024). *Learning Elementary Cellular Automata with Transformers.* arXiv:2412.01417. https://arxiv.org/abs/2412.01417
- Zhang et al. (2025). *Intelligence at the Edge of Chaos.* ICLR 2025. https://arxiv.org/abs/2410.02536
- Lžičar (2025). *CellARC: Measuring Intelligence with Cellular Automata.* arXiv:2511.07908. https://arxiv.org/abs/2511.07908
- Hamming-distance-based CA classification (2024). arXiv:2407.06175. https://arxiv.org/abs/2407.06175
- Eppstein. *Wolfram's Classification of Cellular Automata* (lecture note, secondary). https://ics.uci.edu/~eppstein/ca/wolfram.html

**TDA and persistent homology**
- Fasy, Lecci, Rinaldo, Wasserman, Balakrishnan & Singh (2014). *Confidence sets for persistence diagrams.* Ann. Statist. 42(6), 2301–2339. https://projecteuclid.org/journals/annals-of-statistics/volume-42/issue-6/Confidence-sets-for-persistence-diagrams/10.1214/14-AOS1252.full
- Chazal, Fasy, Lecci, Michel, Rinaldo & Wasserman (2015). *Subsampling Methods for Persistent Homology.* ICML 2015. https://proceedings.mlr.press/v37/chazal15.html
- Rieck et al. (2019). *Neural Persistence.* ICLR 2019. https://arxiv.org/abs/1812.09764
- Gebhart, Schrater & Hylton (2019). *Characterizing the Shape of Activation Space in Deep Neural Networks.* arXiv:1901.09496. https://arxiv.org/abs/1901.09496
- Naitzat, Zhitnikov & Lim (2020). *Topology of Deep Neural Networks.* JMLR 21(184). https://jmlr.org/papers/v21/20-345.html
- Corneanu, Escalera & Martinez (2020). *Computing the Testing Error without a Testing Set.* CVPR 2020. https://openaccess.thecvf.com/content_CVPR_2020/html/Corneanu_Computing_the_Testing_Error_Without_a_Testing_Set_CVPR_2020_paper.html
- Bauer (2021). *Ripser: efficient computation of Vietoris–Rips persistence barcodes.* J. Appl. Comput. Topology. https://link.springer.com/article/10.1007/s41468-021-00071-5
- Birdal, Lou, Guibas & Şimşekli (2021). *Intrinsic Dimension, Persistent Homology and Generalization in Neural Networks.* NeurIPS 2021. https://proceedings.neurips.cc/paper/2021/hash/35a12c43227f217207d4e06ffefe39d3-Abstract.html
- Pérez-Fernández et al. (2021). *Persistent Homology Captures the Generalization of Neural Networks Without A Validation Set.* arXiv:2106.00012. https://arxiv.org/abs/2106.00012
- Burella Pérez et al. (2021). *giotto-ph: A Python Library for High-Performance Computation of Persistent Homology.* arXiv:2107.05412. https://arxiv.org/abs/2107.05412
- Barannikov, Trofimov, Balabin & Burnaev (2022). *Representation Topology Divergence.* ICML 2022. https://proceedings.mlr.press/v162/barannikov22a.html
- Turkeš, Montúfar & Otter (2022). *On the Effectiveness of Persistent Homology.* NeurIPS 2022. https://arxiv.org/abs/2206.10551
- Vishwanath, Sriperumbudur, Fukumizu & Kuriki (2022). *Adversarially Robust Topological Inference.* arXiv:2206.01795. https://arxiv.org/abs/2206.01795
- Bobrowski & Skraba (2023). *A universal null-distribution for topological data analysis.* Sci. Rep. 13. https://www.nature.com/articles/s41598-023-37842-2
- Girrbach, Christensen, Winther, Akata & Akata (2023). *Addressing caveats of neural persistence with deep graph persistence.* TMLR. https://arxiv.org/abs/2307.10865
- Ballester, Casacuberta & Escalera (2023). *Topological Data Analysis for Neural Network Analysis: A Comprehensive Survey.* arXiv:2312.05840. https://arxiv.org/abs/2312.05840
- Damrich, Berens & Kobak (2024). *Persistent Homology for High-dimensional Data Based on Spectral Methods.* NeurIPS 2024. https://arxiv.org/abs/2311.03087
- Tan, García-Redondo, Wang, Bronstein & Monod (2024). *On the Limitations of Fractal Dimension as a Measure of Generalization.* NeurIPS 2024. https://arxiv.org/abs/2406.02234
- Gourgoulias et al. (2024). *Estimating class separability of text embeddings with persistent homology.* TMLR. https://arxiv.org/abs/2305.15016
- Hiraoka, Imoto, Kanazawa & Liu (2026). *Curse of Dimensionality on Persistence Diagrams.* Foundations of Data Science. https://arxiv.org/abs/2404.18194
- Tang, Wang, García-Redondo & Monod (2026). *Topological Signatures of Grokking.* arXiv:2605.06352. https://arxiv.org/abs/2605.06352
