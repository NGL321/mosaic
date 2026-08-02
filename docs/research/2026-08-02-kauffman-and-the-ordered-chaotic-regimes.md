---
ticket: 100
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 3
debt: [121, 122]
supersedes: null
---

# Kauffman (1969) has no chaotic regime; the ordered/chaotic dichotomy and its closed-form boundary are Derrida & Pomeau (1986)

**Provenance.** Machine-produced, unverified. Three primary sources were read in full from page scans of the original journal typesetting: Kauffman (1969), all 31 pages of *J. Theor. Biol.* **22**:437–467; Derrida & Pomeau (1986), all 5 pages of *Europhys. Lett.* **1**(2):45–49, with every displayed equation read off the rendered page rather than from OCR, because the OCR dropped them; and Derrida & Weisbuch (1986), *J. Physique* **47**:1297–1303, whose prose was read in full but whose displayed equations are images that did not extract — nothing here rests on a Derrida & Weisbuch equation. **Kauffman's *The Origins of Order* (1993) was not reached**, so the ticket's part (c) is undischarged and every row about Kauffman's *later* formulation is **Unresolved**. The critical condition `K · 2p(1−p) = 1` was **derived here** in one line from Derrida & Pomeau's equation (15); it is not written in their paper, and §3 shows the derivation so a reader can attack it. The routes tried and refused are itemised, by URL and status code, under *Sources not reached*. None of these readings has been checked by Noah unaided.

## 0. Verdict

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | Does Kauffman (1969) contain an ordered/chaotic *regime* distinction? | **Refuted** | §1 |
| 2 | Does Kauffman (1969) contain a critical connectivity, a phase transition, or the word "chaotic"? | **Refuted** | §1 |
| 3 | What *does* Kauffman (1969) establish — spontaneous order at low connectivity, stated as a biological plausibility argument? | **Established** | §1 |
| 4 | Is Derrida & Pomeau's annealed approximation what the ticket takes it to be — a mean-field map on Hamming distance with a transition at K=2? | **Established** | §2 |
| 5 | Is the closed form `K · 2p(1−p) = 1` stated in Derrida & Pomeau (1986)? | **Refuted** | §3 |
| 6 | Does it nevertheless follow from their equation (15), in one line? | **Supported** | §3 |
| 7 | Is it a computable membership test on a *given* discrete-state system, requiring no limit estimated from data? | **Refuted** | §4 |
| 8 | Is it a closed-form boundary on a *generator* of systems — an ensemble of random Boolean networks at fixed K and p? | **Supported** | §4 |
| 9 | Does the condition constrain both of the Bound's axes, Informational Capacity and Order? | **Loose** | §4 |
| 10 | Kauffman's later ordered/critical/chaotic trichotomy, as he himself stated it in *The Origins of Order* (1993) | **Unresolved** | §5 |
| 11 | Does the Bound's `_After_` line survive as written? | **Refuted** | §5, Proposals |

> **The `_After_` line credits Kauffman with a distinction he did not draw.** The 1969 paper contains no chaotic regime, no critical connectivity and no phase transition — it reports that low-connectivity random nets are surprisingly *orderly* and says explicitly that the failure of that order as K grows "will require careful delineation". The dichotomy the Bound actually leans on is Derrida & Pomeau (1986), whose annealed approximation yields, in one line, `K · 2p(1−p) = 1` — a genuine closed form, but a condition on an *ensemble's parameters*, not a test any particular system can be fed to.

## 1. What Kauffman (1969) actually claims

