# Curriculum

Mosaic's learning track, scheduled off the **Verification Debt** ledger rather than off a
syllabus — the mathematics the programme's own results demand, in the order they demand it.

## Where the ledger is

**The ledger is the issue tracker.** Verification Debt is a GitHub issue labelled
[`debt:open`](https://github.com/NGL321/mosaic/issues?q=is%3Aissue+label%3Adebt%3Aopen), and
that issue is the source of truth. There is no ledger file in this repository, by decision —
see [#5](https://github.com/NGL321/mosaic/issues/5).

The reasoning, briefly: a debt item is already an issue in everything but name. It blocks
other work, it is discharged by someone doing something, it wants a thread, and it wants to
be assigned. Mosaic already runs its planning on this tracker with native blocking edges
wired between tickets. A second, parallel bookkeeping system in Markdown would be a system
to keep in sync with the first, and the failure mode the design was chosen against is
bookkeeping heavy enough to be abandoned by month two.

```console
gh issue list --label debt:open
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

Then close the issue, relabel it `debt:discharged`, and cite the SHA that promoted the tier.
The issue is retained, never deleted — a discharged debt is a record of what the programme
did not know and when, which is the whole point of keeping it.

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
