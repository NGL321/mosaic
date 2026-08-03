---
ticket: 48
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 5
debt: [116]
supersedes: null
---

# Žunkovič & Ilievski (2024): the exponents are analytic and correct, but they are proved for a perceptron on frozen features, and "locality of the teacher" will not carry the survey's generalisation

The JMLR paper was reached and read **in full** — all 52 pages of the published PDF, text-extracted from `jmlr.org` and read section by section, including Sections 3 and 4, the Summary, and Appendices B–D. The arXiv record was opened for version history only (abstract page; v1, no later version). The [#4 survey](https://github.com/NGL321/mosaic/issues/4) §2.1 that this ticket holds down was opened in full on `research/grokking-eca-tda-survey` and its specific sentences are checked against the paper below. Nothing here is derived from an abstract, a citation, or recollection. What was **not** done is an independent re-derivation of the paper's algebra: Eqs. 14, 23, 30, 43–50 and Appendix B were read and their logic followed, not recomputed. Quotations are transcribed from the PDF text layer; ligature and inter-word spacing artefacts of extraction have been silently normalised, no words changed.

## 0. Verdict

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | Was the primary source reached in full? | **Established** | §1 |
| 2 | Are the critical exponents exact analytic results? | **Supported** | §2 |
| 3 | Are they analytic *for the cellular-automaton task*? | **Refuted** | §2, §3 |
| 4 | Are the rule-30 exponents obtained by finite-size scaling? | **Refuted** | §3 |
| 5 | Is the grokking probability derived in closed form? | **Loose** | §4 |
| 6 | Is the grokking-time distribution derived rather than fitted? | **Loose** | §4 |
| 7 | What model is the analysis proved for — is it the tensor-network attention model? | **Refuted** — it is a perceptron on frozen features | §5 |
| 8 | Is "locality of the teacher" a claim about the task rather than the architecture? | **Contested** | §6 |
| 9 | Does the survey's generalisation past the tensor-network model survive? | **Refuted** as a quantitative claim | §6, §7, §8 |
| 10 | What does the paper claim about its own generality? | **Established** | §7 |

> **The analytic results are real and correctly described as exact, but they are exact about a single perceptron trained on hand-chosen or rejection-sampled frozen features; the critical exponent is a function of the *student's* latent distribution, not of the rule; and the paper's own closing sentence — "Extending the presented theory to deep neural networks appears to be difficult within the proposed framework" — is a direct denial of the generalisation the survey rests on it.**

## 1. What was read, and what the paper is

*Grokking phase transitions in learning local rules with gradient descent*, Bojan Žunkovič and Enej Ilievski, [JMLR 25(199), 1–52 (2024)](https://www.jmlr.org/papers/v25/22-1228.html), submitted 10/22, revised 6/24, published 7/24, editor Maxim Raginsky, CC-BY 4.0. The [full PDF](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf) is 52 pages: Introduction, Related work, §3 *Perceptron grokking* (two solvable models), §4 *Learning local rules with shallow tensor networks*, §5 Summary and discussion, and Appendices A–D. The [arXiv preprint](https://arxiv.org/abs/2210.15435) is v1 of 26 Oct 2022 and was never revised on arXiv; the JMLR version is the one that carries the 6/24 revision, and it is the version read here. Where the extracted PDF retains a stale page from an earlier draft (a duplicated "Figure 11/Figure 12" block bearing line numbers, physically present in the file between pages 31 and 32), the published figure numbering — Figure 15, Figure 16, Table 1 — is used.

The paper has four stated contributions, in its own list: a solvable grokking scenario with "exact critical exponents and grokking-time distributions"; a tensor-network map from "the sequence prediction model in the thermodynamic limit to the proposed grokking setup"; a numerical study of rule-30 learning and structure formation; and a finding that L1 and L2 regularisation differ materially.

## 2. The critical exponents: exact, and exactly about what

Three distinct exponents appear in the [paper](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf), and the survey's phrase "exact analytic expressions for critical exponents" is true of the first two only.

**(a) 1D exponential model, ν = 1, exact.** The model is a one-parameter classifier `f(x) = sgn(x − b)` with `w` fixed to 1, trained by gradient flow on squared loss with L1/L2 penalties, on two exponential class densities `P⁺(x̃) = e^{−(x̃−ϵ)}Θ(x̃−ϵ)` separated by a gap `2ϵ`. Expanding the test error about the zero-error time `t_ϵ` gives `⟨⟨E(t)⟩⟩ ≈ (ϵ_λ/2)(t_ϵ − t)`, and the paper states: "Grokking in the considered 1D exponential model is a second-order phase transition with the test-error critical exponent equal to one. The regularisation parameters and the distance between positive and negative class distributions change only the prefactor." This is a closed-form derivation with no fitting.

**(b) D-dimensional uniform-ball model, ν = (D+1)/2, exact.** Positive and negative samples fill unit balls shifted by `±ϵ`; the student is `f(x̃) = sgn(x̃·w)`. Near the critical point the test error is `E_D(t) ∝ (1 − h(t))^{(D+1)/2}`, and "the critical exponent is hence determined only by the dimensionality of the feature distribution."

**(c) The generalisation to isotropic densities, §3.3.4 — this is the result that actually gets used.** For an isotropic density on a compact domain whose radial profile `ρ(r)` is analytic at the boundary, ν = (D+1)/2 again; if instead `ρ(δh) ≈ ρ_ξ δh^{−ξ}` with an algebraic divergence, then `E_test(t) ∝ (t − t_ϵ)^{(D+1−2ξ)/2}`. The paper is explicit about the domain of validity: "0 < ξ < 1". It then adds the hedge that matters — "we might have to relax the condition 0 < ξ < 1 to accommodate a more general divergence" — and in the cellular-automaton section it does exactly that, reporting measured `ξ* = 1.2, 1.8, 1.6`, every one of them outside the range the formula was derived in. **This is the load-bearing step and it is the weakest in the analytic chain**: the formula that connects the toy model to the rule-learning experiment is applied outside its stated hypothesis, and the paper says so rather than hiding it.

Note also what the exponent is a property *of*: `D` in every one of these expressions is the dimension of the **latent feature distribution** the linear classifier sees, and `ξ` is the boundary behaviour of that same latent distribution. Neither is a property of the rule being learned.

## 3. The rule-30 exponents are fitted, not scaled

The ticket asks whether the exponents are obtained "numerically by finite-size scaling". They are not. There is no scaling collapse and no finite-size-scaling ansatz anywhere in the [paper](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf). The procedure is: run ~1000 trainings from different random initialisations; for each run locate `t_ϵ`, the first time the test error hits zero; align all runs on `t_ϵ`; average the test error; fit a straight line to a log–log plot of mean error against `t_ϵ − t`. The slope is ν.

The numbers, all fitted this way:

- **Fixed (frozen) attention tensors, bond dimension d = 2, 1-local rule** (Figure 15, three rejection-sampled examples): ν = 0.86, 0.85, 0.82 / 0.77, 0.76, 0.72 / 0.82, 0.86, 0.82 across regularisation settings. The paper's reading: "the critical exponent ν does not depend on the regularisation strengths λ₁,₂ and is in all cases smaller than one, which is in agreement with the predictions of the simple grokking model."
- **Full model trained end to end** (Figure 19, 1-local): unregularised ν = 1.99 (d=10), 2.81 (d=20), 2.80 (d=40); L2 at λ₂=1e−4: 1.09, 0.82, 0.87; L1 at λ₁=1e−3: 0.64, 0.72, 0.67. Appendix D repeats this for 2-local and 3-local rules with the same pattern, and finds ν "smaller for larger rule range K".

Two things follow that the survey does not record. First, in the **full** model the exponent depends strongly on regularisation (≈2.5 unregularised versus ≈0.7 under L1) — the paper flags this itself: "Larger regularisation leads to a sharper transition to zero test error, in contrast with the linear case studied in the Section 3.3.2 and in the Section 4.3.1, where the critical exponent was found to be independent of the regularisation strengths λ₁,₂." The analytic prediction and the end-to-end experiment therefore disagree on the one qualitative feature the analytic result is confident about. Second, the claim that ν "depends only slightly on the model size" is doing work in the paper (it is the evidence that `D_eff` is size-independent), yet in the unregularised full-model column ν runs 1.99 → 2.81 → 2.80 as d goes 10 → 20 → 40, which is a 40% move.

The quantitative check of the theory against the experiment is Table 1, and it is a three-point comparison of `ξ = ½(D_eff − 2ν + 1)` against the measured `ξ*`: 1.15 vs 1.2, 1.65 vs 1.8, 1.16 vs 1.6. The paper's own verdict is calibrated — "reasonably close in two out of the three considered cases" — and the third case misses by 0.44 on a quantity of order 1.5. `D_eff` here is not an integer dimension but `exp` of the entropy of PCA explained-variance ratios (3.0, 3.8, 3.0), substituted into a formula derived for an integer-dimensional ball. The survey's summary that "the numerics validate them" is stronger than two-of-three agreement on three hand-picked frozen-attention instances supports.

Minor, but worth knowing when reading the paper: the vertical axes of the Figure 15 panels are labelled `E_train` while the caption and the surrounding text both describe the mean **test** error. The caption is right; the axis label is a typo.

## 4. Grokking probability and grokking time: derived, approximated, and redefined

**Grokking probability.** In the 1D exponential model this is genuinely exact and closed-form: the condition for zero final test error is `|x̄| < ϵ_λ`, the mean of N exponential samples is gamma-distributed, and `P_{E(∞)=0}` comes out in regularised generalised hypergeometric functions (Eq. 14), collapsing for N = 2 to `1 − (1 + 2ϵ_λ)e^{−4ϵ_λ}`. In the D-dimensional ball model it is not: "A general calculation of the grokking probability and the grokking-time PDF is not feasible since we would have to invert a random matrix G." What is derived is the `N ≫ 1` limit in which `G` becomes near-diagonal, and for λ₁ > 0 Appendix B delivers only a **lower bound** (Eq. 90). For the cellular-automaton task nothing is derived at all, and the quantity reported is not the same quantity: "We estimate the grokking probability as the fraction of the sampled attention tensors A that leads to linearly separable latent space data for the studied rule. In contrast to the grokking probabilities discussed in Section 3, we fix the training set to contain all possible samples of length M = 3." The measured value is small — of order 0.01–0.02 out of 20k sampled attention tensors (Figure 14).

**Grokking time.** 1D: `t_G` is closed form (Eq. 16) and its PDF is closed form for N = 2 (Eq. 17), which the paper concedes is "not very instructive" and leaves unnormalised. D-dimensional: the PDF is bimodal by construction — a fast-relaxation branch obtained by pushing a χ²_{D−1} initial-condition distribution through Eq. 44, plus a slow branch that is a **Dirac delta**, because "the grokking time is independent of the initial condition" in that regime. The paper's own caveat is explicit: "We do not expect the analytically obtained grokking-time PDF to quantitatively describe real experiments, particularly because it is a zeroth-order large N solution. However, the bimodal structure and the qualitative parameter dependence should also be present in more realistic scenarios." On the CA task the comparison is duly qualitative — bimodality is observed, the `N ≫ 1` condition is stated to be invalid, and "increasing the regularisation strength λ₂ often leads to increased grokking time, which is not the case in the simple uniform ball model."

So the [ticket's](https://github.com/NGL321/mosaic/issues/48) question — what is derived versus fitted — has a clean answer. Derived: 1D probability and time PDF; D-dimensional probability under `N ≫ 1` (a bound under L1); D-dimensional time PDF at zeroth order. Fitted or merely estimated: everything about rule 30. And in the solvable models grokking is *atypical* — "the typical dataset sampled from the initial probability distribution does not display the grokking behaviour" — so the illustrative figures are produced from datasets deliberately shifted away from the probability mass. In the full tensor-network model, by contrast, "The grokking phenomenon is, in this case, a typical behaviour, in contrast to our effective distributions discussed in the previous section." The solvable models and the phenomenon they are offered to explain differ on whether grokking is rare.

## 5. What model the analysis is actually proved for

This is where [the survey's description](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md) drifts. **Every analytic result in the [paper](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf) is a result about a single perceptron** — Eq. 1, `f(x̃) = sgn(w·x̃ + b)` — trained by gradient flow on a squared loss with L1/L2 penalties, on synthetic latent distributions assumed linearly separable. Section 3 says so in its own framing: the feature-learning half of a network is *replaced* by the assumption of separable latent densities `P±`, and "This training dynamics does not account for feature learning, which is a crucial aspect of the grokking process."

The tensor-network attention model of §4.2 is a separate object and it is not what the analysis is proved about. Precisely, it is: a binary embedding `φ: {−1,1} → R²`; two parameter tensors `A, B ∈ R^{d×d×2}` (attention and classification) with `d` the bond dimension; input-contracted matrices `A(i)`; left and right context matrices `H_L(i) = H_L(i−1)A(i−1)`, `H_R(i) = A(i+1)H_R(i+1)`, normalised; a local weight vector `w(i)_j = Tr(H_L^N(i) B_j H_R^N(i))`; output `ŷ_i = w(i)·φ(x_i)` followed by `sgn`, with a sigmoid inserted before the sign during full training for stability. It is *uniform* (one `A` and one `B` shared across positions), shallow, and handles variable input length — which is why it was chosen over a perceptron. The paper calls it "a simplified version of the tensor network proposed in Žunkovič (2022)" and "a generalisation of the linear-dot attention mechanism". It is built from matrix-product-state-style contractions; **the paper never calls it an MPO**, and the survey's parenthetical "matrix-product-operator style" is the survey's gloss, not the paper's word.

The **tensor-network map** (§4.2.3) is the bridge, and it is a one-line observation, not a theorem: with the attention tensors `A` held **fixed**, the layer becomes a feature map `z_i(x) = H_R^N(i) H_L^N(i) ⊗ φ(x_i) ∈ R^{2d²}`, and then `ŷ = z_i(x) · vec(B)` — a perceptron in `D = 2d²` dimensions whose weight vector is the classification tensor `B`. "By setting D = 2d², we have mapped the local-rule learning problem in the thermodynamic limit to a (grokking) classification problem of the form discussed in Section 3."

That sentence is the whole of the connection, and it costs three things. The attention tensors are frozen, so no feature learning happens in the regime the theory covers. They are not learned but **rejection-sampled** for solvability — "Since not all attention vectors lead to solvable problems, we perform rejection sampling by checking if the final model parameters given by Eq. 21 have zero test error. The rejection sampling procedure works well for D ≤ 3." And the reported numerics for the theory-comparison run at `d = 2`. When the full nonlinear model is trained, the paper withdraws the theory itself: "Since the full tensor-attention model is non-linear, we do not expect the theory developed in Section 3 to be valid."

There is one construction that is architecture-specific and exact: for the 1-local rule the paper writes down attention tensors `A₀, A₁` (Eq. 68) under which `z_i(x)` carries exactly the neighbourhood state, and the transition becomes **first order** with a jump of 1/4 — "the factor 1/4 comes from the fact that the neighbourhood of any given position has four possible different values". The second-order transition with a fractional exponent appears only for *randomly sampled, inexact* attention tensors, because "Sampled attention vectors H_{L,R}(i) also contain information about the input beyond only the neighbouring sites. Moreover, information about the neighbours is not complete." The order of the phase transition is therefore set by how well the student's frozen map matches the rule's neighbourhood — an architecture-and-initialisation property, not a property of rule 30.

## 6. "Locality of the teacher": task or architecture — the step that matters

The claim has a task half and an architecture half, and they are not separable in the way [the survey](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md) needs.

**The task half is real.** The paper's contrast is with standard teacher–student statistical mechanics, where teacher and student weights live on an M-sphere, `N = αM`, and the replica calculation gives `E_test ∝ 1/α`. The paper's diagnosis: "In this case, all values of the input contribute to the final result. In the thermodynamic limit this leads to a mean-field-like behaviour, i.e. the value of the input at any particular position has only infinitesimal influence on the result/rule." Restricting the teacher to `y_i = rule(x_{i−K},…,x_{i+K})` breaks that, and "The locality of the teacher/rule enables us to map the problem to a finite-dimensional latent space where we discuss grokking (a second-order phase transition) and latent-space structure formation." Locality of the *rule* is unambiguously a property of the task, and it is what makes a finite-dimensional latent description possible at all. To that extent the survey is right that the mechanism is not a statement about transformers.

**But the architecture half is where the grokking comes from, and it is not eliminable.** Three observations, all from the text:

1. **The map that realises locality is the student's.** Locality of the teacher does not by itself produce a finite-dimensional latent space; the *student's* fixed attention tensors do, and `D = 2d²` is a property of the student's bond dimension. The exponent `ν = (D+1−2ξ)/2` is then a function of `D_eff` and `ξ` measured on `z_i(x)` — quantities computed, in §4.3.1, by PCA on the student's features. The rule enters only as a lower bound: Appendix D notes that "the smallest effective dimension is determined by the locality of the rule and is expected to increase exponentially with K". Locality bounds the exponent's argument from below; it does not determine it.

2. **The paper's strongest generality sentence is existential over architectures.** "Interestingly, for a K−local rule, we can find 4^K-dimensional matrices A for which the transformed problem is solvable by a simple perceptron model and exhibits the grokking phenomena. Therefore, the 1/α dependence on the training set size obtained from the standard rule-learning theory seems to be a consequence of the mean-field type infinite-range rule. **For any local rule, we will observe grokking.**" Read carefully, the licensed claim is *there exists a tensor-network student in which a K-local rule grokks* — not *any student learning a local rule grokks*. The measured grokking probability in exactly that setting is 1–2% of randomly sampled attention tensors (§4). "For any local rule, we will observe grokking" is a universal quantifier over rules resting on an existential over architectures, and the paper offers no argument that removes the existential.

3. **The one place the architecture is made to match the rule exactly, the phenomenology changes qualitatively** — the transition becomes first order with a 1/4 jump (§5). If locality of the task were the whole mechanism, the order of the transition would not be a free parameter set by the student's frozen map.

**Decision.** "Locality of the teacher" is a claim about the task — and it is correctly *not* a claim about transformers — but it is an **enabling condition, not the mechanism**. The mechanism the exponents, probabilities and time distributions belong to is: a local task, *plus* a student whose frozen map compresses the input into a low-dimensional latent space in which the classes are linearly separable, *plus* a final linear classifier trained by gradient flow. Every quantitative prediction is a function of the second ingredient. So the inference the survey draws — that because the mechanism is about the task, the result should carry past the tensor-network attention model — **does not go through for anything quantitative**. What survives is weaker and still worth having: locality of the rule is the reason a grokking-type transition is *available* in this class of tasks at all, where the mean-field teacher–student setting forbids it. That is a qualitative existence argument about the task, and it is architecture-independent. The exponents, the grokking probability, and the grokking-time PDF are not.

## 7. What the paper claims about generality, in its own words

The [paper](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf) is more modest than its citers. Its broader-impact paragraph conjectures rather than concludes: "Although based on simple models, our results can also be relevant for deep learning training practice. We conjecture that good generalisation is more likely in models with latent space data distributions with small effective dimensions." Its extrapolations are about **L1 versus L2 regularisation**, not about exponents: "we expect that L1 regularisation leads to improved generalisation properties … also in a more general classification setting."

On the critical exponent it makes exactly one portability claim, and it is scoped to the data distribution rather than the architecture: "While both the grokking probability and the grokking-time PDF depend on the details of the model's initial parameters and the evolution, the critical exponent ν depends only on the data distribution at the boundary of the domain. Therefore, we expect that Eq. 50 describes the critical exponent quantitatively also in a more general setting." Note what this licenses: if you can *measure* `D_eff` and `ξ` of a model's latent features, Eq. 50 may predict its exponent. It does not license predicting a number for a new architecture in advance, because `D_eff` and `ξ` are outputs of that architecture.

And the closing paragraph of §5 states the limit directly:

> "The considered local tensor-network rule learning setup is an extreme example of a learning rule. The standard teacher-student mean-field setup is the opposite extreme. It would be interesting to study if the proposed grokking setup and the tensor-network map can be extended to study algebraically decaying rules which interpolate between the two extremes. **Extending the presented theory to deep neural networks appears to be difficult within the proposed framework.**"

The survey leans on this paper to argue the result should generalise past the model it was proved for. The paper's last sentence says the opposite about the direction that matters.

## 8. Consequences for survey §2.1

Checked sentence by sentence against the [paper](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf), [survey §2.1](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md) holds up on the facts and overreaches on the scope.

- "derives *exact* analytic expressions for critical exponents, grokking probability, and the grokking-time distribution" — **true of the solvable perceptron models**, and only of the 1D one without qualification; the D-dimensional probability is an `N ≫ 1` result and an L1 lower bound, the D-dimensional time PDF is zeroth-order. Nothing is exact for the CA task. The sentence should carry that scope.
- "argues grokking is a consequence of locality of the teacher model" — accurate, and note the JMLR abstract's own verb is weaker than the arXiv abstract's: JMLR says "provide evidence that", where arXiv v1 said "show that". The published paper hedged this claim between 2022 and 2024. That is a meaningful signal about how much weight the authors think it bears.
- "The architecture is a tensor-network attention model (matrix-product-operator style), *not* a standard transformer or MLP" — correct on the negative, loose on the positive: the paper builds from MPS-style contractions and never uses "MPO".
- "Rule 30 is expressible as an MPO with bond dimension 4, which is why it is tractable in this framework" — **not supported by this paper.** What the paper says is that for a K-local rule one *can find* `4^K`-dimensional attention matrices `A` making the mapped problem perceptron-solvable, and that for the exact 1-local solution "The minimal bond dimension of the exact solution can be reduced to 2 if we generalise the model and train different left and right attention tensors A." The exact `A₀, A₁` of Eq. 68 are 4×4, so the number 4 has a real referent, but it is the dimension of an attention matrix in this construction, not a bond dimension of an MPO representation of rule 30. If the survey wants the MPO claim it must be sourced elsewhere (Žunkovič 2022, or Guo et al. 2018) or dropped.
- "The analytic results are strong and the numerics validate them" — "validate" is too strong; the paper's own word is that the prediction "roughly agrees" and is "reasonably close in two out of the three considered cases".
- "The 'locality of the teacher' mechanism is a claim about the *task*, not about transformers specifically — which is a point in its favour for generalisation, but it has not been tested that way" — the first clause is right, the inference in the second is not, per §6. It is not merely untested; the paper's quantitative machinery is constitutively about the student's latent geometry, and the authors say extending it to deep networks looks hard.

The survey's *headline* use of the paper — that ECA "remains a good substrate … with a genuine grokking result attached to it" — survives all of this intact. What does not survive is any plan that expects the exponents or the grokking-time distribution to transfer to a transformer on the same task. The survey's own open question 4 already poses that as a replication question; this reading says it should be posed as an **open** question, not as a prediction with a number attached.

## What this does not establish

### Sources not reached

The primary source was reached in full and every number quoted above was read in the published PDF. Two things adjacent to it were not opened: Žunkovič (2022), the tensor-network attention paper this model is "a simplified version of", which is where the gauge-symmetry argument and the exponential-in-K effective-dimension claim actually live; and Guo, Jie, Lu & Poletti (2018), *Matrix product operators for sequence-to-sequence learning*, which is the plausible origin of the survey's "MPO with bond dimension 4" claim. Neither is needed for any verdict here, but the MPO sentence in the survey cannot be settled without them.

### Open gaps

Three, in descending order of value to Mosaic. **First**, nobody has measured `D_eff` and `ξ` of the latent representation of a *standard* architecture — transformer or MLP — learning an elementary CA rule, and checked Eq. 50 against its fitted exponent. That is the sharpest available test of whether the locality mechanism is architecture-portable, it is cheap, and the paper hands over the prediction formula. **Second**, the analytic theory covers only frozen features; the paper explicitly says it does not expect it to hold for the full nonlinear model, and the full-model exponents indeed disagree with it on regularisation dependence. What governs the exponent when features are learned is open, and it is precisely the regime Mosaic's rung cares about, since the rung is *about* representation formation. **Third**, and this is the candidate new Verification Debt described in the report accompanying this document rather than filed here: the survey's claim that rule 30 is an MPO of bond dimension 4 is not in this paper, and needs either a source or a deletion.

### Load-bearing ifs

The verdict on sub-question 9 turns on one reading: that `D` in Eq. 50 is the effective dimension of the *student's* latent features and not a quantity fixed by the rule. If that reading is wrong — if some argument pins `D_eff` to the rule's locality tightly enough that the student's contribution is a bounded correction — then the exponent becomes a task invariant and the survey's generalisation is restored. Appendix D's remark that the minimal effective dimension "is determined by the locality of the rule and is expected to increase exponentially with K" is the strongest text in that direction, and it is a *lower bound* remark citing another paper, not a derivation; the measured `D_eff` values (3.0, 3.8, 3.0 with fixed attention; 1.8, 1.3, 1.1 in the full model under different regularisers) vary with the regulariser at fixed rule, which is what decided the reading. Second, the whole §3 → §4 comparison depends on Eq. 50 remaining valid at `ξ > 1`, outside its derived range; if it does not, then the two-of-three agreement in Table 1 is coincidence and the paper's validation of its own theory on the CA task is weaker still — which would strengthen, not weaken, the verdict here.

## Verification Debt

One item, filed and open.

- **[#116](https://github.com/NGL321/mosaic/issues/116)** — the survey's claim that *"Rule 30 is
  expressible as an MPO with bond dimension 4, which is why it is tractable in this framework"* is
  **not in this paper**. The paper never uses the term MPO; it says one can find 4^K-dimensional
  *attention matrices* for a K-local rule, and that for K = 1 the minimal bond dimension is **2** with
  separately trained left and right tensors. The number 4 has a referent — the 4×4 exact A₀, A₁ of
  Eq. 68 — but it is not an MPO bond dimension and not a property of the rule. The sentence does causal
  work in the survey, so it needs sourcing to Žunkovič (2022) or Guo et al. (2018) — neither opened
  here, both recorded under *Sources not reached* — or deleting.

## Proposals

Two, both for Noah to apply.

**(1) Replacement text for the fourth and sixth bullets of survey §2.1** (`docs/research/2026-07-25-grokking-eca-tda-survey.md`, on `research/grokking-eca-tda-survey`):

> - The concrete CA instance is **rule 30**, a single Class-III rule; 2-local and 3-local rules appear in an appendix. For a K-local rule the authors exhibit `4^K`-dimensional attention matrices under which the mapped problem is solvable by a perceptron; for K=1 the exact tensors are 4×4, and the paper notes the minimal bond dimension of the exact solution drops to 2 if left and right attention tensors are trained separately.

> **Robustness assessment.** The analytic results are exact but narrowly scoped: they are results about a *perceptron* trained on frozen, rejection-sampled features, and the paper states it does not expect them to hold for the full nonlinear model. On the CA task the exponent is a log-log fit, not a finite-size-scaling result, and the theory's prediction is "reasonably close in two out of the three considered cases" by the authors' own assessment. "Locality of the teacher" is a property of the task and correctly not a claim about transformers, but it is an *enabling* condition rather than the mechanism: every quantitative prediction is a function of the student's latent effective dimension and boundary exponent, not of the rule. The paper's closing sentence is "Extending the presented theory to deep neural networks appears to be difficult within the proposed framework." Whether the exponents port to a standard architecture is therefore an open replication question, not a prediction.

**(2) Badge for the `CONTEXT.md` claim site**, if and only if Noah accepts §6:

> Grokking in local-rule learning is an analytically solved phenomenon for a perceptron on frozen tensor-network features; its critical exponents are properties of the learner's latent geometry, not of the rule ⟦T3 · #48⟧

## Appendix: primary sources, all retrieved 2026-08-02

1. Žunkovič, B. & Ilievski, E., *Grokking phase transitions in learning local rules with gradient descent*, JMLR 25(199):1–52, 2024 — [publisher record](https://www.jmlr.org/papers/v25/22-1228.html). Abstract, bibliographic data, licence.
2. The same paper, [full published PDF, 52 pages](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf). Read in full; every quotation and every number in this document comes from here.
3. arXiv preprint of the same paper, [arXiv:2210.15435](https://arxiv.org/abs/2210.15435). Abstract page only, used for version history (v1, 26 Oct 2022, never revised) and for the abstract wording that differs from the published version.
4. Mosaic issue [#48, *Žunkovič & Ilievski (2024) critical exponents are taken on the paper's authority*](https://github.com/NGL321/mosaic/issues/48). The ticket this document discharges; read in full including labels and dependencies.
5. Mosaic survey [`docs/research/2026-07-25-grokking-eca-tda-survey.md` on `research/grokking-eca-tda-survey`](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md). §2.1 read in full; it is the text whose claims §8 checks.
