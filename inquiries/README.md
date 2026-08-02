# Inquiries

**Research track.** Everything under this directory fails the test in
[`PROTOCOL.md` §1](../PROTOCOL.md): if it changed silently, a result already in the record
could become wrong. Dataset generators, analysis pipelines, seed handling and schedulers all
live here and are versioned as research, despite reading as tools.

## Layout

```
inquiries/
└── NNN-short-slug/
    ├── README.md        the claim this serves, and what would falsify it
    ├── config.yaml      seeds and configuration
    ├── src/
    └── runs/
        └── <date>-<run-id>.md    manifest only
```

Inquiries are numbered and named for their **Question**, not for the notebook entry that
discusses them — several entries may cite one Inquiry, and an Inquiry that only ever
served one entry is still findable a year later.

An Inquiry's `README.md` names the Protective Belt claim it serves and the observation
that would retire it. An Inquiry that cannot say what would falsify the claim it serves is
not ready to run.

**One Inquiry, one directory, many runs.** The instruments an Inquiry searches over are
configurations under it, never sibling directories: the directory names the line of
investigation, not a single experiment. That leaves `experiment` free for what it means one
level down — an instrument run inside an Inquiry's budget.

## What is not stored here

**Regenerable output never enters this repository.** Under
[`docs/DATA-PROTOCOL.md` §3.3](../docs/DATA-PROTOCOL.md), adopted in
[#3](https://github.com/NGL321/mosaic/issues/3), runs publish to
`Desk/mosaic/runs/<run-id>/` (§3.4) and the repository keeps only what is needed to
reproduce them: seeds, configuration, and code.

`runs/` therefore holds **manifests, not bytes** — one small file per run, recording the
run id, the config SHA it was produced from, the sha256 of the output, and the Drive path.
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
has explicitly reopened.
