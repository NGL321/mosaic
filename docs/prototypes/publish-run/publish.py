"""
PROTOTYPE (ticket #42) — the model behind prototype_tui.py.

A pure, in-memory model of publishing one run's output to
`Desk/mosaic/runs/<run-id>/` per docs/DATA-PROTOCOL.md §3.4 and §5.

Nothing here touches rclone, Drive, the network, or disk. The world is a dict.
The point is to make the collision, crash-recovery and verification cases
happen rather than be argued about.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field, replace
from enum import Enum

DRIVE_ROOT = "Desk/mosaic/runs"
MIRROR_ROOT = "~/Drive/Desk/mosaic/runs"  # the pull-only local mirror — §5's footgun


# --------------------------------------------------------------------------
# vocabulary
# --------------------------------------------------------------------------


class Verdict(Enum):
    PUBLISHED = "published"
    NOOP = "no-op (already published, byte-identical)"
    REFUSED = "refused"
    FAILED = "failed"
    PARTIAL = "partial — bytes up, nothing recorded"


class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"


class Collision(Enum):
    """What publish does when <run-id>/ already exists at the destination."""

    COMPARE = "compare: identical is a no-op, different is Noah's call"
    REFUSE = "refuse: any existing run id stops the publish"
    OVERWRITE = "overwrite: rclone copy's own default"
    MINT = "mint: publish under <run-id>-2"


class ManifestPoint(Enum):
    """When inquiries/NNN/runs/<run-id>.md gets written."""

    AFTER_VERIFY = "after verify"
    BEFORE_COPY = "before copy"


class Verify(Enum):
    SHA256 = "sha256 readback from Drive"
    RCLONE_CHECK = "rclone check (md5)"
    TRUST = "trust the copy (size + modtime)"


class Auth(Enum):
    ENV = "RCLONE_CONFIG_PASS from the environment"
    GITIGNORED = "git-ignored ~/.config/rclone/rclone.conf"
    IN_REPO = "tools/rclone.conf, committed"
    MISSING = "nothing configured"


# --------------------------------------------------------------------------
# world
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Blob:
    name: str
    content: str
    regenerable: bool = False

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.content.encode()).hexdigest()[:12]

    @property
    def size(self) -> int:
        return len(self.content)


@dataclass(frozen=True)
class RemoteFile:
    name: str
    sha256: str
    size: int
    has_sha256: bool = True  # Drive omits it for a small fraction of files


@dataclass(frozen=True)
class Manifest:
    run_id: str
    config_sha: str
    seed: int
    output_sha: str
    drive_path: str
    complete: bool = True


@dataclass
class World:
    """Everything publish.sh can see."""

    run_id: str = "2026-08-01-a1b2c3"
    config_sha: str = "cfg:9f4e21"
    seed: int = 20260801
    local: list[Blob] = field(default_factory=list)
    remote: dict[str, dict[str, RemoteFile]] = field(default_factory=dict)
    manifests: dict[str, Manifest] = field(default_factory=dict)
    dest_root: str = DRIVE_ROOT
    note: str = ""


@dataclass
class Config:
    collision: Collision = Collision.COMPARE
    manifest_point: ManifestPoint = ManifestPoint.AFTER_VERIFY
    verify: Verify = Verify.SHA256
    auth: Auth = Auth.GITIGNORED
    immutable: bool = True
    crash_after: int | None = None  # simulate the process dying mid-copy


# --------------------------------------------------------------------------
# the one thing worth naming: what "the sha256 of the output" means
# --------------------------------------------------------------------------


def tree_sha(blobs: list[Blob]) -> str:
    """A directory has no sha256. This is the one the manifest carries.

    sha256 over `<name> <sha256>` lines, sorted by name — so it is stable under
    upload order, and changes if any file's name or content changes.
    """
    lines = "".join(f"{b.name} {b.sha256}\n" for b in sorted(blobs, key=lambda b: b.name))
    return hashlib.sha256(lines.encode()).hexdigest()[:12]


# --------------------------------------------------------------------------
# the publish attempt
# --------------------------------------------------------------------------


@dataclass
class Step:
    stage: str
    ok: bool
    detail: str


@dataclass
class Finding:
    severity: Severity
    text: str


@dataclass
class Attempt:
    verdict: Verdict
    steps: list[Step] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    escalation: str = ""


def _dest(world: World) -> str:
    return f"{world.dest_root}/{world.run_id}"


def attempt(world: World, cfg: Config) -> tuple[World, Attempt]:
    """Run one publish. Returns the world it leaves behind and what happened."""
    world = replace(
        world,
        remote={k: dict(v) for k, v in world.remote.items()},
        manifests=dict(world.manifests),
    )
    steps: list[Step] = []
    out = Attempt(verdict=Verdict.FAILED, steps=steps)
    dest = _dest(world)
    local_sha = tree_sha(world.local)

    def step(stage: str, ok: bool, detail: str) -> None:
        steps.append(Step(stage, ok, detail))

    def fail(stage: str, detail: str, verdict: Verdict = Verdict.FAILED) -> tuple[World, Attempt]:
        step(stage, False, detail)
        out.verdict = verdict
        out.findings = findings(world, cfg, out)
        return world, out

    # -- preflight ---------------------------------------------------------
    if not world.local:
        return fail("preflight", "no output directory to publish")

    if cfg.auth is Auth.MISSING:
        return fail("preflight", "no rclone remote configured — nothing to copy to")

    step("preflight", True, f"{len(world.local)} file(s), tree sha256 {local_sha}")

    if world.dest_root.startswith("~"):
        # §5: this "succeeds" at every stage and publishes nothing.
        for b in world.local:
            world.remote.setdefault(dest, {})[b.name] = RemoteFile(b.name, b.sha256, b.size)
        step("copy", True, f"wrote {len(world.local)} file(s) into the local mirror")
        step("verify", True, "every byte present — locally")
        world.manifests[world.run_id] = Manifest(
            world.run_id, world.config_sha, world.seed, local_sha, dest
        )
        step("manifest", True, f"recorded drive_path {dest}")
        out.verdict = Verdict.PUBLISHED
        world.note = "next sync moves all of it to a dated safety-net folder"
        out.findings = findings(world, cfg, out)
        return world, out

    # -- collision ---------------------------------------------------------
    existing = world.remote.get(dest, {})
    if existing:
        same = {n: f for n, f in existing.items()}
        local_by_name = {b.name: b for b in world.local}
        identical = all(
            n in local_by_name and local_by_name[n].sha256 == f.sha256 for n, f in same.items()
        )
        complete = set(local_by_name) == set(same)

        if cfg.collision is Collision.REFUSE:
            return fail(
                "collision",
                f"{dest} exists ({len(same)} file(s)) — refusing",
                Verdict.REFUSED,
            )

        if cfg.collision is Collision.MINT:
            world.run_id = f"{world.run_id}-2"
            dest = _dest(world)
            step("collision", True, f"minting a second id — publishing to {dest}")

        elif cfg.collision is Collision.OVERWRITE:
            note = " (--immutable must be dropped to do this)" if cfg.immutable else ""
            step("collision", True, f"{dest} exists — overwriting {len(same)} file(s){note}")

        elif cfg.collision is Collision.COMPARE:
            if identical and complete:
                step("collision", True, f"{dest} exists and is byte-identical — nothing to do")
                if world.run_id not in world.manifests:
                    world.manifests[world.run_id] = Manifest(
                        world.run_id, world.config_sha, world.seed, local_sha, dest
                    )
                    step("manifest", True, "manifest was missing — written now")
                out.verdict = Verdict.NOOP
                out.findings = findings(world, cfg, out)
                return world, out
            if identical and not complete:
                missing = sorted(set(local_by_name) - set(same))
                step(
                    "collision",
                    True,
                    f"{len(same)} file(s) present and matching, {len(missing)} missing — resuming",
                )
            else:
                differing = sorted(
                    n
                    for n, f in same.items()
                    if n in local_by_name and local_by_name[n].sha256 != f.sha256
                )
                out.escalation = (
                    f"run id {world.run_id} exists at {dest} with different content "
                    f"({', '.join(differing) or 'file set differs'}). Overwriting an "
                    "original is irreversible — law 4 makes it Noah's call."
                )
                return fail("collision", out.escalation, Verdict.REFUSED)

    # -- manifest, early variant ------------------------------------------
    if cfg.manifest_point is ManifestPoint.BEFORE_COPY:
        world.manifests[world.run_id] = Manifest(
            world.run_id, world.config_sha, world.seed, local_sha, dest
        )
        step("manifest", True, f"recorded output_sha {local_sha}, drive_path {dest}")

    # -- copy --------------------------------------------------------------
    uploaded = 0
    for i, b in enumerate(world.local):
        if cfg.crash_after is not None and i >= cfg.crash_after:
            step("copy", False, f"process died after {uploaded} of {len(world.local)} file(s)")
            out.verdict = Verdict.PARTIAL
            out.findings = findings(world, cfg, out)
            return world, out
        prior = world.remote.get(dest, {}).get(b.name)
        if prior and prior.sha256 == b.sha256:
            continue
        if prior and cfg.immutable and cfg.collision is not Collision.OVERWRITE:
            return fail(
                "copy",
                f"--immutable: {b.name} exists at the destination and differs — rclone stops",
                Verdict.REFUSED,
            )
        world.remote.setdefault(dest, {})[b.name] = RemoteFile(b.name, b.sha256, b.size)
        uploaded += 1
    step("copy", True, f"rclone copy — {uploaded} file(s) transferred")

    # -- verify ------------------------------------------------------------
    remote_now = world.remote.get(dest, {})
    if cfg.verify is Verify.TRUST:
        step("verify", True, "size + modtime match (rclone's default comparison)")
    elif cfg.verify is Verify.RCLONE_CHECK:
        bad = [b.name for b in world.local if remote_now.get(b.name, None) is None]
        if bad:
            return fail("verify", f"missing at destination: {', '.join(bad)}")
        step("verify", True, f"rclone check --checksum — {len(world.local)} file(s), md5")
    else:
        no_sha = [n for n, f in remote_now.items() if not f.has_sha256]
        bad = [
            b.name
            for b in world.local
            if remote_now.get(b.name) is None or remote_now[b.name].sha256 != b.sha256
        ]
        if bad:
            return fail("verify", f"sha256 mismatch or missing: {', '.join(bad)}")
        detail = f"sha256 read back for {len(world.local) - len(no_sha)} file(s)"
        if no_sha:
            detail += f"; Drive returned none for {', '.join(no_sha)} — fell back to md5"
        step("verify", True, detail)

    # -- manifest ----------------------------------------------------------
    if cfg.manifest_point is ManifestPoint.AFTER_VERIFY:
        world.manifests[world.run_id] = Manifest(
            world.run_id, world.config_sha, world.seed, local_sha, dest
        )
        step("manifest", True, f"recorded output_sha {local_sha}, drive_path {dest}")

    out.verdict = Verdict.PUBLISHED
    out.findings = findings(world, cfg, out)
    return world, out


# --------------------------------------------------------------------------
# findings — deliberately separate from the verdict
#
# A publish can succeed and be wrong in the same breath. Collapsing the two is
# how "it said OK" becomes "nothing was ever published".
# --------------------------------------------------------------------------


def findings(world: World, cfg: Config, out: Attempt) -> list[Finding]:
    f: list[Finding] = []

    if world.dest_root.startswith("~"):
        f.append(
            Finding(
                Severity.CRITICAL,
                "destination is inside the pull-only local mirror. Every stage passed and "
                "nothing was published — §5's footgun, reported as success.",
            )
        )

    if cfg.auth is Auth.IN_REPO:
        f.append(
            Finding(
                Severity.CRITICAL,
                "rclone credentials committed to the repo — §3.2 forbids the repo, Drive "
                "plaintext, logs and notebook output. The repo is public.",
            )
        )

    if cfg.collision is Collision.OVERWRITE and out.verdict is Verdict.PUBLISHED:
        f.append(
            Finding(
                Severity.CRITICAL,
                "overwrote an existing run id. Law 4: overwriting an original is "
                "irreversible and needs Noah's explicit go-ahead, not a flag default.",
            )
        )

    if cfg.collision is Collision.MINT and out.verdict is Verdict.PUBLISHED:
        f.append(
            Finding(
                Severity.HIGH,
                "minted a second run id to dodge a collision. The run id is now not the "
                "run's identity, and a notebook citation cannot be resolved without "
                "knowing which attempt it meant.",
            )
        )

    if cfg.manifest_point is ManifestPoint.BEFORE_COPY and out.verdict in (
        Verdict.FAILED,
        Verdict.PARTIAL,
        Verdict.REFUSED,
    ):
        f.append(
            Finding(
                Severity.HIGH,
                "a manifest exists for a publish that did not finish. The record claims a "
                "Drive path with nothing behind it — §8.2's convenience made into a lie.",
            )
        )

    if out.verdict is Verdict.PARTIAL:
        f.append(
            Finding(
                Severity.MEDIUM,
                "bytes are at the destination with no manifest. Not corruption — but the "
                "next attempt meets a collision that is really a resume.",
            )
        )

    if cfg.verify is Verify.TRUST and out.verdict is Verdict.PUBLISHED:
        f.append(
            Finding(
                Severity.HIGH,
                "verified nothing. rclone's default compares size and modtime, which a "
                "fresh upload satisfies by construction; the manifest's sha256 was never "
                "checked against what Drive holds.",
            )
        )

    if cfg.verify is Verify.RCLONE_CHECK and out.verdict is Verdict.PUBLISHED:
        f.append(
            Finding(
                Severity.MEDIUM,
                "verified against md5. Fine as a transfer check, but the manifest's claim "
                "is a sha256 and Drive can return one — so the claim itself stays "
                "unverified end to end.",
            )
        )

    regen = [b.name for b in world.local if b.regenerable]
    if regen and out.verdict in (Verdict.PUBLISHED, Verdict.NOOP):
        f.append(
            Finding(
                Severity.MEDIUM,
                f"published regenerable bytes ({', '.join(regen)}). §3.3 says store the "
                "seed and regenerate; these ride the mirror and the backup forever.",
            )
        )

    if not cfg.immutable and cfg.collision is Collision.COMPARE:
        f.append(
            Finding(
                Severity.MEDIUM,
                "the compare rule is enforced only by this script. Without --immutable, "
                "any hand-run `rclone copy` overwrites silently.",
            )
        )

    return f


# --------------------------------------------------------------------------
# scenarios
# --------------------------------------------------------------------------

CKPT = Blob("checkpoint-final.pt", "weights@step50000")
METRICS = Blob("metrics.jsonl", "loss curve, 50k steps")
FIG = Blob("fig-grokking.png", "the plot")
ACTS = Blob("activations.npz", "layer 3, all steps", regenerable=True)


def fresh() -> World:
    return World(local=[CKPT, METRICS, FIG])


SCENARIOS: dict[str, tuple[str, callable]] = {}


def scenario(key: str, label: str):
    def deco(fn):
        SCENARIOS[key] = (label, fn)
        return fn

    return deco


@scenario("1", "a clean first publish")
def _s1() -> World:
    return fresh()


@scenario("2", "re-run of a run that already published, byte-identical")
def _s2() -> World:
    w = fresh()
    dest = _dest(w)
    w.remote[dest] = {b.name: RemoteFile(b.name, b.sha256, b.size) for b in w.local}
    w.manifests[w.run_id] = Manifest(w.run_id, w.config_sha, w.seed, tree_sha(w.local), dest)
    return w


@scenario("3", "the same run id, different bytes")
def _s3() -> World:
    w = fresh()
    dest = _dest(w)
    stale = [Blob(CKPT.name, "weights@step10000"), METRICS, FIG]
    w.remote[dest] = {b.name: RemoteFile(b.name, b.sha256, b.size) for b in stale}
    w.manifests[w.run_id] = Manifest(w.run_id, w.config_sha, w.seed, tree_sha(stale), dest)
    return w


@scenario("4", "resume after a crash — half the files up, no manifest")
def _s4() -> World:
    w = fresh()
    dest = _dest(w)
    w.remote[dest] = {CKPT.name: RemoteFile(CKPT.name, CKPT.sha256, CKPT.size)}
    return w


@scenario("5", "Drive returns no sha256 for one file")
def _s5() -> World:
    w = fresh()
    dest = _dest(w)
    w.remote[dest] = {
        CKPT.name: RemoteFile(CKPT.name, CKPT.sha256, CKPT.size, has_sha256=False)
    }
    return w


@scenario("6", "the output carries regenerable intermediates")
def _s6() -> World:
    return World(local=[CKPT, METRICS, FIG, ACTS])


@scenario("7", "destination points into the local Drive mirror")
def _s7() -> World:
    w = fresh()
    w.dest_root = MIRROR_ROOT
    return w
