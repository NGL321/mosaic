"""
PROTOTYPE (ticket #11) — the I/O half: fill `entry.py`'s model from real sources.

Reads, in order of trust:

1. **This repository's history** — merges and commits in the day's window. Mechanical
   and verifiable from the artifact, which is *not* the same as verified: these notes are
   `T3` like everything else generated, and ride into the ledger via `spine`.
2. **GitHub** — PR and issue transitions for the same window, via `gh`. Optional; the
   prototype degrades to git-only if `gh` is missing, and says so.
3. **A real Transcript Archive session** — the Claude Code JSONL under
   `~/.claude/projects/`. Used for its *metadata and content hash only*: the entry
   cites `sha256` and never quotes the transcript. A scrub pass runs before anything
   could reach a public file and **fails closed**: a candidate secret raises
   `ScrubBlocked` and no entry is produced (#3 §3.2 is a prohibition, not a reporting
   requirement).
4. **A narrative pass** — `pass-<session>.json`, the lines only a reader of the
   transcript can write: *why*, and *what was abandoned*. Emitted at `T3`
   (machine-produced, unverified) because that is exactly what they are until Noah
   annotates them. This is the file a generation agent writes in production; the one
   in this directory was written from the real session named in it.

Nothing here is pure and nothing here is worth keeping — the model in `entry.py` is.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

from entry import Cite, Entry, Kind, Note, Session, Trigger, anchor

REPO = Path(__file__).resolve().parents[3]
GH = "https://github.com/NGL321/mosaic"
ARCHIVE = Path.home() / ".claude" / "projects" / "C--Users-noahl-mosaic"

SECRET_PATTERNS = [
    re.compile(p) for p in (
        r"sk-[A-Za-z0-9]{20,}", r"gh[pousr]_[A-Za-z0-9]{16,}", r"AKIA[0-9A-Z]{16}",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"(?i)(api[_-]?key|password|secret)\s*[:=]\s*\S{8,}",
    )
]


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True,
                          text=True, encoding="utf-8", check=True).stdout


def _gh(*args: str) -> object | None:
    try:
        out = subprocess.run(["gh", *args], cwd=REPO, capture_output=True,
                             text=True, encoding="utf-8", check=True).stdout
        return json.loads(out)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None


# ------------------------------------------------------------------- sessions

IDLE = timedelta(hours=1)
"""A session ends when it has not been worked on for an hour. Noah's rule, and it is
not cosmetic: a transcript *file* is not a session. `b1243c96` splits into four
segments spanning two days, one of them straddling midnight. So the file's hash alone
cannot cite a day's work — the entry cites hash **plus segment window**."""


def segments(stamps: list[datetime]) -> list[tuple[datetime, datetime]]:
    if not stamps:
        return []  # a truncated or in-progress transcript has no segments, not one empty one
    stamps = sorted(stamps)
    out = [[stamps[0], stamps[0]]]
    for t in stamps[1:]:
        if t - out[-1][1] > IDLE:
            out.append([t, t])
        else:
            out[-1][1] = t
    return [(a, b) for a, b in out]


def owning_day(segment: tuple[datetime, datetime]) -> str:
    """The day a session belongs to is the local day it **ended** on.

    Only one day can own it, and the end is the side the generator is standing on: an
    entry is written when the segment closes, so the owning day is the day whose entry is
    being generated at that moment. Dating by the start would mean reopening — and
    regenerating — a day already annotated and already read, every time a session crossed
    midnight. (Not, as the first draft claimed, because the end is "the side that is
    actually defined": the idle rule cuts both edges with the same threshold.)"""
    return segment[1].astimezone().date().isoformat()


class ScrubBlocked(Exception):
    """A candidate secret reached the public boundary. #3 §3.2 is a prohibition, so the
    entry is not emitted at all — the count surfaces here and generation stops. Counting
    without blocking would publish the secret and note underneath that it had."""


class NoSessionForDay(Exception):
    """This day owns none of the file's segments. The honest citation is none: quietly
    substituting the file's last segment would publish a window the day does not own,
    which is the exact over-citation the window exists to prevent."""


