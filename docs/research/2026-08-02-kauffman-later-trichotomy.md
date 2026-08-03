---
ticket: 121
map: 1
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 3
debt: [130]
supersedes: null
---

# Kauffman's trichotomy is ordered / complex / chaotic, it is stated in *The Origins of Order* (1993), and Kauffman himself credits Derrida & Pomeau for the analytics

**Provenance.** Machine-produced, unverified. **The primary source was reached.** Kauffman's *The Origins of Order* (Oxford University Press, 1993) was obtained as an unrestricted page-image scan of the original edition on the Internet Archive — an item distinct from the access-restricted one [#100](https://github.com/NGL321/mosaic/issues/100) was refused — and the edition was verified from the scanned copyright page itself (© 1993 Oxford University Press, ISBN 0-19-505811-9, LCCN 91-11148), not from catalogue metadata. Every passage quoted below was read off the rendered **page image** at the cited printed page, not from OCR: the OCR was used only to *locate* passages, and it is visibly lossy (it renders "systems" as "Sys- tems" and mangles the bibliography). Four pages were read as images in full — pp. 174, 183, 198 and 671 — plus p. 219; the surrounding OCR of Chapter 5 (pp. 173–236) was read as text for context. The `dokumen.pub` re-typeset copy was **not** used and no route to it was followed. The two *Physica D* papers were **not** reached and are now confirmed to have no open-access copy in existence; their routes and status codes are itemised under *Sources not reached*. Kauffman (1969) and Derrida & Pomeau (1986) are cited here from [#100](https://github.com/NGL321/mosaic/issues/100)'s document, where they were read in full; they were not re-read here. None of this has been checked by Noah unaided.

## 0. Verdict

| # | Sub-question | Verdict | Argued in |
|---|---|---|---|
| 1 | Was a first-party Kauffman text stating the trichotomy reached, in the original edition? | **Established** | §1 |
| 2 | Is the copy used the original OUP 1993 typesetting rather than a re-typeset upload? | **Established** | §1 |
| 3 | Does Kauffman state a three-regime classification in his own words, and what are its names? | **Established** | §2 |
| 4 | Is the middle regime *critical* in the phase-transition sense, or merely "interesting"? | **Established** | §2 |
| 5 | Does Kauffman claim the ordered/chaotic dichotomy for himself? | **Refuted** | §3 |
| 6 | Whom does Kauffman credit for the analytic order/chaos result? | **Established** | §3 |
| 7 | Does the book's own credit to Kauffman (1969) match what [#100](https://github.com/NGL321/mosaic/issues/100) read in the 1969 paper? | **Supported** | §3 |
| 8 | Does the attribution in the record move off Derrida & Pomeau? | **Refuted** | §4, Proposals |
| 9 | Should the `_After_` line nevertheless be amended to name Kauffman (1993)? | **Supported** | §4, Proposals |
| 10 | Were Kauffman (1984a) and Kauffman (1990), *Physica D*, reached? | **Unresolved** | Sources not reached |
| 11 | Is Kauffman's own priority claim for the edge-of-chaos hypothesis resolvable from the book? | **Refuted** | §5 |

