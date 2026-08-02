# PROTOTYPE — what `publish.sh` does when the happy path does not happen

Ticket [#42](https://github.com/NGL321/mosaic/issues/42). Built to be thrown away, and
retained as a **primary source** for how the publish semantics were chosen — not as a tool.
Nothing runs it, nothing depends on it, and it never touches rclone, Drive, git, or the
network.

```console
python docs/prototypes/publish-run/prototype_tui.py
```

## The question

[`docs/DATA-PROTOCOL.md`](../../DATA-PROTOCOL.md) §3.4 requires durable run artifacts to land
at `Desk/mosaic/runs/<run-id>/`, and §5 says how: an explicit `rclone copy` at the end of a
run, never a write into the pull-only mirror. Nothing implements it. #42 names four things
the protocol does not decide, and they are the only interesting part:

1. Where the run manifest is emitted, relative to the upload.
2. What happens when the run id already exists at the destination.
3. Whether the tool verifies the hash after upload or trusts the copy.
4. Where the Drive credential lives.

`rclone copy` answers all four by default, and every default is wrong for this repository.
The prototype exists to make that visible: seven worlds, four switchable policies, and a
verdict that is deliberately separate from the findings — because a publish can succeed and
be wrong in the same breath.

## What the prototype proposes

### 1. A directory has no sha256, so name the one the manifest carries

[`inquiries/README.md`](../../../inquiries/README.md) says a manifest records "the sha256 of
the output". A run's output is a *directory*, and the protocol never says what that hashes
to. The prototype uses a **tree hash** — sha256 over `<name> <sha256>` lines, sorted by name:

```
checkpoint-final.pt e127d46974de
fig-grokking.png    1452a7e1d2d5
metrics.jsonl       86a0869f7b4b   → sha256 → a71fa6ade5b2
```

Stable under upload order, changes if any file's name or content changes, and computable
without Drive. §2's identity rule says files are identified by content hash and paths are
mutable — a tree hash extends that to the run without inventing anything.

### 2. Collision is two questions, and the protocol already answers both

This is the finding, and the reason the prototype was worth building. "What happens when the
run id exists" reads as one question with four candidate answers — refuse, overwrite, skip,
mint a new id. Driving it shows there are **two different situations** wearing one name, and
each already has an answer in the five laws:

| Destination state | What it is | Verdict |
|---|---|---|
| Same files, same hashes | a re-run of a publish that already worked | **no-op**, and write the manifest if it is missing |
| A subset, all matching | a crash mid-copy | **resume** — copy what is missing |
| Any file differs | a second run reused the id, or the config changed | **refuse**, escalate to Noah |

Only the third is law 4 territory, and there it is unambiguous: overwriting an original is
irreversible, so it is Noah's explicit go-ahead, not a flag default. The other two are not
collisions at all — they are idempotency, which is the property the tool needs to be safe to
re-run from a workflow.

Press `[4]` then `[p]`: the crash resumes cleanly. Press `[c]` to `refuse` and `[p]`: the
strict policy — the one that looks safest — makes crash recovery impossible without manual
cleanup in Drive, which is the operation nobody should be doing by hand. Press `[3]` `[p]`
for the refusal that matters, then `[c]` to `overwrite` and `[p]` to watch it published,
green, with a critical finding under it.

**`--immutable` is what moves this rule out of the script.** rclone with `--immutable`
"disallows modification… existing files will never be updated" — so a hand-run copy hits the
same wall as the tool. Without it, the compare rule is enforced only by whoever remembers to
run `publish.sh` instead of `rclone copy`. This is the same reasoning
[#24](https://github.com/NGL321/mosaic/issues/24)'s prototype settled for the depth cap: *a
guard belongs wherever it is most effective, not wherever the code that noticed it lives.*

`mint` is included because it is the tempting answer and it is a trap: it makes the run id
not the run's identity, so a notebook citation can no longer be resolved without knowing
which attempt was meant.

### 3. Hash before the copy; write the manifest after the verify

The two are separable and the prototype separates them. The output hash is computable the
moment the run ends, and it must be, because it is what the verify step compares Drive
against — computing it twice invites two answers.

The manifest is a different act: it is the record asserting that a result exists. Press
`[m]` to `before-copy`, `[x]` to crash mid-copy, then `[p]`: the repository now holds a
manifest whose `drive_path` points at a directory with one file in it. The sha256 in that
manifest is still *true* — §8.2's "the hash is the claim, the path is a convenience" holds —
but the record has published a convenience that is a lie, and nothing marks it.

So: **hash first, manifest last.** The window where bytes exist and the record does not is
recoverable — the next run resumes and writes the manifest. The reverse window is not
detectable at all without going and looking.

### 4. Verify by reading sha256 back, and say so when Drive cannot

`rclone copy`'s default comparison is size and modification time, which a fresh upload
satisfies by construction. It proves the transfer was attempted, not that it landed.

The good news is a fact worth recording, because it decides this: **Google Drive returns
SHA256.** rclone's Drive backend documents "Hash algorithms MD5, SHA1 and SHA256 are
supported. Note, however, that a small fraction of files uploaded may not have SHA1 or SHA256
hashes especially if they were uploaded before 2018" (rclone.org/drive, retrieved
2026-08-01). So the manifest's own claim can be verified end to end against the destination,
rather than proxied through md5.

Where Drive returns none, the prototype falls back to md5 and **prints which file it fell
back on** rather than reporting a clean pass (`[5]`, `[p]`). A verification that silently
degrades is worse than one that does not exist, because it is believed.

### 5. Auth: git-ignored file locally, environment variable in CI

§3.2, applied without novelty — `~/.config/rclone/rclone.conf` outside the repo, or
`RCLONE_CONFIG_*` from the environment where a runner needs it. `[a]` cycles to
`tools/rclone.conf, committed` so the failure is visible: it publishes perfectly and reports
critical, because the repository is public by design and §3.2's ban covers the repo, Drive
plaintext, logs *and notebook output*.

### The §6 contract, drafted

```markdown
- reads   — a local run output directory; inquiries/NNN-slug/config.yaml for the config SHA
- writes  — Desk/mosaic/runs/<run-id>/ (canonical); inquiries/NNN-slug/runs/<run-id>.md (canonical)
- auth    — Drive, via rclone; credentials from a git-ignored rclone.conf or the environment
- surface — CLI, invoked at the end of a run
- safe to regenerate from scratch? — the tool yes; its output no. Published bytes are
  originals under law 4 once the manifest cites them.
```

## Findings from building it

1. **Three of the four questions were already answered by the five laws; only the manifest's
   emission point was genuinely open.** Idempotency is law 4 plus law 2, verification is the
   §2 identity rule, credentials are §3.2. What the ticket read as four design decisions is
   really one decision and three applications — which is a good sign about the protocol, and
   the reason this ticket did not need to become a policy debate.
2. **`rclone copy`'s defaults are the anti-pattern list in executable form.** Overwrite on
   difference, compare by modtime, no manifest. `publish.sh` is not a wrapper that adds
   convenience; it is a wrapper that *removes* defaults, and it should be read that way when
   somebody is tempted to bypass it.
3. **The mirror footgun cannot be caught by testing the happy path.** `[7]` passes every
   stage, writes a manifest, and reports `PUBLISHED` — and nothing is published. A preflight
   assertion that the destination resolves to a *remote*, not a local path, is the only thing
   between the tool and a silent §5 violation, and it costs one line.
4. **§3.3 shows up here and cannot be settled here.** `[6]` publishes an `activations.npz`.
   The tool can warn that regenerable bytes are riding to canonical storage; it cannot decide
   whether they should, because that is a property of the experiment's design, which §3.3
   makes a design-time constraint rather than a cleanup policy. A warning is the right amount
   of opinion for a publish step to hold.

## Still open

- **Retention.** §3.4's runs × checkpoints × size arithmetic is a separate ticket and needs
  [#7](https://github.com/NGL321/mosaic/issues/7)'s first rung. `publish.sh` should not
  prune, and this prototype does not model it.
- **Who calls it.** A run inside a container on a hosted runner has to get a Drive credential
  and a network path out. That is the research loop map's
  ([#55](https://github.com/NGL321/mosaic/issues/55)) dispatch question, not this one — but
  it is the reason the credential must work from the environment as well as a file.
- **The `Index` manifest Sheet.** §8.2 and §3.6 put the hash → path manifest in `Index`, as a
  Drive-native Sheet appended through a tool. The per-run manifest in `inquiries/*/runs/` is
  not that Sheet. Whether `publish.sh` also appends a row, or a second tool does, is unfiled.

## Not in scope

No `publish.sh` written, no rclone invoked, no `tools/` change, no network, no persistence,
no tests. The prototype does not build the tool — it makes four policies disagree out loud
over the same seven worlds.
