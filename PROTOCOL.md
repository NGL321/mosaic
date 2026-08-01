# Working protocol

How work enters this repository: what gets versioned, who may write what, and what
happens when two workers collide. `README.md` is the entry point and states the
human–machine boundary in summary; this document is the mechanical reference.

Mosaic runs concurrent agents against one repository, with a single human researcher.
Every rule below exists to keep that arrangement legible to an outside reader — not to
add ceremony.

---

## 1. Two tracks

The repository carries two independently versioned tracks.

- **Research track** — the programme itself: vocabulary, claims, evidence, notebook,
  ledger, and any artifact whose behaviour a recorded result depends on.
- **Tooling track** — the apparatus: hosting, sync, CI, notebook generation, this
  document, `README.md`, configuration.

The boundary is decided by one test, applied when the branch is created:

> **If this artifact changed silently, could a result already in the record become
> wrong?**
>
> Yes → research track. No → tooling track.

**Worked example.** A deterministic dataset generator is **research track**, despite
reading as a tool. Change its generation logic and every experiment citing those
datasets now describes data that no longer exists. The same holds for analysis
pipelines, seed handling, and any scheduler whose ordering can reach a result. The
tooling track is smaller than "tooling" sounds: it is the apparatus that can garble the
record but cannot falsify a result.

Tags carry their track: `research-v0.2.1`, `tooling-v0.1.0`.

---

## 2. Versions

`main` is the programme's **current state of belief**, not its published state.
Unverified work lands on `main` and carries its provenance tier with it; the warrant
discipline does the job that a merge gate would do worse, and does it as a graded,
auditable annotation rather than a binary.

Research-track versions are read through Lakatos:

| | Meaning |
|---|---|
| **MAJOR** | The **Hard Core** changed. Under the Negative Heuristic this is not supposed to happen — a major bump is an admission that the programme was refounded or abandoned. `0.x` is pre-charter; ratifying the charter is `1.0.0`. |
| **MINOR** | A **Protective Belt** rung was added, retired, or falsified. |
| **PATCH** | The **record** accreted: evidence landed, debt was discharged, vocabulary was written, corrections were made. |

Version bump and diff size are **uncorrelated by design**. A 457-line research document
is a PATCH — it landed evidence and changed no claim. A two-line edit that retires a
belt rung is a MINOR. The version answers the one question a reader cannot get from the
diff: *did the programme's commitments move, or did its evidence?* Unlike software,
Mosaic has no build to break; the contract is **commitment**, not compatibility.

**Side effect worth reading.** A history where MAJOR never moves, MINOR moves steadily,
and each MINOR is preceded by PATCHes that landed evidence is the shape of a
*progressive* problemshift. MINOR churn with no PATCHes underneath — belt rungs added to
absorb anomalies, with no new evidence — is a *degenerating* one. This is evidence for
the programme-health review, not the whole of it.

Tooling-track versions are ordinary: `feat:` bumps minor, `fix:` bumps patch.

### The scaffolding era — `0.x`

`0.x` is **pre-charter**, and §5's custody obligations are suspended inside it. Bounded
three ways, because a grace whose expiry its beneficiary controls is a rule that was never
written:

1. **It defers, never excuses.** A suspended obligation is filed as an issue labelled
   **`custody:deferred`**, and no such issue may be open when `1.0.0` is tagged. Nothing is
   forgiven; it is rescheduled, in the open, where a stranger can read the list and watch it
   fail to shrink.

   **A deferred obligation is not Verification Debt**, in exactly the sense §5 already
   distinguishes. Verification Debt (`debt:open`) is a derivation step the *programme* has
   not checked; it is discharged by learning and outlives the charter by construction. A
   deferred custody obligation is a *record-keeping* gap — a missing defence or session
   citation on an authored file — and it dies at the charter. Both live in issues; only the
   second blocks `1.0.0`.
2. **It covers only the unrecordable.** If the machinery to discharge an obligation existed
   when the commit landed, the obligation was *skipped*, not impossible, and the grace does
   not reach it. The grace is for the scaffolding era's missing mechanisms, not for haste.
3. **It never covers an agent deciding.** An agent identity committing an authored file is a
   violation in every era. No grace reaches §5's first sentence.

