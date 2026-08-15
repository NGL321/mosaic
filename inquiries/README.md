# Inquiries

**Research track.** Everything under this directory fails the test in
[`PROTOCOL.md` §1](../PROTOCOL.md): if it changed silently, a result already in the record
could become wrong. Dataset generators, analysis pipelines, seed handling and schedulers all
live here and are versioned as research, despite reading as tools.

## Layout

```
inquiries/
└── NNN-short-slug/
    ├── README.md        the charter — frozen at open
    ├── axiom.md         the axiom's life — append-only
    ├── configs/         candidate instruments, tried during Searching
    ├── config.yaml      the frozen instrument; exists only after the freeze
    ├── src/
    └── runs/
        └── <date>-<run-id>.md    manifest only
```

Inquiries are numbered and named for their **Question**, not for the notebook entry that
discusses them — several entries may cite one Inquiry, and an Inquiry that only ever
served one entry is still findable a year later. `NNN` is the Inquiry's **issue number**:
agents open Inquiries themselves, so the tracker is the only allocator two concurrent
sessions can both see.

An Inquiry's `README.md` names the **Conjecture** it bridges toward — one or several, in
`conjectures/`, which is a sibling of this directory and never a parent of it — together
with a hypothesis-blind **Adequacy Criterion** and an environment requirement. An Inquiry
that cannot state an Adequacy Criterion cannot be delegated, and the refusal is itself a
finding about the Inquiry.

**The falsifier is not here.** It belongs to the Conjecture, which is what the Inquiry
serves; a Protective Belt claim is what a conjecture may *become*, several human acts
later. What the charter holds is the **decision rule** — the falsifier's local,
machine-checkable shadow over one instrument.

**Nothing in the charter is signed.** The Question is drafted by the agent that opens the
Inquiry and the Adequacy Criterion is apparatus, so the freeze is **git ancestry** rather
than a human signature; the human's hand is on the Conjecture. The budget, the stall
tolerance and the continue/return/retire rule live there too — an Inquiry declaring any of
them is writing its own cheque.

**One Inquiry, one directory, many runs.** The instruments an Inquiry searches over are
configurations committed with it, never sibling directories: the directory names the line of
investigation, not a single **Experiment**. Three levels, defined in
[`CONTEXT.md`](../CONTEXT.md) — an Inquiry is a searchable domain, an Experiment is one
instrument configured, and a **Run** executes one Experiment under one Inquiry. Only the Run
is produced rather than declared, and only the Run leaves a record: the manifest in `runs/`.

**The appearance of `config.yaml` is the freeze.** During Searching there is no such file,
only candidates under `configs/`. When one passes the Adequacy Criterion it is committed to
that path, and *that commit is the freeze event* — dated, attributable, and an ancestor of
everything measured afterwards, which is what makes the discriminating result confirmatory
without anyone having to assert that it is. Changing it afterwards is a new Inquiry, not an
amendment to this one.

**Committed here, but not owned here.** A config's nesting is where the file sits, not what
makes it what it is — an Experiment is identified by its config's sha256 and nothing else, so
a byte-identical config under another Inquiry is the same Experiment, not a copy of it.
Committing one here binds it to this Inquiry's *search*, never to this Inquiry's *identity*.

Seeds are therefore **not** in `config.yaml`. A number is hard-coded into a configuration only
if it is essential to what defines that configuration, and a seed never defines one — written
in, every seed would be a different Experiment, every Experiment would have exactly one run,
and the multi-seed object would have no name. The config declares how seeds are drawn; each
run's manifest records the value it drew, which is where the seed the repository must keep to
reproduce a run now lives.

## The axiom ledger

An Inquiry contributes **one sentence** — the charter's `axiom_if_carried` — to every
Conjecture it bridges toward. `axiom.md` records that sentence's life, and it is the one
record the Protective Belt graph cannot derive.

