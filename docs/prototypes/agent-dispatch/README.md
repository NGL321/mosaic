# PROTOTYPE — what decides that an agent runs

Ticket [#24](https://github.com/NGL321/mosaic/issues/24). Built to be thrown away, and
retained as a **primary source** for how the dispatch model was chosen — not as a tool.
Nothing runs it, nothing depends on it, and it never touches GitHub, git, or the network.

```console
python docs/prototypes/agent-dispatch/prototype_tui.py
```

## The question

#24 asks for asynchronous work to run "as automation, **triggered by and reported through
issue and pull-request comments**, under an identity that is not the researcher's," and
names four hazards it does not resolve: unbounded loops, prompt injection through comments,
secrets, and cost visibility.

This prototype takes the gate on its own: given an event, what decides that an agent runs,
what identity its commits carry, what it may read and write, whose money it spends, and
whether what it posts when it finishes triggers another one. Four things are switchable —
trigger model, runner, identity model, and the two footguns — so the hazards can be made to
happen rather than described.

## Why Sandcastle changed the answer

Noah proposed [Sandcastle](https://github.com/mattpocock/sandcastle) as the dispatcher.
Reading it (v0.12.0, 2026-06-29; retrieved 2026-07-30) produces two findings, and the
second is the more useful one.

**1. Sandcastle is not a dispatcher.** It is `run()` — a harness that puts an agent in a
sandbox, iterates it, collects its commits, and merges them back. It has no GitHub trigger,
no identity, and no opinion about who is allowed to start it. What it does give the seam is
real and worth having:

| | What it buys #24 |
|---|---|
| `promptArgs` | Untrusted text is substituted **before** shell expansion, and `` !`…` `` inside an argument value is inert text by construction — so issue bodies pass in as data, [documented as such](https://github.com/mattpocock/sandcastle#prompt-arguments-with-key). |
| `Output.object` | The agent's report is a **schema'd payload**, not stdout. What gets posted to the thread is fields, so a report cannot accidentally be a command. |
| `maxIterations`, `idleTimeoutSeconds`, `completionSignal` | The run is bounded from outside the agent. |
| `docker()` / `noSandbox()` | Isolation is a choice at the call site rather than a property of where it runs. |

**2. Its own repository already runs the pipeline #24 is asking for — and does not trigger
on comments.** `.github/workflows/agent-review.yml` and `agent-implement-pr.yml` fire on
`pull_request_target: [labeled]`, gated on `github.event.label.name == 'agent:review'`.
The workflow removes the label, adds `agent:in-progress`, runs `npx tsx` over a Sandcastle
script with `noSandbox()`, pushes with `--force-with-lease`, posts the structured payload as
a review, and on failure adds `agent:blocked` with a comment saying *"Re-add `agent:review`
to retry."*

That is a working answer to three of #24's four hazards, and it is not the design #24
describes. **The dispatch primitive is a label; comments are the report channel.**

## What the prototype proposes

### Labels command, comments report

This is the finding, and the prototype exists to make it visible rather than argued:

- **A label is consumed by the run that answers it.** Re-dispatch requires re-applying a
  label that was deliberately removed — an act, by a named actor, visible in the timeline.
- **Applying a label already requires a write bit.** Under a comment trigger, that is a
  check this repository writes, keeps right, and keeps right again when GitHub adds an
  association value. Under a label trigger it is GitHub's, and cannot be written wrong.
- **The two channels come apart.** An agent can say what it did without asking for
  anything. Under comment triggers, report and command are the same channel, so any rule
  strong enough to stop the loop stops the legitimate handoff as well.

Drive `[t]` to comment-triggered, `[i]` to GitHub App, then `[1]` and `[c]`, and the chain
runs research → review → revise → review → revise until the depth cap catches it. Press
`[a]` to close the loop and run it again: the loop stops, and so does research → review.
That is the trade the comment trigger forces and the label trigger does not.

**The label trigger is not free of it.** With machine dispatch on, a bot re-labelling still
chains to the cap — visible in the prototype as the same runaway, one channel over. The cap
is load-bearing in both models. What labels buy is that *reporting* is never *commanding*,
which is the common case and the one that would otherwise recur silently.

### The gate does not decide whether the run is safe

`dispatch()` and `findings()` are separate functions on purpose. A run can be legitimate
and dangerous in the same breath, and collapsing the two is precisely how
`pull_request_target` ships: **the label gate authorises the maintainer and says nothing
about the code.** Press `[3]` — a maintainer labels a fork PR, the gate is satisfied, and
the job checks out the fork's head with `CLAUDE_CODE_OAUTH_TOKEN` and `GITHUB_TOKEN` in the
environment, where `npm ci` reaches them before the agent ever starts. Press `[p]` to drop
`pull_request_target` and watch the secrets leave with it — and the write scope with them.
The safe configuration is also a mute one: the run can no longer post its own result, and
reporting needs a second privileged job, which is where the privilege comes back. Where the
trust boundary sits is a choice; whether there is one is not.

The same split gives injection its honest reading. Press `[6]`: a stranger comments, a
maintainer starts a run, and third-party text is in the agent's context without the
stranger having triggered anything. Three channels, three severities:

| Channel | Severity | Why |
|---|---|---|
| Interpolated into the workflow (`[n]`) | **critical** | The comment is shell on the runner before it is ever a prompt. No agent behaviour is involved and no refusal helps. |
| `promptArgs` / fetched by the agent's tools | **high** when nobody with a write bit put it there | It cannot execute, but the agent holds `contents:write`. |

The second is irreducible while agents read issues. The mitigation is not obedience; it is
that everything the agent writes arrives as a reviewable pull request.

### Identity

Three models, `[i]`:

- **Inherited** — today. `git log --format='%an'` returns one name regardless of who wrote
  the text. This is [#23](https://github.com/NGL321/mosaic/issues/23), and the prototype
  reports it as a **high** finding on every run.
- **git-config bot** — what Sandcastle's workflows do: `git config user.name
  "sandcastle-agent[bot]"`. Makes `%an` true, costs nothing, and is **unverifiable** — any
  workflow and any human can set the same string, and the push is still `GITHUB_TOKEN`.
- **GitHub App** — author and pusher are both the App, and PROTOCOL §5's check becomes a
  fact rather than a convention. The price is named in the prototype: the App is not the
  `github-actions` actor, so Actions' recursion guard no longer applies to it.

That last line is the one to carry into #23. **The identity that makes custody checkable is
the identity that forfeits the platform's loop guard** — which is an argument for the label
trigger, not against the App.

### Cost

Metered spend is **off** by default and the ceiling reads `$0.00/$12.00`, because
[#27](https://github.com/NGL321/mosaic/issues/27) established that all three runners draw a
`CLAUDE_CODE_OAUTH_TOKEN` at zero marginal cost. `[m]` turns metering on with #27's measured
$2.55-per-run figure, because #27 also records that Anthropic *paused* rather than withdrew
the change that would move this usage onto separate credit. A ceiling that has never
rejected anything is a ceiling nobody knows is wired up; this one can be made to fire.

## How to drive it

`[1]`–`[6]` inject events; `[f]` finishes a run and feeds back what it posts; `[c]` runs the
chain out. `[t]` `[r]` `[i]` switch trigger, runner and identity; `[p]` `[n]` toggle
`pull_request_target` and the interpolation mistake; `[h]` `[a]` control the handoff and
machine dispatch; `[m]` meters spend; `[z]` resets the world and keeps the settings.

Three things are worth doing deliberately:

1. `[t]`, `[i]`, then `[1]` `[c]` — the loop, running. Then `[a]`, `[z]`, `[1]` `[c]` — the
   loop closed and the handoff dead with it. Then `[t]` back to labels and `[1]` `[c]`.
2. `[3]` on the fork PR, then `[p]`. The gate's verdict never changes; the findings do.
3. `[5]` while something is running. `agent:in-progress` is the concurrency guard, and it
   works whether or not the workflow's `concurrency:` block was written correctly — which
   is the argument for it being a label rather than only a YAML key.

## Findings from building it

1. **"Comment-driven" was the wrong primitive, and the ticket's own hazard list is the
   evidence.** Loops, authorisation, and idempotence are three problems under comments and
   roughly zero under labels. The one thing comments do better — carrying an argument to
   the agent — is served by the agent reading the thread it was dispatched on.
2. **Sandcastle belongs in the design, one layer down from where it was proposed.** It is
   the runner and the output contract, not the dispatcher; the workflow YAML is the
   dispatcher, and it is short. Adopting Sandcastle does not remove the need to write the
   gate — it removes the need to write the harness, the iteration loop, and the
   report-shaping, which is the part that would otherwise be reinvented badly.
3. **Sandboxing is not what Sandcastle buys inside Actions.** Its own CI passes
   `noSandbox()`, because a GitHub-hosted runner is already ephemeral. The sandbox providers
   earn their keep in exactly one place: the self-hosted Pi, where the host survives the
   run — and that is also the one configuration where a fork PR is unacceptable at any
   price.

## Settled — Noah, 2026-07-31, after driving this

1. **The depth cap goes in the workflow.** The prototype puts it in the gate, which is the
   wrong place for the same reason the prototype itself gives: a cap the workflow cannot
   see stops being enforced the first time somebody adds a second workflow. The rule
   generalises past the cap — *a guard belongs wherever it is most effective, not wherever
   the code that noticed it happened to live.*
2. **`agent:blocked` is an ordinary label in the standard workflow**, removed by whichever
   agent or human clears the block. Recovery belongs in the same traffic as the work;
   anything a person has to remember to go and look at is a thing that will not be looked
   at. The failure reason goes on the comment, as Sandcastle already does.
   **The third identical block opens an issue instead of retrying** — that is the point
   where retrying has stopped being a strategy, and #24 requires a check nobody can satisfy
   to become visible rather than routed around. A label cannot count; that is the only job
   the escalation does.

## Still open

- **The generative loop is not covered here, and this prototype's guards would give false
  comfort that it is.** Every guard modelled above is per-thread: the depth cap is one
  chain, the concurrency group is `agent-mutate-{n}`, the consumed label is that thread's.
  The research loop is a growth *rate across the tracker* — a document emits `debt:open`
  issues, each dispatchable, each producing a document that can emit more. Every one of
  those dispatches passes this gate cleanly: different thread, one hop deep, legitimate
  identity. The only guard that transfers is the daily ceiling, and under #27's
  subscription finding that reads `$0.00`. Noah's ticket, not this prototype's.
- **A prototype that has discharged its question leaves the ticket in a state the label
  vocabulary cannot say.** #24 is not done — what remains is design and implementation,
  and neither needs another prototype. `wayfinder:prototype` is a ticket *type*, so there
  is no way to record that the prototype phase is spent while the ticket stays open. A gap
  in the vocabulary, noted rather than fixed here.
- **The CI gate suite** — #24's "also in scope" half (custody, bump consistency, links,
  front matter, branch naming, and the waiver model that keeps an unsatisfiable gate
  visible). Untouched. A second question, and it deserves its own prototype.

## Not in scope

No workflows written, no `.github/` changes, no network, no persistence, no tests. The
prototype does not decide the pipeline — it makes two trigger models, three runners and
three identities disagree out loud over the same six events.
