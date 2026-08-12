# Mosaic

Mosaic is a long-running, LLM-accelerated research programme in computational cognitive science,
investigating cognition as a heterogeneous network of inference engines whose schemas each carry
their own metric space, and the **Transport** between them.

## Language

### Programme structure

Vocabulary adopted from Imre Lakatos, *The Methodology of Scientific Research Programmes* (1978).

**Hard Core**:
The programme's non-negotiable commitments — the downstream claims Mosaic exists to pursue, plus
its starting axioms. Not the target of falsification.
_Avoid_: Thesis, hypothesis, north star

**Protective Belt**:
The auxiliary claims built up around the Hard Core as work proceeds. Individually falsifiable, and
revised or discarded without abandoning the programme.
_Avoid_: The ladder, sub-hypotheses, orbit

**Positive Heuristic**:
The programme's plan for developing itself — the rules governing how Protective Belt claims are
added, pursued, and retired.
_Avoid_: Methodology, process, roadmap

**Negative Heuristic**:
The injunction that falsification is aimed at the Protective Belt, never the Hard Core.

**Problemshift**:
A revision to the Protective Belt. *Progressive* if it predicts novel facts; *degenerating* if it
only accommodates facts already in hand. The programme's own health check.
_Avoid_: Pivot, course correction

### Warrant

