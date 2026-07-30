"""
PROTOTYPE (ticket #11) — the portable half: what a Lab Notebook entry *is*.

The question this module answers: given a day's worth of mechanically harvestable
facts (merges, PR transitions, label transitions, session metadata) plus a narrative
pass over the transcript, what is the entry's data model, what gets *left out*, and
how are generated and annotated content kept visually distinct?

Pure. No I/O, no terminal codes, no git. `harvest.py` fills the model from real
sources; `prototype_tui.py` drives it. Nothing flows back into here.

**Settled by Noah, 2026-07-30**, after driving this:

1. **Nothing in the notebook promotes a Provenance Tier.** An annotation is a T1 claim
   sitting next to a T3 one; the generated line stays T3. Promotion needs Noah restating
   the thing himself, which is the gate the tiers exist to impose. Most generated content
   lives at T3 until it is bumped, and T1 is his own thinking.
2. **A session ends after an hour without work, and belongs to the day it ended.** Only
   one day can own it, and the end is the side the *generator* is standing on: the entry
   being written when the segment closes is that day's. (The first draft justified this
   by claiming the end is "the side that is actually defined", which review correctly
   rejected — the idle rule cuts both edges with the same threshold.)
3. **Annotations are not canonical.** Anything worth making canon earns its own entry and
   its own work — a promotion for the idea, not a louder annotation. `reanchor()` is what
   that buys: regeneration is permitted, orphans are reported rather than dropped.
4. **Rendering B — annotation-first — is the format.** "This is my research project. It
   just happens to be AI-accelerated. Tool output shouldn't be the first thing anyone
   sees." A, C and D stay in this file as the comparison that produced the choice.

Three things are load-bearing and are the bits worth lifting out if the design holds:

1. `Note.cites` is non-optional in practice — `admissible()` drops any generated line
   that cannot name an artifact. This is the volume rule with teeth: the generator
   cannot narrate, because narration has nothing to cite.
2. `select()` splits prose from ledger and applies a hard word budget to the prose.
   Mechanically restated history (`Note.spine`) never competes for that budget, and
   nothing over budget is dropped silently — it collapses into a table that is cheap
   to skip and still auditable.
3. Annotations are a separate layer keyed to a line's **anchor** — its primary
   citation, never its position — and never edits to generated text. That is what makes
   the visual distinction mechanical rather than a habit.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum

# ------------------------------------------------------------------ provenance

TIERS = {
    "T1": "derived unaided",
    "T2": "derived with assistance, personally verified",
    "T3": "machine-produced, unverified",
}


class Kind(str, Enum):
    """What a generated line is *about*. Decides whether it survives the volume dial."""

    LANDED = "landed"        # a decision reached the record
    REVERSED = "reversed"    # something the programme took back
    DEADEND = "deadend"      # a direction abandoned — kept deliberately
    DEBT = "debt"            # an obligation filed
    MILESTONE = "milestone"  # curriculum / charter movement
    ACTIVITY = "activity"    # mechanical churn. Machine exhaust, by definition.


class Volume(str, Enum):
    DECISIONS = "decisions"    # what moved, and what was taken back
    FULL = "full"              # + dead ends and debt — the intended default
    EVERYTHING = "everything"  # + churn. The failure mode, kept visible for contrast.


KINDS_AT = {
    Volume.DECISIONS: {Kind.LANDED, Kind.REVERSED, Kind.MILESTONE},
    Volume.FULL: {Kind.LANDED, Kind.REVERSED, Kind.MILESTONE, Kind.DEADEND, Kind.DEBT},
    Volume.EVERYTHING: set(Kind),
}

BUDGET_WORDS = 320
"""Hard ceiling on generated prose per entry. Not a guideline — `select()` enforces it
by moving the tail into a collapsed ledger. Picked so an entry is readable in about a
minute; the number is exactly the kind of thing to argue with while driving this."""


# ----------------------------------------------------------------- data model

@dataclass(frozen=True)
class Cite:
    """An artifact a generated line points at. No cite, no line."""

    kind: str  # commit | pr | issue | doc | session
    ref: str
    url: str = ""

    def md(self) -> str:
        label = {"commit": f"`{self.ref}`", "pr": f"PR {self.ref}", "issue": self.ref}.get(
            self.kind, f"`{self.ref}`"
        )
        return f"[{label}]({self.url})" if self.url else label


LEDGER_NS = "ledger:"


def anchor(cites: "tuple[Cite, ...]", used: dict[str, int], spine: bool = False) -> str:
    """Derive a line's anchor from its primary citation, with an ordinal for collisions.

    Stable under both of the things that move a line: rewording by the narrative pass,
    and reordering by `select()`. `used` carries the counts across one generation pass;
    the caller owns it, so this stays pure.

    **Two namespaces, and both halves of that are load-bearing.** Ordinals are counted
    per layer, so a ledger line citing the same commit cannot push a narrative line from
    `a598221` to `a598221#2` — an anchor that moves when the ledger changes is the
    positional bug in a different costume. But per-layer counters alone let the two layers
    mint the *same* anchor for the same commit, and then one annotation attaches to two
    lines: this prototype had exactly that, ten collisions on one day, latent until
    `select()` started pinning annotated lines and each pinned line appeared twice. So the
    ledger gets a prefix and prose gets the bare citation, which is also the right way
    round — the bare form is the one that appears in `notebook/README.md` and the one
    Noah types.

    An uncited line gets a positional placeholder, which is harmless because
    `admissible()` drops it before it can be rendered or annotated."""
    ns = LEDGER_NS if spine else ""
    if not cites:
        n = used["uncited"] = used.get("uncited", 0) + 1
        return f"{ns}uncited#{n}"
    base = ns + cites[0].ref
    n = used[base] = used.get(base, 0) + 1
    return base if n == 1 else f"{base}#{n}"


@dataclass(frozen=True)
class Note:
    """One generated line. `tier` is the Provenance Tier of the *line*, not of the
    work it describes. Only two tiers can appear: **T3** for everything generated — both
    harvested facts and narrative claims, because verifiable is not verified and nobody
    has read them — and **T1** for Noah's annotations. Badging a harvested line T2 was
    the first draft's mistake, corrected in review against `curriculum/README.md`, which
    rejects exactly that reading. Harvested versus narrative is a real distinction and it
    rides `spine`, not the tier ladder."""

    id: str
    """The line's **anchor**: its primary citation plus an ordinal when one artifact
    yields several lines — `a598221`, `a598221#2`, `#40`. Never positional. An index
    survives neither `select()`'s reordering nor a regeneration that adds an earlier
    commit, and the failure is silent: the index still resolves, so an annotation is
    re-attached to a different claim rather than orphaned. See `anchor()`."""

    kind: Kind
    text: str
    cites: tuple[Cite, ...] = ()
    tier: str = "T3"
    debt: str = ""  # issue ref, when the line rests on undischarged Verification Debt
    spine: bool = False
    """True for a line mechanically restated from the history — a commit subject, an
    issue title. **These never become prose.** `git log` already carries them, and the
    first render of this prototype showed them crowding the narrative lines out of the
    budget: 14 commit restatements above the two sentences worth reading. So the entry
    is prose for *why*, and a collapsed ledger for *what*."""

    def badge(self) -> str:
        return f"⟦{self.tier} · {self.debt}⟧" if self.debt else f"⟦{self.tier}⟧"


@dataclass(frozen=True)
class Session:
    """A Transcript Archive session, cited by content hash (#3 §2) because the archive
    is private and has no public URL to link. The manifest resolves hash → Drive path.

    A session is **a segment of a transcript file**, not the file: it ends after an
    hour without work, and it belongs to the local day it ended on. So the citation is
    hash *plus* window — the hash identifies the file, the window says which part of it
    this day owns. `segment` states that plainly on the page rather than leaving a
    reader to assume the hash covers only what they are reading."""

    sha256: str
    started: str
    ended: str
    events: int
    prompts: int
    branch: str
    skill: str = ""
    segment: str = ""  # e.g. "1 of 4" — which segments of the file this day owns

    @property
    def short(self) -> str:
        return self.sha256[:12]


@dataclass(frozen=True)
class Trigger:
    """Why an entry exists at all. Sessions are *cited*, never a trigger — see README."""

    kind: str  # merge | task | milestone
    ref: str
    label: str


@dataclass(frozen=True)
class Annotation:
    """Noah's layer. Keyed to a line's **anchor**, or `@lede` for the entry as a whole,
    and never an
    edit to generated text — the separation is what makes the rendering distinction real.

    **Not canonical.** An annotation is commentary for the record; anything Noah wants
    to be canon earns its own work, which is a tier promotion for the idea rather than a
    louder note. What follows from that is `reanchor()`: regeneration is allowed to
    happen, and annotations are re-applied by anchor rather than treated as untouchable."""

    anchor: str
    text: str


def reanchor(annotations: list[Annotation], notes: tuple[Note, ...]
             ) -> tuple[list[Annotation], list[Annotation]]:
    """Re-apply an annotation layer to a regenerated entry. Returns (applied, orphaned).

    Annotations are not canonical, so a regenerated entry does not have to preserve
    them — but it must not lose them *silently*. An orphan is a note the regeneration
    no longer produces, and the honest thing is to report it rather than drop it.

    **Membership is tested against the annotatable layer, not against every note.** Two
    ways this set was wrong, both of which made an orphan report as applied:

    - *Namespace* — spine and prose count ordinals separately, so both layers could mint
      `2611689`. Unioning them meant membership stopped saying *the annotated line still
      exists* and started saying *some line citing that commit still exists*. The
      `ledger:` prefix on spine anchors closes it; testing `not n.spine` closes it
      explicitly, rather than leaving the guarantee resting on a naming convention.
    - *Admissibility* — an uncited line still gets a placeholder anchor, and `anchor()`
      calls that harmless because `admissible()` drops the line before anything can
      render it. True of rendering, and it was not true here: an annotation on a dropped
      line reported applied while appearing on no page at all."""
    ids = {n.id for n in notes if not n.spine and admissible(n)} | {"@lede"}
    applied = [a for a in annotations if a.anchor in ids]
    return applied, [a for a in annotations if a.anchor not in ids]


@dataclass
class Entry:
    date: str
    slug: str
    title: str
    triggers: tuple[Trigger, ...] = ()
    notes: tuple[Note, ...] = ()
    sessions: tuple[Session, ...] = ()
    annotations: list[Annotation] = field(default_factory=list)

    @property
    def path(self) -> str:
        return f"notebook/{self.date}-{self.slug}.md"

    def annotated(self, anchor: str) -> list[Annotation]:
        return [a for a in self.annotations if a.anchor == anchor]


# ------------------------------------------------------------ selection rules

def admissible(note: Note) -> bool:
    """The volume rule with teeth: a generated line that cannot name an artifact is
    not a record of anything. Activity lines usually can cite, which is why the
    citation rule alone is not enough and the `Volume` dial exists as well."""
    return bool(note.cites)


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))


@dataclass
class Selection:
    kept: list[Note]              # prose: why it happened, what was taken back
    ledger: list[Note]            # collapsed table: the mechanical spine, plus prose overflow
    dropped_uncited: list[Note]
    dropped_volume: list[Note]
    budget_words: int
    pinned: list[Note] = field(default_factory=list)
    """Lines held in prose because Noah annotated them. See `select()` rule 0."""
    orphans: list[Annotation] = field(default_factory=list)
    """Annotations whose anchor names no line in this entry. Rendered as orphans rather
    than dropped — the whole point of anchoring by citation is that this case is visible."""

    @property
    def spent(self) -> int:
        return sum(words(n.text) for n in self.kept)


ORDER = {Kind.REVERSED: 0, Kind.DEADEND: 1, Kind.LANDED: 2, Kind.MILESTONE: 3,
         Kind.DEBT: 4, Kind.ACTIVITY: 5}


def select(entry: Entry, volume: Volume, budget: int = BUDGET_WORDS) -> Selection:
    """Decide what an entry actually shows. Five rules, applied in this order:

    0. **An annotated line is pinned** — it cannot be demoted by the dial or the budget.
    1. **No citation, no line** — a claim with no artifact is not a record of anything.
    2. **Volume class** — the dial says which kinds of line are in play at all.
    3. **Spine to the ledger** — mechanically restated history never competes for prose
       budget with a line about *why*.
    4. **Budget** — what is left is ordered reversals and dead ends first, then what
       landed, and the tail past the budget collapses into the same ledger.

    Rule 4's ordering is deliberate: a programme that spends its readable budget on
    wins and pushes its reversals into a fold is the one nobody should trust.

    **Rule 0 exists because of a bug this prototype had.** Without it, turning the budget
    down to 160 words moved an annotated line into the collapsed ledger, and
    `render_annotation_first` — which reads annotations off `kept` — stopped rendering
    Noah's note at all. Nothing reported it. That is the budget truncating *him*, which
    `notebook/README.md` says it must never do, and it is the same silent-suppression
    family as the positional-anchor bug: the words were not lost, they were just no longer
    on the page. An annotation is evidence he engaged with the line, so the line stays."""
    annotated = {a.anchor for a in entry.annotations}
    dropped_uncited = [n for n in entry.notes if not admissible(n)]
    live = [n for n in entry.notes if admissible(n)]
    dropped_volume = [n for n in live if n.kind not in KINDS_AT[volume] and n.id not in annotated]
    live = [n for n in live if n.kind in KINDS_AT[volume] or n.id in annotated]

    ledger = sorted((n for n in live if n.spine and n.id not in annotated),
                    key=lambda n: ORDER[n.kind])
    prose = sorted((n for n in live if not n.spine or n.id in annotated),
                   key=lambda n: ORDER[n.kind])
    pinned = [n for n in prose if n.id in annotated]
    orphans = [a for a in entry.annotations
               if a.anchor != "@lede" and a.anchor not in {n.id for n in entry.notes}]

    kept: list[Note] = []
    spent = 0
    for n in prose:
        w = words(n.text)
        if n.id in annotated:          # rule 0: pinned, and it still spends budget so the
            kept.append(n)             # count on screen stays honest about the page's length
            spent += w
        elif spent + w > budget and kept:
            ledger.append(n)
        else:
            kept.append(n)
            spent += w
    return Selection(kept, ledger, dropped_uncited, dropped_volume, budget, pinned, orphans)


def should_emit(entry: Entry, sel: Selection) -> tuple[bool, str]:
    """The other half of volume control: most days do not deserve an entry. A day whose
    only content is churn produces nothing — silence is the default, not the exception."""
    if not sel.kept:
        return False, "nothing citable survived selection"
    if all(n.kind is Kind.ACTIVITY for n in sel.kept):
        return False, "activity only — no decision, no reversal, no milestone"
    return True, ""


# --------------------------------------------------------------- rendering

HEADER = (
    "<!-- GENERATED from the Transcript Archive and this repository's history.\n"
    "     Generated lines are plain; every {marker} block is Noah's, written by hand. -->"
)
"""Kept for A and C **only**, and deliberately: those two are preserved exactly as they
were driven, and the banner is part of what was compared. The chosen rendering does not
emit it — a page whose thesis is that the top level is Noah's cannot open with a machine's
front matter, which `notebook/README.md` now states as a decision.

The banner also no longer names a regeneration command. It named `tools/notebook_entry.py`,
which does not exist and never will: the generator is unbuilt and destined for Apps Script,
so a committed artifact telling a reader to run it was a broken promise in a record whose
value is that its references resolve."""


def _cites(note: Note) -> str:
    return " · ".join(c.md() for c in note.cites)


def _sessions_block(entry: Entry) -> str:
    """Citation by content hash, because the archive is private (#3 §2). The hash is
    verifiable by anyone holding the transcript and resolvable by Noah through the
    `Index` manifest; it does not leak the archive's shape."""
    rows = "\n".join(
        f"| `sha256:{s.short}…` | {s.started[:16]} → {s.ended[:16]} | {s.segment} | "
        f"{s.prompts} prompts / {s.events} events | `{s.branch}` |"
        for s in entry.sessions
    )
    # No scrub count on the page, deliberately: an entry whose transcript held a
    # candidate secret is never emitted at all (`harvest.ScrubBlocked`), so a count here
    # could only ever read zero — and a number that can only read zero is decoration
    # impersonating a control.
    return (
        "## Sessions\n\n"
        "Cited by content hash; the Transcript Archive is private and the `Index` "
        "manifest resolves hash → path. A session ends after an hour without work and "
        "belongs to the day it ended, so the window selects which part of the file this "
        "entry covers.\n\n"
        "| session | window | segment | size | branch |\n|---|---|---|---|---|\n" + rows
    )


def _legend(entry: Entry, sel: Selection) -> str:
    used = sorted({n.tier for n in sel.kept} | {"T1"} if entry.annotations else {n.tier for n in sel.kept})
    lines = [f"`⟦{t}⟧` {TIERS[t]}" for t in used if t in TIERS]
    debts = sorted({n.debt for n in sel.kept if n.debt})
    if debts:
        lines.append("debt: " + " ".join(f"`{d}`" for d in debts))
    return "<sub>" + " · ".join(lines) + "</sub>"


def _orphans(sel: Selection) -> str:
    """Annotations whose line the regeneration no longer produces. On the page, not in a
    log: `notebook/README.md` says orphans are reported rather than dropped, and a report
    Noah has to go looking for is a drop with extra steps."""
    if not sel.orphans:
        return ""
    return "\n\n".join(
        f"> **Orphaned** — {a.text} <sub>anchored to `{a.anchor}`, which this entry no "
        f"longer carries</sub>"
        for a in sel.orphans
    )


def _ledger(sel: Selection) -> str:
    """The mechanical spine, and whatever prose ran past the budget. Collapsed, because
    a reader who wants this can also read `git log` — but auditable, because it is here."""
    if not sel.ledger:
        return ""
    rows = "\n".join(f"| {n.kind.value} | {n.text} | {_cites(n)} |" for n in sel.ledger)
    return (
        f"<details>\n<summary>Ledger — {len(sel.ledger)} line(s) the history already "
        f"carries</summary>\n\n"
        "| | | |\n|---|---|---|\n" + rows + "\n\n</details>"
    )


def _triggers(entry: Entry) -> str:
    return "<sub>generated by " + ", ".join(f"{t.kind} {t.label}" for t in entry.triggers) + "</sub>"


def render_inline(entry: Entry, sel: Selection) -> str:
    """A — generated prose, annotations as blockquotes under the line they answer."""
    out = [HEADER.format(marker="> **Noah —**"), "",
           f"# {entry.date} — {entry.title}", "", _triggers(entry), ""]
    for a in entry.annotated("@lede"):
        out += [f"> **Noah —** {a.text}", ""]
    for n in sel.kept:
        out.append(f"- {n.text} {_cites(n)} `{n.badge()}`")
        for a in entry.annotated(n.id):
            out += ["", f"  > **Noah —** {a.text}", ""]
    out += ["", _ledger(sel), "", _sessions_block(entry), "", _legend(entry, sel)]
    return "\n".join(x for x in out if x is not None).replace("\n\n\n", "\n\n")


def render_annotation_first(entry: Entry, sel: Selection) -> str:
    """B — Noah's reading is the entry; the generated spine collapses beneath it.
    Aimed straight at the machine-exhaust failure: the human layer is what a reader
    meets first, and the generated record is one click away and skippable."""
    out = [f"# {entry.date} — {entry.title}", ""]
    lede = entry.annotated("@lede")
    if lede:
        out += [a.text for a in lede] + [""]
    else:
        out += ["*Unannotated.* The generated record is below; nothing here has been read back.", ""]
    keyed = [(n, entry.annotated(n.id)) for n in sel.kept]
    for n, anns in keyed:
        for a in anns:
            out += [f"{a.text} <sub>on {_cites(n)}</sub>", ""]
    out += [_orphans(sel), ""]
    out += ["<details>\n<summary>Generated record — "
            f"{len(sel.kept)} line(s), {sel.spent} words</summary>\n"]
    for n in sel.kept:
        out.append(f"- {n.text} {_cites(n)} `{n.badge()}`")
    out += ["", "</details>", "", _ledger(sel), "", _sessions_block(entry), "",
            _legend(entry, sel)]
    return "\n".join(out).replace("\n\n\n", "\n\n")


def render_ledger(entry: Entry, sel: Selection) -> str:
    """C — a table of what landed, annotations in their own section. Densest, and the
    one that reads most like a changelog, which `CONTEXT.md` explicitly avoids."""
    out = [HEADER.format(marker="## Noah's notes"), "",
           f"# {entry.date} — {entry.title}", "", _triggers(entry), "",
           "| | what | where | tier |", "|---|---|---|---|"]
    for n in sel.kept:
        mark = "◆" if entry.annotated(n.id) else ""
        out.append(f"| {mark}{n.kind.value} | {n.text} | {_cites(n)} | `{n.badge()}` |")
    out += ["", _ledger(sel), ""]
    anns = entry.annotations
    if anns:
        out += ["## Noah's notes", ""]
        by_id = {n.id: n for n in sel.kept}
        for a in anns:
            where = f" — on *{by_id[a.anchor].text[:48]}…*" if a.anchor in by_id else ""
            out += [f"- {a.text}{where}", ""]
    out += [_sessions_block(entry), "", _legend(entry, sel)]
    return "\n".join(out).replace("\n\n\n", "\n\n")


def render_raw(entry: Entry, sel: Selection) -> str:
    """D — control. Generated only, no annotation layer, no budget applied. This is
    what the notebook becomes if nobody annotates it; it exists to be compared against."""
    out = [f"# {entry.date} — {entry.title}", ""]
    for n in sorted(entry.notes, key=lambda n: n.kind.value):
        out.append(f"- [{n.kind.value}] {n.text} {_cites(n)}")
    out += ["", _sessions_block(entry)]
    return "\n".join(out)


VARIANTS = {
    "A inline blockquote": render_inline,
    "B annotation-first": render_annotation_first,
    "C ledger table": render_ledger,
    "D raw generated (control)": render_raw,
}

CHOSEN = "B annotation-first"
"""The format, settled 2026-07-30. The others are kept because the comparison is the
evidence for the choice, not because any of them is still a candidate."""


# ------------------------------------------------------------------- metrics

@dataclass
class Metrics:
    total_words: int
    generated_words: int
    annotated_words: int
    lines: int
    shown: int
    ledgered: int
    dropped: int
    annotated_notes: int
    seconds: int

    @property
    def human_share(self) -> float:
        return self.annotated_words / self.total_words if self.total_words else 0.0


def prose_only(rendered: str) -> str:
    """What a reader's eye actually crosses. Link targets, HTML and the generation
    header are not read, and counting them made the first draft of these numbers
    flatter the entry by roughly a third."""
    text = re.sub(r"<!--.*?-->", "", rendered, flags=re.S)
    text = re.sub(r"\((?:https?|mailto):[^)]*\)", "", text)
    text = re.sub(r"</?[a-z]+[^>]*>", "", text)
    return text


def measure(entry: Entry, sel: Selection, rendered: str) -> Metrics:
    ann_words = sum(words(a.text) for a in entry.annotations)
    gen = sum(words(n.text) for n in sel.kept + sel.ledger)
    total = words(prose_only(rendered))
    return Metrics(
        total_words=total,
        generated_words=gen,
        annotated_words=ann_words,
        lines=len(rendered.splitlines()),
        shown=len(sel.kept),
        ledgered=len(sel.ledger),
        dropped=len(sel.dropped_uncited) + len(sel.dropped_volume),
        annotated_notes=len({a.anchor for a in entry.annotations} & {n.id for n in sel.kept}),
        seconds=round(total / 250 * 60),  # 250 wpm
    )
