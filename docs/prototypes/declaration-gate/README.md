# PROTOTYPE — the declaration gate: refusing a malformed run-set declaration where it is committed

Ticket [#181](https://github.com/NGL321/mosaic/issues/181). Built to be thrown away, and
retained as a **primary source** for how the third gate was decided — not as a tool.
Nothing runs it, nothing depends on it, and it never touches GitHub, git, or the network.

```console
python docs/prototypes/declaration-gate/prototype_tui.py
```

- `gate.py` — the check: seven **refusals**, and the `READS` table that decides which
  findings are entitled to fire here at all.
- `prototype_tui.py` — sixteen cases. `p` is the one the ticket exists for; `h` and `c`
  are the two the gate **accepts** and the reason the partition is written as data; `d` is
  the hole the gate did not cause and is the first thing to see; `B` prices the posture
  question instead of arguing it.
- `example/` — the two declarations from [#63](https://github.com/NGL321/mosaic/issues/63)'s
  prototype, plus the successor carrying [#182](https://github.com/NGL321/mosaic/issues/182)'s
  `follows:`.

## The question

[#63](https://github.com/NGL321/mosaic/issues/63) introduced the run-set declaration and
left it the only frozen artifact in the loop with no gate of its own. #60's dispatch gate
refuses a malformed charter before Searching begins; #64's publish gate refuses a malformed
manifest before a run enters the record. A malformed *declaration* is discovered when the
register comes out as **exit 2**, by which point the whole set has been run and its budget
spent.

The ticket asks three things: whether this is a third gate or a case in an existing one,
what it fires on, and whether it blocks.

## What the prototype found

**1. The gate introduces no refusal of its own, which is what makes the third-gate
question answerable.** Every name it fires was already defined by #63 or ruled by #182. The
gate is not new authority, a new vocabulary or a new place where a set can be judged — it
is #63's own refusal, fired at the first commit that could carry it. That reframes the
ticket's first question: the cost of a third gate is normally the cost of a third thing
that can disagree with the other two, and here there is nothing to disagree with, because
the gate and the backstop are the same predicate over the same text.

**2. Which findings move is a partition, not a judgement.** The criterion is one line:

> a finding whose inputs are all present at the declaring commit can fire at the declaring
> commit.

Tagging #63's and #182's twenty-one findings by what each one reads sorts them without
anybody weighing symmetry against cost. Four read the declaration alone
(`DECLARATION_ASSERTS_REGISTER`, `SEEDS_NOT_DERIVABLE`, `NO_ATTRITION_POLICY`,
`DATASET_UNPINNED`); three read the declaration and its siblings in `runs/`
(`NO_PREDECESSOR`, `HOLDOUT_SALT_REUSED`, `DECLARATION_AMENDED`); one needs manifests;
thirteen are downgrades. Seven move. **The ticket named five of them.**

The partition is written as a table in `gate.py` rather than as prose here, so a later
finding gets sorted by the rule rather than by whoever is adding it.

**3. A downgrade may never move, and `NO_HOLDOUT` is what makes that concrete.** The
temptation is to read the gate as *catch declaration defects early*, and under that reading
a kind-(1) declaration with no hold-out is an obvious catch: it is a defect, it is in the
declaration, it is cheap to see. It is also a **downgrade** — the set derives `exploratory`
at close, and exploratory results are first-class in the record (premise 3) with a route
into the Belt via a new preregistered Inquiry. A gate refusing it would be deciding what
kind of evidence the programme is allowed to gather.

So the gate's subject is not *defects*. It is exactly the findings under which the register
**cannot be derived at all**. Case `h` is that line, drawn where nobody would draw it by
eye.

**4. The trigger is a path and a diff mode, and the mode is worth as much as the path.**
`inquiries/NNN-slug/runs/*.declared.yaml` — #60's shape rather than #64's, because the
declaration's *appearance* is the freeze event exactly as `config.yaml`'s appearance is.
What falls out free is `DECLARATION_AMENDED`: a declaration is never legitimately edited,
so `modify` on this path is a refusal with no case analysis behind it.

That one is not decoration. #63 derives the register from the declaration's text **as it
stands**, so editing `master_seed` after the runs retroactively makes the draw rule produce
whichever seed was published — the entire mechanism, reversed by a text editor, and
invisible to every check downstream. #60 needed git history to tell a legitimate pre-open
charter edit from an illegitimate post-open one; here the diff mode settles it alone. This
is the strongest argument in the prototype for the gate existing, and it is an argument the
ticket did not have: **a commit-time gate can see something no later reader can.**

**5. `HOLDOUT_SALT_REUSED` was ruled by #182 and misfiled.** #182 refuses a successor
reusing its predecessor's byte-identical salt at exit 2, and handed #181 only
`NO_PREDECESSOR`. It reads two committed files and nothing else, so the partition claims
it. A criterion that finds a case its authors did not is the evidence that it is a
criterion rather than a rationalisation.

**6. `NO_PREDECESSOR` is three conditions under one name.** Driving it showed all three
emitting the same sentence: the absent field, the wrong predecessor, and the predecessor
that has not closed. They are not fixed the same way — the first is a missing line, the
second a wrong line, and the third is not a defect in the declaration at all but a
declaration arriving too early, fixed by waiting. The gate emits the condition alongside
the name.

**7. The posture question, priced rather than argued (case `B`).** Bypass the gate — commit
the declaration to a branch nobody opened a pull request for — and the same finding arrives
at set close with the same name and the same exit code, after roughly $2.40 of Modal time
at #57's rate. So:

- **The gate is not load-bearing, and does not need to be.** #64's finding was that the
  load-bearing gate is the one policing the artifact the act must produce. A declaration
  polices an artifact that has produced nothing yet, so this gate is advisory in
  `check_freeze`'s sense.
- **What makes advisory acceptable here is that the backstop is the same function.** #53's
  failure is an advisory gate that *reads* as load-bearing — a green run covering nothing.
  This gate cannot cover anything, because a set it wrongly passed is still refused at
  close by the identical predicate. It buys the budget and the declaring party's attention,
  not the guarantee.
- Which is why the gate says `ACCEPTED`, never `CONFIRMATORY`, and why nothing in it can
  pronounce on a register.

**8. Exit 2, never exit 1.** The gate's refusal *is* #63's exit 2 arriving early, so it
carries the same code. Exit 1 means `exploratory` in the register check, which is not an
error and is not the gate's to pronounce — no run has produced a number yet, and the
declaration in front of it may be a perfectly good exploratory one.

## Found and not fixed

**A declaration that is abandoned before it runs is a dead end** (case `d`). #182 requires
the predecessor to have **closed**, and nothing closes a set with no runs: the honest
account is `SET_INCOMPLETE`, a downgrade over manifests that will never exist. The
Inquiry's `runs/` then admits no further declaration. The two exits both cost something —
delete the declaration, which the gate refuses as an amendment and which erases the
sequence #182 exists to record; or run a set nobody wants in order to close it.

The gate did not cause this. #182's line has no termination rule, and the gate is only
where it becomes visible: without it the dead end is found at set close, after the
successor has already run. Raised on the ticket rather than settled here, because *what
closes an unrun set* is #182's question and not this one's.
