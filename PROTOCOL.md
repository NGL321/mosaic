# Working protocol

How work enters this repository: what gets versioned, who may write what, and what
happens when two workers collide. `README.md` is the entry point and states the
human–machine boundary in summary; this document is the mechanical reference.

Mosaic runs concurrent agents against one repository, with a single human researcher.
Every rule below exists to keep that arrangement legible to an outside reader — not to
add ceremony.

---

## 1. Two tracks

The repository carries two independently versioned tracks.

- **Research track** — the programme itself: vocabulary, claims, evidence, notebook,
  ledger, and any artifact whose behaviour a recorded result depends on.
- **Tooling track** — the apparatus: hosting, sync, CI, notebook generation, this
  document, `README.md`, configuration.

The boundary is decided by one test, applied when the branch is created:

> **If this artifact changed silently, could a result already in the record become
> wrong?**
>
> Yes → research track. No → tooling track.

**Worked example.** A deterministic dataset generator is **research track**, despite
reading as a tool. Change its generation logic and every experiment citing those
datasets now describes data that no longer exists. The same holds for analysis
pipelines, seed handling, and any scheduler whose ordering can reach a result. The
tooling track is smaller than "tooling" sounds: it is the apparatus that can garble the
record but cannot falsify a result.

Tags carry their track: `research-v0.2.1`, `tooling-v0.1.0`.

---

## 2. Versions

`main` is the programme's **current state of belief**, not its published state.
Unverified work lands on `main` and carries its provenance tier with it; the warrant
discipline does the job that a merge gate would do worse, and does it as a graded,
auditable annotation rather than a binary.

Research-track versions are read through Lakatos:

| | Meaning |
|---|---|
| **MAJOR** | The **Hard Core** changed. Under the Negative Heuristic this is not supposed to happen — a major bump is an admission that the programme was refounded or abandoned. `0.x` is pre-charter; ratifying the charter is `1.0.0`. |
| **MINOR** | A **Protective Belt** rung was added, retired, or falsified. |
| **PATCH** | The **record** accreted: evidence landed, debt was discharged, vocabulary was written, corrections were made. |

Version bump and diff size are **uncorrelated by design**. A 457-line research document
is a PATCH — it landed evidence and changed no claim. A two-line edit that retires a
belt rung is a MINOR. The version answers the one question a reader cannot get from the
diff: *did the programme's commitments move, or did its evidence?* Unlike software,
Mosaic has no build to break; the contract is **commitment**, not compatibility.

**Side effect worth reading.** A history where MAJOR never moves, MINOR moves steadily,
and each MINOR is preceded by PATCHes that landed evidence is the shape of a
*progressive* problemshift. MINOR churn with no PATCHes underneath — belt rungs added to
absorb anomalies, with no new evidence — is a *degenerating* one. This is evidence for
the programme-health review, not the whole of it.

Tooling-track versions are ordinary: `feat:` bumps minor, `fix:` bumps patch.

---

## 3. Commit types

Types map one-to-one onto bump levels, so the release bump is **computed** from the log
rather than judged at release time.

### Research track

| Type | Bump | Use |
|---|---|---|
| `core:` | MAJOR | Hard Core revision |
| `belt:` | MINOR | A Protective Belt rung added, retired, or falsified |
| `evidence:` | PATCH | Research output, verification results, experiment runs |
| `record:` | PATCH | Notebook, ledger, corrections, vocabulary |

### Tooling track

| Type | Bump | Use |
|---|---|---|
| `feat:` | minor | New capability |
| `fix:` | patch | Repair |
| `chore:` | none | Config, formatting, ignores |

**Release bump = the highest level appearing since the last tag.**

**Vocabulary is `record:`, not `belt:`.** A definition is not a claim — there is no
falsifier for *Extraction*, because it is the language claims are made in. `belt:` is
reserved for rungs that have falsifiers, which keeps the MINOR gate (§5) meaningful: it
fires only where a falsifier can exist. Vocabulary that revises the Hard Core is `core:`.

### Squashing

> **Squash within a type. Never squash across types.**

Squashing a `belt:` into an `evidence:` destroys the bump computation and buries the
moment the programme's commitment moved — the most important thing the log records.
Collapsing an agent's twelve working commits into one `evidence:` loses nothing,
provided the message enumerates the sub-actions.

---

## 4. Branches

| Class | Lifetime | Owner |
|---|---|---|
| `research/` `grilling/` `prototype/` `task/` | Dies on merge | Exactly one — the ticket's assignee |
| `inquiry/<name>` | Persists | Shared, under sync discipline |
| `tooling/<slug>` | Dies on merge | Whoever is doing it |

Ticket-branch prefixes are wayfinder's ticket types, so a branch name says which skill
produced it and which ticket to read. Nothing extra to remember.

**Ownership needs no new mechanism.** Wayfinder already requires claiming a ticket by
assigning it before any work begins. A branch's owner *is* the ticket's assignee, and
**nobody else commits to a claimed branch**.

Branches are named for **work, never for workers**. A branch named `agent/<id>` cannot
be wrong about its contents, so it silently absorbs whatever that session touched and
never signals contamination. Naming by work is what makes a collision visible.

