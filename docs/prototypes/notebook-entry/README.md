# PROTOTYPE — how a Lab Notebook entry is generated and annotated

Ticket [#11](https://github.com/NGL321/mosaic/issues/11). Built to be thrown away, and retained
in-tree as a **primary source** for how the format was chosen — not as a tool. Nothing
regenerates from it and nothing depends on it.

```console
python docs/prototypes/notebook-entry/prototype_tui.py
```

## The question

`notebook/README.md` held no format when this was built, because writing one before the
mechanism existed would be the revision that directory was created to avoid. So this
prototype
generates **one real entry from one real session** — Transcript Archive session
`f0900d60…`, the night §5 custody was decided (2026-07-29T23:16Z → 2026-07-30T03:35Z,
505 events, 8 prompts) — and renders it four ways, so the format is chosen by reacting to
an entry rather than to a description of one.

The entry is real in both halves: the mechanical spine is read live out of `git log` and
`gh`, and the narrative lines were written by reading that transcript. The sample
annotations are **verbatim excerpts from Noah's own prompts in that session** — used so the
annotation layer can be seen rendered without anyone inventing words for him.

## What the prototype proposes

### Triggers — and the one that is deliberately absent

| Trigger | Fires on | Kind of line it produces |
|---|---|---|
| **merge** | a merge commit reaching `main` | what landed, at the commit type's bump level |
| **task** | a pull request closing **without** merging | a direction abandoned |
| **milestone** | `debt:discharged`, a tier promotion, a charter criterion met | Curriculum movement |

**A session ending is not a trigger.** The ticket lists working sessions as a source, and
that is where the reasoning comes from — but a session is not a unit of work. It spans
branches, it abandons things, it stops for dinner. If sessions triggered entries, the
notebook's volume would track how often Noah opens a terminal, which is precisely the
machine-exhaust failure. Sessions are **cited**, never announced.

The unit is **the day**, not the session or the commit: one file per day, **regenerated in
full** on each trigger. Not appended to — rule 3 below orders reversals ahead of wins across
the whole entry, which an append cannot express without moving lines that may already be
annotated.

### Volume — four mechanisms, because one is not enough

1. **No citation, no line.** `admissible()` drops any generated line that cannot name a
   commit, PR, issue or document. The generator *cannot* narrate, because narration has
   nothing to point at. One line was dropped by this rule in the real entry, and it was the
   right one to lose.
2. **Prose is for *why*; the ledger is for *what*.** Anything mechanically restated from
   the history (`Note.spine`) never reaches prose — it collapses into a `<details>` table.
   This rule exists because the first render of this prototype was **14 commit-subject
   restatements above the two sentences worth reading**, which is the failure mode arriving
   on schedule, in the artifact meant to test for it.
3. **A hard word budget** — 320 words of prose, enforced rather than advised. What runs over
   joins the same collapsed ledger; nothing is silently dropped. Reversals and dead ends are
   ordered *ahead* of what landed, so a squeezed entry loses a win rather than a mistake.
4. **Most days get no entry at all.** `should_emit()` returns false when nothing but churn
   survives selection. Silence is the default.

The measured effect, on the real entry — counted with this prototype's own `prose_only()`
and `words()` over the renderings committed in [`out/`](out/), with the annotation layer
fixed at 136 words throughout:

| | words | reading | Noah's share |
|---|---|---|---|
| D — raw generated, no rules | 1128 | ~4m 30s | 12% |
| A — inline, `full` | 955 | ~3m 50s | 14% |
| B — annotation-first, `full` | 953 | ~3m 50s | 14% |
| B — annotation-first, `decisions` | 560 | **~2m 15s** | **24%** |

**Read the third and fourth rows against the second, not the first.** A and B at the same
volume differ by *two words*: the rendering choice is invisible to a word count, and the
whole measured effect belongs to the volume dial. Noah's share moves only because the
denominator shrinks — the numerator is the same 136 words in every row.

An earlier version of this table compared A at `full` against B at `decisions` and read the
difference as evidence for B. That was a confounded comparison and review caught it. **The
numbers argue for the rules, not for the rendering.** B's case is the prose one two sections
down, and it needs no numbers: an unannotated entry under B admits that it is unannotated,
and under A it looks finished.

D is the control — what the notebook becomes if nobody annotates and nothing is budgeted.

> These counts are pinned to the committed `out/` files. `harvest.py` reads live
> `git log --all`, so regenerating on a repository that has moved will produce a different
> day and different numbers. Re-measure from `out/` rather than trusting the table against
> a fresh run.

### Generated versus annotated

Annotations are a **separate layer keyed to a line's anchor** — its primary citation plus
an ordinal, never its position, and never edits to generated text.
That is what makes the distinction mechanical rather than a habit, and it is the one
structural claim here worth keeping whichever rendering wins.

| | Rendering | Generated content | Noah's content |
|---|---|---|---|
| **A** | inline blockquote | plain bullets | `> **Noah —**` under the line it answers |
| **B** | annotation-first | collapsed in `<details>` | **plain prose, and the whole visible page** |
| **C** | ledger table | table rows, `◆` where annotated | its own `## Noah's notes` section |
| **D** | raw (control) | everything | *none* |

**B was chosen.** It inverts the emphasis: what a reader meets is Noah's
reading of the day, and the generated record is one click away. It is also the only variant
where an unannotated entry looks visibly unfinished — it says *"Unannotated. Nothing here has
been read back."* — which turns the annotation debt into something a stranger can see.

A's blockquotes are the most conventional and the most legible line-by-line; C reads like a
changelog, which `CONTEXT.md` explicitly tells the notebook not to be.

### Citing a private archive

The entry cites `sha256:6c69d0f604dd…`, the content hash of the transcript, in a Sessions
table with the window, size and branch — per [#3](https://github.com/NGL321/mosaic/issues/3)
§2, with the `Index` manifest resolving hash → Drive path. No public URL, nothing about the
archive's shape, and reorganising the archive never breaks the reference.

`harvest.py` reads the transcript's **content** for exactly one purpose — scanning for
anything that looks like a secret at the boundary where public output is generated — and its
*structure* for windows, segments and the hash.

The scrub **fails closed**: a candidate secret raises `ScrubBlocked` and no entry is
produced, for the whole file rather than the requested day — a transcript is one artifact
and a partial scrub is not a scrub. #3 §3.2 is a prohibition, not a reporting requirement,
and counting without blocking would publish the secret and note underneath that it had.
Nothing is on the page, because an entry that would carry a count is an entry that was never
emitted.

**Two places the prototype is narrower than the record, both deliberate.** It scans only the
*transcript*, whose content never reaches the page; `notebook/README.md` requires the
generator to scan **the emitted text** as well, which is the actual public boundary — commit
subjects, issue titles, narrative lines and annotations. And the patterns here will fire on
ordinary content (a JSON field named `secret`, a pasted config), which under a blocking rule
needs a way out; the record answers that with a hand-written, per-line, auditable
acknowledgement rather than a quieter scanner, because a control that cannot be satisfied
gets switched off.

### Provenance Tiers in an entry

A badge per line, `⟦T3⟧` / `⟦T3 · #40⟧`, the debt issue named when one exists — the spelling
`curriculum/README.md` already fixed. The tier belongs to **the line**, not to the work it
describes:

- **T3** — everything generated, harvested facts included. *Verifiable is not verified*:
  `curriculum/README.md` rejects a tier for machine-produced-but-checkable content, and
  review caught this file claiming T2 for harvested lines. Corrected.
- **T1** — Noah's annotations, by construction.

So a fresh entry is a page of T3 with a T1 layer accreting on top, and the badges make the
generated/annotated split legible even in raw Markdown, where the visual distinction is
otherwise a rendering trick.

## How to drive it

`[1]`–`[4]` switch rendering, `[d]` turns the volume dial, `[+]`/`[-]` move the budget in
80-word steps, `[s]` and `[x]` add and drop the sample annotation layer, `[n]`/`[p]` move
focus and `[a]` annotates the focused line in your own words, in memory. `[w]` writes the
current rendering to `out/` — the only thing this touches on disk, and the way to see how
GitHub renders it.

Two things are worth doing deliberately:

- Press `[x]` on variant **B**, then on variant **A**. B admits it is unannotated; A looks
  finished. That difference is the whole choice between them.
- Turn the budget down to 80 with `[-]` and watch what survives. The lines that hold on are
  the reversal and the two dead ends, which is rule 3 working as intended.

## Findings from building it

1. **The mechanically generated half is nearly worthless as prose.** Every commit-subject
   line is already in `git log`, better. The generator's value is entirely in the narrative
   pass and in the *selection* — deciding what not to say. This is the finding that reshaped
   the model mid-build.
2. **The dead ends are the only lines a reader could not reconstruct.** Nothing outside the
   transcript records that the three custody readings were driven to failure before a fourth
   was drafted, or that the first CI check convicted correctly cited commits. If the notebook
   carries anything, it is these.
3. **Annotation is a debt, and it should be visible as one.** A generated entry is a page of
   T3 claims; if nobody annotates it, the notebook is a machine reciting the programme back
   to itself. `annotated lines n/m` is on screen for that reason, and B renders the deficit
   rather than hiding it.

## Settled — Noah, 2026-07-30, after driving this

> The settled format lives in [`../../../notebook/README.md`](../../../notebook/README.md),
> which is the record. This section is why it says what it says. Two of the rulings below
> were revised in review after they were made — the day-ownership *justification* in (2),
> and the tier reading corrected above — and this file carries the revised versions, not
> the versions as first written.

1. **Nothing in the notebook promotes a Provenance Tier.** Annotating a line does not lift
   it: the annotation is a T1 claim sitting beside a T3 one, and the T3 line stays T3.
   Promotion requires Noah restating the thing himself, which is the gate the tiers exist to
   impose — most generated content lives at T3 until it is bumped, and T1 is his thinking.
   *So the notebook reports tiers and never issues them.*
2. **A session ends after an hour without work, and belongs to the day it ended.** Only one
   day can own it, and the end is the side the *generator* is standing on: an entry is
   written when the segment closes, so the owning day is the day whose entry is being
   generated at that moment. Dating by the start would reopen — and regenerate — a day
   already annotated and already read, every time a session crossed midnight.
3. **The narrative pass runs on Google Apps Script**, not the Pi 5 — source in this repo,
   execution on Google's infrastructure with direct Drive access, so failure requires Google
   failing. The Pi is data-sovereignty backup and moves house.
4. **Annotations are not canonical.** Anything worth making canon earns its own entry and
   its own work — a tier promotion for the idea, not a louder note. Regeneration is
   therefore permitted; `reanchor()` re-applies the layer by anchor and **reports orphans
   rather than dropping them**, because not canonical is not the same as disposable.
5. **Rendering B is the format.** *"This is my research project. It just happens to be
   AI-accelerated. Tool output shouldn't be the first thing anyone sees."* A, C and D stay in
   the code as the comparison that produced the choice.

### What (2) turned out to mean

The idle rule is not cosmetic, and this is the prototype earning its keep: **a transcript
file is not a session.** `b1243c96` splits into four segments across two days, one of them
straddling midnight; the entry's own source file splits into two, both landing on the 29th.

So a file's hash cannot cite a day's work on its own, and the Sessions table now carries
**hash plus window plus segment count** — the hash identifies the file, the window says
which part of it this day owns. Windows are printed in local time, because a UTC window
under a locally-dated heading contradicts itself on the page: this entry's session would
read as ending on the 30th beneath a heading dated the 29th.

### What (3) changes about the tool contract

Apps Script is V8, not Python, and cannot run `git` or `gh` — so the harvest half moves to
the GitHub REST API over `UrlFetchApp`, and the four-line contract (#3 §6) reads: **reads**
Drive archive + GitHub API; **writes** a notebook entry by API commit; **auth** Drive OAuth
plus a token in Script Properties, never in source; **safe to regenerate from scratch?**
yes for the generated record, and per (4) that is now the whole answer, with orphaned
annotations reported.

## Still open

- **Which repository does the generator commit through, and as whom?** §5's identity
  obligation applies: notebook entries are record files and agent-writable, but the Apps
  Script identity still has to be a named one.

## Checks

```console
python docs/prototypes/notebook-entry/checks.py
```

**A prototype should not have tests, and this one does** — the rule is right for a
throwaway, and this stopped being one when it landed in-tree as the cited source and its
model became the spec the Apps Script generator will be written against.

Four defects were found here by driving the TUI by hand: positional anchors that silently
re-attributed an annotation, anchors colliding across layers, the budget suppressing an
annotation into a fold, and `select()` disagreeing with `reanchor()` about what is
annotatable. Each is now an assert. They cost thirty lines and they are the difference
between the next reader finding out in a second and finding out by reading a rendering
closely enough to notice Noah's words are missing.

## Not in scope

No persistence beyond `out/`, no CI, no scheduling, nothing written to `notebook/`. The
prototype does not decide the format — it makes four candidate formats disagree out loud
over one real day of work.