def read_session(session_id: str, day: str | None = None) -> tuple[Session, dict]:
    """Session metadata plus the content hash the entry will cite. The transcript's
    *content* is read only for the scrub; its *structure* — timestamps, branches, skills —
    is what the metadata comes from. Neither is carried into the entry.

    `day` selects the segments the idle rule assigns to that day; everything counted
    below is counted **within those segments**, so a file feeding two days does not
    report the same 505 events to both."""
    path = ARCHIVE / f"{session_id}.jsonl"
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()

    records = []
    hits: list[int] = []
    for n, line in enumerate(raw.decode("utf-8", "replace").splitlines(), 1):
        if not line.strip():
            continue
        records.append(json.loads(line))
        if any(p.search(line) for p in SECRET_PATTERNS):
            hits.append(n)
    if hits:
        raise ScrubBlocked(
            f"{len(hits)} candidate secret(s) in {path.name} at line(s) "
            f"{', '.join(map(str, hits[:10]))} — no entry emitted for {day or 'this day'}"
        )

    stamps = [datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00"))
              for d in records if d.get("timestamp")]
    segs = segments(stamps)
    mine = [s for s in segs if owning_day(s) == day] if day else segs
    if not mine:
        raise NoSessionForDay(f"{path.name} has no segment ending on {day}")
    owned = [i + 1 for i, s in enumerate(segs) if s in mine]
    window = (mine[0][0], mine[-1][1])

    prompts = events = 0
    branches: set[str] = set()
    skills: set[str] = set()
    prs: set[int] = set()
    for d in records:
        ts = d.get("timestamp")
        if ts and not (window[0] <= datetime.fromisoformat(ts.replace("Z", "+00:00")) <= window[1]):
            continue
        events += 1
        if d.get("type") == "user" and not d.get("isMeta") and isinstance(
            (d.get("message") or {}).get("content"), str
        ):
            prompts += 1
        if d.get("gitBranch"):
            branches.add(d["gitBranch"])
        if d.get("attributionSkill"):
            skills.add(d["attributionSkill"])
        if d.get("prNumber"):
            prs.add(d["prNumber"])

    session = Session(
        sha256=digest,
        # Local, not UTC: the owning day is a local day, and a window printed in UTC
        # next to a local date contradicts itself on the page — this entry's session
        # would read as ending on the 30th under a heading dated the 29th.
        started=window[0].astimezone().isoformat(), ended=window[1].astimezone().isoformat(),
        events=events, prompts=prompts,
        branch=sorted(branches)[-1] if branches else "?",
        skill=", ".join(sorted(skills)),
        # Which segments, not how many: "2 of 4" cannot distinguish a day owning
        # segments 1 and 2 from one owning 1 and 4, and the window only bounds them.
        segment=f"segment(s) {','.join(map(str, owned))} of {len(segs)}",
    )
    return session, {"prs": sorted(prs), "branches": sorted(branches),
                     "segments": segs, "owning_days": sorted({owning_day(s) for s in segs})}


# --------------------------------------------------------- mechanical notes

TYPE_KIND = {"core:": Kind.LANDED, "belt:": Kind.LANDED, "evidence:": Kind.LANDED,
             "record:": Kind.LANDED, "feat:": Kind.LANDED, "fix:": Kind.ACTIVITY,
             "chore:": Kind.ACTIVITY}


def commit_notes(start: str, end: str, used: dict[str, int]) -> list[Note]:
    """Commits in the window, as the entry sees them. Note what this *cannot* produce:
    a line about why anything happened. Everything here is a fact about an artifact,
    which is why it is cheap to verify and boring to read on its own."""
    fmt = "%h%x1f%aI%x1f%s"
    out = _git("log", "--all", "--no-merges", f"--since={start}", f"--until={end}",
               f"--format={fmt}")
    notes: list[Note] = []
    seen: set[str] = set()
    for line in reversed([x for x in out.splitlines() if x.strip()]):
        sha, _when, subject = line.split("\x1f")
        ctype = subject.split(" ")[0] if ":" in subject.split(" ")[0] else ""
        kind = TYPE_KIND.get(ctype, Kind.ACTIVITY)
        text = subject.split(": ", 1)[1] if ": " in subject else subject
        text = text[:1].upper() + text[1:]  # not .capitalize(): it lowercases PR, CI, T3
        # `--all` is necessary — the day's work lives on branches, not on main — and it
        # returns the same subject several times over, once per branch it was replayed
        # onto. Deduplicating on the subject is the cheap fix; the first render without
        # it showed the same scaffold commit three times in one entry.
        key = re.sub(r"\W+", "", text.lower())
        if key in seen:
            continue
        seen.add(key)
        cites = (Cite("commit", sha, f"{GH}/commit/{sha}"),)
        notes.append(Note(
            id=anchor(cites, used), kind=kind, text=text.rstrip("."), tier="T3",
            spine=True, cites=cites,
        ))
    return notes


