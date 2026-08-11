# Mosaic

Mosaic is a long-running, LLM-accelerated research programme in computational cognitive science,
investigating cognition as a heterogeneous network of inference engines operating in
representation-constrained metric spaces.

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
claim wherever the claim goes.
_Avoid_: Confidence level, epistemic status

**Verification Debt**:
A logged step in a claim's derivation that Noah cannot yet defend unaided. Discharged by learning,
not by argument.
_Avoid_: TODO, gap, caveat

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

**Prospect**:
A notion in flight — a direction the programme could take, recorded because it is worth keeping
and not yet worth acting on. Either a *proto-conjecture* (a notion not yet defensible enough to
post to the belt graph) or a *proto-Inquiry* (a line of investigation with no statable frozen
Question), or both at once. Deliberately incomplete, and asserted of nothing: a Prospect is never
a claim, carries no warrant, and obliges the programme to nothing. Filing one is free and open to
anyone — Noah, an agent, or an outsider.
_Avoid_: Seed, idea, lead, hunch, backlog item

<!-- "Seed" is barred here specifically: it is reserved for the mathematical sense already defined
     on Run, in this same section — "the seed is drawn per run and recorded". -->

<!-- The backlog is #109, open permanently; entries are its comments and its body is the
     authoring format. A Prospect precedes an Inquiry, which is why it is first in this section. -->

**Conjecture**:
A node posted at a distance from the Hard Core and the admitted Protective Belt because Noah
suspects it is true and cannot yet show it. Noah's prose, by hand, always — agents may propose
one as a Prospect and may never post one. It is the unit that holds a token allocation, a spend
ceiling, a stall tolerance, and the formal system its Inquiries reason into. Retiring one is his
alone: a conjecture is a belief he holds, so a silent retirement would leave him believing what
the programme has abandoned.
_Avoid_: Hypothesis, direction, line, thesis, guess

<!-- The Hard Core is premise-only in a conjecture's system: it may support a derivation and may
     never be its goal. A result that bears on the core is one whose admission makes the system
     inconsistent, which is how #61 mechanises the Negative Heuristic's mandatory return. -->

**Inquiry**:
A single line of empirical investigation delegated to agents, and the unit in which the
programme buys evidence: a frozen Question, an Adequacy Criterion, and an environment
requirement. Opened by an agent under a posted Conjecture, whose budget pays for it and whose
formal system its results enter as axioms. One Inquiry may serve several Conjectures, because an
axiom is not owned by the system that bought it. Persistent and stateful — an Inquiry may lie
dormant for years and resume where it stopped. It is the machinery by which a Protective Belt
claim is earned or refused, and is never itself such a claim.
_Avoid_: Commission, experiment, study, line, direction, project, task

<!-- Nine states, fixed in #56 and formalised in #62. Non-terminal: Searching, Measuring,
     Awaiting Acknowledgement, Awaiting Decision, Awaiting Competence, Dormant. Terminal:
     Answered, Exhausted, Retired. Answered and Exhausted are mutually unreachable — the
     freeze between Searching and Measuring partitions them. -->

**Question**:
The empirical matter an Inquiry exists to settle. Drafted by the agent that opens the Inquiry,
frozen the moment it opens, and never altered afterwards — the freeze is what matters here, and
it binds agents absolutely. Reviewed by Noah when the Inquiry returns a result worth
acknowledging. A *hypothesis* is a falsifiable claim about a Question, committed in advance; an
Inquiry may run without one.
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
gives it a configuration, the Inquiry gives it a Question, and the Conjecture that Inquiry
serves pays for it. What varies between
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

**Inference Engine**:
A system delineated by a Markov blanket whose internal state carries predictive information about
states beyond that blanket — over and above what its current boundary state carries. Its dynamics
are a controlled Markov process over internal and boundary states jointly. Being an engine is a
matter of degree — measured by **Extraction**, below — and many blanketed systems are not one at
all. The degree is **not a scalar**: an engine's Extraction is one number, but the **Closure** of
each of its schemas is another, and the two move independently.
_Avoid_: Agent, model, module, particle, node
_After_: Pearl (1988) for the blanket as conditional independence; Friston for its use as the
boundary of a thing.
_Departs_: The blanket **individuates** but does not **qualify**. Friston's construct does both —
every blanketed thing is already minimising free energy. A Mosaic engine has to hold predictive
information to count, so the criterion is thermodynamic rather than definitional.

**Extraction**:
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

**Representation**:
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

