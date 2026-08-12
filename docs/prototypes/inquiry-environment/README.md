# PROTOTYPE — the environment contract, and the two gates that enforce it

Ticket [#64](https://github.com/NGL321/mosaic/issues/64). Built to be thrown away, and
retained as a **primary source** for how the contract was chosen — not as a tool. Nothing
runs it, nothing depends on it, and it never touches GitHub, git, a registry, or the
network.

```console
python docs/prototypes/inquiry-environment/prototype_tui.py
```

- `example/base/Dockerfile` — the base recipe. Tooling track.
- `example/base.digest` — the repo-level pin. **The default for new freezes, and nothing else.**
- `example/env.lock` — the other file that freezes, beside `config.yaml`.
- `example/run-manifest.md` — the run manifest, with the `env:` block this ticket adds.
- `contract.py` — fourteen named refusals across **two** gates.
- `prototype_tui.py` — breaks the contract one field at a time, so each refusal can be
  *made to happen* rather than described.

## The question

#64 asks what a reproducible Inquiry environment consists of and when it freezes. Premise
12 already fixes the shape — base image by digest plus a per-experiment resolved lock, both
committed, image built and never stored, resolved during the adequacy phase, frozen with
the config SHA. What was open is the five items the ticket lists: what is in the base, what
the lock format is, what is cached and on what key, what the manifest records, and how the
self-hosted tier is held to the same container.

The standard being met is not devops hygiene. It is **defensibility in an infant field**: a
stranger rebuilds the environment from committed text rather than being asked to find an
image.

## What the prototype found

**1. The base holds exactly what a lockfile cannot express — and that is not "the big
things".** The tempting division is by size or by build time. The real one is *what pip
resolves* versus *what pip presupposes*. A lock naming `torch` presupposes an interpreter,
a libc and a CUDA userspace it cannot itself install; those are baked. Research packages
are never baked, because they are the thing being searched over. This answers the ticket's
second item in the direction it suspected: system libraries **do** force pinning up into
the base, but **CUDA mostly does not** — modern torch wheels carry their own CUDA
userspace, so the base is thinner than expected and the lock is doing more work than
"a Python lock" suggests.

**2. There is exactly one thing neither the digest nor the lock can pin, and it is the
host NVIDIA driver.** It lives outside the container *by construction* — the container
runtime injects it from the host — so no recipe in this repository reaches it. The honest
response is not to pretend otherwise: `env.lock` states a **range**, every manifest states
the **observed value**, and the gap is visible rather than assumed away. This is the edge
of the reproducibility claim, and writing it down is what keeps the claim true. Silence
would read as *no host dependency*, which is false for every job the accelerator
requirement will route — the map's own retrieval rule, in its local dialect: **an absent
line item is not a documented zero.**

**3. The environment is a second file, committed in the same commit as `config.yaml` — not
a field inside it.** `inquiries/README.md` says an Experiment is identified by its config's
sha256 **and nothing else**. Fold the environment in and two things break at once: a base
bump forks every Experiment into a new one, and a byte-identical config under another
Inquiry stops being the same Experiment, which is the property #164 leaned on when it made
one Inquiry serviceable by many Conjectures. So: **frozen together, identity kept apart.**
The freeze event is unchanged — one commit, now containing two files.

**4. `env.lock` pins the base digest itself; the repo-level pin is a default, never a
pointer.** This is where the prototype pushes back on premise 12. The premise says bumping
the base *"never invalidates past results, because manifests pin the digest they ran on"* —
true of results **already recorded**, and silent about the re-run. Under an indirection,
re-running an unchanged frozen config next year executes it on a different CUDA, and the
disagreement has no visible cause. Copying the digest into `env.lock` at freeze makes a
frozen Inquiry **immune to the tooling track**, which is what freezing was supposed to
mean. The cost is real and is the thing to decide out loud: a frozen Inquiry never receives
a security patch, and unfreezing to get one is a new Inquiry.

**5. The cache is keyed on the inputs, and the key is a correctness property rather than a
performance one.** `sha256(base_digest ‖ lock_sha256)`, and nothing else — not the Inquiry,
not the branch, not the date. Two Inquiries that resolved to the same environment *should*
collide; that is the cache working. The rule that matters is that **a hit and a miss must
produce the same environment**, which is exactly what keying on the inputs buys: a miss
costs minutes and can never be a correctness event. A key containing a branch name or
`latest` names two different environments on two different days and is refused. GHCR is
free for public repositories, and the derived image living in a registry is not a §3.3
violation — a registry is not this repository, which still holds only the recipe.

**6. The manifest's `env:` block is per run, and that is a deliberate asymmetry rather than
a filing choice.** An Experiment is its config SHA; a Run happens on an environment. So two
runs of *the same Experiment* on two base digests are the same Experiment and may still
disagree. That looks like a defect until you notice the alternative is worse — the manifest
is what converts such a disagreement from mysterious into diagnosable, and it is the only
place the driver value can live.

**7. The block is written by the runner, never by the job.** A container cannot verify its
own digest from the inside; a job reporting its own image is reporting a string it was
handed. The only party that can honestly say what was pulled is the party that pulled it.
The `/etc/mosaic-env` marker in the base is retained anyway, and the recipe says plainly
what it is: a **self-report** that catches the accident, not the adversary.

**8. Containerisation on the self-hosted tier is enforced at publish, not at execution —
and this is the ticket's main structural finding.** The failure to prevent is a result that
only reproduces on Noah's desktop, and it arrives the first time someone runs a script
directly. No execution-side check survives that, because the person bypassing the workflow
is the person who would have had to run the check. So the gate moves: **a run whose
environment the publish gate refuses produces no manifest, and a result with no manifest is
not in the record.** The script still runs. It just cannot become a finding. This is the
same move #60 made with `config.yaml` — do not police the act, police the artifact the act
must produce — and it is why `contract.py` has two gates rather than one. The freeze gate
is cheap and bypassable; the publish gate is the one that holds.

**9. The trust root is the runner, and #58's finding recurs one layer down.** If the runner
is the only honest reporter of the environment, then the environment guarantee rests on who
may register a runner — which is exactly where #58 landed the tier guarantee: on the admin
list, not on a label. Two independent properties of this design now depend on the same
fact, and #58's rule that **the dispatch App never holds `administration`** is load-bearing
for both.

## Open, and handed on

- **The driver range is declared and never enforced.** `env.lock` states `>= 550.54` and
  the manifest records what it saw, but nothing refuses a run on a host below the range.
  Enforcing it needs the runner to read the driver *before* claiming the job, which is a
  dispatch-pipeline question rather than a format one — [#66](https://github.com/NGL321/mosaic/issues/66).
- **[#68](https://github.com/NGL321/mosaic/issues/68) is still the load-bearing `if`.**
  Everything here assumes a provider that accepts `@sha256:`. Modal's acceptance remains
  undocumented; a negative moves the tier to RunPod and changes nothing in this contract
  except which provider satisfies it.
- **What the base costs to bump.** Bumping is tooling track and cheap by finding 4, but
  nothing here says who bumps it, on what schedule, or what re-validates it. It is a
  tooling-track chore with no owner yet.