**Provenance Tier**:
The label every Mosaic claim carries, recording how it was reached: derived unaided, derived with
assistance and personally verified, or machine-produced and unverified. The tier travels with the
claim wherever the claim goes. **Agent verification does not promote a tier** — an agent's reading
is evidence attached to the claim, and the ladder measures what Noah can defend;
[`curriculum/README.md`](curriculum/README.md#provenance-tiers) holds the normative statement and
the three tiers themselves.
_Avoid_: Confidence level, epistemic status

**Verification Debt**:
A logged step in a claim's derivation that Noah cannot yet defend unaided. Discharged by learning,
not by argument.
_Avoid_: TODO, gap, caveat

**Source**:
One piece of external literature, at a fixed version, together with the claims Mosaic has taken
from it. External evidence **steers and never legs**: **Register** is derived from ancestry, and
Mosaic has no ancestry over another programme's data, so a Source can never be confirmatory — by
construction rather than by policy. Warrant is generated, never received; the route to a leg is
**reproduction**, which is an Inquiry and produces a *new* claim rather than promoting this one,
so the record shows that Mosaic checked rather than trusted. Each claim is held twice — verbatim
and in this repository's own vocabulary — and is frozen at admission, a poor rendering being
superseded by another claim and never edited.
_Avoid_: Citation, reference, paper, literature, prior work, testimony

<!-- Lives in `literature/author-year-slug/`, a sibling of `inquiries/` and `conjectures/`;
     `literature/README.md` holds the rest. Fixed in #167, which also found that the instrument
     a paper supplies needs no Source at all — an Adequacy Criterion is blind to an instrument's
     provenance, and that blindness is where the saving actually comes from. The reading of a
     Source is machine-produced until Noah reads the paper, so its Provenance Tier is derived
     from the sourcing debt's state rather than stored; the debt kinds themselves are being
     separated on the founding-charter map. -->

**Lab Notebook**:
The public, dated audit trail of the programme's process, living in this repo — in effect a rich
commit history. Entries are largely generated — by working sessions, agent task completion, and
Curriculum milestones — and then annotated by Noah. Carries the mistakes and abandoned directions
deliberately. Distinct from Noah's personal notes, which are private reference material in Drive
and serve a different purpose.
_Avoid_: Journal, log, devlog, changelog, notes

**Secure Research**:
A project Noah does not intend to keep public from the outset. The test is intent, not publication
status — unpublished work that is public-by-design is not secure. Mosaic is **not** Secure
Research: it is algorithmic and empirical work whose whole point is being seen, and its loss or
theft would cost nothing. Consequently the sensitive-work compute restrictions in
[`docs/DATA-PROTOCOL.md` §4](docs/DATA-PROTOCOL.md) do not bind it.
_Avoid_: Sensitive, private, confidential

<!-- Noah has flagged this term as needing sharpening; the above records current usage, not a
     settled definition. A future programme phase — testing high-capacity cognitive systems — may
     well be Secure Research. -->


**Transcript Archive**:
The private, append-only store of raw working-session transcripts, held outside this repo. Exists
for defensibility and influence tracing, not publication; Lab Notebook entries cite it by session.
_Avoid_: Logs, history, backups

**Weekly Reflection**:
The once-a-week written consolidation of whatever mattered that week — the programme, the
Curriculum, a paper, or an adjacent thought. A discipline instrument whose value is the act of
writing it, not a rendering of other artifacts. Deliberately unconstrained in topic.
_Avoid_: Blog post as digest, weekly update, devlog

**Curriculum**:
Mosaic's learning track, scheduled off the Verification Debt ledger rather than off a syllabus —
the mathematics the programme's own results demand, in the order they demand it.
_Avoid_: Study plan, coursework

### Delegated inquiry

**Inquiry**:
A single line of empirical investigation delegated to agents, and the unit in which the
programme buys evidence: a frozen Question, an Adequacy Criterion, a search budget, a signed
continue/return/retire rule, and an environment requirement. Persistent and stateful — an
Inquiry may lie dormant for years and resume where it stopped. It is the machinery by which a
Protective Belt claim is earned or refused, and is never itself such a claim.
_Avoid_: Commission, experiment, study, line, direction, project, task

<!-- Nine states, fixed in #56 and formalised in #62. Non-terminal: Searching, Measuring,
     Awaiting Acknowledgement, Awaiting Decision, Awaiting Competence, Dormant. Terminal:
     Answered, Exhausted, Retired. Answered and Exhausted are mutually unreachable — the
     freeze between Searching and Measuring partitions them. -->

**Question**:
The empirical matter an Inquiry exists to settle. Frozen when the Inquiry opens and Noah's
alone — agents search for instruments capable of answering it and may never alter it. A
*hypothesis* is a falsifiable claim about a Question, committed in advance; an Inquiry may run
without one.
_Avoid_: Target, query, goal, objective, research question

**Adequacy Criterion**:
The machine-decidable test of whether an instrument is fit to answer an Inquiry's Question at
all, stated without reference to any hypothesis. Passing it freezes the configuration by SHA
and ends the Inquiry's search. An Inquiry that cannot state one cannot be delegated — a
visible refusal, and itself a finding about the Inquiry.
_Avoid_: Competence criterion, fitness function, validity check, baseline

<!-- Distinct from the competence floor, which is a property of Noah rather than of an
     instrument. The two were both called "competence" until #56 separated them. -->

**Experiment**:
One instrument, configured — the functional process a Run executes. Identified by the sha256
of its configuration and by nothing else: two configurations differing at all are two
Experiments however alike their intent, and two that are byte-identical are one however
separately they were arrived at. It does not belong to an Inquiry — the two are independent,
and it is a Run that names both. Declared, never produced.
_Avoid_: Inquiry, trial, condition, arm, variant

<!-- In Searching, Experiments are tried against the Adequacy Criterion; at the freeze one
     Experiment's configuration becomes the Inquiry's frozen config, and the discriminating
     measurement is runs of that one. The word is phase-neutral — what changes at the freeze
     is who may open one, which is a property of the state. -->

**Run**:
One execution of an Experiment under an Inquiry — the only one of the three that is produced
rather than declared, and the only one that leaves a record. It names both axes: the Experiment
gives it a configuration, the Inquiry gives it a Question and pays for it. What varies between
runs of one Experiment is only what that configuration itself declares varies; the seed is drawn
per run and recorded, never written into the config. Output publishes outside the repository
and one manifest stays behind — run id, config SHA, seed, output sha256, Drive path.
_Avoid_: Experiment, job, trial, iteration

<!-- One Run is several CI jobs: #58's checkpoint-and-resume, forced by GITHUB_TOKEN's
     24-hour expiry, resumes as a fresh job. A job is a dispatch event, not a unit of evidence. -->

**Register**:
Which of two modes a result was produced in. *Confirmatory* if its metric and decision rule
are ancestors of the data they judge; *exploratory* otherwise. Exploratory results are
first-class in the record and barred from the Protective Belt; their only route in is to
become the committed hypothesis of a new Inquiry. A property of a result, never of an
Inquiry — one Inquiry ordinarily produces both.
_Avoid_: Preregistered, post-hoc, mode, class, tier

### Research substance

Every term here is contested in the contemporary literature. Where Mosaic borrows one, the source
is named on an `_After_` line; where Mosaic's usage diverges from that source, the divergence is
named on a `_Departs_` line. Departures are fine; unmarked departures are not.

> **The terms are here; the commitments are in the charter.** Where an entry below says *the
> programme's first axiom* or *an axis of the Edge of Chaos Bound*, it is naming a Hard Core
> member, not stating it. What each member commits the programme to, which stratum it sits in and
> what fires its escape hatch are the charter's ([`CHARTER.md`](CHARTER.md), assembled under
> [#12](https://github.com/NGL321/mosaic/issues/12)); `PROTOCOL.md` §3's rule that a definition is
> not a claim is why they are not restated here. Until the charter exists,
> [#6](https://github.com/NGL321/mosaic/issues/6) is canonical for the roster.

Each term carries its **Provenance Tier** as a badge — `⟦T3 · #33⟧`, the tier and the debt issues
holding it down. Every one of them is **T3**; see [Provenance of this
section](#provenance-of-this-section) at the foot of the section for what that means here and what
it does not.

**Inference Engine**: ⟦T3⟧
A system delineated by a Markov blanket whose internal state carries predictive information about
states beyond that blanket — over and above what its current boundary state carries. Being an
engine is a matter of degree — measured by **Extraction**, below — and many blanketed systems are
not one at all. The degree is **not a scalar**: an engine's Extraction is one number, but the
**Closure** of each of its schemas is another, and the two move independently.
_Avoid_: Agent, model, module, particle, node
_After_: Pearl (1988) for the blanket as conditional independence; Friston for its use as the
boundary of a thing.
_Departs_: The blanket **individuates** but does not **qualify**. Friston's construct does both —
every blanketed thing is already minimising free energy. A Mosaic engine has to hold predictive
information to count, so the criterion is thermodynamic rather than definitional.

**Extraction**: ⟦T3 · #33⟧
How much of the predictive structure *available in what an engine observes* the engine actually
captures — its achieved predictive information as a fraction of the ceiling set by the observed
process itself. A property of the inference machinery, and the sense in which an engine has a
degree. Because it is a ratio against a ceiling, it compares across environments without requiring
a measure over environments.
_Avoid_: Accuracy, performance, capability, intelligence
_Departs_: Not a raw quantity. Attempts to define machine intelligence as an absolute aggregate —
Legg & Hutter (2007) summing over environments under a Kolmogorov-complexity weighting — inherit an
uncomputable and reference-machine-dependent measure. Normalising against the observed process's own
ceiling avoids needing one. Closer in spirit to Chollet (2019), where the quantity is achievement
relative to what was given, though Mosaic normalises by *observational access* rather than by priors
and experience.

**Representation**: ⟦T3 · #32⟧
A set of world-states an engine's internal state does not distinguish, whose separation from other
such sets is *sensitive* and *specific* to some feature, *invariant* to the rest, and *functional*
— carrying predictive information the engine's inference actually uses. Structure that is not
functional is not a representation; whatever it retains that is not predictive is, under least
action, dissipated work.
_Avoid_: Feature, encoding, latent, embedding, concept
_After_: Pohl, Walker, Barack, Lee, Denison, Block, Meyniel & Ma (2026) for the four dimensions;
Tishby, Pereira & Bialek (1999) for compression against a relevance variable, and Still (2014) for
making that variable the future.
_Departs_: Pohl et al.'s dimensions are **evidential** — they say when an experimenter's evidence
for a representation is strong. Mosaic's definition is **constitutive**, and takes their dimensions
as its measurement instrument rather than as its content. Named by *content* (which world-states
are collapsed), not by *vehicle* (which internal states do the collapsing).

**Schema**: ⟦T3 · #30, #31⟧
A coherent set of representations that hang together and update as a unit, carrying **its own
metric space** — not every problem is solvable from the same perspective, so schemas addressing
different problems are not commensurable by default. An engine holds many; holding exactly one is a
special case. Schemas nest, combine, and conflict. The metric attaches here and not to the engine,
so an engine holding several schemas is itself a small network.
_Avoid_: Ontology, scheme, carving, representational scheme, frame, script, world model
_After_: Piaget, for the unit and for **assimilation** (input sorted into representations already
held) and **accommodation** (the set itself re-carves); Piaget & García, *Psychogenesis and the
History of Science* (1989), for the same mechanism in scientific theory change.
_Departs_: Piaget's *schème* is the generalisable structure of an **action**; a Mosaic Schema is a
set of representations. English translation collapses *schème* and *schéma*, and Mosaic's usage
matches neither exactly.

**Closure**: ⟦T3 · #33⟧
How much of the environment's influence on what a schema observes is accounted for by those
observations themselves — whether the schema is self-sufficient or driven from outside. A property
of *which* variables were carved together, so it belongs to the schema and not to the engine
reasoning over it. Under low Closure a schema may still predict well, with most of what drives its
observations unseen.
_Avoid_: Modularity, encapsulation, independence, sufficiency
_After_: **Informational closure** (Bertschinger, Olbrich, Ay & Jost, on closure and level
identification in systems theory); **lumpability** of Markov chains (Kemeny & Snell) as the exact
degenerate case, where a coarse-graining is a Markov chain in its own right.
_Departs_: Treated as a **graded** quantity and as an object of study, where the systems-theory
literature largely treats closure as a property a level either has or lacks.

<!-- Closure is a schema-level sibling of Obstruction: Obstruction measures whether schemas agree
     with each other, Closure whether a schema is self-sufficient against the world. One faces
     inward across the network, the other outward. -->

<!-- Extraction and Closure are ratios against ceilings, which is why the degree of an engine can be
     compared across environments at all. That property is load-bearing and should not be traded
     away for a more convenient absolute measure. -->

<!-- Poincaré, "Mathematical Creation" (Science and Method, 1908), is cited for the incubation
     phenomenology — the fuzzy conception that sharpens while one is occupied elsewhere, and the
     aesthetic sieve that selects which combinations surface. The *word* schema is not his; the
     mechanism claim is Piaget's. -->

**Transport**: ⟦T3⟧
The structured relation carrying a representation in one schema to its counterpart in another —
what makes two inferences held in different metric spaces comparable at all.
_Avoid_: Mapping, translation, alignment, projection, correspondence
_After_: Cellular sheaves for the structure (restriction maps between stalks); gauge theory for the
symmetry acting on it (a choice of coordinates within a stalk is a gauge, and Transport is the
connection that survives that choice). Singer & Wu's connection Laplacian is the special case of
Hansen & Ghrist's sheaf Laplacian over a graph in which every map is orthogonal.
_Departs_: "Gauge symmetry between inferences" was the programme's original phrasing and is
retired. In physics a gauge symmetry is **exact** — redundancy in describing one system. Mosaic
keeps that sense only *within* a schema, and treats the between-schema case as a connection rather
than a symmetry. The apparatus borrowed is the fibre bundle, not the phrase.

**Obstruction**: ⟦T3 · #97⟧
The failure of Transport to be consistent: a representation carried around a loop of schemas does
not come back to itself. Not noise and not error — a property of the network's structure.
Occurs *within* an engine (its own schemas will not reconcile) as well as between them.
_Avoid_: Disagreement, inconsistency, error, misalignment, conflict
_After_: Curvature and holonomy in gauge theory; sheaf cohomology for the obstruction to a
consistent global section.

**Schema Dynamics**: ⟦T3 · #29⟧
The level of description above the engine — how representations relate within a schema and schemas
relate across engines — together with the claim that general cognitive capacity is a property of
those relations rather than of any single engine. Mosaic's object of study.
_Avoid_: Emergence, integration, binding, higher-order cognition
_After_: Mountcastle's columnar organisation (1957; 1978) for the repeated-unit picture, held here
as a **hypothesis** and a contested one (Horton & Adams, 2005), never a theorem — Mountcastle
himself offered it as an organising principle. Piaget for the within-schema case. Applied
mathematics generally, where a problem is decomposed into local approximations that compose into a
whole.
_Departs_: This line of thought **originated** in reading the **Thousand Brains Theory** (Hawkins,
Lewis, Klukas, Purdy & Ahmad, 2019; Hawkins, 2021) and disagreeing with it — the disagreement is
the programme's seed, not a boundary drawn afterwards. There, many cortical columns model *the same
object*, each from its own sensory patch and its own location in an object-anchored reference
frame, and vote toward a consensus about which object is present. Mosaic's schemas are
heterogeneous by construction — different problems, not one problem in different coordinates — and
the two accounts face opposite directions: Thousand Brains' voting is engineered to make
reconciliation **succeed**, where Mosaic looks at where it **fails** (Obstruction). A contrast in
direction, and not a claim that Obstruction is the programme's primary observable —
[#9](https://github.com/NGL321/mosaic/issues/9) withdrew that claim, and Obstruction holds no
status in the Positive Heuristic, neither primacy nor preference. The
specific disagreements, and which of them Noah attributes to engineering assumptions imported into
the theory, are stated in their own ticket rather than here.

**Least Action**: ⟦T3 · #32⟧
The programme's first axiom: information transformation is a thermodynamic process, so inference is
subject to the same variational principle as any other physical process. Free energy is one
candidate functional under it, not the axiom itself.
_Avoid_: Free energy principle, efficiency, optimisation pressure
_After_: Jaynes (1957) for entropy as an inferential quantity and Landauer (1961) for the
thermodynamic cost of erasure — a *bound*, not an identity; Still, Sivak, Bell & Crooks (2012) for
retained non-predictive information as dissipated work.
_Departs_: Held as Hard Core by *disciplinary* declaration — Mosaic is computational cognitive
science, not physics, and does not investigate the axiom's own falsifiers.

**Scale Corollary**: ⟦T3⟧
The programme's second axiom, and an actual corollary of **Least Action** rather than a second
stipulation: thermodynamic systems are information systems, and least action applies to any system
describable as a complex system of discrete parts, so the principles above hold at every such
level. A mathematical model, an artificial network and a biological one are therefore corollaries
of one another — differing in scale, not in kind. It is what licenses Mosaic to speak of minds
without speaking of brains.
_Avoid_: Scale invariance, level independence
_Departs_: **Exposed, not permitted.** This is the one Hard Core member ordinary belt work can
falsify as a side effect. The cross-domain convergence search rule tests it every time it runs,
because this axiom is what licenses treating artificial and biological networks as corollaries of
one another: if features found in machine-learning systems reliably fail to appear in neural
population data, the thing that has failed is the Scale Corollary. That is an exposure the
programme's own method creates, not a permission it grants itself, and it does **not** make the
axiom a targetable Inquiry Question — the Negative Heuristic's injunction stands uniform.

**Structural Realisation**:
The programme's third axiom: cognition arises from **structure, not substance**. Held separately
from the **Scale Corollary** because the warrant is different in kind — reasoned from bounded
solution spaces and the dynamical-systems view, not from physics. *Monist rider:* structure is
always the structure **of** a physical system. There is no structure without a substrate, and no
dependence on **which** substrate — multiple realisability without Plato's dualism.
Together with the **Scale Corollary** this yields a derived consequence, one level above
substrate: independence from the *implementing computation*. A Turing machine built inside
Conway's Game of Life does not depend on the hardware Life runs on — the Scale Corollary holds the
principles at every level of the stack, and Structural Realisation fixes the machine's identity at
the level where its structure lives. Stated as a derivation rather than a fourth axiom, because
that derivation is where the physics-sourced and dynamics-sourced commitments unify.
_Avoid_: Substrate independence, multiple realisability, universality

**Informational Capacity**:
One of the two axes of the **Edge of Chaos** Bound — the axis excluding the under-ordered. Named
here so the Bound has vocabulary to be stated in; **operationalised under
[#87](https://github.com/NGL321/mosaic/issues/87) and landing under
[#104](https://github.com/NGL321/mosaic/issues/104)**, and this entry says so rather than guessing
at a definition. *Informational* is not decoration: bare "capacity" collides with the general
cognitive capacity named in **Schema Dynamics**.
_Avoid_: Capacity, bandwidth, expressivity, complexity

**Order**:
The other axis of the **Edge of Chaos** Bound — the axis excluding the over-ordered. Named here on
the same terms as **Informational Capacity**, with its operational definition deferred to
[#104](https://github.com/NGL321/mosaic/issues/104).
_Avoid_: Structure, regularity, stability, criticality

---

### Provenance of this section

**Every attribution above is T3 — machine-produced and not verified by Noah.** The `_After_` and
`_Departs_` lines were read back to primary sources by an agent in
[#13](https://github.com/NGL321/mosaic/issues/13), which is **evidence, not warrant**; the tier
does not move until Noah does the reading. See
[`curriculum/README.md`](curriculum/README.md#provenance-tiers) for why. Open debt:
[`label:debt:open`](https://github.com/NGL321/mosaic/issues?q=is%3Aissue+label%3Adebt%3Aopen).

Verified as written under [#13](https://github.com/NGL321/mosaic/issues/13): Still et al. (2012),
Tishby et al. (1999), Still (2014), Pearl (1988), Friston (2013; 2019), Piaget, Piaget & García
(1989), Poincaré (1908), Horton & Adams (2005), Singer & Wu / Hansen & Ghrist, and the Pohl/Walker
bibliographic details. Corrected as a result: the Jaynes/Landauer line (Landauer states a bound,
not an identity, and explicitly declines to rest his argument on an entropy–information
connection); the Tishby/Still credit split; **Representation**'s "dissipated work" line; the
Mountcastle hedge; and the Hawkins "interchangeable reference frames" claim.

**The badge attaches to an entry's `_After_` and `_Departs_` lines, not to its definition** — those
are factual claims about what a cited source says, and a definition is not a claim
([`PROTOCOL.md` §3](PROTOCOL.md)). That is why **Programme structure** and **Warrant** carry no
badges, and why **Structural Realisation**, **Informational Capacity** and **Order** carry none
either: they cite nothing yet.
