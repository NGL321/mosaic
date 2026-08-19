# PROTOTYPE — what a factored Operation looks like on disk

Ticket [#224](https://github.com/NGL321/mosaic/issues/224), on
[Map: The Operation set](https://github.com/NGL321/mosaic/issues/220). Built to be thrown
away, and retained as a **primary source** for how the source format was chosen — not as a
tool. Nothing runs it, nothing depends on it, and it never touches GitHub, git, or the
network.

```console
python docs/prototypes/operation-format/prototype_tui.py
```

- `source/` — the factored form. `classes.yaml`, `intents.yaml`, `glossary.yaml`,
  `fragments/` (the spine, written once) and `operations/` (four cells: three ruled in,
  one ruled null). Three files were added later by [#228](https://github.com/NGL321/mosaic/issues/228):
  `derivations.yaml` (the arithmetic — every null, actor column and defence obligation a
  flag can predict), `couplings.yaml` (the six couplings visible now, staged until their
  cells exist) and `gaps.yaml` (named gaps, declared per class).
- `render.py` — the generator. The whole claim is in `flatten()`.
- `out/` — the flat form: what an actor is actually handed. **This is the artifact the
  acceptance test judges**, and nothing else is.
- `prototype_tui.py` — eight cases. `c` is the hard cell; `t` is the one that breaks
  something; `n` and `x` are the null and the absence, side by side; `f` is premise 10
  shown rather than argued.

## The question

#224 asks what a factored Operation looks like on disk, how a Procedure is attached to it,
and what renders. Its instruction was to discover the format by writing entries rather than
by holding the axis enumerations first, against three maximally different Operations:
`add-a-CONTEXT-entry`, `regenerate-curriculum/open.md`, and one tracker Operation where the
artifact is not a file.

The three were written as `add@CONTEXT-entry`, `regenerate@curriculum-open` and
`file@debt-issue`. A fourth, `add@curriculum-open`, appeared while writing the second and is
the reason premise 18 needed testing at all.

## The shape that came out

Five files, four layers, and one function.

| Layer | Holds | Premise |
|---|---|---|
| `classes.yaml` | artifact classes and their flags | 4 |
| `intents.yaml` | the intent axis | 2 |
| `glossary.yaml` | terms an entry uses | 10, applied to vocabulary |
| `fragments/` | spines written once, parameterised — **Procedure** spines, plus `issue.yaml`, a **class** fragment (#227) | 10 |
| `operations/<intent>@<class>.yaml` | the cell: Operation, actors, Procedure, couplings | 1, 2, 3, 9, 18 |

A cell separates cleanly into `operation:` (postconditions, actors, whose decision) and
`procedure:` (steps, executors, tooling). **Nothing under `operation:` in any of the three
cells names git, GitHub, `gh`, a branch or a pull request** — premise 1 held without being
enforced, which is the useful result: the separation was not hard to maintain, it was hard
to violate.

`<intent>@<class>` as a filename is the identity, and it doubles as the redirect target a
null and an actor refusal both point at. No counter appeared anywhere and none was wanted.

## What the prototype found

**1. Premise 4's third flag collides with custody, and both need the word "authored".**
Custody asks who may hold the pen; origin asks what put the bytes there. All three live
combinations exist in this repository — `CONTEXT.md` is human-only *and* authored,
`PROTOCOL.md` is agent-writable *and* authored, `curriculum/open.md` is agent-writable *and*
generated. One flag cannot carry it. Split here as `custody:` and `origin:`.

**2. `intent × class` strained in exactly one place, and it is a real one.** An agent may
file a `debt:source` on its own authority; a `debt:verification` asserts what Noah cannot
yet defend unaided, which is a claim about him. Same intent, same location, same three
flags — **different actor ruling**. So either the two labels are two artifact *classes*, or
the actor column needs a condition and stops being a column. Carried to
[the hard cells ticket](https://github.com/NGL321/mosaic/issues/228); it is precisely that
ticket's ~8 pairs arriving early.

**3. The tracker surface inherits nothing, and nothing replaces it.** Writing
`file@debt-issue` dropped `PROTOCOL.md` §4's branch spine and §6's merge spine entirely —
no branch, no pull request, no review, no custody check, no reviewer of record. Five of the
prototype's seven filed gaps are on that one cell. The repository surface has three sections
of protocol; the tracker surface has none.

**4. Premise 9 works, and it works by being annoying to fill in.** Seven steps across three
Operations have `executor: none`. Each was filed by being unable to type a name into a
required field — not by anybody auditing anything. Two are new:

- `tools/snapshot_debt.py` has a `--check` mode whose docstring says *"for CI"*, **and no CI
  calls it**. The snapshot goes stale silently.
- Nothing at all fires the regeneration. `curriculum/open.md` refreshes when somebody
  remembers, which is [#198](https://github.com/NGL321/mosaic/issues/198) on a second
  surface.

**5. The coupling premise 18 predicted is here, not in Drive.** *A debt-issue `file`
requires a curriculum-open `regenerate`* — a legal action on the tracker carrying an
obligation in the repository. Filed as a null it would have deleted a legal action; it needs
its own field, and it renders on both cells because both actors need to see it.

**6. A null has to be a file.** `add@curriculum-open` is ruled out with a reason and a
redirect. `edit@CONTEXT-entry` simply has no file. Case `x` puts the two beside each other:
they route differently — a null **refuses**, an absence is a **mint** — so the catch-all
([#230](https://github.com/NGL321/mosaic/issues/230)) cannot tell them apart unless a
ruling leaves a physical artifact. An absent cell must mean *nobody looked*, always.

**7. Writing the spine found `record/` mechanically.** Substituting `{prefix}` into §4's
branch table found no cell for the six branches that use `record/`. The map already carries
this as fog; the point is that filling in a required field is what surfaced it.

## The acceptance test — premise 16

Run, not reasoned about. Two rendered entries were handed to two fresh agents holding **no
other context**, forbidden to read files or run commands.

**The entry an agent may execute** (`regenerate@curriculum-open`). It acted: produced the
branch command with the ticket substituted, ran the tool, committed, opened the pull
request, and stopped at `review` — the first step that is not its own — correctly, without
being told where to stop. **Premise 16 passes.** It then named three things the entry did
not give it, and all three were format defects rather than content defects:

1. **No failure route.** Exit 3 was defined and unrouted: *"it tells me what it means and
   not what to do."* Steps now carry `on_failure:`.
2. **No commit-message shape** for the working commit — only for the merge commit — so it
   invented one.
3. **A step that was true but not executable.** *"Confirm you are the ticket's assignee"*
   with no mechanism was the first thing it would have left the entry to find out.

**The entry an agent may not execute** (`add@CONTEXT-entry`), handed a user request to write
a vocabulary entry. It **refused, cited custody, and redirected to `propose@CONTEXT-entry`**
from the entry alone. Premise 3's separate `propose` intent is doing visible work: the
refusal is not a dead end, it is a route. Two further defects:

4. **Inputs were assumed, not handed.** `<ticket>` appears in a command and nowhere in the
   entry as something you must be given. Cells now declare `inputs:`.
5. **Undefined vocabulary leaks the reader out of the entry.** It used *competence floor*
   and *Provenance Tier* undefined, and the agent reported the pull to go open
   `PROTOCOL.md`. **That pull is the premise-16 failure** — an entry that sends you
   elsewhere to understand it has not been flattened, only shortened. Terms became a fourth
   factored layer.

All five were absorbed and re-rendered; the diff is in this branch's history, and the
sections marked `ADDED AFTER THE ACCEPTANCE TEST` in `source/` are exactly them.

**What the test costs is about ninety seconds**, and it found five format defects that
reading the format did not. Premise 16 should be run on every entry, not on a sample.

## What this does not settle

The intent axis. `intents.yaml` stops at five intents on purpose —
[#226](https://github.com/NGL321/mosaic/issues/226) owns it, and enumerating it here would
have been the thing #224 was written to avoid.

**`classes.yaml` is no longer a prototype.** [#227](https://github.com/NGL321/mosaic/issues/227)
enumerated the artifact axis in full: 42 classes over five flags — `track`, `custody`
(three values, not two), `origin` (three, not two), `facing`, `mutability` — plus the typed
address `locate{surface, path, licence}`. `defence` left for #226 as a property of the
intent. The file's own header carries the argument. Nothing above depends on the axes being
complete; finding 2 is the only place the *key* is at risk, and it is stated as a question
for [#228](https://github.com/NGL321/mosaic/issues/228) rather than answered here.

## Amended after #224

This prototype was built to be thrown away and has instead been amended twice, which is
itself the finding: the source format survived two enumerations landing on top of it.

- [#227](https://github.com/NGL321/mosaic/issues/227) filled `classes.yaml` — 42 classes,
  five flags, a typed address — and minted the first **class** fragment, `issue.yaml`.
- [#228](https://github.com/NGL321/mosaic/issues/228) worked six hard cells against it.
  The key held. It added `derivations.yaml`, `couplings.yaml` and `gaps.yaml`; ratified
  `trigger:` and `couples:`, which #224 had invented ad hoc, as required fields with
  rules; minted `enforcement:`; and added three classes the location sweep could not see —
  `pull-request`, `review-record` and `defence`.

**The four cells in `operations/` are stale against `classes.yaml` and `render.py` no
longer runs.** `add@CONTEXT-entry` names a class #227 renamed to `vocabulary-entry`, and
`file@debt-issue` names an intent #226 collapsed and a class #227 split in two. This was
true before #228 and is left alone deliberately: renaming them is transcription against a
now-settled model, and premise 15 batches execution at the end. The cells remain readable
as the primary source they were retained to be.
