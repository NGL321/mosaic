# PROTOTYPE — the CI gate suite, and where a waiver may live

Ticket [#176](https://github.com/NGL321/mosaic/issues/176). Built to be thrown away, and
retained as a **primary source** for how the suite and its waiver model were decided — not
as a tool. Nothing runs it, nothing depends on it, and once `example/history.json` exists it
never touches git, GitHub, or the network.

```console
python docs/prototypes/ci-gates/prototype_tui.py
```

- `harvest.py` — run once, against the real repository. Produces `example/history.json`.
- `example/history.json` — **21 merged pull requests, 62 commits, 45 branches, 123 relative
  links, and the signature verdict GitHub actually returns for every commit.** Nothing in
  the case list is synthetic.
- `gates.py` — five gates, twenty finding codes, four candidate waiver homes.
- `prototype_tui.py` — the census plus eight cases. Case `133` is the one the suite exists
  for; the `w*` cases are the design question.

## The question

The gates are individually straightforward. #176 says so on its face, and driving it
confirms it: the suite took an afternoon and the interesting part was never the checking.
The question is **what happens when a check nobody can satisfy fires**, so that it becomes
visible rather than routed around.

Driving it moved the centre of gravity twice. The waiver answered quickly and by reuse — §11
below — and the afternoon's real work turned out to be §6a, where a gate designed to catch a
mistyped bump ended up deleting the field it was checking.

**The rulings, in one place.** §2 the type/bump gate is load-bearing and reads the **commit
stack only**; §3 custody classifies three ways and fails closed on the undecidable; §5 a
mixed-track branch is a violation and gets split; §6 a recurring finding is a protocol defect
rather than a waiver candidate; §6a **the merge commit is computed and `Bump:` is deleted**;
§7 the link gate is blocking under three scoping rules; §8 links are checked and prose paths
are not; §11 **a waiver is a `custody:deferred` issue read from a committed snapshot**; §12
custody is unwaivable, and a gate goes *required* only when the repository is green on it.

## What the prototype found

### 1. Twenty-one of twenty-one pull requests would not have merged — and the number is honest rather than rhetorical

Every pull request in this repository's history fails the suite. But the failures are not
evenly distributed, and the shape is the finding:

| | Code | n | |
|---|---|---|---|
| **custody** | C1 / C2 | 79 | every commit, blocked on [#175](https://github.com/NGL321/mosaic/issues/175) |
| **protocol defect** | T7 | 17 | §6's own wording is wrong — §6 below |
| **grammar that never existed** | T4 | 6 | `Bump:` has no defined form |
| **real, substantive** | T2 / T5 / T6 / T1 | 9 | mistyped bumps and cross-track branches |
| **the doc backlog** | D:* | 22 | three pre-contract documents, already [#50](https://github.com/NGL321/mosaic/issues/50) |
| **branch class** | B1 | 3 | `record/`, a class §4 never declared |
| **links** | L1 | **0** | in owned content; L2's single hit is deliberate |

Two thirds of that column is one unbuilt mechanism and one wrongly-worded sentence. The
substantive defect count across a year of work is **nine**, and one of them is serious
enough to be the headline.

### 2. The headline: a Hard Core revision landed as a PATCH, and the contradiction was written out twice in the same commit message

[`b2b3b2c`](https://github.com/NGL321/mosaic/commit/b2b3b2c) — pull request #133, branch
`task/context-md-proposals`. Two `core:` commits on the branch, `e89bbe4` *"land the Hard
Core's term-level changes"* and `fe88801` *"restate the two assertions #9 found
undefended"*. §3 maps `core:` to **MAJOR**. The merge commit's subject is `record:` and its
body says:

```text
Resolve #89 (core)
Resolve #91 (core)

Bump: research PATCH
```

The merge commit **names the two `core:` tickets four lines above stating `research
PATCH`**. §6 justifies the `Bump:` field on exactly this ground — *"a mistyped commit shows
up as a visible contradiction between the merge commit and the branch it landed, instead of
being silently miscounted at release time."* The mechanism worked perfectly. The
contradiction was visible, in one screen, and nothing read it, because reading it was a
human's job and nobody had been given it.

This is the single strongest argument in the record for mechanising §3 — and it is an
argument the record made against itself, in writing, without noticing.

**Ruled on #176: the type/bump gate is the suite's load-bearing member**, ahead of custody
in value if not in principle, because it is the only one with a demonstrated live failure
that changed what the version history claims.

**And driving that finding is what dissolved half the gate.** The failure was possible only
because the merge subject's type *and* its `Bump:` line were both written by hand, so both
could be wrong together — and they were, consistently, which is exactly why nothing caught
it. See *The merge commit is computed* below, which is the largest ruling this ticket makes
and was not in its brief.

### 3. The custody gate cannot be built the way #24 ruled it, because GitHub's signature attests the API call and never the hand

#24 ruled the boundary is *a signature, not a name*: agents commit as a GitHub App through
the API and are signed by GitHub; Noah signs his own commits; the check verifies signature
and signer. Harvesting the real verdicts turns that into three facts:

- **22 of 22 merge commits are `verified: true`.** Every one is signed by GitHub's own
  `web-flow` key, with `login: NGL321`.
- **0 of 57 branch commits carry any signature at all.**
- `git log %G?` returns `N` for all of them locally, because it shells out to gpg and gpg
  is not configured. **A gate built on `%G?` would fail the entire repository on any runner
  without a gpg keyring** — which is the default runner.

The consequence is the hole: `verified: true` under a human login means *GitHub performed
this write for a party holding that account's credentials*. Every local agent session in
this repository holds exactly those credentials — `gh` authenticates as `NGL321`
([#161](https://github.com/NGL321/mosaic/issues/161)). An agent creating a commit through
the contents API today produces a commit indistinguishable, by signature, from Noah pressing
the merge button.

**Ruled on #176: three classifications, not two, and the third fails closed.** An App login
signed by GitHub is an **agent**; a commit signed by a key registered to Noah is a **human**;
a GitHub-signed commit under a human login is **undecidable** — reported as such and never
counted as a pass. `custody_check.py` already takes this posture (*a green run must mean
something*), and this extends it to the case that will actually occur.

**Two consequences hand back to [#175](https://github.com/NGL321/mosaic/issues/175).** Noah's
own signing key must be registered before the gate can distinguish anything, and the
web-merge button stops being an act of authorship the gate can read — either merges are
exempted on the ground that merging is not authoring, or merges move to a signed path too.
**Open, and it is Noah's to decide** — see *Open, and handed on*.

### 4. The `Bump:` field has never had a grammar, and six of twenty-one are outside every candidate one

Five distinct spellings in twenty-one merges: `research PATCH`, `tooling MINOR`, `tooling
FEAT`, `tooling FIX`, `tooling minor`, and bare `tooling`. `FEAT` and `FIX` are *commit
types* in a field that wants a *bump level*; §3's tooling table maps them to `minor` and
`patch`, so the field is repeating the type rather than stating the level it computes to.
One merge has no `Bump:` line at all.

Nothing in the record defines this field's form. §6 shows one example and stops. That is not
a compliance failure; it is a specification gap that has been filled six different ways by
the same person because there was nothing to be consistent with.

The prototype's first ruling here was to pin a grammar in §6, the way §5 pins the `Session:`
trailer's spelling. **Driving it with Noah overturned that.** The field should not have a
grammar because it should not exist — see the next section.

### 5. One branch, two tracks: three merges leave a bump with nowhere to go

`6ebd321` carries `fix:` and `record:`; `343e2d3` and `70a10f5` do the same. §1 says the
track is decided **when the branch is created**, one test, one answer. So a branch carrying
both is either a violation of §1 or evidence that §1's premise does not survive contact with
work — and the visible cost is arithmetic: `6ebd321` states `research PATCH`, and the
tooling-track `fix:` it also landed advances nothing, ever.

This is not a nuisance finding. §3's whole claim is that *the release bump is computed
rather than judged*, and a computation that silently drops one of its inputs is not a
computation.

**Ruled on #176: split the branch — §1 stands.** A mixed branch is a violation, the gate
blocks it, and the fix is two branches and two pull requests. The two alternatives were
*state two bumps* and *§1 is wrong, a branch has a primary track*; both keep §1's one-test
-one-answer premise only by weakening it, and neither pays for the ceremony it saves. The
cost is real and accepted: three of this repository's twenty-one pull requests would have
been six.

### 6. §6's `(#PR)` is wrong, and the check found the protocol rather than the history

§6's merge subject form is `<type>: <what landed> (#PR)`. Seventeen of twenty-one merges do
not follow it. Reading what they *do*:

- **Twelve name the ticket**, not the pull request — `(#76)`, `(#5)`, `(#26)`.
- **Five name nothing.**
- **Four "match"**, and all four are pull requests 19–25, where the pull request number and
  the ticket number happened to coincide. Not one modern merge follows the rule.

The ticket is the better reference and everyone chose it: a pull request is the mechanism, a
ticket is the decision, and §6's own next bullet already tells the author to put *"the
tickets closed"* in the body. The rule and the practice disagree, and the practice is right.

**This is the first real instance of #176's own worry, and it resolves the opposite way from
how the ticket frames it.** A check firing on seventeen correct commits is not a check that
needs a waiver; it is **a defect report against the protocol**. If the waiver model can
absorb this, the waiver model is the mechanism by which a wrong rule survives.

**Ruled on #176: a finding that recurs is a protocol defect, not a waiver candidate** — the
same move §5 already makes for the defence override (*"a recurring override is evidence the
table above is wrong"*). Mechanised the cheapest possible way: the waiver ledger is
countable, so **the same code waived N times is a visible number**, and the number is the
signal. Nothing needs to enforce it beyond making it impossible not to see.

This particular finding then stops existing at all: under the next section the merge
subject is emitted rather than typed, so whatever it names, it names by construction.

### 6a. The merge commit is computed, and `Bump:` is deleted

The largest ruling of the ticket, and it was not in its brief. It came out of Noah's reading
of §2 above: *version bumping should not belong to those merge commits but rather the commit
stacks that are being merged.*

**Merge commits survive, and that is a derivation rather than a taste.** Fast-forward-only
needs a linear history, and §7 forbids rebasing a pushed branch. The only route to linearity
without rebase is to merge `main` *into* the branch and then fast-forward — which puts every
branch commit and every sync merge onto the trunk, and `git log --first-parent main` stops
being a changelog of units of work. `--no-ff` is not defended by preference; it is what is
left once §7 binds.

**`Bump:` restates the subject's own type prefix.** §3's two tables partition the type set by
track and map each type 1:1 onto a level, so `record:` *is* research PATCH and `feat:` *is*
tooling MINOR. The line tells a reader nothing the first word of the subject does not, and it
is a second **hand-written** statement of a fact §3 says is **computed**. That is
[#90](https://github.com/NGL321/mosaic/issues/90)'s stored copy that can disagree with the
recomputation with no tiebreaker, and [#63](https://github.com/NGL321/mosaic/issues/63)'s
*computed always, rendered only where it is read*, arriving for the third time in the same
programme.

**Ruled on #176:**

1. **The merge commit's mechanical content is generated, never authored** — the subject's
   type from the highest type on the stack, the body's ticket list from the branch's
   `Resolve #N` lines. Its **prose** stays authored: the *what landed* clause and the
   one-line gist §6 already has written once and used three times are the parts no function
   can produce. This is §5's own pull-quote in a new dialect — *custody is over the decision,
   not the keystrokes* — with the tool wording a decision Noah made.
2. **`Bump:` is deleted from §6.**
3. **The tie is broken by §3's table order** — `core > belt > evidence > record`,
   `feat > fix > chore`. §6 says the merge takes *the highest* type, and `evidence:` against
   `record:` is a tie on level; a generator cannot be ambiguous, so the order is pinned.
4. **CI offers, Noah pastes, `main` verifies.** A pre-merge check computes the exact message
   and posts it; Noah pastes it into the merge button; a post-merge check on `main`
   recomputes and verifies. The obvious alternative — an Action performing the merge through
   the API so the text cannot be edited at all — is **refused because it reverses a #24
   ruling**: the App needs no write access to `main`, and buying message integrity with trunk
   write access is a bad trade for a message the human is pasting anyway. Running the
   function twice costs nothing, because it is a function.

**What this dissolves.** §4's missing grammar (nothing is typed, so nothing can be
misspelt), §6's `(#PR)`-versus-`(#ticket)` disagreement (whatever the generator emits is the
form), and `b2b3b2c` itself — with the subject type computed it would have read `core:`, and
the MAJOR would have been sitting at trunk level in the changelog where §6 wanted it.

**And it settles the custody gate's scope by consequence rather than by decision.** A merge
commit under this rule carries no authored content and introduces no tree its parents did not
already carry, both of which the branch commits were checked on. **Custody has nothing to
adjudicate there**, so the custody gate reads the commits a pull request adds and not the
merge — which is exactly where `custody_check.py` already looks. The GitHub-signed-under-a-
human-login case in §3 above therefore stops being the common case and becomes what it should
be: a finding about commits, where an agent could actually forge one.

### 7. Link integrity is clean, and the nuisance the ticket predicted is entirely a scoping failure

Unscoped, the link check produces **24 dangling links and zero of them are ours** — every
one lives in the vendored `.agents/skills/` and `.claude/skills/` trees, whose own
cross-references point at files those upstream packages ship and this repository does not.
Scoped to owned content, the count is:

- **0 dangling links** across `README.md`, `PROTOCOL.md`, `CONTEXT.md`, `docs/`, `notebook/`,
  `curriculum/`, `inquiries/`, `conjectures/`.
- **1 advisory**: `CONTEXT.md` → `CHARTER.md`, which §5 declares in advance *on purpose*, so
  that the custody check keys on the path before the file exists.

**The scope is not a new list.** `README.md`'s licence path table already excludes the
vendored trees as third-party — [#22](https://github.com/NGL321/mosaic/issues/22) settled
that — so the gate reads a boundary the repository has already drawn, exactly as
`contribution.yml` reuses `custody_check.py`'s `AUTHORED` rather than declaring a second
copy.

**Ruled on #176: three scoping rules, and with them the link gate is blocking rather than
advisory.**

1. **Owned content only** — the licence path table's boundary, second consumer.
2. **Files the pull request touched only** — a repository-wide check convicts a branch of a
   link somebody else wrote, which is the fastest way to teach everyone that red means
   nothing.
3. **Declared-future paths are advisory, not failures** — a small list, and `CHARTER.md` is
   on it because §5 put it there.

### 8. The check review actually asked for — "does this path exist" over prose — is a false-positive machine and is refused

Review caught a dangling `docs/research/` path and a reference to a deleted file, and #176
inherits both as *"machine-detectable"*. They are — as **markdown links**. As backticked
paths in prose, the same check over the current tree returns: `mattpocock/skills` (a GitHub
repository), `Desk/mosaic/` (a Google Drive path), `tooling/custody-and-charter-gate` (a
branch name), `ai.google.dev/gemini-api/docs/pricing` (a third-party URL). Every hit a false
positive; nothing else in the tree.

**Ruled on #176: the gate checks markdown links and never prose paths.** A checker whose
population is entirely false positives does not have a tuning problem; it has the wrong
subject. The two real defects review caught were both links, and links are checkable.

### 9. The waiver already exists, it works, and it is a sentence in a README

The strongest case for the whole waiver question was in the repository before the ticket was
written. `docs/research/README.md`:

> The checker is deliberately **not** wired into CI until that sweep lands; wiring it now
> would put the repository in permanent red, which teaches everyone to ignore it.

Three of three research documents fail #26's contract (22 findings). The gate exists, it is
correct, and it is switched off — with the reason stated, the blocking ticket named
([#50](https://github.com/NGL321/mosaic/issues/50)), and an expiry implied. That is a
**complete waiver**. It is also invisible to CI, uncountable, and enforced by Noah
remembering.

So the design question is narrower than #176 poses it. The repository does not need a waiver
*concept*; it has one and it is sound. It needs the same act to be **countable and to come
due** without depending on someone's memory.

### 10. Four homes, five properties, and nothing scores five

| model | attributable | durable | countable | expires | offline |
|---|---|---|---|---|---|
| commit trailer | ✓ | ✓ | ✗ | ✗ | ✓ |
| pull request body | ✗ | ✗ | ✗ | ✗ | ✓ |
| `.github/waivers.toml` | ✓ | ✓ | ✓ | ✗ | ✓ |
| a `custody:deferred`-shaped issue | ✓ | ✗ | ✓ | **✓** | ✗ |

The properties are not invented; each is somewhere the record has already been bitten.
*Attributable* is newly answerable at all — #24's ruling is what makes "who granted this"
a fact rather than a claim. *Durable* is [#63](https://github.com/NGL321/mosaic/issues/63)'s
rule for the register attestation: evidence that expires with a retention window is not
evidence. *Countable* is #24's own requirement handed to this ticket. *Expiring* is §2's
grace, bounded three ways because *a grace whose expiry its beneficiary controls is a rule
that was never written*.

**The pull request body loses outright** and is worth stating because it is the obvious
first idea: it is editable after the fact by anyone with a write bit, carries no signature,
and leaves no git object. It is the one model where CI cannot say who granted the waiver,
which under #24's ruling is the one thing that has just become knowable.

**`file` and `issue` differ on exactly one axis each, and it is the axis the other one
needs.** A committed file never comes due. An issue is not readable by the gating run.

### 11. Ruled: the waiver *is* `custody:deferred`, plus the snapshot mechanism #5 already built

#176 asks whether these gates *"reuse it rather than invent a second one."* They do, and the
one objection — that the tracker is not offline-readable at gate time — was answered eight
months of tickets ago by a decision made for the identical reason.

[#5](https://github.com/NGL321/mosaic/issues/5) ruled **the ledger is the issue tracker**,
refused a parallel Markdown system on the grounds that it is one more thing to keep in sync,
and then paid the one real cost with `curriculum/open.md`: a **generated, committed
snapshot**, so a clone stays self-contained and `git log` can say what the programme owed in
March. `tools/snapshot_debt.py` already exists, already has a staleness exit-code contract
(`1` stale, `2` tool broken, `3` tracker data malformed), and that contract is already on
[#66](https://github.com/NGL321/mosaic/issues/66)'s list to wire.

So a waiver is:

- **an open issue labelled `custody:deferred`**, filed the way §2 already requires, blocking
  `1.0.0` like every other one — which is the expiry, and it is not one the beneficiary
  controls;
- **cited from the branch** as `Waive: <code> #<issue>`, so the gating run knows which
  finding is answered and by what;
- **read by CI from the committed snapshot**, not from the API, so the gate is a function of
  committed text — [#63](https://github.com/NGL321/mosaic/issues/63)'s standing requirement
  in its local dialect;
- **granted by Noah and by nobody else** — enforceable for the first time, because §3 above
  makes the granting act's identity a fact. An agent may *report* that a gate is
  unsatisfiable and may *draft* the issue; filing the label is Noah's, the same shape as §5's
  defence override, which *"an agent may not invoke and may not propose."*

No new mechanism, no second ledger, no second expiry, and the census that §2 already runs
before ratification (`gh issue list --label custody:deferred --state open` → empty) becomes
the census of open waivers too.

### 12. Which gates may be waived — and the gate that is unwaivable *and* unsatisfiable

**Custody is not waivable.** C1, C2 and C3 refuse a waiver however it is granted (case `x`).
The rest are waivable. This is #176's own instinct — *a link check is a nuisance when it
fires wrongly; a custody check is the programme's central claim* — and §5's argument carries
it: a custody rule with a single exception *"makes the check stop being an answer to
anything."*

Which produces the problem the prototype most wants to hand back. **C1 is unwaivable and
unsatisfiable at the same time.** No commit in this repository can be signed by an identity
the check would accept, because [#175](https://github.com/NGL321/mosaic/issues/175) has not
run. A gate that is mandatory and impossible is not a gate; it is a red mark everyone learns
to click past — the precise failure `docs/research/README.md` avoided by hand.

**Ruled on #176: a gate becomes *required* only when the repository is green on it, and
until then it runs advisory with its blocking ticket named on its own output.** The suite
lands in three waves, and the waves are already filed:

| Gate | Required when | Blocked on |
|---|---|---|
| type / bump, branch, link | immediately — one branch of fixes clears them | §6a's amendment |
| research front matter | the retrofit lands | [#50](https://github.com/NGL321/mosaic/issues/50) |
| custody | the App exists and Noah's key is registered | [#175](https://github.com/NGL321/mosaic/issues/175), [#161](https://github.com/NGL321/mosaic/issues/161) |

This is not a waiver — nothing is being excused. It is the ordering that already governs
`docs/research/README.md`, stated once for the suite instead of rediscovered per gate.

## Open, and handed on

- **`record/` is a real branch class and §4 does not have it.** Five branches, all landing a
  record change that answers no wayfinder ticket type. §4 says prefixes *are* wayfinder's
  ticket types; practice invented a sixth. Either §4 gains the class or the branches were
  misnamed — a one-line protocol question, not worth a ticket of its own until someone
  amends §4. Left in the map's fog.
- **Nothing counts how often a code is waived.** §6 above rules that a recurring waiver is a
  protocol defect and leans on the count being visible. The snapshot makes it countable; what
  reads it, and at what threshold anyone is told, is [#88](https://github.com/NGL321/mosaic/issues/88)'s
  shape rather than this ticket's. Left in fog.
