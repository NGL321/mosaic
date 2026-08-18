# `add@CONTEXT-entry`

> Bring a new instance of the class into being. — applied to *A vocabulary entry in CONTEXT.md § Research substance*.

| | |
|---|---|
| **Where** | CONTEXT.md, section "Research substance" (repository) |
| **Track** | research |
| **Custody** | human-only |
| **Origin** | authored |
| **Defence** | owed |

## When this is done, all of the following are true

- **entry-present** — CONTEXT.md § Research substance contains an entry for the term, carrying its _After_ / _Departs_ lines and a Provenance Tier.
- **hand** — The entry's text entered the record under Noah's hand.  <br>*PROTOCOL.md §5 "Custody — whose hand"*
- **defended** — A defence exists — what changed and why, in Noah's own words — or a citation to reasoning already recorded, enumerating the terms it covers.  <br>*PROTOCOL.md §5 "The defence — which changes owe one"*
- **session-cited** — Where an agent held the pen, the record carries a session citation resolving in the Transcript Archive.
- **debt-filed** — Anything the entry's derivation needs from below the competence floor is filed as debt, against the term.  <br>*PROTOCOL.md §5 "The competence floor"*

**Whose decision:** noah

## What you must be given before you start

- **`ticket`** — the wayfinder ticket or issue this work is claimed against
- **`term`** — the term being defined

*If you were not given one of these, you are not equipped to run this Operation. Ask; do not invent.*

## Terms used here

- **competence floor** — Noah's declared statement of what he can defend unaided. Defence terminates AT the floor, not at first principles. Declared in curriculum/FLOOR.md. <sub>PROTOCOL.md §5 "The competence floor"</sub>
- **Provenance Tier** — A graded annotation of how well warranted a claim is. External contributions land at the bottom tier. <sub>PROTOCOL.md §8</sub>
- **defence** — What changed and why, in Noah's own words, on the pull request thread. Judged for COMPREHENSION, never prose — a checker rejecting on polish has broken the instrument. <sub>PROTOCOL.md §5 "The defence — which changes owe one"</sub>

## May you do this?

| Actor | | |
|---|---|---|
| noah | **may** |  |
| agent | **may-not** | PROTOCOL.md §5 — CONTEXT.md is human-only. An agent DECIDING vocabulary is the breach. **You want `propose@CONTEXT-entry`.** |
| external | **may-not** | PROTOCOL.md §8 — "human only" means Noah, not any human. A fork pull request touching an authored file is refused on custody grounds however good it is. **You want `propose@CONTEXT-entry`.** |

## How it is met today

### 1. branch — **an agent**

git checkout -b record/<ticket>-<term> origin/main

*Branch prefixes are wayfinder ticket types. FINDING: `record/` is in use on six branches and §4 has no row for it — the map's own fog patch, reached here by trying to fill in {prefix} from the table and finding no cell.*

<sub>PROTOCOL.md §4</sub>

### 2. single-owner — **an agent**

Confirm you are the ticket's assignee. Nobody else commits to a claimed branch.

    gh issue view <ticket> --json assignees

<sub>PROTOCOL.md §4</sub>

### 3. decide — **Noah**, by hand

Decide the term, the carving, and what it departs from.

### 4. draft — **an agent**

Draft the entry's prose, rendering the decision Noah made.

*Agent-drafted, human-signed is the sanctioned pipeline, not a concession.*

### 5. floor-check — **Noah**, by hand

Decide whether the derivation reaches below the competence floor.

### 6. file-debt — **an agent**

File what it needs from below the floor.

> **Also required: `file@debt-issue`.**

### 7. apply — **Noah**, by hand

Apply the text and commit it under a human identity, with Claude-Session: on the commit.

### 8. defence — **Noah**, by hand

Put the defence artifact on the pull request thread, or cite the grilling tickets it discharges through, ENUMERATING the terms covered.

### 9. identity-check — **`ci:.github/workflows/custody.yml`**

Check the authored file was committed under a human identity.

### 10. citation-check — **`ci:.github/workflows/custody.yml`**

Check a Session: trailer is PRESENT.

### 11. citation-resolves — **NOBODY — filed gap**

Check the cited session RESOLVES in the Transcript Archive.

> **GAP.** unmechanised — a public runner cannot reach a private archive (PROTOCOL §5)

### 12. grill-defence — **an agent**

Grill the defence for comprehension, not prose. Must not be the agent that drafted the text.

### 13. no-rewrite — **an agent**

Never rebase, amend, or force-push once pushed. Corrections are added commits.

<sub>PROTOCOL.md §6, §7</sub>

### 14. open-pr — **an agent**

Open a pull request. Every branch merges through one, on both tracks.

<sub>PROTOCOL.md §6</sub>

### 15. review — **Noah**, by hand

A reviewer other than the author is required when the author is an agent. An agent is never the reviewer of record for its own output.

<sub>PROTOCOL.md §6</sub>

### 16. merge-commit — **Noah**, by hand

Merge with --no-ff. Never squash-merge. The merge commit takes the highest
commit type on the branch:

    record: <one-line gist> (#PR)

    Resolves #<ticket>.

    Bump: research PATCH

*FINDING: `Bump:` is a hand-typed statement of a fact the log already computes (#176). It is written here as a step with executor `noah` because that is what is TRUE today, not because it is right. The honest entry makes the defect visible at the exact step that carries it.*

<sub>PROTOCOL.md §6</sub>

### 17. merge — **Noah**, by hand

Merge the pull request.

<sub>PROTOCOL.md §6</sub>

## Couplings

- **`file@debt-issue`** — An entry whose derivation reaches below the floor requires a debt-issue `file`. This is a LEGAL action carrying a companion obligation, not a null (premise 18).

