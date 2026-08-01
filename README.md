# Mosaic

A long-running research programme in computational cognitive science, conducted openly
with LLM acceleration.

Mosaic studies cognition as a heterogeneous network of inference engines whose schemas
each carry their own metric space, and the transport between them — of which the primary
observable is where transport **fails**. The resolved vocabulary for that sentence lives
in [`CONTEXT.md`](CONTEXT.md); every term there names its source, and marks where
Mosaic's usage departs from it.

The programme is framed on Lakatos: a **Hard Core** that is not revised, a **Protective
Belt** of falsifiable claims that is, and a **Positive Heuristic** governing how belt
rungs are added and retired. Work is planned and decided in the issue tracker, indexed
from the [wayfinder map](https://github.com/NGL321/mosaic/issues/1).

---

## Where the human is

Mosaic is machine-accelerated and says so. The obvious objection — *how much of this did
the researcher actually do?* — is answered structurally rather than by assertion, so that
it can be checked rather than believed.

**Two rules, in [`PROTOCOL.md`](PROTOCOL.md):**

**Custody.** Agents write the record; the human writes the beliefs. Research documents,
notebook entries, and experiment output are agent-writable. `CONTEXT.md` and the charter
are human-only — agents propose exact text, the human applies it. So:

```console
git log --format='%an' -- CONTEXT.md   →  one name
```

**Warrant.** Evidence lands freely, carrying its provenance tier. But a claim entering the
Protective Belt requires the researcher to write **its falsifier, in their own words**, and
a revision to the Hard Core requires a **public, human-authored work product**. Those
drafts are grilled on the pull request by an agent that did not produce the work. Failing
that gate does not reject the merge — it starts a teach cycle, and the fact that it fired
is recorded.

Custody without warrant is transcription. Warrant without custody is a signature on
someone else's page. The pair is the claim.

---

## Reading the version

Two independently versioned tracks, tagged `research-v*` and `tooling-v*`.

On the research track, the number is Lakatosian rather than sized by effort:

- **MAJOR** — the Hard Core changed. This is an admission that the programme was
  refounded. `0.x` is pre-charter.
- **MINOR** — a Protective Belt rung was added, retired, or falsified.
- **PATCH** — the record accreted: evidence, vocabulary, corrections.

Bump and diff size are deliberately uncorrelated. A 457-line research document is a
PATCH; a two-line edit retiring a belt rung is a MINOR. The version tells you the one
thing the diff cannot: whether the programme's **commitments** moved, or its **evidence**.

Which also means the version is honest about how young this is. Mosaic currently has
language and evidence and **no belt rungs at all** — so it sits at `0.0.x`, and will until
the first falsifiable claim is named.

---

## Layout

| | |
|---|---|
| [`CONTEXT.md`](CONTEXT.md) | Resolved vocabulary. Human-authored. Read before using any of its terms. |
| [`PROTOCOL.md`](PROTOCOL.md) | Branches, commit types, custody and warrant, review, collisions. |
| [`docs/DATA-PROTOCOL.md`](docs/DATA-PROTOCOL.md) | What is stored, what is regenerated, and where run artifacts live. Drive-first. |
| `docs/research/` | Agent-produced research output. Record, not belief. |
| `.claude/skills/` | The skills that run the sessions — wayfinder, grilling, research, teach. |

Repository structure beyond this is
[not yet settled](https://github.com/NGL321/mosaic/issues/8).

---

## Licensing

Mosaic is a research record with software attached, not a software project with docs
attached, so it carries **two licences split by artifact kind** — code under MIT, the
prose record under CC BY 4.0. Take the code freely; if you carry the ideas, name where
they came from.

This table is the single place the mapping lives.

Copyright © 2026 Noah Litov. Attribute the CC BY 4.0 material to *Noah Litov, Mosaic*,
with a link back to this repository and to the licence.

| Path | Licence |
|---|---|
| `CHARTER.md`, `CONTEXT.md`, `PROTOCOL.md`, `README.md`, `CONTRIBUTING.md` | **CC BY 4.0** ([`LICENSE-DOCS`](LICENSE-DOCS)) |
| `notebook/`, `docs/`, `curriculum/` | **CC BY 4.0** ([`LICENSE-DOCS`](LICENSE-DOCS)) |
| `.claude/skills/`, `.agents/skills/` | **Third-party — neither.** Vendored from [`mattpocock/skills`](https://github.com/mattpocock/skills) per [`skills-lock.json`](skills-lock.json), under their upstream licence. |
| everything else, `experiments/` included in full | **MIT** ([`LICENSE`](LICENSE)) — the default |

`LICENSE` and `LICENSE-DOCS` are licence texts rather than licensed material: MIT's is
reproduced under its own terms, and Creative Commons dedicates its licence texts to the
public domain under CC0.

**The directory wins**, and **MIT is the default**: a file nobody has classified fails
safe toward permissive rather than into unlicensed limbo. `experiments/` is MIT in full,
prose write-ups included.

Three riders:

- **The licence follows the whole file.** A code block inside `PROTOCOL.md` is CC BY; a
  prose docstring in `tools/` is MIT. There is no sub-file licensing.
- **Generated files inherit their directory.** `curriculum/open.md` is CC BY whatever
  emitted it.
- **A new top-level file or directory is assigned a licence in the pull request that
  creates it** — the one rule here with teeth. It reaches *files* as well as directories
  because a root-level file has no directory to inherit from, so the default is all that
  catches it, and the default is wrong for prose: `CONTRIBUTING.md` is in the table above
  for exactly that reason.

Contributions are inbound = outbound: you licence each file you touch under whatever
that file's path already carries. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the
checklist and [`PROTOCOL.md` §8](PROTOCOL.md) for the reasoning.

## Citing Mosaic

[`CITATION.cff`](CITATION.cff) at the root. **A citation must pin a version** — a
`research-vX.Y.Z` tag, or a commit sha for anything predating one. `main` is the
programme's current state of belief, not its published state, so an unversioned citation
names a target designed to move.
