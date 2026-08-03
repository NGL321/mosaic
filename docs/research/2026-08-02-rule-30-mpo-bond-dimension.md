---
ticket: 116
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 8
debt: []
supersedes: null
---

# Rule 30 really is an exact MPO of bond dimension 4 — the source is Guo et al. (2018), the number is true of all 256 elementary rules, and the survey's clause "which is why it is tractable in this framework" is false in the framework it names

Both candidate origins that [#48](https://github.com/NGL321/mosaic/issues/48) recorded as *not reached* were reached here and read as PDFs in full: Guo, Jie, Lu & Poletti (2018), [arXiv:1803.10908v3](https://arxiv.org/abs/1803.10908), 13 pages including Appendices A–C; and Žunkovič (2022), [arXiv:2209.09098v1](https://arxiv.org/abs/2209.09098), 13 pages. Both were downloaded and text-extracted locally; every quotation below is transcribed from that text layer, with ligature and inter-word spacing artefacts of extraction silently normalised and no words changed. The [Žunkovič & Ilievski (2024) JMLR PDF](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf) was retrieved again and searched exhaustively for the acronym and for the two citations, rather than re-read end to end — [#48](https://github.com/NGL321/mosaic/issues/48) read it in full and this document does not repeat that. The two **publisher** records — Physical Review E and Springer's *Quantum Machine Intelligence* — were attempted and refused (403 and an authentication redirect), so the published versions are *not reached*; the arXiv versions are what this document rests on. Nothing here is derived from an abstract or from recollection. What was **not** done is an independent verification that the explicit rule-30 tensors of Guo et al. Appendix B reproduce rule 30 when contracted; they were read, not multiplied out.

## 0. Verdict

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | Does a primary source state that rule 30 is exactly an MPO of bond dimension 4? | **Established** | §2 |
| 2 | Does Guo et al. (2018) exhibit the rule-30 MPO explicitly, or only assert it? | **Established** — explicit tensors, Appendix B | §2 |
| 3 | Does Žunkovič (2022) state the claim in the survey's own words? | **Established** | §3 |
| 4 | Is bond dimension 4 a distinguishing property *of rule 30*? | **Refuted** | §2 |
| 5 | Is the number 4 unconditional? | **Loose** — it is the fixed-boundary value | §2 |
| 6 | Is D = 4 what makes rule 30 tractable even inside the MPO framework? | **Refuted** | §3 |
| 7 | Is "which is why it is tractable in this framework" true of Žunkovič & Ilievski's framework? | **Refuted** | §4 |
| 8 | Should the survey sentence be deleted? | **Refuted** — re-sourced and re-scoped, not deleted | §5 |

> **The MPO claim is true and has a real primary source — [Guo, Jie, Lu & Poletti (2018)](https://arxiv.org/abs/1803.10908) Appendix B writes down the rule-30 tensors and states that *all* 256 elementary rules are exact MPOs of bond dimension 4 — but it belongs to a different line of work than the one the survey attaches it to, it does not single out rule 30, and Žunkovič & Ilievski cite that very line of work to say that "no grokking phenomena have been reported" in it, which is the opposite of the causal role the survey gives it.**

## 1. What was being asked

[Issue #116](https://github.com/NGL321/mosaic/issues/116) holds down one sentence of [survey §2.1](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md), inside a bullet list describing Žunkovič & Ilievski (2024):

> The concrete CA instance is **rule 30**, a single Class-III rule; 2-local and 3-local rules appear in an appendix. Rule 30 is expressible as an MPO with bond dimension 4, which is why it is tractable in this framework.

[#48's document](https://github.com/NGL321/mosaic/blob/research/debt-sweep-2026-08-02/docs/research/2026-08-02-zunkovic-ilievski-grokking-exponents.md) established that the claim is not in the [JMLR paper](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf) and named two candidate origins it had not opened. This document opens both. The sentence has two halves and they turn out to have opposite fates: the **factual** half is sourced, and the **causal** half is not merely unsourced but contradicted by the paper it is attached to.

A confirmation of #48's negative first, since it is one grep and it is stronger than "not found in the sections read": the acronym `MPO` occurs **zero times** in the 52-page JMLR PDF, bibliography included. The string *matrix product operator* occurs exactly twice, both times inside a reference title — Guo et al. (2018) and Žunkovič (2022). The two candidate origins were therefore not arbitrary guesses; they are the only two places in that paper where the words appear at all.

## 2. Guo et al. (2018): where the claim actually lives, with the tensors written out

The source is *Matrix Product Operators for Sequence to Sequence Learning*, Chu Guo, Zhanming Jie, Wei Lu and Dario Poletti, [arXiv:1803.10908](https://arxiv.org/abs/1803.10908) (v1 29 Mar 2018, v2 1 May 2018, v3 3 May 2018), published as Phys. Rev. E **98**, 042114 (2018). It trains an MPO to map an input sequence to an output sequence; cellular automata are its first test case, chosen precisely because the exact answer is known.

The main text (§III A) sets that up — "Steady states of cellular automata can be written exactly using matrix product states, however here we are interested in training an MPO that describes the evolution rule of a cellular automata. Such cellular automata rule can be exactly mapped to MPOs" — and defers the construction to **Appendix B**, *Example of matrix product operator rewriting of cellular automata evolution*. Note that the main text's supporting citation here is a footnote-style endnote about unitary evolutions, not a prior paper: Appendix B is the derivation, not a pointer to one.

Appendix B opens with the sentence the survey is downstream of:

> "The cellular automata considered in the main text, rule 153, is such that the value at one site at the next iteration only depends on a site to its right and it is independent from those to the left. For this reason the evolution can be exactly described by a matrix product operator of bond dimension D = 2. However, in general, the 256 rules of cellular automata by Wolfram, can be exactly described by an MPO of bond dimension D = 4. We here describe two examples, rules 18 and 30."

It then writes the rule-30 MPO out. Five tensor types along the chain (Eqs. B1–B3 and their mirrors): a 1×2 first site, a 2×4 second site, 4×4 intermediate sites — the four matrices `W^{0,0}`, `W^{0,1}`, `W^{1,0}`, `W^{1,1}` are given explicitly, entrywise, all 0/1 — a 4×2 second-to-last site, and a 2×1 last site. "Since for both cases, rule 18 and rule 30, the maximum needed bond dimension is D = 4, there will be 5 types of tensors." This is an explicit, checkable construction, not an assertion. **Sub-question 1 and 2 are Established.**

Two qualifications follow immediately, and both matter for how the survey should use the number.

**It is not about rule 30.** The claim Guo et al. prove by construction is a claim about the *class*: D = 4 because an elementary rule reads three cells, so a left-to-right sweep needs to carry two bits of context, and 2² = 4. Rule 153, which depends on one neighbour only, needs D = 2; the paper's own long-range variant needs `D_W = 2^j` for interaction distance `j` and is run at `D_W = 8`. Rule 30's bond dimension is 4 for the same reason rule 110's and rule 18's are: it is a nearest-neighbour rule. Saying "rule 30 is expressible as an MPO with bond dimension 4" is true, and carries exactly as much information about rule 30 as saying it has 8 rows in its lookup table. **Sub-question 4 is Refuted.**

**The number is boundary-conditioned.** Guo et al. work with fixed boundaries, and say so in the same paragraph: "Rule 30 instead is chaotic, but not within fix boundary conditions considered here, and hence, with such boundary conditions the evolution becomes regular in a short time (periodic boundary conditions can be also considered with MPOs but in this case the bond dimension `D_W` could be the square of the fix boundaries condition case)." Under periodic boundaries the figure is 16, not 4 — and worth noticing for Mosaic specifically, the rule-30 chaos that makes it an interesting Class-III instance is *absent* in the setting where the D = 4 statement is made. **Sub-question 5 is Loose:** 4 is correct, and it is correct under a stated condition the survey does not carry.

## 3. Žunkovič (2022): the sentence the survey is almost quoting, and the number it disproves

*Deep tensor networks with matrix product operators*, Bojan Žunkovič, [arXiv:2209.09098v1](https://arxiv.org/abs/2209.09098) (16 Sep 2022), *Quantum Machine Intelligence* 4(21). This is the paper Žunkovič & Ilievski call the one their attention model is "a simplified version of". Its §5, *Sequence prediction with deep tensor networks*, is a rule-30 experiment, and contains:

> "We will consider the rule 30 one-dimensional automata, which exhibits chaotic behaviour. We can express the rule 30 automata as an MPO transformation with a bond dimension `D_MPO = 4` [14]."

Reference [14] is Guo et al. (2018). This is the sentence the survey's phrasing tracks almost word for word, and it is a citation to §2's construction rather than a new result. **Sub-question 3 is Established.**

The same section then destroys the tractability reading. Žunkovič's *trained* uniform-MPO model solves the one-step rule-30 prediction problem at **bond dimension 2**, below the exact representation: "we can solve the problem of predicting the next sequence for j = 1 for a finite fixed input size (e.g. N = 30) by using sigmoid activation functions and the bond dimension `D_MPO = 2`. Our trained solution for the standard rule 30 automata is more compact than the exact solution presented in [14]." The explanation offered is probabilistic — the model only needs the correct class to win, not the exact map — and the paper flags the result as notable: "it is interesting to observe that already for this simple task we find a more compact solution as the analytic MPO representation of the rule 30." Conversely, with a different activation the same architecture *fails* at D = 4 and only succeeds by adding a layer: "we were unable to solve the j = 1 problem with matrix exponential activation and even `D_MPO = 4`."

So inside the MPO framework itself, 4 is neither necessary (2 suffices with a sigmoid) nor sufficient (4 fails with a matrix exponential). It is the bond dimension of one exact analytic representation, not a tractability threshold. **Sub-question 6 is Refuted.**

Worth recording alongside it, because it is the real reason rule 30 is a hard sequence-prediction target rather than an easy one: Žunkovič's difficulty axis is *j*, the number of applications, and "Due to chaoticity, we expect that the bond dimension of a single MPO describing the j-step transition grows exponentially with j, i.e. `D_MPO(j) ≈ 4^j`." The whole argument of that paper is that shallow one-layer tensor networks are exponentially disadvantaged on rule 30 and depth is what recovers it. The MPO representation is small only for a single step.

## 4. Why "which is why it is tractable in this framework" fails

"This framework", in the survey bullet, is unambiguously Žunkovič & Ilievski's, since the bullet sits inside a list of what that paper does. Three things then go wrong at once.

**The framework has no MPOs in it.** Per §1, the acronym is absent from the [JMLR paper](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf) entirely. Its attention layer is built from MPS-style contractions of two tensors `A, B ∈ R^{d×d×2}`, and what tractability rests on there — established in [#48's reading](https://github.com/NGL321/mosaic/blob/research/debt-sweep-2026-08-02/docs/research/2026-08-02-zunkovic-ilievski-grokking-exponents.md) §5 — is freezing `A` so the layer collapses to a `D = 2d²`-dimensional feature map and the problem becomes a perceptron. The bond dimension that appears in the theory-comparison runs is **d = 2**, not 4.

**The number 4 has a different referent there.** Žunkovič & Ilievski's `4^K` is the dimension of *attention matrices* for a K-local rule — an existence claim about students, `4^1 = 4` for rule 30 — and their exact `A₀, A₁` are 4×4. The coincidence of the numeral is why the error is easy to make and why it is worth writing down: two different objects in two different papers by an overlapping author are both 4-dimensional for the same underlying reason (an elementary rule reads three cells), and neither is the other.

**Žunkovič & Ilievski cite the MPO line to say grokking is *not* there.** On page 24 of the JMLR PDF: "The rule-30 automaton has already been discussed in the context of sequence-to-sequence prediction with tensor networks Guo et al. (2018); Efthymiou et al. (2019); Žunkovič (2022), however, no grokking phenomena have been reported." That is the paper explicitly separating the MPO-representation literature from its own result. The survey's sentence fuses them and then uses the fused thing as the reason the grokking result is available. **Sub-question 7 is Refuted.**

## 5. What the survey should say instead

Deleting the sentence would lose a true and useful fact, so **sub-question 8 is Refuted**: the fix is re-sourcing and re-scoping, not deletion. Exact text is in *Proposals*. The three changes it makes are:

1. Attribute the MPO fact to [Guo et al. (2018)](https://arxiv.org/abs/1803.10908) and [Žunkovič (2022)](https://arxiv.org/abs/2209.09098), where it is derived and restated, rather than to Žunkovič & Ilievski, where it does not appear.
2. State it as a property of *elementary* rules, since D = 4 covers all 256 and therefore cannot be a reason to pick rule 30.
3. Drop the causal clause, and replace it with what actually makes the mapped problem solvable in Žunkovič & Ilievski — frozen, rejection-sampled attention tensors and a `D = 2d²` perceptron — which [#48](https://github.com/NGL321/mosaic/issues/48) already proposed text for. This document's replacement bullet is written to sit in place of that one, not beside it.

There is a small dividend for Mosaic beyond the correction. Guo et al. Appendix B is a *free exact reference model* for any ECA learning experiment: an explicit, entrywise, 0/1 tensor network that computes the rule. A representation-formation rung that wants to ask whether a learner has found the rule now has something to compare a learned representation against, and Žunkovič (2022) §5 is the demonstration that a trained model can be **more** compact than that reference — which is a concrete, published instance of the compression claim Mosaic's rung is about, in the substrate Mosaic has chosen. It is also a caution: the D = 4 statement holds under fixed boundaries, where rule 30 is not chaotic.

## What this does not establish

### Sources not reached

The two publisher records were attempted and refused: Physical Review E 98, 042114 returned HTTP 403, and Springer's *Quantum Machine Intelligence* 4(21) redirected to an authentication endpoint. Everything quoted from Guo et al. and Žunkovič is therefore from the arXiv PDFs — v3 and v1 respectively — and it is possible, though unlikely for an appendix of explicit tensors, that the published versions differ. Efthymiou et al. (2019), the third paper Žunkovič & Ilievski name in the same sentence as the MPO line, was not opened; it is not needed for any verdict here and no claim is attributed to it.

### Open gaps

Two. **First**, the tensors of Guo et al. Appendix B were read but not contracted; nobody in this repository has confirmed by computation that they reproduce rule 30, and doing so is a twenty-line exercise that would convert an Established verdict resting on a reading into one resting on a check. **Second**, and more valuable: Guo et al. assert D = 4 for all 256 rules and demonstrate it for two. The general construction is easy to believe — two bits of carried context — but it is asserted, not proved, in the only source that states it, and whether every elementary rule is *exactly* 4 rather than *at most* 4 is not settled by anything read here. Neither gap is load-bearing for the survey correction, which is why neither was filed as debt.

### Load-bearing ifs

The verdict on sub-question 7 turns on reading "this framework" in the survey bullet as Žunkovič & Ilievski's tensor-network attention model. If the sentence were instead meant loosely as "in tensor-network approaches to rule 30 generally", the causal clause becomes merely wrong rather than misattributed — §3 shows that even there D = 4 is neither necessary nor sufficient — so the proposed replacement survives either reading, but the sharpness of the "Refuted" does not. Second, §2's claim that D = 4 does not distinguish rule 30 rests on Guo et al.'s one sentence about all 256 rules; if that sentence were false and rule 30 were somehow special among elementary rules, the survey's original emphasis would be partially rehabilitated. Nothing read here suggests it is, and the three-cell-neighbourhood argument makes it very unlikely.

## Verification Debt

None. The ticket is discharged by sourcing, the two open gaps in §4 above are cheap and not load-bearing for any claim in `CONTEXT.md`, and filing either would put an item in the tracker that no downstream claim depends on.

## Proposals

Two, both for Noah to apply.

**(1) Replacement for the fourth bullet of survey §2.1** (`docs/research/2026-07-25-grokking-eca-tda-survey.md`, on `research/grokking-eca-tda-survey`). This supersedes the replacement bullet proposed in [#48's document](https://github.com/NGL321/mosaic/blob/research/debt-sweep-2026-08-02/docs/research/2026-08-02-zunkovic-ilievski-grokking-exponents.md) *Proposals* (1) — apply this one in its place, not both:

> - The concrete CA instance is **rule 30**, a single Class-III rule; 2-local and 3-local rules appear in an appendix. Tractability here is *not* an MPO property: for a K-local rule the authors exhibit `4^K`-dimensional **attention** matrices under which the mapped problem is solvable by a perceptron, the exact K=1 tensors are 4×4, and the minimal bond dimension of the exact solution drops to 2 if left and right attention tensors are trained separately. (Rule 30 *does* have an exact matrix-product-operator representation of bond dimension 4 — written out entrywise in [Guo, Jie, Lu & Poletti (2018)](https://arxiv.org/abs/1803.10908) Appendix B and restated in [Žunkovič (2022)](https://arxiv.org/abs/2209.09098) §5 — but that is a separate line of work, the figure is 4 for *all 256* elementary rules and so does not single out rule 30, it is the fixed-boundary value, and Žunkovič & Ilievski cite exactly those papers to note that "no grokking phenomena have been reported" in them.)

**(2) Optional addition to survey §4.3**, in the row on tensor-network analysis of the ECA learner, if Noah wants the dividend in §5 recorded:

> An exact 0/1 MPO for rule 30 is published and explicit ([Guo et al. 2018](https://arxiv.org/abs/1803.10908), Appendix B), which gives any ECA experiment a free reference model to compare a learned representation against; [Žunkovič (2022)](https://arxiv.org/abs/2209.09098) §5 already reports a *trained* model more compact than it (bond dimension 2 versus 4), which is a published instance of the compression claim this rung is about.

## Appendix: primary sources, all retrieved 2026-08-02

1. Guo, C., Jie, Z., Lu, W. & Poletti, D., *Matrix Product Operators for Sequence to Sequence Learning* — [arXiv:1803.10908v3, full PDF](https://arxiv.org/pdf/1803.10908v3), 13 pages. Read in full; §III A and Appendix B are where every quotation and every tensor dimension in §2 above comes from. Published as Phys. Rev. E 98, 042114 (2018); the publisher record was refused (403) and is not reached.
2. The same paper's [arXiv abstract page, 1803.10908](https://arxiv.org/abs/1803.10908). Used for version history (v1 29 Mar 2018, v2 1 May 2018, v3 3 May 2018), author list, and the journal reference.
3. Žunkovič, B., *Deep tensor networks with matrix product operators* — [arXiv:2209.09098v1, full PDF](https://arxiv.org/pdf/2209.09098), 13 pages. Read in full; §5 is the source of every quotation in §3 above. Published as *Quantum Machine Intelligence* 4(21), 2022; the Springer record redirected to authentication and is not reached.
4. The same paper's [arXiv abstract page, 2209.09098](https://arxiv.org/abs/2209.09098). Used for version history (v1 only, 16 Sep 2022), the journal reference and the DOI.
5. Žunkovič, B. & Ilievski, E., *Grokking phase transitions in learning local rules with gradient descent*, JMLR 25(199):1–52 — [full published PDF](https://www.jmlr.org/papers/volume25/22-1228/22-1228.pdf), 52 pages. Retrieved and searched exhaustively for `MPO`, `matrix product operator`, and the two citations; page 24 and the bibliography read directly. Not re-read in full — [#48](https://github.com/NGL321/mosaic/issues/48) did that.
6. Mosaic issue [#116](https://github.com/NGL321/mosaic/issues/116), the ticket this document discharges. Read in full including labels.
7. Mosaic research document [`docs/research/2026-08-02-zunkovic-ilievski-grokking-exponents.md`](https://github.com/NGL321/mosaic/blob/research/debt-sweep-2026-08-02/docs/research/2026-08-02-zunkovic-ilievski-grokking-exponents.md), the document that filed #116. Read in full; its §5 and §8 are what this document builds on and its *Proposals* (1) is what §5 above supersedes.
8. Mosaic survey [`docs/research/2026-07-25-grokking-eca-tda-survey.md` on `research/grokking-eca-tda-survey`](https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md). §2.1 read in full; it carries the sentence under test.
