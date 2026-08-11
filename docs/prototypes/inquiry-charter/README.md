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
- `gate.py` — the dispatch gate. Twelve named refusals, each structural or checked against
  git; none of them reads prose for meaning.
- `prototype_tui.py` — breaks the charter one field at a time so each refusal can be *made
  to happen* rather than described.

## The question

#60 asks what the charter contains and what the dispatch gate checks before a run starts.
Premise 2 of the map says an Inquiry with no hypothesis-blind Adequacy Criterion **cannot
be dispatched AFK** — "a visible refusal, and itself a finding about the Inquiry."
Everything here is an attempt to make that sentence mechanical, under `#26` R6's warning
that **a rule satisfiable by writing a word is not a rule**.

## What the prototype found

**1. Hypothesis-blindness is enforceable by *scope*, and not by inspection.** No checker
can read an Adequacy Criterion and decide whether it smuggles the hypothesis in. But it
can decide whether the `adequacy` block and the `hypothesis`/`discriminating` blocks share
a *name*. Declare the apparatus in two namespaces, require them disjoint, and the
criterion is blind by construction. An agent can still rename its way across the boundary
— and renaming is a visible diff on a frozen file, which is the point. Case 3 in the
driver is the real mistake this catches: tuning the apparatus against the very metric that
will be used to judge it.

**2. The ticket's `register policy` field must not exist.**
[#56](https://github.com/NGL321/mosaic/issues/56) made Register *derived from git ancestry,
never declared* — a property of a result, not of an Inquiry. A `register:` field in the
charter would be exactly the assertion [#63](https://github.com/NGL321/mosaic/issues/63)
exists to prevent, so the gate refuses a charter that carries one (case 6). The ticket
body listed it; the ticket body predates #56.

**3. "One file or two" is the wrong axis; the split is already made.** Premise 9 puts the
freeze in the repo and dispatch state on the issue, and that is the whole of it. Inside the
directory, custody is **per path**, not per file-pair: `README.md` is frozen and
human-signed, while `configs/`, `probes/` and `runs/` are agent-writable. No second file is
needed, because the agent-maintained progress part was never going to live in the
directory.

**4. The appearance of `config.yaml` *is* the freeze.** During Searching there is no
`config.yaml`, only candidates under `configs/`. When adequacy passes, the winning
configuration is committed to that path, and that commit is the freeze event — dated,
attributable, and an ancestor of everything measured afterwards. This gives
[#63](https://github.com/NGL321/mosaic/issues/63) its ancestry hook without asking anyone
to assert anything, and it fits `inquiries/README.md`'s existing layout rather than
amending it.

**5. A keyword scan for the Hard Core refuses the Negative Heuristic itself.** The gate
initially refused the charter as first written, because its `return` rule said *"return
immediately on any result bearing on the axioms"* — the honest statement of the mandatory
return, and indistinguishable by token from the thing the rule bars. The resolution is
that the mandatory Hard-Core return is **loop behaviour, not a charter field**: identical
for every Inquiry, never restated locally, and a charter that mentions the Hard Core is
making policy that is not its to make. That keeps the check a token scan, which is the only
kind of check that cannot be argued with.

## Open — for the ticket thread, not for this file

- Who authors the **positive control**? It is the freeze line, so it must be frozen and
  therefore Noah's; constructing one for a topological instrument is exactly the expertise
  being delegated.
- **Numbering.** Proposal: `NNN` *is* the Inquiry's issue number — allocated by the
  tracker, so two concurrent sessions cannot collide, and the directory names its own
  dispatch state. Cost: sparse numbers. Fan-out does not stress numbering at all, because
  a fan-out is many Runs of one Inquiry.
- What the refusal **emits**, and whether a refused charter is an Inquiry at all or a
  [Prospect](https://github.com/NGL321/mosaic/issues/109).
