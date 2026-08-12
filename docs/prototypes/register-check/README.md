# PROTOTYPE — the register check: confirmatory or exploratory, by ancestry

Ticket [#63](https://github.com/NGL321/mosaic/issues/63). Built to be thrown away, and
retained as a **primary source** for how the register was mechanised — not as a tool.
Nothing runs it, nothing depends on it, and it never touches GitHub, git, or the network.

```console
python docs/prototypes/register-check/prototype_tui.py
```

- `example/2026-08-14-s3f9c1.declared.yaml` — the run-set declaration, kind (2).
- `example/2026-08-14-p7b2e4.declared.yaml` — the kind-(1) form, over a dataset older than
  the repository.
- `register.py` — five **refusals** (the register cannot be derived), thirteen
  **downgrades** (it derives, to `exploratory`), and one **hazard**, which is neither.
- `prototype_tui.py` — nineteen cases, each breaking one thing. Case `t` is the one the
  ticket exists for; case `s` is the one nothing before this ticket could see at all.

## The question

#63 asks how a result's register is established so that no argument can move it. Premise 3
bars exploratory results from the Protective Belt, and that guarantee is only as good as
the check behind it — which must be **ancestry, not persuasion**, because the argument
*"this metric was obvious in advance, we just forgot to write it down"* will be made, by an
agent, persuasively.

## What the prototype found

**1. The ticket's own rule does not hold, and this is the headline.** It says the config
SHA and the charter's metric must be **ancestors of the commit recording the output
sha256**. Ancestry orders *commits*. It does not order a commit against *the data*:

1. run the training script against a candidate under `configs/`, read the number;
2. liking it, commit that candidate to `config.yaml` — which under
   [#60](https://github.com/NGL321/mosaic/issues/60) **is** the freeze;
3. commit the run manifest carrying the number from step 1.

The freeze is a genuine ancestor of the manifest. Every ancestry check passes. The result
is exploratory and the check calls it confirmatory. This is `#26` R6's failure in a new
dress — not a rule satisfiable by writing a word, but one **satisfiable by committing in a
convenient order**. Case `t` runs exactly this history and the check refuses it.

**2. Ancestry is a property of one result, and the leak lives in the siblings that were
never committed.** An agent runs twenty seeds against the frozen config, reads twenty
numbers, and publishes the manifest for the one that cleared the decision rule. *Every
ancestry check passes perfectly* — the freeze precedes every run, the charter precedes the
freeze — and the data chose the result. `inquiries/README.md` is what makes this reachable:
the seed is deliberately **outside** `config.yaml` ("the config declares how seeds are
drawn; each run's manifest records the value it drew"), so the freeze pins the instrument
and says nothing about which seeds get run. Nothing in the record before this ticket could
notice: under [#64](https://github.com/NGL321/mosaic/issues/64) a run that produces nothing
leaves no manifest, and **absence is not a record**.

**Ruled on #63: the register attaches to a declared set of Runs, never to one Run.** A
**run-set declaration** is committed before any run in the set produces a number, naming
the config SHA and *how the seeds are drawn*. Its appearance is the second freeze event,
symmetric with #60's first: `config.yaml` freezes the instrument, the declaration freezes
the measurement. Absence becomes visible for the first time — six declared, one published
is now a refusal (case `s`) rather than a silence.

This kills the ticket's own filing proposal. The ticket asks for the register as *"a fifth
field"* on the run manifest, and a Run cannot carry it: whether these twenty seeds were
named before any of them produced a number is not a fact any one of them can see. Twenty
manifests each carrying `register: confirmatory` would be twenty assertions about something
none of them observes — the declared-register failure [#56](https://github.com/NGL321/mosaic/issues/56)
and [#60](https://github.com/NGL321/mosaic/issues/60) both abolished, relocated one level
down.

**3. What actually closes the ordering hole is the dispatch witness, and it is in-graph
where it matters.** Git can only ever timestamp commits, and both author and committer
dates are settable to anything. What orders a commit against the data is that the run was
**launched from the declaration commit**: the runner's record of *what it checked out* is
written by the party outside the job — the same trust root #64 rests the environment block
on, and the third time [#58](https://github.com/NGL321/mosaic/issues/58)'s admin-list
finding turns out to be load-bearing.

**The attestation is copied into the manifest at publish, never referenced.** GitHub
expires logs on a retention window, and a register derivable only until that window closes
is not derivable. Same author, same moment and same trust root as #64's `env:` block, which
makes the whole derivation a function of committed text in a clone, in ten years, with no
live service in the loop. This is Noah's standing requirement in its local dialect: outside
evidence is welcome **if it is traceable and cannot disappear**, and git is preferred
because its history is immutable rather than because it is git.

**4. Seeds must be derivable rather than chosen, and that is what makes attrition
arithmetic.** The declaration names a master seed and a rule, not a list. Seed *i* is a
function of committed text, so the sequence is recomputable in a clone by anyone and
choosable by nobody — and *"the next seed"* after a failed run is arithmetic rather than a
decision taken with the data in view. A literal list is honest about the runs it names and
silent about replacements, which is why case `l` cannot derive a register at all.

**Ruled on #63: the attrition policy is declared in advance** — how many replacements, and
where they come from. A set with no declared response to a failure improvises one *after*
the failure, which is a judgement made with the data in view.

**5. A null is not a failure, and the distinction is checkable rather than a matter of
trust.** The prototype initially treated "a run that failed" as an unverifiable agent
claim. That was wrong, and the correction is a finding:

- A run that **completes and misses the threshold** is a *result* — bytes, an
  `output_sha256`, a Drive path, a full manifest. Nulls are first-class and
  [#61](https://github.com/NGL321/mosaic/issues/61) has them sorting themselves. Filing one
  as attrition is contradicted by the output that exists (case `n`).
- A run that **produces nothing** is attrition, and its evidence is the runner's own
  record: run id, conclusion, exit code. **Attested by the runner, never claimed by an
  agent** (case `c`).

So there is no unverifiable middle. What looked like a hole was two well-evidenced cases
that had been run together.

**6. One narrow leak survives, and it is marked rather than engineered against.** Logs
stream. A party watching a run can read the metric before the job writes output and cancel;
the run then legitimately has no output, is honestly attested as *cancelled*, and the
attrition policy replaces it with the next derivable seed. **One peek per cancellation —
visible and countable**, because every cancellation is in the run record with the party
that fired it. `contract.py`'s pattern is reused exactly: the check appends an untestable
hazard (`cancellation_peek`) rather than refusing, so it cannot be omitted by the party
with a motive to omit it, and it travels into the coverage report someone reads at a stall.

**7. The kind-(1) case needs a second rule, and the second rule is a hold-out.** Nothing in
this repository can precede a dataset released in 2019. Ancestry against the data is not
weak there, it is **meaningless** — there is no commit that could be an ancestor of bytes
published before the repository existed. **You cannot make old data new; you can
manufacture a portion that has not been seen.** The declaration commits a split by a
derivable rule — the same trick as the seed draw, pointed at records instead of runs — the
search and adequacy phase read only the exploratory portion, and the discriminating
measurement runs on records no run has ever read. The check recomputes the split and
confirms no earlier read intersects it.

Two failure modes fall out and both are ordinary rather than adversarial: an enumerated
split is a *choice*, and a choice made by someone who has already seen the data is the
exploratory move wearing a confirmatory label (case `E`); and an exploratory pass that read
the whole dataset destroys the hold-out permanently, because unlike a seed it cannot be
redrawn (case `T`). A dataset with no checksum is refused outright — unpinned, it is a tag
rather than a digest, one layer up from #64's `BASE_BY_TAG`.

**Ruled on #63: settled now, not deferred.** Premise 6 puts early work in kind (2) and
institutional access at autumn 2026, so nothing here is on the critical path — but
splitting datasets is ordinary practice agents will do anyway, and the rule costs nothing
to fix in advance.

**8. The register is never written down in `inquiries/`.** It is a pure function of
committed text — declaration, manifests, attestations — so there is no field to forge and
nothing that can drift. Materialising it would recreate exactly the problem
[#90](https://github.com/NGL321/mosaic/issues/90) refused for the belt graph: a stored copy
that can disagree with the recomputation, with no tiebreaker, surfacing as a wrong reading
rather than a failing check.

**Ruled on #63: computed always, rendered only where it is read** — into the coverage
report and the notebook entry, which are already projections rather than sources. That buys
the legibility [#60](https://github.com/NGL321/mosaic/issues/60) found these formats
otherwise lose (a verdict nobody sees until a stall is a verdict that arrives too late)
without creating a second thing that claims to be true.

**9. Three exit codes, because two would let a green run cover nothing.** `0`
confirmatory, `1` exploratory, `2` **the register could not be derived**. The third is
[#53](https://github.com/NGL321/mosaic/issues/53)'s lesson made structural, and it follows
`custody_check.py`'s precedent of treating "nothing to measure" as a failure rather than a
pass. It matters here more than usual because **exit 1 is not an error**: an exploratory
result is first-class in the record and its route into the Belt is premise 3's — becoming
the preregistered hypothesis of a new confirmatory Inquiry, which is Noah's transition
alone. The check never blocks work; it names what kind of evidence the work produced.

**10. Where it fires.** Not at every merge, and not at publish. Publish is
[#64](https://github.com/NGL321/mosaic/issues/64)'s gate and it decides whether a run is in
the record at all; the register decides what a *set* of runs is worth, so it fires at set
close (for the rendering) and again as a **refusal at `belt:` time**, beside §5's warrant
gate. Since it is a pure function, firing twice costs nothing and cannot disagree with
itself.

## Open, and handed on

- **The declaration has no gate of its own.** #60's dispatch gate refuses a malformed
  charter and #64's publish gate refuses a malformed manifest; a malformed *declaration*
  is only discovered later, when the register comes out as exit 2 and the set's work is
  already spent. A cheap freeze-time check on the declaration would catch cases `g`, `l`,
  `p` and `P` before any GPU time is bought. Filed as
  [#181](https://github.com/NGL321/mosaic/issues/181).
- **Re-runs across sets.** A second declaration against the same frozen config is a fresh
  determination and confirmatory in its own right — that much fell out of the set ruling.
  What is *not* settled is the pair: set 1 misses the decision rule, set 2 is declared and
  passes, and both are individually confirmatory while the sequence is a search. Every
  declaration against one config is visible in the directory, so the evidence is present
  and nothing reads it. Filed as [#182](https://github.com/NGL321/mosaic/issues/182).
- **The hold-out's budget.** A dataset has finitely many hold-outs. Each confirmatory
  kind-(1) determination consumes one, and nothing tracks the balance or says what happens
  when an Inquiry wants a second bite at a dataset it has already split. Left in the map's
  fog rather than ticketed — it cannot be specified before a kind-(1) Inquiry is real.
