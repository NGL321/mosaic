"""PROTOTYPE — the CI gate suite of #176, and four candidate waiver models.

Pure. No git, no network, no GitHub: everything is read from `example/history.json`,
which `harvest.py` built once from this repository's real history. A gate is a
function from a **Change** — one merged pull request — to a list of **Findings**.

The suite is five gates. They are individually straightforward and are not the
question; the question is the **waiver**, which is why `waiver.py`'s worth of logic
lives at the bottom of this file rather than in a corner of it.

    §3  commit types and the computed bump          TYPE
    §4  branch classes                              BRANCH
    §5  custody: whose hand committed                CUSTODY
    #26 research-output front matter                 DOC
    --  links and paths that resolve                 LINK
"""

from __future__ import annotations

import json
import posixpath
import re
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).parent
HISTORY = json.loads((HERE / "example" / "history.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# What a gate returns
# ---------------------------------------------------------------------------

BLOCKING, ADVISORY, UNDECIDABLE = "blocking", "advisory", "undecidable"


@dataclass
class Finding:
    code: str          # C1, T3, L1 … stable, because a waiver names one
    gate: str
    severity: str
    subject: str       # the sha, path or branch the finding is about
    detail: str
    waived_by: object = None   # a Waiver, once resolution has run

    def __str__(self) -> str:
        mark = {BLOCKING: "FAIL", ADVISORY: "warn", UNDECIDABLE: "????"}[self.severity]
        if self.gate == "type" and self.code not in LIVE_CODES:
            mark = "gone"   # superseded by #176 §6a — the field it checks is deleted
        if self.waived_by is not None:
            mark = "WAIV"
        line = f"  {mark}  {self.code}  {self.subject:<28} {self.detail}"
        if self.waived_by is not None:
            line += f"\n            ↳ {self.waived_by.describe()}"
        return line


@dataclass
class Change:
    """One merged pull request, as CI sees it."""
    pr: int | None
    branch: str | None
    merge: dict
    commits: list[dict]
    waivers: list = field(default_factory=list)

    @property
    def files(self) -> set[str]:
        return {f for c in self.commits for f in c["files"] if f}

    def __str__(self) -> str:
        return f"#{self.pr} {self.branch} → {self.merge['sha']} {self.merge['subject'][:52]}"


def changes() -> list[Change]:
    return [Change(c["pr"], c["branch"], c["merge"], c["commits"]) for c in HISTORY["changes"]]


# ---------------------------------------------------------------------------
# CUSTODY — §5, now decidable, because #24 ruled the boundary is a signature
# ---------------------------------------------------------------------------
#
# #24: agents commit as a GitHub App through the API and are signed by GitHub;
# Noah signs his own commits; the check verifies signature and signer, never a
# name. Three classifications fall out, and the third is the one this repository
# is actually full of.

AUTHORED = frozenset({"CONTEXT.md", "CHARTER.md"})

HUMAN_KEYS = frozenset()   # Noah's own signing key. Empty: #175 has not run yet.
APP_LOGIN_SUFFIX = "[bot]"


def classify(commit: dict) -> tuple[str, str]:
    """(who, why) — `human`, `agent`, or `undecidable`."""
    login = commit.get("login") or ""
    signer = commit.get("signer")
    if not commit.get("verified"):
        return "undecidable", f"unsigned ({commit.get('reason')})"
    if login.endswith(APP_LOGIN_SUFFIX) and signer == "GitHub":
        return "agent", "App identity, signed by GitHub"
    if signer == "GitHub":
        # The hole. GitHub signs anything routed through its own API or web UI,
        # under a human's login, with a key that human does not hold. It attests
        # *the API call*, never the hand behind it — and every local agent
        # session in this repository holds a token that makes that call.
        return "undecidable", "signed by GitHub's key under a human login"
    if signer in HUMAN_KEYS or (HUMAN_KEYS and signer in HUMAN_KEYS):
        return "human", f"signed by {signer}"
    return "undecidable", f"signed by an unregistered key ({signer})"


def gate_custody(ch: Change) -> list[Finding]:
    out = []
    for c in ch.commits + [ch.merge]:
        who, why = classify(c)
        touched = sorted(set(c.get("files", [])) & AUTHORED)
        if who == "agent" and touched:
            out.append(Finding("C3", "custody", BLOCKING, c["sha"],
                               f"an agent identity committed {', '.join(touched)} — "
                               f"no era excuses this (§5)"))
        elif who == "undecidable":
            sev = BLOCKING if touched else UNDECIDABLE
            extra = f" while touching {', '.join(touched)}" if touched else ""
            code = "C2" if "GitHub's key" in why else "C1"
            out.append(Finding(code, "custody", sev, c["sha"], f"{why}{extra}"))
    return out


# ---------------------------------------------------------------------------
# TYPE — §3's computed bump, against §6's stated one
# ---------------------------------------------------------------------------
#
# **Half of this gate was ruled out of existence by driving it.** T3, T4, T5 and
# T7 all check a hand-written statement of something §3 says is computed, and
# #176 §6a deleted the statement instead: the merge commit is generated, so the
# only human judgement left is the type on each commit (T1), whether the branch
# stayed on one track (T6), and — post-merge, on `main` — whether the merge
# commit agrees with what `merge_message()` recomputes (T2).
#
# The superseded checks are kept because this file is a primary source for how
# that was decided, and because their counts against real history are the
# argument that decided it. `LIVE_CODES` is what survives.

LIVE_CODES = frozenset({"T1", "T2", "T6"})

RESEARCH = {"core": "MAJOR", "belt": "MINOR", "evidence": "PATCH", "record": "PATCH"}
TOOLING = {"feat": "MINOR", "fix": "PATCH", "chore": None}
RANK = {None: 0, "PATCH": 1, "MINOR": 2, "MAJOR": 3}
BUMP_GRAMMAR = re.compile(r"^(research|tooling) (MAJOR|MINOR|PATCH)$")


def type_of(subject: str) -> str | None:
    m = re.match(r"^([a-z]+):", subject)
    return m.group(1) if m else None


def track_of(t: str | None) -> str | None:
    return "research" if t in RESEARCH else "tooling" if t in TOOLING else None


def computed_bump(types: list[str]) -> dict[str, str]:
    """{track: level} — a branch on one track yields one entry."""
    best: dict[str, str] = {}
    for t in types:
        track, level = track_of(t), RESEARCH.get(t) or TOOLING.get(t)
        if track and level and RANK[level] > RANK.get(best.get(track)):
            best[track] = level
    return best


# §3's table order, pinned because a generator cannot be ambiguous: `evidence:`
# and `record:` tie on level, and §6 says the merge takes *the highest* type.
TABLE_ORDER = ["core", "belt", "evidence", "record", "feat", "fix", "chore"]


def highest_type(types: list[str]) -> str | None:
    known = [t for t in types if t in TABLE_ORDER]
    return min(known, key=TABLE_ORDER.index) if known else None


def merge_message(ch: Change, prose: str, gist: str) -> str:
    """The merge commit, computed. Ruled on #176 §6a.

    Everything mechanical is emitted; `prose` and `gist` are the author's, because
    they are the parts no function can produce. There is no `Bump:` line: §3 maps
    the subject's own type 1:1 onto track and level, and a second hand-written
    statement of a computed fact is how `b2b3b2c` landed a MAJOR as a PATCH.
    """
    top = highest_type([type_of(c["subject"]) for c in ch.commits]) or "chore"
    # The branch's own commits name their tickets — `(#96)`, `Resolves #5` — and
    # that is the convention §6 finding 6 above found everyone had already chosen
    # over naming the pull request. The generator reads it rather than fighting it.
    # …and it reads only the *trailing* parenthesised group, because a subject
    # like `record: land #5's provenance notation (#96)` cites #5 and resolves
    # #96. Harvesting every `#N` in the line conflates the two, which the first
    # draft of this function did.
    resolved: set[str] = set()
    for c in ch.commits:
        tail = re.search(r"\(([#\d,\s/]+)\)\s*$", c["subject"])
        if tail:
            resolved |= set(re.findall(r"#?(\d+)", tail.group(1)))
    resolved = sorted(resolved, key=int)
    tickets = ", ".join(f"#{n}" for n in resolved) or "no ticket"
    return f"{top}: {prose} (#{ch.pr})\n\nResolves {tickets}.\n\n{gist}\n"


def gate_type(ch: Change) -> list[Finding]:
    out, types = [], []
    for c in ch.commits:
        t = type_of(c["subject"])
        types.append(t)
        if t is None or track_of(t) is None:
            out.append(Finding("T1", "type", BLOCKING, c["sha"],
                               f"type {t!r} is outside §3's set — the bump cannot be computed"))
    known = [t for t in types if track_of(t)]
    tracks = {track_of(t) for t in known}
    if len(tracks) > 1:
        out.append(Finding("T6", "type", BLOCKING, ch.merge["sha"],
                           f"the branch carries both tracks {sorted(tracks)} — §1 decides the "
                           f"track when the branch is created, so one of these bumps goes nowhere"))

    computed = computed_bump(known)
    stated_raw = next((ln.split(":", 1)[1].strip()
                       for ln in ch.merge["body"].splitlines()
                       if ln.lower().startswith("bump:")), None)

    if stated_raw is None:
        out.append(Finding("T3", "type", BLOCKING, ch.merge["sha"],
                           "no `Bump:` line — §6 requires it stated, not inferred"))
    elif not BUMP_GRAMMAR.match(stated_raw):
        out.append(Finding("T4", "type", BLOCKING, ch.merge["sha"],
                           f"`Bump: {stated_raw}` is not `<track> <MAJOR|MINOR|PATCH>` — "
                           f"nothing in the record defines this field's grammar"))
    else:
        track, level = stated_raw.split()
        if computed.get(track) != level:
            out.append(Finding("T5", "type", BLOCKING, ch.merge["sha"],
                               f"stated `{stated_raw}`, computed "
                               f"{track} {computed.get(track)} from {sorted(set(known))}"))
        for other, lvl in computed.items():
            if other != track:
                out.append(Finding("T5", "type", BLOCKING, ch.merge["sha"],
                                   f"the branch also earns {other} {lvl}, and the merge "
                                   f"commit states only {track}"))

    merge_t = type_of(ch.merge["subject"])
    if merge_t and known:
        top = max(known, key=lambda t: RANK[RESEARCH.get(t) or TOOLING.get(t)])
        mine = RESEARCH.get(merge_t) or TOOLING.get(merge_t)
        best = RESEARCH.get(top) or TOOLING.get(top)
        if RANK[mine] < RANK[best]:
            out.append(Finding("T2", "type", BLOCKING, ch.merge["sha"],
                               f"merge subject is `{merge_t}:` ({mine}) but the branch's highest "
                               f"is `{top}:` ({best}) — §6 says the merge takes the highest"))
    if merge_t and ch.pr and f"(#{ch.pr})" not in ch.merge["subject"]:
        named = re.findall(r"#(\d+)", ch.merge["subject"])
        out.append(Finding("T7", "type", ADVISORY, ch.merge["sha"],
                           f"§6's form is `<type>: … (#PR)`; this names "
                           f"{'ticket ' + ', '.join('#' + n for n in named) if named else 'nothing'}"
                           f", not pull request #{ch.pr}"))
    return out


# ---------------------------------------------------------------------------
# BRANCH — §4's classes
# ---------------------------------------------------------------------------

CLASSES = frozenset({"research", "grilling", "prototype", "task", "inquiry", "tooling"})


def gate_branch(ch: Change) -> list[Finding]:
    if not ch.branch:
        return []
    cls = ch.branch.split("/")[0]
    if cls not in CLASSES:
        return [Finding("B1", "branch", BLOCKING, ch.branch,
                        f"`{cls}/` is not one of §4's classes {sorted(CLASSES)}")]
    return []


# ---------------------------------------------------------------------------
# LINK — relative links that resolve, against the tree the change produces
# ---------------------------------------------------------------------------
#
# `CHARTER.md` is *declared before it exists*, deliberately, by §5 — so the
# repository's one and only dangling link today is not a defect. This is the
# check that fires wrongly, on its first real case, in a repository with no
# broken links at all.

DECLARED_FUTURE = frozenset({"CHARTER.md"})

# Not ours. `README.md`'s licence path table already says so — the vendored
# `mattpocock/skills` trees are third-party and excluded from it — so the scope
# this gate needs is not a new list, it is that one, read by a second consumer.
THIRD_PARTY = (".agents/skills/", ".claude/skills/")


def gate_link(ch: Change | None, tree: set[str] | None = None) -> list[Finding]:
    """Scoped to the markdown the change touched — or the whole tree if `ch` is None.

    The scoping is not a detail. A repository-wide link check on every pull
    request convicts a branch of a dangling link somebody else wrote, which is
    the fastest way to teach everyone that red means nothing.
    """
    tree = tree if tree is not None else set(HISTORY["tree"])
    touched = None if ch is None else ch.files
    out = []
    for link in HISTORY["links"]:
        if touched is not None and link["file"] not in touched:
            continue
        if link["file"].startswith(THIRD_PARTY):
            continue
        target = link["target"].split("#")[0]
        if not target:
            continue
        here = posixpath.dirname(link["file"])
        resolved = posixpath.normpath(posixpath.join(here, target)).lstrip("./")
        if resolved in tree or any(p.startswith(resolved + "/") for p in tree):
            continue
        if resolved in DECLARED_FUTURE:
            out.append(Finding("L2", "link", ADVISORY, link["file"],
                               f"`{target}` does not exist yet — declared in advance by §5"))
            continue
        out.append(Finding("L1", "link", BLOCKING, link["file"],
                           f"`{target}` resolves to nothing"))
    return out


# ---------------------------------------------------------------------------
# DOC — #26's contract, over the research documents a change touches
# ---------------------------------------------------------------------------

def gate_doc(ch: Change) -> list[Finding]:
    out = []
    for path in sorted(ch.files):
        verdict = HISTORY["research_docs"].get(path)
        if verdict is None or verdict["pass"]:
            continue
        for failed in verdict["failed"]:
            code, detail = failed.split("  ", 1)
            out.append(Finding(f"D:{code}", "doc", BLOCKING, path, detail))
    return out


GATES = {
    "custody": gate_custody,
    "type": gate_type,
    "branch": gate_branch,
    "link": gate_link,
    "doc": gate_doc,
}


def run_gates(ch: Change) -> list[Finding]:
    return [f for name, fn in GATES.items() for f in fn(ch)]


# ---------------------------------------------------------------------------
# The waiver — the actual design question
# ---------------------------------------------------------------------------
#
# Four candidate homes, judged on five properties. The properties are not
# invented here; each is a place the record has already been bitten.
#
#   attributable  can CI tell *who* granted it? #24 made agent and human tellable
#                 apart at last, so this is newly answerable — and a waiver
#                 granted by the party the check constrains is not a waiver.
#   durable       is it still readable in a clone, in ten years, with no live
#                 service? (#63's rule for the register's attestation.)
#   countable     can the set be listed, so it cannot grow silently? The whole
#                 requirement #24 handed on: *visible rather than routed around.*
#   expiring      is there a moment it comes due, that its beneficiary does not
#                 control? (§2's grace, bounded three ways.)
#   in-scope-CI   can the gating run see it, offline, at the moment it fails?

@dataclass
class Waiver:
    code: str          # the finding code it waives — never a whole gate
    subject: str       # the sha/path/branch, or "*"
    reason: str
    model: str
    granted_by: str    # identity classification of the granting act
    expires: str | None

    def covers(self, f: Finding) -> bool:
        return f.code == self.code and self.subject in ("*", f.subject)

    def describe(self) -> str:
        return (f"waived via {self.model} by {self.granted_by}; "
                f"expires {self.expires or 'never'} — {self.reason}")


MODELS = {
    # model         attributable durable countable expiring in-CI
    "trailer":     (True,        True,   False,    False,   True),
    "pr-body":     (False,       False,  False,    False,   True),
    "file":        (True,        True,   True,     False,   True),
    "issue":       (True,        False,  True,     True,    False),
}
MODEL_NOTES = {
    "trailer": "a `Waive: C2 — reason` trailer on the commit that needs it. Attributable "
               "by the same signature the custody gate reads, and in the clone forever — "
               "but scattered across the history, so nothing can count the open set.",
    "pr-body": "a block in the pull request description. Editable by anyone with a write "
               "bit, after the fact, with no signature and no git object behind it: the "
               "one model where CI cannot say who granted it.",
    "file": "`.github/waivers.toml`, committed. Countable by reading one file, attributable "
            "to the commit that added the line, durable — and it never comes due.",
    "issue": "the `custody:deferred` mechanism, reused: an open issue that blocks `1.0.0`, "
             "cited as `Waive: #NNN`. The only model that expires. Not offline-readable, so "
             "the gating run must trust the tracker.",
}

# Which gates may be waived at all. #176: *a link check is a nuisance when it
# fires wrongly; a custody check is the programme's central claim.*
WAIVABLE = {
    "L1": True, "L2": True,
    "T7": True,
    "D:R10": True, "D:R13": True,
    "T1": True, "T2": True, "T3": True, "T4": True, "T5": True, "T6": True,
    "B1": True,
    "C1": False, "C2": False, "C3": False,
}


def resolve(ch: Change, findings: list[Finding], waivers: list[Waiver]) -> list[Finding]:
    """Attach waivers to findings, refusing the ones that must not be waivable."""
    for f in findings:
        for w in waivers:
            if not w.covers(f):
                continue
            if not WAIVABLE.get(f.code, False):
                f.detail += (f"  [REFUSED WAIVER: {f.code} is not waivable — "
                             f"the gate is the claim]")
                continue
            if w.granted_by != "human":
                f.detail += (f"  [REFUSED WAIVER: granted by {w.granted_by}; a waiver "
                             f"granted by the party the check constrains is not a waiver]")
                continue
            f.waived_by = w
            break
    return findings


def verdict(findings: list[Finding]) -> tuple[int, str]:
    live = [f for f in findings if f.waived_by is None
            and not (f.gate == "type" and f.code not in LIVE_CODES)]
    if any(f.severity == BLOCKING for f in live):
        return 1, "BLOCKED"
    if any(f.severity == UNDECIDABLE for f in live):
        return 2, "UNDECIDABLE — the gate could not measure what it claims to"
    if any(f.severity == ADVISORY for f in live):
        return 0, "PASS (with advisories)"
    return 0, "PASS"


def render(ch: Change, findings: list[Finding]) -> str:
    lines = [str(ch), ""]
    if not findings:
        lines.append("  (nothing to report)")
    for gate in GATES:
        rows = [f for f in findings if f.gate == gate]
        if rows:
            lines.append(f"  {gate.upper()}")
            lines.extend(str(f) for f in rows)
    code, word = verdict(findings)
    waived = sum(1 for f in findings if f.waived_by is not None)
    lines += ["", f"  {word}   (exit {code}; {len(findings)} findings, {waived} waived)"]
    return "\n".join(lines)
