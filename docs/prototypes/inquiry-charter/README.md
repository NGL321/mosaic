# PROTOTYPE — the Inquiry charter, and the gate that refuses it

Ticket [#60](https://github.com/NGL321/mosaic/issues/60). Built to be thrown away, and
retained as a **primary source** for how the charter format was chosen — not as a tool.
Nothing runs it, nothing depends on it, and it never touches GitHub, git, or the network.

```console
python docs/prototypes/inquiry-charter/prototype_tui.py
```

- `example/README.md` — one concrete charter, for a plausible ML Inquiry. **Illustrative
  only**: the phenomenon it names is one of the two still open under
  [#17](https://github.com/NGL321/mosaic/issues/17), and nothing here commits the
  programme to it. It lives under `docs/prototypes/` and not under `inquiries/` precisely
  so that it encodes no decision the programme has reopened.
- `gate.py` — the dispatch gate. Fifteen named refusals, each structural or checked
  against git; none of them reads prose for meaning.
- `prototype_tui.py` — breaks the charter one field at a time so each refusal can be *made
  to happen* rather than described.

## The question

#60 asks what the charter contains and what the dispatch gate checks before a run starts.
Premise 2 says an Inquiry with no hypothesis-blind Adequacy Criterion **cannot be
dispatched AFK** — "a visible refusal, and itself a finding about the Inquiry." Everything
here is an attempt to make that sentence mechanical, under `#26` R6's warning that **a rule
satisfiable by writing a word is not a rule**.

The charter was drafted before [#61](https://github.com/NGL321/mosaic/issues/61) and
[#164](https://github.com/NGL321/mosaic/issues/164) resolved, and revised after. Both
revisions **removed** fields. That is recorded below rather than smoothed over, because the
direction of the correction is the finding.

## What the prototype found

**1. Hypothesis-blindness is enforceable by *scope*, and not by inspection.** No checker
can read an Adequacy Criterion and decide whether it smuggles the hypothesis in. It can
decide whether the `adequacy` block and the `hypothesis` / `axiom_if_carried` /
`discriminating` blocks share a *name*. Declare the apparatus in two namespaces, require
them disjoint, and the criterion is blind by construction. An agent can still rename its
way across — and renaming is a visible diff on a file frozen at open, which is the point.
Case 3 is the real mistake this catches: tuning the apparatus against the very metric that
will judge it.

**2. The ticket's `register policy` field must not exist.**
[#56](https://github.com/NGL321/mosaic/issues/56) made Register *derived from git ancestry,
never declared*. A `register:` field would be exactly the assertion
[#63](https://github.com/NGL321/mosaic/issues/63) exists to prevent, so the gate refuses a
charter carrying one (case 9). The ticket body listed it; the ticket body predates #56.

**3. "One file or two" is the wrong axis; the split was already made.** Premise 9 puts the
freeze in the repo and dispatch state on the issue. Inside the directory, custody is **per
path**: `README.md` is frozen at open, `configs/`, `probes/` and `runs/` are agent-writable.
No second file is needed, because the agent-maintained progress part was never going to
live in the directory. After #164 this is cleaner still — see finding 6.

**4. The appearance of `config.yaml` *is* the freeze.** During Searching there is no
`config.yaml`, only candidates under `configs/`. When adequacy passes, the winner is
committed to that path, and that commit is the freeze event — dated, attributable, and an
ancestor of everything measured afterwards. This gives
[#63](https://github.com/NGL321/mosaic/issues/63) its ancestry hook without asking anyone to
assert anything, and it fits `inquiries/README.md`'s existing layout rather than amending it.

**5. A keyword scan for the Hard Core refuses the Negative Heuristic itself.** The gate
initially refused the charter as first written, because its return rule said *"return
immediately on any result bearing on the axioms"* — the honest statement of the mandatory
return, and indistinguishable by token from the thing the rule bars. #61 then removed the
rule from the charter altogether, which resolves it: the check is repointed at the
**Question's goal position** (case 7), which is #61's typing rule — *core sentences may be
premises, never goals* — rather than a scan for a forbidden word.

**6. Nothing in the Inquiry charter is signed, and that is a consequence rather than a
convenience.** Custody follows the hypothesis. Premise 18 sharpened the human-authored set
to *falsification criteria*; the Adequacy Criterion is by construction the one field that
says nothing about the hypothesis, so a signature on it certifies what the signer's
authority does not reach. Worse, it is a **false defence** — the reason to want a check on
adequacy is that an agent authoring its own bar can set it low, and a signature only guards
that if the signer can evaluate the control, which is the expertise being delegated. #164
then removed the last candidate by making the Question agent-drafted too. The freeze is now
**ancestry throughout**, and #61's *"an Adequacy Criterion it did not write"* is secured by
ancestry and role — frozen at open, before the search, by a different party than the agents
searching against it — rather than by custody.

**7. Three refusals exist only to keep authority one level up.** `GOVERNOR_DECLARED`,
`RULE_DECLARED` and `REGISTER_DECLARED` refuse fields that would otherwise read as helpful.
Case `b` runs the **pre-#164 charter** — the format as this prototype first wrote it — and
it is now refused. That is the cheapest available regression test for a level shift.

**8. The gate cannot enforce the field that matters most.** #61 rules that accumulated
instrument failure is evidence about the **perspective**, that the inference is
core-directed, and therefore that **no agent may ever draw it** — the signal reaches Noah
through coverage reports and his own reading, or it reaches nobody. So the positive control
must be legible **at a stall**, months later, in aggregate, against nineteen others. That
requirement lands on `adequacy.rationale`, the one field the gate deliberately ignores
because it is prose. Machine-decidability and aggregate legibility pull in opposite
directions, and this is where the format stops being able to help.

## Open, and handed on

- **Numbering**: `NNN` is the Inquiry's issue number. Proposed and adopted in the worked
  example. After #164 this stopped being a filing preference — agents open Inquiries
  themselves, so concurrent directory-number allocation is a live collision, and the
  tracker is the only allocator both sessions can see.
- `axiom_if_carried` is prose until [#166](https://github.com/NGL321/mosaic/issues/166)
  fixes a formal language; [#165](https://github.com/NGL321/mosaic/issues/165) is what
  checks it. The field is a hook, deliberately not a design.
- `conjectures/README.md` has no owner. #164 ruled that nothing else from it needed a file,
  and this ticket owns `inquiries/` rather than its sibling.
