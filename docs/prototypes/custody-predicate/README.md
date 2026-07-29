# PROTOTYPE — what does §5 custody claim, and what checks it?

Throwaway. Ticket [#23](https://github.com/NGL321/mosaic/issues/23). Not part of the record.

```console
python docs/prototypes/custody-predicate/prototype_tui.py
```

## The question

`PROTOCOL.md` §5 claims authored files (`CONTEXT.md`, the charter) are human-only, and
offers one mechanical check: `git log --format='%an' -- CONTEXT.md → one name`. The command
does not work today, and [#24](https://github.com/NGL321/mosaic/issues/24) will make it
*work* without deciding *what it should say*. Three readings are on the table, and they are
**not nested** — each convicts commits the others acquit:

| | Reading | Violation is… |
|---|---|---|
| **A** | the human **typed** it | an agent co-author trailer on an authored file |
| **B** | the human **authored** it, agent as amanuensis | an *unattended* session committing an authored file |
| **C** | the human **understood and endorsed** it | nothing, at the file level — custody collapses into warrant |

`custody.py` is the decision procedure for all three, as pure predicates over one commit.
It is the bit worth keeping: whichever reading wins becomes the CI check, and the TUI is
thrown away.

## How to drive it

`[n]`/`[p]` walk the case library — first this repository's **real** `CONTEXT.md` history
(loaded from `git log` at startup, read-only), then synthetic hard cases. The toggles mutate
whichever case is on screen, so any case can be pushed into any corner; `[r]` restores it.

Watch for the disagreements. The ones that matter:

- **The two `record:` commits that landed the vocabulary.** A convicts them, B cannot rule
  on them at all, C never looks. This is the ticket's uncomfortable consequence, on screen.
- **Human types the vocabulary unaided but cannot defend a word of it.** A passes it, C
  convicts it. The readings are not a strictness ordering.
- **Agent writes a research document.** All three acquit — custody follows the file, never
  the topic (§5), and this is the case that keeps that rule visible.

## Two verdicts beyond pass/fail, which turned out to be the point

`UNDECIDABLE` means the policy needs a fact git does not carry. `VACUOUS` means the policy
applies and demands nothing. Both are failures of the thing §5 exists to provide — an
unverifiable authorship claim is what a sceptical reader discounts — so the frame's last
block asks the question directly: **can a stranger check this with one command?** A can.
B needs an attendance trailer that does not exist. C's artifact lives on a PR thread,
outside the history.

## Not in scope

No persistence, no tests, no CI wiring. The prototype does not decide anything — it makes
the three readings disagree out loud so the decision can be made against cases rather than
against prose.