**`inquiry/` is the long-lived class** — a subprogram or empirical line that persists and
contributes back whenever it has something worth logging. Long-lived *identity*, short-lived
*divergence*: it merges `main` in continuously, and it is the class most likely to produce
a hard collision. It cannot hold the single-owner rule, so it holds sync discipline
instead: **merge `main` before you push, always.**

---

## 5. Custody and warrant

Two rules, stated together because each is hollow alone.

### Custody — whose hand

- **Authored files** (`CONTEXT.md`, the charter): **human only.** Agents propose exact
  replacement text in a ticket or pull request; the human applies it.
- **Record files** (research documents, notebook entries, ledger rows, experiment
  output): agent-writable.
- **Gate artifacts are record, not belief.** A checker agent's critique of a falsifier
  draft, and a teach-cycle transcript, are agent-written and land in the record even
  though their *subject* is belief. **Custody follows the file, never the topic.**

This makes one claim mechanically checkable:

```
git log --format='%an' -- CONTEXT.md   →  one name
```

*"The vocabulary was written by the model"* is the form the credibility objection takes
against an openly LLM-accelerated programme. Under this rule it has a verifiable answer,
produced as a side effect rather than asserted in prose.

### Warrant — whose understanding

| Commit level | What the human must produce |
|---|---|
| `record:` / `evidence:` | Nothing. Verbatim transcription of an agent's proposal is fine. |
| `belt:` (MINOR) | **The falsifier, in their own words**, drafted before merge. |
| `core:` (MAJOR) | **A public, human-authored work product** — publication, essay, something externally addressed. Agents may not open a MAJOR ticket; they may report anomalies that pressure the Hard Core. |

A gate satisfiable by ceremony is worse than none, because in the record it is
*indistinguishable* from the real thing — a commit message written after skimming looks
exactly like one written after thinking. The gate must demand an artifact hard to
produce without the comprehension. A falsifier qualifies: it is not an extra
deliverable but the rung's minimum content, vagueness is visible on the page, and it is
auditable later against whether the rung was actually retired when the falsifier fired.

**The gate is an instrument, not a filter.** The human submits a *draft*. A checker agent
grills it, and — critically — **the checker must not be the producing agent**, which knows
the answer and cannot distinguish the human's understanding from its own priors. On
failure it diagnoses which failure:

- *Understands, expresses poorly* → coaching toward better expression, by analogy.
- *Does not understand* → a **teach cycle** (`.claude/skills/teach/`), from what the human
  does understand up to what the artifact requires.

So the gate can never be routed around by lowering the bar: failing it produces work
rather than a rejection. **Being unable to write the falsifier is the comprehension
ceiling reporting itself** — the measurement firing, not friction to route around.

**The loop's outcome is data.** A MINOR that took three teach cycles is a recorded fact
about where the ceiling sits, and is Curriculum input. Verification debt says what the
*programme* has not checked; failed explanation gates say what the *researcher* cannot yet
carry. Different deficits, both scheduled.

### Why both

Custody without warrant is **transcription** — the human pastes agent text, `git log`
returns one name, and the claim is true and empty. Warrant without custody leaves the
vocabulary agent-owned with a human signature on top. Custody governs vocabulary;
warrant governs claims. Neither category is ungoverned, and neither gate is applied
where it has nothing to bite on.

---

## 6. Merges

**Every branch merges through a pull request, on both tracks.**

> A reviewer other than the author is required when the author is an **agent**, or the
> contributor is **external**.

Ceremony uniform, scrutiny proportionate: a `.gitignore` fix is a pull request opened and
self-merged in seconds; an agent-built dataset generator sits until someone reads it.
Review exists to catch what the author cannot see, which is orthogonal to whether the
artifact is cited by the record.

**An agent is never the reviewer of record for its own output.** It may respond to review
and repair its own work. It cannot independently assess reasoning it generated.

- PATCH-level research: a fresh agent may review; the human merges.
- MINOR / MAJOR: the human, through the §5 gate. The draft goes on the pull request, the
  checker agent grills it there, and the teach cycle, if it fires, happens in that
  thread — which makes the human–machine boundary **visible in the record** rather than
  advertised in a README.

**Merge commits. Never rebase a pushed branch.** `inquiry/` branches take `main` by
merging it in. This produces uglier history, and the ugliness is correct: rebase rewrites
*when* something was known, and a programme whose asset is an auditable record of what it
believed and when cannot afford a history that lies about chronology to look tidy. Same
reason as the squash rule.

---

## 7. Collisions

> **Unpushed collisions are reconstructed. Pushed collisions are split, never rewritten.**

The line is `git push`. Before it, history is a draft: discard the malformed commits and
re-commit the tree onto correctly named, correctly typed, singly-owned branches from
`main`. After it, history is part of the record — an agent may have pulled it, a pull
request may cite it — and it gets corrected by **adding** commits, not rewriting them.

Reconstruction backs the affected file contents up outside the repository first, and
retains the original branch under `backup/` until the replacement branches have merged.

Most collisions are prevented rather than recovered, by three rules already stated:
single-owner branches (§4), short divergence (§4), and human-only authored files (§5) —
which makes the contended-file collision structurally impossible for `CONTEXT.md`.

---

## 8. External contributions

External work arrives as a fork pull request, always carries a reviewer, and **does not
merge** until the attribution, licensing, and citation policy exists. That policy is its
own ticket; it must be answered before the first external contribution arrives rather
than during it.
