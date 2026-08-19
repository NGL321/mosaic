# PROTOTYPE — the command surface and dispatch, as one object

Ticket [#232](https://github.com/NGL321/mosaic/issues/232), on
[Map: The Operation set](https://github.com/NGL321/mosaic/issues/220). Built to be thrown
away, and retained as a **primary source** for how the interface was chosen — not as a
tool. Nothing runs it, nothing depends on it, and it never touches GitHub, git, or the
network.

```console
python docs/prototypes/operation-interface/prototype_tui.py
```

## The question

[Premise 17](https://github.com/NGL321/mosaic/issues/220) asserts that the command surface
and dispatch are **one object seen from two sides**, and does not say what the object is.
#232 asks what it is: naming, what it reads to check current state, what it refuses versus
what it warns about, whether it ever writes — and, on the other face, how an agent is given
work, what it may write, and what it must return.

The answer settled before building: **the object is the rendered cell, resolved from a
key.** A human types `python tools/operation.py add@vocabulary-entry` and gets the entry;
an agent is handed the same key as a mandate and its first act is the same call. *What an
agent may write and must return* is then not a separate dispatch protocol — it is
`inputs:`, `actors:` and the postconditions on the cell it was dispatched to, all of which
already exist. Premise 16's acceptance test tests both faces at once, which is the
strongest argument for the collapse: a separate dispatch envelope would need its own
delegability test, and nothing runs one.

The prototype exists to make the alternatives fail out loud rather than be argued down.
Four things are switchable — **dispatch primitive**, **whether the command writes**, **what
happens when live state is unreadable**, and **where a proposal routes** — over ten events
and one chain.

## How to drive it

`1`–`4` are the four doors: a custody refusal, a derived null, a stated null, and a key
that does not resolve. `5`–`8` are the dispatch loop. `9` runs the command from a sandbox.
`0` is the base case and `d` is self-certification. `c` runs the chain out.

Three things are worth doing deliberately:

1. `c`, then `p`, `z`, `c`. The proposal reaching Noah, then the same proposal handed to an
   agent. Premise 19 reads as satisfied in both.
2. `u`, then `5` `6` `9`. Every refusal keyed to unreadable state stops firing, silently.
3. `0`. The chain that could never route a proposal, refused before it exists.

## What was settled, and where

Seventeen questions across four rounds. The load-bearing ones:

| | Settled |
|---|---|
| The object | The rendered cell, resolved from a key. One executable, two doors — `tools/operation.py`, with the `/operation` skill's whole body being *run this with your key and follow what it prints*. |
| Naming | `operation`, not `op`. It is `OPERATIONS.md`'s live twin, and the two renderings reading as one object is the whole of premise 11. |
| Writing | **Never.** It renders and refuses; every write is the actor executing rendered steps. |
| Refuse vs. warn | Refuse on **computable facts**, warn on heuristics — and every refusal is a **redirect**, never a dead end. A refusal the set has not recorded is *novel*, and exits to the catch-all as `propose:edit@operation-cell`, so the command's failure path is a writing path. |
| Unreadable state | A **refusal**, not a warning, and the mode is detected rather than chosen. |
| Mandate scope | The mandate names the **ticket**; the command is entered **once per write**. A Ralph iteration is one key, never a bundle. |
| The mandate | Not a 46th class — a **label**, `agent:dispatched` / `agent:in-progress` / `agent:blocked`, adopted verbatim from [#24](https://github.com/NGL321/mosaic/issues/24) and added to `ticket`'s declared label set. Open mandates are a query (premise 20). |
| Dispatch's classes | `dispatch@ticket` **in**; `dispatch@map` **null** — a mandate over a map has no close. Everything else **absent, not null**: absent means nobody looked, and ruling the research-loop classes null from here would be a ruling on [#55](https://github.com/NGL321/mosaic/issues/55)'s side of premise 5's seam. |
| The return | A **structured comment** on the dispatching ticket: keys entered, addresses written, evidence for the proposed close, and **the step it stopped at**. |
| Who closes | The **dispatcher**, by a stated actor override on `close@ticket` — the machinery [#228](https://github.com/NGL321/mosaic/issues/228) minted for `close@debt-verification`, on the same shape of reason. |
| Agent dispatching agent | **Allowed, ungated, any form.** The research programme's branching *is* parallel sandboxes, and a no-dispatch rule collapses it into one session. |
| The two returns | **Asymmetric.** A `close` pops **one frame**; a `propose` jumps to the **root**, which is always a human. |

### Why the return paths are asymmetric

This is the finding the whole design rests on, and it is Noah's, not the prototype's.

Gating dispatch was the obvious way to bound an agent chain, and it is the wrong one: it
gates the honest case — a controlling agent running a Ralph loop, which premise 16
*requires* — while doing nothing about the generative loop, which
[#24](https://github.com/NGL321/mosaic/issues/24)'s prototype already established is a
**rate across the tracker** rather than a depth in one thread.

The asymmetry bounds the thing that actually needs bounding. **Depth is free; the propose
channel does not get deeper.** A chain of agents may run arbitrarily deep, and every
proposal raised anywhere in it lands on the same human. Under the one-hop alternative
(`p`), each agent passes the proposal to another agent, and premise 19 — *no new way to
interface with this project comes into being without Noah seeing it first* — holds
formally while being false in fact. The prototype prints that as `CRITICAL`, and the
distinction is invisible in prose because both readings satisfy the sentence.

### Why unreadable state refuses

Noah's framing, and sharper than the one the question was asked with: a warning there is a
**control surface**. Anything that can make state unreadable can make a refusal not fire,
so the degradation path is an injection primitive rather than a convenience. Case `9` under
`u`: the sandboxed delegate — the configuration [#236](https://github.com/NGL321/mosaic/issues/236)
*requires*, since a delegate with live repository access goes false-green on the exact
defect the test exists to find — is the one place where every refusal silently stops
firing. Refusing instead converts [#224](https://github.com/NGL321/mosaic/issues/224)'s
defect 3, *a step true but not executable*, from a format defect into a computed refusal.

## What the prototype found

Two findings, both from driving it, and both invisible in the design as agreed.

**1. The parent edge is not the authority edge.** The rule settled in grilling was *store
the parent edge, compute the root*. The first implementation did exactly that — walked
parent-ticket edges to the root and read the root's actor — and routed a proposal **to an
agent**, correctly, on the first run. The root ticket's assignee is the first **delegate**;
the human is the first **dispatcher**. Two edges hang off one dispatch and they point at
different trees: the parent edge is the *work* tree, the dispatcher is the *authority*
chain, and a proposal routes up authority. The stored fact is unchanged and the arithmetic
over it is not: walk parents, read the **dispatcher**, never the assignee. Both roots are
printed side by side in the ticket table (`work=` and `auth=`) because they genuinely
differ.

**2. The base case is a refusal on the cell, not a step in the procedure.** *Compute the
root* has no answer when no human appears anywhere in the chain — a cron-started agent
dispatching another agent — and that chain can still raise a proposal. Checking it at
proposal time discovers the unroutable mandate *after* the work is done, so it is checked
at dispatch. The first implementation put it in `dispatch@ticket`'s step list, where it
fired **after the entry had already rendered**: the actor was handed a complete procedure
and then told it was void. **A step can be skipped and a refusal cannot**, so a condition
that invalidates the whole cell belongs in the command's refusal set, above the render.
Case `0`.

The generalisation worth carrying: anything that can void a cell is a refusal; only what
can fail *within* a valid cell is a step. That is a rule the format can be checked against,
and it is a candidate lint for [#236](https://github.com/NGL321/mosaic/issues/236)'s suite.

## What this does not settle

**The `/operation` skill's own text**, and the command's implementation — both are
[#234](https://github.com/NGL321/mosaic/issues/234)'s, which is execution with no decisions
left in it. The cell table here is a hand-cut slice of `source/`, not a generator; premise
11's *one generator, two renderings* is asserted by this prototype and demonstrated by
that ticket.

**Where the depth cap lives.** #24 ruled it belongs in the workflow rather than in the gate
that noticed it, and this prototype does not model a workflow. The asymmetry bounds the
propose channel and does not bound spend or fan-out — #24's *generative loop* remains open
by reference, as it was.
