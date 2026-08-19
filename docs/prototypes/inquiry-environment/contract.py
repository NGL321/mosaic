"""PROTOTYPE — the environment contract, and the two gates that enforce it.

Ticket #64. Throwaway. Nothing depends on this and nothing runs it in CI.

The question: *what does a reproducible Inquiry environment consist of, and when does it
freeze?* Premise 12 fixes the shape — base image by digest plus a resolved lock, both
committed, image built and never stored, resolved during the adequacy phase and frozen
with the config SHA. This file is the attempt to make that mechanical, under #26 R6's
warning that a rule satisfiable by writing a word is not a rule.

**There are two gates, not one, and the split is the ticket's main finding.**

- `check_freeze` runs at the freeze commit, over `config.yaml` + `env.lock`. It is the
  cheap one, and it is advisory in the sense that a determined person can bypass it by
  not running the workflow at all.
- `check_manifest` runs at publish, over the run manifest. It is the load-bearing one,
  because a run whose environment it refuses **produces no manifest, and a result with no
  manifest is not in the record.** That is the same move #60 made with `config.yaml`: do
  not police the execution, police the thing the execution has to produce. It is how
  premise 12's last clause — the self-hosted tier runs the same container — is enforced
  without anyone having to be trusted at the keyboard.

Run the driver, not this file:

    python docs/prototypes/inquiry-environment/prototype_tui.py
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# Refusals. Each is a named, emittable finding — never a bare exit code.
# --------------------------------------------------------------------------

REFUSALS = {
    # ---- the freeze commit -------------------------------------------------
    "NO_LOCK_AT_FREEZE": (
        "config.yaml appeared without env.lock in the same commit. Premise 12 freezes the "
        "environment WITH the config SHA, and a half-freeze is worse than none: the "
        "instrument is fixed while the thing it runs on is still free, so the "
        "discriminating measurement is confirmatory about an apparatus nobody pinned."
    ),
    "LOCK_BEFORE_CONFIG": (
        "env.lock is committed and config.yaml is not. The environment froze while the "
        "search is still running. Resolving the environment IS adequacy-phase work — "
        "hypothesis-blind by construction, and therefore exactly what agents were "
        "authorised to search over. Freezing it early takes a tunable away from them "
        "before the criterion that justifies fixing it has passed."
    ),
    "BASE_BY_TAG": (
        "The base image is named by tag rather than by digest. A tag can be repointed "
        "underneath you; a digest cannot. This is the single failure the whole contract "
        "exists to prevent, and it costs nothing to make impossible."
    ),
    "BASE_INDIRECTION": (
        "env.lock refers to the repo-level base pin instead of carrying a digest of its "
        "own. Indirection means a tooling-track bump silently reaches backwards into a "
        "frozen Inquiry — a re-run of an unchanged config on a different CUDA. The "
        "repo-level file is the DEFAULT FOR NEW FREEZES and never a live pointer."
    ),
    "UNPINNED_PACKAGE": (
        "A package is named without a sha256, or with a range rather than a version. A "
        "version alone is a name an index can repoint, which is the same failure a tag "
        "is, one layer up."
    ),
    "NO_HOST_BOUNDARY": (
        "env.lock declares no host boundary. Neither the digest nor the lock can pin the "
        "NVIDIA driver — the container runtime injects it from outside — so it is the one "
        "part of the environment this repository cannot reproduce. Silence reads as 'no "
        "host dependency', which is false for every job the accelerator requirement will "
        "route. Absence is not a documented zero."
    ),
    "ENV_IN_CONFIG": (
        "The environment is declared inside config.yaml. inquiries/README.md: an "
        "Experiment is identified by its config's sha256 AND NOTHING ELSE. Folding the "
        "environment in forks every Experiment on a base bump, and stops a byte-identical "
        "config under another Inquiry from being the same Experiment. Two files, one "
        "commit: frozen together, identity kept apart."
    ),

    # ---- the publish gate --------------------------------------------------
    "NO_ENV_BLOCK": (
        "The manifest records no environment. This is the refusal that enforces "
        "containerisation on a tier nobody administers remotely: a run that cannot state "
        "what it ran on does not enter the record. Someone running the training script "
        "directly on the desktop is not stopped from running it — they are stopped from "
        "producing a result."
    ),
    "ENV_SELF_REPORTED": (
        "The environment block was written by the job, from inside the container. A "
        "container cannot verify its own digest from the inside, so a job reporting its "
        "own image is reporting a string it was handed. The honest reporter is THE PARTY "
        "THAT PULLED — the CI runner in the cloud, the launch tool on the desktop. Which "
        "one it is does not matter; being outside the container does."
    ),
    "ENV_DRIFT": (
        "The manifest's base digest is not the one env.lock froze. For a run in Measuring "
        "this is fatal — the discriminating measurement was made on an apparatus other "
        "than the frozen one, and calling that result confirmatory is exactly the "
        "assertion #63 exists to prevent."
    ),
    "CACHE_KEY_MISMATCH": (
        "The image digest is not the one the cache key derives. The cache is keyed on "
        "base digest + lock, so a hit and a miss must produce the same environment or the "
        "cache is a reproducibility hazard rather than a speedup. A mismatch is the one "
        "symptom a poisoned or misconfigured cache shows."
    ),
    "CACHE_KEYED_ON_MUTABLE_REF": (
        "The cache key includes a branch, a tag or 'latest'. A key that can name two "
        "different environments on two different days does not identify an environment. "
        "Key on the inputs — digest and lock — and a miss becomes a cost in minutes "
        "rather than a correctness event."
    ),
    "NO_DRIVER_OBSERVED": (
        "The manifest states no observed driver. env.lock states a range because the "
        "driver is outside the container; the manifest is where the range becomes a "
        "value. Without it, two runs of one Experiment that disagree are mysterious "
        "instead of diagnosable."
    ),
}

MUTABLE_REFS = ("latest", "main", "branch", "ref_name", "head", "nightly")

DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
PINNED_PACKAGE = re.compile(r"^[A-Za-z0-9._-]+==[^\s]+\s+--hash=sha256:[0-9a-f]{64}$")


# A hazard is not a refusal. #9: an untestable hazard is DECLARED and attaches permanently
# to every leg the Inquiry earns — a hazard you must test is a cost, a hazard you must name
# is not, which is what keeps naming truthful. This one is appended by the gate rather than
# written by anyone, so it cannot be forgotten by the party with the motive to forget it.
HAZARDS = {
    "environment_unattested": (
        "The manifest was hand-entered rather than written by the party that pulled the "
        "image, so no attested record exists of what this run executed on. Ancestry is "
        "intact and the Register is unaffected — #56 derives Register from ancestry and "
        "#63 exists to stop anything else moving it — but the environment claim rests on "
        "a person's word. Attaches to every leg this Inquiry earns, and travels into the "
        "coverage report someone reads at a stall."
    ),
}


@dataclass
class Verdict:
    refusals: list[tuple[str, str]] = field(default_factory=list)
    hazards: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.refusals

    def refuse(self, code: str, detail: str = "") -> None:
        self.refusals.append((code, detail))

    def hazard(self, name: str) -> None:
        self.hazards.append(name)


def cache_key(base_digest: str, lock_sha: str) -> str:
    """base + lock, and nothing else.

    Deliberately not the Inquiry, not the branch, not the date. Two Inquiries that
    resolved to the same environment SHOULD collide — that is the cache working. Adding
    identity to the key would buy nothing and cost every hit.
    """
    return "sha256:" + hashlib.sha256(
        (base_digest + "\n" + lock_sha).encode()).hexdigest()


# --------------------------------------------------------------------------
# Gate 1 — the freeze commit.
# --------------------------------------------------------------------------

def check_freeze(
    lock: dict | None,
    config: dict | None,
    *,
    cache_key_inputs: tuple[str, ...] = ("base_digest", "lock_sha256"),
) -> Verdict:
    v = Verdict()

    if config and not lock:
        v.refuse("NO_LOCK_AT_FREEZE")
    if lock and not config:
        v.refuse("LOCK_BEFORE_CONFIG")

    if config and any(k in config for k in ("env", "environment", "image", "base")):
        named = [k for k in ("env", "environment", "image", "base") if k in config]
        v.refuse("ENV_IN_CONFIG", f"declared: {', '.join(named)}")

    if lock:
        base = lock.get("base") or {}
        digest = str(base.get("digest") or "")
        if base.get("from_repo_pin") or digest.endswith(".digest"):
            v.refuse("BASE_INDIRECTION", f"points at: {digest or 'tools/env/base.digest'}")
        elif not DIGEST.match(digest):
            v.refuse("BASE_BY_TAG", f"reference: {base.get('image', '')}:{digest or 'latest'}")

        bad = [p for p in (lock.get("packages") or []) if not PINNED_PACKAGE.match(str(p))]
        if bad:
            v.refuse("UNPINNED_PACKAGE", ", ".join(str(p) for p in bad))

        boundary = lock.get("host_boundary") or {}
        if not boundary.get("nvidia_driver"):
            v.refuse("NO_HOST_BOUNDARY")

    bad_keys = [k for k in cache_key_inputs
                if any(m in k.lower() for m in MUTABLE_REFS)]
    if bad_keys:
        v.refuse("CACHE_KEYED_ON_MUTABLE_REF", f"in key: {', '.join(bad_keys)}")

    return v


# --------------------------------------------------------------------------
# Gate 2 — publish. The load-bearing one.
# --------------------------------------------------------------------------

def check_manifest(
    manifest: dict,
    lock: dict,
    *,
    state: str = "Measuring",
    authored_by: str = "app",
) -> Verdict:
    v = Verdict()
    env = manifest.get("env")

    if not env:
        v.refuse("NO_ENV_BLOCK")
        return v

    if env.get("reported_by") == "job":
        v.refuse("ENV_SELF_REPORTED")

    # Hand-entered, and ALLOWED. The gate does not refuse it and does not touch the
    # Register — it names a hazard. Authorship is what makes hand-entry visible, and #17
    # already pays for that: once the App signs as itself, a manifest committed by Noah's
    # account is a different object in git, permanently, in ancestry. The gate never has
    # to detect a forgery, because there is nothing to forge — the mark is the author.
    if authored_by != "app":
        v.hazard("environment_unattested")

    frozen = str((lock.get("base") or {}).get("digest") or "")
    ran = str(env.get("base_digest") or "")
    if state == "Measuring" and frozen and ran and frozen != ran:
        v.refuse("ENV_DRIFT", f"frozen {frozen[:19]}… ran {ran[:19]}…")

    expected = cache_key(ran, str(env.get("lock_sha256") or ""))
    got = str(env.get("image_digest") or "")
    if got and got != expected:
        v.refuse("CACHE_KEY_MISMATCH", f"key {expected[:19]}… image {got[:19]}…")

    if not env.get("nvidia_driver"):
        v.refuse("NO_DRIVER_OBSERVED")

    return v


def render(v: Verdict, *, label: str, subject: str) -> str:
    if v.ok:
        lines = [f"ACCEPTED — {subject}", f"  {label}"]
    else:
        lines = [
            f"REFUSED — {subject}",
            f"  {len(v.refusals)} refusal(s). {label}",
            "",
        ]
        for code, detail in v.refusals:
            lines.append(f"  [{code}]{(' ' + detail) if detail else ''}")
            lines.append(f"      {REFUSALS[code]}")
            lines.append("")
    for name in v.hazards:
        lines.append("")
        lines.append(f"  + untestable hazard appended to the Inquiry: {name}")
        lines.append(f"      {HAZARDS[name]}")
    return "\n".join(lines)
