# Data protocol

Where Mosaic's bytes live, which of them are stored at all, and what has to be true before a
result counts as saved. `PROTOCOL.md` governs how work enters the repository; this document
governs everything the repository deliberately does **not** hold.

**Provenance.** Mosaic does not own this discipline. It is a programme-scoped derivation of
Noah's **System Brief** — a personal document governing his whole file estate, which stays
outside this repository because most of it concerns personal data Mosaic has no business
restating. Reproduced here is the part the record actually depends on, in Mosaic's terms,
plus the research-specific rules the brief does not carry (§8). Adopted in
[#3](https://github.com/NGL321/mosaic/issues/3); recovered and rewritten as this file in
[#35](https://github.com/NGL321/mosaic/issues/35), which found the discipline had been
enforced in prose and cited by section number since, with no artifact anyone could open.

**The section numbers are inherited, not chosen.** Tickets and files already in the record
cite `§3.4` and `§5` of "the storage protocol". Renumbering would silently redirect
citations that a reader will follow, so this document keeps the source brief's skeleton even
where a fresh document would order it differently. New material goes in §8, where it cannot
collide with an existing citation.

This is a **record** file under [`PROTOCOL.md` §5](../PROTOCOL.md) — agent-writable. What it
records was decided by Noah.

---

## 1. The five laws

1. **No tool owns data.** Nothing built here may be the sole holder of anything valuable. If
   a tool is the only place a fact exists, that is a liability, not a feature.
2. **Cache is never origin.** Scratch space may vanish at any moment. Before anything counts
   as saved, it must already have a canonical home.
3. **Don't store what you can regenerate.** Deterministic outputs are configs, not data.
   Store the config and the seed; regenerate on demand. This is the law with the most
   teeth for Mosaic — see §3.3.
4. **Reversible vs irreversible.** Reversible operations on Noah's data may be performed
   with a stated plan. Irreversible ones — deletion, overwriting originals, force-pushing,
   mass renames without a record — require his explicit go-ahead. When unsure which one is
   in progress, it is irreversible.
5. **Comprehension ceiling.** Anything load-bearing must be re-explainable by Noah after six
   months away. Prefer few, standard, boring components. Clever is a liability. A solution
   that needs a diagram to justify itself gets proposed, not built.

**Load-bearing vs disposable sets rigor** — not the language, not where the source lives.
Research or analysis code whose output someone will rely on is load-bearing: pinned
dependencies, deterministic seeds, tests at the seams, reproducible from a clean checkout.
Viewers, dashboards, one-off scripts and glue are disposable: build fast, delete freely, no
ceremony. In Mosaic this distinction is not a second taxonomy — it is
[`PROTOCOL.md` §1](../PROTOCOL.md)'s two-track test wearing different clothes, and §8.3
states why the two must be kept aligned.

---

## 2. Where things live

Noah's Drive root is an office, and the metaphor is load-bearing for navigation.

| Root | Role | Holds | Mosaic's use |
|---|---|---|---|
| `_inbox` | the desktop surface | new unsorted arrivals; triaged toward empty | none |
| `Desk` | desk drawers | active work, one folder per project | `Desk/mosaic/` — run outputs (§3.4) |
| `Shelf` | open shelves, for guests | anything shareable **read-only**. The discriminator is *permission*, not file type | papers cited by the record |
| `Archive` | locked filing cabinet | done or historical, structure preserved as found | retired runs, once retention exists |
| `Index` | the ledger | manifests, reading lists, catalogs, as Drive-native Sheets | the hash → path manifest (§8.2) |
| `Utility` | the workshop | agent context, built tools, scratch | none yet |
| `Notes` | loose reference | Noah's private reference material: anything in text or markdown he wants to find later | Weekly Reflections |

`Notes` is not in the source brief. It was omitted there because it is the least developed
part of the framework — a loose Zettelkasten without Zettelkasten's strictness, deliberately
protocol-agnostic — and named explicitly in [#3](https://github.com/NGL321/mosaic/issues/3)'s
second resolution when the omission surfaced. It is recorded here so the next reader does
not re-discover the gap and invent a root to fill it.

**Identity rule: files are identified by content hash (sha256), not by path.** Renaming and
reorganising are therefore safe *if recorded* — the manifest is append-only, while names and
paths are mutable attributes. **Never remove a row from a manifest.** §8.2 is what this rule
buys the programme.

**Never invent a new top-level scheme.** Something that does not seem to fit is a question,
not a licence. An eighth root, or a parallel folder taxonomy, is the failure mode this
system exists to prevent.

---

## 3. Storage decision tree

Walk in order; stop at the first match.

**3.1 — Is it code?** → git. Never loose in Drive. This repository is canonical for Mosaic's
code, including research-track code that reads as tooling.

**3.2 — Is it a secret** (key, token, password, credential)? → Noah's password manager.
Never in the repo, never in Drive in plaintext, never in a log **or a notebook output**.
Read from an environment variable or a git-ignored local file. The last clause binds the Lab
Notebook generator directly: its output is public by construction, so a secret reaching a
generated entry is published the moment it is written.

**3.3 — Can it be regenerated from a config, seed, or deterministic function?** → **do not
store it.** Store the generator config in the repo. Regenerable bytes in canonical storage
are pure cost: they ride the nightly mirror and the backup forever.

For Mosaic this covers activation tensors, distance matrices, derived features, intermediate
representations and re-renderable figures — which is to say most of what a Run
produces by volume. **This is a design constraint on every Experiment**, not a cleanup
policy: a config that cannot regenerate its intermediates from a seed has failed §3.3 at
design time, and is also failing the load-bearing standard in §1.

**3.4 — Is it a durable artifact someone will rely on later** (model checkpoints, run
metrics, analysis outputs, final figures)? → Drive, under the project's `Desk` folder, at a
**deterministic path**: `Desk/mosaic/runs/<run-id>/`.

> **A retention policy is proposed before the first large sweep**, not after: runs ×
> checkpoints × size, arithmetic checked with Noah.

This is the clause the map's *Not yet specified* cites as a precondition on the first sweep.
It is not yet dischargeable — the arithmetic needs a first rung's experimental design, which
[#7](https://github.com/NGL321/mosaic/issues/7) has not produced. The *mechanism* around it
is settled and lives in [`inquiries/README.md`](../inquiries/README.md): the repository
keeps one manifest per run and never the bytes.

**3.5 — Is it scratch for a running process?** → local temp or the scratch area. Never the
origin of anything (law 2).

**3.6 — Is it a list or table queried or browsed across projects** (manifests, reading
lists, catalogs)? → `Index`, as a Drive-native Sheet so version history works. **Do not
hand-edit; append through a tool.** Rows are never removed (§2).

**3.7 — Is it a note or document?** → `Notes`, as markdown, with a **globally unique
filename** — prefixed by project or date (`eca-grok-methods.md`, `2026-07-24-standup.md`).
Folders are sync and sharing boundaries; filenames are identity.

The Lab Notebook is **not** a note and does not route here; see §8.1.

---

## 4. Compute placement

| Need | Where | Notes |
|---|---|---|
| Glue over Google services, light UI, small automations | Apps Script / browser | Hard execution limits — minutes, not hours. No filesystem, no long jobs. |
| Always-on light services: sync, backup, git host, schedulers, small web apps | Raspberry Pi 5 | ARM, modest RAM. Not for training or transcoding. Candidate host for notebook-generation triggers. |
| GPU work, heavy training | local PC | Reached over Tailscale. Mosaic's default for training. |
| **Anything Secure Research** | local PC only | Does not leave the local network. |
| Large jobs | cloud / institutional compute | **Permitted for Mosaic** — see below. |

**Mosaic is not Secure Research, so §4's sensitive-work restriction does not bind it.** The
discriminator is *intent*, not publication status: Secure Research is work Noah does not
intend to keep public from the outset, and Mosaic is public-by-design from day one. Its loss
or theft would cost nothing, because being seen is the whole point. Institutional and cloud
compute are therefore available, which means Runs need not be sized to one desktop.

This corrects a first reading that took "unpublished" to mean "sensitive" and excluded cloud
compute; the correction is [#3](https://github.com/NGL321/mosaic/issues/3)'s second
resolution and the definition lives in `CONTEXT.md` under **Secure Research**, flagged there
as provisional. A later programme phase — testing high-capacity cognitive systems — may well
be Secure Research, at which point this is re-decided rather than inherited.

**No externally hosted database** for state that could live in Drive, a Sheet, or a file. If
one is genuinely required, say why and propose SQLite on a known host first.

---

## 5. Getting artifacts into Drive — the footgun

The local mirror of Drive is **pull-only**: Drive → local, one direction, on a schedule.
Read-only by convention.

> **Writing into the mirror is not publishing.**

A file written there does not exist upstream, so the next sync treats it as deleted-from-
source and moves it into a dated safety-net folder. It is not destroyed, and it is not
published either, and it will confuse everyone who looks. **Do not write to the mirror.**

To publish, do it explicitly: an `rclone copy` from a local output directory up to the
project's Drive path, as a deliberate step at the end of a run. Explicit publish beats
ambient two-way sync — it is auditable, scriptable, and has no conflict semantics to reason
about. Use the Drive API directly only where an application needs live read/write rather
than batch publish.

**Mosaic has no `publish.sh` yet.** Until it does, no run has a mechanised path to §3.4's
deterministic location, and the first experiment will need one before its outputs can be
cited.

---

## 6. Contract for anything built

Every tool declares four things plus one, in a `README.md` in its own folder:

- **reads** — which paths, indices, or services
- **writes** — which paths, and whether they are canonical or scratch
- **auth** — none / Drive OAuth / local only
- **surface** — CLI / HTML page / library / scheduled job
- **safe to regenerate from scratch?** — yes/no

Five lines. This is what keeps a collection of small tools from becoming a junk drawer, and
it is how Noah knows six months later what is safe to delete. It binds everything Mosaic
builds: the notebook generator, the debt snapshot tool, `publish.sh`.

---

## 7. Anti-patterns

Each has already cost Noah a rebuild.

- Inventing a new folder taxonomy instead of using the office roots.
- Storing regenerable data in canonical storage.
- Making a tool the sole home of its data.
- Treating load-bearing research code as disposable.
- Building something clever that cannot be re-explained later.
- Hand-editing an index instead of appending through a tool.
- Ambient two-way sync where an explicit publish step would do.
- **Gradual migrations.** Consolidation happens once, mechanically; interpretation is
  deferred and optional. Do not start a half-migration. This bears directly on how Noah's
  prior work on the programme gets folded in.

---

## 8. Where this protocol meets the record

The four clauses below are Mosaic's, not the source brief's. The brief governs a personal
file estate; a research programme needs its storage discipline to reach the *record*, and
these are the places it does.

### 8.1 The Lab Notebook is not a note

§3.7 routes notes and documents to `Notes`, in Drive, privately. The Lab Notebook is public
and lives in this repository. That is not an exception to §3.7 but a case §3.7 does not
cover: a note is private reference material Noah keeps to think with, and the notebook is an
**audit trail** — in effect a rich commit history, carrying mistakes and abandoned
directions deliberately, for an outside reader. Different artifacts, different purposes,
different homes.

The Weekly Reflection *is* a note by this test, and lands in `Notes` per §3.7.

### 8.2 A public citation of a private archive

§2's identity rule solves a problem the record had independently: how a public notebook
entry cites a session in a private Transcript Archive without either publishing the archive
or making the citation unverifiable.

**The entry cites a content hash; a manifest Sheet in `Index` maps hash → Drive path.** The
citation is stable and checkable by anyone Noah grants access to, the archive stays closed,
and reorganising the archive never breaks a citation already in the record — which is
exactly the property §2 promises and the reason its append-only rule has no exceptions.

The same construction is what lets `inquiries/*/runs/` hold manifests rather than bytes: a
manifest records the run id, the config SHA it was produced from, the seed it drew, the
sha256 of the output, and the Drive path. The hash is the claim; the path is a convenience
that may change.

### 8.3 Load-bearing maps onto the two tracks, and must keep mapping

§1's load-bearing/disposable split and [`PROTOCOL.md` §1](../PROTOCOL.md)'s research/tooling
split ask nearly the same question and must not be allowed to drift apart. Research track is
"could a silent change falsify a result already in the record"; load-bearing is "will
someone rely on this output". Anything on the research track is load-bearing by
construction, and the repository structure is required to make that boundary visible rather
than implicit.

Where they can differ: a tooling-track artifact may still be load-bearing — a restore path,
or `publish.sh`, breaks nothing in the record when it changes but everything in practice
when it fails. **Tooling track is not a licence to be disposable.** The reverse never holds:
nothing on the research track is disposable.

### 8.4 Publication-time release is not a §3.3 violation — but the rule is not written

§3.3 forbids storing regenerable bytes. [#4](https://github.com/NGL321/mosaic/issues/4)'s
survey recommends releasing seeds, checkpoints, distance matrices and barcodes *as a
condition of credibility*, given the field's reproducibility record. The two collide only if
"store" is read as one thing.

The reconciliation available is to distinguish **canonical storage during work** — store the
seed, regenerate the artifact, per §3.3 — from **publication-time release**, where derived
artifacts are frozen once, at the paper, as a deliberate deliverable with its own retention.
That is a Positive Heuristic question about what Mosaic owes a reader, so it is
[#9](https://github.com/NGL321/mosaic/issues/9)'s to settle and **is recorded here as open**,
not as decided. Until it closes, a release freeze is proposed to Noah rather than performed.

---

## Open against this protocol

| | What is missing | Where it is tracked |
|---|---|---|
| §3.4 | The retention arithmetic — runs × checkpoints × size — before the first large sweep | map [#1](https://github.com/NGL321/mosaic/issues/1), *Not yet specified*; needs [#7](https://github.com/NGL321/mosaic/issues/7)'s first rung |
| §5 | `publish.sh` — no mechanised path from a run's output to `Desk/mosaic/runs/<run-id>/` | unfiled; blocks the first experiment's outputs being citable |
| §8.4 | Whether publication-time artifact release is exempt from §3.3, and under what retention | [#9](https://github.com/NGL321/mosaic/issues/9) |
