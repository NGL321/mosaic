# `regenerate@curriculum-open`

> Recompute a generated instance from its source of truth. Distinct from `edit` by construction: there is nothing to decide, so nobody may decide it. — applied to *The committed snapshot of the debt ledger*.

| | |
|---|---|
| **Where** | curriculum/open.md (repository) |
| **Track** | tooling |
| **Custody** | agent-writable |
| **Origin** | generated |
| **Defence** | not-owed |

## When this is done, all of the following are true

- **current** — curriculum/open.md agrees with the tracker as of the moment it was written, and says on its face when that was.
- **derived-only** — Every row in the file is a function of tracker state. Nothing in it was typed by a hand, and nothing in it can be edited into agreement.
- **disagreement-loud** — Where the kind label and the issue state disagree, the run FAILS rather than filing a plausible-looking row.

**Whose decision:** none

## What you must be given before you start

- **`ticket`** — the issue this work is claimed against

*If you were not given one of these, you are not equipped to run this Operation. Ask; do not invent.*

## Terms used here

- **Verification Debt** — A derivation step the programme has not checked. Owed by Noah, discharged by learning. Label debt:verification. <sub>PROTOCOL.md §5, #189</sub>
- **Source Debt** — An assertion the record has never sourced. Owed by an agent, discharged by search. Label debt:source. <sub>#189</sub>

## May you do this?

| Actor | | |
|---|---|---|
| noah | **may** |  |
| agent | **may** |  |
| external | **may-not** | PROTOCOL.md §8 — external work arrives as a fork pull request and lands through review. **You want `propose@curriculum-open`.** |

## How it is met today

### 1. branch — **an agent**

git checkout -b tooling/<ticket>-debt-snapshot origin/main

*Branch prefixes are wayfinder ticket types. FINDING: `record/` is in use on six branches and §4 has no row for it — the map's own fog patch, reached here by trying to fill in {prefix} from the table and finding no cell.*

<sub>PROTOCOL.md §4</sub>

### 2. single-owner — **an agent**

Confirm you are the ticket's assignee. Nobody else commits to a claimed branch.

    gh issue view <ticket> --json assignees

<sub>PROTOCOL.md §4</sub>

### 3. run — **`tool:tools/snapshot_debt.py`**

python tools/snapshot_debt.py

- exit `0` — fine
- exit `2` — the tool could not run — gh missing, unauthenticated, bad JSON → **Fix your environment and re-run. Nothing has been written.**
- exit `3` — the tracker data is malformed — an issue is missing required fields → **STOP. Do not commit. The malformed issue is the defect; repair it on the tracker and re-run.**

### 4. commit — **an agent**

Commit the regenerated file. Do not edit it.

    chore: refresh the debt snapshot

### 5. staleness-gate — **NOBODY — filed gap**

python tools/snapshot_debt.py --check — exit 1 means the snapshot is stale.

> **GAP.** the tool has a --check mode written FOR CI and no CI calls it. The snapshot goes stale silently every time a debt issue is filed or discharged, which is exactly the coupling below, unenforced.

### 6. no-rewrite — **an agent**

Never rebase, amend, or force-push once pushed. Corrections are added commits.

<sub>PROTOCOL.md §6, §7</sub>

### 7. open-pr — **an agent**

Open a pull request. Every branch merges through one, on both tracks.

<sub>PROTOCOL.md §6</sub>

### 8. review — **Noah**, by hand

A reviewer other than the author is required when the author is an agent. An agent is never the reviewer of record for its own output.

<sub>PROTOCOL.md §6</sub>

### 9. merge-commit — **Noah**, by hand

Merge with --no-ff. Never squash-merge. The merge commit takes the highest
commit type on the branch:

    chore: refresh the debt snapshot (#PR)

    Resolves #<ticket>.

    Bump: tooling none

*FINDING: `Bump:` is a hand-typed statement of a fact the log already computes (#176). It is written here as a step with executor `noah` because that is what is TRUE today, not because it is right. The honest entry makes the defect visible at the exact step that carries it.*

<sub>PROTOCOL.md §6</sub>

### 10. merge — **Noah**, by hand

Merge the pull request.

<sub>PROTOCOL.md §6</sub>

## What fires this

Regenerate whenever a debt issue is filed, discharged, or relabelled. — executor: **NOBODY — filed gap**

> **GAP.** nobody and nothing holds this. It is the map's standing case (#198: eighteen closed issues still carried debt:open) arriving on a second surface.

## Couplings

- **`file@debt-issue`** — A debt-issue `file` requires a curriculum-open `regenerate`.

