---
ticket: 105
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 6
debt: [120]
supersedes: null
---

# For a stationary process, E = 0 if and only if the process is i.i.d. — true, but nowhere retrieved: the equivalence is derived here from four cited theorems

Six primary sources were opened and read directly, five of them in full: Crutchfield & Feldman's
*Regularities Unseen, Randomness Observed* (the arXiv PDF, all 35 pages), Feldman, McTague &
Crutchfield's *The Organization of Intrinsic Computation* (all 18 pages), Feldman &
Crutchfield's *Measures of Statistical Complexity: Why?* (all 7 pages), Bradley & Pruss's
*A strictly stationary, N-tuplewise independent counterexample to the central limit theorem*
(all 25 pages), and Dębowski's *Excess entropy in natural language* (all 12 pages). The sixth,
Polyanskiy & Wu's *Information Theory: From Coding to Learning*, is a 730-page book; its
Chapter 1 §1.1, Chapter 3 §§3.1 and 3.4, and Chapter 4 §4.7 were read in full and everything
cited from it below comes from those sections. **Cover & Thomas was not reached** — see
*Sources not reached*.

The load-bearing distinction in this document: the **direction i.i.d. ⟹ E = 0 is retrieved**,
stated in as many words by Crutchfield & Feldman. The **direction E = 0 ⟹ i.i.d. is derived
here**, in §3, from four separately cited theorems in Polyanskiy & Wu plus stationarity. No
source was found that states the equivalence, or that direction of it, as a theorem — which is
exactly the defect [#105](https://github.com/NGL321/mosaic/issues/105) names, and this document
does not pretend to have fixed it by retrieval. What it does is make the derivation
step-by-step citable rather than gestural, and confirm by a genuine counterexample search that
the derivation is not merely plausible but correct.

## 0. Verdict

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | E is defined as the mutual information between the semi-infinite past and future | **Established** — Crutchfield & Feldman, Prop. 8 | §1 |
| 2 | i.i.d. ⟹ E = 0 | **Established** — stated in the source, for the fair *and* the biased coin | §1 |
| 3 | E = 0 in the limit-of-finite-blocks sense ⟺ every finite past/future cut is independent | **Supported** — monotonicity plus Polyanskiy & Wu Thm 3.2(c),(e) | §2 |
| 4 | The limit definition and the semi-infinite-σ-algebra definition agree | **Supported** — Polyanskiy & Wu (4.31) | §2 |
| 5 | E = 0 ⟹ the process is i.i.d., for an arbitrary stationary process | **Supported** — **derived here**, not retrieved; proof in four cited steps | §3 |
| 6 | Some primary source states the equivalence as a theorem | **Open** — none found after a genuine search across six sources | §3 |
| 7 | A stationary, non-i.i.d. process with exactly E = 0 exists | **Refuted** — the proof in §3 forecloses it; the sharpest near-miss in the literature confirms where the gap is | §4 |
| 8 | Feldman, McTague & Crutchfield (2008) establishes the claim | **Refuted** — three restrictions in their own words, and the implication runs the other way | §5 |
| 9 | "Excluded on Informational Capacity" must be a threshold on small E, not a test for zero | **Supported** | §6 |
| 10 | The third exclusion case is "the biased-i.i.d. line **and its neighbourhood**, unique up to the bias parameter" | **Loose** on "unique up to the bias parameter" (binary only); **Refuted** on "neighbourhood" | §6 |

> **The claim under audit is true — E = 0 ⟺ i.i.d. for any stationary process, with no
> counterexample possible — but it remains a derivation, not a retrieval, and the consequence
> the ticket draws holds only in half: the exclusion must indeed become a threshold on small E,
> but the resulting set is not a *neighbourhood* of the i.i.d. line, because E is not continuous
> on the space of stationary processes.**

## 1. What excess entropy is, in the source that defines it

[Crutchfield & Feldman](https://arxiv.org/abs/cond-mat/0102181) define a process as the joint
distribution over the bi-infinite chain, and give i.i.d. its own definition (their Eq. 3):
a process is i.i.d. if `Pr(S↔) = … Pr(S_i)Pr(S_{i+1})Pr(S_{i+2}) …` and `Pr(S_i) = Pr(S_j)`
for all `i, j`. That is the target predicate for the whole of this document: full
factorisation of the joint law plus a common marginal. It is *not* pairwise independence, and
§4 turns on the difference.

Their excess entropy is introduced as the subextensive part of the block entropy
(**Proposition 7**, Eq. 51): `E = lim_{L→∞} [H(L) − h_μ L]`, equivalently as the summed
convergence excess `E = Σ_{L=1}^{∞} [h_μ(L) − h_μ]`. The mutual-information form is a
separate proposition (**Proposition 8**, Eq. 53):

> "The excess entropy is the mutual information between the left and right (past and future)
> semi-infinite halves of the chain ↔S : `E = lim_{L→∞} I[S_0 S_1 ⋯ S_{2L−1} ; S_{2L} S_{2L+1} ⋯ S_{4L−1}]`
> … when the limit exists."

They add, in the same paragraph, "Note that E is not a two-symbol mutual information, but is
instead the mutual information between two semi-infinite blocks of variables." So the ticket's
framing — E = I[past ; future] — is the source's own, with the caveat that the source states it
as a *limit of finite blocks*, not directly as an information between σ-algebras. §2 closes
that gap.

The easy direction is retrieved outright. In §VI A, on i.i.d. processes, they compute the fair
coin and a coin of bias 0.7 and conclude:

> "As is clear from Fig. 5, for both processes the excess entropy E and the transient
> information T are zero. … Each coin flip does not depend on past flips, and so there is no
> mutual information between the past and the future. Thus, E = 0."

This is the whole biased-i.i.d. line, at E = 0, in the source, with a worked non-fair example —
and it already contradicts any reading of §5's Feldman–McTague–Crutchfield result as
enumerating the E = 0 locus. Two further values are used later: **Proposition 10**,
`E = log₂ p` for a period-p process (Eq. 56), and **Proposition 11**, `E = H(R) − R h_μ` for an
order-R Markov process (Eq. 57). The second gives i.i.d. ⟹ E = 0 a second time, since an
i.i.d. process is order-1 Markov with `h_μ = H(1)`.

What the source conspicuously does **not** say is the converse. Its own process taxonomy in
§VIII A reads: "**Memoryless processes**: For these, H(L) scales as h_μ L and h_μ(L) converges
immediately to h_μ. We have E = 0 and T = 0. Independent, identically distributed (IID)
processes are examples of this class." *Examples of* — the sentence is written so as not to
claim that the class contains nothing else. The same reticence appears in
[Feldman & Crutchfield's earlier review](https://csc.ucdavis.edu/~cmg/papers/mscw.pdf), which
treats vanishing E as a "boundary condition" a complexity measure ought to satisfy and observes
only, of a specific family, that "For maximal randomness (h_μ = 1), the excess entropy E
vanishes, as expected. At h_μ = 1, corresponding to infinite temperature, the spins decouple
and there is no information shared between them." A statement about one point of one Ising
family, not a characterisation.

## 2. E = 0 is exactly "every finite cut is independent", and the two definitions agree

Write `a_L := I[X_{−L}^{−1} ; X_0^{L−1}]` for a stationary process. Two facts about mutual
information, both from [Polyanskiy & Wu](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf)
Theorem 3.2, and both stated there for random variables on general (not merely discrete)
spaces, since their Definition 3.1 is `I(X;Y) = D(P_{X,Y} ‖ P_X P_Y)`:

- **Thm 3.2(c)**: "(Positivity) `I(X;Y) ≥ 0`, with equality `I(X;Y) = 0` iff `X ⊥⊥ Y`."
- **Thm 3.2(e)**: "(More data ⟹ more information) `I(X₁, X₂; Z) ≥ I(X₁; Z)`."

Applying (e) to each argument in turn makes `a_L` nondecreasing in `L`; (c) makes it
nonnegative. A nondecreasing nonnegative sequence has a limit equal to its supremum, so
**E = 0 if and only if `a_L = 0` for every L**, and by (c) that is exactly: for every L, the
length-L past block is independent of the length-L future block. This is a derivation, but a
one-line one from two quoted theorems.

The ticket asks specifically about "the whole past independent of the whole future", which is a
statement about the semi-infinite σ-algebras rather than about finite blocks. Polyanskiy & Wu
§4.7 closes that by (4.31), "**(Monotone convergence I)** … `I(X^∞ ; Y^∞) = lim_{n→∞} I(X^n ; Y^n)`",
with the gloss that "the full amount of mutual information between two processes X^∞ and Y^∞ is
contained in their finite-dimensional projections, leaving nothing in the tail σ-algebra." So
Crutchfield & Feldman's limit-of-blocks E and the information between the two semi-infinite
halves are the same number, and vanish together. No separate argument is needed for the
infinite case.

The same section is worth reading for what it rules *out* as a route to a counterexample. Their
(4.32) concerns the tail σ-algebra, and their worked example is that for `X_j` i.i.d. Ber(1/2)
and `Y = X_0^∞`, "each `I(X_n^∞ ; Y) = 1`, but `X_tail` = constant a.e. by Kolmogorov's 0-1 law".
Tail triviality is therefore a strictly weaker condition than past–future independence: a
process can have a trivial tail and still carry information across every cut. Anyone hunting a
counterexample among K-processes or mixing processes — the ticket names them as a candidate
source — is hunting in a class defined by the weaker condition, and §4 says what happens there.

## 3. E = 0 ⟹ i.i.d.: the proof, derived here and not retrieved

**This section is a derivation.** Each step cites a theorem, but the composite statement was
not found in any of the six sources read; see sub-question 6 and *Open gaps*. Assume
`(X_n)_{n∈ℤ}` is stationary with values in a standard Borel space, and that E = 0.

**Step 1 (every cut, every width).** By §2, `a_L = 0` for all L. Fix `n ≥ 2` and `1 ≤ k ≤ n−1`.
Taking `L = n` gives `X_{−n}^{−1} ⊥⊥ X_0^{n−1}`. Shifting by `k` — legitimate because the
process is stationary, which is the *only* place stationarity is used before Step 4 — gives
`X_{k−n}^{k−1} ⊥⊥ X_k^{n+k−1}`, hence `I[X_{k−n}^{k−1} ; X_k^{n+k−1}] = 0` by
[Polyanskiy & Wu](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf) Thm 3.2(c).

**Step 2 (restrict to the block).** Since `k ≤ n`, the block `X_0^{k−1}` is a coordinate
projection of `X_{k−n}^{k−1}`; since `k ≥ 1`, the block `X_k^{n−1}` is a coordinate projection
of `X_k^{n+k−1}`. Thm 3.2(d) — "(Deterministic maps) For any function f we have
`I(f(X); Y) ≤ I(X; Y)`" — applied on each side gives
`0 ≤ I[X_0^{k−1} ; X_k^{n−1}] ≤ I[X_{k−n}^{k−1} ; X_k^{n+k−1}] = 0`. By Thm 3.2(c) again,
`X_0^{k−1} ⊥⊥ X_k^{n−1}` **for every `1 ≤ k ≤ n−1`**. This is the step the ticket flags as the
one to get right: E = 0 gives independence across *one* cut per block length, and stationarity
is what transports that single cut to every interior position of every block.

**Step 3 (factorise, by induction on n).** For Borel sets `A_0, …, A_{n−1}`, the case `k = 1`
of Step 2 gives `P[X_0∈A_0, …, X_{n−1}∈A_{n−1}] = P[X_0∈A_0] · P[X_1∈A_1, …, X_{n−1}∈A_{n−1}]`.
By stationarity the second factor equals `P[X_0∈A_1, …, X_{n−2}∈A_{n−1}]`, to which the
induction hypothesis applies; the base case `n = 1` is trivial. Hence every finite-dimensional
distribution is the product of its one-dimensional marginals, which is mutual independence of
the whole family `{X_n}`.

**Step 4 (identically distributed).** Stationarity gives `P_{X_i} = P_{X_j}` for all `i, j`.
Together with Step 3 this is precisely
[Crutchfield & Feldman's](https://arxiv.org/abs/cond-mat/0102181) definition of i.i.d. (their
Eq. 3). ∎

Three remarks on the shape of the proof.

**It needs no finite entropy.** A shorter argument is available for finite alphabets — Thm
3.7(e), "(Full chain rule) `I(X^n; Y) = Σ_k I(X_k; Y | X^{k−1})`", together with Theorem 1.4(g),
"(Full chain rule) `H(X_1,…,X_n) = Σ H(X_i|X^{i−1}) ≤ Σ H(X_i)`, with equality iff `X_1,…,X_n`
are mutually independent" — but that route silently assumes finite block entropies. The
factorisation route above uses only Thm 3.2(c) and (d), both of which Polyanskiy & Wu state via
divergence and so hold on standard Borel spaces. The result is therefore not an artefact of
finite alphabets, which matters because the Mosaic use of E is not restricted to them.

**Stationarity is indispensable, and does close the gap.** Without it, the implication fails on
its face: a non-stationary process independent across the single cut at time 0 but with
`X_1 = X_2` is a counterexample to Step 2 at `k = 2`. What stationarity buys is that the *one*
independence statement E = 0 delivers is simultaneously an independence statement at every
integer split point, and it is the conjunction over all split points — not any single one —
that forces full factorisation.

**The converse direction is retrieved, not derived.** i.i.d. ⟹ E = 0 is
[Crutchfield & Feldman](https://arxiv.org/abs/cond-mat/0102181) §VI A, quoted in §1 above, and
also follows from their Proposition 11. So exactly one half of the equivalence rests on this
document's own reasoning.

## 4. The counterexample search: what the near-misses are, and why none of them lands

A proof forecloses a counterexample only if the proof is right, so the search was run
independently, and it is instructive about *where* a wrong derivation would have gone wrong.

The natural attempt is a process whose variables are independent in every small collection but
not jointly — the XOR triple `X_2 = X_0 ⊕ X_1`, generalised. This is a real phenomenon and it
survives stationarity: [Bradley & Pruss](https://arxiv.org/abs/0810.1707) construct, "for an
arbitrary integer N ≥ 2 … a strictly stationary, N-tuplewise independent sequence of
(nondegenerate) bounded random variables such that the Central Limit Theorem fails to hold",
where N-tuplewise independence means "for every choice of N distinct integers k(1), …, k(N),
the random variables X_{k(1)}, …, X_{k(N)} are independent". Their introduction also records
Flaminio's example: "a strictly stationary, finite-state, N-tuplewise independent random
sequence X := (X_k, k ∈ ℤ) which also has zero entropy and is mixing (in the ergodic-theoretic
sense)". These are stationary, arbitrarily-highly-tuplewise-independent, non-i.i.d. processes —
about as close to a counterexample as anything in the literature gets.

They are not counterexamples, and the reason is exactly Step 2. N-tuplewise independence
constrains *sets of N individual coordinates*; E = 0 constrains *whole blocks* on either side
of a cut, which is a strictly stronger demand as soon as the block exceeds N symbols. In
Bradley and Pruss's sequences the failure of full independence must show up as
`I[X_{−L}^{−1} ; X_0^{L−1}] > 0` for some L, and by §2 that makes E > 0 however large N is.
Flaminio's example makes the point sharply from the other side: it has `h_μ = 0`, and
[Crutchfield & Feldman's](https://arxiv.org/abs/cond-mat/0102181) Proposition 7 notes "if
h_μ = 0, then E = lim_{L→∞} H(L)" — so a non-degenerate zero-entropy-rate process has E equal
to its total block entropy, the opposite of zero.

The second attempt is the ergodic-theoretic one the ticket names: a K-process, or any process
with trivial tail σ-algebra. §2 disposes of it — Polyanskiy & Wu's own Kolmogorov-0-1-law
example has trivial tail and `I = 1` across every cut. Tail triviality is a statement about
what survives *infinitely far* into the future; E = 0 is a statement about what crosses a
finite cut. They are not the same condition and the second is much stronger.

The third attempt is to look for slack in the definition — a process where the limit in
Crutchfield & Feldman's Proposition 8 is zero while some finite-block information is positive.
The monotonicity in §2 rules that out: `a_L` is nondecreasing, so the limit is the supremum and
cannot be zero unless every term is.

No candidate survives. **Verdict: Refuted** — no stationary, non-i.i.d. process has exactly
E = 0.

## 5. What Feldman, McTague & Crutchfield (2008) does and does not license

The ticket already suspected this source of being corroborating rather than establishing. It is
worse than that: the class it enumerates *excludes by construction* most of the E = 0 locus.

[The paper](https://arxiv.org/abs/0806.4789) says, of its enumeration: "The minimum complexity,
E = 0, corresponds to machines with only a single state. There are two possibilities for such
binary ǫ-machines. Either they generate all 1s (or 0s) or all sequences occurring with equal
probability (at each length). If the latter, then h_μ = 1; if the former, h_μ = 0. These two
points, (0, 0) and (1, 0), are denoted with solid circles along Fig. 9's horizontal axis."

Three restrictions are stated in the paper's own words, in the paragraphs immediately before:

1. **Fair branching.** "We do this by restricting attention to the class of topological
   ǫ-machines whose branching transition probabilities are fair (equally probable)." A biased
   coin is a single-state machine with branching probabilities `p, 1−p`; it is therefore *not
   in the enumerated class at all*. This is precisely why the paper finds two E = 0 points
   rather than the whole segment `h_μ ∈ [0,1]` that Crutchfield & Feldman's own §VI A puts
   there (§1). The result is an artefact of the sampling scheme, not a fact about processes.
2. **Binary alphabet.** "Here we consider only ǫ-machines for binary processes: A = {0, 1}."
3. **Finitely many states.** "the topological ǫ-machines with a finite number of states can be
   systematically enumerated". Nothing is said about infinite-state or non-finitary stationary
   processes, which is where a counterexample would most plausibly have hidden.

And the implication direction is as the ticket says: the sentence reads *single state ⟹ E = 0*
(and "minimum complexity" is a claim about the enumerated set having no smaller value), not
*E = 0 ⟹ single state*, and certainly not *E = 0 ⟹ i.i.d.* over stationary processes.

What it *does* license: within finite-state, binary, fair-branching topological ǫ-machines,
E = 0 occurs and occurs only at two points. That is consistent with the theorem of §3 —
restricting to fair branching leaves exactly two i.i.d. processes, the fair coin and the point
mass — and consistency is all it is. **It corroborates and cannot establish.**

## 6. The consequence for the third exclusion case

The ticket names the consequence: *if exact E = 0 forces i.i.d., then "excluded on Informational
Capacity" must be a threshold on small E rather than a test for zero, and the third exclusion
case is the biased-i.i.d. line and its neighbourhood, unique up to the bias parameter.* The
antecedent holds (§3). The consequent holds in part.

**The threshold half holds.** `{E = 0}` is exactly the set of i.i.d. processes, an extremely
thin set inside the stationary processes: on a binary alphabet it is a one-parameter family,
while the surrounding space is infinite-dimensional. A test for exact zero would exclude
essentially nothing, and would be undecidable from any finite sample. So an operational
exclusion has to read `E < ε`. **Supported.**

**"Unique up to the bias parameter" is loose.** On a binary alphabet the i.i.d. processes are
parameterised by a single bias `b ∈ [0,1]`, with `h_μ = H(b)`, so the phrasing is exact —
this is the segment [Crutchfield & Feldman](https://arxiv.org/abs/cond-mat/0102181) exhibit in
§VI A with their fair and `p = 0.7` coins. On an alphabet of size `|A|`, the E = 0 set is the
whole `(|A|−1)`-dimensional simplex of marginals. It remains a *one-dimensional curve* in the
`(h_μ, E)` complexity–entropy plane, because only `H(marginal)` is visible there, but it is not
a one-parameter family of processes. If the Mosaic claim is about the diagram, it survives; if
it is about the processes, "unique up to the marginal distribution" is the correct phrasing.
**Loose.**

**"And its neighbourhood" is refuted as stated.** `{E < ε}` is not a neighbourhood of the
i.i.d. line in any natural topology on stationary processes, because **E is not continuous**.
[Polyanskiy & Wu](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf) §4.7 give only
lower semicontinuity, (4.28): "If `(X_n, Y_n) → (X, Y)` converge in distribution, then
`I(X;Y) ≤ liminf_{n→∞} I(X_n; Y_n)`", and supply two examples of strict inequality, including
one where the limit law is a point mass while `I(X_p; Y_p) → ∞`. **Derived here, not
retrieved:** the corresponding statement in process space follows by combining that with
[Crutchfield & Feldman's](https://arxiv.org/abs/cond-mat/0102181) Proposition 10, `E = log₂ p`
for a period-p process — take `μ_p` to be the shift-invariant measure on the orbit of a
length-`p` binary word chosen so that its length-ℓ subword frequencies approach `2^{−ℓ}`; then
`μ_p` agrees with the fair coin on longer and longer block statistics while `E(μ_p) = log₂ p`
grows without bound. (The block-frequency concentration this construction needs was not
verified against a source; it is flagged under *Load-bearing ifs*.) The upshot is directional
and does not depend on that detail: since the sublevel sets of a lower semicontinuous function
are closed but need not be neighbourhoods of anything, `{E < ε}` is a well-defined closed-ish
band containing the i.i.d. line but is not a *neighbourhood* of it, and processes arbitrarily
close to i.i.d. in finite-block statistics can have arbitrarily large E. **Refuted.**

The practical reading for the exclusion case: `E < ε` is a legitimate criterion and the right
replacement for `E = 0`, but it must be justified as a criterion in its own right, not as
"i.i.d. plus a small perturbation" — because it is not the set of small perturbations of i.i.d.
processes, and no threshold on E ever will be.

## What this does not establish

### Sources not reached

Cover & Thomas, *Elements of Information Theory* — named in the ticket as a candidate — was not
reached; no copy the repository can legitimately open was available, and the mutual-information
and chain-rule facts the ticket wanted from it were taken instead from Polyanskiy & Wu's
prepublication book, which states them for general alphabets rather than only discrete ones and
is therefore strictly stronger for this purpose. No ergodic-theory text on K-processes and the
tail σ-algebra was reached either; the tail-versus-cut distinction in §2 and §4 rests on
Polyanskiy & Wu (4.32) and its worked Kolmogorov-0-1-law example rather than on a treatment of
K-processes as such, so the claim "K-processes are not counterexamples" is argued here from the
general theorem of §3 and not from any statement about K-processes. Flaminio's construction is
known only through Bradley & Pruss's description of it and was not opened. Dębowski's review was
opened in full specifically to look for a citable `E = 0` characterisation and contains none;
it is listed in the appendix as a searched-and-negative source.

### Open gaps

No primary source stating `E = 0 ⟺ i.i.d.` as a theorem was found, and the search was not
exhaustive — six sources, three of them by the same group. Löhr's work on the statistical
complexity functional and on excess entropy was surfaced by search but not reached, and is the
most likely place for a careful measure-theoretic statement to exist. Separately: whether `E`
or a threshold `E < ε` is *estimable* from finite data at all — as opposed to well defined — was
not investigated, and it bears directly on whether the reformulated exclusion in §6 is
operational. Finally, §6's characterisation of the E = 0 set for non-binary alphabets was
derived, not retrieved, and the claim that the complexity–entropy diagram collapses it to a
curve was not checked against a source that plots one.

### Load-bearing ifs

If Polyanskiy & Wu's Theorem 3.2(c) — `I = 0` iff independence — required more than standard
Borel value spaces, the proof in §3 would need a separate argument for general spaces; every
step of §3 rests on it or on Thm 3.2(d). If Crutchfield & Feldman's Proposition 8 were not the
definition Mosaic intends by E — for instance if Mosaic means the summed form
`Σ [h_μ(L) − h_μ]` for a process where the two disagree — the monotonicity argument of §2 would
have to be redone, though Proposition 7 and Proposition 8 are stated as equivalent in the source.
If stationarity were weakened to any condition that does not transport the cut at 0 to every
integer, Step 2 collapses and the whole result fails; the non-stationary counterexample in §3
shows this is not a hypothetical. And the concrete period-p construction in §6 assumes a
block-frequency concentration fact that was not verified against a source — if it fails, the
non-continuity of E in process space would need a different witness, though the lower
semicontinuity result it is built on is cited and stands on its own.

## Verification Debt

One item, filed and open.

- **[#120](https://github.com/NGL321/mosaic/issues/120)** — **no primary source states
  `E = 0 ⇔ i.i.d.` as a theorem.** Six were searched, three by the same group. The mathematics is
  settled here and the counterexample search came back empty, but the forward direction remains
  Mosaic's own derivation rather than a retrieval, and §3 flags it as derived at the claim site. Löhr's
  work on the statistical complexity functional is the most likely home for a careful measure-theoretic
  statement; it was surfaced by search and **not reached**.

Two further gaps found here are **already on the tracker** and are not re-filed. Whether `E`, or a
threshold `E < ε`, is estimable from finite data at all — which decides whether §6's reformulated
exclusion is operational rather than merely well defined — is
[#99](https://github.com/NGL321/mosaic/issues/99) and
[#107](https://github.com/NGL321/mosaic/issues/107). The period-p witness in §6 assumes a
block-frequency concentration fact not verified against a source; it is carried in *Load-bearing ifs*
rather than as debt, because the lower-semicontinuity result the finding actually rests on is cited and
stands without it.

## Proposals

None.

## Appendix: primary sources, all retrieved 2026-08-02

1. James P. Crutchfield and David P. Feldman, *Regularities Unseen, Randomness Observed: Levels of Entropy Convergence*, arXiv:cond-mat/0102181 (Santa Fe Institute Working Paper 01-02-012), 35 pp. — read in full from the PDF. Definition of i.i.d. (Eq. 3); Proposition 7 (Eq. 51); Proposition 8 (Eq. 53); Proposition 10 (Eq. 56); Proposition 11 (Eq. 57); §VI A on the fair and biased coin; §VIII A process taxonomy. https://arxiv.org/abs/cond-mat/0102181
2. David P. Feldman, Carl S. McTague and James P. Crutchfield, *The Organization of Intrinsic Computation: Complexity-Entropy Diagrams and the Diversity of Natural Information Processing*, Chaos 18, 043106 (2008), arXiv:0806.4789, 18 pp. — read in full from the PDF. §III E on topological ǫ-machines, the fair-branching and binary and finite-state restrictions, and the "minimum complexity, E = 0" sentence. https://arxiv.org/abs/0806.4789
3. Yury Polyanskiy and Yihong Wu, *Information Theory: From Coding to Learning*, Cambridge University Press; prepublication PDF dated 16 August 2024, 730 pp. — §1.1 (Theorem 1.4), §3.1 (Definition 3.1, Theorem 3.2, Lemma 3.3), §3.4 (Theorem 3.7) and §4.7 (equations 4.28–4.32) read in full. https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf
4. Richard C. Bradley and Alexander R. Pruss, *A strictly stationary, N-tuplewise independent counterexample to the central limit theorem*, arXiv:0810.1707, 25 pp. — read in full. Abstract, §1 definitions of strict stationarity and N-tuplewise independence, Theorem 1.1, and the survey of prior constructions including Flaminio's. https://arxiv.org/abs/0810.1707
5. David P. Feldman and James P. Crutchfield, *Measures of Statistical Complexity: Why?*, Physics Letters A 238 (1998) 244–252; author PDF dated 11 November 1997, 7 pp. — read in full. §I on the "boundary conditions" of vanishing, the excess entropy as mutual information between two semi-infinite halves, and the 1D Ising complexity–entropy figure. https://csc.ucdavis.edu/~cmg/papers/mscw.pdf
6. Łukasz Dębowski, *Excess entropy in natural language: present state and perspectives*, arXiv:1105.1306, 12 pp. — read in full, specifically to look for a citable statement that E = 0 characterises i.i.d. processes. It contains no such statement; its treatment of E concerns growth rates, Hilberg's conjecture and strongly nonergodic processes. Listed as a searched-and-negative source. https://arxiv.org/abs/1105.1306