> **[#121](https://github.com/NGL321/mosaic/issues/121) is discharged, and the answer is the opposite of what the ticket feared.** Kauffman's trichotomy is *ordered, complex, chaotic*, stated in his own words on pp. 174, 183 and 219 of the original 1993 edition, with the complex regime defined as the phase-transition boundary "where frozen components just melt". But on p. 219 he credits the analytic order/chaos result to "the solid-state physicist B. Derrida and his colleagues (Derrida and Pomeau 1986)", and credits his own 1969 paper only for spontaneous order at K = 2 — so the attribution the record already carries is the one Kauffman himself gives, and it does not move. What changes is smaller and additive: Kauffman (1993) can now be cited for the *trichotomy* and the frozen-component account, because it has been read.

## 1. The source that was reached, and why it is the original edition

The Internet Archive item [`stuart-a-kauffman-the-origins-of-order-selforganization-and-complexity-in-evolution`](https://archive.org/details/stuart-a-kauffman-the-origins-of-order-selforganization-and-complexity-in-evolution) is in the `opensource` collection, is **not** `access-restricted`, and serves an 88 MB `Image Container PDF` with a full JP2 page set, hOCR, and a working search-inside index. It is a different item from [`originsoforderse0000kauf`](https://archive.org/details/originsoforderse0000kauf), which [#100](https://github.com/NGL321/mosaic/issues/100) tried and which remains lending-restricted; it did not surface in that document's searches and was found here by querying the Internet Archive's `advancedsearch` API for `title:(origins of order) AND creator:kauffman` rather than by web search.

**The edition is verified from the book, not from the metadata**, and this matters because the uploader's metadata is *wrong*: the item title reads "self-organization and complexity in evolution", which is not the book's subtitle. The scanned copyright page (leaf 1) reads, as printed:

> Copyright © 1993 by Oxford University Press, Inc.
> …
> The origins of order : self-organization and selection in evolution / Stuart A. Kauffman.
> …
> ISBN 0-19-505811-9
> ISBN 0-19-507951-5 (pbk.)
> QH325.K39 1993 577—dc20 91-11148

with the impression line `9 8 7 6 5 4 3` — a later impression of the original edition, in the original setting, not a revised or re-typeset one. The title page names the author as of "University of Pennsylvania and The Santa Fe Institute", and the running heads, page numbers, small-caps headings and italic technical terms are all present as typeset. The scan carries a previous owner's pencil marginalia in the margins of pp. 174 and 219; the printed text is unobscured. This is the "scan of the original edition" that [`docs/research/README.md` §3](README.md) requires, and it is not the aggregator copy [#121](https://github.com/NGL321/mosaic/issues/121) forbids.

## 2. The trichotomy, as Kauffman gives it

**Chapter 5, "Self-Organization and Adaptation in Complex Systems", pp. 173–236.** The chapter's own overview, p. 174, read from the page image:

> Random Boolean networks are a vast family of disordered systems. Yet we shall find that they exhibit three broad regimes of behavior: ordered, complex, and chaotic. In the *ordered* regime, many elements in the system freeze in fixed states of activity. These frozen elements form a large connected cluster, or *frozen component,* which spans, or *percolates,* across the system and leaves behind isolated islands of unfrozen elements whose activities fluctuate in complex ways. In the *chaotic* regime, there is no frozen component. Instead, a connected cluster of unfrozen elements, free to fluctuate in activities, percolates across the system, leaving behind isolated frozen islands. In this chaotic regime, small changes in initial conditions unleash avalanches of changes which propagate to many other unfrozen elements. These avalanches demonstrate that, in the chaotic regime, the dynamics are very sensitive to initial conditions. The transition from the ordered regime to the chaotic regime constitutes a phase transition, which occurs as a variety of parameters are changed. The transition region, on the edge between order and chaos, is the *complex* regime. Here the frozen component is just percolating and the unfrozen component just ceasing to percolate, hence breaking up into isolated islands. In this transition region, altering the activity of single unfrozen elements unleashes avalanches of change with a characteristic size distribution having many small and few large avalanches.

That is the whole trichotomy in one paragraph, with its order parameter (percolation of the frozen component), its control parameters, and its signature at criticality (a broad avalanche-size distribution). **Kauffman's middle term is "complex", not "critical" and not "edge of chaos"** — those are his names for the *region*, not for the regime. This settles row 3 and row 4 together: the middle regime is defined *as* the phase transition, so it is critical in the strict sense, not merely a heuristically interesting band.

The same three names recur, in Kauffman's summary of why the Boolean idealisation is worth adopting, p. 183, item 4, read from the page image:

> Disordered complex Boolean networks, it has turned out, exhibit three major regimes of behavior: ordered, complex, and chaotic. Thus analysis of these extremely complex systems reveals unexpected simplicity with important biological implications for development and evolution.

and again at p. 219, where the classification is stated in terms of the frozen component alone:

> While the zoo of control parameters awaits full disclosure, a critical fact remains: Boolean networks, among the most general class of massively parallel-processing systems, exhibit three broad regimes of behavior. Systems may lie in the ordered regime with frozen components, in the chaotic regime with no frozen components, or in the boundary region between order and chaos where frozen components just melt.

**One wording difference is worth recording**, because it is the one a citer is likely to reproduce. In the front matter ("Themes", p. xvi) Kauffman writes the list as "**ordered, chaotic, and a complex regime on the frontier between order and chaos**" — chaotic second, complex last and glossed. In the body (pp. 174, 183, 219) and in the Chapter 5 précis (p. 30) it is "**ordered, complex, and chaotic**", in dynamical order. Both are Kauffman's; the body form is the one to quote.

The book also states the control parameters plainly, p. 219: `P` (internal homogeneity of the Boolean functions) tuned "from near 1.0 toward 0.5" carries a system from ordered to chaotic; the fraction of canalyzing functions is a second; and "[w]ith *P* constant, for example, systems pass from ordered to chaotic if the number of inputs per variable increases." This is the same two-parameter family that [#100](https://github.com/NGL321/mosaic/issues/100) derived `K · 2p(1−p) = 1` for, written in Kauffman's `P = max(p, 1−p)` convention rather than Derrida & Pomeau's `p`.

## 3. Kauffman does not claim the dichotomy — he credits Derrida & Pomeau

This is the load-bearing finding for the record, and it is on p. 198, in the subsection headed "**K = 2: A Phase Transition to Order in Random Boolean Networks**". Read from the page image:

> It has now been known for over 20 years that Boolean networks which are *entirely random* but subject to the simple constraint that each element is directly controlled by *K* = 2 elements spontaneously exhibit very high order (Kauffman, 1969, 1971a, 1971b, 1971c, 1974). … Three approaches to understanding that order—two analytic, one numerical—have been taken. I shall begin with rather remarkable recent analytic work by the solid-state physicist B. Derrida and his colleagues (Derrida and Pomeau 1986).

Two things follow directly.

**First, row 7.** Kauffman's own credit to his 1969 paper is for *spontaneous order at K = 2* and nothing more — exactly the scope [#100](https://github.com/NGL321/mosaic/issues/100) established by reading the 1969 paper in full and finding zero occurrences of *chaotic*, *critical*, *phase transition* or *regime* in 31 pages. The 1993 book does not retroactively enlarge the 1969 claim; it corroborates the narrow reading.

**Second, rows 5 and 6.** The analytic result that produces the dichotomy is attributed by Kauffman himself, in his own book, to Derrida & Pomeau (1986). He goes on to describe their annealed approximation over pp. 198–200 — quenched versus annealed, Hamming distance, the convergence of initially different states "for *K* = 2 annealed networks but not for *K* > 2" — and then, on p. 219, applies it against himself:

> Theoretical results due to Derrida and Pomeau (1986), described above, powerfully indicate that *K* = 3 networks with randomly chosen Boolean functions are already chaotic.

What Kauffman does claim on p. 219 is narrower and different: not the dichotomy but the **hypothesis that the boundary region is where useful behaviour lives** — "This suggestion has been made by myself (1985c), by Packard (1988), by Langton (1986, 1990), and most recently by Crutchfield (private communication)" — followed immediately by the concession "It is not yet unambiguously clear that this hypothesis is correct."

## 4. What this licenses for Mosaic

**The attribution does not move.** [#100](https://github.com/NGL321/mosaic/issues/100) declined to re-credit the dichotomy to Kauffman (1993) on the grounds that doing so would cite an unread text. The text has now been read, and it turns out to credit Derrida & Pomeau itself. The replacement `_After_` line proposed in [#100](https://github.com/NGL321/mosaic/issues/100) is therefore correct as written, and correct for a stronger reason than it was drafted with: it is not merely *safe* under either resolution of that document's row 10, it is what the source says.

**What is now available that was not.** Three claims can be carried at T3 with a page citation instead of being unciteable:

- the trichotomy's names and the definition of each regime by percolation of the frozen component (p. 174);
- that the middle regime *is* the phase transition, with a heavy-tailed avalanche-size distribution as its signature (p. 174) — this is the closest thing in the read literature to an *observable* at criticality, and unlike `K · 2p(1−p) = 1` it is stated about behaviour rather than about a generator's parameters, which bears on [#122](https://github.com/NGL321/mosaic/issues/122);
- that selection can tune a network between regimes "by relatively simple alterations in a few parameters" (p. 183, item 7), which is the mechanism the Bound's evolvability framing assumes and had not been sourced.

**One caution.** Nothing on these pages gives a criticality test computable on a *given* network; p. 219's control parameters are still ensemble parameters (`P`, canalyzing fraction, in-degree). [#122](https://github.com/NGL321/mosaic/issues/122) is untouched by this document and remains open.

## 5. The one thing the book cannot settle about itself

Kauffman's priority claim on p. 219 — "myself (1985c)" — **points at nothing**. The bibliography's Kauffman entries on p. 671, read from the page image, run `1985a` (*Self-organization, selective adaptation and its limits*, in *Evolution at the Crossroads*), `1985b` (*New questions in genetics and evolution*, *Cladistics* 1:247), and then straight into the 1986 group; there is no `1985c`. Across the entire book the string `1985c` occurs exactly once, in that sentence. Neither 1985a nor 1985b is about Boolean network regimes by title.

This matters beyond pedantry because the Bound's `_After_` line puts Langton (1990) first. If `1985c` resolves to a real dated text, Kauffman precedes Langton on the edge-of-chaos hypothesis by five years and the ordering in that line is wrong; if it is a typo, the claim is unsupported and the line stands. The book cannot decide it, and neither can this document. Filed as [#130](https://github.com/NGL321/mosaic/issues/130).

Adjacent and recorded here because it is checkable and surprising: **the 1990 *Physica D* paper is not in the book's bibliography at all.** The Kauffman entries jump from `1989b` to `1991`. Kauffman (1984a), *Emergent properties in random complex automata*, *Physica* 10D:145, *is* present and is cited repeatedly in Chapter 5 alongside 1969 for the spontaneous-order finding.

## What this does not establish

### Sources not reached

**Both *Physica D* papers were sought and not reached, and there is no open-access copy of either in existence.** Kauffman (1984a), *Emergent properties in random complex automata*, *Physica D* 10:145–156, DOI [`10.1016/0167-2789(84)90257-4`](https://doi.org/10.1016/0167-2789%2884%2990257-4): ScienceDirect landing page [`/science/article/pii/0167278984902574`](https://www.sciencedirect.com/science/article/pii/0167278984902574) returned **HTTP 403**, and the tokenised direct-PDF URL surfaced by search (`…/pdf?md5=7cec23d…&pid=1-s2.0-0167278984902574-main.pdf`) also returned **HTTP 403**; Semantic Scholar's record ([`DOI:10.1016/0167-2789(84)90257-4`](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/0167-2789(84)90257-4?fields=title,openAccessPdf)) returns `openAccessPdf.status: "CLOSED"` with an empty URL; Unpaywall returns `is_oa: false`, `oa_status: "closed"`, `has_repository_copy: false`, `oa_locations: []`. Kauffman (1990), *Requirements for evolvability in complex systems: orderly dynamics and frozen components*, *Physica D* 42:135–152, DOI [`10.1016/0167-2789(90)90071-V`](https://doi.org/10.1016/0167-2789%2890%2990071-V): ScienceDirect [`/science/article/abs/pii/016727899090071V`](https://www.sciencedirect.com/science/article/abs/pii/016727899090071V) returned **HTTP 403**; Semantic Scholar `CLOSED`; Unpaywall `closed`, `has_repository_copy: false`. The DOI resolvers themselves returned HTTP 200 but land on the same 403-gated ScienceDirect pages, so nothing beyond bibliographic metadata was obtained from them. Web search for author-hosted or course-page scans of either paper surfaced only third-party papers *citing* them. **No Santa Fe Institute working-paper copy was found**: a site-scoped search returned nothing first-party, and both papers predate or fall outside the SFI working-paper series' online holdings as surfaced by search. The consequence is bounded: rows 3–7 rest on the 1993 book, which is the ticket's own primary discharge target and is the later, fuller statement; the *Physica D* papers would establish *when* Kauffman first wrote the trichotomy, not *what* it is. **Also not reached, and not attempted:** the `dokumen.pub` re-typeset copy, refused on the same grounds as in [#100](https://github.com/NGL321/mosaic/issues/100); and the access-restricted Internet Archive item [`originsoforderse0000kauf`](https://archive.org/details/originsoforderse0000kauf), which was not re-attempted because a better copy was found — its status is presumed unchanged from [#100](https://github.com/NGL321/mosaic/issues/100)'s 403 and was not re-verified today. **Read only as OCR, not as page images:** the bulk of Chapter 5 outside pp. 174, 183, 198 and 219, and the whole of Chapter 6, so any claim here about what the book does *not* say elsewhere rests on OCR that is demonstrably lossy.

### Open gaps

Three. **First, the date of Kauffman's trichotomy is still unknown.** This document establishes what he says in 1993 and that he credits Derrida & Pomeau for the analytics, but not whether he had the three-regime language before 1986 — which is precisely what the unreached 1984 *Physica D* paper would settle, and the 1984 paper *is* cited in the book for the spontaneous-order finding rather than for regimes, which is weak evidence that he did not. **Second, the avalanche-size distribution at criticality (p. 174) is asserted, not derived, in the passage read.** Kauffman presumably supports it later in Chapter 5, at pages read only as OCR; if it holds up it is a candidate observable for the Bound's Order axis, and a much better one than an ensemble parameter, but this document has not verified it. **Third, whether "complex" and "critical" are the same claim.** Kauffman defines the complex regime as the transition region, which makes it critical by construction — but whether the systems *in* it satisfy the usual criticality diagnostics (power-law avalanche exponents, diverging correlation length) is a separate empirical question the book gestures at and this document did not pursue.

### Load-bearing ifs

**If the Internet Archive item is not what its copyright page says it is, everything here falls.** The defence is that the copyright page, the title page, the running heads, the pagination and the bibliography were each read as page images and are internally consistent with the 1993 OUP setting, and that the printed page numbers cited resolve through the item's own page-number index rather than through leaf counting — but a sufficiently careful forgery would survive all of that, and this document has not compared the scan against a second physical copy. **If the page-number mapping is off by a leaf, the page citations are wrong while the quotations are right.** The mapping was taken from the item's `_page_numbers.json` and cross-checked against the printed folio visible in each page image — p. 174, p. 183, p. 198, p. 219, p. 671 are all legible in the scans quoted — so this is checkable by anyone opening the same item. **If Kauffman elsewhere in the book claims the dichotomy for himself, §3 and row 5 weaken.** The evidence against is that the one place he sets out the analytic result is p. 198, and there he credits Derrida & Pomeau explicitly and in the first person; the evidence is not exhaustive, because the rest of the chapter was read as OCR. **If `1985c` resolves to a real 1985 text on Boolean regimes**, then §5's caution becomes a correction and the `_After_` line's ordering of Langton first is wrong — this is [#130](https://github.com/NGL321/mosaic/issues/130), and it is the single change most likely to move the record next.

## Verification Debt

One item, filed and open.

- **[#130](https://github.com/NGL321/mosaic/issues/130)** — Kauffman's own priority claim for the edge-of-chaos hypothesis, "myself (1985c)" (p. 219), cites a work that does not appear in the book's bibliography (p. 671) and occurs exactly once in the whole text. It cannot be resolved from the book. It bears directly on the `_After_` line, which orders Langton (1990) first: if `1985c` is real, that ordering is wrong. The two *Physica D* papers — Kauffman (1984a) and Kauffman (1990) — remain unread and have no open-access copy anywhere, and are folded into the same item because either would likely resolve it.

[#122](https://github.com/NGL321/mosaic/issues/122) (no per-system criticality test) is unchanged by this document and stays open on its own terms; it is not re-filed here.

## Proposals

**1. The `_After_` line correction proposed in [#100](https://github.com/NGL321/mosaic/issues/100) should be applied as drafted, with one addition.** That document's replacement text is confirmed by the source it could not read: Kauffman credits Derrida & Pomeau for the dichotomy himself. The only change is to add the now-readable 1993 citation for the *three-regime* classification, which [#100](https://github.com/NGL321/mosaic/issues/100) had to omit. Exact replacement text, in the form the line takes in the [#6](https://github.com/NGL321/mosaic/issues/6) answer comment:

```
*After* Langton (1990) on computation at the edge of chaos; Kauffman (1969) for the
finding that randomly constructed low-connectivity Boolean nets are spontaneously
ordered — short state cycles, few attractors, high stability under single-bit noise —
and Derrida & Pomeau (1986) for the ordered/chaotic dichotomy itself, whose annealed
approximation puts the transition at K · 2p(1−p) = 1 for random Boolean networks in
the N → ∞ limit; Kauffman (1993, pp. 174, 219) for the three-regime form Mosaic
actually uses — ordered, complex, chaotic, separated by percolation of the frozen
component — which credits Derrida & Pomeau for the analytics in the same breath;
*departs* by carrying Mitchell, Hraber & Crutchfield's (1993) pushback in-line rather
than inheriting the frame unexamined.
```

If the line is written into `CONTEXT.md` in that file's `_After_:` form, the same text with `*After*` replaced by `_After_:` and the `*departs*` clause moved to its own `_Departs_:` line, per the surrounding entries. As in [#100](https://github.com/NGL321/mosaic/issues/100), the Langton and Mitchell/Hraber/Crutchfield clauses are untouched: this document did not read either.

**2. Use Kauffman's own middle term.** Where Mosaic names the third regime, the word from the source is **complex**, and "critical" and "edge of chaos" are names for the *region*, not the regime (p. 174). Writing "ordered / complex / chaotic" is quoting; writing "ordered / critical / chaotic" is paraphrase and should be marked as such.

**3. Do not order Langton before Kauffman on the edge-of-chaos hypothesis without a caveat**, until [#130](https://github.com/NGL321/mosaic/issues/130) is discharged. Kauffman claims 1985 priority on p. 219 and the citation is dangling; the honest short form is *"Langton (1986, 1990), Packard (1988) and Kauffman independently"* rather than a dated ordering.

**4. Badge text, for Noah to apply if and where the correction lands:** `⟦T3 · #121⟧`.

## Appendix: primary sources

Three. The first is the book, read as page images; the second and third are the open-access-status records that make the "no copy exists" claim in *Sources not reached* checkable rather than merely reported. All retrieved 2026-08-02.

1. S. A. Kauffman (1993), *The Origins of Order: Self-Organization and Selection in Evolution*, Oxford University Press, New York. Original edition, verified from the scanned copyright page: © 1993 Oxford University Press, Inc.; ISBN 0-19-505811-9 (0-19-507951-5 pbk.); QH325.K39 1993; LCCN 91-11148; impression line `9 8 7 6 5 4 3`. Read from the unrestricted page-image scan at [archive.org/details/stuart-a-kauffman-the-origins-of-order-selforganization-and-complexity-in-evolution](https://archive.org/details/stuart-a-kauffman-the-origins-of-order-selforganization-and-complexity-in-evolution) (retrieved 2026-08-02; note the uploader's item title misstates the subtitle — the book's own title page and copyright page are authoritative and were read). Pages read as rendered images: copyright page (leaf 1); **p. 174**, Chapter 5 overview, the trichotomy in full; **p. 183**, chapter summary items 4 and 7; **p. 198**, "K = 2: A Phase Transition to Order in Random Boolean Networks", the Derrida & Pomeau credit; **p. 219**, the three-regime restatement, the control parameters, the Derrida & Pomeau K = 3 result, and the "myself (1985c)" priority claim; **p. 671**, the Kauffman bibliography entries. Read as OCR text only, for locating and for context: Contents (chapter and section pagination), "Themes" p. xvi, the Chapter 5 précis p. 30, and the remainder of Chapter 5, pp. 173–236.
2. Unpaywall open-access record for S. A. Kauffman (1984a), *Emergent properties in random complex automata*, *Physica D* 10:145–156, DOI `10.1016/0167-2789(84)90257-4`: [api.unpaywall.org/v2/10.1016/0167-2789(84)90257-4](https://api.unpaywall.org/v2/10.1016/0167-2789%2884%2990257-4?email=noahlitov@gmail.com) (retrieved 2026-08-02). Read directly, HTTP 200. Cited for exactly one fact: `is_oa: false`, `oa_status: "closed"`, `has_repository_copy: false`, `oa_locations: []` — there is no open-access copy of this paper for any route to find. Corroborated by Semantic Scholar's record for the same DOI, `openAccessPdf.status: "CLOSED"`.
3. Unpaywall open-access record for S. A. Kauffman (1990), *Requirements for evolvability in complex systems: orderly dynamics and frozen components*, *Physica D* 42:135–152, DOI `10.1016/0167-2789(90)90071-V`: [api.unpaywall.org/v2/10.1016/0167-2789(90)90071-V](https://api.unpaywall.org/v2/10.1016/0167-2789%2890%2990071-V?email=noahlitov@gmail.com) (retrieved 2026-08-02). Read directly, HTTP 200. Same single fact: `oa_status: "closed"`, `has_repository_copy: false`. Corroborated by Semantic Scholar, `CLOSED`.

Kauffman (1969), *J. Theor. Biol.* **22**:437–467, and Derrida & Pomeau (1986), *Europhys. Lett.* **1**(2):45–49, are load-bearing for §3 and §4 but were **not read here** — they were read in full under [#100](https://github.com/NGL321/mosaic/issues/100), and their scans and publisher records are in the appendix of [`docs/research/2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md`](2026-08-02-kauffman-and-the-ordered-chaotic-regimes.md). They are cited from that document rather than re-listed, so that this document's source count states what this document opened.
