---
ticket: 58
map: 55
date: 2026-07-31
kind: question
tier: T3
session: unrecorded
sources: 18
debt: [69, 72, 74]
supersedes: null
---

# Runner mechanics: the 6-hour cap does not bind self-hosted runners, and a runner's labels are a claim, not a credential

Every figure below was retrieved on **2026-07-31** from a page on `docs.github.com` and is
quoted rather than recalled. The pages were read in full where short and by section where
long; the Markdown sources of the same pages, published by GitHub in
[`github/docs`](https://github.com/github/docs), were used to read the text GitHub's own
templating hides behind version conditionals — which is how the `queue:` property and the
plan gate on runner groups were established. Nothing here was measured: no runner was
registered, no job was dispatched, and no queue was observed. Three facts the loop depends
on are therefore documentation-deep only, and are filed as debt in §Verification Debt.

## 0. Verdict

| Sub-question | Verdict | Argued in |
|---|---|---|
| **1.1** Does the 6-hour job cap bind self-hosted runners? | **Refuted** — self-hosted runners get 5 days | §1 |
| **1.2** Is there a maximum `timeout-minutes`? | **Supported** — no ceiling on the job key beyond the runner's own limit; steps are capped at 360 | §1 |
| **1.3** What are the workflow-run and queueing caps? | **Established** — 35 days per run; 24 hours in the queue | §1 |
| **1.4** Does a long job need checkpoint-and-resume anyway? | **Supported** — the `GITHUB_TOKEN` dies at 24 hours | §1 |
| **2.1** When no matching runner is online, does the job queue, fail, or time out? | **Established** — it queues, then fails at 24 hours | §2 |
| **2.2** Is that state visible through the API? | **Loose** — `queued` is visible; *why* it is queued is not | §2 |
| **2.3** Can a job be assigned to a machine that is switched off? | **Contested** — GitHub says it cannot guarantee otherwise | §2 |
| **3.1** What are the per-repo concurrency limits? | **Established** — 20 concurrent jobs on Free, 40 on Pro | §3 |
| **3.2** Do runner-group limits apply to Mosaic? | **Refuted** — runner groups need an organization on Team or above | §3 |
| **3.3** Does the map's fan-out shape fit? | **Supported** — with a large margin, and one real hazard | §3 |
| **4.1** Can any runner claiming `local-only` satisfy a `local-only` job? | **Supported** — yes, and this is the finding | §4 |
| **4.2** Who may register a runner with which labels? | **Established** — repository admin, or a GitHub App with `administration` | §4 |
| **4.3** Is label-based tier refusal safe for `0.x`? | **Supported**, conditionally — the condition is that nothing else gets admin | §4 |
| **5.1** Do first-party GPU hosted runners exist? | **Supported** — Tesla T4, `linux_4_core_gpu`, $0.052/min | §5 |
| **5.2** Does that collapse [#57](https://github.com/NGL321/mosaic/issues/57) into this ticket? | **Refuted** — they require an organization on Team or Enterprise Cloud | §5 |

> **The tier-refusal mechanism holds, but not for the reason the map gives.** A cloud runner
> cannot pick up a `local-only` job because GitHub-hosted runners carry only GitHub's preset
> labels — not because a label is a credential. A label is an unverified self-assertion made
> at registration time by whoever holds repository admin. The refusal is therefore exactly as
> strong as the admin list, and no stronger; and the one thing that would weaken it is the
> `administration` permission that [#24](https://github.com/NGL321/mosaic/issues/24)'s
> dispatch App may be tempted to ask for.

## 1. Job duration — the cap is 5 days on self-hosted, and the token is the real limit

[#27](https://github.com/NGL321/mosaic/issues/27) recorded a 6-hour job cap. It is correct
and it is scoped. GitHub's [Actions limits](https://docs.github.com/en/actions/reference/limits)
table carries two separate rows, one per runner class:

| Limit category | Limit | Threshold |
|---|---|---|
| All GitHub-hosted runners | Job execution time | 6 hours |
| Self-hosted | Job execution time | 5 days |

The self-hosted wording is the hosted wording with a different number: *"Each job in a
workflow can run for up to 5 days of execution time. If a job reaches this limit, the job is
terminated and fails."* Neither row can be raised by support. **So the 6-hour cap does not
bind self-hosted runners** — the answer the ticket asked for, and it is a twenty-fold
difference. A training sweep that does not fit in six hours may well fit in five days.

**`timeout-minutes` has no documented ceiling of its own at the job level.** The
[workflow syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
gives `jobs.<job_id>.timeout-minutes` as *"The maximum number of minutes to let a job run
before GitHub automatically cancels it. Default: 360"* and then defers:

> If the timeout exceeds the job execution time limit for the runner, the job will be
> canceled when the execution time limit is met instead.

The step-level key is different and is capped: `jobs.<job_id>.steps[*].timeout-minutes` is
*"Maximum: 360 for both GitHub-hosted and self-hosted runners."* **A five-day job is
therefore a job made of steps no longer than six hours each** — which is a checkpoint
boundary handed to the loop for free, whether or not it wanted one.

**Two caps sit above the job.** The same limits table gives *"Workflow run time — 35 days /
workflow run … This period includes execution duration, and time spent on waiting and
approval"*, and, for self-hosted, *"Job queue time — 24 hours. A job can be in the queue for
24 hours before it is automatically cancelled."* The 35-day figure is what bounds a stalled
commission if nothing else does.

**The load-bearing footnote is the token, not the cap.** The same syntax page attaches a note
to `timeout-minutes`: *"The `GITHUB_TOKEN` expires when a job finishes or after a maximum of
24 hours. For self-hosted runners, the token may be the limiting factor if the job timeout is
greater than 24 hours."* A job may run for five days; its credential to talk to GitHub lasts
one. Anything the loop does at the end of a long run — pushing a branch, posting a report,
uploading an artifact through the Actions API — is unauthenticated after hour 24.

**Consequence for the loop.** Checkpoint-and-resume is required, but not for the reason the
ticket anticipated. It is not that the wall is at six hours; on the self-hosted tier the wall
is at five days. It is that (a) no single *step* may exceed six hours, and (b) the job's
identity expires at 24 hours, so a run longer than a day cannot report its own result. A
commission that expects to exceed 24 hours must checkpoint to durable storage and be resumed
by a *new* job with a fresh token — which makes resumption a dispatch event the tracker can
see, rather than a detail inside a run nobody is watching.

## 2. Availability — the job queues, then fails at 24 hours, and the API will not say why

The map names the failure it fears: *a commission silently waiting on a sleeping machine is
indistinguishable from one that is running*. GitHub answers the first half of that precisely.
[Self-hosted runners reference](https://docs.github.com/en/actions/reference/runners/self-hosted-runners),
under **Routing precedence for self-hosted runners**:

> * If GitHub finds an online and idle runner that matches the job's `runs-on` labels and
>   groups, the job is then assigned and sent to the runner.
>   * If the runner doesn't pick up the assigned job within 60 seconds, the job is re-queued
>     so that a new runner can accept it.
> * If GitHub doesn't find an online and idle runner that matches the job's `runs-on` labels
>   and groups, then the job will remain queued until a runner comes online.
> * If the job remains queued for more than 24 hours, the job will fail.

Restated for the ticket's three options: **it queues indefinitely up to 24 hours, and then it
fails.** Not immediately, and the same page is emphatic about that: *"If a job is labeled for
a certain type of runner, but none matching that type are available, the job does not
immediately fail at the time of queueing. Instead, the job will remain queued until the
24 hour timeout period expires."* So a `local-only` commission dispatched at a desktop that
is off is a job that looks alive for a day and then dies — which is a bounded stall, and a
much better answer for the loop than an unbounded one.

**The state is visible, but underspecified.** The
[workflow-jobs REST reference](https://docs.github.com/en/rest/actions/workflow-jobs) gives
each job a `status` from the enum `queued`, `in_progress`, `completed`, `waiting`,
`requested`, `pending`, a `conclusion` that includes `cancelled` and `timed_out`, and
nullable `runner_id` / `runner_name` alongside the job's `labels`. The
[`workflow_job` webhook](https://docs.github.com/en/webhooks/webhook-events-and-payloads#workflow_job)
fires on `queued`, `in_progress`, `completed` and `waiting`, and GitHub explicitly names it
as the signal to build autoscaling on. The
[self-hosted runners REST reference](https://docs.github.com/en/rest/actions/self-hosted-runners)
gives each runner a `status`, a `busy` boolean, and its `labels` with a `type` of
`read-only` or `custom`. The Actions UI shows the same three states in words —
[monitoring and troubleshooting](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/monitor-and-troubleshoot)
defines **Idle**, **Active**, and **Offline** ("*the machine is offline, the self-hosted
runner application is not running on the machine, or the self-hosted runner application
cannot communicate with GitHub*").

What no page reached here documents is a field that says *why* a job is queued. `queued`
covers "no eligible runner", "at the repository's concurrency limit", and "waiting behind a
`needs:` dependency" alike. The distinction the map wants is therefore **not reported by
GitHub; it has to be computed** — join the job's `labels` against the runner list and ask
whether any runner is `online` and not `busy` and carries all of them. That is a real
inference the dispatcher owns, and it is [#74](https://github.com/NGL321/mosaic/issues/74).

**And GitHub says the sleeping-machine case is worse than the routing rules imply.** On the
same reference page, under *Ephemeral runners for autoscaling*:

> GitHub recommends implementing autoscaling with ephemeral self-hosted runners; autoscaling
> with persistent self-hosted runners is not recommended. **In certain cases, GitHub cannot
> guarantee that jobs are not assigned to persistent runners while they are shut down.** With
> ephemeral runners, this can be guaranteed because GitHub only assigns one job to a runner.

A desktop that is powered on and off is a persistent runner by definition. GitHub is saying,
in its own documentation, that the map's feared failure is real and that it does not bound
it — *"in certain cases"* is the entire specification. Verdict **Contested**: the routing
rules say an offline runner is not eligible, and this paragraph says that guarantee does not
hold for persistent runners. Filed as [#72](https://github.com/NGL321/mosaic/issues/72).

**Consequence for the loop.** Three things follow. First, the dispatcher must treat
`status: queued` with no eligible online runner as a *distinct reportable state* and surface
it on the issue, because GitHub will not. Second, 24 hours is the honest upper bound on how
long that report can be delayed, and the loop should surface it far sooner than that — the
information is available within one API call of dispatch. Third, if the self-hosted tier is
ever built, `--ephemeral` registration is the configuration GitHub actually stands behind,
which sits awkwardly with a desktop that is not autoscaled and is a design question the
rollout ticket inherits.

## 3. Concurrency — 20 jobs is the wall, and the fan-out is nowhere near it

The [limits](https://docs.github.com/en/actions/reference/limits) page publishes job
concurrency per plan for GitHub-hosted runners:

| Runner type | Plan | Total concurrent jobs | Max concurrent macOS |
|---|---|---|---|
| Standard GitHub-hosted | Free | 20 | 5 |
| Standard GitHub-hosted | Pro | 40 | 5 |
| Standard GitHub-hosted | Team | 60 | 5 |
| Standard GitHub-hosted | Enterprise | 500 | 50 |
| Larger runner | Team / Enterprise | 1000 | 5 / 50 |

**These are account limits, and support can raise them.** The 20-job figure
[#24](https://github.com/NGL321/mosaic/issues/24) cited is the Free-plan row; a Pro account
gets 40. **No concurrency limit is published for self-hosted runners at all** — the
self-hosted rows in the same table are registration rate (1,500 runners / 5 minutes),
runners per group (10,000), job execution time and job queue time. Self-hosted concurrency is
bounded by how many runners are registered and idle, which is Mosaic's own number.

**Runner-group limits do not apply to Mosaic.** Runner groups are the mechanism GitHub names
for restricting which repositories may reach which runners — the
[secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use)
recommends *"you can create boundaries by organizing your self-hosted runners into separate
groups"* — but
[managing access to self-hosted runners using groups](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access)
states the permission as *"Enterprise accounts, organizations owned by enterprise accounts,
and organizations using GitHub Team … plans can create and manage additional runner groups"*.
Every clause names an **organization**. `NGL321/mosaic` is a user-account repository, so
runner groups are not available to it and the `runs-on` label is the only routing mechanism
Mosaic has. That is not a limitation on the fan-out; it is a limitation on §4's security
story, and §4 is where it lands.

**The map's fan-out shape fits, with two caveats.** One dataset agent followed by *n*
instrument agents is a job matrix or a `needs:` fan-out. The matrix ceiling is far away —
*"A job matrix can generate a maximum of 256 jobs per workflow run. This limit applies to
both GitHub-hosted and self-hosted runners"* — and 20 concurrent jobs against a handful of
instruments is not a binding constraint. The caveats are elsewhere:

1. **A fan-out that exceeds the concurrency limit does not fail; it queues.** And on the
   self-hosted tier, queuing is the state §2 just established is hard to distinguish from
   working. A fan-out wider than the number of registered runners is a fan-out that stalls
   silently by construction.
2. **`concurrency:` is a cancel mechanism by default, not a queue.** Per the
   [workflow syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax):
   *"At most one job or workflow run can be `pending` in the concurrency group"*, and *"By
   default, any existing `pending` job or workflow in the same concurrency group will be
   canceled and the new queued job or workflow will take its place."* Applying `#24`'s
   `agent-mutate-{n}` group naively across a fan-out would have instrument agents cancelling
   each other. The fix is documented — `queue: max` raises the pending ceiling to *"Up to 100
   jobs or workflow runs"*, processed FIFO, with additional runs cancelled beyond that, and
   `queue: max` may not be combined with `cancel-in-progress: true` — but it has to be asked
   for.

**Consequence for the loop.** The fan-out is not concurrency-bound at Mosaic's scale, so the
governor stays where premise 10 put it: a per-commission budget, not a job count. What the
loop does need is (a) `queue: max` on any concurrency group shared by sibling instrument
agents, and (b) a check that the number of instruments dispatched does not exceed the number
of runners that can serve them, since the excess is indistinguishable from work.

## 4. Label matching semantics — the security property, and what it actually rests on

This is the question the ticket called the most important, and the answer is a split verdict.

**Labels match cumulatively, and the runner declares them.** Per
[using self-hosted runners in a workflow](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/use-in-a-workflow):
*"These labels operate cumulatively, so a self-hosted runner must have all four labels to be
eligible to process the job."* The
[workflow syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
says the same from the job's side: *"If you specify an array of strings or variables, your
workflow will execute on any runner that matches all of the specified `runs-on` values."*
So `runs-on: [self-hosted, local-only]` is satisfied by any runner carrying **both** labels.

**A label is asserted by the runner at registration, and GitHub verifies nothing about it.**
[Applying labels to self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/apply-labels)
documents the mechanism plainly: *"You can pass label names to the `config` script using the
`labels` parameter"*, as in `./config.sh --url <URL> --token <TOKEN> --labels gpu`, with
multiple labels comma-separated. Even the *default* labels are optional — the same family of
pages notes *"You may pass in the `--no-default-labels` flag to prevent the self-hosted label
from being applied"*, and the REST API's just-in-time endpoint
(`POST /repos/{owner}/{repo}/actions/runners/generate-jitconfig`) takes a caller-supplied
`labels` array of 1 to 100 entries. The API's runner schema types each label as `read-only`
or `custom`; `custom` is exactly the class `local-only` would belong to, and it means
*asserted by whoever configured this runner*.

**So the answer to 4.1 is yes: any runner that merely claims `local-only` satisfies a
`local-only` job.** There is no attestation, no hardware binding, no network check. The label
`gpu` in GitHub's own example means "somebody said this machine has a GPU."

**The question therefore reduces to who may register a runner.** Three first-party statements
bound it. [Adding self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners):
*"To add a self-hosted runner to a user repository, you must be the repository owner"*; for an
organization repository, *"you must be an organization owner, have admin access to the
repository, or have the 'Manage organization runners and runner groups' permission."* The
[REST reference](https://docs.github.com/en/rest/actions/self-hosted-runners) requires admin
access for both listing runners and creating a registration token. And the
[self-hosted runners reference](https://docs.github.com/en/actions/reference/runners/self-hosted-runners)
gives the programmatic equivalents: a token with `repo` scope for private repositories,
**`public_repo` scope for public ones**, `admin:org` for organizations — or, for a GitHub App,
*"For repositories, assign the `administration` permission."*

**This is where the map's premise 11 needs amending, and where the finding bites.** The
refusal property is real but it is not the property the map states. A cloud runner cannot
pick up a `local-only` job — true, and the mechanism is that GitHub-hosted runners carry only
GitHub's own preset labels, maintained in
[`actions/runner-images`](https://github.com/actions/runner-images) and enumerated on the
[GitHub-hosted runners page](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners).
Nobody can attach `local-only` to a GitHub-hosted runner because nobody configures
GitHub-hosted runners. The refusal holds *because GitHub owns that namespace*, not because
the label is trusted.

Three consequences follow, in ascending order of how much they should worry the loop:

1. **Do not collide with the preset namespace.**
   [Troubleshooting workflows](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows):
   *"We recommend using unique label names for larger and self-hosted runners. If a label
   matches to any of the existing preset labels, there can be runner assignment issues where
   there is no guarantee on which matching runner option the job will run on."* A tier label
   that collided with a preset would be a tier refusal with no guarantee attached. `local-only`
   does not collide today; the rule is that tier labels must be chosen so they never can.
2. **Always pin `self-hosted` as well.** `runs-on: local-only` alone asserts nothing about the
   runner class. `runs-on: [self-hosted, local-only]` is two independent conditions, and the
   first is one GitHub enforces structurally.
3. **The `administration` permission is the thing to watch.** `#24` ruled that a GitHub App is
   the only identity that makes custody checkable, and this page says an App with repository
   `administration` can register runners — with any labels it likes. **An App that can both
   dispatch jobs and register runners can manufacture a runner that satisfies `local-only` and
   route a placement-constrained job to it.** That is the tier widening premise 7 forbids, done
   entirely through documented API calls by an identity the programme installed on purpose.
   The mitigation is one line in the App manifest: the dispatch App must not hold
   `administration`.

**One further note, and it is not small for a public repository.** GitHub's guidance on
self-hosted runners for public repos is a warning, not a caveat. From the
[secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use):
*"self-hosted runners should almost never be used for public repositories on GitHub, because
any user can open pull requests against the repository and compromise the environment"*, and
*"Self-hosted runners for GitHub do not have guarantees around running in ephemeral clean
virtual machines, and can be persistently compromised by untrusted code in a workflow."*
Mosaic is public by design. `#24`'s ruling — **no `pull_request_target` in `0.x`**, no fork-PR
automation — is what makes a self-hosted tier defensible here at all, and it stops being a
stylistic preference the moment a runner exists on Noah's desktop. It becomes the control.

**Consequence for the loop.** The tier-refusal mechanism is sound enough to build on, and
premise 11's wording should be tightened to say what it actually rests on: *a job requiring
`local-only` is never picked up by a cloud runner because GitHub-hosted runners carry only
GitHub's preset labels; the label itself is an unverified assertion by whoever registered the
runner, so the refusal is exactly as strong as the set of principals holding repository
admin.* Two mechanical rules fall out — tier labels are always paired with `self-hosted`, and
the dispatch App never holds `administration` — and both are cheap enough to adopt now.

## 5. GPU hosted runners — they exist, they are cheap, and Mosaic cannot buy them

They exist. The
[larger runners reference](https://docs.github.com/en/actions/reference/runners/larger-runners)
publishes a GPU specification table with one row: **4 vCPU, 1 GPU, Tesla T4, 28 GB RAM, 16 GB
VRAM, 176 GB SSD, Ubuntu or Windows**, running the NVIDIA GPU-Optimized VMI partner image
from the Azure Marketplace. The
[pricing reference](https://docs.github.com/en/billing/reference/actions-runner-pricing)
gives two billing SKUs:

| Operating system | Billing SKU | Per-minute rate (USD) |
|---|---|---|
| Linux 4-core | `linux_4_core_gpu` | $0.052 |
| Windows 4-core | `windows_4_core_gpu` | $0.102 |

$0.052/minute is **$3.12/hour**. Under premise 10's $50/month ceiling that is roughly 16
GPU-hours a month — thin for a training sweep, but a real number, from a first-party page,
with billing already wired to the account.

**And Mosaic cannot use them.** Two independent gates. First, plan:
[larger runners](https://docs.github.com/en/actions/concepts/runners/larger-runners) states
its permission as *"Larger runners are only available for organizations and enterprises using
the GitHub Team or GitHub Enterprise Cloud plans"* — an **organization**, on a paid tier.
`NGL321/mosaic` is a user-account repository. Second, billing: the same page notes larger
runners *"are not eligible for the use of included minutes on private repositories. For both
private and public repositories, when larger runners are in use, they will always be billed
at the per-minute rate"*, and the pricing page states *"The larger runners are not free for
public repositories."* Mosaic's public-repo free-minutes advantage, which `#27` established,
does not extend here.

**So this does not collapse [#57](https://github.com/NGL321/mosaic/issues/57), but it changes
its baseline.** `#57` asks which cloud GPU provider fits under $50/month and lists Modal,
RunPod, Lambda, vast.ai and Together — and explicitly includes *"any GitHub-native GPU runner
offering"*. There is one, and it costs $3.12/hour for a T4. `#57` should now evaluate a fourth
option alongside those providers: **move Mosaic into a GitHub organization on the Team plan
and use `linux_4_core_gpu`**, priced as the Team seat plus $3.12/hour, against the operational
saving of never writing a provider integration, never handling a second set of credentials in
CI, and getting a container-by-digest story that is just `runs-on`. That comparison is `#57`'s
to make; this document's contribution is the number and the two gates.

## What this does not establish

### Sources not reached

Everything cited is a page on `docs.github.com` or its published Markdown source, and every
appendix entry was opened. Three classes of source were *wanted* and are not documentation:

- **GitHub's actual scheduler behaviour.** Nothing here was measured. The three debt items
  below all have the same shape: a documented sentence that the loop's design leans on, whose
  behavioural meaning cannot be read off the sentence.
- **The GitHub Team plan's price and the mechanics of converting a user repository to an
  organization.** §5 asserts the plan gate but not what clearing it costs. That is `#57`'s
  question and was left there deliberately rather than half-answered here.
- **The `actions/runner` source.** The routing rules in §2 are GitHub's server-side scheduler,
  which is not open source; the open-source
  [`actions/runner`](https://github.com/actions/runner) is the client and would not settle
  what the service does with an unmatched label set. Not reached, and it would not have helped.

### Open gaps

- **Whether `--ephemeral` is usable for a desktop tier at all.** GitHub's guarantee about
  shut-down machines holds only for ephemeral runners, and an ephemeral runner de-registers
  after one job. A desktop that is not autoscaled would need something to re-register it —
  which is either a daemon on the machine or a scheduled workflow, and both are new
  infrastructure the self-hosted rollout does not currently plan for.
- **What a resumed commission is, in tracker terms.** §1 concludes that a run longer than
  24 hours must be resumed by a fresh job. Whether that is a new workflow run, a new issue
  comment, or a re-applied label is a dispatch-model question that `#24` did not face because
  it never had a job that outlived its token.
- **Whether the 20/40-job concurrency limit is per-account or per-repository.** The limits
  table names a plan, not a scope, and Mosaic is one repository under one account, so the
  distinction is currently invisible. It stops being invisible the day a second repository
  runs agents.
- **Nothing was found on rate-limiting the `workflow_job` webhook**, which is the signal §2
  recommends building stall detection on. If the loop polls the REST API instead, the
  `GITHUB_TOKEN` limit of 1,000 requests/hour/repository is the budget it spends.

### Load-bearing ifs

- **If the 24-hour queue timeout does not apply when no matching runner is registered at all**
  ([#69](https://github.com/NGL321/mosaic/issues/69)), then §2's "bounded stall" becomes a
  35-day stall and the loop's stall detection cannot rely on a terminal job state.
- **If jobs can be assigned to a powered-off persistent runner and are not re-queued**
  ([#72](https://github.com/NGL321/mosaic/issues/72)), the 24-hour backstop is not a backstop,
  and the map's sleeping-machine failure is unmitigated by anything GitHub provides.
- **If a runner's labels could be verified by GitHub** — they cannot, on the evidence in §4 —
  then §4's whole argument collapses into the map's original wording and the `administration`
  warning is unnecessary. This is the claim to attack first, because the entire security
  conclusion rests on an absence, and an absence is what a careless reading misses.
- **If Mosaic moves into a GitHub organization** for any other reason, §5's first gate falls
  and `linux_4_core_gpu` becomes purchasable — which would materially change `#57`'s answer
  without anyone reopening `#57`.

## Verification Debt

1. [#69](https://github.com/NGL321/mosaic/issues/69) — **the 24-hour queue timeout is
   documented under "Routing precedence for self-hosted runners"**, and §2 applies it to the
   case where no matching runner is registered at all. That extension is an inference from the
   routing text. Discharged by one instrumented dispatch against a label nothing carries.
2. [#72](https://github.com/NGL321/mosaic/issues/72) — **"In certain cases, GitHub cannot
   guarantee that jobs are not assigned to persistent runners while they are shut down."**
   Neither the cases nor the consequence is documented. This is the map's named failure,
   admitted by GitHub and left unbounded. Discharged by powering a registered runner off and
   watching a matching job.
3. [#74](https://github.com/NGL321/mosaic/issues/74) — **no API field was found that
   distinguishes "queued, no eligible runner" from "queued, waiting its turn."** §2's
   recommendation that the dispatcher compute the distinction is a design decision taken
   because a search of the REST and webhook references did not find one, which is weaker than
   establishing that none exists. Discharged by producing all three states and diffing the
   payloads.

## Proposals

For [`CONTEXT.md`](https://github.com/NGL321/mosaic/blob/main/CONTEXT.md), no change is
proposed: nothing here is a claim about cognition or a rung of the Protective Belt, and §5's
badge machinery has nothing to attach to.

For **map [#55](https://github.com/NGL321/mosaic/issues/55), premise 11**, the following
replacement is proposed for the clause beginning *"and **runner labels are the tier-refusal
mechanism**"*, on the grounds that the current wording states a security property GitHub does
not provide:

> and **runner labels are the tier-refusal mechanism** — a job requiring `local-only` is never
> picked up by a cloud runner, because GitHub-hosted runners carry only GitHub's own preset
> labels and no one can add a custom label to one. The label itself is an unverified assertion
> made at registration by whoever holds repository admin, so the refusal is exactly as strong
> as that admin list. Two rules follow: a tier label is always paired with `self-hosted` in
> `runs-on`, and the dispatch App of [#24](https://github.com/NGL321/mosaic/issues/24) must
> never hold the `administration` permission, which would let it register a runner claiming
> any tier it liked.

For **[#57](https://github.com/NGL321/mosaic/issues/57)**, the recommendation is to add a
fourth option to its comparison rather than to close it: GitHub-hosted `linux_4_core_gpu`
(Tesla T4, 16 GB VRAM) at **$0.052/minute — $3.12/hour**, gated on moving Mosaic into an
organization on the GitHub Team plan, and not eligible for public-repo free minutes.

## Appendix: primary sources, all retrieved 2026-07-31

1. [Actions limits](https://docs.github.com/en/actions/reference/limits) — the job-execution,
   workflow-run, queue-time, matrix, registration and job-concurrency tables. The single most
   load-bearing page here.
2. [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
   — `jobs.<job_id>.timeout-minutes`, `steps[*].timeout-minutes`, `runs-on`, `concurrency`
   and the `GITHUB_TOKEN` expiry note.
3. [Self-hosted runners reference](https://docs.github.com/en/actions/reference/runners/self-hosted-runners)
   — routing precedence, the 24-hour queue failure, the persistent-runner warning, autoscaling
   and the registration scopes and App permissions.
4. [Using self-hosted runners in a workflow](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/use-in-a-workflow)
   — default labels, custom labels, cumulative matching, `--no-default-labels`.
5. [Applying labels to self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/apply-labels)
   — who may create and assign labels, and the `config.sh --labels` mechanism.
6. [Adding self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners)
   — the permission required to register a runner at repository, organization and enterprise
   level.
7. [Managing access to self-hosted runners using groups](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access)
   — the plan gate that puts runner groups out of Mosaic's reach.
8. [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/monitor-and-troubleshoot)
   — the Idle / Active / Offline runner states.
9. [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
   — hardening for self-hosted runners, the public-repository warning, runner groups as a
   boundary, and JIT runners.
10. [Troubleshooting workflows](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows)
    — the preset-label collision warning and the scheduled-workflow load note.
11. [Larger runners](https://docs.github.com/en/actions/concepts/runners/larger-runners) —
    the capability list including GPU-powered runners, and the billing note.
12. [Larger runners reference](https://docs.github.com/en/actions/reference/runners/larger-runners)
    — the GPU specification table (Tesla T4) and the NVIDIA partner image.
13. [Actions runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing)
    — the `linux_4_core_gpu` and `windows_4_core_gpu` per-minute rates.
14. [REST API: self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners)
    — the runner schema (`status`, `busy`, `labels[].type`), registration-token access
    requirements, and `generate-jitconfig`.
15. [REST API: workflow jobs](https://docs.github.com/en/rest/actions/workflow-jobs) — the job
    `status` and `conclusion` enums, `runner_id`, `runner_name`, `labels`.
16. [Webhook events and payloads: `workflow_job`](https://docs.github.com/en/webhooks/webhook-events-and-payloads#workflow_job)
    — the `queued` / `in_progress` / `completed` / `waiting` activity types.
17. [GitHub-hosted runners](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners)
    — the preset runner labels GitHub owns, which is why the tier refusal holds at all.
18. [Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners)
    — what a self-hosted runner is, and the note that it need not have a clean instance for
    every job.
