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
# 2026-07-29 — custody stops claiming attendance, and 1.0.0 becomes computed

Noah's lede, in plain prose. Then one paragraph per annotated line, each carrying a
subscript naming the anchor of the generated line it answers.

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

**There is no `GENERATED` banner at the top of an entry**, deliberately. A file whose
thesis is that the top level is Noah's cannot open with a machine's front matter. Each
fold's `<summary>` names what is inside it, which is where the marker belongs and is the
only place it is needed: everything above the first fold is annotation.

**Generated and annotated content are separate layers, not two styles of prose.** An
annotation is attached to the **anchor** of the line it answers and is *never an edit to
generated text*. That is what makes the distinction mechanical rather than a habit someone
has to keep: everything at the top level of the page is Noah's, and everything the machine
wrote is behind a fold or inside a table.

### Anchors

**The anchor is the line's primary citation** — the first artifact it names — plus an
ordinal when one artifact yields more than one line: `a598221`, `a598221#2`, `#40`. Not a
line index, and not a hash of the generated prose.

This is forced rather than chosen. Rule 3 below reorders lines within an entry, so an index
is wrong by the second trigger of the day; and the narrative half is a model pass, so its
wording changes on every regeneration and a prose hash never survives one. Rule 1 already
guarantees every generated line names an artifact, and that identifier is stable under both
rewording and reordering.

Ledger lines take the same form under a `ledger:` namespace. Annotations never attach to
them, but without the namespace both layers mint the same anchor for the same commit, and
one annotation then answers two different lines.

A line whose citations change is a **different line**: its annotation orphans, and orphans
are reported **on the page**, not in a log — a report Noah has to go looking for is a drop
with extra steps. That is the cost of the rule and it is the right cost: an annotation
answering a claim that no longer exists should not be silently re-attached to a claim that
does.

An entry with no annotations says so — *"Unannotated. The generated record is below;
nothing here has been read back."* The deficit is on the page where a stranger can see it,
which is the point of choosing this shape over an inline-comment one that looks finished
either way.

## What triggers an entry

| Trigger | Fires on |
|---|---|
| **merge** | a merge commit reaching `main` |
| **task** | a pull request closing **without** merging |
| **milestone** | `debt:discharged`, a tier promotion, a charter criterion met |

**`task` is narrowed to abandonment on purpose.** Every merged pull request is already a
merge commit reaching `main` — §6 requires the pull request and requires `--no-ff` — so a
trigger on "closing or merging" fires twice for one artifact. Narrowing it removes the
overlap and buys the more interesting case: an abandoned pull request is exactly the
*direction abandoned* this notebook exists to carry, and it is the one thing the **merge**
trigger structurally cannot see. Triggers also dedupe per artifact per day, as a backstop.

**A session ending is not a trigger, deliberately.** A session is not a unit of work — it
spans branches, abandons things, and stops for dinner. If sessions triggered entries, the
notebook's volume would track how often Noah opens a terminal, which is the failure mode
this format exists to prevent. Sessions are **cited**, never announced.

The unit is **the day**: one file per day, **regenerated in full** on each trigger, not
appended to. Appending cannot work: rule 3 orders reversals ahead of what landed across the
whole entry, so an afternoon reversal has to be inserted above lines that were already
there — and possibly already annotated. Regeneration is what makes that legal, and it is
legal only because anchors survive reordering and annotations are not canonical. The two
rules hold each other up.

## Keeping the volume down

The failure mode is a log so complete that nobody reads it, including Noah, and that reads
externally as machine exhaust rather than thinking. Four rules, because no one of them is
sufficient:

1. **No citation, no line.** A generated line that cannot name a commit, PR, issue or
   document is dropped. The generator cannot narrate, because narration has nothing to
   point at.
2. **Prose is for *why*; the ledger is for *what*.** Anything mechanically restated from
   the history collapses into a table. `git log` already carries it, better.
