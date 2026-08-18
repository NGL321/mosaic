# `file@debt-issue`

> Open a tracker instance recording an obligation. — applied to *A debt row — a GitHub issue labelled debt:verification or debt:source*.

| | |
|---|---|
| **Where** | github:NGL321/mosaic issue, label debt:verification|debt:source (tracker) |
| **Track** | research |
| **Custody** | agent-writable |
| **Origin** | authored |
| **Defence** | not-owed |

## When this is done, all of the following are true

- **row-exists** — A tracker issue exists carrying exactly one kind label — debt:verification (owed by Noah, discharged by learning) or debt:source (owed by an agent, discharged by search).  <br>*#189, which separated the two kinds*
- **holds-down** — The issue names what it holds down — the term or document whose derivation needs it.
- **curriculum** — The issue names what reading would discharge it.
- **measured-against-floor** — A verification debt is measured against the declared competence floor. Until the floor is declared, the obligation is undecidable rather than satisfied.  <br>*PROTOCOL.md §5 "The competence floor"*
- **snapshot-agrees** — The committed snapshot reflects the new row.

**Whose decision:** noah

## What you must be given before you start

- **`holds_down`** — the term or document whose derivation needs this
- **`kind`** — debt:verification or debt:source

*If you were not given one of these, you are not equipped to run this Operation. Ask; do not invent.*

## Terms used here

- **Verification Debt** — A derivation step the programme has not checked. Owed by Noah, discharged by learning. Label debt:verification. <sub>PROTOCOL.md §5, #189</sub>
- **Source Debt** — An assertion the record has never sourced. Owed by an agent, discharged by search. Label debt:source. <sub>#189</sub>
- **competence floor** — Noah's declared statement of what he can defend unaided. Defence terminates AT the floor, not at first principles. Declared in curriculum/FLOOR.md. <sub>PROTOCOL.md §5 "The competence floor"</sub>

## May you do this?

| Actor | | |
|---|---|---|
| noah | **may** |  |
| agent | **may** | An agent may file debt:source on its own authority — the debtor is an agent and the discharge is search. debt:verification asserts what Noah cannot yet defend unaided, which is a claim about him: an agent may file it, and premise 3's `propose` shape is the honest form. FINDING: this is a may/may-not distinction that splits ACROSS one cell by label value, which the key `intent x class` cannot express. Either debt:verification and debt:source are two artifact CLASSES, or the actor column needs a condition. Carried to #228. |
| external | **may** | An issue is not a fork pull request. PROTOCOL §8's gate does not reach the tracker. |

## How it is met today

### 1. choose-kind — **Noah**, by hand

Decide debt:verification or debt:source by asking who owes it and what discharges it.

### 2. write — **an agent**

Open the issue with the kind label, what it holds down, and the curriculum.

### 3. regenerate — **NOBODY — filed gap**

Regenerate the committed snapshot.

> **GAP.** the coupling below is stated nowhere and held by nobody.

### 4. link-back — **NOBODY — filed gap**

Add the debt to the term's entry or the document's debt section, so it is reachable from the claim.

> **GAP.** no mechanism, no convention, and no check. The ledger points at CONTEXT.md; CONTEXT.md does not point back.

### 5. field-check — **NOBODY — filed gap**

Refuse an issue missing a required field.

> **GAP.** snapshot_debt.py exits 3 on a malformed issue — at REGENERATION time, long after the issue was filed and by a different actor. There is no gate at the write.

### 6. state-label-agreement — **NOBODY — filed gap**

Flip the kind/state labels when the debt is discharged.

> **GAP.** #198 — eighteen closed issues still carried debt:open, because the flip was a job nobody had been given.

## Couplings

- **`regenerate@curriculum-open`** — A tracker `file` on this class requires a repository `regenerate` of curriculum-open.

