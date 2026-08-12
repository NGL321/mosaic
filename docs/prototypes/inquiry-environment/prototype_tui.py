"""PROTOTYPE — drive the two environment gates over a real lock and a real manifest.

    python docs/prototypes/inquiry-environment/prototype_tui.py

Loads `example/env.lock` and `example/run-manifest.md`, then breaks them one field at a
time. Every defect below is one somebody will actually commit — the plausible mistake, not
the absurd one. Case `d` is the one the whole ticket exists for: the script run straight on
the desktop, which works fine, and cannot produce a result.
"""

from __future__ import annotations

import copy
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import contract  # noqa: E402
import yaml  # noqa: E402

HERE = Path(__file__).parent


def load(path: Path) -> dict:
    """These files are YAML with a comment banner. Strip nothing; PyYAML reads comments."""
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


# The frozen instrument. Not this ticket's object, so it is a stub — what matters is
# whether it is present at the freeze commit and whether it is trying to hold the
# environment.
CONFIG = {"model": {"width": 128, "depth": 2}, "task": "modular_addition", "seed_policy": "drawn"}


# ---------------------------------------------------------------------------
# Freeze-commit mutations
# ---------------------------------------------------------------------------

def base_by_tag(lock, man, cfg):
    lock["base"]["digest"] = None
    lock["base"]["image"] = "ghcr.io/ngl321/mosaic-base:cuda12.4"
    return lock, man, cfg


def base_indirection(lock, man, cfg):
    """The tidy-looking refactor. One pointer, one place to bump — and it reaches backwards."""
    lock["base"] = {"from_repo_pin": "tools/env/base.digest"}
    return lock, man, cfg


def unpinned_package(lock, man, cfg):
    lock["packages"][2] = "ripser>=0.6"
    return lock, man, cfg


def version_without_hash(lock, man, cfg):
    """The commonest real mistake: `pip freeze` output, which pins versions and no hashes."""
    lock["packages"] = [str(p).split(" --hash")[0] for p in lock["packages"]]
    return lock, man, cfg


def drop_host_boundary(lock, man, cfg):
    lock.pop("host_boundary", None)
    return lock, man, cfg


def env_in_config(lock, man, cfg):
    """Folding the environment into config.yaml. Reads as simplification; forks every Experiment."""
    cfg["image"] = lock["base"]["digest"]
    return lock, man, cfg


def no_lock_at_freeze(lock, man, cfg):
    return None, man, cfg


def lock_before_config(lock, man, cfg):
    return lock, man, None


# ---------------------------------------------------------------------------
# Publish-gate mutations
# ---------------------------------------------------------------------------

def desktop_run(lock, man, cfg):
    """THE case. Ran outside any container, on Noah's machine, successfully."""
    man.pop("env", None)
    return lock, man, cfg


def self_reported(lock, man, cfg):
    man["env"]["reported_by"] = "job"
    return lock, man, cfg


def base_drift(lock, man, cfg):
    """A base bump landed between the freeze and the discriminating run."""
    man["env"]["base_digest"] = "sha256:" + "b" * 64
    man["env"]["image_digest"] = contract.cache_key(
        man["env"]["base_digest"], man["env"]["lock_sha256"])
    return lock, man, cfg


def stale_cache(lock, man, cfg):
    man["env"]["cache"] = "hit"
    man["env"]["image_digest"] = "sha256:" + "e" * 64
    return lock, man, cfg


def drop_driver(lock, man, cfg):
    man["env"].pop("nvidia_driver", None)
    return lock, man, cfg


def identity(lock, man, cfg):
    return lock, man, cfg


CASES = [
    ("0", "the contract as written", identity, {}),
    ("1", "base named by tag", base_by_tag, {}),
    ("2", "env.lock points at the repo-level pin", base_indirection, {}),
    ("3", "a package pinned by range", unpinned_package, {}),
    ("4", "pip freeze output — versions, no hashes", version_without_hash, {}),
    ("5", "no host boundary declared", drop_host_boundary, {}),
    ("6", "environment folded into config.yaml", env_in_config, {}),
    ("7", "config.yaml froze without env.lock", no_lock_at_freeze, {}),
    ("8", "env.lock committed while still Searching", lock_before_config, {}),
    ("d", "ran on the desktop, no container", desktop_run, {}),
    ("s", "env block written by the job", self_reported, {}),
    ("b", "base bumped between freeze and measurement", base_drift, {}),
    ("c", "cache hit returned a foreign image", stale_cache, {}),
    ("n", "no observed driver", drop_driver, {}),
    ("k", "cache keyed on the branch name", identity,
     {"cache_key_inputs": ("base_digest", "lock_sha256", "github_ref_name")}),
]


def run(key: str) -> None:
    label, mutate, flags = next((c[1], c[2], c[3]) for c in CASES if c[0] == key)
    lock = load(HERE / "example" / "env.lock")
    man = load(HERE / "example" / "run-manifest.md")
    cfg = copy.deepcopy(CONFIG)
    lock, man, cfg = mutate(lock, man, cfg)

    print("\n" + "=" * 76)
    print(f"CASE {key} — {label}")
    print("=" * 76)

    freeze = contract.check_freeze(lock, cfg, **flags)
    print(contract.render(
        freeze, label="Freeze commit: config.yaml + env.lock.", subject="freeze 172"))

    if lock:
        publish = contract.check_manifest(man, lock)
        print(contract.render(
            publish,
            label="Publish: the run enters the record, or it does not.",
            subject=f"run {man.get('run_id', '?')}"))


def main() -> None:
    print(__doc__)
    while True:
        print("\n" + "-" * 76)
        for k, label, _, _ in CASES:
            print(f"  {k}  {label}")
        print("  all  run every case      q  quit")
        choice = input("\n> ").strip().lower()
        if choice in ("q", "quit", ""):
            return
        if choice == "all":
            for k, *_ in CASES:
                run(k)
            continue
        if choice in {c[0] for c in CASES}:
            run(choice)
        else:
            print("  ?")


if __name__ == "__main__":
    main()
