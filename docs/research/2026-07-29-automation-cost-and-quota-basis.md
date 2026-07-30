# The real cost and quota basis for automating async agent work

**Ticket:** [#27 — Establish the real cost and quota basis for automating async agent work](https://github.com/NGL321/mosaic/issues/27)
**Map:** [#1 — Founding charter for Mosaic](https://github.com/NGL321/mosaic/issues/1)
**Date:** 2026-07-29
**Provenance Tier:** machine-produced, unverified. Every figure below was retrieved on **2026-07-29** from a first-party page — `ai.google.dev`, `developers.google.com`, `docs.cloud.google.com`, `one.google.com`, `support.google.com`, `antigravity.google`, `support.claude.com`, `platform.claude.com`, `code.claude.com`, `docs.github.com`, or a first-party GitHub repository — and is quoted, not recalled. Where a page did not state a figure, the item is marked **Unresolved** rather than filled from memory. The cost arithmetic in §5 is *derived*, and its token assumptions are stated as assumptions and are not measured; that is the weakest part of this document and is logged as debt in §7. None of this has been checked by Noah unaided.

> **Volatility warning.** Two of the load-bearing findings (§1.3, §2.1) are *changes made in June 2026* — six weeks before retrieval. This is the class of fact [#27](https://github.com/NGL321/mosaic/issues/27) itself calls "the kind of thing that changes annually," and it changed twice this year. Re-check before writing workflows.

---

## 0. Summary

| Sub-question | Verdict | One-line reason |
|---|---|---|
| **1.1** Does a Google AI Pro / Ultra subscription include API quota usable from CI? | **Refuted** | "Google AI plan benefits for developer usage apply only within the Google AI Studio web interface. Direct use of the Gemini API… is billed and managed separately." |
| **1.2** Does the subscription convert into *any* spendable programmatic value? | **Supported, narrowly** | AI Pro carries Google Developer Program Premium, which is "$10 GenAI and Cloud monthly credit" usable on the Gemini API — conditional on a Cloud Billing account. Ultra: $40 or $100. |
| **1.3** Do Gemini CLI / Code Assist free or subscription tiers grant CI-usable quota? | **Refuted as of 2026-06-18** | "Starting June 18, 2026, Gemini Code Assist IDE extensions stopped serving requests for the Gemini Code Assist for individuals, Google AI Pro, and Google AI Ultra tiers." "This also applies to usage of Gemini CLI." |
| **1.4** Does the successor (Antigravity CLI) work unattended in CI? | **Unresolved** | Headless mode exists and ships a CI example, but "uses your cached credentials. Authenticate once with an interactive `agy` session first." No documented service-account or long-lived credential path. |
| **2.1** Does a Claude Pro / Max plan carry usable quota for the Claude Code GitHub Action? | **Supported** | The action accepts `CLAUDE_CODE_OAUTH_TOKEN`, which "Pro and Max users can generate… by running `claude setup-token` locally"; Anthropic's own help centre names "The Claude Code GitHub Actions integration" as subscription-drawn usage. |
| **2.2** How much subscription quota, numerically? | **Unresolved** | Anthropic publishes limits only as multiples ("5x or 20x more usage than the Pro plan") and never in tokens, messages, or hours. Not computable from public documentation. |
| **3.1** Are GitHub Actions free for Mosaic's public repository? | **Supported** | "GitHub Actions usage is free for self-hosted runners and for public repositories that use standard GitHub-hosted runners." |
| **3.2** Does Mosaic's plausible workload exceed the hosted-runner limits? | **Refuted** (it does not) | 6-hour per-job cap, 20 concurrent jobs on Free, 35-day workflow cap. A research run is tens of minutes, serial. Enormous headroom. |
| **4** Per-run cost for one research ticket | See §5 | Sonnet 5 **$0.51 / $2.55 / $10.74** (low/typical/high). Opus 5 **$1.27 / $6.37 / $26.85**. Gemini 3.1 Pro **$1.50 / $8.40 / $39.60**. Runner minutes **$0.00** on a public repo. |

### The one-line verdict

> **No. The "I already pay Google" argument does not survive.** A consumer Google AI subscription buys no Gemini API quota — benefits are scoped to the AI Studio *web interface* — and since 2026-06-18 it buys no Gemini CLI access either. What it does buy is a $10/month Google Cloud credit, worth roughly *one* typical research run at Gemini 3.1 Pro rates.

**And the symmetric finding inverts the premise in [#24](https://github.com/NGL321/mosaic/issues/24):** "I already pay Anthropic" *does* survive. A Claude Pro or Max subscription authenticates the Claude Code GitHub Action directly, via `claude setup-token`. The cost advantage #24 worried it was losing is on the Anthropic side, not the Google side.

---

## 1. Google — **Refuted**, with one narrow exception

### 1.1 The subscription grants no Gemini API quota

The decisive page is Google's own developer documentation on what an AI plan does for a developer: [ai.google.dev/gemini-api/docs/google-ai-plans](https://ai.google.dev/gemini-api/docs/google-ai-plans) (retrieved 2026-07-29). Verbatim:

> "Google AI plan benefits for developer usage apply only within the Google AI Studio web interface. Direct use of the Gemini API (such as using API keys or external applications) is billed and managed separately."

That sentence answers #27's primary question on its own. A GitHub Actions runner calling the Gemini API with an API key is precisely "external applications," and it is "billed and managed separately."

Corroborating this from the other direction, the [rate-limits page](https://ai.google.dev/gemini-api/docs/rate-limits) (retrieved 2026-07-29) ties quota exclusively to a billing relationship, never to a consumer subscription:

> "Rate limits are applied per project, not per API key."

| Usage tier | Qualification |
|---|---|
| Free | "Active project or free trial" |
| Tier 1 | "Set up and link an active billing account" |
| Tier 2 | "Paid $100 + 3 days from first successful payment" |
| Tier 3 | "Paid $1,000 + 30 days from first successful payment" |

Google One, Google AI Pro, and Google AI Ultra appear **nowhere** in that ladder. The escalator is Cloud spend, and only Cloud spend.

**Verdict: Refuted.** Programmatic access is strictly Gemini API / Vertex AI (now "Gemini Enterprise Agent Platform") on separate billing.

### 1.2 The one thing the subscription *does* convert into — **Supported, narrowly**

The subscription is not worth literally zero to a CI pipeline, and #24's premise slightly overstates. From [developers.google.com/program/plans-and-pricing](https://developers.google.com/program/plans-and-pricing) (retrieved 2026-07-29), the Google Developer Program **Premium** tier — list price **"$19.99/month"** — includes:

> "$10 GenAI and Cloud monthly credit"
>
> "Start building in AI Studio and Vertex AI or any Google Cloud product."

and is obtained without separate purchase by AI subscribers:

> "Included with Google AI Pro"
>
> "$10 per user per month with Google AI Pro"
> "$40 per user per month for Google AI Ultra (20TB)"
> "$100 per user per month for Google AI Ultra (30TB)"

Google's consumer-side page agrees. [support.google.com/googleone/answer/14534406](https://support.google.com/googleone/answer/14534406?hl=en) lists "Google Developer Program premium" among AI Pro benefits and says: **"This includes a $10 Google Cloud credits each month."**

The condition matters, and is stated on the developer page cited in §1.1:

> "Subscribers with Gemini API developer accounts and **Cloud Billing enabled accounts** are eligible to receive monthly Cloud credits from the Google Developer Program for Cloud services, including the Gemini API."

and

> "For users on prepay billing, a paid balance greater than $0 is required in AI Studio to activate promotional credits."

So the credit is real and *is* spendable on the Gemini API — but only once you have already stood up the separately-billed thing #24 assumed you would have to. It is a discount on a bill, not an alternative to having one. At the §5 typical figure of **$8.40 per Gemini 3.1 Pro research run**, $10/month is approximately **one run per month**.

**Verdict: Supported, narrowly.** It converts into about one free run a month, conditional on a live Cloud billing account.

### 1.3 Gemini CLI and Code Assist — **Refuted as of 2026-06-18**

This is the finding most likely to be stale in anyone's head, including the one recorded in #24. From Google's own deprecation notice, [developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals) (page reports last updated **2026-06-23**; retrieved 2026-07-29):

> "Starting June 18, 2026, Gemini Code Assist IDE extensions stopped serving requests for the Gemini Code Assist for individuals, Google AI Pro, and Google AI Ultra tiers."
>
> "This also applies to usage of Gemini CLI."
>
> "Access to Gemini Code Assist IDE extensions and Gemini CLI using Gemini Code Assist Standard or Enterprise subscriptions remain unchanged."

The "Login with Google" option is described as no longer available for IDE extensions or Gemini CLI access. The first-party announcement thread, [google-gemini/gemini-cli discussion #27274](https://github.com/google-gemini/gemini-cli/discussions/27274), confirms the same cut-over and adds what survives:

> "Gemini CLI will also remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys."

So as of the retrieval date there are exactly two Google paths that a CI runner can use:

1. **A paid Gemini API key** (or Vertex / Agent Platform service account) — separate billing, §1.1.
2. **A Gemini Code Assist Standard or Enterprise seat** — a Cloud-billed subscription, not a consumer one. Per [docs.cloud.google.com/gemini/docs/quotas](https://docs.cloud.google.com/gemini/docs/quotas) (retrieved 2026-07-29), agent-mode and Gemini CLI requests are capped at **"Standard: 1500"** and **"Enterprise: 2000"** maximum requests per user per day.

Neither is a consumer subscription.

> **A note on the pre-deprecation state, for the record.** The archived first-party quota table ([`google-gemini/gemini-cli/docs/resources/quota-and-pricing.md`](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/quota-and-pricing.md), retrieved 2026-07-29) shows what *was* true: 1,000 requests/day on a personal Google account, 1,500/day with Google AI Pro, 2,000/day with Ultra, 250/day on an unpaid Gemini API key. Had this document been written in May it would have found a genuine, generous, consumer-subscription-backed CI path. That path closed on 2026-06-18. **This is the single most important reason not to re-derive this answer from memory.**

**Verdict: Refuted** for the free and consumer-subscription tiers, as of 2026-06-18.

### 1.4 Antigravity CLI, the successor — **Unresolved**

Google's migration target is Antigravity. [antigravity.google/pricing](https://antigravity.google/pricing) (retrieved 2026-07-29) shows an Individual (Free) tier with "Basic weekly rate limits," and AI Pro / AI Ultra tiers with "More generous rate limits" and a "Flexible AI credit pool" — no numbers, and no per-token or per-request figures published on that page.

Headless operation exists. [antigravity.google/docs/cli/headless](https://antigravity.google/docs/cli/headless) (retrieved 2026-07-29):

> "Headless mode (also called print mode) sends a single prompt to the agent, streams or returns the response, and exits."
>
> "Headless mode uses your cached credentials. Authenticate once with an interactive `agy` session first."

The page carries a section titled "Example: run the agent in CI," so CI is a contemplated use. But the credential model is the blocker: it requires a prior *interactive* session, and the page documents no service-account, API-key, or long-lived-token path for a fresh ephemeral runner. Whether a cached credential can be lawfully and durably exported into a GitHub Actions secret — and whether Google's terms permit that — is **not answered by any primary page I reached**.

**Verdict: Unresolved.** Do not build on it without settling the credential question first. See §7, item 2.

### 1.5 A terms-of-service consideration for the unpaid path — **Supported**

If anyone is tempted to run Mosaic's research on the Gemini API free tier, the [Gemini API Additional Terms of Service](https://ai.google.dev/gemini-api/terms) (retrieved 2026-07-29) are explicit about what that costs in a different currency:

> "Any Services that are offered free of charge like direct interactions with Google AI Studio or unpaid quota in Gemini API are unpaid Services"

and for unpaid Services, Google uses content to "provide, improve, and develop Google products and services and machine learning technologies," with:

> "human reviewers may read, annotate, and process your API input and output"
>
> "Do not submit sensitive, confidential, or personal information to the Unpaid Services."

Mosaic is a public repository, so the confidentiality exposure is near nil. Recorded for completeness, not as an objection.

---

## 2. Anthropic — **Supported**

### 2.1 A Pro or Max subscription does authenticate the GitHub Action

Two independent first-party sources agree.

**The action's own setup documentation**, [`anthropics/claude-code-action/docs/setup.md`](https://github.com/anthropics/claude-code-action/blob/main/docs/setup.md) (retrieved 2026-07-29), lines 9–10, verbatim:

> "- Either `ANTHROPIC_API_KEY` for API key authentication
> - Or `CLAUDE_CODE_OAUTH_TOKEN` for OAuth token authentication (**Pro and Max users can generate this by running `claude setup-token` locally**)"

repeated at line 223 in the secrets instructions:

> "OAuth Token: Name: `CLAUDE_CODE_OAUTH_TOKEN`, Value: Your Claude Code OAuth token (Pro and Max users can generate this by running `claude setup-token` locally)"

**Anthropic's help centre**, [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) (article dated **June 16, 2026**; retrieved 2026-07-29), names the GitHub Action explicitly as subscription-drawn usage. It lists among Agent SDK usage:

> - "Claude Agent SDK usage in your own projects (Python or TypeScript)"
> - "The `claude -p` command in Claude Code (non-interactive mode)"
> - "**The Claude Code GitHub Actions integration**"
> - "Third-party apps that authenticate with your Claude subscription through the Agent SDK"

**The current billing treatment is the important part, and it is the result of a reversal.** The article's top banner, verbatim:

> "**Update June 15:** We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage **still draw from your subscription's usage limits.** The previously announced monthly credit, which would have been available to eligible claimants in connection with these changes, isn't available. We're working to update the plan to better support how users build with Claude subscriptions. When we have an update, we'll share it before anything takes effect."

The paused-but-documented scheme, preserved on the same page, would have moved this usage onto a separate monthly credit — **$20 (Pro), $100 (Max 5x), $200 (Max 20x)** — and off the subscription limits. It is *not* in effect. So today: **GitHub Action runs consume the same pool as interactive Claude Code and claude.ai chat.**

One caveat worth carrying, from the same page, and it applies to Mosaic's eventual shape rather than to today:

> "**Production automation at scale.** The Agent SDK monthly credit is sized for individual experimentation and automation. Teams running shared production automation should use Claude Platform with an API key for predictable pay-as-you-go billing."

That is guidance, not a prohibition, and it was written about the paused credit scheme. But it is Anthropic saying, in its own voice, where the subscription path stops being the intended one.

**Verdict: Supported.** A Claude Pro or Max plan carries usable quota for the Claude Code GitHub Action, no separate API credits required.

### 2.2 How much quota — **Unresolved**

Anthropic does not publish its consumer limits in any unit that can be divided by a research run. From [What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) (retrieved 2026-07-29):

> "**Max 5x** provides 5 times more usage per session than the Pro plan."
> "**Max 20x** provides 20 times more usage per session than the Pro plan."
> "Max plans also have two weekly usage limits: one that applies across all models and another for Sonnet models only."
> "In addition, to manage capacity and ensure fair access to all users, **we may limit your usage in other ways, such as weekly and monthly caps or model and feature usage, at our discretion.**"

And from [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work):

> "Your usage is affected by several factors, including the length and complexity of your conversations, the features you use, which Claude model you're chatting with, and the effort level you've selected."
>
> "Note that your usage of all different Claude product surfaces (claude.ai, Claude Code, Claude Desktop) counts towards the same usage limit."

Everything is relative to an unpublished base, and the discretionary clause makes even a measured base non-durable. **The number of research tickets a Pro or Max plan will dispatch per week is not derivable from public documentation.** It is measurable empirically — `/usage` reports a breakdown — but that is an experiment, not a citation.

**Verdict: Unresolved**, and unresolvable from documentation. §7, item 1.

### 2.3 One operational trap, worth recording now

From [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) (retrieved 2026-07-29):

> "**Important:** If you have an `ANTHROPIC_API_KEY` environment variable set on your system, Claude Code will use this API key for authentication instead of your Claude subscription (Pro, Max, Team, or Enterprise plans), **resulting in API usage charges rather than using your subscription's included usage.**"

The action's setup doc states the same precedence rule for its federation path: "a static credential takes precedence." A workflow that sets both secrets will silently bill the API. Whatever #24 builds should set exactly one.

### 2.4 Plan prices, for the arithmetic in §5

From [claude.com/pricing](https://www.claude.com/pricing) and the Max plan article (both retrieved 2026-07-29):

| Plan | Price |
|---|---|
| Pro | "$17/month (annual)" / "$20/month (billed monthly)" |
| Max 5x | "$100 per month" |
| Max 20x | "$200 per month" |

---

## 3. GitHub Actions — **Supported** (free), **Refuted** (that Mosaic exceeds it)

### 3.1 Public repositories

From [docs.github.com — About billing for GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions) (retrieved 2026-07-29), verbatim:

> "GitHub Actions usage is **free** for **self-hosted runners** and for **public repositories** that use standard GitHub-hosted runners."

Two words in that sentence are load-bearing and worth stating explicitly, because "free for public repositories" is routinely over-read:

- **"standard"** — larger runners, GPU runners, and runners with extra cores are *not* covered by the public-repository exemption. Mosaic's workload has no reason to leave `ubuntu-latest`.
- **The exemption covers minutes, not everything.** Storage and other billed products follow their own rules.

Private-repository allowances, for the counterfactual only (Mosaic is public):

| Plan | Included minutes/month | Artifact storage |
|---|---|---|
| GitHub Free | 2,000 | 500 MB |
| GitHub Pro | 3,000 | 1 GB |
| GitHub Team | 3,000 | 2 GB |
| Enterprise Cloud | 50,000 | 50 GB |

Standard Linux runner rates, for the same counterfactual: **Linux 2-core x64 $0.006/minute**, Linux 1-core $0.002/min, Linux 2-core arm64 $0.005/min, Windows $0.010/min, macOS $0.062/min.

### 3.2 The limits that actually bind

From [docs.github.com — GitHub Actions limits](https://docs.github.com/en/actions/reference/limits) (retrieved 2026-07-29):

| Limit | Value |
|---|---|
| Job execution time (GitHub-hosted) | "Each job in a workflow can run for up to **6 hours** of execution time." |
| Job execution time (self-hosted) | "up to 5 days" |
| Workflow run time | 35 days max, including "execution duration, and time spent on waiting and approval" |
| Concurrent jobs — Free plan | 20 |
| Concurrent jobs — Pro plan | 40 |
| `GITHUB_TOKEN` API rate | "1,000 requests per hour per repository" |
| Job matrix | "a maximum of 256 jobs per workflow run" |

**Does Mosaic's plausible workload exceed this?** No, and not close. A research ticket of the shape already in the record — [#13's output](2026-07-28-verifying-cited-influences.md) is a 460-line document produced from perhaps 40–80 tool turns — runs in tens of minutes, well inside the 6-hour cap. Mosaic's ticket rate is a handful per day at most, and the tickets are serial by construction (one owner per branch, `PROTOCOL.md` §4), so 20 concurrent jobs is an order of magnitude of slack.

**The one limit worth watching is `GITHUB_TOKEN`'s 1,000 requests/hour**, not because a research run approaches it, but because #24 contemplates comment-triggered agents, and #24's own "unbounded loops" constraint describes exactly the failure mode that would hit it. That is a design constraint for #24, not a cost finding.

**Verdict: 3.1 Supported, 3.2 Refuted** (the workload does not exceed the allowance).

---

## 4. Model prices, as retrieved

All from [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) and [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), both retrieved 2026-07-29. Per million tokens (MTok), USD.

### Anthropic

| Model | Input | 5m cache write | Cache read | Output |
|---|---|---|---|---|
| Claude Opus 5 | $5 | $6.25 | $0.50 | $25 |
| Claude Sonnet 5 (**introductory, through 2026-08-31**) | $2 | $2.50 | $0.20 | $10 |
| Claude Sonnet 5 (from 2026-09-01) | $3 | $3.75 | $0.30 | $15 |
| Claude Haiku 4.5 | $1 | $1.25 | $0.10 | $5 |

**Effective date, recorded per the sourcing rules:** "Introductory pricing of $2/$10 per million input/output tokens is in effect through August 31, 2026, after which the standard pricing of $3/$15 per million input/output tokens will take effect." **Any Sonnet 5 figure in §5 rises by ~50% on 2026-09-01.**

A second dated note from the same page, which matters for cost forecasting and is easy to miss:

> "Claude 4.7 and later models and Claude Mythos Preview use a newer tokenizer… This tokenizer produces approximately **30% more tokens for the same text.**"

Batch API: 50% off both directions. Prompt caching: 1.25x write / 0.1x read (5-minute), 2x write / 0.1x read (1-hour).

### Google

| Model | Free tier | Input | Output |
|---|---|---|---|
| Gemini 3.1 Pro Preview | "Not available" | $2.00 (≤200k prompt) / $4.00 (>200k) | $12.00 (≤200k) / $18.00 (>200k) |
| Gemini 3.6 Flash | "Free of charge" | $1.50 | $7.50 |
| Gemini 3.5 Flash | "Free of charge" | $1.50 | $9.00 |
| Gemini 2.5 Flash | "Free of charge" | $0.30 (text/image/video), $1.00 (audio) | $2.50 |

Note the first row: **the strongest Gemini model has no free tier at all.** The free tier reaches only Flash-class models.

**Unresolved:** the free tier's *numeric* rate limits. The rate-limits page no longer publishes an RPM/TPM/RPD table and instead says "View your active rate limits in AI Studio" — which is behind auth. So "how many free Flash runs per day" is not answerable from public documentation. §7, item 3.

**Unresolved:** Gemini context-caching prices were not retrieved, so §5's Gemini figures are computed *without* a caching discount and are therefore biased high relative to the Anthropic figures, which assume caching. See §5's honesty note.

---

## 5. Per-run cost for one research ticket — the arithmetic

### 5.1 The model of a run (all of this is assumption)

> **These are assumptions, not measurements.** Nothing in the Mosaic record measures the token cost of a research ticket. The bands below are constructed from a plausible shape of agentic run and should be treated as an order-of-magnitude estimate whose *ratios* between options are more trustworthy than its absolute values. Discharging this by instrumenting one real run is §7, item 4.

An agentic run resends its accumulated context on every turn, so cumulative input ≈ (turns × average context), not (context). That is the term that dominates, and it is the term people forget.

| Parameter | Low | Typical | High |
|---|---|---|---|
| Tool turns | 20 | 60 | 150 |
| Average context per turn | 30k tok | 60k tok | 120k tok |
| **Cumulative input** | **0.6M tok** | **3.6M tok** | **18M tok** |
| Cache hit fraction (Anthropic) | 90% | 90% | 90% |
| Total output tokens | 25k | 100k | 300k |
| Wall-clock runtime | 8 min | 25 min | 90 min |

*Calibration note:* the "typical" column is sized against the [#13 verification document](2026-07-28-verifying-cited-influences.md) — roughly two dozen primary sources fetched, several read at length, a 460-line output. That is Mosaic's actual research-ticket shape, so it is the right anchor. The "high" column is a ticket that goes long, thrashes, and re-reads.

### 5.2 Claude Sonnet 5 via the GitHub Action (introductory pricing)

Cache reads at $0.20/MTok, cache writes at $2.50/MTok, output at $10/MTok.

**Typical:**
- cache reads: 3.6M × 0.90 = 3.24M × $0.20/M = **$0.648**
- cache writes: 3.6M × 0.10 = 0.36M × $2.50/M = **$0.900**
- output: 0.1M × $10/M = **$1.000**
- **total ≈ $2.55**

**Low:** (0.54M × 0.20) + (0.06M × 2.50) + (0.025M × 10) = 0.108 + 0.150 + 0.250 = **$0.51**
**High:** (16.2M × 0.20) + (1.8M × 2.50) + (0.3M × 10) = 3.240 + 4.500 + 3.000 = **$10.74**

From 2026-09-01 these become roughly **$0.76 / $3.82 / $16.11** at standard Sonnet 5 pricing.

### 5.3 Claude Opus 5 via the GitHub Action

Cache reads $0.50, cache writes $6.25, output $25.

**Typical:** (3.24M × 0.50) + (0.36M × 6.25) + (0.1M × 25) = 1.620 + 2.250 + 2.500 = **$6.37**
**Low:** (0.54M × 0.50) + (0.06M × 6.25) + (0.025M × 25) = 0.270 + 0.375 + 0.625 = **$1.27**
**High:** (16.2M × 0.50) + (1.8M × 6.25) + (0.3M × 25) = 8.100 + 11.250 + 7.500 = **$26.85**

### 5.4 Gemini 3.1 Pro via a paid Gemini API key

No caching discount applied (prices not retrieved — see §4). Input $2.00, output $12.00, assuming prompts stay under 200k tokens; the "high" row would partly cross into the $4.00/$18.00 band and so is understated.

**Typical:** (3.6M × $2/M) + (0.1M × $12/M) = 7.200 + 1.200 = **$8.40**
**Low:** (0.6M × 2) + (0.025M × 12) = 1.200 + 0.300 = **$1.50**
**High:** (18M × 2) + (0.3M × 12) = 36.000 + 3.600 = **$39.60**

### 5.5 Gemini 2.5 Flash via a paid Gemini API key

Input $0.30, output $2.50, no caching discount.

**Typical:** (3.6M × 0.30) + (0.1M × 2.50) = 1.080 + 0.250 = **$1.33**
**Low:** **$0.24** · **High:** **$6.15**

Cheapest option on the board — and the one where the model doing Mosaic's primary-source reading is a Flash-class model. That is a research-quality decision, not a cost decision, and this document does not make it.

### 5.6 Runner minutes

**$0.00** for all rows. Mosaic is a public repository on standard hosted runners (§3.1). For the private-repository counterfactual at $0.006/min on Linux 2-core: **$0.05 / $0.15 / $0.54** per run, against 2,000 free minutes/month on GitHub Free — about 80 typical runs a month before a single minute is billed.

### 5.7 The table

Per one research ticket, USD, retrieved 2026-07-29.

| Option | Low | **Typical** | High | Runner | Subscription needed |
|---|---|---|---|---|---|
| **Claude Pro/Max subscription** (`CLAUDE_CODE_OAUTH_TOKEN`) | $0 marginal | **$0 marginal** | $0 marginal | $0 | $20–$200/mo; **quota per run Unresolved** (§2.2) |
| Claude Sonnet 5, API key | $0.51 | **$2.55** | $10.74 | $0 | none |
| Claude Opus 5, API key | $1.27 | **$6.37** | $26.85 | $0 | none |
| Gemini 3.1 Pro, paid API key | $1.50 | **$8.40** | $39.60 | $0 | none; $10/mo credit ≈ 1 run |
| Gemini 2.5 Flash, paid API key | $0.24 | **$1.33** | $6.15 | $0 | none |
| Gemini CLI on Google AI Pro | — | — | — | — | **Not available since 2026-06-18** (§1.3) |
| Antigravity CLI headless | — | — | — | $0 | **Unresolved** — no unattended credential path documented (§1.4) |

**Reading the table honestly:** the Gemini figures are inflated relative to the Anthropic ones because no caching discount was applied to them (§4). If Gemini context caching offers a comparable 10x read discount, Gemini 3.1 Pro typical would fall toward roughly $2.50 and the two would be near parity. **The ranking of Gemini against Sonnet is therefore not established by this document.** What *is* established, and does not depend on the caching gap, is the top row: on a Claude subscription the marginal cost per run is zero, and no Google option offers that.

---

## 6. What this means for #24

Stated narrowly, as findings and not as a recommendation — the platform decision is #24's.

1. **The premise #24 flagged is confirmed, and then some.** "I already pay Google" does not convert into CI quota (§1.1), and since 2026-06-18 it does not even convert into Gemini CLI access (§1.3). The apparent cost advantage does disappear.
2. **The symmetric premise #24 did not check goes the other way.** A Claude subscription *does* authenticate the GitHub Action (§2.1), at zero marginal cost per run. #24 recommended Actions + the Claude Code action for reasons independent of cost; the cost analysis now supports rather than merely tolerates that recommendation.
3. **The subscription path is soft, though.** Anthropic paused a change that would have moved this usage off subscription limits (§2.1), publishes no numeric quota (§2.2), and says in its own voice that shared production automation should use an API key. Treat the subscription as the cheap default and an API key as the fallback, and design the workflow so switching is a one-secret change — noting §2.3's precedence trap.
4. **Runner minutes are a non-issue** while Mosaic is public and on standard runners (§3). #24's "cost visibility" constraint is entirely about tokens.
5. **A hybrid is available and cheap.** Nothing prevents Flash-class or Haiku-class models on the mechanical CI checks #24 folds in (front-matter validation, link integrity, commit-type consistency) while research tickets run on a stronger model. Those checks are near-free at any of §4's prices, and most of them do not need a model at all.

---

## 7. Surviving Verification Debt

Items this document could not settle, and what would settle them.

1. **How many research tickets a Claude Pro or Max plan actually dispatches per week.** Anthropic publishes limits only as unlabelled multiples with a discretionary clause (§2.2). *What would settle it:* an empirical measurement — dispatch a real ticket through the action on a subscription token and read `/usage`. This is a one-run experiment, not a reading exercise, and it is the highest-value item here because it is the only remaining unknown in the recommended path.
2. **Whether Antigravity CLI can be authenticated in an ephemeral CI runner at all, and whether Google's terms permit it.** The headless docs require a prior interactive session and document no service-account path (§1.4). *What would settle it:* an Antigravity terms-of-service page or an authentication doc describing a non-interactive credential. I did not find one; the pricing page is silent and the CLI docs are silent.
3. **The Gemini API free tier's numeric rate limits.** The rate-limits page has stopped publishing the RPM/TPM/RPD table and defers to AI Studio, which is behind auth (§4). Explicitly unreachable, not merely unfound. *What would settle it:* a signed-in read of the AI Studio limits page, recorded with a date.
4. **Gemini context-caching prices.** Not retrieved, which is why §5's Gemini rows carry no caching discount and the Gemini-vs-Sonnet ranking is not established. *What would settle it:* the caching section of `ai.google.dev/gemini-api/docs/pricing`, read directly.
5. **The token model in §5.1 is entirely assumed.** Turn counts, context growth, and the 90% cache-hit fraction are constructed, not measured. Every absolute figure in §5 inherits that uncertainty; the *ratios* are more robust than the levels, because the same assumed workload is priced under every option. *What would settle it:* instrument one real research run and replace the table. Same experiment as item 1 — it discharges both.
6. **Volatility.** Two load-bearing facts changed in June 2026 (§1.3, §2.1), one Anthropic price changes on 2026-09-01 (§4), and Anthropic reserves the right to change consumer limits "at our discretion" (§2.2). Anything in this document older than a quarter should be re-fetched before it decides anything. Recorded here so a future reader does not mistake a dated retrieval for a standing fact.
7. **Not investigated:** Vertex AI / Gemini Enterprise Agent Platform pricing for Claude models, GitHub Models, and self-hosted runners on owned hardware. Each is a live option for #24 and none was in this ticket's scope.

---

## Appendix: primary sources, all retrieved 2026-07-29

**Google**
- Google AI Plans for developers — https://ai.google.dev/gemini-api/docs/google-ai-plans
- Gemini API rate limits — https://ai.google.dev/gemini-api/docs/rate-limits
- Gemini API pricing — https://ai.google.dev/gemini-api/docs/pricing
- Gemini API Additional Terms of Service — https://ai.google.dev/gemini-api/terms
- Google Developer Program plans & pricing — https://developers.google.com/program/plans-and-pricing
- Google AI plans (Google One) — https://one.google.com/about/google-ai-plans/
- Use Google AI Pro benefits — https://support.google.com/googleone/answer/14534406?hl=en
- Gemini Code Assist consumer accounts deprecation (page updated 2026-06-23) — https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals
- Gemini for Google Cloud quotas and limits — https://docs.cloud.google.com/gemini/docs/quotas
- Gemini CLI quota and pricing (first-party repo, archival) — https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/quota-and-pricing.md
- Transitioning Gemini CLI to Antigravity CLI (first-party announcement) — https://github.com/google-gemini/gemini-cli/discussions/27274
- Antigravity pricing — https://antigravity.google/pricing
- Antigravity CLI headless mode — https://antigravity.google/docs/cli/headless

**Anthropic**
- claude-code-action setup guide (first-party repo) — https://github.com/anthropics/claude-code-action/blob/main/docs/setup.md
- Claude Code GitHub Actions — https://code.claude.com/docs/en/github-actions
- Use the Claude Agent SDK with your Claude plan (dated 2026-06-16) — https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
- Use Claude Code with your Pro or Max plan — https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
- What is the Max plan? — https://support.claude.com/en/articles/11049741-what-is-the-max-plan
- How do usage and length limits work? — https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
- Claude pricing — https://www.claude.com/pricing
- Claude Platform pricing — https://platform.claude.com/docs/en/about-claude/pricing

**GitHub**
- About billing for GitHub Actions — https://docs.github.com/en/billing/concepts/product-billing/github-actions
- GitHub Actions limits — https://docs.github.com/en/actions/reference/limits
