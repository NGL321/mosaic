# PROTOTYPE — where the Protective Belt graph lives

Ticket [#90](https://github.com/NGL321/mosaic/issues/90). Built to be thrown away, and retained
in-tree as a **primary source** for how the store was chosen — not as a tool. Nothing regenerates
from it and nothing depends on it.

```console
python docs/prototypes/belt-graph/prototype_tui.py
```

## The question

[#9](https://github.com/NGL321/mosaic/issues/9) specified the graph in full and never said where
any of it is stored. [#5](https://github.com/NGL321/mosaic/issues/5) ruled *the ledger is the issue
tracker*, on the grounds that a debt item was already an issue in everything but name. This
prototype exists to find out whether that argument carries to a graph, by building the graph three
ways and asking each store to do the things #9 obliges it to do.

The model is transcribed from #9, not invented here: three conditions, disjunctive eligibility held
by legs carrying kind / domain / untestable hazard, per-leg demotion, dead branches retained in
place, blanket demotion on a MAJOR, and the five health readings.

The seed is the programme's **real** graph as of #17 — six posted conjectures, no legs, an empty
belt. The scripted steps `[1]`–`[7]` are not predictions; each is the cheapest event that exercises
one rule #9 fixed, so the store gets asked a question it actually has to answer.

## What the prototype found

### 1. The naive index goes *up* when the belt is emptied

Fire `[m]` after taking all seven steps. The blanket demotion empties the belt, so
`predictive_to_connective` and `inert_share` lose their denominators and drop out of the mean — and
the index moves **-0.31 → -0.18**. A Hard Core revision reads as an improvement in programme
health.

This is a flat mean over readings that return "no reading" on an empty denominator, and #88 owns
the real weighting — but the failure is not in the arithmetic. It is that **an empty belt has no
health**, and any formula that averages over present readings will reward emptying it. The same
shape as #9's own argument against rewarding MINOR count, one level up.

### 2. GitHub's dependency edge already means something else, on the same issue graph

Store A has to spell support edges as `dependencies/blocked_by`. That relationship means *blocked
by* — and `/wayfinder` already uses it, on this repo, for exactly that. A support edge and a
blocking edge would be the same edge type on the same graph with two incompatible readings, and the
frontier query would start walking belt structure.

### 3. The chart's x-axis is what breaks the issue store

#9 puts the chart *against releases*, which means the index has to be computable **as the graph
stood at each past release**. A committed tree gives that for free: check out the tag, recompute.
An issue tracker has no cheap query for "what were these labels in March" — the information is in
per-issue timeline events, unbounded and rate-limited, and the chart is a build artifact that has
to generate unconditionally.

### 4. #5's argument does not carry

A debt item *is* an issue in everything but name: it has an assignee, an open/closed state, a
discussion, and a closing event. A graph node has none of those. Its condition is **computed** from
its legs rather than set; nobody is assigned to it; and what the programme does with it is compute
over it, not discuss it. Two of #5's three reasons are absent, and the third — *don't keep a
parallel Markdown system in sync* — argues the other way here, because under Store A the structured
half ends up in issue-body YAML anyway, unvalidated and un-diffable.

### 5. Custody can be a path instead of a convention

`PROTOCOL` §5 splits custody by **file**. So the proposal puts the two rates in two trees:

| Path | Hand | Rate |
|---|---|---|
| `belt/nodes/<id>.md` | Noah — statement, falsifier, relevance, admission | human |
| `belt/legs/<id>.jsonl` | agents — append-only, one leg per line | machine |

The impedance boundary #9 named becomes a directory boundary that `custody_check.py`'s existing
`AUTHORED` set can enforce, rather than a rule about which paragraph of a document you may touch.
One file per node also means agent-rate appends never contend on a shared file.

## What the prototype proposes

**Store B — committed files, custody split at the file boundary.** Issues keep the *conversation*
about admission where §5's grilling already happens (Store C's one addition), but they are never the
record of the claim. The chart is generated from the tree at each tag and written into `README.md`
unconditionally.

## What it does not settle

The five readings' formula and weighting are #88's. This prototype computes them only far enough to
show they are reachable off the store — and to surface finding 1, which #88 now has to answer.
