# Krakauer et al. (2020) — The information theory of individuality

Admitted 2026-08-13 by [#199](https://github.com/NGL321/mosaic/issues/199), which split
[#144](https://github.com/NGL321/mosaic/issues/144) into this Source and a reproduction Prospect.

**Reading debt: [#209](https://github.com/NGL321/mosaic/issues/209), open.** While it is open the
reading below is **T3** — machine-produced and unverified. The tier is derived from that issue's
state and is stored nowhere, here included.

## Citation

Krakauer, D., Bertschinger, N., Olbrich, E., Flack, J. C. & Ay, N. (2020). *The information theory
of individuality.* **Theory in Biosciences 139:209–223.**
DOI [10.1007/s12064-020-00313-7](https://doi.org/10.1007/s12064-020-00313-7). PMID 32212028,
PMCID [PMC7244620](https://pmc.ncbi.nlm.nih.gov/articles/PMC7244620/). Open access, CC BY.

**The fixed version is the 2020 version of record, and this matters here more than usual.**
[arXiv:1412.2447v1](https://arxiv.org/abs/1412.2447) (8 December 2014) is a *different text* under
the same title and authors — it carries a different abstract, and the correspondence of its body to
the published article has not been established. Every claim below is located in the 2020 article.
Any future claim taken from the arXiv preprint is a claim from a different Source and must be
admitted as one.

**Retrieval route.** Publisher record via `link.springer.com`, **status: redirected to an
authorization endpoint and not read**. Full text read at the PMC open-access deposit
`https://pmc.ncbi.nlm.nih.gov/articles/PMC7244620/`, **status: 200, read**, 2026-08-13. Bibliographic
record cross-checked at the Europe PMC REST API, **status: 200**. The arXiv abstract page
`https://arxiv.org/abs/1412.2447`, **status: 200**; the arXiv PDF `https://arxiv.org/pdf/1412.2447v1`,
**status: 200 but the text layer was not extractable**, which is why the preprint's body is declared
unread above rather than compared.

Section headings referenced below are the article's own, in order: *The architecture of
individuality*, *Standard assumptions and challenges*, *A way forward*, *Formalizing individuality*,
*Fine-grained decomposition*, *Forms of individuality*, *Individuality measures in an illustrative
example*, *Implications of ITI*, *Future work*, *Appendix: Reflections on closure and sufficiency*.
**The displayed equations in *Forms of individuality* carry no printed numbers**, so they are located
by their labels and by section, which is the finest locator the article affords.

## Claims

### claim-1 — the individuation criterion

**Quoted** — *Appendix: Reflections on closure and sufficiency*:

> "We can think about an individual as a system that is a sufficient predictor of its own future.
> This implies that that S<sub>n−1</sub> does not add any information about S<sub>n+1</sub> besides
> the one already contained in S<sub>n</sub>."

with the formal condition, same appendix:

> I(S<sub>n+1</sub>; S<sub>n−1</sub> | S<sub>n</sub>) = 0

**Rendered** — An **Inference Engine** is individuated by selecting the partition of a declared
observable that is a sufficient statistic for its own future: conditioning on the present screens
off the past. This is the same predictive-sufficiency criterion Mosaic already uses to *qualify* an
engine, applied one level up to *select* what the engine is, so individuation and qualification are
one criterion at two levels rather than two criteria glued together.

**Note on an earlier misquotation.** `docs/research/2026-07-28-markov-blanket-individuation.md` §6
renders this as *"a system **partition** that is a sufficient predictor of its own future"*. The
article says *"a system"*. The inserted word is load-bearing in that document's argument — its whole
recommendation is that the *partition search* carries individuation — and the article puts the
partition search elsewhere (claim-4, and *A way forward*). The reading survives, but it is Mosaic's
inference and not the authors' sentence. This is the first thing the Quoted/Rendered pair was built
to catch, and it caught it on the first Source admitted.

### claim-2 — closure is strictly stronger than sufficiency

**Quoted** — *Appendix: Reflections on closure and sufficiency*:

> "Informational closure is therefore a stronger notion than sufficiency which allows the system to
> be influenced by the environment as long as this influence cannot be predicted from within the
> system."

**Rendered** — Informational closure implies predictive sufficiency and is not implied by it. A
system may be sufficient for its own future while still being driven by an environment, provided the
drive is unpredictable from inside. So a **Closure** result licenses a sufficiency result, and never
the reverse.

### claim-3 — the three forms, and what is *not* in the paper

**Quoted** — *Forms of individuality*, four unnumbered displayed definitions:

> **Organismal Individuality**: A\* = SI(S<sub>n+1</sub>; S<sub>n</sub>, E<sub>n</sub>) + UI(S<sub>n+1</sub>; S<sub>n</sub> \\ E<sub>n</sub>)
>
> **Colonial Individuality**: A = CI(S<sub>n+1</sub>; S<sub>n</sub>, E<sub>n</sub>) + UI(S<sub>n+1</sub>; S<sub>n</sub> \\ E<sub>n</sub>)
>
> **Environmental determination**: nC = I(S<sub>n+1</sub>; E<sub>n</sub> | S<sub>n</sub>) = CI(S<sub>n+1</sub>; S<sub>n</sub>, E<sub>n</sub>) + UI(S<sub>n+1</sub>; E<sub>n</sub> \\ S<sub>n</sub>)
>
> **Environmental Coding**: NTIC = SI(S<sub>n+1</sub>; S<sub>n</sub>, E<sub>n</sub>) − CI(S<sub>n+1</sub>; S<sub>n</sub>, E<sub>n</sub>)

**Rendered** — Individuality is graded and comes in three forms distinguished by how the information
a system carries about its own future is split between shared, unique and complementary parts of a
partial-information decomposition. `A*` is the organismal form, `A` the colonial form, `NTIC` the
difference between the shared and complementary terms.

**`A* − A = NTIC` is not a statement in this paper.** It is an immediate consequence of the three
definitions above — the `UI(S_{n+1}; S_n \ E_n)` term is common to `A*` and `A` and cancels, leaving
`SI − CI`, which is the definition of `NTIC`. But the article states it nowhere, and the expansion
*"non-trivial informational closure"* does not appear in the article at all; it belongs to the
earlier informational-closure literature (Bertschinger, Olbrich, Ay & Jost), which is a different
Source not yet admitted. Two things follow, and both are corrections to
[#144](https://github.com/NGL321/mosaic/issues/144) as filed:

1. The identity is **one line of algebra from the paper's own definitions**, not the half-page
   derivation #144 described. What is genuinely half a page, and genuinely worth reproducing, is the
   appendix that gives claim-2.
2. #144 says the closure ⇒ sufficiency implication *"follows from"* the identity. **It does not.**
   Claim-2 is an appendix result relating two notions; claim-3 is a decomposition of individuality
   into forms. They are independent, and the reproduction Prospect treats them as two items.

### claim-4 — individuals nest, by construction

**Quoted** — *A way forward*:

> "We wish to allow for a hierarchy of such partitions in order to capture biological examples such
> as organelles within cells, and cells within bodies within populations."

**Rendered** — The criterion admits nested individuals rather than a single flat carve, so an engine
may contain engines. This is what makes it usable at both the schema and the engine level of
Mosaic's existing nesting without a second apparatus.

### claim-5 — what the criterion presupposes

**Quoted** — abstract, 2020 version of record, in full:

> "Despite the near universal assumption of individuality in biology, there is little agreement about
> what individuals are and few rigorous quantitative methods for their identification. Here, we
> propose that individuals are aggregates that preserve a measure of temporal integrity, i.e.,
> "propagate" information from their past into their futures. We formalize this idea using
> information theory and graphical models. This mathematical formulation yields three principled and
> distinct forms of individuality—an organismal, a colonial, and a driven form—each of which varies
> in the degree of environmental dependence and inherited information. This approach can be thought
> of as a Gestalt approach to evolution where selection makes figure-ground (agent–environment)
> distinctions using suitable information-theoretic lenses. A benefit of the approach is that it
> expands the scope of allowable individuals to include adaptive aggregations in systems that are
> multi-scale, highly distributed, and do not necessarily have physical boundaries such as cell walls
> or clonal somatic tissue. Such individuals might be visible to selection but hard to detect by
> observers without suitable measurement principles. The information theory of individuality allows
> for the identification of individuals at all levels of organization from molecular to cultural and
> provides a basis for testing assumptions about the natural scales of a system and argues for the
> importance of uncertainty reduction through coarse-graining in adaptive systems."

**Rendered** — The criterion selects a partition of a **declared** observable; it does not choose
the observable. Mosaic's boundary is therefore a fact relative to a stated measurement, and the
modeller's discretion is reduced from *where is the boundary* to *what is being measured* — an
explicit, reportable, criticisable choice, not a hidden ontological assertion. **This is a reduction
of the map/territory problem and not a solution to it, and must never be presented as one.**

## Corroboration

Append-only.

- **2026-08-13** — Not yet searched. `docs/research/2026-07-28-markov-blanket-individuation.md` §6.1
  observes that Mosaic's **Closure** entry independently credits Bertschinger, Olbrich, Ay & Jost —
  three of these five authors — for the same informational-closure apparatus. That is a shared
  lineage, **not independent corroboration**, and is recorded here so it is not later mistaken for
  one. Whether Mosaic's schema-level Closure and this article's engine-level non-closure are one
  quantity at two levels is open; see [#144](https://github.com/NGL321/mosaic/issues/144) item 6a.

## Reproduction

Append-only.

- **2026-08-13** — None. Filed as a Prospect on the backlog —
  [#109 comment](https://github.com/NGL321/mosaic/issues/109#issuecomment-5286742091) — re-aimed at
  claim-2 and claim-3 as two independent items rather than at the single identity #144 named. No
  Inquiry is open, and until one is, nothing here may enter the eligibility fragment.