**The belt graph is a projection, not a store** ([#90](https://github.com/NGL321/mosaic/issues/90)).
Its nodes are `conjectures/`, its edges are the `conjectures:` list in the charter above, an
admitted rung is in `CHARTER.md`, and a **leg** is the pair (Inquiry, Conjecture) once the
axiom has carried — the leg's kind, domain, axiom text and declared untestable hazards are
all *read* from the frozen charter and never copied. Materialising the graph as a fourth
artifact would buy nothing and could disagree with the three trees that already say it, with
no tiebreaker; the discrepancy would surface as a wrong health reading rather than a failing
check.

Three event kinds, appended and never edited:

- **`carried`** — the discriminating measurement passed the frozen `decision_rule` and Noah
  acknowledged the result. This is the event that brings a leg into existence.
- **`hazard`** — an untestable hazard discovered after the freeze. The charter cannot take it,
  being frozen at open, and under [#9](https://github.com/NGL321/mosaic/issues/9) a late one
  obliges a corroboration Inquiry and retires nothing.
- **`retracted`** — the axiom no longer holds. Two routes, below.

**Retraction is written once, here — never per conjecture.** An axiom is not owned by the
system that bought it, which is why `conjectures/` is a sibling of this directory rather than
a parent; a retraction filed per-conjecture would re-introduce that ownership and store one
fact in three places. `#9`'s **per-leg demotion survives in full as a computation**: a leg is
live exactly when its axiom is live *and* the conjecture's system still proves its goal with
it, so a leg genuinely can die for one Conjecture and stand for another without either fact
being asserted anywhere.

The cost is deliberate and is the reason for the placement: reading *why a Conjecture lost a
leg* means opening the Inquiry that bought it. A lost leg is exactly the moment that warrants
Noah's own investigation, and the layout forces the trace rather than summarising it.

### The two routes

|  | Fires on | Whose hand | Defence |
|---|---|---|---|
| **Rule-dictated** | a Run of the frozen Experiment fails the frozen `decision_rule` | agent-written | `PROTOCOL` §5 discharges **by citation** — the rule, and the Run that fired it, both committed before the data existed |
| **Discretionary** | the declared hazard bit; the Adequacy Criterion turns out not to establish competence; a better instrument supersedes it | Noah's | full defence, unchanged |

Neither route waits. A rule-dictated retraction **executes immediately and files a return**.
The argument that protects conjecture retirement — *a silent retirement would leave Noah
believing what the programme has already abandoned* — does not transfer: a Conjecture is a
belief he holds, while an axiom is a fact about a measurement, and an axiom known not to
replicate but left standing means the Conjecture's formal system keeps proving things off a
premise known to be false.

**The cascade stops at the projection.** A retraction can leave an admitted rung with no live
leg, and that state is real and visible — but a rung is retired only by a commit to
`CHARTER.md` in Noah's hand, under `PROTOCOL` §5's *the Protective Belt is Noah's to decide*.
An agent's retraction can never move the Belt; it can only stop the graph from claiming
support that is gone.

Three things do **not** retract an axiom, and each is settled elsewhere: **inconsistency**
with another axiom fires a mandatory return
([#61](https://github.com/NGL321/mosaic/issues/61)) — neither sentence is wrong for
conflicting; a **stall** returns and never retires
([`conjectures/`](../conjectures/README.md)); and a **MAJOR** demotes the whole Belt while
retaining every leg in place, which is what makes the rebuild a re-validation rather than a
re-run.

## What is not stored here

**Regenerable output never enters this repository.** Under
[`docs/DATA-PROTOCOL.md` §3.3](../docs/DATA-PROTOCOL.md), adopted in
[#3](https://github.com/NGL321/mosaic/issues/3), runs publish to
`Desk/mosaic/runs/<run-id>/` (§3.4) and the repository keeps only what is needed to
reproduce them: configuration, code, and the per-run seed each manifest records.

`runs/` therefore holds **manifests, not bytes** — one small file per run, recording the
run id, the config SHA it was produced from, the seed it drew, the sha256 of the output, and
the Drive path.
The manifest is what a notebook entry cites, and it is what makes a result traceable after
the bytes have been moved or pruned.

Retention arithmetic for large sweeps — runs × checkpoints × size — is required by
[`docs/DATA-PROTOCOL.md` §3.4](../docs/DATA-PROTOCOL.md) before the first sweep and has not
been done. It cannot be, until a
first rung has an experimental design; that is tracked on the map's **Not yet specified**.

## Nothing here yet

Deliberately. The first empirical line is still open — [#17](https://github.com/NGL321/mosaic/issues/17)
reopened the choice of *phenomenon* (formation versus structure), and
[#7](https://github.com/NGL321/mosaic/issues/7) has not yet named the first Protective Belt
claim. Scaffolding a plausible `001-eca-grokking/` here would encode a decision the programme
has explicitly reopened. Nothing can be opened here before a Conjecture exists to open it
under, either — an Inquiry serving nothing is unaimed and nobody's budget pays for it.

A worked charter, written against this layout and deliberately kept out of it, is in
[`docs/prototypes/inquiry-charter/`](../docs/prototypes/inquiry-charter/) with the dispatch
gate that refuses a malformed one.
