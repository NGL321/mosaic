# DRAFT — proposed text for `PROTOCOL.md` §2

Not applied. Exact replacement text, for review — per §5, agents propose and the human
applies. Drafted 2026-07-29 from the researcher's statement of what `0.x` owes. The
prototype's `may_ratify()` implements it, so the criteria can be driven before they are
prose.

Insert as a new subsection at the end of §2 (Versions), after the *Side effect worth
reading* paragraph.

---

### Ratifying the charter — `1.0.0`

`0.x` is the **scaffolding era**, and §5's obligations are suspended inside it — *deferred*
into the ledger, never excused, because a suspension nobody has to discharge is a rule that
was never written. That makes the end of `0.x` load-bearing: ratification is the moment
every deferred obligation comes due. So the tag is **computed, not chosen**.

> **The first experiment is the gate.** `1.0.0` may be tagged when there is a Protective
> Belt rung the programme intends to test, an experiment designed to test it, and every tool
> and protocol that experiment needs already present in the repository.

| | Criterion | Discharged by |
|---|---|---|
| 1 | **A closed Hard Core** | the Hard Core stated as a finite list, with the Negative Heuristic binding on it from that point. Closed, not complete: it may be *wrong*, but it may not be *pending*. |
| 2 | **A thin Protective Belt** | at least one rung, carrying its falsifier in Noah's own words (§5). Not the whole belt — one rung worth testing. |
| 3 | **Restatement-level comprehension of every part** | the **competence floor**, declared: an unaided, intuitive restatement of every aspect of the programme. **Rigour is not required here.** Whatever is missing is Verification Debt, scheduled through the Curriculum, which by construction outlives the charter. |
| 4 | **An operational repository** | a restore path demonstrated **by restoring**, not by existing; and the programme's routine tasks runnable without improvisation. |
| 5 | **A first experiment, designed and executable** | the experiment names the rung it tests, and the toolchain runs it end to end at least once. Its **results are not required**. |
| 6 | **A public work product** | already required, and not new: §5's warrant table puts a public, human-authored deliverable on every MAJOR, and ratification is `core:`. An essay stating the programme and the direction intended for it satisfies this. |

**Why the experiment and not a checklist.** A checklist of intentions is satisfiable by
ceremony, and §5 has already argued that a gate satisfiable by ceremony is worse than none —
in the record it is indistinguishable from the real thing. An experiment is not: it either
exists as a runnable design or it does not. It is also **diagnostic**, which a checklist is
not. An experiment that cannot be written down reports *which* criterion is actually missing
— a belt with no testable rung, a Hard Core still pending, a toolchain that cannot carry a
run, all surface as *"I cannot state the experiment."* This is §5's falsifier argument
applied to the programme as a whole: demand the artifact whose vagueness is visible on the
page.

**Why results are not required.** A charter that waits on nature's answer is not a
scaffolding gate — it is a research result, and it could be years or never. What `1.0.0`
claims is that the programme is *equipped*, not that it is *right*. Executing the experiment
once, even on trivial input, is what proves the equipment; the answer belongs to the belt.

**Why `0.x` cannot be extended indefinitely.** The grace's expiry is otherwise the one thing
its beneficiary controls, which makes every suspended rule optional in practice. Criteria 1–6
are the forcing condition. Their state is a fact about the repository, publicly visible, and
a stranger can watch the list fail to move.

---

## Where `0.x` stands today

Read off the repository, 2026-07-29. Criteria 3 and 4 are Noah's to judge; the rest are
visible from the tree.

| | Criterion | State |
|---|---|---|
| 1 | closed Hard Core | **partial** — `CONTEXT.md` states two axioms (Least Action, Scale Corollary); whether that list is *closed* has not been declared |
| 2 | thin belt | **not met** — `CONTEXT.md` defines *Protective Belt* but states no rungs |
| 3 | restatement-level grasp | **not met** — no competence floor is declared anywhere |
| 4 | operational repository | **not met** — no CI, no demonstrated restore; #24 outstanding |
| 5 | first experiment | **not met** |
| 6 | public work product | **not met** |

Plus the deferred obligations the prototype finds: **5 commits touching `CONTEXT.md`**, each
owing a defence pass, and the two carrying agent co-authorship also owing a retroactive
session citation.

## Two places this draft goes past what was said

1. **"Results are not required"** is a sharpening, not a quotation. The statement was that
   the experiment is one you *are trying to conduct*, and the tools to conduct it exist. I
   read that as designed-and-runnable, and made the smoke execution the proof of criterion 4
   rather than requiring an outcome. If ratification should instead wait on a first result,
   criterion 5 changes and the charter's date becomes unpredictable by design.
2. **Criterion 4 is an interpretation.** "Seamless", "autonomous", and "no accidental
   deletion without restore" do not mechanise as stated, so they are rendered as two
   testable things: a restore demonstrated by performing one, and routine tasks runnable
   without improvisation. That is narrower than the intent. Anything else meant by
   *seamless* needs naming, or it will not survive into the check.