3. **A hard budget** — 320 words of **generated** prose per entry, enforced rather than
   advised. What runs over joins the ledger; nothing is silently dropped. Reversals and
   dead ends are ordered *ahead* of what landed, so a squeezed entry loses a win rather
   than a mistake.

   The budget binds one layer. **Noah's annotations are unbudgeted** — the generator has no
   business truncating him, and an entry that is mostly his words is the outcome this
   format is trying to produce, not a violation. Enforcement is therefore something the
   generator does to itself: it spills its own tail into the ledger and stops.

   **An annotated line is pinned**: neither the budget nor the volume dial may demote it
   into the ledger. Otherwise a rule that binds only generated prose reaches Noah's layer
   anyway — the line folds away and his note goes with it, unrendered and unreported. An
   annotation is evidence he engaged with that line, and evidence of engagement is the
   last thing an entry should be able to hide.
4. **Most days get no entry.** When nothing but churn survives selection, the generator
   emits nothing. Silence is the default.

## Citing the Transcript Archive

The archive is private ([#3](https://github.com/NGL321/mosaic/issues/3)), so an entry cites
a session it cannot link to: **`sha256` of the transcript, plus the window, plus which
segments of the file the day owns.** The `Index` manifest resolves hash → Drive path.

**A session is a segment of a transcript file, not the file.** It ends after an hour
without work, and it belongs to the local day it **ended** on. Only one day can own it, and
the end is the side the generator is standing on: an entry is written when the segment
closes, so the owning day is the day whose entry is being generated at that moment. Dating
by the start would mean reopening yesterday's entry — regenerating a day that is already
annotated and already read — every time a session crossed midnight. One file therefore feeds
more than one entry: a real transcript in the archive splits into four segments across two
days, one of them straddling midnight. The hash alone would cite all of it, which is why the
window is part of the citation and not decoration.

Windows are printed in local time. A UTC window beneath a locally-dated heading contradicts
itself on the page.

### The scrub fails closed

Besides the narrative pass, the generator reads a transcript's **content** — as opposed to
its structure, which it also reads, for windows, segments and the hash — for one purpose:
scanning for anything that looks like a secret, at the boundary where public output is
produced.

#3 §3.2 is a prohibition, not a reporting requirement: secrets never reach repo, Drive
plaintext, logs, or notebook output. So a non-zero count **blocks the entry**. Nothing is
emitted, the count and its location surface to Noah out-of-band, and generation for that day
stays blocked until he resolves it.

Counting without blocking would be worse than not counting at all: it would publish an entry
containing a secret and helpfully note underneath that it contains one, advertising the leak
to a reader who would otherwise have scrolled past. A count is the residue of a scrub, never
a substitute for one.

## Provenance Tiers in an entry

A badge per line, in the form [`../curriculum/README.md`](../curriculum/README.md) fixes:
`⟦T3⟧` bare, and `⟦T3 · #40⟧` when a Verification Debt issue holds that line down. **Most
notebook lines have no debt behind them** — a narrative line about why something was
reversed has nothing to discharge — so the bare form is the common case, and the rule is
*tier, plus the debt issue when one exists*. A generator that cannot find an issue emits
the bare badge; it never invents a reference and never drops the badge.

The tier belongs to **the line**, not to the work it describes, and only two of the three
tiers can appear:

- **T3** — everything generated. Both the narrative claims about *why* and the lines
  harvested mechanically from the history: machine-produced and unverified.
- **T1** — Noah's annotations, which are derived unaided by construction.

**Harvested lines are T3, not T2, and the difference matters.** T2 requires that Noah
personally verified the claim, and `curriculum/README.md` rejects a fourth tier for
machine-produced-but-checkable content on exactly this ground: *verifiable is not verified*,
and *an instrument that reports on itself measures nothing*. A harvested line nobody has
read is machine output whether or not a commit SHA sits beside it. Badging it T2 would
inflate the census the curriculum deliberately made uncomfortable, while claiming a
verification nobody performed.

The distinction between *harvested from an artifact* and *narrative about why* is real and
worth showing — it is simply not the tier ladder. It shows up on the axis that already
carries it: harvested lines are the ledger, narrative lines are the prose.

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
same day, with the measured word counts that decided between them — is retained in-tree at
[`../docs/prototypes/notebook-entry/`](../docs/prototypes/notebook-entry/), alongside the
rendered entries it produced.

It is **kept as a primary source, not as a tool**: nothing regenerates from it, nothing
depends on it, and it is not the generator described above. It is in the tree rather than on
its branch because §4 gives `prototype/` branches a lifetime that ends at merge, and a
record whose central asset is resolving years later cannot cite a ref that is scheduled to
die. A throwaway and a primary source cannot be the same ref; this is the second.
