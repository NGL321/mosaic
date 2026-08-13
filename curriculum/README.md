# Curriculum

Mosaic's learning track, scheduled off the **Verification Debt** ledger rather than off a
syllabus — the mathematics the programme's own results demand, in the order they demand it.

## Where the ledger is

**The ledger is the issue tracker.** A debt item is a GitHub issue, and that issue is the
source of truth. There is no ledger file in this repository, by decision — see
[#5](https://github.com/NGL321/mosaic/issues/5).

**Two kinds, and the Curriculum reads only one of them.**
[#189](https://github.com/NGL321/mosaic/issues/189) split the original single `debt:open`
label, which held four populations of which only a fifth were Verification Debt:

| Label | Kind | Debtor | Discharged by |
|---|---|---|---|
| [`debt:verification`](https://github.com/NGL321/mosaic/issues?q=is%3Aissue+label%3Adebt%3Averification+-label%3Adebt%3Adischarged) | **Verification Debt** — a derivation step Noah cannot defend unaided | Noah | learning, on this Curriculum |
| [`debt:source`](https://github.com/NGL321/mosaic/issues?q=is%3Aissue+label%3Adebt%3Asource+-label%3Adebt%3Adischarged) | **Source Debt** — an assertion the record has not sourced | an agent | search, producing a **Source** |

The labels are **not exclusive**: an assertion may be both unsourced and undefended, and
carries both. The Curriculum schedules off `debt:verification` alone — which is what
`CONTEXT.md`'s definition always said and what the single label never held.

**What is not debt.** An **open problem** nobody can discharge is a Prospect, not a debt; an
**unreproduced external result** is a Source plus a reproduction Inquiry; and work whose
discharge is a *measurement* rather than a document is a task. All three left the ledger in
#189. The test is *is there a debtor and a discharge procedure* — not whether the record is
uncomfortable about something.

The reasoning, briefly: a debt item is already an issue in everything but name. It blocks
other work, it is discharged by someone doing something, it wants a thread, and it wants to
be assigned. Mosaic already runs its planning on this tracker with native blocking edges
wired between tickets. A second, parallel bookkeeping system in Markdown would be a system
to keep in sync with the first, and the failure mode the design was chosen against is
bookkeeping heavy enough to be abandoned by month two.

```console
gh issue list --label debt:verification            # what Noah owes — the Curriculum's queue
gh issue list --label debt:source                  # what an agent owes
```

## Why `open.md` exists anyway

Scheme C's real cost is that a clone of this repository would not contain the programme's
debt, and `git log` could not answer *what did the programme owe in March?* — which is a
poor position for a project whose central asset is an auditable record.

[`open.md`](open.md) closes that. It is a **generated, committed snapshot** of the tracker:
a read-through cache, never a source of truth. The tracker stays authoritative; the snapshot
makes the repository self-contained and puts the debt history in `git log`, where it can be
read years later without an API call.

Regenerate it with:

```console
python tools/snapshot_debt.py
```

Do not hand-edit it. If the snapshot and the tracker disagree, the tracker is right and the
snapshot is stale.

## Discharging debt

A debt item is discharged when the reading is actually done, not when someone is confident.
That requires two things, both of them artifacts:

1. A document in `docs/research/` that does the reading.
2. The commit that promotes the **Provenance Tier** badge at the claim site.

Then **add `debt:discharged`**, close the issue, and cite the SHA that promoted the tier.
**The kind label stays** — a discharged debt is a record of what the programme did not know
and when, which is the whole point of keeping it, and that record is worth nothing if it no
longer says *which* debt it was. The issue is retained, never deleted.

**The kind is one axis and the state is another.** A bare `debt:source` or
`debt:verification` is open; the same label beside `debt:discharged` is discharged. This
replaces the old `debt:open` / `debt:discharged` pair, which spent one axis on a state and so
had none left for the kind — the whole defect #189 was filed on. `snapshot_debt.py` groups on
the kind and cross-checks `debt:discharged` against issue state; an issue that is closed and
not discharged, or discharged and open, is reported as a bookkeeping error rather than quietly
filed under whichever heading its state implies.

## Provenance Tiers

Three, and deliberately only three:

| | Meaning |
|---|---|
| **T1** | Derived unaided. |
| **T2** | Derived with assistance and **personally verified** by the researcher. |
| **T3** | Machine-produced, unverified. |

A claim carries its tier at the claim site, as a badge: `⟦T3 · #31⟧` — the tier, and the
debt issue holding it down. The badge is typed by the researcher; agents propose it and do
not apply it, because `CONTEXT.md` and the charter are authored files under
[`PROTOCOL.md` §5](../PROTOCOL.md).

**Agent verification is not verification.** A claim an agent checked against primary sources
is still **T3**. This was decided against a live case: [#13](https://github.com/NGL321/mosaic/issues/13)
read most of `CONTEXT.md`'s citations back to their sources, and `CONTEXT.md` responded by
inventing a fourth tier in an HTML comment — *"machine-produced, checked against primary
sources"* — which is neither T2 nor T3 as defined.

That fourth tier is rejected. The agent's reading is **evidence attached to the claim**; it
lowers the cost of discharging the debt and it does not move the tier. The ladder measures
what *Noah* can defend, and an instrument that reports on itself measures nothing. The
consequence is a census that currently reads **five claims, all at T3, none verified** — which
is the honest number and is meant to be uncomfortable.
