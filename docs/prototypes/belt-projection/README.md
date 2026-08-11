# PROTOTYPE — the Protective Belt graph as a projection

Ticket [#90](https://github.com/NGL321/mosaic/issues/90). Built to be thrown away, and
retained in-tree as a **primary source** for how the store was chosen — not as a tool.
Nothing regenerates from it and nothing depends on it.

```console
python docs/prototypes/belt-projection/prototype_tui.py
```

## Why there is a second prototype

The first one is on `prototype/90-belt-graph` and was built on 2026-08-01. It is still
the primary source for the *store* question — it built the graph three ways and found
that [#5](https://github.com/NGL321/mosaic/issues/5)'s *the ledger is the issue tracker*
does not carry to a graph. But it predates the vocabulary it would now have to be checked
against: [#164](https://github.com/NGL321/mosaic/issues/164) and
[#60](https://github.com/NGL321/mosaic/issues/60) landed `conjectures/` and `inquiries/`
on 2026-08-11, and `PROTOCOL` §5 pinned the Belt to `CHARTER.md` on 2026-08-01, hours
after that branch was cut. Its `belt/nodes/` + `belt/legs/` proposal is against paths that
no longer make sense.

This one tests what the grilling on #90 actually decided.

## The claim under test

**The belt graph has no store of its own.** It is a projection over three trees that
already exist, plus exactly one record none of them can derive:

| | Holds | Decided by |
|---|---|---|
| `conjectures/NNN-slug/README.md` | the nodes | [#164](https://github.com/NGL321/mosaic/issues/164) |
| `inquiries/NNN-slug/README.md` | the edges, and everything a leg is made of | [#60](https://github.com/NGL321/mosaic/issues/60) |
| `CHARTER.md` | the admitted rungs | `PROTOCOL` §5 |
| **`inquiries/NNN-slug/axiom.md`** | **the axiom's life — carried, hazarded late, retracted** | **this ticket** |

`fixture/` is shaped exactly like the real trees, so the projection is parsing the real
formats rather than a convenient stand-in.

## What it found

### 1. The three structural claims hold, and one line does the work

Event `[1]` appends a single `retracted` line to `inquiries/172/axiom.md`. Inquiry 172
serves **two** conjectures, so that one line kills two legs at once — and 043 stays
standing on Inquiry 178's leg while 051, which had nothing else, falls to `dead`.

[#9](https://github.com/NGL321/mosaic/issues/9)'s per-leg demotion is therefore preserved
*without being stored*: it falls out of the computation. Nothing is written three times
and nothing can disagree.

The MAJOR (`[m]`) empties `CHARTER.md` and changes **not one ledger line**. Every leg is
retained, which is the property that makes a rebuild a re-validation rather than a re-run.

### 2. The cascade stopping at the projection is visible, not theoretical

Between `[1]` and `[2]` there is a real interval in which 051's **rung stands with zero
live legs**. That is the intended behaviour — a rung is only retired by Noah's commit to
`CHARTER.md` — and the projection displays it rather than hiding it. An agent's retraction
can never move the Belt; it can only stop the graph from claiming support that is gone.

### 3. The five readings have no declared **polarity**, and that is not a weighting problem

`inert_share` and `hazarded_leg_share` are *bad when high*. `predictive_to_connective` is
*good when high*. The flat mean adds them with the same sign, so the run above reports
`inert_share +1.00` — every admitted rung inert — as maximally healthy.

[#88](https://github.com/NGL321/mosaic/issues/88) has to declare a direction per reading
**before** the weighting question arises. A weighted mean over readings whose sign is
undeclared is wrong more quietly than a flat one.

### 4. The empty-belt pathology is far worse than the first prototype reported

The first prototype found a MAJOR moving the index **-0.31 → -0.18**. Under the projection
it moves **+0.33 → +1.00**: the maximum. Emptying the Belt does not merely flatter the
programme, it reports a *perfect* one.

The mechanism is sharper than "a flat mean over present readings". Two readings are
**structurally unreachable** (below), and two more lose their denominators when the Belt
empties — so the index is computed over **one** surviving reading and converges to
whatever that reading happens to say. Any formula that averages over *whichever readings
happen to be available* has this failure; the fix has to be in what the index does when a
reading is missing, not in how the present ones are weighted.

### 5. Unreachable must not read as silence

`Reading` is deliberately three-valued: a number, **no reading** (an empty denominator —
honest silence about a real question), and **unreachable** (the question cannot be computed
off the store at all, naming the ticket that owes the mechanism). Two of the five are
unreachable today:

- **`bridged_over_posted`** — and it is not merely unbuilt, it is *ill-defined* as the
  first prototype computed it. That one walked support edges to the core;
  [#164](https://github.com/NGL321/mosaic/issues/164) made the whole Hard Core and whole
  admitted Belt inherited premises of **every** conjecture, so the walk now returns true
  for everything. It has to be re-derived off the **open gap**, which
  [#165](https://github.com/NGL321/mosaic/issues/165) owns and has not built.
- **`release_shape`** — needs each MINOR matched to the `evidence:` PATCHes underneath it,
  and `PROTOCOL` §5 states plainly that there is no declared way for an `evidence:` commit
  to name the rung it bears on ([#82](https://github.com/NGL321/mosaic/issues/82)).

Collapsing these into "no reading" would make a missing instrument look like a quiet
programme.

### 6. `axiom.md` needed no fields beyond three event kinds

`carried`, `hazard`, `retracted`. Everything else a leg has — its axiom text, its domain,
its declared untestable hazards — is already in the charter frozen beside it and is read,
never copied. The ledger holds only what cannot be derived, which is the test it had to
pass to justify existing at all.

## What it does not settle

- **Condition is [#62](https://github.com/NGL321/mosaic/issues/62)'s.** The projection
  derives it (rung → belt, live leg → eligible, else conjecture). That is a proposal to
  #62, not a ruling.
- **Derivation legs have a `LegKind` and no source.** Proof bridging is
  [#163](https://github.com/NGL321/mosaic/issues/163), deferred; nothing produces one yet,
  and the projection would need a second ledger shape when something does.
- **`inert_share`'s definition is a placeholder** — a rung is inert here if no live
  conjecture's leg comes from an Inquiry that also serves it. The real definition is #88's.
- **The chart is a shape, not a series.** There are no tags in the repository yet, so
  `chart()` demonstrates the rebuilt-from-scratch form and plots nothing real.

## One requirement this places elsewhere

`fixture/CHARTER.md` carries `from_conjecture` and `relevance` on every rung, and the
projection does not work without them: reading 1 is predictive-to-connective, and
relevance is set at admission. That is a requirement on
[#12](https://github.com/NGL321/mosaic/issues/12), filed rather than decided here.
