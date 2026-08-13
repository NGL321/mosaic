# Literature

**Research track.** Everything under this directory fails the test in
[`PROTOCOL.md` §1](../PROTOCOL.md): if it changed silently, a result already in the record
could become wrong. A **Source**'s claims are premises that steered a search, and under
[#61](https://github.com/NGL321/mosaic/issues/61) a result is judged against what was a git
ancestor of its data — so a premise that could change without leaving a trace would silently
re-judge work already done.

A **Source** is one piece of external literature, at a fixed version, together with the claims
Mosaic has taken from it. Mosaic is not a survey of other people's research, but it must be
able to consume it, and this directory is where that consumption is recorded.

## Layout

```
literature/
└── author-year-slug/
    └── README.md        the citation and its claims
```

**A sibling of `inquiries/` and `conjectures/`, never a child of either.** One Source may steer
several Conjectures, for the reason [#164](https://github.com/NGL321/mosaic/issues/164) gives one
level up: *an axiom is not owned by the system that bought it*. Nesting would force a second
Conjecture citing the same paper to import it again, and the programme would then hold two
readings of one paper with no tiebreaker.

**Named for the citation, not by a counter.** `inquiries/` and `conjectures/` take their `NNN`
from an issue number because the tracker is the only allocator two concurrent sessions can both
see. A Source has no issue — it has no dispatch state, because nothing runs — and it needs no
allocator either: `author-year-slug` is content-addressed by the thing itself, which is a better
name than a counter for an object that already has an identity in the world.

## External evidence steers; it never legs

**A Source can never be confirmatory, by construction rather than by policy.**
[#56](https://github.com/NGL321/mosaic/issues/56) derives **Register** from ancestry — a result
is confirmatory exactly when its metric and decision rule are git ancestors of the data they
judge — and Mosaic has no ancestry over someone else's data. Under
[#61](https://github.com/NGL321/mosaic/issues/61)'s split that confines every claim here to the
**steering fragment**, which is what `continue`/`return`/`retire` reasons over. It may never
enter the **eligibility fragment**, so no derivation offered as a **leg** may draw on it.
Citation buys no warrant.

**Warrant is generated, never received.** The route from a Source to a leg is **reproduction**,
and reproducing is an Inquiry with its own freeze and its own ancestry. This is the third site of
one principle — premise 3's exploratory→confirmatory route, and
[#9](https://github.com/NGL321/mosaic/issues/9)'s release trigger 2, which regenerates a bundle
from scratch and *"turns release into a reproduction check."*

**What a Source actually buys is search, not warrant.** A paper naming a working instrument
collapses `Searching` to near-zero, and the Inquiry pays only for the freeze and the
measurement. That saving needs nothing in this directory: instrumentation is agnostic to its
source, which is the whole point of searching for one, and the **Adequacy Criterion** judges an
instrument blind to where it came from — enforced by [#60](https://github.com/NGL321/mosaic/issues/60)'s
disjoint namespaces on a charter frozen at open. An instrument found in a paper leaves a citation
on the Run manifest and nothing more. **This directory exists only for a claim used as a
premise**, which is the rarer case and the one that carries risk.

## What a Source holds

```markdown
## Citation
    the full bibliographic record, its DOI, and the fixed version it names
    the retrieval route, by URL and status

## Claims
    ### claim-N
    **Quoted**    verbatim, with a page, section or equation locator
    **Rendered**  the axiom, in this repository's own vocabulary

## Corroboration
    independent sources found to support or contradict — append-only

## Reproduction
    Inquiry #N — corroborated / refuted — append-only
```

**The version is load-bearing, not bibliographic manners.** The freeze below rests on the
literature being immutable, and that is only true of a *named* version: an arXiv posting's
`v2`, a DOI, an edition. A Source pointing at "the paper" points at something that can change
underneath it.

**The retrieval route is not bookkeeping.** The map's standing retrieval rule requires every
route logged by URL and status, and forbids accepting a re-typeset upload as a primary source.
A Source with no route recorded is one nobody can re-check.

### Quoted and Rendered, always both

A verbatim quotation is faithful and re-checkable but is not usable as a premise in a
Conjecture's formal system. A rendering in this repository's vocabulary is usable but inserts a
translation step nobody has checked — and that translation is exactly where a plausible
misreading hides, several inferential steps back from anything Noah is asked to sign. Both are
kept, side by side, and the reading debt discharges **against the pair**: what Noah checks when
he reads the paper is whether `Rendered` follows from `Quoted`, and whether `Quoted` is really
there.

Each half answers a failure the other cannot. **Without `Quoted`**, the programme cannot state
its own influences precisely, cannot catch itself misquoting, and any later reinterpretation
means re-reading a whole corpus most of which is no longer relevant. **Without `Rendered`**, the
claim stays framed as its authors framed it — the **earth mover's distance** case, where optimal
transport was posed as a construction-foreman's problem and stayed largely invisible until
somebody separated it from that context.

### Frozen, in the strong sense

**Claims are frozen at admission; `Corroboration` and `Reproduction` are append-only.** A claim's
`Quoted` and `Rendered` text is immutable once admitted, because a claim that could be rewritten
after seeing where the search went is [#63](https://github.com/NGL321/mosaic/issues/63)'s register
hazard one level over. Admitting a further claim from the same paper is an append, not an edit.

The literature itself cannot change — the Citation names a fixed version — so the only thing that
could ever move is **how a passage was interpreted**, and interpretation moving does not correct a
claim:

> **A poor extraction is not fixed. It becomes another claim.**

Superseding, never editing, which is [#61](https://github.com/NGL321/mosaic/issues/61)'s
*axioms immutable, append-only, never retracted* holding at the level of the file.

## Reproduction produces a new node

A reproduced claim is **new work**, so it is a new node with its own **Register**, and the Source
merely gains a link. Nothing is promoted in place. That is forced rather than chosen — no commit
ordering can make Mosaic an ancestor of someone else's data — and it is also the only shape in
which the record shows that Mosaic **checked rather than trusted**. A node quietly acquiring a leg
would erase exactly that distinction.

**A refutation invalidates the result, not the literature.** Nothing is retracted here: the
refuting result is admitted as a superseding axiom, and the Source records the attempt in both
directions. The literature continues to exist and simply happens to be wrong from this
programme's perspective; whether it is wrong from its own is not this programme's question. That
a reproduction failed is a research output in its own right — the field's reproducibility record
is [#4](https://github.com/NGL321/mosaic/issues/4)'s stated reason for demanding artefact release.

The asymmetry is deliberate: a **successful** reproduction produces a confirmatory axiom that may
enter the eligibility fragment, while a **failed** one produces a result about the literature,
which steers and never legs. You cannot refute someone else's claim into your own Protective Belt.

## The Provenance Tier is derived, never stored

A claim here was not *reached* by Mosaic at all, so the claim carries no tier. What is Mosaic's is
the **reading** — *this paper says X* — and that is an assertion of ours, machine-produced until
Noah has read the paper. It is the case [`CONTEXT.md`](../CONTEXT.md) § Provenance of this section
already handles, where the badge attaches to the `_After_` lines and not to the definitions.

**An open reading debt *is* T3; discharging it is the promotion.** The two are one fact, and
storing both invites them to disagree with no tiebreaker. This is the fourth site of the same
move — Register derived and stored nowhere ([#56](https://github.com/NGL321/mosaic/issues/56),
[#63](https://github.com/NGL321/mosaic/issues/63)), the freeze as the appearance of a file
([#60](https://github.com/NGL321/mosaic/issues/60)), the environment gate at publish
([#64](https://github.com/NGL321/mosaic/issues/64)) — and it is enough of a pattern to state as
the house style it has become:

> **Record the act; derive the label.**

An act is roughly irrefutable, because the evidence that it happened is the record of it. A
derivation is deterministic, and therefore checkable by anyone who disagrees. Neither is a claim
anybody has to be trusted about, which is what an openly LLM-accelerated programme needs its
foundations to be.

<!-- The debt this opens is a *sourcing* debt — dischargeable by an agent, by search — and not
     Verification Debt, which is discharged by Noah learning. The two were filed under one label
     until #167 surveyed the ledger; the four-way split, its CONTEXT.md entry and the re-labelling
     of the existing issues are the founding-charter map's. -->

## The growth surface needs no gate

Agents can import faster than anyone can read, and nothing here stops them — deliberately.
**An import can never close the open gap**, because the gap closes only on eligibility-fragment
progress and everything here is steering-only. So importing at volume burns a Conjecture's token
allocation while moving the gap by exactly zero, which is
[#61](https://github.com/NGL321/mosaic/issues/61)'s definition of **degenerating**, and fires a
**return**. The flood is self-punishing and already visible; a dedicated cap would be a threshold,
which [#9](https://github.com/NGL321/mosaic/issues/9) refuses outright. Revisitable if the
argument turns out not to hold in practice.

Nothing here reaches Noah's acknowledgement queue, either. Premise 13's line holds: backpressure
applies to obligations that block a **result** from being real, never to obligations that block
Noah from being expert.

## What is not here

**Instruments.** See above — an instrument's provenance is inadmissible to the Adequacy Criterion
by design, so a paper that supplies one leaves a citation on the Run manifest and no Source.

**External datasets.** A dataset is an **input an Inquiry runs over**, not a claim: it has no
truth-value, and giving it a record in a shelf built for things that have one would confuse the
two. Its declared placement constraint is the Inquiry charter's field under the research loop
map's premise 7, and the DUA-class policy behind that is the founding-charter map's.

**External theorems.** Not reproduced but *checked*, which is
[#163](https://github.com/NGL321/mosaic/issues/163)'s territory and deliberately deferred.

## Nothing here yet

Deliberately. A Source is admitted by an Inquiry or a literature-research task that needs the
claim, and neither exists yet — [#7](https://github.com/NGL321/mosaic/issues/7) has not named the
first Protective Belt claim and no Conjecture has been posted. Seeding a plausible Source here
would import a claim nothing is steering by, which is the growth surface above with none of the
budget that punishes it.

One live case is already waiting: [#144](https://github.com/NGL321/mosaic/issues/144) records the
Krakauer identity `A* − A = NTIC` as *unreproduced*, which is a Source and a reproduction Inquiry
misfiled as a debt item. It is named in the re-labelling handed to the founding-charter map.
