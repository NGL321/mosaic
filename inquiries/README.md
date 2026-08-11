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
