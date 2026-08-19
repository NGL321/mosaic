# 0001 — A private Transcript Archive inside a transparent programme

**Status:** Accepted, 2026-08-02. Recorded in
[#10](https://github.com/NGL321/mosaic/issues/10); the concrete facts it depends on were
settled in [#3](https://github.com/NGL321/mosaic/issues/3) and live in
[`docs/DATA-PROTOCOL.md`](../DATA-PROTOCOL.md).

---

## Context

Mosaic is machine-accelerated and says so, which buys it a standing objection:
*these are the model's ideas.* [`PROTOCOL.md` §5](../../PROTOCOL.md) names the form it
actually takes — *"the vocabulary was written by the model"* — and commits the programme to
answering it structurally rather than by assertion. Custody's third obligation is the
instrument: an agent co-author on an authored file carries a `Session:` trailer **resolving in
the Transcript Archive**. The research document contract carries the same obligation in front
matter ([`docs/research/README.md` §1](../research/README.md)), and so does every Lab Notebook
entry ([`notebook/README.md`](../../notebook/README.md)).

All three presuppose a store that already exists. A session that was not captured cannot be
captured afterwards, and a citation that resolves to nothing is a citation in appearance only —
the same failure the record already names for a truncated digest. So the question is not
whether to keep transcripts. It is whether keeping them means **publishing** them.

Transcripts are also the rawest material the programme produces: unperformed, unredacted,
carrying half-formed positions, third-party content, personal matter, and — the case
[`DATA-PROTOCOL.md` §3.2](../DATA-PROTOCOL.md) prohibits outright — secrets.

## Decision

**Raw working-session transcripts are archived, not published.** The Transcript Archive is
private, append-only, and held outside this repository. The public record cites it; the public
record does not contain it.

Grounded in what #3 settled:

- **A session is identified by content hash, never by path.** [`§2`](../DATA-PROTOCOL.md)'s
  identity rule governs: `sha256` is the claim, the Drive path is a mutable attribute. A
  manifest Sheet in `Index` resolves hash → path ([`§8.2`](../DATA-PROTOCOL.md)), appended
  through a tool, with rows never removed.
- **A session is a segment of a transcript file, not the file.** It ends after an hour without
  work and belongs to the local day it ended on, so a notebook citation is the transcript's
  `sha256` **plus the window** — the hash alone would cite material the entry does not cover
  ([`notebook/README.md`](../../notebook/README.md)).
- **The digest is never truncated.** `session:` is `sha256:` and a whole 64-character digest,
  or the literal `unrecorded` ([`docs/research/README.md` §1](../research/README.md)).
- **The commit trailer key is `Session:`, or any `<Tool>-Session:`, and nothing else**
  ([`PROTOCOL.md` §5](../../PROTOCOL.md)). Claude Code emits `Claude-Session:`, which is what
  agent-co-authored commits here actually carry.

This construction is why the archive can stay closed without the citation becoming worthless:
the citation is stable and checkable by anyone Noah grants access to, and reorganising the
archive never breaks one already in the record.

## The rejected alternative: publish raw transcripts as primary artifacts

The maximal reading of an open programme is that the transcripts go up with everything else.
It lost on five counts.

1. **It answers the charge in the wrong direction.** Publication *pre-loads the evidence for
   the prosecution*: a searchable corpus of a model proposing things, handed to a reader
   already disposed to conclude the model did the work, stripped of the defence artifact that
   accompanies each claim in the record. Archiving answers the same charge **on demand and
   with receipts** — the challenger names a claim, the record names the session, and the
   defence Noah wrote is attached to it. Volume is not disclosure. A dump nobody audits is
   transparency in appearance only.
2. **It is irreversible in the direction that matters.** Under [law 4](../DATA-PROTOCOL.md), a
   publication cannot be unpublished, so every redaction failure is permanent, and §3.2's
   prohibition on secrets in public output has no recovery path. The archive keeps that blast
   radius inside a private store, and gives the notebook generator a single boundary to scan
   at — which is exactly where its scrub already fails closed.
3. **It would change the transcripts.** A transcript written to be read is a performance, and
   the archive's whole evidentiary value is that it is not one. Publishing raw material is
   self-defeating the moment the author knows it is raw material being published.
4. **It would drown the artifact that is meant to be read.** The Lab Notebook already carries
   the mistakes and abandoned directions deliberately, curated and annotated. Transparency is
   discharged by the notebook, not by the volume of bytes behind it.
5. **It buys nothing the citation does not already buy.** Anything a reader could establish
   from the published corpus, they can establish from a resolved citation plus a grant — with
   the scope of the question, and the burden of asking it, both stated.

## The memetic premise

Influence is unavoidable. Working with models at this volume produces model-shaped ideas: some
Noah's construction, some the model's, most jointly held and not cleanly separable at the
moment they form. A programme that set out to manage *influence* would have to stop working
the way it works, and would be lying about the result.

**The risk being managed is therefore untraceable influence, not influence.** An idea in the
record with no route back to the moment it entered is the failure. The archive does not reduce
influence by one line; it makes influence *traceable*, converting an unanswerable insinuation
into a question with a lookup. §5 already states the honest answer in full: not that no model
touched the work — one did — but that every place one did is recorded, traceable to a session,
and accompanied by a defence Noah wrote. That answer is stronger than a denial, and unlike a
denial it is true.

## What the archive is for

Two purposes, and it is worth being exact that publication is not among them
([`CONTEXT.md`](../../CONTEXT.md), *Transcript Archive*):

- **Defensibility.** It is the resolvable end of custody's citation obligation. Without it,
  every `Session:` trailer in this repository is an attendance claim — free to write,
  indistinguishable from the truth, and precisely the ceremony §5 argues against.
- **Adjudication, later.** Whether a particular idea was Noah's construction or
  model-influenced is a question that can only be settled against contemporaneous raw
  material. Recollection at the time of challenge is not evidence, and it is the party under
  challenge who would be supplying it.

## Obligations this creates

- **Citation, from three places.** Notebook entries cite `sha256` + window + the segments the
  day owns; research documents carry `session:` in front matter; commits with an agent
  co-author on an authored file carry the trailer. `unrecorded` is a permitted and honest
  value — an absent key and an unrecordable session are different facts, and only one of them
  is anybody's fault.
- **Capture, from day one.** This is the clause that makes the decision expensive to reverse:
  an archive not kept cannot be reconstructed, and an uncaptured session can never be cited.
- **Append-only, with no exceptions.** Reorganising the archive is safe *if recorded*; removing
  a manifest row is not, because it retroactively converts live citations in the public record
  into dead ones. §2's rule is load-bearing here rather than tidy.
- **Retention.** Not settled by the record. [`§3.4`](../DATA-PROTOCOL.md)'s retention
  obligation is scoped to run artifacts under `Desk/mosaic/runs/`, and nothing in #3 sets a
  period for transcripts. Until one is set, the operative rule is law 4: deletion is
  irreversible and requires Noah's explicit go-ahead. Recorded here as **open**, not decided.
- **Opening.** What #3 settles is the *mechanism*: access is a grant Noah makes, and the
  citation is what a grantee checks against — §8.2's property is that the citation is
  "checkable by anyone Noah grants access to". The natural unit of a grant is therefore the
  cited session, since the citation already names one and its window. **The conditions under
  which a grant is owed** — which challenges compel one, to whom, and whether refusal is
  itself recorded — are **not settled** by #3 or by `DATA-PROTOCOL.md`, and this ADR does not
  invent them. An agent never makes such a grant; the archive is private research material and
  disclosure is Noah's alone.

## Consequences

- **The custody defence is only as good as the archive's coverage.** A gap in capture is
  invisible from the public side, because a missing session and a session never held look
  identical from a clone.
- **Resolution stays unmechanised.** §5 is already candid about this: CI can check the trailer
  is *present*, but a public runner cannot resolve it against a private archive. The check
  against fabricated citations is a human or checker-agent reading the archive, not the
  pipeline.
- **The archive is the sole holder of its contents**, which [law 1](../DATA-PROTOCOL.md)
  identifies as a liability rather than a feature. The decision accepts it deliberately —
  the alternative holder would be the public record, which is the thing being refused — and
  discharges it through backup rather than through a second copy anywhere in the repository.
- **The hash → path manifest is a precondition, not a detail.** Until the `Index` Sheet exists
  and is appended through a tool, every citation already in the record is unresolvable in
  practice. `DATA-PROTOCOL.md` records the construction; it does not record that the Sheet has
  been built.

## Not settled here

| | What is open |
|---|---|
| Placement | Which Drive root holds the archive. #3's second resolution named `Notes` as the notes tree and routed Weekly Reflections there; it did not assign the Transcript Archive a root, and §2's table leaves it unlisted. §2 forbids inventing one. |
| Retention | No period, and no arithmetic. §3.4 covers run artifacts only. |
| Disclosure | The conditions under which a grant of access is owed, and the scope of one. |
| Mechanism | Whether the `Index` hash → path manifest Sheet exists yet. |
