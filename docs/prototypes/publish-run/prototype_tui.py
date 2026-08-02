"""
PROTOTYPE (ticket #42) — throwaway TUI shell over publish.py.

Run:  python docs/prototypes/publish-run/prototype_tui.py

Number keys load a world; [p] publishes into it. Switch the collision rule with
[c], where the manifest is written with [m], verification with [v], --immutable
with [i], and where credentials come from with [a]. Everything is in memory;
nothing touches rclone, Drive, git, the network, or disk.

The three things worth doing deliberately are written on the screen.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from publish import (  # noqa: E402
    SCENARIOS,
    Attempt,
    Auth,
    Collision,
    Config,
    ManifestPoint,
    Severity,
    Verdict,
    Verify,
    World,
    attempt,
    tree_sha,
)

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

B, D, R = "\x1b[1m", "\x1b[2m", "\x1b[0m"
RED, YEL, GRN, CYA, MAG = ("\x1b[31m", "\x1b[33m", "\x1b[32m", "\x1b[36m", "\x1b[35m")

VERDICT_COLOUR = {
    Verdict.PUBLISHED: GRN,
    Verdict.NOOP: CYA,
    Verdict.REFUSED: YEL,
    Verdict.FAILED: RED,
    Verdict.PARTIAL: MAG,
}
SEV_COLOUR = {Severity.CRITICAL: RED, Severity.HIGH: YEL, Severity.MEDIUM: CYA}

CYCLE = {
    "c": (
        "collision",
        [Collision.COMPARE, Collision.REFUSE, Collision.OVERWRITE, Collision.MINT],
    ),
    "m": ("manifest_point", [ManifestPoint.AFTER_VERIFY, ManifestPoint.BEFORE_COPY]),
    "v": ("verify", [Verify.SHA256, Verify.RCLONE_CHECK, Verify.TRUST]),
    "a": ("auth", [Auth.GITIGNORED, Auth.ENV, Auth.IN_REPO, Auth.MISSING]),
}


def getkey() -> str:
    try:
        import msvcrt

        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):
            msvcrt.getch()
            return ""
        return ch.decode("utf-8", "replace").lower()
    except ImportError:
        import termios
        import tty

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def rule(text: str = "") -> None:
    print(f"{D}{'─' * 78}{R}" + (f" {B}{text}{R}" if text else ""))


def render(world: World, cfg: Config, last: Attempt | None, scenario: str) -> None:
    print("\x1b[2J\x1b[H", end="")
    print(f"{B}PROTOTYPE #42 — publishing a run to Drive{R}   {D}throwaway; nothing is real{R}\n")

    print(f"  {D}world{R}   {scenario}")
    print(
        f"  {D}config{R}  collision {B}{cfg.collision.value}{R}\n"
        f"          manifest {B}{cfg.manifest_point.value}{R}   "
        f"verify {B}{cfg.verify.value}{R}\n"
        f"          auth {B}{cfg.auth.value}{R}   "
        f"--immutable {B}{'on' if cfg.immutable else 'off'}{R}   "
        f"crash {B}{'after 1 file' if cfg.crash_after is not None else 'off'}{R}"
    )

    rule("local output")
    for b in world.local:
        tag = f" {MAG}regenerable{R}" if b.regenerable else ""
        print(f"    {b.name:<24} {D}sha256 {b.sha256}  {b.size}B{R}{tag}")
    print(f"    {D}tree sha256 → {R}{B}{tree_sha(world.local)}{R}")

    rule("destination")
    if not world.remote:
        print(f"    {D}(empty){R}")
    for path, files in world.remote.items():
        colour = RED if path.startswith("~") else ""
        print(f"    {colour}{path}/{R}")
        for f in files.values():
            miss = f"  {YEL}no sha256 from Drive{R}" if not f.has_sha256 else ""
            print(f"      {f.name:<22} {D}{f.sha256}{R}{miss}")
    if world.note:
        print(f"    {RED}→ {world.note}{R}")

    rule("repo — inquiries/NNN-slug/runs/")
    if not world.manifests:
        print(f"    {D}(no manifests){R}")
    for m in world.manifests.values():
        print(
            f"    {m.run_id}.md  {D}config {m.config_sha}  seed {m.seed}  "
            f"output {m.output_sha}{R}\n      {D}drive_path {m.drive_path}{R}"
        )

    if last:
        rule("last publish")
        for s in last.steps:
            mark = f"{GRN}✓{R}" if s.ok else f"{RED}✗{R}"
            print(f"    {mark} {s.stage:<10} {s.detail}")
        c = VERDICT_COLOUR[last.verdict]
        print(f"\n    {c}{B}{last.verdict.value.upper()}{R}")
        for f in last.findings:
            sc = SEV_COLOUR[f.severity]
            print(f"    {sc}{f.severity.value:>8}{R}  {f.text}")

    rule()
    for k, (lbl, _) in SCENARIOS.items():
        print(f"  {B}[{k}]{R} {lbl}")
    print(f"\n  {B}[p]{R} publish")
    print(
        f"  {B}[c]{R} collision  {B}[m]{R} manifest point  {B}[v]{R} verify  "
        f"{B}[i]{R} --immutable  {B}[a]{R} auth  {B}[x]{R} crash mid-copy  "
        f"{B}[z]{R} reset  {B}[q]{R} quit"
    )
    print(
        f"\n  {D}Worth doing: (3) then [p] — the refusal that matters. Then [c] to "
        f"overwrite and [p].{R}\n"
        f"  {D}             (4) then [p] — a collision that is really a resume; [c] to "
        f"refuse and [p].{R}\n"
        f"  {D}             (1), [m] to before-copy, [x], [p] — the record claims a path "
        f"that is empty.{R}"
    )


def main() -> None:
    cfg = Config()
    key = "1"
    label, build = SCENARIOS[key]
    world, last = build(), None

    while True:
        render(world, cfg, last, f"({key}) {label}")
        k = getkey()
        if k == "q":
            print()
            return
        if k in SCENARIOS:
            key = k
            label, build = SCENARIOS[k]
            world, last = build(), None
        elif k == "p":
            world, last = attempt(world, cfg)
        elif k == "z":
            world, last = build(), None
        elif k == "i":
            cfg.immutable = not cfg.immutable
        elif k == "x":
            cfg.crash_after = None if cfg.crash_after is not None else 1
        elif k in CYCLE:
            attr, options = CYCLE[k]
            cur = getattr(cfg, attr)
            setattr(cfg, attr, options[(options.index(cur) + 1) % len(options)])


if __name__ == "__main__":
    main()
