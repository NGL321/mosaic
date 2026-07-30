# Lab Notebook

The public, dated audit trail of the programme's process — in effect a rich commit history.
Entries are largely generated, then annotated by Noah, and carry the mistakes and abandoned
directions deliberately.

Distinct from `docs/research/`, which is the **evidence** layer: a research document is a
piece of work, a notebook entry is the narrative of work happening. An entry may cite a
research document; they are not the same artifact.

## Layout

`YYYY-MM-DD-short-slug.md`, one file per entry, flat. Dates are the entry's date, not the
date of whatever it describes.

## What an entry is for

**Annotation comes first, on the page and in the argument.** A reader meets Noah's reading
of the day in plain prose; the generated record sits beneath it, folded away, one click
from anyone who wants it. This is a research programme that happens to be LLM-accelerated,
and tool output is not the first thing anyone should see.

The entry's value is what a reader **could not reconstruct** from `git log` and the issue
tracker: why something was reversed, what direction was abandoned, and what the programme
now believes it got wrong. Everything else is spine, and the spine belongs in a fold.

## Format

Settled by [#11](https://github.com/NGL321/mosaic/issues/11).

```markdown
<!-- GENERATED from the Transcript Archive and this repository's history. -->

# 2026-07-29 — custody stops claiming attendance, and 1.0.0 becomes computed

Noah's lede, in plain prose. Then one paragraph per annotated line, each carrying a
subscript pointing at the generated line it answers.

<details><summary>Generated record — 9 line(s), 303 words</summary>

- One generated line per decision, each citing its artifacts, each badged ⟦T3⟧.

</details>

<details><summary>Ledger — 15 line(s) the history already carries</summary>

| kind | what | where |

</details>

## Sessions

| session | window | segment | size | branch |

<sub>tier legend</sub>
```

**Generated and annotated content are separate layers, not two styles of prose.** An
annotation is keyed to the id of the line it answers and is *never an edit to generated
text*. That is what makes the distinction mechanical rather than a habit someone has to
keep: everything at the top level of the page is Noah's, and everything the machine wrote
is behind a fold or inside a table.

An entry with no annotations says so — *"Unannotated. The generated record is below;
nothing here has been read back."* The deficit is on the page where a stranger can see it,
which is the point of choosing this shape over an inline-comment one that looks finished
either way.

## What triggers an entry

| Trigger | Fires on |
|---|---|
| **merge** | a merge commit reaching `main` |
| **task** | an agent pull request closing or merging |
| **milestone** | `debt:discharged`, a tier promotion, a charter criterion met |

**A session ending is not a trigger, deliberately.** A session is not a unit of work — it
spans branches, abandons things, and stops for dinner. If sessions triggered entries, the
notebook's volume would track how often Noah opens a terminal, which is the failure mode
this format exists to prevent. Sessions are **cited**, never announced.

The unit is **the day**: one file, appended to as that day's triggers fire.

## Keeping the volume down

The failure mode is a log so complete that nobody reads it, including Noah, and that reads
externally as machine exhaust rather than thinking. Four rules, because no one of them is
sufficient:

1. **No citation, no line.** A generated line that cannot name a commit, PR, issue or
   document is dropped. The generator cannot narrate, because narration has nothing to
   point at.
2. **Prose is for *why*; the ledger is for *what*.** Anything mechanically restated from
   the history collapses into a table. `git log` already carries it, better.
3. **A hard budget** — 320 words of prose per entry, enforced rather than advised. What
   runs over joins the ledger; nothing is silently dropped. Reversals and dead ends are
   ordered *ahead* of what landed, so a squeezed entry loses a win rather than a mistake.
4. **Most days get no entry.** When nothing but churn survives selection, the generator
   emits nothing. Silence is the default.

## Citing the Transcript Archive

The archive is private ([#3](https://github.com/NGL321/mosaic/issues/3)), so an entry cites
a session it cannot link to: **`sha256` of the transcript, plus the window, plus which
segments of the file the day owns.** The `Index` manifest resolves hash → Drive path.

**A session is a segment of a transcript file, not the file.** It ends after an hour
without work, and it belongs to the local day it **ended** on — only one day can own it,
and the end is the side that is actually defined. One file therefore feeds more than one
entry: a real transcript in the archive splits into four segments across two days, one of
them straddling midnight. The hash alone would cite all of it, which is why the window is
part of the citation and not decoration.

Windows are printed in local time. A UTC window beneath a locally-dated heading contradicts
itself on the page.

The generator reads a transcript's text for exactly one purpose besides the narrative pass:
counting anything that looks like a secret, at the boundary where public output is produced
(#3 §3.2). The count is reported in the entry when it is non-zero.

## Provenance Tiers in an entry

A badge per line — `⟦T2⟧`, `⟦T3 · #40⟧` with the debt issue named, as
[`../curriculum/README.md`](../curriculum/README.md) spells it. The tier belongs to **the
line**, not to the work it describes:

- **T2** — mechanically harvested, verifiable from the artifact it cites.
- **T3** — a narrative claim about *why*; machine-produced and unverified.
- **T1** — Noah's annotations, by construction.

**The notebook never promotes a tier.** Annotating a T3 line does not lift it: the
annotation is a T1 claim sitting beside a T3 one. Promotion requires Noah restating the
thing himself, which is the gate the tiers exist to impose. The notebook reports tiers; it
does not issue them.

## Annotations are not canonical

Anything worth making canon earns its own entry and its own work — which is a tier
promotion for the idea, not a louder note. An annotation is commentary for the record.

Two consequences:

- **Regeneration is permitted.** The generated record is reproducible from the transcript
  and the history; the file is not frozen the moment it is annotated.
- **Orphans are reported, never dropped.** Re-applying an annotation layer to a regenerated
  entry matches by anchor; an annotation whose line no longer exists is surfaced. Not
  canonical is not the same as disposable.

## Not built yet

The generator itself. It will run as **Google Apps Script** — source in this repository,
execution on Google's infrastructure with direct Drive access to the archive, so a failure
requires Google to fail. That rules out `git` and `gh` at generation time: the harvest half
goes through the GitHub REST API. Its four-line contract (#3 §6) and the identity it
commits under are open.

Until then, this file is the format and there are no entries. The first one should be
produced by the generator rather than written by hand, so that the mechanism is exercised
rather than retrofitted.

## Where this was decided

The format was chosen by generating a real entry from a real session and reacting to it,
rather than by writing a specification. That prototype — four candidate renderings of the
same day, with the measured word counts that decided between them — is kept as a primary
source on the throwaway branch
[`prototype/notebook-entry`](https://github.com/NGL321/mosaic/tree/prototype/notebook-entry/docs/prototypes/notebook-entry).