Read in full from a page scan of the original *J. Theor. Biol.* typesetting ([Kauffman 1969](https://web.archive.org/web/20110331190838/http://gbic.biol.rug.nl/~rbreitling/dagstuhlpublications/002_Kauffman1969.pdf), pp. 437–467).

**The mechanical finding first, because it settles the ticket.** Across the whole 31-page text the word *chaotic* occurs **zero** times; *critical* zero; *phase transition* zero; *regime* zero; *edge* zero. The word *chaos* occurs **once**, and not about networks at all — it is an analogy to statistical mechanics in the opening paragraph: "In the thermodynamics of gases, the mathematical laws of statistics bridge the gap between a chaos of colliding molecules and the simple order of the gas laws." The word *ordered* occurs twice, both times in the framing question of whether evolution had to select "non-random and ordered" nets, or whether order is generic.

**The model.** N binary "genes"; each receives exactly K inputs chosen at random from N; each is assigned, at random, one of the 2^(2^K) Boolean functions of its K inputs; both the wiring and the functions are then **fixed** — quenched — and the net is deterministic and synchronously updated. This is the object Derrida & Pomeau would later call Kauffman's model, and it is unchanged in their hands.

**What he studied.** Four connectivities, and only four: K = N (totally connected), K = 1, K = 2, and K = 3. For K = 2 he simulated N = 15, 50, 64, 100, 191, 400, 1024, 4096 and 8191.

**What he found.** For K = 2: median state-cycle length grows with an asymptotic log–log slope of about 0.3 with all 16 functions allowed and about 0.6 with tautology and contradiction disallowed — "just slightly greater than the square root N"; the median number of distinct cycles per net scales with a log–log slope of about 0.5, "slightly less than square root N"; activity decays sharply so that "most genes are constant throughout the cycle"; and under a single-bit perturbation the net returns to the cycle it was on "with probabilities between 0.85 and 0.95", so that "behavior in randomly connected binary nets is highly stable to infrequent noise". K = 3 nets gave "cycles slightly longer, the number of cycles about the same".

**What the contrast is, and what it is not.** Kauffman does contrast this with high connectivity: for K = N the state-transition map is a random map on 2^N states, so the expected cycle length is 2^(N/2), which for N = 200 he computes at ~10^30 states and calls "biologically impossible". But the same verdict falls on K = 1 — "state cycles generally exceed several millions of states in length … capable of realization by no earthly organism". **The 1969 contrast is therefore biologically-realisable versus biologically-impossible, not ordered versus chaotic**, and it is not monotone in K: both ends of his range are excluded, for different reasons. There is no order parameter, no transition, and no claim about *where* between K = 3 and K = N the behaviour changes. He says so in as many words, closing §5.7: "The rate of their failure as K approaches N will require careful delineation."

That sentence is the finding. In 1969 the ordered/chaotic boundary is not merely unstated — it is explicitly flagged as future work.

## 2. The annealed approximation, read and checked

Read in full from a scan of *Europhys. Lett.* **1**(2):45–49 ([Derrida & Pomeau 1986](https://web.archive.org/web/20221221185507/http://www.lps.ens.fr/~derrida/PAPIERS/1986/pomeau-86.pdf)); equations (2)–(15) were read off the rendered pages, since the text layer lost them.

**The approximation.** Kauffman's model is hard because the functions f_i and the input sets (i_1,…,i_K) are quenched, which correlates a configuration at time t with the rule that produced it. Derrida & Pomeau **discard exactly that correlation**: they study the model in which the functions and the wiring are re-randomised at every time step. In their words, "this is a kind of annealed approximation."

**The observable.** Not a cycle length, and not an entropy — the **Hamming distance** between two configurations. Take two configurations at distance n; equation (4) gives the exact one-step distribution P₁(m, n) for the *quenched* model when the two configurations are randomly chosen at t = 0. Iterating it as a product (equation (6)) is the approximation; the quenched model's true P_t is not that product, which they state as an inequality at equation (5).

**The map.** With x = n/N and y = m/N and N → ∞, the distribution concentrates, and the whole problem collapses to a one-dimensional map — equation (9):

```
y_{t+1} = [1 − (1 − y_t)^K] / 2
```

For K ≤ 2 the only fixed point is y = 0 and it is attractive, so the normalised distance vanishes (equation (10)). For K > 2, y = 0 is unstable and a new attractive fixed point y\* appears (equation (11)). "So we see that this simple annealed approximation gives a critical value K_c = 2."

**It is checked against the quenched model, twice.** Their Table I compares y\* against measured distances between the 24th and 25th iterates at N = 108: K = 2 gives y\* = 0 against 0.113 ± 0.097; K = 3 gives 0.38197 against 0.37 ± 0.078; K = 5 gives 0.48121 against 0.485 ± 0.047. (0.38197 is (3−√5)/2, and substituting it into the K = 3 map reproduces it to five places — the fixed points are exact, not fitted.) The check is then repeated and strengthened by [Derrida & Weisbuch (1986)](https://web.archive.org/web/20191029120133/http://www.lps.ens.fr/~derrida/PAPIERS/1986/weisbuch-86.pdf), who simulate both models at N = 32, 256, 2048 and 16384 for K = 2 and K = 3 and report that "for N large enough, one cannot distinguish the time evolution of the quenched and of the annealed models", with a sketch of why: the correlations the annealed model throws away arise only when two signal paths re-converge, whose probability at fixed time-depth vanishes as N → ∞. They also note the convergence is *slower* at K = 2 than at K = 3 and that finite-size effects there are stronger — which is what a marginal case should look like.

**Two limitations the authors state themselves.** The annealed model has no limit cycles at all, "because the rule is changed at each time step", so it makes **no prediction about cycle lengths** — precisely the quantity Kauffman's 1969 biology rested on. And they propose the approximation could be improved by computing P₂ exactly; it is an approximation they expected to be superseded, not a theorem.

## 3. The critical condition, derived

The condition the ticket names — `K · 2p(1−p) = 1` — **does not appear in Derrida & Pomeau (1986)**. What appears is the biased generalisation at equation (15). Give each entry of each truth table an independent bias, so that a function taking the value 1 on α of its 2^K rows has probability proportional to p^α (1−p)^(2^K − α) — that is, each output bit is 1 with probability p. Then equation (9) becomes:

```
y_{t+1} = [1 − (1 − y_t)^K] · 2p(1−p)
```

The condition follows in one line, and this document is where that line is done, not [the paper](https://web.archive.org/web/20221221185507/http://www.lps.ens.fr/~derrida/PAPIERS/1986/pomeau-86.pdf). y = 0 is a fixed point of (15) for every K and p. Differentiate the right-hand side and evaluate at y = 0:

```
d/dy [1 − (1 − y)^K] · 2p(1−p)  =  K(1 − y)^(K−1) · 2p(1−p)   →   K · 2p(1−p)   at y = 0
```

So the zero-distance fixed point is linearly stable iff **K · 2p(1−p) < 1** — two nearby configurations converge, perturbations die, the network is *ordered*; and unstable iff **K · 2p(1−p) > 1** — perturbations spread to a finite fraction y\* of the network, which is what the later literature calls the *chaotic* phase. The boundary is `K · 2p(1−p) = 1`.

**The sanity check is the paper's own headline.** Unbiased functions are p = 1/2, where 2p(1−p) = 1/2, so the condition reads K/2 = 1, i.e. K = 2 — exactly the K_c = 2 that Derrida & Pomeau state. The derivation reproduces their result and generalises it along p.

**A caveat the closed form hides.** At K = 2, p = 1/2 the slope is exactly 1: the case is *marginal*, not strictly ordered. Derrida & Pomeau nonetheless group it with the ordered side ("For K ≤ 2 … it is attractive"), which is right for the map — convergence at slope 1 is algebraic rather than exponential — and is consistent with Derrida & Weisbuch finding K = 2 the slow, finite-size-sensitive case. Anything that uses this boundary as a membership test inherits a boundary case that behaves differently from both sides of it.

Their equation (14) gives the other generalisation: for a mixture in which a fraction ρ_K of nodes has in-degree K, the map becomes y_{t+1} = Σ_K ρ_K [1 − (1 − y_t)^K] / 2, so the unbiased condition becomes ⟨K⟩ = 2 with ⟨K⟩ the *mean* in-degree. The two generalisations are given separately and are not combined in the paper; the combined form ⟨K⟩ · 2p(1−p) = 1 is the obvious composition and is not established here.

## 4. What this licenses for Mosaic, and what it does not

The ticket's hope was that this is "a candidate for a computable membership test on discrete-state systems that does not require estimating a limit from data". Stating precisely what the condition is a condition *on* is what decides that, and the answer is mixed.

**It is a condition on four things at once.** (i) A *random Boolean network* — N binary nodes, synchronous deterministic update, Boolean functions of exactly K inputs; (ii) the *ensemble parameters* K (in-degree) and p (output bias of the truth tables), not any realised network; (iii) the *annealed* approximation, in which wiring and functions are re-randomised each step — an approximation whose agreement with the quenched model is empirical and asymptotic, per §2, not proved; (iv) the limit **N → ∞**, without which the distance does not concentrate and the map does not exist.

**So it is not a membership test on a system.** Given one particular Boolean network — a specific wiring diagram and a specific set of truth tables — `K · 2p(1−p) = 1` has nothing to consume. K and p are properties of the *generator* that drew the network, and two networks drawn from the same (K, p) can behave differently at finite N; [Derrida & Weisbuch's](https://web.archive.org/web/20191029120133/http://www.lps.ens.fr/~derrida/PAPIERS/1986/weisbuch-86.pdf) finite-size saturation data is the direct evidence of that. Row 7 is **Refuted** on this ground and it is the load-bearing negative result of this document: the prior survey's estimation problem is not sidestepped by this condition, because this condition answers a different question.

**What it does license, and it is not nothing.** If Mosaic ever specifies a *family* of discrete-state systems by a generator rather than exhibiting one system — "random Boolean networks with in-degree K and bias p" — then the Bound's exclusion of the over-ordered and the under-ordered becomes decidable on that family in closed form, exactly, with no data and no limit estimated from a trajectory. That is a real and rare thing to have, and it is why row 8 is **Supported**. It also gives the region a *shape*: the boundary is a hyperbola in (K, p), so criticality is achievable at any K ≥ 2 by tuning the bias, and at no K < 2 for any p — since 2p(1−p) ≤ 1/2, the product K · 2p(1−p) ≤ K/2 < 1 whenever K < 2. Sparse connectivity is ordered whatever the functions do.

**It speaks to one axis, not two.** The quantity the map governs is the asymptotic normalised Hamming distance between perturbed copies — sensitivity to perturbation, a discrete analogue of a Lyapunov exponent. That is a measure on the **Order** axis of the Bound, and it is silent about **Informational Capacity**: Derrida & Pomeau compute no entropy, no mutual information and no channel capacity anywhere in the paper, and they say plainly that their model can say nothing about cycle lengths, which is the closest thing in Kauffman's 1969 work to a capacity-like quantity. A verdict that the condition operationalises "the Edge of Chaos" as the Bound states it would be overclaiming by one whole axis. Row 9 is **Loose** for that reason.

## 5. The `_After_` line, and Kauffman's later formulation

The Bound was settled in [#6](https://github.com/NGL321/mosaic/issues/6); the line at issue is in that ticket's answer comment and has **not yet been written into `CONTEXT.md`** — the file on `main` contains no occurrence of "Edge of Chaos", "Kauffman" or "chaos" at all. So this correction is cheap to apply: it lands wherever the Bound lands, and no committed line has to be edited.

The line, as it stands in the #6 answer:

```
*After* Langton (1990) on computation at the edge of chaos, and Kauffman on the
ordered/chaotic regimes; *departs* by carrying Mitchell, Hraber & Crutchfield's
(1993) pushback in-line rather than inheriting the frame unexamined.
```

Against §1, the clause "Kauffman on the ordered/chaotic regimes" is unattributable to [Kauffman (1969)](https://web.archive.org/web/20110331190838/http://gbic.biol.rug.nl/~rbreitling/dagstuhlpublications/002_Kauffman1969.pdf). The line does not carry a year, which is what has let it survive — but the paper the repository has been pointing at throughout, including in [#100](https://github.com/NGL321/mosaic/issues/100) itself, is the 1969 one, and the 1969 one does not contain the distinction.

**Kauffman plainly did adopt the trichotomy later**, and the honest position is that this document could not read him doing it. *The Origins of Order* (1993) was refused (see *Sources not reached*), and no first-party Kauffman text stating an ordered/critical/chaotic trichotomy was reachable in full by any route tried. Row 10 is therefore **Unresolved**, and the replacement text below deliberately does **not** credit Kauffman with the dichotomy at any date — it credits him with what §1 confirms he did, and credits the dichotomy to the source that was read in full. Crediting a later Kauffman work this document has not opened would repeat the exact failure the ticket exists to correct.

## What this does not establish

### Sources not reached

**Kauffman, *The Origins of Order* (1993)** — the ticket's part (c) — was not reached, and this is the one gap that matters. Routes tried, all on 2026-08-02: the Internet Archive item [`originsoforderse0000kauf`](https://archive.org/details/originsoforderse0000kauf) is `access-restricted-item: true` with lending status `None`, its `_djvu.txt` and PDF derivatives are not served, and the search-inside endpoint (`ia601905.us.archive.org/fulltext/inside.php`) returned **HTTP 403 "Item not available"**, so not even a snippet was obtained; web search surfaced no first-party or repository scan; a copy exists on the aggregator `dokumen.pub` and was **deliberately not used**, because a re-typeset upload of unverifiable fidelity is not "the scan of the original edition" that §3 of the contract requires, and quoting it would launder provenance. Two adjacent Kauffman primaries were also sought and not reached: **Kauffman (1990)**, *Requirements for evolvability in complex systems: orderly dynamics and frozen components*, *Physica D* **42**:135–152 — the same volume as Langton (1990), which [#87](https://github.com/NGL321/mosaic/issues/87) read from a single-paper scan that does not extend to the volume — and **Kauffman (1984)**, *Physica D* **10**:145, both behind ScienceDirect. Separately: **ScienceDirect** for Kauffman (1969) was not re-attempted, since [#87](https://github.com/NGL321/mosaic/issues/87) recorded 403 and the wayback route succeeded instead; **IOPscience** for Derrida & Pomeau was likewise not needed; **HAL** (`hal.science/hal-03285912/document`) returned an Anubis bot-challenge page rather than the PDF; and **`lps.ens.fr` directly** — Derrida's own author page, the origin of two of the three sources here — refused HTTPS (connection refused on 443) and timed out on HTTP port 80, so both Derrida papers came from Internet Archive captures of that page rather than from the live host.

### Open gaps

Three, in descending order of how much they would move things. **First: is there a per-system analogue?** §4 refutes the condition as a test on a given network, but the natural repair — computing a specific network's *average sensitivity*, the mean number of outputs a single-bit flip changes, and comparing it to 1 — is a real object in the later literature (Shmulevich & Kauffman, and the activity/influence formalism) that this document did not read and therefore cannot assert. If it works, Mosaic gets what [#100](https://github.com/NGL321/mosaic/issues/100) hoped for; if it does not, the closed form stays confined to ensembles. **Second: the combined generalisation.** Equations (14) and (15) generalise the map along in-degree distribution and along bias separately; ⟨K⟩ · 2p(1−p) = 1 is the obvious composition, is what the secondary literature quotes, and is not derived in the paper or here. **Third: the Informational Capacity axis is untouched.** Nothing read here bounds, measures or even defines a capacity-like quantity on random Boolean networks; the Bound's second axis has no closed form and this document did not find one.

### Load-bearing ifs

**If the derivation in §3 is wrong, rows 5–9 fall.** It is four lines of calculus on an equation transcribed from a page image, and the transcription is the weaker half: equation (15) was read visually off page 49 of the scan, and if `2p(1−p)` is misread the whole condition changes shape. The check that it is not misread is that setting p = 1/2 reproduces the paper's own stated K_c = 2, which is an independent constraint the transcription would have to satisfy by accident to be wrong. **If the annealed approximation does not track the quenched model, §4's "closed form" is a closed form for the wrong object.** The evidence that it does is empirical and asymptotic — three rows of Table I and Derrida & Weisbuch's simulations — and is not a proof; both papers present it as an approximation. **If Kauffman stated the ordered/chaotic trichotomy somewhere between 1969 and 1993 in a text this document did not reach**, the `_After_` line's *year-free* wording could be defended as-is, and the replacement below would be over-correcting by removing a true credit. That is why the proposed text removes the claim rather than re-dating it: it is the change that is safe under either resolution of row 10.

## Verification Debt

Two items, both filed, both open.

- **[#121](https://github.com/NGL321/mosaic/issues/121)** — Kauffman's *later* trichotomy is still
  unread. §1 establishes that the 1969 paper contains no ordered/chaotic distinction at all, so
  wherever Kauffman states one it is later work. *The Origins of Order* (1993) is access-restricted at
  the Internet Archive down to the search-inside snippet, and the *Physica D* papers were not reached.
  A re-typeset upload was located and **deliberately not used**. This is why the correction below does
  not re-credit the dichotomy to 1993: citing an unread text would repeat the failure this ticket
  exists to correct.
- **[#122](https://github.com/NGL321/mosaic/issues/122)** — no **per-system** criticality test.
  `K · 2p(1−p) = 1` is closed-form on the *generator* — an ensemble at (K, p), annealed, N → ∞ — not
  a test a given network can be fed to, and it constrains only the Order axis. The natural repair is a
  specific network's **average sensitivity** against 1 (Shmulevich & Kauffman), which was not reached.
  Also unestablished: the combined `⟨K⟩ · 2p(1−p) = 1`, which the secondary literature quotes but
  Derrida & Pomeau never compose.

## Proposals

**1. Replace the Bound's `_After_` line.** Exact replacement text, in the form the line currently takes in the [#6](https://github.com/NGL321/mosaic/issues/6) answer comment:

```
*After* Langton (1990) on computation at the edge of chaos; Kauffman (1969) for the
finding that randomly constructed low-connectivity Boolean nets are spontaneously
ordered — short state cycles, few attractors, high stability under single-bit noise —
and Derrida & Pomeau (1986) for the ordered/chaotic dichotomy itself, whose annealed
approximation puts the transition at K · 2p(1−p) = 1 for random Boolean networks in
the N → ∞ limit; *departs* by carrying Mitchell, Hraber & Crutchfield's (1993)
pushback in-line rather than inheriting the frame unexamined.
```

If the line is instead written into `CONTEXT.md` in that file's `_After_:` form, the same text with the leading `*After*` replaced by `_After_:` and the `*departs*` clause moved to its own `_Departs_:` line, per the surrounding entries.

Two things are deliberately preserved: the Langton and Mitchell/Hraber/Crutchfield clauses are untouched, including the name order, because this document did not read either and has no standing to amend them.

**2. Do not attach the closed form to the Bound's operationalisation without the qualifier.** If `K · 2p(1−p) = 1` is used anywhere as a membership criterion, it should be written as a criterion on a *generator* — "random Boolean networks with in-degree K and truth-table bias p, in the annealed approximation, N → ∞" — and never on a system. §4 is the argument; the short form for a badge or a note is: *closed-form on the ensemble, not computable on an instance.*

**3. Badge text, for Noah to apply if and where the correction lands:** `⟦T3 · #100⟧`.

## Appendix: primary sources

All three were read in full from scans of the original journal typesetting; all links retrieved 2026-08-02.

1. S. A. Kauffman (1969), *Metabolic stability and epigenesis in randomly constructed genetic nets*, **J. Theor. Biol. 22**:437–467. Read in full, 31 pages, from an Internet Archive capture of a page scan: [web.archive.org/…/002_Kauffman1969.pdf](https://web.archive.org/web/20110331190838/http://gbic.biol.rug.nl/~rbreitling/dagstuhlpublications/002_Kauffman1969.pdf) (the live host returns 404). Publisher record: [doi.org/10.1016/0022-5193(69)90015-0](https://doi.org/10.1016/0022-5193%2869%2990015-0). Model definition §2; K = N, K = 1, K = 2 at §§3–5; cycle-length scaling §5.1; number of cycles §5.4; noise perturbation §5.6; the "careful delineation" concession closing §5.7; conclusion §9.
2. B. Derrida & Y. Pomeau (1986), *Random Networks of Automata: A Simple Annealed Approximation*, **Europhys. Lett. 1**(2):45–49. Read in full, 5 pages, from an Internet Archive capture of the authors' own copy on Derrida's ENS page: [web.archive.org/…/pomeau-86.pdf](https://web.archive.org/web/20221221185507/http://www.lps.ens.fr/~derrida/PAPIERS/1986/pomeau-86.pdf) (live host unreachable). Publisher record: [doi.org/10.1209/0295-5075/1/2/001](https://doi.org/10.1209/0295-5075/1/2/001). Exact one-step distribution eq. (4); annealed product eq. (6) and the inequality eq. (5); the map eq. (9); K_c = 2 at eqs. (10)–(11); Table I; in-degree mixture eq. (14); the biased map eq. (15).
3. B. Derrida & G. Weisbuch (1986), *Evolution of overlaps between configurations in random Boolean networks*, **J. Physique 47**:1297–1303. Prose read in full, 7 pages, from an Internet Archive capture of the same author page: [web.archive.org/…/weisbuch-86.pdf](https://web.archive.org/web/20191029120133/http://www.lps.ens.fr/~derrida/PAPIERS/1986/weisbuch-86.pdf). Publisher record: [doi.org/10.1051/jphys:019860047080129700](https://doi.org/10.1051/jphys:019860047080129700). Cited here only for prose claims — the quenched/annealed agreement at large N (§5 and §6), the path-reconvergence argument for it (§6), and the slower convergence and stronger finite-size effects at K = 2 (§5). Its displayed equations are page images that did not extract, and nothing here rests on one.