**Worked example.** The `record:` commits that landed Mosaic's vocabulary carry agent
co-authorship and a session trailer, but no defence — because the defence mechanism did not
exist when they landed, while the trailer already did. So the grace reaches the defence and
not the citation, which is bullet 2 doing its work: what the machinery could record, it
recorded. Each owes a defence pass before the charter can be ratified, and each is a
`custody:deferred` issue until it gets one (#37, #38, #39).

### Ratifying the charter — `1.0.0`

Ratification is the moment every deferred obligation comes due, which makes the end of `0.x`
load-bearing. So the tag is **computed, not chosen**.

> **The first experiment is the gate.** `1.0.0` may be tagged when there is a Protective Belt
> rung the programme intends to test, an experiment designed to test it, and every tool and
> protocol that experiment needs already present in the repository.

| | Criterion | Discharged by |
|---|---|---|
| 1 | **A closed Hard Core** | the Hard Core stated as a finite list, with the Negative Heuristic binding on it from that point. Closed, not complete: it may be *wrong*, but it may not be *pending*. |
| 2 | **A thin Protective Belt** | at least one rung, carrying its falsifier in Noah's own words (§5). Not the whole belt — one rung worth testing. |
| 3 | **Restatement-level grasp of every part** | the **competence floor** (§5), declared: an unaided, intuitive restatement of every aspect of the programme. **Rigour is not required here.** What is missing below is Verification Debt (`debt:open`), scheduled through the Curriculum, which by construction outlives the charter. Open debt does not block the charter; open `custody:deferred` does. |
| 4 | **An operational repository** | a restore path demonstrated **by restoring**, not by existing; and the programme's routine tasks runnable without improvisation. Nothing wider than those two things. |
| 5 | **A first experiment, designed and executable** | the experiment names the rung it tests, and the toolchain runs it end to end at least once, on trivial input if need be. Its **results are not required**. |
| 6 | **A public work product** | not new: §5's warrant table puts a public, human-authored deliverable on every MAJOR, and ratification is `core:`. An essay stating the programme and the direction intended for it satisfies this. |

**Why the experiment and not a checklist.** A checklist of intentions is satisfiable by
ceremony, and §5 argues at length that such a gate is worse than none — in the record it is
indistinguishable from the real thing. An experiment is not: it either exists as a runnable
design or it does not. It is also **diagnostic**, which a checklist is not. A Hard Core still
pending, a belt with no testable rung, a toolchain that cannot carry a run — all three
surface as *"I cannot state the experiment."* This is the falsifier argument of §5 applied to
the programme as a whole: demand the artifact whose vagueness is visible on the page.

**Why results are not required.** A charter that waits on nature's answer is not a
scaffolding gate; it is a research result, and it could be years or never. `1.0.0` claims the
programme is *equipped*, not that it is *right*. Executing the experiment once proves the
equipment. The answer belongs to the belt.

Criteria 1, 2, 5 and 6 are artifacts a reader can find; 3 and 4 are Noah's to assert. The
deferred set is mechanical:

```console
gh issue list --label custody:deferred --state open   →  empty
```

---

## 3. Commit types

Types map one-to-one onto bump levels, so the release bump is **computed** from the log
rather than judged at release time.

### Research track

| Type | Bump | Use |
|---|---|---|
| `core:` | MAJOR | Hard Core revision |
| `belt:` | MINOR | A Protective Belt rung added, retired, or falsified |
| `evidence:` | PATCH | Research output, verification results, experiment runs |
| `record:` | PATCH | Notebook, ledger, corrections, vocabulary |

### Tooling track

| Type | Bump | Use |
|---|---|---|
| `feat:` | minor | New capability |
| `fix:` | patch | Repair |
| `chore:` | none | Config, formatting, ignores |

**Release bump = the highest level appearing since the last tag.**

**Vocabulary is `record:`, not `belt:`.** A definition is not a claim — there is no
falsifier for *Extraction*, because it is the language claims are made in. `belt:` is
reserved for rungs that have falsifiers, which keeps the MINOR gate (§5) meaningful: it
fires only where a falsifier can exist. Vocabulary that revises the Hard Core is `core:`.

### Squashing

> **Squash within a type. Never squash across types.**

Squashing a `belt:` into an `evidence:` destroys the bump computation and buries the
moment the programme's commitment moved — the most important thing the log records.
Collapsing an agent's twelve working commits into one `evidence:` loses nothing,
provided the message enumerates the sub-actions.

---

## 4. Branches

| Class | Lifetime | Owner |
|---|---|---|
| `research/` `grilling/` `prototype/` `task/` | Dies on merge | Exactly one — the ticket's assignee |
| `inquiry/<name>` | Persists | Shared, under sync discipline |
| `tooling/<slug>` | Dies on merge | Whoever is doing it |

Ticket-branch prefixes are wayfinder's ticket types, so a branch name says which skill
produced it and which ticket to read. Nothing extra to remember.

**Ownership needs no new mechanism.** Wayfinder already requires claiming a ticket by
assigning it before any work begins. A branch's owner *is* the ticket's assignee, and
**nobody else commits to a claimed branch**.

Branches are named for **work, never for workers**. A branch named `agent/<id>` cannot
be wrong about its contents, so it silently absorbs whatever that session touched and
never signals contamination. Naming by work is what makes a collision visible.

**`inquiry/` is the long-lived class** — a subprogram or empirical line that persists and
contributes back whenever it has something worth logging. Long-lived *identity*, short-lived
*divergence*: it merges `main` in continuously, and it is the class most likely to produce
a hard collision. It cannot hold the single-owner rule, so it holds sync discipline
instead: **merge `main` before you push, always.**

---

## 5. Custody and warrant

Two rules, stated together because each is hollow alone.

### Custody — whose hand

- **Authored files** — `CONTEXT.md` and the charter, which lands at `CHARTER.md` in the
  repository root: **human only.** Agents propose exact replacement text in a ticket or
  pull request; the human applies it. The charter's path is named here, before it is
  written, because the custody check keys on paths: a charter under any other name would
  leave that check green and covering nothing.
- **Record files** (research documents, notebook entries, ledger rows, experiment
  output): agent-writable.
- **Gate artifacts are record, not belief.** A checker agent's critique of a falsifier
  draft, and a teach-cycle transcript, are agent-written and land in the record even
  though their *subject* is belief. **Custody follows the file, never the topic.**

> **Custody is over the decision, not the keystrokes.**

Which term, which carving, which departure gets marked is Noah's. The prose that renders
that decision may be drafted with an agent holding the pen — that is what the first bullet
above already prescribes, and it is how most of the vocabulary was in fact written. An agent
**deciding** the vocabulary is the breach. An agent **wording** a decision Noah made is the
sanctioned pipeline, and forbidding it would forbid the protocol's own instruction.

A `Co-Authored-By:` trailer on an authored file is therefore **not a violation**. It is a
routing signal: it triggers obligations rather than convicting the commit. Three obligations,
each checked where it can be:

| | Obligation | Checked by |
|---|---|---|
| **Identity** | an authored file is committed under a human identity | CI, in one command, once agents commit under their own identity |
| **Citation** | an agent co-author on an authored file carries a `Session:` trailer resolving in the Transcript Archive | CI, **for presence only** — resolution is not checkable from a public runner against a private archive, and is unmechanised |
| **Defence** | a meaning-changing commit to an authored file carries a defence artifact — what changed, why, in Noah's own words | a checker agent, on the pull request, as the §5 gate below already works |

An obligation the scaffolding era defers (§2) is not dropped — it is filed as a
`custody:deferred` issue and blocks `1.0.0` until discharged.

The de minimis exception (§6) carries over unchanged, and is what keeps the defence
obligation affordable: a change that cannot alter meaning owes nothing further.

**The session trailer's spelling is pinned here**, because a document and a checker that
disagree about a key produce a check that convicts correctly cited commits — which is
exactly what happened on the first draft of this section's CI.

> The canonical key is **`Session:`**. A tool-specific prefix is equally valid — the
> trailer `Claude-Session:` that Claude Code emits is what every agent-co-authored commit
> in this repository actually carries. The check accepts `Session:` and any
> `<Tool>-Session:`, and nothing else.

**This file is not an authored file, and that is a decision, not an omission.** `PROTOCOL.md`
is agent-writable, and this section was drafted by an agent — the rule about who may decide
was worded by the party it constrains. That is tolerable only because the protocol is
*procedure*, reviewable line by line against whether it works, and because every change to it
lands through a pull request Noah merges. The vocabulary is not like that: a definition cannot
be checked against anything outside the belief it encodes, which is why `CONTEXT.md` and the
charter are human-only and this file is not. If that argument ever stops holding, the fix is
to move `PROTOCOL.md` into the authored set and re-derive it under custody, not to leave the
question unasked.

**Why not simply forbid the trailer.** Because typing is not the claim worth making. Noah can
type every character of a definition and still only be reciting it, and a rule that passes
that commit while convicting a monitored, cited, defended one is measuring the wrong thing —
strictly, it is *wrong in both directions at once*. Custody can only ever answer **whose
hand**; whether the text can be defended is warrant's question, and the table above is where
the two rules meet.

*"The vocabulary was written by the model"* is the form the credibility objection takes
against an openly LLM-accelerated programme. The honest answer is not that no model touched
it — it did — but that every place one did is recorded, traceable to a session, and
accompanied by a defence Noah wrote. That answer is stronger than a denial, and unlike a
denial it is true.

### The competence floor — where defence stops

Defence is unbounded until the programme says where it bottoms out. The **competence floor**
is Noah's declared statement of what he can defend unaided; it is an authored file's content
and so must be written by him, unassisted, which is the one place custody's strictest reading
belongs. An agent co-authoring a root assertion about Noah is circular.

- Defence terminates **at the floor**, not at first principles.
- Whatever a derivation needs from below the floor is **Verification Debt** — filed as a
  `debt:open` issue and discharged the way #5 settled it: a document in `docs/research/`
  plus the commit promoting the tier. It is not a custody failure, and it does not block the
  charter.
- Until the floor is declared, the defence obligation is **undecidable rather than
  satisfied**. The deficiency reports itself instead of being papered over.

Verification Debt has always presupposed a floor: *"a logged step Noah cannot yet defend
unaided"* is measured against one. Declaring it gives the ledger its zero point.

### Warrant — whose understanding

| Commit level | What the human must produce |
|---|---|
| `record:` / `evidence:` | Nothing. Verbatim transcription of an agent's proposal is fine. |
| `belt:` (MINOR) | **The falsifier, in their own words**, drafted before merge. |
| `core:` (MAJOR) | **A public, human-authored work product** — publication, essay, something externally addressed. Agents may not open a MAJOR ticket; they may report anomalies that pressure the Hard Core. |

A gate satisfiable by ceremony is worse than none, because in the record it is
*indistinguishable* from the real thing — a commit message written after skimming looks
exactly like one written after thinking. The gate must demand an artifact hard to
produce without the comprehension. A falsifier qualifies: it is not an extra
deliverable but the rung's minimum content, vagueness is visible on the page, and it is
auditable later against whether the rung was actually retired when the falsifier fired.

**The gate is an instrument, not a filter.** The human submits a *draft*. A checker agent
grills it, and — critically — **the checker must not be the producing agent**, which knows
the answer and cannot distinguish the human's understanding from its own priors. On
failure it diagnoses which failure:

- *Understands, expresses poorly* → coaching toward better expression, by analogy.
- *Does not understand* → a **teach cycle** (`.claude/skills/teach/`), from what the human
  does understand up to what the artifact requires.

So the gate can never be routed around by lowering the bar: failing it produces work
rather than a rejection. **Being unable to write the falsifier is the comprehension
ceiling reporting itself** — the measurement firing, not friction to route around.

**The loop's outcome is data.** A MINOR that took three teach cycles is a recorded fact
about where the ceiling sits, and is Curriculum input. Verification debt says what the
*programme* has not checked; failed explanation gates say what the *researcher* cannot yet
carry. Different deficits, both scheduled.

### Why both

Custody without warrant is **transcription** — the human pastes agent text, the identity
check returns one name, and the claim is true and empty. Warrant without custody leaves the
vocabulary agent-owned with a human signature on top. Custody governs vocabulary;
warrant governs claims. Neither category is ungoverned, and neither gate is applied
where it has nothing to bite on.

This is why custody's third obligation is a *defence* and not an attendance claim. An
attendance trailer would be asserted by the one party whose attendance is in question —
free to write, indistinguishable from the truth, and so exactly the ceremony this section
argues against. A defence is asserted by the same party, but it cannot be produced without
the comprehension it claims, and its vagueness is visible on the page.

---

## 6. Merges

**Every branch merges through a pull request, on both tracks.**

> A reviewer other than the author is required when the author is an **agent**, or the
> contributor is **external**.

Ceremony uniform, scrutiny proportionate: a `.gitignore` fix is a pull request opened and
self-merged in seconds; an agent-built dataset generator sits until someone reads it.
Review exists to catch what the author cannot see, which is orthogonal to whether the
artifact is cited by the record.

**An agent is never the reviewer of record for its own output.** It may respond to review
and repair its own work. It cannot independently assess reasoning it generated.

- PATCH-level research: a fresh agent may review; the human merges.
- MINOR / MAJOR: the human, through the §5 gate. The draft goes on the pull request, the
  checker agent grills it there, and the teach cycle, if it fires, happens in that
  thread — which makes the human–machine boundary **visible in the record** rather than
  advertised in a README.
- **Any pull request touching an authored file**, at whatever level: the defence artifact
  (§5) goes on the thread and is grilled there, by an agent that did not draft the text. A
  `record:` change to `CONTEXT.md` is PATCH by §3 and still carries this, because the
  obligation follows the *file*, not the bump.

**Never rebase a pushed branch.** `inquiry/` branches take `main` by merging it in. This
produces uglier history, and the ugliness is correct: rebase rewrites *when* something
was known, and a programme whose asset is an auditable record of what it believed and
when cannot afford a history that lies about chronology to look tidy. Same reason as the
squash rule.

### Revisions during review

**The branch owner applies feedback, as new commits.** Never by amend or force-push: a
review thread whose commits have been rewritten no longer refers to anything, and the
prohibition above applies to every pushed branch without exception. Threads resolve by
citing the SHA that addressed them.

**De minimis exception.** The human researcher may commit directly to a branch under
review for changes that **cannot alter meaning** — spelling, punctuation, typography,
formatting, broken links. Round-tripping a misspelt name through an agent is overhead
with no reviewer benefit. The test is strict:

> *If the change could alter what a reader takes the text to claim, it is not de minimis.*

Bounded three ways:

- It runs **one direction only** — the human writing on an agent's branch, never the
  reverse. Agents do not acquire de minimis access to authored files. Custody's identity
  obligation (§5) has no exceptions, because a single exception makes the check stop being
  an answer to anything. What de minimis exempts is the *defence* obligation, and only
  because the test above already establishes that nothing was claimed.
- The change is a **separate commit**, never amended into the author's work, so
  authorship in the log stays truthful about who wrote what.
- Anything failing the test goes back to the owner as a request, however small it looks.
  "Small" and "cannot alter meaning" are different claims, and only the second one counts.

**Substantive revision re-fires the gate.** If review changes what a `belt:` claim
asserts, the falsifier drafted before review no longer covers the claim being merged, and
§5 runs again on the revised version. Otherwise the gate could be satisfied by a draft
and the merge carried by something else.

### Merge commits

**Always `--no-ff`**, including single-commit branches: a pull request is a unit of work
and history should show it as one. **Squash-merge is never used** — it collapses across
commit types by construction, which §3 forbids for the same reason.

The merge commit takes **the highest commit type on the branch**. This makes
`git log --first-parent main` the programme's changelog, and puts the version bump at
trunk level where it can be read without descending into branches.

```text
record: fill the research substance section of CONTEXT.md (#21)

Resolves #2, #15. Applies the corrections from #13.

Bump: research PATCH
```

- **Subject** — `<type>: <what landed> (#PR)`.
- **Body** — the tickets closed, and the one-line gist that also goes to the ticket
  resolution and the map's *Decisions so far*. Written once, used three times.
- **`Bump:`** — track and level, **stated rather than inferred**. §3 computes the release
  bump from commit types; stating it here means a mistyped commit shows up as a visible
  contradiction between the merge commit and the branch it landed, instead of being
  silently miscounted at release time.

---

## 7. Collisions

> **Unpushed collisions are reconstructed. Pushed collisions are split, never rewritten.**

The line is `git push`. Before it, history is a draft: discard the malformed commits and
re-commit the tree onto correctly named, correctly typed, singly-owned branches from
`main`. After it, history is part of the record — an agent may have pulled it, a pull
request may cite it — and it gets corrected by **adding** commits, not rewriting them.

Reconstruction backs the affected file contents up outside the repository first, and
retains the original branch under `backup/` until the replacement branches have merged.

Most collisions are prevented rather than recovered, by three rules already stated:
single-owner branches (§4), short divergence (§4), and human-only authored files (§5) —
which makes the contended-file collision structurally impossible for `CONTEXT.md`.

---

## 8. External contributions

**The gate lifts.** External work used to sit unmerged pending this policy. It now merges
on a checklist, half of it automated:

> An external contribution merges when it **arrives as a fork pull request**, carries
> **`Signed-off-by:` on every commit it adds**, **touches no authored file**, and has
> **passed review**. Nothing else.

### Where the boundary is

**External means the fork boundary, and nothing else.** Work arriving through this repo's
own branch and pull request flow (§4) is internal whoever or whatever held the pen — Noah,
and agents operated out of this repo through the same pipelines. Work arriving as a fork
pull request is external.

That keys the rule to a fact CI can read rather than to a judgement about authorship, and
it is why internal work is exempt from the sign-off: §5's custody trailers already answer
*whose hand* far more precisely than a `Signed-off-by:` would, and adding one would be
ceremony.

### Licensing and provenance

**Licensing splits by artifact kind, not by track** — MIT for code, CC BY 4.0 for the
prose record. §1's research/tooling test asks whether a silent change could falsify a
recorded result, which is a question about falsifiability and has nothing to do with
copyright: a dataset generator is research track and still MIT, and this document is
tooling track and is CC BY. The path table lives in `README.md` and is not restated here.

**Inbound = outbound.** A contributor licenses each file under whatever that file's path
already carries — touch `tools/`, MIT; touch `docs/research/`, CC BY. The table does
double duty, which is the sign it was carved right. This binds prose contributions too;
the origin claim matters *more* for a paragraph of research writing than for a bug fix.

**DCO, not a CLA.** A CLA's only real payoff is relicensing, which the split forecloses,
and there is no entity to assign rights to. `Signed-off-by:` — `git commit -s` — joins the
trailer mechanism §5 already runs on rather than adding a parallel one.

**No fourth provenance tier, and no third custody category.** The tiers measure *Noah's*
warrant, not authorship, so an external contribution lands at the bottom tier until he
does the reading: **someone else's verification is not verification**, which is #5's
*"agent verification is not verification"* generalised. And §5's *"human only"* means
Noah, not any human — so an external contributor sits exactly where an agent sits. A fork
pull request touching an authored file is refused on custody grounds however good it is,
and the contributor proposes exact replacement text in the thread, through the identical
channel §5 gives agents. Record files are open to them, subject to review.

### Review

Review inherits §6's agent rule, because the paragraph above puts external work in the
agent's seat.

- A **reviewer is always required, and is always Noah.** A contributor never merges their
  own pull request.
- **Research-track external contributions additionally get a checker agent** that did not
  produce the work — the second pair of eyes agent-authored apparatus already gets.
- External work does **not** fire §5's falsifier gate. A tool is not a claim. If merging
  it later enables a claim, that claim carries its own warrant obligations, unchanged.

### Credit

A tool whose silent change could falsify a recorded result is *apparatus* by §1's own
test, and apparatus gets cited in a methods section. So an outside author has a claim on
the research record, not merely on `git log`.

- **Baseline, every contribution:** git history plus the licence's notice requirement.
- **Where a recorded result depends on external apparatus,** the experiment record names
  the tool and its author, methods-section style. Where that field sits belongs to the
  record format; the obligation is fixed here.
- **Minor contributions earn no research citation.** The obligation binds only where a
  recorded result depends on the contribution.
- **No `CONTRIBUTORS.md`.** It decays into a thank-you page and is a second list to keep
  in sync with `git log`, which already holds the data.
- **Citation, never authorship.** Co-authorship follows intellectual contribution to the
  *claim* — a conversation held directly, never an entitlement this policy confers.
  Substantive research collaboration is arranged out of band, and the programme is
  reorganised then to accommodate it.

### What CI enforces

`.github/workflows/contribution.yml` checks the mechanical half — fork detection,
`Signed-off-by:` on every commit the pull request adds, and the authored-file
prohibition — so the only human step is judging the content. It **runs unconditionally
and skips internally**, which is what lets it be a *required* check: a path-filtered
workflow never runs on pull requests touching nothing in `paths:`, and a required check
that never runs sits *expected* forever and blocks the merge. It **reuses
`custody_check.py`'s `AUTHORED` set** rather than declaring a second copy of the authored
file list, because that script already cross-checks its set against its workflow and exits
2 on drift, and a third copy would unlearn the lesson.

`CONTRIBUTING.md` carries the checklist and nothing else, because GitHub surfaces it in
the pull request composer — reaching the contributor at the moment they contribute. This
section is the decision of record; restating it there would create a second copy to keep
in sync.
