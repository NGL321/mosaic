---
ticket: 75
map: 55
date: 2026-08-02
kind: verification
tier: T3
session: unrecorded
sources: 19
debt: [117, 118]
supersedes: null
---

# vast.ai publishes no price, and no further reading will produce one

**Ticket:** [#75 — vast.ai cannot be priced from first-party documentation at all](https://github.com/NGL321/mosaic/issues/75)
**Map:** [#55 — Map: The research loop](https://github.com/NGL321/mosaic/issues/55)
**Date:** 2026-08-02

**Provenance.** Machine-produced, unverified. Every quotation below was retrieved on **2026-08-02** from a first-party vast.ai property — `vast.ai` or `docs.vast.ai` — and is quoted, not recalled. The documentation corpus was not sampled: the site's own index, [`docs.vast.ai/llms.txt`](https://docs.vast.ai/llms.txt), enumerates 634 pages, and **all 131 pages under `guides/`, `pricing` and `host/` were retrieved in full as Markdown and searched exhaustively** for currency amounts, digest references and spend-cap language. The negative claims in §1 and §2 are therefore claims about a complete sweep of that subtree, not about a search that stopped early. No account was created, nothing was logged into, and nothing was purchased. One finding — §6 — comes from an unauthenticated HTTP GET against a first-party host rather than from a document, and is labelled as an observation rather than a citation throughout. None of this has been checked by Noah unaided.

> **This document's purpose is to close a search, not to open one.** [#57](https://github.com/NGL321/mosaic/issues/57) found vast.ai unpriceable and logged it as debt. The discharge of that debt is not a price; it is a *record of why there will never be one*, so that the next reader does not spend an afternoon rediscovering it. The precedent for recording an unreachable source as a finished result is [#13](https://github.com/NGL321/mosaic/issues/13).

---

## 0. Verdict

| Sub-question | Verdict | Where argued |
|---|---|---|
| **a** Does vast.ai publish any citable price — a floor, a reference rate, or an SKU table? | **Refuted** — no rate, no floor, no table exists on any first-party page | §1, §2 |
| **a′** Is #57's quotation "Prices are set by the market, not by Vast" accurate, and does the marketplace framing hold? | **Established** — confirmed verbatim today, and restated in the docs in stronger words | §1 |
| **b** Is digest pinning of container images documented, denied, or unmentioned? | **Unresolved** — unmentioned in the API reference; the one published format statement excludes it without discussing it | §4 |
| **c** Is any egress or bandwidth fee documented? | **Refuted** — #57's finding that vast.ai's pages "do not mention egress" is wrong; bandwidth is documented as a charge on every byte, in both directions, at an unpublished rate | §3 |
| **d** Does vast.ai document any provider-enforced spend cap or budget mechanism? | **Refuted** — none exists; every documented balance control raises the balance rather than capping the spend | §5 |
| **e** Is #57's claim that "live offers exist only in the authenticated console" correct? | **Refuted** — the offer table is served to unauthenticated GET requests, contradicting vast.ai's own documented auth requirement | §6 |
| **f** Can vast.ai be priced from first-party *documentation*? | **Established** as impossible — the party that owns the fact declines to publish it, by design and in writing | §1, §2, §3, §7 |
| **g** What does a 24 GB-class card cost per hour on vast.ai? | **Unresolved** — a dated sample is obtainable and is recorded in §6; a *rate* is not, and the sample must never be quoted as one | §6, §7 |

> **vast.ai is not underdocumented; it is structurally unpriceable.** The price of a vast.ai instance is not a fact vast.ai possesses and withholds — it is a fact that does not exist until a host lists a machine and a renter queries the market at an instant. Three of the four cost components (compute, storage, bandwidth) are set independently per machine, so even a perfect snapshot is a sample of three dispersions at one moment, not a rate. Mosaic can obtain such a sample today without an account (§6). It cannot obtain a citation, ever, and should stop trying.

---

## 1. The pricing page states that there is no price, and the docs say it twice more

[vast.ai/pricing](https://vast.ai/pricing) (retrieved 2026-08-02) is titled "GPU Pricing — Live Platform Rates" and contains, in its "Why Vast Pricing Works" block, the sentence [#57](https://github.com/NGL321/mosaic/issues/57) quoted — confirmed verbatim, with the clause that follows it:

> "**Supply & Demand Pricing.** Prices are set by the market, not by Vast. More supply means lower prices — and you always see the real rate."

The three tiers are named and described in relative terms only, exactly as #57 recorded:

> "**On-Demand** — Most Popular. Guaranteed uptime. Best for production."
> "**Interruptible** — Best Value. 50%+ cheaper. Best for batch training."
> "**Reserved** — Up to 50% Off. Long-term commitment. Best for steady workloads. 1, 3, or 6 month terms."

Every comparative on that page — "50%+ cheaper," "Up to 50% Off" — is relative to a base the page never states. The page also carries the strings "Live GPU Prices," "Real-time pricing from across the Vast.ai platform," and "Pricing Calculator." **All three are client-rendered widgets; the served HTML document contains no currency amount at all.** Its Next.js payload (`__NEXT_DATA__`) carries an empty `pageProps`, so there is no price embedded in the page for a citation to point at even in principle. This matters for the ticket's framing: the page does not merely omit a rate — it advertises rates and then declines to place any in the document.

The documentation site says the same thing more explicitly, and in a sentence worth having on the record because it forecloses the question rather than merely leaving it open. From [docs.vast.ai/guides/pricing](https://docs.vast.ai/guides/pricing) (retrieved 2026-08-02):

> "Unlike traditional cloud providers with fixed pricing, Vast.ai uses a **marketplace model** where hosts set their own prices. This creates competitive rates without static price quotes-the market determines pricing in real-time."

"**without static price quotes**" is vast.ai, in its own voice, describing the absence of the thing #57 went looking for as a product feature. The same page directs every price question to a live query rather than a document:

> "**Web**: [Dashboard](https://cloud.vast.ai/create/) shows real-time prices"
> "**CLI**: Use `vastai search offers` to query prices programmatically"
> "**API**: Query programmatically via the [search offers endpoint](/api-reference/hello-world)"

And it names the dispersion directly, which is why an average would be as unciteable as a rate:

> "Rates vary significantly based on: **GPU model** … **GPU quantity** … **Host reliability** … **Geographic location** … **Market conditions**"

The billing reference adds the same warning for the two non-compute components, from [docs.vast.ai/guides/reference/billing](https://docs.vast.ai/guides/reference/billing) (retrieved 2026-08-02):

> "The prices for base rental, storage, and bandwidth vary considerably from machine to machine, so make sure to check them."

**Verdict: Refuted** on sub-question **a** — no floor, no reference rate, no SKU table exists. **Established** on **a′** — #57's quotation is accurate and its reading of it was correct.

## 2. The three numbers vast.ai does publish, and why none of them is a price

An exhaustive scan of all 131 retrieved pages under `guides/`, `pricing` and `host/` for currency amounts returns a small, enumerable set. It is worth listing in full, because "vast.ai publishes no numbers" would be false and "vast.ai publishes no *price*" is the true and stronger claim.

| Published figure | Source | Why it is not a price |
|---|---|---|
| "The minimum deposit amount on Vast.ai is \$5." | [quickstart](https://docs.vast.ai/guides/get-started/quickstart), retrieved 2026-08-02 | A floor on a *prepayment*, not on a rate. It bounds the smallest experiment, not the cost of one. |
| "storage price in \$/GB/month (price for inactive instances), **default: \$0.10/GB/month**" | [`vastai list machine`](https://docs.vast.ai/host/cli/list-machine), retrieved 2026-08-02 | A CLI default applied to a **host's listing** when the host omits the flag. It is a supply-side default, not a rate charged to renters, and any host may override it. |
| `price` — "Bid price per machine (in \$/hour). Only for interruptible instances," `minimum: 0.001`, `maximum: 128` | [create-instance OpenAPI schema](https://docs.vast.ai/api-reference/instances/create-instance), retrieved 2026-08-02 | Validation bounds on a *bid the renter submits*. They describe what the API will accept, not what anything costs. |

Everything else that looks like a price is explicitly a worked example. [Reserved Instances](https://docs.vast.ai/guides/instances/choosing/reserved-instances) (retrieved 2026-08-02) computes a refund from "On-demand: \$1/hr → \$720/month," under a heading that reads "**Example:**"; [the hosting overview](https://docs.vast.ai/host/hosting-overview) (retrieved 2026-08-02) walks a host through relisting "a 4×A100 machine at \$2.00/GPU/hr" and then at "\$2.50/GPU/hr" purely to illustrate that two contracts can coexist at different prices. Neither is a quotation of a market rate, and treating either as one would be a worse error than reporting nothing.

The serverless product, which on other platforms carries its own rate card, explicitly declines to have one. From [docs.vast.ai/guides/serverless/pricing](https://docs.vast.ai/guides/serverless/pricing) (retrieved 2026-08-02):

> "Vast Serverless offers pay-per-second pricing for all workloads at the same price as Vast.ai's non-Serverless GPU instances."

A pricing page whose entire content is "the same as the other thing, which also has no price" is the clearest available demonstration that the absence is structural rather than an oversight.

**Verdict: Refuted** on sub-question **a**, restated with the exceptions enumerated so a later reader does not mistake one of the three for a rate.

## 3. Bandwidth is documented as a charge — #57's egress finding is wrong, in the direction that matters

[#57](https://github.com/NGL321/mosaic/issues/57) §7 recorded that "Neither vast.ai's nor Together's pages mention egress either," and #75 repeated it as "no egress fee is mentioned on the billing page — an absence, not a documented zero." **The first half is refuted; the caution in the second half survives and is strengthened.**

From [docs.vast.ai/guides/reference/billing](https://docs.vast.ai/guides/reference/billing) (retrieved 2026-08-02), under the heading "Pricing," verbatim:

> "There are separate prices and charges for:
> * Active rental (GPU)  (in \$/hr)
> * Storage costs (in \$/GB/hr)
> * **Bandwidth costs (in \$/TB)**"

and:

> "You are charged bandwidth prices for **every byte sent or received to or from the instance, regardless of what state it is in.**"

The [billing FAQ](https://docs.vast.ai/guides/reference/faq/billing) (retrieved 2026-08-02) repeats it independently, and the same page states the trap that makes an unquantified bandwidth charge operationally dangerous rather than merely unknown:

> "You may be see your Vast credit decline at a greater rate than expected due to upload and downloads costs, **which is not shown in your \$cost/hr or \$cost/day pricing breakdowns** as it is charged on a usage basis and not a constant rate."

The [pricing guide](https://docs.vast.ai/guides/pricing) adds that the charge is bidirectional and per-host:

> "Data transfer costs vary by host and include both upload and download traffic. Charges apply per byte transferred. Review bandwidth rates during instance selection as these can significantly impact total costs for data-intensive workloads."

So vast.ai's egress position is the worst of the three possibilities for a cost study. It is not "free" (as RunPod's and Lambda's pages state), and it is not "unmentioned" (as #57 believed, and as Modal's page genuinely is). It is **documented as a non-zero charge whose rate is not published, is set per machine, is levied in both directions, and is invisible in the hourly figure the console displays.** #57's own principle — an absence is not a documented zero — applies here in the harder form: a *documented presence at an unpublished rate* is strictly worse than an absence, because a reader who assumed zero has been contradicted in writing.

The host-side CLI confirms that bandwidth price is a per-listing field rather than a platform rate. [`vastai list machine`](https://docs.vast.ai/host/cli/list-machine) (retrieved 2026-08-02) documents `-u`, "price for internet upload bandwidth in \$/GB," and `-d`, "price for internet download bandwidth in \$/GB," as flags the host sets — and, unlike storage, **neither carries a documented default.**

**Verdict: Refuted** on sub-question **c**, correcting #57.

## 4. Digest pinning is unmentioned in the API and excluded by the one published format rule

[#55](https://github.com/NGL321/mosaic/issues/55) premise 12 requires that a provider accept a container image by digest. The [create-instance API reference](https://docs.vast.ai/api-reference/instances/create-instance) (retrieved 2026-08-02) documents the `image` field in full as:

> `image` (required, string) — "Docker image to use for the instance."

with a schema default and request example of `vastai/base-image:@vastai-automatic-tag`. That is the entirety of the specification. It imposes no format, forbids nothing, and — decisively for this ticket — **says nothing about tags, digests, or `sha256:` references either way.** A sweep of all 131 retrieved pages for `digest`, `@sha256` and `image@` returns only HMAC helpers in the [webhooks guide](https://docs.vast.ai/guides/reference/notification-webhooks); the concept of a content-addressed image reference appears nowhere in vast.ai's documentation.

The nearest thing to a ruling is in the console template editor's documentation, [Template Settings](https://docs.vast.ai/guides/templates/template-settings) (retrieved 2026-08-02):

> "**Image Path:Tag** — Here is where you can define the docker image to run. This field **must be in the format `repository/image_name:tag`.**"

A digest reference (`repository/image_name@sha256:…`) is not of that form. This is an exclusion, not a denial: the sentence is a positive format requirement written by someone who was not thinking about digests, and it constrains the *template editor*, whereas the API's `image` field carries no format constraint at all. Whether the API accepts a digest is therefore an empirical question about an undocumented behaviour — the exact shape of question that a document cannot answer and a five-minute paid experiment could.

The same page documents a mechanism that runs directly against pinning, and is worth recording because it makes the gap load-bearing rather than academic:

> "There is also a special `[Automatic]` tag you can use. With this selected, the machine you choose for your instance will pull the most recent docker image that is compatible with that machine's own CUDA version."

vast.ai's *default* image reference — the one in the API's own example — uses this mechanism. The platform's documented, recommended path for image selection is one in which the bytes that run are chosen by the machine at launch time, which is the precise property digest pinning exists to eliminate.

**Verdict: Unresolved** on sub-question **b** — undocumented rather than denied, and the one adjacent format statement excludes digests without addressing them.

## 5. There is no spend cap; the documented mechanisms are top-ups, not ceilings

Sub-question **d** admits a clean negative. A sweep of all 131 retrieved pages for `spending limit`, `spending cap`, `budget limit`, `maximum spend` and `hard cap` returns **nothing**. What vast.ai documents instead, on [the billing page](https://docs.vast.ai/guides/reference/billing) and in [Notifications](https://docs.vast.ai/guides/reference/notifications) (both retrieved 2026-08-02), is a set of controls that all point the other way:

- **Prepaid credit** is the nearest thing to a ceiling, and vast.ai explicitly documents it *failing* as one: "the system allows a short grace period where your balance may go negative before deletion occurs — the length of this buffer is calculated based on your account's average daily spend. Accounts with higher historical spend receive a proportionally larger buffer." The buffer grows with spend, which is the opposite of a cap's behaviour.
- **Autobilling** is a threshold that triggers a *charge*: "Set your autobilling threshold to approximately your average daily or weekly spend." Its documented purpose is to prevent the balance from constraining usage. The page's own Warning is unambiguous about the direction: "When your balance drops to your autobilling threshold or goes negative, your card will automatically be charged."
- **Low-balance notification** is an email, with no enforcement: the Notifications page lists `client:low_credit` among the "Billing" group and describes setting "the credit threshold that should trigger the warning."
- **The "Budget" search filter** — "Maximum price you're willing to pay per hour," from [Choosing Instances Overview](https://docs.vast.ai/guides/instances/choosing/overview) (retrieved 2026-08-02) — filters the offer list before rental. It does not bind anything after.
- **The interruptible `price` bid** caps a per-hour rate for one instance, not a total.

The only documented behaviour that stops spending is running out of credit with no card on file, and vast.ai documents its consequence as data loss, not as a budget being honoured: "Your instances and stored data will be **destroyed** to prevent indefinite unpaid usage." Running Mosaic's ceiling on that mechanism would mean accepting deletion of the artefact as the enforcement action.

**Verdict: Refuted** on sub-question **d**. On #57's §6 axis — "can a hard spend ceiling be set at the provider" — vast.ai is a documented **no**.

## 6. The ticket's premise is wrong on one point: the offer table is served without authentication

#75 and #57 both assert that "live rates exist only in the authenticated console." That is refuted, and the correction changes which of the ticket's two options is cheap.

vast.ai's [API introduction](https://docs.vast.ai/api-reference/introduction) (retrieved 2026-08-02) is unambiguous about its own contract:

> "All endpoints require `Authorization: Bearer $VAST_API_KEY`. Get your key from the [Keys page](https://cloud.vast.ai/manage-keys/)."

The [search offers reference](https://docs.vast.ai/api-reference/search/search-offers) (retrieved 2026-08-02) documents the offer query as `POST /api/v0/bundles` under that requirement. **In fact, an unauthenticated `GET https://console.vast.ai/api/v0/bundles/` returns a JSON offer table** — HTTP 200, `application/json`, `server: gunicorn`, `Date: Sun, 02 Aug 2026 18:58:41 GMT`, 189,160 bytes, 64 offers, no credential of any kind sent. The same payload is served from `cloud.vast.ai`. No account was created and nothing was rented to obtain it.

**What that observation is worth, stated carefully.** It is first-party data from a vast.ai host, and it is *not* a citation. It is an **undocumented** endpoint behaviour that contradicts vast.ai's own published auth requirement, which means it carries no stability commitment whatsoever and may be closed without notice or announcement. The response is also a **default slice, not the market**: 64 offers across 16 GPU models, unfiltered and unsorted, out of a marketplace the pricing page describes as spanning "40+ data centers" and "68+ GPU Types." Six of the 64 were 24 GB-class cards. So it is a sample of a truncated default view of three independent price dispersions, taken at one instant.

Recorded as a **dated observation, 2026-08-02 18:58 UTC**, in the units the endpoint reports, for the 24 GB class at one GPU — and never to be quoted as a rate:

| GPU | Location | `dph_total` ($/hr) | Storage ($/GB/mo) | Up ($/TB) | Down ($/TB) | Rentable |
|---|---|---|---|---|---|---|
| RTX 3090 | Croatia, HR | 0.0800 | 0.0003 | 0.00 | 0.00 | yes |
| RTX PRO 4000 | Utah, US | 0.1356 | 0.2000 | 4.00 | 2.67 | yes |
| RTX 4090 | CN | 0.1356 | 0.2000 | 1.33 | 1.33 | **no** |

Across the whole 64-offer slice, `dph_total` ranged from **$0.0104 to $5.3146 per hour** — a 500-fold spread within one unfiltered response, which is the single most useful number here. It is also the number that shows why no average would be citable.

The three cost components behave exactly as §1 and §3 predicted: storage varied by a factor of ~660 between two offers of the same GPU class, and bandwidth ranged from **$0.00/TB to $4.00/TB** with upload and download priced independently on the same machine. The cheapest offer in the sample was also the one with effectively free bandwidth, and the second-cheapest charged $4.00/TB up — so the ordering by headline `dph_total` is not the ordering by total cost, and no headline figure can be corrected into one without knowing the workload's byte volume.

**Verdict: Refuted** on sub-question **e**. **Unresolved** on **g** — a sample is obtainable, a rate is not.

## 7. The consequence: what Mosaic can actually decide

The ticket names two decisions and asks for a recommendation. §6 changes their relative costs, so both are restated at today's prices.

**Option A — treat a console read as a dated sample.** Cheaper than #75 assumed: it needs no account, no card, and no console (§6). But its output is what §6 already contains, and its defects are not defects of effort. A sample cannot be re-derived by a later reader (the market has moved), cannot be checked (the endpoint is undocumented and may be gone), and cannot be compared like-for-like against a row such as Modal's or RunPod's published rate without a category error — one is a commitment, the other is a weather report. Adopting Option A means putting an observation with a 500-fold internal spread and an unpriced bandwidth term next to a rate card and calling the two commensurable.

**Option B — rule that a provider whose price cannot be cited is not eligible for the tier.** Needs nothing external, is a decision Mosaic can take unaided, and is durable: it does not go stale, because it is a statement about what evidence Mosaic accepts rather than about what anything costs. It also generalises — Together AI and any future marketplace entrant are decided by the same rule rather than by a fresh argument each time. Its cost is that it forecloses what may genuinely be the cheapest compute on the board; §6's sample suggests a 24 GB card at $0.08/hr, roughly half [#57](https://github.com/NGL321/mosaic/issues/57)'s cheapest cited row.

**The recommendation is Option B, with §6 retained as an observation and explicitly barred from the tier table.** Four reasons, in order of weight.

1. **The ceiling is the binding constraint, not the price.** #57's own verdict says the loop fits under $50/month "with room — the binding constraint is the ceiling's enforcement, not the price." §5 finds vast.ai has no provider-enforced ceiling at all, and documents a grace buffer that *grows with spend*. vast.ai therefore fails on #57's actual binding constraint independently of what it costs. **Pricing it would not make it eligible, so the pricing question is moot** — which is the cleanest possible discharge of a debt item.
2. **A cheap headline with an unbounded bandwidth term is not cheap, it is unbounded.** §3 establishes that bandwidth is charged on every byte in both directions at a per-host rate invisible in the hourly figure. `DATA-PROTOCOL` §3.4 puts artefacts across a network boundary on every run. A tier row of "$0.08/hr" that omits a term Mosaic is guaranteed to incur, at a rate nobody published, is a number that would mislead precisely the reader it was written for.
3. **Digest pinning is unresolved and the platform default runs against it** (§4). #55 premise 12 is a hard requirement, and vast.ai's documented default resolves the image at launch time on the machine's own terms. Even a priced vast.ai would sit behind an unresolved premise.
4. **The rule is honest about what a research document is for.** Admitting an uncitable sample into a comparison table is the mechanism by which a document comes to certify less than it advertises — the failure [#53](https://github.com/NGL321/mosaic/issues/53) hardened the checker against, in the argument layer rather than the tooling layer.

The rule is not "vast.ai is bad." It is: *a provider enters the cost tier on a citable published rate, or it does not enter.* vast.ai does not, will not, and says so itself.

---

## What this does not establish

### Sources not reached

Two, both named rather than glossed. **The authenticated console was not opened** — no account exists, none was created, and §6 obtains a sample without one, so the console read #75 contemplated was not merely skipped but rendered unnecessary; what a signed-in view would add over §6 is unknown and is probably filters rather than facts. **The runtime data source behind vast.ai/pricing's "Live GPU Prices" widget was not identified**: the page's JS chunk names no API host, `__NEXT_DATA__` is empty, and the widget's fetch was not traced. §6 reaches an equivalent endpoint by a different route, so the gap does not change any verdict, but the specific claim "the pricing page's own widget draws from endpoint X" is unproven. Beyond `guides/`, `pricing` and `host/`, roughly 500 further pages in `llms.txt` — chiefly per-endpoint API, CLI and SDK reference stubs — were not retrieved; the two most relevant to this ticket were, and the negative sweeps in §2, §4 and §5 are scoped to the 131 pages actually read.

### Open gaps

**Whether the API accepts a digest reference in `image` is empirically answerable and was not answered** (§4): the docs neither permit nor forbid it, so only a paid instance launch settles it, and that was out of scope. **Whether the unauthenticated `GET /api/v0/bundles/` is intentional or an oversight** is unknown, and it matters: if intentional, it is a durable observation channel worth building a dated-sample habit on; if an oversight, it will close. Nothing on any first-party page acknowledges it. **The Interruptible tier was not sampled** — §6's slice is on-demand `dph_total`, and #57 already flagged that a checkpointing workload might find interruptible pricing "nearly free money"; that remains uninvestigated for every provider, not just this one. **Whether any other Mosaic-relevant provider fails the Option B rule** was not tested; #57 lists Together AI as refuted on other grounds, and the rule's blast radius beyond vast.ai is unmeasured.

### Load-bearing ifs

The document's central claim survives all of its numbers being wrong, which is unusual and is the point: §1 and §2 rest on vast.ai's own published sentences ("without static price quotes," "Prices are set by the market, not by Vast"), and those would have to be *withdrawn* — not merely supplemented — for **f** to fail. The claim that would move is narrower: **if vast.ai publishes a rate card or a reference SKU table at any future date, sub-questions a, f and g all reopen at once**, and this document should be superseded rather than patched. **If the §2 sweep missed a currency amount** — it covered 131 of ~634 indexed pages — then the enumeration in §2 is incomplete, though a rate buried in an unswept API stub would still not be a published price in any useful sense. **If the recommendation's reason 1 is wrong** — that is, if #57's spend-ceiling requirement is softened or dropped — then Option B loses its strongest leg and rests on reasons 2–4, which are about honesty of comparison rather than eligibility, and a reviewer might reasonably re-weigh them. **If the §6 endpoint is closed**, Option A becomes as expensive as #75 originally assumed, which strengthens rather than weakens the recommendation.

## Verification Debt

Two items, both filed, both open — and both may be retired as moot rather than discharged, since
*Proposals* recommends ruling vast.ai ineligible for the tier outright.

- **[#117](https://github.com/NGL321/mosaic/issues/117)** — the API neither permits nor forbids a
  digest image reference. The only published format rule in the whole corpus is the template editor's
  *"must be in the format `repository/image_name:tag`"*, which excludes a digest without addressing it,
  and is attached to a different surface from the API. §4. Blocks
  [#55](https://github.com/NGL321/mosaic/issues/55) premise 12 for this provider, and is the same shape
  as [#68](https://github.com/NGL321/mosaic/issues/68) for Modal.
- **[#118](https://github.com/NGL321/mosaic/issues/118)** — the offer table answered an
  **unauthenticated** GET, contradicting vast.ai's own published requirement that all endpoints carry a
  bearer token. §6. It decides whether a durable dated-sample channel exists, which is why §6's
  response is recorded as an observation rather than cited as a price.

A third item is **not** debt. This document refutes two findings in
`docs/research/2026-07-31-gpu-tier-cost-basis.md` — its egress conclusion (§3 here) and its
"authenticated console only" claim (§6 here). Those are known defects in an unmerged draft with the
replacement text already written below, which makes them a task:
[#119](https://github.com/NGL321/mosaic/issues/119).

## Proposals

Two, both exact text. Neither was applied — `docs/research/2026-07-31-gpu-tier-cost-basis.md` is on branch `research/gpu-tier-cost` and this dispatch was scoped to one new file.

**1. An eligibility rule for the cost tier.** Proposed as a new line in #57's §6 or wherever the tier's admission criteria settle, with the badge drafted for Noah to apply:

> A provider enters the cost tier on a **citable published rate** — a page, retrievable without an account, that states what a unit of compute costs. A marketplace whose prices exist only as live offers is not underdocumented but structurally unpriceable, and is **not eligible**, regardless of what a console or an API sample shows. Samples may be recorded as dated observations; they may not occupy a row in the comparison table. ⟦T3 · #75⟧

**2. Three corrections to `docs/research/2026-07-31-gpu-tier-cost-basis.md`,** when it lands. Exact replacements:

In §7, replace — "Neither vast.ai's nor Together's pages mention egress either." — with:

> Together's page does not mention egress. **vast.ai's does, and says the opposite of free:** its billing page lists "Bandwidth costs (in \$/TB)" as a separate charge and states that "You are charged bandwidth prices for every byte sent or received to or from the instance, regardless of what state it is in," at a rate set per host and, in its own words, "not shown in your \$cost/hr or \$cost/day pricing breakdowns." A documented charge at an unpublished rate is worse than an absent line item, not better.

In §4.2, replace — "Live offers exist only in the authenticated console, which is neither a citable document nor a stable fact." — with:

> Live offers are obtainable without an account — an unauthenticated `GET https://console.vast.ai/api/v0/bundles/` returns the offer table, contradicting vast.ai's own documented requirement that "All endpoints require `Authorization: Bearer $VAST_API_KEY`." That makes a sample cheap and a citation no less impossible: the endpoint is undocumented, the response is a truncated default slice, and the result is a weather report rather than a rate.

In the §0 verdict table, replace row 11's reason — "the provider publishes no price a document can cite" — with:

> **Refuted** as a candidate — no published price *and* no provider-enforced spend ceiling, which is the constraint §8 says actually binds

## Appendix: primary sources, all retrieved 2026-08-02

Every entry was opened directly. All are first-party vast.ai properties; nothing below is a third-party summary, a search-engine snippet, or a recollection. Pages under `docs.vast.ai` were retrieved as raw Markdown by appending `.md`, which is vast.ai's own documented convention (see `llms.txt`), and are linked here at their human URLs.

**vast.ai — marketing site**
- GPU Pricing — Live Platform Rates — https://vast.ai/pricing

**docs.vast.ai — pricing and billing**
- Documentation index, 634 pages — https://docs.vast.ai/llms.txt
- Pricing overview ("without static price quotes") — https://docs.vast.ai/guides/pricing
- Billing (charge components, bandwidth per byte, negative balances, autobilling) — https://docs.vast.ai/guides/reference/billing
- Billing FAQ (bandwidth invisible in the hourly breakdown) — https://docs.vast.ai/guides/reference/faq/billing
- Serverless pricing ("at the same price as Vast.ai's non-Serverless GPU instances") — https://docs.vast.ai/guides/serverless/pricing
- Quickstart (the \$5 minimum deposit) — https://docs.vast.ai/guides/get-started/quickstart
- Reserved Instances (the \$1/hr worked example, and reserved-price preview) — https://docs.vast.ai/guides/instances/choosing/reserved-instances
- Choosing Instances Overview (the "Budget" search filter) — https://docs.vast.ai/guides/instances/choosing/overview
- Notifications (low-balance thresholds, `client:low_credit`) — https://docs.vast.ai/guides/reference/notifications
- Notification webhooks (swept for `digest`; only HMAC helpers) — https://docs.vast.ai/guides/reference/notification-webhooks

**docs.vast.ai — images, templates and API**
- Template Settings ("must be in the format `repository/image_name:tag`", the `[Automatic]` tag) — https://docs.vast.ai/guides/templates/template-settings
- Creating Templates (image examples, all tag-form) — https://docs.vast.ai/guides/templates/creating-templates
- create instance API reference (the `image` field; `price` bid bounds) — https://docs.vast.ai/api-reference/instances/create-instance
- API introduction ("All endpoints require `Authorization: Bearer $VAST_API_KEY`") — https://docs.vast.ai/api-reference/introduction
- search offers API reference (`POST /api/v0/bundles`) — https://docs.vast.ai/api-reference/search/search-offers

**docs.vast.ai — host side, for the supply-side defaults**
- `vastai list machine` (the \$0.10/GB/month storage default; undefaulted bandwidth flags) — https://docs.vast.ai/host/cli/list-machine
- Hosting overview (the \$2.00 / \$2.50 per-GPU-hour worked example) — https://docs.vast.ai/host/hosting-overview

**Observation, not a citation — recorded per §6**
- Unauthenticated offer table, HTTP 200, `Date: Sun, 02 Aug 2026 18:58:41 GMT`, 64 offers — https://console.vast.ai/api/v0/bundles/
