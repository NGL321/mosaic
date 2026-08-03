---
ticket: 120
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 7
debt: []
supersedes: null
---

# Löhr was reached and does not state it: no source says E = 0 ⟺ i.i.d., but Shalizi & Crutchfield state the hard direction in an equivalent form for finite-entropy discrete processes

Seven primary sources were opened directly. **Wolfgang Löhr's PhD thesis** — the source
[#120](https://github.com/NGL321/mosaic/issues/120) names as the most likely home and records as
not reached — was retrieved as a PDF from the Leipzig repository and its excess-entropy material
read in full (§3.1.2, §3.2.1, §3.4.4, §4.1, §4.2); the rest was searched by keyword. **Löhr's
*Entropy* 2009 paper** was read in full (17 pp.) from the MDPI article-deploy PDF, the journal's
own HTML and `/pdf` endpoints both returning 403. **Shalizi & Crutchfield's** *Computational
Mechanics: Pattern and Prediction, Structure and Simplicity* was read in the sections that define
the entropy rate, patterns in ensembles, and excess entropy (§II D, §IV A–B). **Bradley's**
*Basic Properties of Strong Mixing Conditions* was read in §1.1, §2.1 and §4.1. **Dębowski's**
*A Short Course in Universal Coding* was read in Chapter 13 (*Excess*) in full. **Crutchfield &
Feldman** was re-opened in this session to check Propositions 6 and 7 and the definition
`h_μ(L) = H(L) − H(L−1)` at first hand rather than through
[#105](https://github.com/NGL321/mosaic/issues/105)'s quotation of them. **Bialek, Nemenman &
Tishby** was opened and its treatment of `I_pred` read (§§2–3 and the trichotomy of limiting
behaviours) specifically to look for a zero-characterisation; it has none.

The load-bearing distinction: this is a **retrieval** ticket and the retrieval **failed at the
target and partly succeeded beside it**. No source reached states `E = 0 ⟺ i.i.d.` as a theorem,
and Löhr — the best candidate anyone had — is now positively excluded rather than merely
unchecked. What was found instead is a near-miss with a stateable hypothesis gap (§3) and two
by-catch retrievals that discharge derivations #105 had to make for itself (§1, §4). Nothing
below re-argues the mathematics; #105 settled that.

## 0. Verdict

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | Löhr's thesis states `E = 0 ⟺ i.i.d.` as a theorem | **Refuted** — it makes "zero on i.i.d." a *definitional requirement* (Def. 4.5) and never states the converse | §1 |
| 2 | Löhr's thesis nonetheless improves Mosaic's footing on E | **Supported** — Def. 3.5 and Prop. 3.4 give the measure-theoretic definition Mosaic uses, on Souslin spaces | §1 |
| 3 | Löhr's *Entropy* (2009) paper states it | **Refuted** — it is about statistical complexity; its only i.i.d. statement is one-directional (Example 9) | §2 |
| 4 | Some reached source states the forward direction `E = 0 ⟹ i.i.d.` in an equivalent form | **Supported** — Shalizi & Crutchfield state `h[S⃗] = H[S] ⟹ IID` for stationary processes; Crutchfield & Feldman Prop. 6 converts | §3 |
| 5 | That near-miss discharges Mosaic's claim as stated | **Refuted** — three hypothesis gaps, and it is an unnumbered assertion, not a theorem | §3 |
| 6 | Mosaic's E already has a name and a coefficient in the mixing literature | **Established** — it is Bradley's information-regularity coefficient `I(1)` | §4 |
| 7 | "`I = 0` iff independence" is retrievable for σ-algebras, not only for random variables | **Established** — Bradley (1.10) | §4 |
| 8 | Dębowski states it | **Refuted** — Markov order, Theorem 13.5 and Exercise 13.72 circle it and stop | §5 |
| 9 | Any primary source states the equivalence as a theorem | **Open** — none of seven does, and the ticket's fallback discharge is the finding | §6 |
| 10 | #105's derived claim that E is not continuous on process space | **Established** — retrieved outright from Löhr Thm. 4.8 and Prop. 4.6; the period-p construction is no longer load-bearing | §1 |

> **The ticket's named home has been reached and read: Löhr defines excess entropy exactly as
> Mosaic does and treats vanishing-on-i.i.d. as an axiom he imposes rather than a theorem he
> proves, so the retrieval fails at its best candidate; the closest anyone comes is Shalizi &
> Crutchfield's one-sentence `h = H[S] ⟹ IID`, which is the forward direction for discrete
> processes of finite marginal entropy and is asserted, not proved — the general
> measure-theoretic equivalence remains Mosaic's own.**

## 1. Löhr's thesis: the definition Mosaic wants, and the theorem it does not contain

[Löhr's thesis](https://ul.qucosa.de/id/qucosa%3A11017) is where #120 sent this ticket, and it is
the right place to have sent it. §3.1.2 defines excess entropy the way Mosaic needs it — as a
mutual information between σ-algebras, on general spaces, with no limit-of-blocks caveat:

> "**Definition 3.5.** Let `X` be a stationary process with distribution `P ∈ P_s(Ω)`. We call
> `E(X) := E(P) := I(X_{≤0} : X_{>0})` excess entropy of `X` or of `P`."

and reconciles it with the block form as a proposition rather than a remark:

> "**Proposition 3.4.** Let `X` be a stationary process with distribution `P ∈ P_s(Ω)` and finite
> marginal entropy `H(X_1) < ∞`. Then `I(X_{≤0} : X_{>0}) = lim_n H(X_{[1,n]}) − n · h(P)`."

That is [Crutchfield & Feldman's](https://arxiv.org/abs/cond-mat/0102181) Propositions 7 and 8
merged into one statement with an explicit hypothesis (`H(X_1) < ∞`) where Crutchfield & Feldman
write "when the limit exists". #105 §2 assembled the same reconciliation from Polyanskiy & Wu's
monotone-convergence identity (4.31); **it is retrieved here in one proposition, for stationary
processes, in a source about excess entropy.** Löhr's ambient setting is a Souslin state space
throughout, which is the generality #105's proof claimed and had to justify itself.

**And then the theorem is not there.** Chapter 4 is where a characterisation of the zero locus
would live, and what Chapter 4 does with the value zero is make it a *hypothesis*:

> "**Definition 4.5.** For `P ∈ P_s(Ω)`, denote the ergodic decomposition by `ν_P ∈ P(P_e(Ω))`.
> We call a function `F : P_s(Ω) → ℝ₊` **entropy-based** if `F(P) = 0` for all i.i.d. processes
> `P`, and `F` satisfies `F(P) = H(ν_P) + ∫ F dν_P` for all `P ∈ P_s(Ω)`."

The remark immediately under it is the clearest single sentence in the literature about why the
converse is never proved — the property is wanted for what it buys, not for what it characterises:

> "b) The assumption that `F(P)` is zero for i.i.d. processes `P` is only needed to ensure that
> `F` is finite for enough processes. It is a very natural requirement for complexity measures of
> stochastic processes and often considered the crucial requirement ([FC98b]). It is obviously
> satisfied for excess entropy, statistical complexity, generative complexity and process
> dimension."

`F(P) = 0` for i.i.d. `P`. Not: `F(P) = 0` only for i.i.d. `P`. The citation `[FC98b]` is
[Feldman & Crutchfield's *Measures of Statistical Complexity: Why?*](https://csc.ucdavis.edu/~cmg/papers/mscw.pdf),
already read for #105 and already found to treat vanishing as a *boundary condition* a complexity
measure ought to satisfy. Löhr inherits that framing intact. **The most likely home for the
theorem turns out to be the source that most explicitly declines to prove it.**

§3.4.4 comes closer than anything else in the thesis, and is worth recording because it is the
route a future prover would take. Specialising his Proposition 3.59 (`I(X : Y) = ∫ D_KL(μ(Y|X) ‖ μ_Y) dμ`,
which he proves for Souslin spaces precisely because "We could not find the corresponding formula
for more general spaces in the literature") to past and future gives

> `E(P) = ∫ D_KL(P(X_{>0} | ·) ‖ P_{>0}) dP = ∫ D_KL(ν ‖ r μ_C(P)) dμ_C(P)`,

described in his words as "the excess entropy is the average Kullback-Leibler divergence from the
conditional distribution of the future to the unconditional one." `E = 0` therefore forces the
conditional law of the future given the past to equal its unconditional law almost surely — Step 1
of #105's proof, in one line, in full measure-theoretic generality. Löhr writes it as an
identity about the effect distribution and draws no conclusion about i.i.d. processes from it.

**By-catch that closes one of #105's own gaps.** #105 §6 argued that `{E < ε}` is not a
neighbourhood of the i.i.d. line because E is not continuous, and had to build a period-`p`
witness whose block-frequency concentration it could not verify against a source — carried there
under *Load-bearing ifs*. Löhr states the non-continuity outright:

> "**Theorem 4.8** (ergodic decomposition). The excess entropy is an entropy-based complexity
> measure, i.e. `E(P) = ∫ E dν_P + H(ν_P)` … In particular, `E` is concave, non-continuous, and
> generically infinite."

with **Proposition 4.6** supplying the mechanism — every entropy-based functional is
"non-continuous, even in variational topology", and if lower semi-continuous its infinite set is a
dense `G_δ`, so `F` is "generically infinite". Löhr's own **Proposition 4.7** supplies the lower
semi-continuity of E. So #105's directional conclusion is retrieved and strengthened: E is not
merely discontinuous, it is *generically infinite* on a dense `G_δ`, and the unverified period-`p`
construction is no longer carrying anything.

## 2. Löhr's *Entropy* (2009) paper: the same author, the same silence

The other Löhr work #120 gestures at is
[*Properties of the Statistical Complexity Functional and Partially Deterministic HMMs*](https://res.mdpi.com/entropy/entropy-11-00385/article_deploy/entropy-11-00385.pdf).
It is the journal version of the thesis's statistical-complexity chapter and it is **about `C`,
not about `E`**. Excess entropy appears twice, both times as a pointer elsewhere: the
introduction notes that "A formula for the ergodic decomposition of excess entropy, which is
another complexity measure" was obtained by Dębowski, and the conclusion repeats it. There is no
statement about the zero locus of either quantity.

Its one i.i.d. statement is Example 9, and it runs in the same direction as everything else:

> "**Example 9.** `μ_C` is not continuous. Let `P` be a non-deterministic i.i.d. (independent,
> identically distributed) process. Obviously, the causal state distribution of an i.i.d. process
> is the Dirac measure `P_ℕ` in its restriction `P_ℕ := P ∘ π_ℕ^{-1}` to positive time."

i.i.d. ⟹ one causal state ⟹ `C = 0`. The converse is not claimed, and `E` is not mentioned in the
example at all. **Verdict: the paper does not state it, and the thesis supersedes it for this
question.**

## 3. The nearest hit: Shalizi & Crutchfield state the forward direction — for a smaller class, and without proof

The one place in seven sources where the hard direction appears in substance is
[Shalizi & Crutchfield §II D](https://arxiv.org/abs/cond-mat/9907176), in the paragraph
introducing "patterns in ensembles", immediately before their Definition 3:

> "These entropy rates are also always bounded above by `H[S]`; which is a special case of
> Eq. (A3). Moreover, if `h[S⃗] = H[S]`, the process consists of independent variables —
> independent, identically distributed (IID) variables, in fact, since we are only concerned with
> stationary processes here."

That is `h_μ = H(S_1) ⟹ i.i.d.`, for stationary processes, with stationarity doing exactly the
work #105 §3 Step 4 gives it. The bridge to `E` is one line of a retrieved proposition. In
[Crutchfield & Feldman](https://arxiv.org/abs/cond-mat/0102181), `h_μ(L) := H(L) − H(L−1)`
(their Eq. 23), so `h_μ(1) = H(1) = H(S_1)`; their **Proposition 6** (Eq. 50) states "The excess
entropy is the intrinsic redundancy of the source: `E = Σ_{L=1}^∞ r(L)`" with `r(L) = h_μ(L) − h_μ ≥ 0`
termwise, since `h_μ(L)` is non-increasing. A sum of non-negative terms vanishes iff every term
does, so `E = 0 ⟹ r(1) = 0 ⟹ h_μ = H(S_1)`, and Shalizi & Crutchfield's sentence completes
`⟹ i.i.d.`

**This is a near-miss, and the difference is the finding.** Three gaps separate it from Mosaic's
statement, and they are not cosmetic:

1. **It is not stated about `E`.** The equivalence `E = 0 ⟺ h_μ = H(S_1)` is a step *Mosaic still
   supplies*, from Prop. 6 plus the monotonicity of `h_μ(L)`. Short, but derived.
2. **It needs finite marginal entropy, and a discrete alphabet.** Shalizi & Crutchfield work
   throughout with a discrete alphabet `A`, and their justification is "a special case of
   Eq. (A3)" — the independence bound on joint entropies, `H[X_1…X_n] ≤ Σ H[X_i]` with equality
   iff mutually independent. That is precisely the route #105 §3 identified and *declined*,
   because it "silently assumes finite block entropies". Mosaic's claim is for stationary
   processes on standard Borel spaces with no entropy assumption; this covers a strictly smaller
   class. Löhr's Proposition 3.4 shows the restriction is real and not pedantry — he attaches
   `H(X_1) < ∞` as an explicit hypothesis to the very identity that makes the two definitions of
   `E` agree.
3. **It is an aside, not a theorem.** No number, no proof, no name; a subordinate clause in a
   motivating paragraph, offered as background before Definition 3. It carries the epistemic
   weight of a remark, which is the whole distinction #120 exists to record. A step that is
   correct-because-a-source-asserts-it-in-passing is not at the same tier as one attached to a
   numbered result with a proof.

So the honest position after this ticket is: **the forward direction is retrievable in an
equivalent form for discrete stationary processes of finite marginal entropy, from two sources
that must be combined by a step neither of them takes.** The general statement — arbitrary
standard Borel alphabet, no entropy hypothesis, phrased about `E` — remains Mosaic's own
derivation. That is a real improvement on #105's position, which had nothing at all in the
forward direction, and it is not a discharge.

## 4. E has an established name outside computational mechanics, and the σ-algebra lemma is retrievable there

The search was widened on the hypothesis that the equivalence, if stated anywhere, would be stated
in the strong-mixing literature rather than in complexity theory, because that literature studies
`I(past ; future)` as a *dependence coefficient* rather than as a complexity measure.

[Bradley's survey](https://projecteuclid.org/journals/probability-surveys/volume-2/issue-none/Basic-Properties-of-Strong-Mixing-Conditions-A-Survey-and-Some/10.1214/154957805100000104.full)
defines, in his (2.2), the coefficient `I(n) := sup_{j∈ℤ} I(F^j_{−∞}, F^∞_{j+n})`, and records in
(2.3) that "In the special case where the sequence `X` is strictly stationary, one has simply
`α(n) = α(F^0_{−∞}, F^∞_n)`, and the same holds for the other dependence coefficients in (2.2)."
**Mosaic's excess entropy is exactly `I(1)` for a strictly stationary sequence** — Pinsker's
information between the past and the future, the coefficient whose decay to zero defines
*information regularity*. This is a naming fact worth having: it says where else to look, and it
explains the failure. The mixing literature is organised entirely around the *asymptotics* of
`I(n)` as `n → ∞` — Bradley's Theorem 4.1(3)(b), for a strictly stationary mixing sequence,
"Either `lim_n I(n) = 0` or `I(n) = ∞ ∀ n ≥ 1`" — and has no reason to characterise the processes
for which `I(1)` is exactly zero, because such a process is i.i.d. and therefore uninteresting to a
theory of weak dependence. **The exact-zero locus is the degenerate boundary of a field that
studies the interior.**

What Bradley does supply is the σ-algebra form of the step #105 took from Polyanskiy & Wu for
random variables. His (1.10) reads:

> "Each of the following equalities is equivalent to the condition that `A` and `B` are
> independent:"

and the displayed list ends with `I(A, B) = 0`, alongside `α(A,B) = 0`, `β(A,B) = 0`,
`ρ(A,B) = 0`, `φ(A,B) = 0`, `ψ′(A,B) = 1` and `ψ*(A,B) = 1`. #105's §2 got "`I = 0` iff
independence" from Polyanskiy & Wu Theorem 3.2(c), stated for random variables, and then needed
their (4.31) to lift it to semi-infinite σ-algebras. Bradley states it for arbitrary σ-fields
directly. Minor, but it removes one lift from the chain.

## 5. Dębowski: the inequality, the exercise, and the definition that stops one word short

[Dębowski's *A Short Course in Universal Coding*](https://home.ipipan.waw.pl/l.debowski/docs/monografie/IT_and_processes.pdf)
(draft dated 26 July 2024) is the most recent rigorous treatment of excess entropy by the author
[#105](https://github.com/NGL321/mosaic/issues/105) already found writing about it, and its
Chapter 13 is the closest a textbook gets. It defines `E := lim_n (H(X_1^n) − nh) = lim_n I(X^0_{−n+1}; X_1^n)`
(13.16), notes the monotonicity that makes the limit a supremum, and then defines:

> "**Definition 13.4 (Markov order)** Let `(X_i)_{i∈ℕ}` be a stationary ergodic process over a
> finite alphabet `X`. The Markov order of the process is defined as
> `M := inf { k ≥ 0 : H(X_i | X^{i−1}_{i−k}) = h }`. … According to the above, IID processes are
> 0-th order Markov processes."

`M = 0` is `H(X_i) = h`, which is Shalizi & Crutchfield's condition again; and his gloss runs
i.i.d. `⟹ M = 0`, not the converse. His **Theorem 13.5** then bounds
`E = sup_n I(X^0_{−n+1}; X^n_1) ≤ M log m`, so `M = 0 ⟹ E = 0` — the easy direction, retrieved as a
numbered theorem for finite alphabets. The hard direction is present in the book only as
**Exercise 13.72**: "For a stationary process `(X_i)_{i∈ℤ}`, show that `H(X_0) − h ≤ E`." Set
`E = 0` and that inequality yields `H(X_0) = h`, hence `M = 0`, hence — by his own gloss read
backwards, which he does not do — i.i.d.

**So the equivalence is, in Dębowski's book, an inequality in an exercise plus a definition read
in the direction he does not read it.** He never assembles them. That is a third independent
confirmation of the shape of the gap: every author has all the pieces and none of them states the
composite, because none of them needs it.

## 6. What the absence means

Three authors, in three research traditions, each hold the equivalence in parts and none states
it. Löhr, writing the most mathematically careful account of these functionals that exists, makes
"zero on i.i.d." an *axiom of the class he defines* and says explicitly why: it is imposed "only
… to ensure that `F` is finite for enough processes." Bradley's tradition studies `I(n) → 0` and
treats `I(1) = 0` as the degenerate case it never has to name. Dębowski's treats zero excess
entropy as the trivial endpoint of a theory about growth rates and Hilberg exponents.

The common cause is the one #120 anticipated: **the exact-zero locus is not an object anyone in
this literature has a use for.** It is a single point of a theory whose content is everywhere
else — the rates, the asymptotics, the divergences. A characterisation of it would be, for these
authors, a remark; and remarks about degenerate cases do not get written down as theorems. That
is the recorded finding the ticket names as its fallback discharge, and it is now supported by a
positive exclusion of the best candidate rather than by an inconclusive search.

The operational consequence for Mosaic is unchanged from #105 §6 and is in fact reinforced. If no
author finds the exact-zero locus worth a theorem, an *exclusion criterion* keyed to it is keyed
to something the field regards as a measure-zero curiosity — which is the same conclusion
`E = 0 ⟹ i.i.d.` reaches from the other side, and the reason "excluded on Informational Capacity"
must read `E < ε`. Nothing here bears on whether `E < ε` is estimable; that remains
[#99](https://github.com/NGL321/mosaic/issues/99) and
[#107](https://github.com/NGL321/mosaic/issues/107).

## What this does not establish

### Sources not reached

Four wanted sources were not opened. **Bradley's *Introduction to Strong Mixing Conditions*
(Kendrick Press, 2007), Chapter 22** — his survey says of the `I(n)` dichotomy that "The material
here in section 4.1 is treated in detail in [43, Chapter 22]", so if a remark on `I(1) = 0` exists
in Bradley's writing it is most likely there; no legitimately openable copy was found, and the
survey stands in for it here. **M. S. Pinsker, *Information and Information Stability of Random
Variables and Processes* (Holden-Day, 1964)** — the origin of the information-regularity
coefficient and the other plausible home for a zero characterisation; not reachable, and known
here only through Bradley's attribution. **Löhr & Ay, *Predictive models and generative
complexity*, J. Syst. Sci. Complex. 25 (2012)** — paywalled at
`https://link.springer.com/article/10.1007/s11424-012-9173-x`; it is the journal version of the
thesis's generative-complexity chapter, and the thesis was read in its place, but the substitution
was not verified section by section. **Dębowski, *Information Theory Meets Power Laws* (Wiley,
2021)** — paywalled at `https://www.oreilly.com/library/view/information-theory-meets/9781119625278/`;
his 2024 course notes were read instead and treat the same material, but the book is longer and
may state more. Two further URLs failed outright and are recorded for the next attempt:
Löhr's publication list at `https://www.uni-due.de/~hm0112/publications/` (HTTP 410 Gone) and the
MDPI article pages `https://www.mdpi.com/1099-4300/11/3/385` and `…/pdf` (HTTP 403; the
`res.mdpi.com` article-deploy PDF served the full text and is what was read).

### Open gaps

The search covered computational mechanics, the strong-mixing literature and universal coding. It
did not cover **ergodic theory proper** — Ornstein-theory and K-process texts, where "the past is
independent of the future" is a natural object and where a characterisation could plausibly sit
under different vocabulary — nor the **Gaussian-process** literature, where past–future
independence is a spectral condition and Bradley's §7 suggests the coefficients are computable in
closed form. Whether the equivalence holds verbatim for **two-sided processes indexed by ℤ versus
one-sided by ℕ** was not separately checked in any source; Löhr and Bradley index by ℤ, Dębowski
by ℕ in places and ℤ in others, and the stationarity argument transports between them but no
source says so. Finally, the exact relationship between Löhr's `μ_C`-based formula in §3.4.4 and a
clean proof of the general statement was not pursued: it looks like the shortest available route
to a fully general theorem, and writing it is a *proof* task, not a retrieval one.

### Load-bearing ifs

If Shalizi & Crutchfield's `h[S⃗] = H[S]` means something other than "entropy rate equals
single-symbol entropy" — their `S` denotes both the causal-state variable and the observed random
variable in different parts of the paper — then §3's near-miss evaporates and the forward
direction has no retrieval at all. The reading taken here is fixed by their surrounding sentence,
which bounds the entropy rates "above by `H[S]`" via the independence bound on joint entropies,
and by their citing Eq. (A3) for it; but the notation is genuinely overloaded. If Crutchfield &
Feldman's `r(L) = h_μ(L) − h_μ` were not termwise non-negative — that is, if `h_μ(L)` were not
non-increasing — the bridge from `E = 0` to `h_μ = H(S_1)` in §3 fails; they state the monotonicity
and #105 §2 derives it independently, so this is secure but it is where the weight sits. If
Löhr's Definition 4.5 were read as a *characterisation* of entropy-based functionals rather than
as a definition of the class, §1's verdict would invert; the remark under it, quoted in full,
forecloses that reading. And the whole document's negative verdict is a claim about seven
sources, not about the literature: a single citation in a text not opened here would move
sub-question 9 from **Open** to **Established**.

## Verification Debt

None. This document is itself the discharge of
[#120](https://github.com/NGL321/mosaic/issues/120) by its recorded-finding branch, and the gaps
it opened are of a kind the contract carries under *Open gaps* rather than as tracker items: the
unsearched literatures (ergodic theory, Gaussian processes) are places a future searcher might
look, not defects in a standing claim, and filing "search somewhere else too" as debt would be the
ceremony [`PROTOCOL.md` §5](../../PROTOCOL.md) warns against. Two adjacent questions found here
are **already on the tracker** and are not re-filed: whether `E` or a threshold `E < ε` is
estimable from finite data is [#99](https://github.com/NGL321/mosaic/issues/99) and
[#107](https://github.com/NGL321/mosaic/issues/107). One item of existing debt is *reduced* rather
than created — #105's *Load-bearing ifs* entry on the unverified period-`p` block-frequency
construction is superseded by Löhr's Theorem 4.8 and Proposition 4.6 (§1), which state the
non-continuity of `E` outright.

## Proposals

Two amendments to
[`docs/research/2026-08-02-zero-excess-entropy-and-iid.md`](2026-08-02-zero-excess-entropy-and-iid.md),
which is the document #120 was filed against. Neither changes a verdict there; both record what
retrieval has since found. Applying them is Noah's call.

**1. Replace sub-question 6's verdict row** in that document's §0 table:

| 6 | Some primary source states the equivalence as a theorem | **Open** — none found across thirteen sources in two sessions; the closest is Shalizi & Crutchfield's unnumbered `h_μ = H(S_1) ⟹ IID`, retrieved under [#120](https://github.com/NGL321/mosaic/issues/120) | §3 |

**2. Append to that document's *Load-bearing ifs*,** after the sentence beginning "And the
concrete period-p construction in §6":

> **Superseded by [#120](https://github.com/NGL321/mosaic/issues/120).** The period-`p` witness is
> no longer load-bearing: [Löhr's thesis](https://ul.qucosa.de/id/qucosa%3A11017) Theorem 4.8
> states that excess entropy is "concave, non-continuous, and generically infinite", and his
> Proposition 4.6 gives non-continuity "even in variational topology" for every entropy-based
> functional. The finding of §6 stands on a retrieved theorem and no longer on an unverified
> construction.

## Appendix: primary sources, all retrieved 2026-08-02

1. Wolfgang Löhr, *Models of Discrete-Time Stochastic Processes and Associated Complexity Measures*, PhD thesis, Universität Leipzig, defended 12 May 2010 (advisors Nihat Ay and Jürgen Jost); PDF from the Leipzig Qucosa repository, ~120 pp. — §3.1.2 (Proposition 3.4, Definition 3.5, Proposition 3.6), §3.2.1 (Definitions 3.7–3.8, Lemma 3.9, Proposition 3.10), §3.4.4 (Proposition 3.59 and the `μ_C` formula for `E`), §4.1 (Definition 4.5 and its remark, Proposition 4.6) and §4.2 (Propositions 4.7, Theorem 4.8) read in full; remainder searched by keyword for "excess entropy", "i.i.d.", "vanish". **The ticket's named target; contains no statement of the equivalence.** https://ul.qucosa.de/id/qucosa%3A11017
2. Wolfgang Löhr, *Properties of the Statistical Complexity Functional and Partially Deterministic HMMs*, Entropy **11**(3):385–401 (2009), doi:10.3390/e110300385, 17 pp. — read in full from the article-deploy PDF after the journal's HTML and `/pdf` endpoints returned 403. Example 9 (i.i.d. ⟹ Dirac causal-state distribution); Propositions 23; the introduction and conclusion, which refer excess entropy to Dębowski. Searched-and-negative. https://res.mdpi.com/entropy/entropy-11-00385/article_deploy/entropy-11-00385.pdf
3. Cosma Rohilla Shalizi and James P. Crutchfield, *Computational Mechanics: Pattern and Prediction, Structure and Simplicity*, Journal of Statistical Physics **104**:817–879 (2001), arXiv:cond-mat/9907176 — §II C–D read in full (Eqs. 7–11, the entropy-rate paragraph containing the `h[S⃗] = H[S] ⟹ IID` sentence, Definition 3), plus Definition 13 and Theorem 5 (`E ≤ C_μ`) in §IV. **The nearest hit in the literature.** https://arxiv.org/abs/cond-mat/9907176
4. Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys **2** (2005) 107–144 — §1.1 (the dependence coefficients, ranges (1.9), the independence equivalences (1.10), inequalities (1.11)–(1.18)), §2.1 (definitions (2.2), the stationary reduction (2.3), the mixing hierarchy) and §4.1 (Theorem 4.1) read in full. Establishes that Mosaic's `E` is the information-regularity coefficient `I(1)`. https://projecteuclid.org/journals/probability-surveys/volume-2/issue-none/Basic-Properties-of-Strong-Mixing-Conditions-A-Survey-and-Some/10.1214/154957805100000104.full
5. Łukasz Dębowski, *A Short Course in Universal Coding*, Institute of Computer Science, Polish Academy of Sciences; draft dated 26 July 2024, ~180 pp. — Chapter 13 (*Excess*) read in full: the excess bounds, Eq. (13.16) defining `E`, Definition 13.2 (Hilberg exponent), Theorem 13.3, Definition 13.4 (Markov order), Theorem 13.5, Definition 13.6 and Theorem 13.7 (Markov order estimation), the "Further reading" note attributing excess entropy to Crutchfield and Feldman, and the thinking exercises including (13.72). Retrieval date matters: this is a live draft. https://home.ipipan.waw.pl/l.debowski/docs/monografie/IT_and_processes.pdf
6. James P. Crutchfield and David P. Feldman, *Regularities Unseen, Randomness Observed: Levels of Entropy Convergence*, arXiv:cond-mat/0102181, 35 pp. — re-opened in this session (it was read in full for [#105](https://github.com/NGL321/mosaic/issues/105)) to verify at first hand Eq. (23) `h_μ(L) = H(L) − H(L−1)`, Eq. (48), Proposition 6 / Eq. (50) (`E` as intrinsic redundancy), Proposition 7 / Eq. (51) and Proposition 8 / Eq. (53), on which §3's bridge from `E = 0` to `h_μ = H(S_1)` depends. https://arxiv.org/abs/cond-mat/0102181
7. William Bialek, Ilya Nemenman and Naftali Tishby, *Predictability, Complexity and Learning*, arXiv:physics/0007070 (Neural Computation **13**:2409–2463, 2001), 65 pp. — the PDF was opened and §§2–3 read, covering Eqs. (4)–(14) defining `I_pred(T)` as the subextensive entropy `S_1(T)`, and the trichotomy of limiting behaviours (bounded, logarithmic, sublinear power). Opened specifically to check whether the `I_pred = 0` case is characterised; it is not — the paper's content is entirely in the divergent regime, and the bounded case is discussed only via periodic processes. Searched-and-negative. https://arxiv.org/abs/physics/0007070
