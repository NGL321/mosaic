# Conjectures

**Research track.** Everything under this directory fails the test in
[`PROTOCOL.md` §1](../PROTOCOL.md): if it changed silently, a result already in the record
could become wrong. A conjecture's governor is the clearest case — under
[#61](https://github.com/NGL321/mosaic/issues/61) a result is judged under the governor that
is a **git ancestor of its data**, so a governor that could change without leaving a trace
would silently re-judge work already done.

A **Conjecture** is a node posted at a distance from the Hard Core and the admitted
Protective Belt because Noah suspects it is true and cannot yet show it. It is what
[Inquiries](../inquiries/README.md) bridge *toward*, and the unit that pays for them.

## Layout

```
conjectures/
└── NNN-short-slug/
    └── README.md        the statement, the governor, the formal rendering
```

**A sibling of `inquiries/`, never a parent of it.** One Inquiry may serve several
Conjectures, because an axiom is not owned by the system that bought it. Nesting would
force the programme either to re-run an Inquiry to re-derive a fact it already owns, or to
reach across directories in a way the nesting no longer explains. This is
[#78](https://github.com/NGL321/mosaic/issues/78)'s ruling one level up, and for the same
reason — *nesting is where a file sits, not what makes it what it is*.

`NNN` is the Conjecture's **issue number**, matching the rule in `inquiries/`: the tracker
is the only allocator that two concurrent sessions can both see.

## Split by ancestry

**Here, in the file** — beliefs and rules that must be *dated*:

- **The statement.** Noah's prose, by hand, always. **No template** — templating intuition
  produces intuition-shaped filler. Agents may propose one as a
  [Prospect](https://github.com/NGL321/mosaic/issues/109) and may never post one.
- **The governor.** Two meters — a **token allocation** and a **spend ceiling** — plus a
  **stall tolerance**. Exhausting either meter ends the work. Both are needed: an Inquiry
  can burn GPU-hours at near-zero token cost.
- **The falsifier.** Agent-drafted, Noah-signed. Conjecture falsifiers are cheap and need no
  grilling; **rung** falsifiers are his own words, much later, at belt admission
  ([#59](https://github.com/NGL321/mosaic/issues/59)). Two levels, two custodies.
- **The formal rendering** of the statement — the goal sentence, in the language
  [#166](https://github.com/NGL321/mosaic/issues/166) fixes. Agent-drafted, Noah-signed:
  reading one sentence back is a far smaller ask than authoring a formalisation. It cannot
  be drafted before #166 lands.

**On the issue** — dispatch state: spend to date, live Inquiries, returns, and the open gap
as it stands. Derived, never written.

## The premise scope is inherited, and declaring one is forbidden

A conjecture's formal system takes **the whole Hard Core and the whole admitted Protective
Belt** as premises. This is a safety property rather than a convenience: core contact is
detected as *inconsistency*, so under a declared subset a result contradicting an
**undeclared** core member would leave the system consistent and the mandatory return would
**never fire** — the Negative Heuristic failing silently, in exactly the case it exists for.

If tractability ever binds, the answer is a stronger prover or a weaker logic, **never a
smaller premise set**.

The Hard Core is **premise-only**: it may support a derivation and may never be its goal. A
conjecture that contradicts an admitted *belt* claim is legitimate, and shows up at posting
as *this conjecture, if it survives, retires claim X* — free, before a cent is spent.

## Stall returns; it never retires

Budget consumed while the **open gap** does not close is a degenerating problemshift, and it
fires a **return** to Noah — never a retirement. A computed stall that retired a conjecture
would restore the threshold [#9](https://github.com/NGL321/mosaic/issues/9) refuses, and let
the loop quietly shed directions that got hard.

**Retirement is Noah's alone.** A conjecture is a belief he holds, so a silent retirement
would leave him believing what the programme has already abandoned.

A stall return carries the gap at posting, the gap now, budget burned, which Inquiries
contributed usable axioms, and **the instrument-null accumulation uninterpreted** —
interpreting it is core-directed, and therefore something no agent may do.

## Amendment

The statement and the falsifier are **frozen for the life of the conjecture**; the escape
hatch is to post a new one, leaving the old on the graph in its dead state. The governor is
**amendable by Noah** — and a loosening amendment is structurally identical to answering a
stall return, so it cannot happen quietly. **Agents amend nothing, ever.**

## Nothing here yet

Deliberately, and for the same reason as `inquiries/`:
[#7](https://github.com/NGL321/mosaic/issues/7) has not named the first Protective Belt
claim and [#17](https://github.com/NGL321/mosaic/issues/17) reopened the choice of
phenomenon. The first conjecture is Noah's to post, by hand, and cannot be scaffolded here
in advance.
