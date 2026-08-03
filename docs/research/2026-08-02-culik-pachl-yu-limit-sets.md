---
ticket: 114
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 4
debt: []
supersedes: null
---

# The bounded-time equivalence holds exactly as Culík & Yu state it — but the step that carries it is theorem 3 of CS-87-47, not the corollary 2 they cite

CS-87-47 **was retrieved and read**: the University of Waterloo Computer Science Department's own scan of Culik, Pachl & Yu, *On the Limit Sets of Cellular Automata*, Research Report CS-87-47, dated August 10, 1987, served from the departmental technical-report archive at [`cs.uwaterloo.ca/research/tr/1987/CS-87-47.pdf`](https://cs.uwaterloo.ca/research/tr/1987/CS-87-47.pdf) (HTTP 200, `content-type: application/pdf`, 1,878,614 bytes, 33 pages, `last-modified: 2005-11-22`). The file carries **no text layer** — `pdftotext` extracts 33 bytes from the whole document — so every page cited below was rendered to a 200-dpi image and read as an image. What was read closely is the front matter and **report pages 1–11** (PDF pages 2–12): the abstract, §1 Introduction, §2 *Cellular automata, basic definitions*, and the whole of §3 *The product topology on configurations*, which is where corollary 2 lives and where the step Culík & Yu defer to is actually proved. Sections 4–7 and the appendix — limit sets of linear CA, the tiling reduction, finite configurations, ωω-regular sets — were **not** read; they are about different results and nothing in §3 forwards to them. The Culík & Yu (1988) side was re-read at the exact citation site, from the publisher's open scan, to fix the wording of the deferral rather than work from [#45's paraphrase](https://github.com/NGL321/mosaic/issues/45). No survey, abstract, citation database or re-typeset upload was used for any claim about what either text says. The published journal version (*SIAM J. Comput.* **18**(4):831–842, 1989) was not consulted and was not needed: CS-87-47 is the object the 1988 paper cites, and it was reached.

## 0. Verdict

> **The equivalence is true and is proved in the cited report, so the debt discharges clean and #45's argument does not narrow — but the pointer is wrong: corollary 2 of CS-87-47 is a Baire-category dichotomy about whether the limit set is reached in finite time, and on its own it does not yield bounded-time homogeneity. The load is carried by theorem 3 together with corollary 1, and the underlying theorem 2 proves something strictly more general than Culík & Yu needed — for *any* closed translation-invariant target set, "every configuration eventually enters it" already implies "within a uniform bound".**

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | Was CS-87-47 itself retrieved, as a primary source rather than a re-typeset or a description? | **Established** — the Waterloo CS technical-report archive serves the 1987 scan at HTTP 200 | §1 |
| 2 | Does the bounded-time equivalence hold as Culík & Yu (1988) theorem 1 states it? | **Established** — statements 1 and 2 are equivalent, and the report proves it | §3 |
| 3 | Is "corollary 2 of [2]" the step that establishes it? | **Refuted** — corollary 2 gives only that some Ω⁽ⁱ⁾ equals Ω; the equivalence comes from theorem 3 plus corollary 1 | §2, §3 |
| 4 | Is the equivalence special to homogeneous or quiescent target configurations? | **Refuted** — theorem 2 gives the uniform bound for every closed translation-invariant subset | §3 |
| 5 | Is the "clearly equivalent" step between statements 2 and 3 as cheap as Culík & Yu make it sound? | **Supported** — it is cheap, but it is topological, not combinatorial: it is density plus closedness | §3 |
| 6 | Does #45's claim that bounded-time convergence is *strictly stronger* than Class One survive? | **Established** — and the report and the 1988 paper both sharpen it | §4 |
| 7 | Does the argument in `2026-08-02-culik-yu-ca-undecidability.md` narrow? | **Refuted** — no claim in it weakens; one citation in it should be repointed | §4 |

## 1. What was retrieved, and how

The report is served by the University of Waterloo Computer Science Department's own technical-report archive, one directory per year, at [`https://cs.uwaterloo.ca/research/tr/1987/CS-87-47.pdf`](https://cs.uwaterloo.ca/research/tr/1987/CS-87-47.pdf). A `HEAD` returns `HTTP/2 200`, `content-type: application/pdf`, `content-length: 1878614`, `last-modified: Tue, 22 Nov 2005 15:29:26 GMT`; `www.cs.uwaterloo.ca` redirects to the same object. The PDF's producer string is `DigiPath`, a document-scanning system, and its creation date is 2005 — this is a 2005 digitisation of the 1987 paper original, which is why there is no text layer and why nothing in it can be checked by string search.

Its cover page identifies it exactly as the 1988 paper's reference [2]: *On the Limit Sets of Cellular Automata*, Karel Culik II, Jan Pachl, Sheng Yu, Research Report CS-87-47, August 10, 1987, Computer Science Department, University of Waterloo. The title page repeats the date and the NSERC grants (A7403, A0952). Thirty-three pages. The abstract states the scope: "We prove a number of results on limit sets, considering both finite and infinite configurations… In our proofs we use results on finite recognizability of sets of biinfinite words and topological properties of product spaces."

The retrieval succeeded on the first route tried, so the failed-retrieval itemisation the ticket anticipated is short and is in *Sources not reached* below.

## 2. What corollary 2 actually says

Culík & Yu's deferral, read from the publisher's scan of [*Complex Systems* **2** (1988) 177–190](https://content.wolfram.com/uploads/sites/13/2018/02/02-2-2.pdf) at page 181, is one sentence:

> **Proof.** The equivalence of the first two statements can be easily proved by considering the stable state as the quiescent state and applying corollary 2 of [2]. Statements 2 and 3 are clearly equivalent. Statement 2 implies statement 4. Statement 4 implies statement 1.

Corollary 2 of CS-87-47 is on report page 8, in §3, and reads:

> **Corollary 2** *For each CA, exactly one of these two conditions is true:*
> *(i) There exists an integer i ≥ 0 such that Ω⁽ⁱ⁾ = Ω.*
> *(ii) There exists a dense G<sub>δ</sub> set D ⊆ S<sup>Zᵏ</sup> such that Ω ∩ ⋃<sub>i=0</sub><sup>∞</sup> G<sub>f</sub><sup>i</sup>(D) = ∅.*

Here Ω⁽⁰⁾ = S<sup>Zᵏ</sup>, Ω⁽ⁱ⁾ = G<sub>f</sub>(Ω⁽ⁱ⁻¹⁾), and Ω = ⋂<sub>i≥0</sub> Ω⁽ⁱ⁾ is the limit set (report p. 5–6). So corollary 2 is a **stability dichotomy**: either the limit set is attained after finitely many steps, or a topologically generic set of configurations never enters it at all. It is not a statement about homogeneity, about quiescence, or about a time bound on reaching anything. The report immediately illustrates both horns — condition (i) holds whenever G<sub>f</sub> is surjective, and their Example 2 (the k=2, r=1 rule that outputs 1 exactly on `111`) satisfies (ii) — which confirms the reading: corollary 2 is about *which* of the two regimes a CA is in, not about bounded-time convergence.

Both corollaries fall out of the section's main result, and it is worth having in view because the whole discharge turns on it:

> **Theorem 2** *Let C be a closed translation-invariant subset of S<sup>Zᵏ</sup>. Exactly one of these two conditions is true:*
> *(i) There exists an integer i ≥ 0 such that G<sub>f</sub><sup>i</sup>(S<sup>Zᵏ</sup>) ⊆ C.*
> *(ii) There exists a dense G<sub>δ</sub> set D ⊆ S<sup>Zᵏ</sup> such that C ∩ ⋃<sub>i=0</sub><sup>∞</sup> G<sub>f</sub><sup>i</sup>(D) = ∅.*

The proof (report pp. 7–8) sets F<sub>i</sub> = { c : G<sub>f</sub><sup>i</sup>(c) ∈ C }, notes each F<sub>i</sub> is closed and translation-invariant, and puts D = S<sup>Zᵏ</sup> − ⋃F<sub>i</sub>. If D is dense, (ii) holds. If not, ⋃F<sub>i</sub> contains a non-empty open set, so by Baire's theorem some F<sub>i</sub> contains a non-empty open subset; being translation-invariant it then contains a non-empty *open translation-invariant* subset, and — the step doing the real work — **every non-empty open translation-invariant subset of S<sup>Zᵏ</sup> is dense**, so the closed set F<sub>i</sub> is the whole space. Corollary 1 and corollary 2 are then read off by taking C = {Q̃} and C = Ω respectively, both being closed and translation-invariant.

## 3. The equivalence is true, and this is the chain that proves it

Take C&Y's stable state *s* as the quiescent state q̃, as their proof directs, so the homogeneous configuration of *s* is the quiescent configuration Q̃. Assume statement 1: **every** configuration evolves to Q̃.

**Step one — the limit set collapses.** [Report](https://cs.uwaterloo.ca/research/tr/1987/CS-87-47.pdf) p. 8, immediately before corollary 2:

> **Corollary 1** *If Ω ≠ {Q̃} then there exists a configuration whose orbit does not contain Q̃.*

Contrapositive: if every configuration's orbit contains Q̃ — which is statement 1, since Q̃ is a fixed point and the orbit stays there — then Ω = {Q̃}. That is C&Y's **statement 4**, obtained from statement 1 directly.

**Step two — collapse forces a uniform bound.** Report p. 9:

> **Theorem 3** *Ω = {Q̃} if and only if there exists an integer i ≥ 0 such that Ω⁽ⁱ⁾ = {Q̃}.*

The *only if* direction is the one wanted, and its proof (report p. 10) is a genuine compactness argument rather than a Baire one: fix a cell I₀, put C = { c : c(I₀) ≠ q̃ } — a *clopen* set, because S is finite and the product topology's subbasis is exactly the coordinate constraints — and observe ⋂<sub>i</sub>(Ω⁽ⁱ⁾ ∩ C) = {Q̃} ∩ C = ∅. A decreasing chain of compact sets with empty intersection has an empty member, so Ω⁽ⁱ⁾ ∩ C = ∅ for some *i*; translation-invariance of Ω⁽ⁱ⁾ upgrades that from the one cell I₀ to every cell, giving Ω⁽ⁱ⁾ = {Q̃}.

And Ω⁽ⁱ⁾ = G<sub>f</sub><sup>i</sup>(S<sup>Zᵏ</sup>) = {Q̃} *is* statement 2: every configuration whatsoever is quiescent after exactly *i* steps, a constant independent of the configuration. Statement 2 trivially implies statement 1. **The equivalence holds, in the report, on the two results flanking the one that was cited.**

Three things follow that the 1988 paper's one-sentence proof hides.

**The citation is off by one result and is not repairable by substitution.** Corollary 2 on its own gives only that Ω⁽ⁱ⁾ = Ω for some *i*. Under statement 1 its second horn is indeed impossible — a dense G<sub>δ</sub> set is non-empty, its members reach Q̃, and Q̃ ∈ Φ ⊆ Ω, so the orbit of D does meet Ω — so horn (i) does hold. But (i) is a statement about Ω, and turning "Ω⁽ⁱ⁾ = Ω" into "Ω⁽ⁱ⁾ = {Q̃}" still needs Ω = {Q̃}, which is corollary 1 and nothing weaker. So corollary 2 is at best one of two ingredients, and once corollary 1 is in hand theorem 3 is the shorter road. The honest citation is *theorem 3 and corollary 1 of [2]*, or, in one step, *theorem 2 of [2] with C the homogeneous configuration*.

**The result is much more general than the use made of it.** Theorem 2 is stated for an arbitrary closed translation-invariant C, so the real content is: *for any closed translation-invariant set of configurations, "every configuration eventually enters C" already implies "every configuration enters C within a uniform bound"*. Homogeneity is only one instance. This matters for C&Y statement 1 in its literal reading — "all configurations evolve to *a* homogeneous configuration", not to a fixed one — because the set of all constant configurations is finite, closed and translation-invariant, so theorem 2 applies to it directly and the equivalence survives without the "considering the stable state as the quiescent state" specialisation the 1988 proof performs.

**"Clearly equivalent" (statements 2 and 3) is clear but topological.** Statement 3 restricts the bound to *s*-finite configurations. It implies statement 2 because the *s*-finite configurations are dense in S<sup>Z</sup> and each F<sub>i</sub> = { c : G<sub>f</sub><sup>i</sup>(c) = Q̃ } is closed, so an F<sub>i</sub> containing all of them is the whole space — the same closed-plus-dense move as in theorem 2's last line. It is not a counting argument and it does not go through for a non-closed target, which is worth knowing before the phrase is reused.

## 4. What this does to #45's argument

Nothing weakens. [`docs/research/2026-08-02-culik-yu-ca-undecidability.md`](https://github.com/NGL321/mosaic/issues/45) leans on C&Y theorem 1 in exactly one place — §2's closing paragraph and §5's item (iii) — for the claim that the natural bounded-time proxy for Class One is *strictly stronger* than the class rather than an approximation of it. That claim needed the equivalence to be true, and it is true.

It is in fact better supported than #45 could show. Class One asks only that all *s*-finite configurations reach homogeneity, in unbounded time; theorem 1 shows that the moment you ask it of *all* configurations you get a constant bound for free. The gap between the two is therefore not a matter of degree, and the 1988 paper measures it: immediately after theorem 1 it observes that "for any computable function T(n), there exists a Class One cellular automaton such that some of its *s*-finite configurations need T(n) steps to evolve to the quiescent configuration", with an explicit four-state, radius-1 automaton (Example 3, p. 181) whose segments count down a binary number and so survive exponentially many steps in their length. So the proxy is not merely stronger — the quantity it would have to approximate is unbounded by any computable function, while the proxy itself is a constant. #45's "strictly stronger, not an approximation" is the right verdict and understates it.

One correction is due, and it is a citation, not a claim. #45's *Sources not reached* says the equivalence "is accepted here on the authors' citation rather than verified"; that is now discharged, and anything downstream repeating C&Y's "corollary 2 of [2]" should say theorem 3 and corollary 1 instead. Exact replacement text is in *Proposals*.

## What this does not establish

### Sources not reached

Two things were deliberately not read and one could not be reached. Report **sections 4 through 7 and the appendix** (report pp. 12–31) were not read: they cover limit sets of linear CA via ωω-regular sets, the tiling reduction giving undecidability of Ω = {Q̃} for k ≥ 2, limit sets of finite configurations, and biinfinite-word automata. Nothing in §3 forwards to them and the cited corollary is entirely contained in §3, but the consequence is that this document cannot say what the report proves outside §3, and in particular has not checked whether any later section restates or strengthens theorem 3. The **published journal version** — *SIAM J. Comput.* **18**(4):831–842 (1989) — was not obtained: [`https://epubs.siam.org/doi/10.1137/0218057`](https://epubs.siam.org/doi/10.1137/0218057) returns **HTTP 403** to an unauthenticated request, and no other route to it was attempted, because the technical report is the object the 1988 paper cites and it was in hand. That leaves one thing genuinely unknown: whether SIAM's renumbering makes the bounded-time result *its* corollary 2, which would explain the misdirected citation as a draft-numbering artifact rather than an error. Wolfram's own papers were not read here, as in #45; nothing in this document depends on them.

### Open gaps

Whether the 1988 citation is an error or a stale pointer to a differently numbered draft is open and is decidable only by reading the SIAM version's §3, which was not reached. The report's own open questions are untouched here: p. 7 records that "it is an open question whether the problem Ω = {Q̃} is decidable for k = 1", and p. 11 that the authors *conjecture* it is decidable for linear CA while proving it undecidable for k ≥ 2 — the status of that conjecture in the literature after 1987 was not checked, and it is the natural next question for anyone who wants to know whether a decision procedure for the strongest form of Class One exists in one dimension. Theorem 2's generality — a uniform bound for entry into any closed translation-invariant set — was not traced forward to see whether later work names it, though it looks like a result that would have been rediscovered. And the quantitative side is untouched: theorem 3 gives an *i* with no bound on it in terms of |S| or the neighbourhood, and whether one exists is not addressed by the report or by this document.

### Load-bearing ifs

The claim that corollary 2 alone does not suffice rests on there being no cheap route from "Ω⁽ⁱ⁾ = Ω for some i" plus "every configuration reaches Q̃" to "Ω = {Q̃}" that avoids corollary 1. I argued above that the obvious compactness route fails because "has not reached Q̃ by time n" is an *open*, not closed, condition — {Q̃} is closed but not open — which is precisely why the section needs Baire's theorem at all; but this is a negative claim about the existence of a proof, and it is the first thing an adversarial reader should attack. If a cheap route exists, sub-question 3 flips to **Loose** and C&Y's citation is merely terse rather than misdirected; nothing else in this document moves, because the equivalence itself is proved either way. Second, the whole reading is from **page images of a 2005 scan with no text layer**, so no claim here was verified by string search and none can be; the corollary and theorem statements above were transcribed by eye from renders at 200 dpi, and a misread subscript in the statement of theorem 3 or corollary 2 would matter. Third, the identification of C&Y's stable state *s* with the report's distinguished quiescent state q̃ is licensed by C&Y's own proof sentence ("considering the stable state as the quiescent state") and by the report's definition of q̃ as any state with f(q̃,…,q̃) = q̃, of which a CA may have several with at most one distinguished; if that identification failed, the whole deferral would fail with it, not just the pointer.

## Verification Debt

None. CS-87-47 was retrieved and the step it was cited for was followed to a proof; the two things this document did not read — the report's §§4–7 and the SIAM reprint — are named in *Sources not reached* as scope decisions rather than as unchecked load-bearing steps, and nothing in the argument above rests on either. Filing the SIAM version as debt would put a duplicate of a source already in hand into a ledger reserved for what nobody has checked.

## Proposals

**1. Replacement text for the second sentence of *Sources not reached* in [`docs/research/2026-08-02-culik-yu-ca-undecidability.md`](https://github.com/NGL321/mosaic/issues/45)** (replacing the sentence beginning "Theorem 1's proof defers the equivalence of its first two statements…"):

> Theorem 1's proof defers the equivalence of its first two statements to "corollary 2 of [2]" — Culik, Pachl & Yu, *On the Limit Sets of Cellular Automata*, Research Report CS-87-47, University of Waterloo (1987). That report has since been retrieved and read ([#114](https://github.com/NGL321/mosaic/issues/114)): the equivalence holds, but it is established by that report's theorem 3 together with its corollary 1, not by its corollary 2, which states a different result. See [`docs/research/2026-08-02-culik-pachl-yu-limit-sets.md`](https://github.com/NGL321/mosaic/issues/114).

**2. Replacement text for the *Verification Debt* item in the same document** (replacing the `#114` bullet):

> - **[#114](https://github.com/NGL321/mosaic/issues/114)** — **discharged.** Culik, Pachl & Yu, *On the Limit Sets of Cellular Automata*, Waterloo Research Report CS-87-47 (1987), was retrieved from the Waterloo CS technical-report archive and read. Theorem 1's bounded-time equivalence holds as stated; the step that proves it is the report's theorem 3 plus corollary 1, and the 1988 paper's citation to "corollary 2" points at a neighbouring result that does not by itself give the equivalence. No claim in this document narrows.

**3. Badge text**, should the sharper form of the proxy claim ever land on a `CONTEXT.md` line — no such line exists today, so this is drafted, not applied:

> If every configuration of a CA reaches homogeneity at all, it does so within a constant number of steps; Class One asks less, and the time it permits is unbounded by any computable function ⟦T3 · #114⟧

## Appendix: primary sources, all retrieved 2026-08-02

1. Karel Culik II, Jan Pachl & Sheng Yu, *On the Limit Sets of Cellular Automata*, Research Report **CS-87-47**, Department of Computer Science, University of Waterloo, August 10, 1987 — departmental technical-report archive: [PDF](https://cs.uwaterloo.ca/research/tr/1987/CS-87-47.pdf) (HTTP 200, `application/pdf`, 1,878,614 bytes, 33 pp., image-only scan, no text layer). Report pp. 1–11 read as 200-dpi page renders; §§4–7 and the appendix not read.
2. The archive directory the report was found in, establishing the route and that the year holds the full CS-87 series: [`cs.uwaterloo.ca/research/tr/1987/`](https://cs.uwaterloo.ca/research/tr/1987/) (HTTP 200); the department's technical-reports landing page redirects there from [`cs.uwaterloo.ca/research/tr/`](https://cs.uwaterloo.ca/research/tr/).
3. Karel Culik II & Sheng Yu, *Undecidability of CA Classification Schemes*, **Complex Systems** 2 (1988) 177–190 — publisher's open scan: [PDF](https://content.wolfram.com/uploads/sites/13/2018/02/02-2-2.pdf). Read at pp. 180–182 for the exact statement of theorem 1, its four statements, the deferral sentence, and example 3.
4. The debt as filed, including the two questions this document was required to answer: [NGL321/mosaic#114](https://github.com/NGL321/mosaic/issues/114); the document that filed it, `docs/research/2026-08-02-culik-yu-ca-undecidability.md`, read from the working tree on `research/debt-sweep-2026-08-02`, resolves [NGL321/mosaic#45](https://github.com/NGL321/mosaic/issues/45).
