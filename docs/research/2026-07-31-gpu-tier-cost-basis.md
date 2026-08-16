---
ticket: 57
map: 55
date: 2026-07-31
revised: 2026-08-02
kind: question
tier: T3
session: unrecorded
sources: 48
debt: [68, 70, 71, 73]
supersedes: null
---

# The GPU tier that fits under $50 a month is Modal, and the ceiling is the weakest part of the answer

**Ticket:** [#57 — Establish the GPU tier that fits under $50 a month](https://github.com/NGL321/mosaic/issues/57)
**Map:** [#55 — Map: The research loop](https://github.com/NGL321/mosaic/issues/55)
**Date:** 2026-07-31

**Provenance.** Machine-produced, unverified. Every price, quota and quoted sentence below was retrieved on **2026-07-31** from a first-party page — the provider's own pricing page, its own documentation, or its own source repository on GitHub — and is quoted rather than recalled. Where a fact could not be reached from first-party documentation the verdict is **Unresolved** and says so, on [#13](https://github.com/NGL321/mosaic/issues/13)'s precedent; three of the six providers have at least one such hole and one of them, vast.ai, is unpriceable in principle. Two claims were settled by reading first-party *source code* rather than prose, and are marked where they occur. The workload sizing in §1 is **derived, not retrieved** — it comes from a paper's method section by way of the programme's own survey, and no wall-clock GPU measurement exists anywhere in Mosaic; that is the weakest number here and everything expressed in *hours per month* inherits it. None of this has been checked by Noah unaided.

**Revised 2026-08-02**, before landing, to carry [#75](https://github.com/NGL321/mosaic/issues/75)'s refutations of two vast.ai findings and the eligibility rule that follows from them — itemised in §0.1. The one fact added on that date, vast.ai's bandwidth charge, is quoted from its billing reference and dated in the appendix; everything else here still carries its 2026-07-31 retrieval.

> **Volatility warning.** Every figure in this document is a GPU spot price or a published rate card in a market that has repriced repeatedly. GitHub's own GPU runner rate is quoted after a January 2026 price change. Treat anything here older than a quarter as a prompt to re-fetch, not as a standing fact.

---

## 0. Verdict

| Sub-question | Verdict | Where argued |
|---|---|---|
| **1** What is the per-hour price of the smallest GPU that trains a grokking-scale transformer? | **Supported** — $0.16/hr (RunPod RTX A5000, 24 GB) to $0.59/hr (Modal T4, 16 GB) | §1, §2, §3 |
| **2** Is GPU capability the constraint that decides the tier? | **Refuted** — the workload is ~10⁶ parameters; the cheapest card on every menu is already oversized | §1 |
| **3** Can the tier be invoked from a GitHub Actions job with *documented* unattended auth? | **Supported** for Modal and RunPod; **Unresolved** for Lambda | §2, §3, §4 |
| **4** Does the tier accept a container image by digest, as [#55](https://github.com/NGL321/mosaic/issues/55) premise 12 requires? | **Supported** for RunPod; **Unresolved** for Modal, Together, vast.ai and GitHub | §2, §3, §5 |
| **5** Is billing per-second, and is idle or stopped time free? | **Supported** for Modal and RunPod; **Refuted** for Lambda, which bills until terminate | §2, §3, §4 |
| **6** Can a hard spend ceiling be set **at the provider**? | **Contested** — the two providers with a documented hard stop are the two that cannot fit $50 | §6 |
| **7** What does storage egress cost on the path to Drive under `DATA-PROTOCOL` §3.4? | **Supported** as free for RunPod and Lambda; **Unresolved** for Modal | §7 |
| **8** Is Together AI a candidate? | **Refuted** — it sells no small GPU, and its minimum volume alone is $163.84/month | §5 |
| **9** Is GitHub's own GPU runner a candidate? | **Refuted** — $3.12/hr and explicitly not free on public repositories | §5 |
| **10** Is Lambda a candidate? | **Refuted** — no stop-without-charge state and no documented spend cap | §4 |
| **11** Is vast.ai a candidate? | **Refuted** as a candidate — no published price *and* no provider-enforced spend ceiling, which is the constraint §8 says actually binds | §4, §8 |
| **12** Does the loop fit under $50/month? | **Supported**, with room — the binding constraint is the ceiling's enforcement, not the price | §8 |

### 0.1 What this revision changed

**Corrected 2026-08-02, before landing, under [#119](https://github.com/NGL321/mosaic/issues/119).** The document was written on 2026-07-31 and has not merged; [#75](https://github.com/NGL321/mosaic/issues/75) then swept all 131 first-party vast.ai pages and refuted two of its findings from first-party documentation. Four things moved, and the exact replacement text for the first three is [#75](https://github.com/NGL321/mosaic/issues/75)'s:

1. **§7 no longer reads vast.ai's egress as an unmentioned absence.** It is a *documented charge at an unpublished rate* — every byte in either direction, whatever state the instance is in — which is worse than an absent line item, not better. `DATA-PROTOCOL` §3.4 guarantees Mosaic incurs it on every commission.
2. **§4.2 no longer claims live rates exist only in the authenticated console.** An unauthenticated `GET https://console.vast.ai/api/v0/bundles/` returned the offer table on 2026-08-02, contradicting vast.ai's own published auth requirement. That makes a sample cheap and a citation no less impossible.
3. **Verdict row 11 moves from Unresolved to Refuted**, and §8 states the eligibility rule the change rests on: a provider whose price cannot be cited is not eligible for the tier. The load-bearing reason is not tidiness — §5 of [#75](https://github.com/NGL321/mosaic/issues/75) found vast.ai has **no provider-enforced spend ceiling at all**, and §12 of this document's own verdict says the binding constraint is the ceiling's enforcement rather than the price. vast.ai fails on that constraint independently of cost, so pricing it would not make it eligible. Its row leaves the §8 comparison table; the dated sample survives as an observation in [#75](https://github.com/NGL321/mosaic/issues/75).
4. **Verification Debt item 5 is discharged.** [#75](https://github.com/NGL321/mosaic/issues/75) settled it, in the second of the two ways that item offered — a ruling that an uncitable price is disqualifying. The two debts that sweep filed against vast.ai's API, [#117](https://github.com/NGL321/mosaic/issues/117) on a digest reference and [#118](https://github.com/NGL321/mosaic/issues/118) on the unauthenticated offer table, are **retired as moot** by the same ruling: a provider outside the tier carries no premise-12 obligation and needs no price channel. Both issues named that outcome as conditional on this decision, which is now taken.

Nothing about Modal, RunPod, Lambda, Together or the GitHub runner moved, and the recommendation is unchanged.

### The one-line verdict

> **Modal, on the T4 at $0.59/hour with per-second billing and $30/month of free credits, which puts roughly 135 GPU-hours a month inside the $50 ceiling.** The price question is not close and was never the hard part. The hard part is [#57](https://github.com/NGL321/mosaic/issues/57)'s own sharpest requirement — *a ceiling that only exists in a config file this repo owns is a ceiling that fails in exactly the case it is for* — and on that requirement the answer is uncomfortable: the only two providers that document a hard, enforced stop are GitHub and Together, and both are priced out of the tier. Modal documents a budget and does not document what it does when you cross it.

**The load-bearing surprise is that this is not a GPU-selection problem.** A grokking-scale transformer is small enough that every provider's *cheapest* card clears the requirement several times over, so nothing is decided by capability. What decides it is billing granularity, idle cost, whether CI can authenticate without a human, and whether the provider will stop taking money when told to.

---

## 1. The workload, and why it decides nothing — **Refuted** as the constraint

The programme's own reference for "grokking-scale" is the study its first survey identified as the template a Mosaic experiment would have to beat: [Tang, Wang, García-Redondo & Monod (2026), *Topological Signatures of Grokking*](https://arxiv.org/abs/2605.06352), whose method section is reproduced in `docs/research/2026-07-25-grokking-eca-tda-survey.md`. The architecture is a **2-layer transformer encoder, d_model=128, 4 heads, d_attn=32, d_ff=256**, trained on (a+b) mod p for p ≤ 197, over **5 seeds × 60,000 steps** with checkpoints every 500.

That is on the order of 10⁶ parameters and a dataset of at most ~38,809 pairs. In fp32, weights, gradients and Adam moments together are a few tens of megabytes. The smallest GPU on any menu surveyed here — a 16 GB T4 — exceeds the requirement by roughly three orders of magnitude, and the survey records that even the downstream persistent-homology step ran at "~2 minutes per model" on **CPU**.

**Verdict: Refuted** that GPU capability constrains the choice. Every candidate card in every table below fits. This inverts the shape of #57's first sub-question: the interesting quantity is not which GPU is big enough, it is which billing model wastes the least of a card that is mostly idle relative to its size.

**And this is the number the study is weakest on.** No wall-clock GPU measurement for this workload exists anywhere in Mosaic. The paper's own compute statement was not reached — only the CPU figure above, quoted at second hand through the survey. Every figure below expressed as *hours per month* is therefore a correct price multiplied by an unmeasured duration. The provider *ranking* is robust to this, because the same assumed workload is priced under every option; the *levels* are not. Logged as [#73](https://github.com/NGL321/mosaic/issues/73).

---

## 2. Modal — **Supported**, and the recommendation

### 2.1 Price and billing granularity

[modal.com/pricing](https://modal.com/pricing) (retrieved 2026-07-31) publishes a per-second rate card. The relevant rows:

| GPU | Per second | Per hour |
|---|---|---|
| Nvidia T4 (16 GB) | $0.000164 | $0.59 |
| Nvidia L4 (24 GB) | $0.000222 | $0.80 |
| Nvidia A10 | $0.000306 | $1.10 |
| Nvidia A100 40 GB | $0.000583 | $2.10 |

The T4 is the cheapest GPU Modal offers and clears §1's requirement. The same page states the billing model plainly — "With Modal, you always pay for what you use and nothing more" — and prices the Starter plan at "**$0 + compute / month**" with "**$30 / month free credits**".

**That free-credit line is worth more than it looks.** It means the first $30 of GPU each month is drawn at zero marginal cost, in exactly the way [#27](https://github.com/NGL321/mosaic/issues/27) found agent time is drawn at zero marginal cost from a `CLAUDE_CODE_OAUTH_TOKEN`. Spending the full $50 out of pocket buys $80 of compute, or **135.6 T4-hours a month**.

### 2.2 Idle cost — free, with one caveat that is not

Modal is serverless and scales to zero, but the [cold-start guide](https://modal.com/docs/guide/cold-start) is honest about the window in which it does not:

> "you will be billed for any resources used while the container is idle (e.g., GPU reservation or residual memory occupancy)."

The default `scaledown_window` is 60 seconds and is configurable from 2 seconds to 20 minutes. For a stalled commission — #57's worry, "the difference between a $12 month and a $200 one when a commission stalls" — the exposure is therefore bounded at one scaledown window per invocation, not at the duration of the stall. This is the single strongest argument for Modal over any instance-rental model, where a stall bills until somebody notices.

### 2.3 Invocation from GitHub Actions — documented, and demonstrated

Modal is the only provider surveyed that publishes **a working GitHub Actions workflow in its own repository**. [`modal-labs/ci-on-modal`](https://github.com/modal-labs/ci-on-modal) exists for exactly this purpose and its README says so:

> "The same command can be executed from inside a CI runner on another platform. We provide a sample GitHub Actions workflow in `.github/workflows/ci.yml`. To run these tests on GitHub Actions, fork this repo and create a new GitHub Actions secret that contains your `MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET`."

[The workflow itself](https://github.com/modal-labs/ci-on-modal/blob/main/.github/workflows/ci.yml) is nine lines of substance — `runs-on: ubuntu-latest`, the two token secrets in `env:`, `pip install modal`, `modal run`. The [continuous-deployment guide](https://modal.com/docs/guide/continuous-deployment) documents the same pattern, and [`modal token set --token-id --token-secret`](https://modal.com/docs/reference/cli/token) is the non-interactive credential path.

**Verdict: Supported.** Unattended CI auth is documented, not inferred — the distinction [#27](https://github.com/NGL321/mosaic/issues/27) had to draw against Antigravity CLI, whose headless mode required a prior interactive session. Note also that the Actions job itself is an ordinary `ubuntu-latest` runner, which under #27's finding is **free on a public repository**; the runner orchestrates and the GPU bills separately.

### 2.4 Container image by digest — **Unresolved**, and it is the load-bearing gap

[#55](https://github.com/NGL321/mosaic/issues/55) premise 12 requires "a base image pinned **by digest**." Modal's documentation never shows one. The [`modal.Image` API reference](https://modal.com/docs/reference/modal.Image) describes the parameter as:

> "tag" … "Registry image reference (e.g. ``python:3.11-slim``)."

and the [custom-container](https://modal.com/docs/guide/custom-container) and [existing-images](https://modal.com/docs/guide/existing-images) guides show only `huanjason/scikit-learn`, `ubuntu:22.04`, `gisops/valhalla:latest`, and an ECR reference ending `:latest`. Not one digest anywhere.

Reading the first-party client source rather than the prose gets closer without closing it: in [`py/modal/_image.py`](https://github.com/modal-labs/modal-client/blob/main/py/modal/_image.py) the reference is documented identically and passed through without being parsed, and [`py/test/image_test.py`](https://github.com/modal-labs/modal-client/blob/main/py/test/image_test.py) contains no digest case at all. A pass-through string suggests a digest would work, because the server does the pull and registries accept digests generically.

**Verdict: Unresolved.** "Probably works" is not what premise 12 asks for, and this is the one **if** that would move the recommendation. Logged as [#68](https://github.com/NGL321/mosaic/issues/68); it is settled by a single one-minute run.

---

## 3. RunPod — **Supported**, the fallback, and cheaper

RunPod undercuts Modal substantially and is the provider that already satisfies the requirement Modal leaves open.

**Price.** [runpod.io/pricing](https://www.runpod.io/pricing) (retrieved 2026-07-31) lists the **RTX A5000 (24 GB) at $0.16/hr on Community Cloud** and $0.27/hr on Secure Cloud — the cheapest rate found anywhere in this study, and 312 hours a month inside the ceiling. The L4 is $0.44/hr Community and $0.39/hr Secure.

**Billing granularity.** [Pod pricing](https://docs.runpod.io/pods/pricing) states pods "are billed by the second for compute and storage," with Network Volumes billed hourly. [Serverless](https://docs.runpod.io/serverless/overview) documents "no idle costs when your application isn't processing requests."

**Idle cost has a trap.** [Managing pods](https://docs.runpod.io/pods/manage-pods) is explicit that stopping is not free — "you'll still be charged for volume disk storage while stopped" — and the pricing page prices idle volume disk at **$0.20/GB/month against $0.10/GB/month while running**, so a stopped pod's storage costs twice a running one's. Terminate, do not stop. This matters less for Mosaic than it would for most users, because under `docs/DATA-PROTOCOL.md` §3.3 regenerable bytes are not stored at all and under §3.4 durable ones go to Drive, so there is no reason to keep a volume alive between runs.

**Invocation.** [`runpodctl`](https://docs.runpod.io/runpodctl/overview) authenticates non-interactively with `runpodctl config --apiKey`, the [v2 REST API](https://docs.runpod.io/api-reference-v2/overview) takes a bearer token, and [the API-keys page](https://docs.runpod.io/get-started/api-keys) documents All / Restricted / Read-Only scopes and suggests storing the key in a GitHub secret. No first-party GitHub Action exists; the CLI in a standard runner is the path, as with Modal.

**Container image by digest — Supported, and this is where RunPod wins.** [The worker deploy guide](https://docs.runpod.io/serverless/workers/deploy) documents digest pinning outright, showing `docker inspect --format='{{index .RepoDigests 0}}' USER/WORKER:VERSION` to obtain an `image@sha256:<hash>` reference, and recommends SHA references over `:latest` for reproducibility. That is premise 12's requirement, met in the provider's own words.

**Verdict: Supported** as a fallback, and on the two criteria the map states most sharply — price and digest pinning — it beats the recommendation. It loses on §6.

---

## 4. Lambda — **Refuted**; vast.ai — **Refuted**

### 4.1 Lambda bills until you destroy the machine

[lambda.ai/service/gpu-cloud](https://lambda.ai/service/gpu-cloud) lists the Quadro RTX 6000 (24 GB) at **$0.69/hr** as its cheapest option and the V100 (16 GB) at $0.79/hr — competitive with Modal on paper. The [billing documentation](https://docs.lambda.ai/public-cloud/billing/) removes it from contention in one sentence:

> "Billing begins the moment you launch an instance and the instance passes health checks, and ends the moment you terminate the instance. Instances are billed for as long as they're running, regardless if they're actively being used."

Billing is in one-minute increments at the hourly rate, and there is **no stop-without-charge state** — only terminate. Filesystem storage compounds it: "Billing continues as long as a filesystem exists, even if it's not mounted to an instance." This is precisely the failure mode #57 asks the tier to be immune to. A commission that stalls on a Friday costs the full weekend.

Two further gaps. Lambda's on-demand product is **VM images, not containers** — the [on-demand docs](https://docs.lambda.ai/public-cloud/on-demand/) describe Ubuntu 22.04, "Lambda Stack" and "GPU Base" as selectable base images, so premise 12's digest requirement has no object to attach to. And the [access-security page](https://docs.lambda.ai/public-cloud/access-security/) documents API keys but never addresses non-interactive or CI use, so unattended auth is **inferable, not documented**.

**Verdict: Refuted.** The idle-cost model alone disqualifies it; no documented spend cap was found either (§6).

### 4.2 vast.ai publishes no price, and is ineligible on the ceiling regardless

vast.ai is a marketplace, and [its pricing page](https://vast.ai/pricing) says so rather than publishing rates: "Prices are set by the market, not by Vast," across "40+ data centers," with only relative tiers — On-Demand, Interruptible ("50%+ cheaper"), and Reserved. There is no floor, no reference SKU rate, and no table. Live offers are obtainable without an account — an unauthenticated `GET https://console.vast.ai/api/v0/bundles/` returns the offer table, contradicting vast.ai's own documented requirement that "All endpoints require `Authorization: Bearer $VAST_API_KEY`." That makes a sample cheap and a citation no less impossible: the endpoint is undocumented, the response is a truncated default slice, and the result is a weather report rather than a rate.

Its mechanics are otherwise sound: [per-second billing](https://docs.vast.ai/billing) — "You are charged the base active rental cost for every second your instance is in the active/connected state" — and a documented [CLI](https://vast.ai/developers/cli) with [bearer-token auth](https://docs.vast.ai/api/authentication) explicitly built for automation ("Pipe to jq. Automate everything."). The same billing page carries the stopped-instance trap in stronger terms than RunPod's: "Storage charges continue even when instances are stopped… As with any stopped instance, you will continue to be billed for disk storage, even if your balance is negative." Digest pinning is neither shown nor denied in [the create-instance reference](https://docs.vast.ai/api-reference/instances/create-instance) or [the templates page](https://docs.vast.ai/templates), which document the field only as `repository/image_name:tag`.

**Verdict: Refuted**, and on two independent grounds. This document originally returned **Unresolved** on [#13](https://github.com/NGL321/mosaic/issues/13)'s precedent — not a search that went badly but a fact the owning party declines to publish. [#75](https://github.com/NGL321/mosaic/issues/75) then swept all 131 first-party pages and found the position worse than unpriced: bandwidth is a **documented charge at an unpublished rate**, billed on "every byte sent or received to or from the instance, regardless of what state it is in" (§7), which `DATA-PROTOCOL` §3.4 guarantees Mosaic incurs on every commission. It also found **no provider-enforced spend ceiling of any kind** — and §6 and §12 both hold that the ceiling's enforcement, not the price, is the binding constraint. vast.ai therefore fails the tier independently of cost, so pricing it would not make it eligible. The eligibility rule that follows from this is stated in §8.

---

## 5. Together AI and GitHub's own GPU runner — both **Refuted**, for opposite reasons

### 5.1 Together sells nothing this small

Together's raw-compute product is Instant Clusters / GPU Clusters, and [the docs](https://docs.together.ai/docs/instant-clusters) name the hardware as "H100, H200, B200," sold as multi-GPU HGX nodes. [together.ai/pricing](https://www.together.ai/pricing) prices on-demand H100 at **$3.99 per GPU-hour**, H200 at $5.99, B200 at $8.19. The smallest GPU on the menu has 80 GB of VRAM against §1's requirement of well under one.

The disqualifier is not even the compute. The same pricing page lists managed storage at **$0.16/GiB/month**, and [the cluster quickstart](https://docs.together.ai/docs/gpu-clusters-quickstart) sets a **minimum shared-volume size of 1 TiB**. That is 1024 × $0.16 = **$163.84/month in storage before a single GPU-second is bought** — 3.3× the entire ceiling.

**Verdict: Refuted.** Worth recording that Together is nonetheless the best-documented provider on §6, which is why it appears there rather than being dropped here.

### 5.2 GitHub's GPU runner is real, native, and too expensive

This is the "first-party GitHub GPU runner offering" #57 asks about, and it exists: [GitHub's changelog](https://github.blog/changelog/2024-07-08-github-actions-gpu-hosted-runners-are-now-generally-available/) announced GA, and [the larger-runners reference](https://docs.github.com/en/actions/reference/runners/larger-runners) specifies 4 vCPU, **1× NVIDIA Tesla T4 (16 GB)**, 28 GB RAM, 176 GB SSD — the same card as Modal's cheapest row, and ample under §1.

Invocation is as native as it gets: a `runs-on` label, no third-party credential, no API. It is also, under premise 11, the mechanism the map already intends to use for tier refusal, which makes it the tidiest option on paper.

[The runner pricing reference](https://docs.github.com/en/billing/reference/actions-runner-pricing) prices it at **$0.052/minute** for `linux_4_core_gpu` — **$3.12/hour**, or 5.3× Modal's rate for the identical GPU — and adds the two sentences that end it:

> "Included minutes cannot be used for larger runners."
>
> "The larger runners are not free for public repositories."

[#27](https://github.com/NGL321/mosaic/issues/27)'s finding that Actions is free for Mosaic's public repository is a fact about **standard** runners and does not transfer. $50 buys **16.0 hours a month**, against Modal's 135.6 for the same silicon.

**Verdict: Refuted** on price. It remains the right answer to a different question — see §6, where it is one of only two providers that can actually stop.

---

## 6. The spend ceiling — **Contested**, and the least comfortable finding here

#57 states the requirement more sharply than any other in the ticket: *"A ceiling that only exists in a config file this repo owns is a ceiling that fails in exactly the case it is for."* The finding is that the providers sort inversely on this axis — the ones that can stop are the ones that cost too much.

| Provider | Provider-side ceiling | Verdict |
|---|---|---|
| Together | "once the limit is hit and enforced, any usage of together.ai services will be blocked until you increase the limit or buy a credit pack" | Documented hard stop |
| GitHub | "Stop usage when budget limit is reached… This option is available for metered products" | Documented hard stop |
| Modal | Workspace and Environment budgets; "the hard outer cap for the entire Workspace" | Cap documented, behaviour not |
| RunPod | "a default spend limit of $80 per hour across all resources" | Rate limit, not a budget |
| vast.ai | Prepaid, with "a short grace period where your balance may go negative" | Soft |
| Lambda | Nothing found | Unresolved |

**Together and GitHub are the only unambiguous answers.** [Together's usage-limit article](https://support.together.ai/articles/1057636019-setting-a-usage-limit) states the enforcement in behavioural terms and defaults Build Tiers 1–4 to a fixed $100 limit; [GitHub's budgets documentation](https://docs.github.com/en/billing/how-tos/set-up-budgets) offers "Stop usage when budget limit is reached" for metered products, of which Actions is one. Both were refuted on price in §5. That is the shape of the problem.

**Modal documents a cap and not its behaviour.** [The budgets guide](https://modal.com/docs/guide/budgets) describes Workspace budgets that "cap total spend for the Workspace during the current billing cycle" and Environment budgets that cap a single Environment, and calls the Workspace budget "the hard outer cap for the entire Workspace." Neither that page nor [the billing guide](https://modal.com/docs/guide/billing) says what crossing it *does* — refuse new containers, kill running ones, or send an email. "Hard outer cap" is suggestive language, and suggestive language is not the thing #57 asked for. Logged as [#70](https://github.com/NGL321/mosaic/issues/70).

**RunPod is weaker still, and this is what costs it the recommendation.** [Its billing documentation](https://docs.runpod.io/accounts-billing/billing) documents only a *rate* limit — "Runpod accounts have a default spend limit of $80 per hour across all resources" — which at $80/hour is 1,168× the monthly ceiling and protects against nothing Mosaic is exposed to. There is no monthly budget. What remains is the prepaid balance: credits are "deducted in real-time," and at zero, pods with network volumes "are stopped and data is preserved" while those without "are terminated." **With auto-pay left switched off, a prepaid balance is a genuine provider-enforced ceiling** — the account cannot spend money it does not hold. It is also blunt, non-refundable ("Runpod credits are non-refundable and cannot be withdrawn once deposited"), and destroys running work rather than declining new work.

**The practical resolution is that the prepaid balance is the real mechanism on every cheap provider**, and it satisfies #57's requirement in substance if not in form: it lives at the provider, not in this repository, and it fails closed. Fund the account monthly, leave auto-recharge disabled, and treat the provider's budget setting as a second line whose behaviour is unverified.

---

## 7. Storage and egress — **Supported** at the destination, **Unresolved** at the recommended source

The bytes have to leave, because `docs/DATA-PROTOCOL.md` §3.4 routes durable artifacts to Drive at `Desk/mosaic/runs/<run-id>/`. Both ends were checked.

**The destination is free, conditionally.** [The Drive API limits page](https://developers.google.com/workspace/drive/api/guides/limits) states "All standard use of the Google Drive API is available at no additional cost," with a 750 GB/day upload limit and a 1 TB/day per-project quota. It also carries a warning worth recording now rather than discovering later: "Exceeding the quota request limits is planned to incur charges to your Google Cloud billing account later in 2026," with "at least 90 days' notice."

**Egress at the source is free where it is documented, and undocumented where it matters.** RunPod's pricing page states "no fees for data ingress or egress." Lambda's billing page states "you are not charged for ingress or egress." **Modal's pricing page carries no egress, bandwidth or data-transfer line at all** — and an absent line item is not a documented price of zero. Logged as [#71](https://github.com/NGL321/mosaic/issues/71).

Together's page does not mention egress. **vast.ai's does, and says the opposite of free:** its [billing page](https://docs.vast.ai/guides/reference/billing) lists "Bandwidth costs (in \$/TB)" as a separate charge and states that "You are charged bandwidth prices for every byte sent or received to or from the instance, regardless of what state it is in," at a rate set per host and, in its own words, "not shown in your \$cost/hr or \$cost/day pricing breakdowns." A documented charge at an unpublished rate is worse than an absent line item, not better. Established by [#75](https://github.com/NGL321/mosaic/issues/75), retrieved 2026-08-02.

**Volumes are small by construction, which is why this is debt and not a blocker.** `DATA-PROTOCOL` §3.3 forbids storing anything regenerable from a config and a seed, and names "activation tensors, distance matrices, derived features, intermediate representations and re-renderable figures — which is to say most of what an experiment produces by volume." What crosses the wire is checkpoints, metrics and final figures. Modal's own volume storage, if any is used, is $0.09/GiB/month with 1 TiB/month included, per [its pricing page](https://modal.com/pricing) — but under §3.3 the right amount of persistent provider-side storage is zero.

---

## 8. Recommendation — **Supported**

**Take Modal's Starter plan, run on the T4, and fund it as prepaid rather than metered.**

**The eligibility rule this study settles, before the table that applies it:**

> A provider enters the cost tier on a **citable published rate** — a page, retrievable without an account, that states what a unit of compute costs. A marketplace whose prices exist only as live offers is not underdocumented but structurally unpriceable, and is **not eligible**, regardless of what a console or an API sample shows. Samples may be recorded as dated observations; they may not occupy a row in the comparison table.

| Provider | Cheapest adequate GPU | $/hr | Hours inside $50/mo |
|---|---|---|---|
| RunPod (Community) | RTX A5000, 24 GB | $0.16 | 312.5 |
| Modal (with $30 credits) | T4, 16 GB | $0.59 | 135.6 |
| Modal (cash only) | T4, 16 GB | $0.59 | 84.7 |
| Lambda | Quadro RTX 6000, 24 GB | $0.69 | 72.5 |
| GitHub GPU runner | Tesla T4, 16 GB | $3.12 | 16.0 |
| Together | H100, 80 GB | $3.99 | 12.5, less $163.84 storage |

**vast.ai has no row**, by the rule above. Its unauthenticated offer sample of 2026-08-02 spread `dph_total` across $0.0104–$5.3146/hr ([#75](https://github.com/NGL321/mosaic/issues/75)), which is the observation's own argument for why a single sample is not a rate; it is retained there as a dated observation and is not a price this table can carry.

The case for Modal over the cheaper RunPod rests on three things and not on price:

1. **It is the only provider with a first-party, runnable GitHub Actions workflow**, in [`modal-labs/ci-on-modal`](https://github.com/modal-labs/ci-on-modal). Everything else is a CLI and an inference about how to use it in CI.
2. **Scale-to-zero bounds the stall.** §2.2's 60-second scaledown window is the direct answer to #57's $12-versus-$200 worry; RunPod's stopped-pod storage bills at double the running rate, and Lambda's does not stop at all.
3. **$30/month of free credits is 60% of the ceiling**, drawn at zero marginal cost, which is the same structural argument [#27](https://github.com/NGL321/mosaic/issues/27) made for the `CLAUDE_CODE_OAUTH_TOKEN`.

Against it: RunPod is 3.7× cheaper and **documents the digest pinning that premise 12 requires**, which Modal does not. If [#68](https://github.com/NGL321/mosaic/issues/68) comes back negative, the recommendation moves to RunPod and this document's §3 becomes the answer.

**Operationally:** a standard `ubuntu-latest` runner (free on a public repo, per [#27](https://github.com/NGL321/mosaic/issues/27)) holds `MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET` as repository secrets, installs the CLI, and calls `modal run`. The GPU bills separately and per-second. Set a Workspace budget as a second line, and do not rely on it until [#70](https://github.com/NGL321/mosaic/issues/70) is discharged.

---

## What this does not establish

### Sources not reached

- **Tang et al.'s own compute statement.** [The arXiv abstract page](https://arxiv.org/abs/2605.06352) carries no hardware or wall-clock figure and the full text was not opened; §1's sizing therefore comes from the architecture spec by way of `docs/research/2026-07-25-grokking-eca-tda-survey.md`, and the only timing figure quoted is for the CPU persistent-homology step. The one number that converts $/hour into $/month is the one number nobody has measured.
- **vast.ai's actual rates.** Behind console authentication, and by the provider's own statement not published at all. Not a search that failed; a fact the owner declines to publish.
- **Lambda's current filesystem storage price.** [Its billing page](https://docs.lambda.ai/public-cloud/billing/) gives $0.20/GiB/month and immediately disclaims it — "The rate above is used for example purposes and might not reflect current pricing." The real figure appears only at filesystem-creation time, behind an account.
- **GitHub's `container.image` digest syntax.** Three candidate first-party URLs for the job-container reference returned 404 or truncated before the relevant section during this session. Immaterial to the verdict, since GitHub was refuted on price, but it is a hole and not an omission.
- **The literal `runs-on` label for GitHub's GPU runner.** [The larger-runners docs](https://docs.github.com/en/actions/reference/runners/larger-runners) specify the hardware but the label is configured per-organisation rather than reserved, so no fixed string could be quoted.

### Open gaps

- **Concurrency against the ceiling.** Premise 11's fan-out — one agent generating a dataset, several evaluating instruments against it — multiplies GPU-hours by a factor this document never models. Every figure here prices one commission at a time. A ceiling that holds serially and fails under fan-out is the interesting failure, and #55 already flags fan-out mechanics as unspecified.
- **Whether the base image should be built at Modal or pulled.** Modal's model is to *build* an image from a recipe and cache it, which sits oddly against premise 12's "built, never stored — it is regenerable output under `DATA-PROTOCOL` §3.3." The two are probably compatible, since Modal's cache is a cache and not an origin under law 2, but nobody has reasoned it through.
- **Spot and interruptible pricing was priced nowhere.** RunPod's Community Cloud and vast.ai's Interruptible tier both offer large discounts against reliability. For a workload that checkpoints every 500 steps this may be nearly free money, and it was not investigated.
- **The self-hosted tier's arithmetic.** Premise 11 defers it and this document honours the deferral, so the break-even point at which owned hardware beats $50/month of Modal is unknown.
- **Academic pricing.** Modal's pricing page mentions an academic programme worth "up to $10k" in credits. Noah enters a UW degree programme in autumn 2026 under premise 6. Nobody has checked whether that changes the tier entirely.

### Load-bearing ifs

1. **If Modal does not accept a `@sha256:` image reference**, premise 12 is unsatisfiable on the recommended provider and the recommendation moves to RunPod, which documents it. This is the single most likely thing here to be wrong, and it is settled by one run. ([#68](https://github.com/NGL321/mosaic/issues/68))
2. **If a Modal Workspace budget only notifies rather than stops**, then the provider-side ceiling is the prepaid balance and nothing else, and §6's recommendation to disable auto-recharge stops being prudent housekeeping and becomes the entire mechanism. ([#70](https://github.com/NGL321/mosaic/issues/70))
3. **If a commission needs materially more than ~135 GPU-hours a month**, the whole ranking recomputes, because the free-credit advantage that carries Modal over RunPod is a fixed $30 and stops mattering as volume grows. RunPod's 312 hours is the better answer at scale. ([#73](https://github.com/NGL321/mosaic/issues/73))
4. **If Modal charges for egress**, the Drive publication path under §3.4 has an unpriced leg, and the §3.3 discipline of not storing regenerable bytes stops being merely good practice and becomes load-bearing on the budget. ([#71](https://github.com/NGL321/mosaic/issues/71))
5. **If the grokking-scale workload is not GPU-bound at all** — and §1's observation that the persistent-homology step runs in two minutes on CPU is a hint in that direction — then the correct tier might be no GPU tier, and this entire document prices a resource the programme does not need. Nothing checked here rules that out.

---

## Verification Debt

1. **Modal's acceptance of a container image by digest is undocumented** ([#68](https://github.com/NGL321/mosaic/issues/68)). Premise 12 depends on it; docs show only tags and the client source passes the string through unparsed. *Settled by:* one `modal run` against a digest reference.
2. **No provider-enforced monthly spend cap was established for the recommended tier** ([#70](https://github.com/NGL321/mosaic/issues/70)). Modal documents a budget and not its behaviour; RunPod documents an hourly rate limit and no budget. *Settled by:* setting a $5 budget and running past it.
3. **Modal publishes no egress or bandwidth price** ([#71](https://github.com/NGL321/mosaic/issues/71)), leaving the `DATA-PROTOCOL` §3.4 publication leg unpriced on the recommended provider while RunPod and Lambda both document it as free. *Settled by:* a first-party statement, or one measured invoice.
4. **GPU-hours per commission is derived, never measured** ([#73](https://github.com/NGL321/mosaic/issues/73)). This is the exact analogue of the assumed token model in the automation-cost study: the provider ranking survives it, the monthly levels do not. *Settled by:* one instrumented training run — the same run that discharges items 1 and 2.
A fifth item, *vast.ai cannot be priced from first-party documentation at all*, stood here until 2026-08-02 and is **discharged** — see §0.1.

---

## Proposals

None. This document answers a question and proposes no change to an authored file. The tier it recommends becomes a fact about the runner configuration when [#55](https://github.com/NGL321/mosaic/issues/55)'s dispatch machinery is built; it is not a claim that lands in `CONTEXT.md` and carries no tier badge.

---

## Appendix: primary sources, all retrieved 2026-07-31

**Modal**
- Plan pricing — https://modal.com/pricing
- Continuous deployment (GitHub Actions pattern) — https://modal.com/docs/guide/continuous-deployment
- `modal token` CLI reference — https://modal.com/docs/reference/cli/token
- Custom containers guide — https://modal.com/docs/guide/custom-container
- Using existing container images — https://modal.com/docs/guide/existing-images
- `modal.Image` API reference — https://modal.com/docs/reference/modal.Image
- Cold start performance and idle billing — https://modal.com/docs/guide/cold-start
- Billing guide — https://modal.com/docs/guide/billing
- Budgets guide — https://modal.com/docs/guide/budgets
- `modal-labs/ci-on-modal` README (first-party repository) — https://github.com/modal-labs/ci-on-modal
- `modal-labs/ci-on-modal` sample workflow — https://github.com/modal-labs/ci-on-modal/blob/main/.github/workflows/ci.yml
- `modal-client` image implementation (first-party source) — https://github.com/modal-labs/modal-client/blob/main/py/modal/_image.py
- `modal-client` image test suite (first-party source) — https://github.com/modal-labs/modal-client/blob/main/py/test/image_test.py

**RunPod**
- Pricing — https://www.runpod.io/pricing
- Pod pricing and billing granularity — https://docs.runpod.io/pods/pricing
- Managing pods (stop versus terminate) — https://docs.runpod.io/pods/manage-pods
- Accounts and billing (spend limit, credits, auto-pay) — https://docs.runpod.io/accounts-billing/billing
- API keys and scopes — https://docs.runpod.io/get-started/api-keys
- `runpodctl` overview — https://docs.runpod.io/runpodctl/overview
- Deploying a serverless worker (digest pinning) — https://docs.runpod.io/serverless/workers/deploy
- Serverless overview (scale to zero) — https://docs.runpod.io/serverless/overview
- REST API v2 overview — https://docs.runpod.io/api-reference-v2/overview

**Lambda**
- GPU Cloud pricing — https://lambda.ai/service/gpu-cloud
- Public cloud billing — https://docs.lambda.ai/public-cloud/billing/
- On-demand instances and base images — https://docs.lambda.ai/public-cloud/on-demand/
- Access and security (API keys) — https://docs.lambda.ai/public-cloud/access-security/

**vast.ai**
- Pricing — https://vast.ai/pricing
- Billing, per-second charging and stopped-instance storage — https://docs.vast.ai/billing
- Billing reference: bandwidth charged per byte in either direction, at a per-host rate not shown in the cost breakdown — https://docs.vast.ai/guides/reference/billing (retrieved 2026-08-02)
- API authentication — https://docs.vast.ai/api/authentication
- CLI for automation — https://vast.ai/developers/cli
- Create-instance API reference — https://docs.vast.ai/api-reference/instances/create-instance
- Templates and image references — https://docs.vast.ai/templates

**Together AI**
- Pricing — https://www.together.ai/pricing
- Instant Clusters — https://docs.together.ai/docs/instant-clusters
- GPU Clusters quickstart (1 TiB minimum volume) — https://docs.together.ai/docs/gpu-clusters-quickstart
- Billing and credits — https://docs.together.ai/docs/billing-credits
- Setting a usage limit (enforced hard stop) — https://support.together.ai/articles/1057636019-setting-a-usage-limit
- API authentication — https://docs.together.ai/reference/authentication

**GitHub**
- Actions runner pricing reference — https://docs.github.com/en/billing/reference/actions-runner-pricing
- Larger runners reference (GPU hardware spec) — https://docs.github.com/en/actions/reference/runners/larger-runners
- About larger runners (per-minute billing) — https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners
- Setting up budgets (stop usage at limit) — https://docs.github.com/en/billing/how-tos/set-up-budgets
- GPU hosted runners generally available (changelog) — https://github.blog/changelog/2024-07-08-github-actions-gpu-hosted-runners-are-now-generally-available/

**The destination, and the workload**
- Google Drive API usage limits and costs — https://developers.google.com/workspace/drive/api/guides/limits
- Tang, Wang, García-Redondo & Monod (2026), *Topological Signatures of Grokking* — https://arxiv.org/abs/2605.06352
- `docs/research/2026-07-25-grokking-eca-tda-survey.md`, the programme's own record of that method section — https://github.com/NGL321/mosaic/blob/research/grokking-eca-tda-survey/docs/research/2026-07-25-grokking-eca-tda-survey.md
- [#27](https://github.com/NGL321/mosaic/issues/27)'s finding that Actions is free on public repositories with standard runners — https://github.com/NGL321/mosaic/issues/27
