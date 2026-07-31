"""
PROTOTYPE (ticket #11) — asserts over the three functions `entry.py` calls load-bearing.

Run:  python docs/prototypes/notebook-entry/checks.py

**A prototype should not have tests, and this one does.** The rule is right for a
throwaway; this directory stopped being one when it landed in-tree as the primary source
for the format, and `entry.py`'s model is the spec the Apps Script generator will be
written against. Four defects were found on this branch by driving the TUI by hand —
positional anchors, cross-layer collisions, the budget suppressing annotations, and
`select()` disagreeing with `reanchor()` — and every one of them is an assert below.
They are here so that the next person to touch the model finds out in a second, rather
than by reading a rendering carefully enough to notice Noah's words are missing.

Pure model only: no git, no `gh`, no transcript. The fixtures are hand-built `Note`s.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from entry import (  # noqa: E402
    Annotation,
    Cite,
    Entry,
    Kind,
    Note,
    Volume,
    anchor,
    annotatable,
    reanchor,
    select,
    should_emit,
)

PASSED = 0


def check(label: str, got, want) -> None:
    global PASSED
    if got != want:
        print(f"\x1b[31mFAIL\x1b[0m {label}\n  got  {got!r}\n  want {want!r}")
        sys.exit(1)
    PASSED += 1
    print(f"\x1b[32mok\x1b[0m   {label}")


def note(id_: str, text: str = "line", kind: Kind = Kind.LANDED, **kw) -> Note:
    cites = kw.pop("cites", (Cite("commit", id_.replace("ledger:", "")),))
    return Note(id_, kind, text, cites, **kw)


def entry(notes, annotations=()) -> Entry:
    return Entry("2026-07-29", "s", "t", notes=tuple(notes), annotations=list(annotations))


# ----------------------------------------------------------------- anchor()

used: dict[str, int] = {}
c = (Cite("commit", "a598221"),)
check("anchor: first use is the bare citation", anchor(c, used), "a598221")
check("anchor: second use takes an ordinal", anchor(c, used), "a598221#2")
check("anchor: ledger is a separate namespace",
      anchor(c, {}, spine=True), "ledger:a598221")
check("anchor: ledger ordinals do not shift prose ordinals",
      anchor((Cite("commit", "x"),), {}), "x")
check("anchor: uncited lines get a placeholder", anchor((), {}), "uncited#1")

# The collision that made one annotation answer two lines.
prose_used: dict[str, int] = {}
spine_used: dict[str, int] = {}
check("anchor: layers cannot mint the same anchor for one commit",
      anchor(c, prose_used) != anchor(c, spine_used, spine=True), True)


# ------------------------------------------------------- annotatable() set

mixed = [note("abc"), note("ledger:def", spine=True), note("uncited#1", cites=())]
check("annotatable: prose only, admissible only",
      annotatable(tuple(mixed)), {"abc"})


# ----------------------------------------------------- select() / reanchor()

e = entry(mixed, [Annotation("abc", "on prose"), Annotation("ledger:def", "on ledger"),
                  Annotation("uncited#1", "on dropped"), Annotation("nope", "on nothing")])
sel = select(e, Volume.FULL)
applied, orphaned = reanchor(e.annotations, e.notes)

check("select: an annotated ledger line is not promoted into prose",
      [n.id for n in sel.kept], ["abc"])
check("select and reanchor agree on orphans",
      {a.anchor for a in sel.orphans}, {a.anchor for a in orphaned})
check("orphans: everything unattachable is reported",
      sorted(a.anchor for a in sel.orphans), ["ledger:def", "nope", "uncited#1"])
check("reanchor: only the live prose anchor applies",
      [a.anchor for a in applied], ["abc"])

# Rule 0 — the budget must not reach Noah's layer.
long_ = [note("keep", "w " * 60, Kind.LANDED), note("pinned", "w " * 60, Kind.LANDED),
         note("spill", "w " * 60, Kind.LANDED)]
pinned_entry = entry(long_, [Annotation("pinned", "Noah")])
tight = select(pinned_entry, Volume.FULL, budget=70)
check("rule 0: an annotated line survives a budget that spills its neighbours",
      "pinned" in {n.id for n in tight.kept}, True)
check("rule 0: unannotated overflow still spills to the ledger",
      "spill" in {n.id for n in tight.ledger}, True)

# Rule 0 against the volume dial, not just the budget.
dead = entry([note("dead", "abandoned", Kind.DEADEND)], [Annotation("dead", "Noah")])
check("rule 0: the dial cannot drop an annotated line either",
      [n.id for n in select(dead, Volume.DECISIONS).kept], ["dead"])

# Reordering must not move an anchor — the positional-id bug.
before = entry([note("first", "a", Kind.LANDED), note("second", "b", Kind.REVERSED)])
check("select: reversals order ahead of what landed",
      [n.id for n in select(before, Volume.FULL).kept], ["second", "first"])
check("anchors survive that reordering",
      {n.id for n in select(before, Volume.FULL).kept}, {"first", "second"})


# --------------------------------------------------------------- should_emit

check("should_emit: churn alone produces no entry",
      should_emit(*(lambda en: (en, select(en, Volume.EVERYTHING)))(
          entry([note("c", "churn", Kind.ACTIVITY)])))[0], False)
check("should_emit: a decision produces one",
      should_emit(*(lambda en: (en, select(en, Volume.FULL)))(
          entry([note("d", "decided", Kind.LANDED)])))[0], True)


# ------------------------------------------------------------- segmentation

from harvest import IDLE, segments  # noqa: E402
from datetime import datetime, timedelta, timezone  # noqa: E402

t0 = datetime(2026, 7, 29, 12, 0, tzinfo=timezone.utc)
check("segments: empty transcript has no segments", segments([]), [])
check("segments: a gap under the threshold does not split",
      len(segments([t0, t0 + IDLE - timedelta(seconds=1)])), 1)
check("segments: a gap over the threshold splits",
      len(segments([t0, t0 + IDLE + timedelta(seconds=1)])), 2)

print(f"\n{PASSED} checks passed")