def issue_notes(day: str, used: dict[str, int]) -> list[Note]:
    """Issue and label transitions — the Curriculum-milestone and debt triggers. `gh`
    is optional here; without it the prototype runs on git alone and says so on screen."""
    data = _gh("issue", "list", "--state", "all", "--limit", "80", "--json",
               "number,title,createdAt,labels")
    if not isinstance(data, list):
        return []
    notes = []
    for it in data:
        created = it["createdAt"][:10]
        if created != day and created != _next_day(day):
            continue
        labels = {lb["name"] for lb in it["labels"]}
        kind = Kind.DEBT if ("custody:deferred" in labels or "debt:open" in labels) else Kind.ACTIVITY
        if "debt:discharged" in labels:
            kind = Kind.MILESTONE
        cites = (Cite("issue", f"#{it['number']}", f"{GH}/issues/{it['number']}"),)
        notes.append(Note(id=anchor(cites, used), kind=kind, tier="T3", spine=True,
                          text=f"Filed: {it['title']}", cites=cites))
    return notes


def _next_day(day: str) -> str:
    return (datetime.fromisoformat(day) + timedelta(days=1)).date().isoformat()


def pr_trigger(number: int) -> Trigger | None:
    data = _gh("pr", "view", str(number), "--json", "number,title,state,mergedAt")
    if not isinstance(data, dict):
        return None
    return Trigger("task", f"#{number}",
                   f"[PR #{number}]({GH}/pull/{number}) {data['state'].lower()}")


# ------------------------------------------------------------------- assembly

def load(session_id: str) -> Entry:
    """Build the entry for the day a real session ran, from real sources."""
    here = Path(__file__).parent
    narrative = json.loads((here / f"pass-{session_id[:8]}.json").read_text(encoding="utf-8"))

    day = narrative["date"]
    session, meta = read_session(session_id, day)
    start, end = f"{day}T00:00:00-07:00", f"{_next_day(day)}T04:00:00-07:00"

    # Two counters, one per layer. Annotations only ever attach to prose lines, so
    # ordinals are counted *within* the annotatable layer: otherwise a ledger line
    # citing the same commit would push a narrative line from `a598221` to `a598221#2`,
    # and an anchor that moves when the ledger changes is the positional bug again in
    # a different costume.
    spine_used: dict[str, int] = {}
    used: dict[str, int] = {}
    notes = commit_notes(start, end, spine_used) + issue_notes(day, spine_used)
    seen = {n.text.lower() for n in notes}
    for raw in narrative["notes"]:
        if raw["text"].lower() in seen:
            continue
        cites = tuple(Cite(c["kind"], c["ref"], _url(c)) for c in raw.get("cites", []))
        # The pass file does not name anchors: they are derived, so that a reworded
        # narrative line keeps its annotation and a recited one cannot steal it.
        notes.append(Note(
            id=anchor(cites, used), kind=Kind(raw["kind"]), text=raw["text"],
            tier=raw.get("tier", "T3"), debt=raw.get("debt", ""), cites=cites,
        ))

    triggers = [Trigger("merge", s, s) for s in narrative.get("merge_triggers", [])]
    for pr in meta["prs"]:
        if t := pr_trigger(pr):
            triggers.append(t)

    return Entry(date=day, slug=narrative["slug"], title=narrative["title"],
                 triggers=tuple(triggers), notes=tuple(notes), sessions=(session,))


def _url(c: dict) -> str:
    return {"commit": f"{GH}/commit/{c['ref']}",
            "issue": f"{GH}/issues/{c['ref'].lstrip('#')}",
            "pr": f"{GH}/pull/{c['ref'].lstrip('#')}",
            "doc": f"{GH}/blob/main/{c['ref']}"}.get(c["kind"], "")