**Schema**:
A coherent set of representations that hang together and update as a unit, carrying **its own
metric space** — not every problem is solvable from the same perspective, so schemas addressing
different problems are not commensurable by default. An engine holds many; holding exactly one is a
special case, and the common one. Schemas nest, combine, and conflict — and that mid-level
structure, not the individual representation, is where compositionality lives. The metric attaches
here and not to the engine, so an engine holding several schemas is itself a small network.
_Avoid_: Ontology, scheme, carving, representational scheme, frame, script, world model
_After_: Piaget, for the unit and for **assimilation** (input sorted into representations already
held) and **accommodation** (the set itself re-carves); Piaget & García, *Psychogenesis and the
History of Science* (1989), for the same mechanism in scientific theory change.
_Departs_: Piaget's *schème* is the generalisable structure of an **action**; a Mosaic Schema is a
set of representations. English translation collapses *schème* and *schéma*, and Mosaic's usage
matches neither exactly.

**Closure**:
How much of the environment's influence on what a schema observes is accounted for by those
observations themselves — whether the schema is self-sufficient or driven from outside. A property
of *which* variables were carved together, so it belongs to the schema and not to the engine
reasoning over it. High **Extraction** under low Closure is the interesting case: predicting well
despite most of what drives the observations being unseen.
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

<!-- Provenance Tier for Extraction and Closure: machine-produced, unverified. Legg & Hutter,
     Chollet, Bertschinger et al., and Kemeny & Snell are recall, not warrant. Verification Debt. -->


<!-- Poincaré, "Mathematical Creation" (Science and Method, 1908), is cited for the incubation
     phenomenology — the fuzzy conception that sharpens while one is occupied elsewhere, and the
     aesthetic sieve that selects which combinations surface. The *word* schema is not his; the
     mechanism claim is Piaget's. -->

**Transport**:
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

**Obstruction**:
The failure of Transport to be consistent: a representation carried around a loop of schemas does
not come back to itself. Not noise and not error — a computable property of the network's
structure. Occurs *within* an engine (its own schemas will not reconcile) as well as between them.
_Avoid_: Disagreement, inconsistency, error, misalignment, conflict
_After_: Curvature and holonomy in gauge theory; sheaf cohomology for the obstruction to a
consistent global section.

**Schema Dynamics**:
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
its primary observable is where reconciliation **fails** (Obstruction), not where it succeeds. The
specific disagreements, and which of them Noah attributes to engineering assumptions imported into
the theory, are stated in their own ticket rather than here.

**Least Action**:
The programme's first axiom: information transformation is a thermodynamic process, so inference is
subject to the same variational principle as any other physical process. Free energy is one
candidate functional under it, not the axiom itself.
_Avoid_: Free energy principle, efficiency, optimisation pressure
_After_: Jaynes (1957) for entropy as an inferential quantity and Landauer (1961) for the
thermodynamic cost of erasure — a *bound*, not an identity; Still, Sivak, Bell & Crooks (2012) for
retained non-predictive information as dissipated work.
_Departs_: Held as Hard Core by *disciplinary* declaration — Mosaic is computational cognitive
science, not physics, and does not investigate the axiom's own falsifiers.

<!-- Provenance Tier: machine-produced, checked against primary sources. Every attribution in this
     section was read back to the source in docs/research/2026-07-28-verifying-cited-influences.md
     (ticket #13). Verified as written: Still et al. (2012), Tishby et al. (1999), Still (2014),
     Pearl (1988), Friston (2013; 2019), Piaget, Piaget & García (1989), Poincaré (1908), Horton &
     Adams (2005), Singer & Wu / Hansen & Ghrist, and the Pohl/Walker bibliographic details.
     Corrected here as a result: the Jaynes/Landauer line (Landauer states a bound, not an identity,
     and explicitly declines to rest his argument on an entropy–information connection); the
     Tishby/Still credit split; Representation's "dissipated work" line; the Mountcastle hedge; the
     Hawkins "interchangeable reference frames" claim.

     Remaining Verification Debt, logged against the Curriculum: Mountcastle (1957; 1978) and
     Piaget's 1929 Limnaea paper were not read in original; Piaget's own distinct use of *schéma*
     is unconfirmed from primary French; and the derivation of Still et al.'s Eq. (14), together
     with its no-feedback assumption, is not yet defensible unaided. -->

**Scale Corollary**:
The programme's second axiom: the properties above hold at any scale and on any substrate, so a
mathematical model, an artificial network and a biological one are corollaries of one another —
differing in scale and substrate, not in kind. Held as a working axiom the programme may itself
falsify. It is what licenses Mosaic to speak of minds without speaking of brains.
_Avoid_: Substrate independence, multiple realisability, universality
