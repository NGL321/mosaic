"""PROTOTYPE — drive the Operation source format over three real Operations.

    python docs/prototypes/operation-format/prototype_tui.py

Nothing here touches git, GitHub or the network. Every case reads the factored source
under `source/` and prints what an actor would actually be handed.

CASE `c` IS THE HARD CELL — authored, custody-split, research track, owes a defence.
It is the one that decides whether `intent x class` survives contact.

CASE `t` IS THE ONE THAT BREAKS SOMETHING. The tracker surface drops PROTOCOL §4's
entire spine and nothing replaces it: five of the seven filed gaps are on this one cell.

CASE `n` IS THE EXPLICIT NULL. `add` on a generated file is ruled out, with a reason and
a redirect — not left absent. Compare it against a cell that simply has no file.

CASE `f` IS PREMISE 10, SHOWN RATHER THAN ARGUED: the same Operation as source and as
the thing handed to an actor, side by side.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

import render  # noqa: E402

HERE = Path(__file__).parent
CLASSES, INTENTS, FRAGMENTS, CELLS = render.load_all()


def rule(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78 + "\n")


def show(name: str) -> None:
    rule("RENDERED — what the actor is handed: " + name)
    print(render.render(name, CELLS[name], CLASSES, INTENTS, FRAGMENTS))


def case_c() -> None:
    show("add@CONTEXT-entry")
    print("-" * 78)
    print("WATCH: seventeen steps, five executors, and not one 'see PROTOCOL.md §4'.")
    print("The branch spine and the merge spine were written once, in source/fragments/,")
    print("and spliced with this cell's parameters already substituted.")


def case_g() -> None:
    show("regenerate@curriculum-open")
    print("-" * 78)
    print("WATCH: `decided_by: none`. There is nothing to decide, so nobody may decide it,")
    print("and the actor table has no may-not row for agents. The generated flag did that.")
    print("WATCH ALSO: the trigger has executor `none`. The tool has a --check mode written")
    print("FOR CI and no CI calls it.")


def case_t() -> None:
    show("file@debt-issue")
    print("-" * 78)
    print("WATCH: no branch, no pull request, no review, no custody check. The tracker")
    print("surface inherits none of PROTOCOL §4-6 and PROTOCOL has no §for it. Five gaps.")


def case_n() -> None:
    show("add@curriculum-open")
    print("-" * 78)
    print("A null is a FILE, exactly like a ruled-in cell. Absent means nobody looked.")
    print("Try `x` for the difference.")


def case_x() -> None:
    rule("ABSENT vs NULL — `edit@CONTEXT-entry` has no file")
    print("There is no source/operations/edit@CONTEXT-entry.yaml.")
    print()
    print("That is not a ruling. Nobody has said whether editing an existing entry is the")
    print("same Operation as adding one, a different one, or impossible. The catch-all")
    print("(#230) must be able to tell this state from the null in case `n`, because they")
    print("route differently: a null REFUSES with a redirect, an absence is a MINT.")
    print()
    print("Ruled cells:")
    for name in sorted(CELLS):
        mark = "NULL" if CELLS[name].get("null_ruling") else "in  "
        print("   " + mark + "   " + name)
    print()
    print("Everything else in intent x class is ABSENT — nobody has looked yet.")
    n = len(INTENTS) * len(CLASSES)
    print("   " + str(len(CELLS)) + " ruled of " + str(n) + " pairs in this prototype's tiny axes.")


def case_f() -> None:
    name = "regenerate@curriculum-open"
    rule("SOURCE — factored (source/operations/" + name + ".yaml)")
    print((render.SRC / "operations" / (name + ".yaml")).read_text(encoding="utf-8"))
    rule("plus source/fragments/branch-spine.yaml and pull-request-spine.yaml")
    print("...which this cell names in four lines of `uses:` and never restates.")
    show(name)
    print("-" * 78)
    print("Premise 10. The left-hand form is what you maintain; the right-hand form is what")
    print("you act from; and no human ever holds both at once.")


def case_G() -> None:
    rule("GAPS — every step whose executor is `none` (premise 9)")
    rows = render.gaps(CELLS, FRAGMENTS)
    for cell, step, why in rows:
        print("  " + cell)
        print("    " + step + ": " + why)
        print()
    print(str(len(rows)) + " gaps, from THREE Operations. The first pass was always going to")
    print("file a lot; the point is that they were filed by writing the format, not found.")


def case_k() -> None:
    rule("WHERE THE KEY STRAINED — carried to #228")
    print("1. `debt:verification` vs `debt:source` split the ACTOR COLUMN inside one cell.")
    print("   An agent may file a source debt on its own authority; a verification debt is")
    print("   a claim about what Noah cannot yet defend. Same intent, same location, same")
    print("   three flags — different actor ruling. So either they are two artifact CLASSES")
    print("   (and class is finer than the label, not the path), or the actor column needs")
    print("   a condition and stops being a column.")
    print()
    print("2. `custody` and `origin` both wanted the word 'authored' (see classes.yaml).")
    print("   All three live combinations exist in this repository. One flag cannot carry it.")
    print()
    print("3. `record/` is a branch prefix six branches use and PROTOCOL §4 has no row for.")
    print("   Found by trying to substitute {prefix} and finding no cell — the fog patch")
    print("   the map already carries, reached mechanically.")


CASES = {
    "c": ("the hard cell — add@CONTEXT-entry", case_c),
    "g": ("the generated cell — regenerate@curriculum-open", case_g),
    "t": ("the tracker cell — file@debt-issue", case_t),
    "n": ("the explicit null — add@curriculum-open", case_n),
    "x": ("absent vs null", case_x),
    "f": ("factored source beside its flat render", case_f),
    "G": ("the gap report", case_G),
    "k": ("where the key strained", case_k),
}


def main() -> int:
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg in CASES:
                CASES[arg][1]()
        return 0
    while True:
        print()
        for k, (desc, _) in CASES.items():
            print("  " + k + "  " + desc)
        print("  q  quit")
        try:
            choice = input("\n> ").strip()
        except EOFError:
            return 0
        if choice == "q":
            return 0
        if choice in CASES:
            CASES[choice][1]()
        else:
            print("no such case")


if __name__ == "__main__":
    raise SystemExit(main())
