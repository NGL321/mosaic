"""PROTOTYPE — the generator: factored source in, one flat entry out (premise 10).

The whole claim under test is in `flatten()`. Nothing a reader of the rendered entry
sees is a reference to somewhere else: fragments are spliced with their parameters
substituted, the actor column is resolved to the reader's own row, and couplings are
stated at the step that carries them. If an entry ever says "see PROTOCOL.md §4", the
generator has failed premise 16 and the acceptance test will find it.

    python docs/prototypes/operation-format/render.py          # write out/
    python docs/prototypes/operation-format/render.py --gaps   # the executor:none report
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

GLOSSARY: dict = {}

HERE = Path(__file__).parent
SRC = HERE / "source"
OUT = HERE / "out"

EXECUTOR_GLOSS = {
    "noah": "**Noah**, by hand",
    "agent": "**an agent**",
    "none": "**NOBODY — filed gap**",
}


def load(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def load_all() -> tuple[dict, dict, dict, dict]:
    classes = load(SRC / "classes.yaml")
    intents = load(SRC / "intents.yaml")
    globals()["GLOSSARY"] = load(SRC / "glossary.yaml")
    fragments = {f.stem: load(f) for f in (SRC / "fragments").glob("*.yaml")}
    cells = {f.stem: load(f) for f in (SRC / "operations").glob("*.yaml")}
    return classes, intents, fragments, cells


def subst(text: str, params: dict) -> str:
    for k, v in params.items():
        text = text.replace("{" + k + "}", str(v))
    return text


def flatten(cell: dict, fragments: dict) -> list[dict]:
    """Splice fragment steps and cell steps into ONE ordered list.

    This is the point of use. After this function runs there is no such thing as
    a spine and a payload — there is a numbered list of steps, each with an
    executor, and an agent can start at 1.
    """
    proc = cell.get("procedure") or {}
    order: list[dict] = []
    for use in proc.get("uses", []):
        frag = fragments[use["fragment"]]
        params = use.get("with", {})
        for step in frag["steps"]:
            s = dict(step)
            s["do"] = subst(s["do"], params)
            s["from_fragment"] = frag["id"]
            if not s.get("authority"):
                s["authority"] = frag.get("authority")
            order.append(s)

    deferred = []
    for step in proc.get("steps", []):
        if step.get("after"):
            deferred.append(dict(step))
        else:
            order.append(dict(step))

    for step in deferred:
        target = step["after"]
        idx = next((i for i, s in enumerate(order) if s["id"] == target), None)
        if idx is None:
            order.append(step)   # target not in this render; degrade to the end
            continue
        # land after the target and after anything already inserted behind it
        j = idx + 1
        while j < len(order) and order[j].get("after") == target:
            j += 1
        order.insert(j, step)
    return order


def actor_rows(cell: dict) -> list[tuple[str, str, str]]:
    rows = []
    for actor, val in (cell["operation"].get("actors") or {}).items():
        if isinstance(val, str):
            rows.append((actor, val, ""))
        else:
            note = val.get("reason") or val.get("qualified_by") or ""
            if val.get("redirect"):
                note = (note + " **You want `" + val["redirect"] + "`.**").strip()
            rows.append((actor, val["ruling"], note))
    return rows


def render(name: str, cell: dict, classes: dict, intents: dict, fragments: dict) -> str:
    key = cell["key"]
    klass = classes[key["class"]]
    L: list[str] = []
    A = L.append

    A("# `" + name + "`")
    A("")
    A("> " + intents[key["intent"]]["gloss"].strip() + " — applied to *" + klass["gloss"] + "*.")
    A("")
    A("| | |")
    A("|---|---|")
    A("| **Where** | " + klass["locate"] + " (" + klass["surface"] + ") |")
    A("| **Track** | " + klass["track"] + " |")
    A("| **Custody** | " + klass["custody"] + " |")
    A("| **Origin** | " + klass["origin"] + " |")
    A("| **Defence** | " + klass["defence"] + " |")
    A("")

    if cell.get("null_ruling"):
        n = cell["null_ruling"]
        A("## RULED OUT — this Operation does not exist")
        A("")
        A(n["reason"].strip())
        A("")
        A("**Do this instead: `" + n["redirect"] + "`.**")
        A("")
        A("Ruled by: " + n["ruled_by"] + "  ")
        A("Already stated at: " + n["header_says_so"])
        A("")
        A("*This is a null, not an absence. Nobody has to wonder whether it was considered.*")
        return "\n".join(L) + "\n"

    op = cell["operation"]
    A("## When this is done, all of the following are true")
    A("")
    for pc in op["postconditions"]:
        auth = "  <br>*" + pc["authority"] + "*" if pc.get("authority") else ""
        A("- **" + pc["id"] + "** — " + pc["text"].strip() + auth)
    A("")
    A("**Whose decision:** " + str(op.get("decided_by")))
    A("")
    if op.get("inputs"):
        A("## What you must be given before you start")
        A("")
        for item in op["inputs"]:
            for k, v in item.items():
                A("- **`" + k + "`** — " + v)
        A("")
        A("*If you were not given one of these, you are not equipped to run this Operation. Ask; do not invent.*")
        A("")
    if op.get("terms"):
        A("## Terms used here")
        A("")
        for term in op["terms"]:
            entry = GLOSSARY.get(term)
            if not entry:
                continue
            A("- **" + term + "** — " + " ".join(entry["gloss"].split()) + " <sub>" + entry["authority"] + "</sub>")
        A("")
    A("## May you do this?")
    A("")
    A("| Actor | | |")
    A("|---|---|---|")
    for actor, ruling, note in actor_rows(cell):
        A("| " + actor + " | **" + ruling + "** | " + " ".join(note.split()) + " |")
    A("")

    steps = flatten(cell, fragments)
    A("## How it is met today")
    A("")
    for i, s in enumerate(steps, 1):
        ex = EXECUTOR_GLOSS.get(s["executor"], "**`" + s["executor"] + "`**")
        A("### " + str(i) + ". " + s["id"] + " — " + ex)
        A("")
        A(s["do"].strip())
        A("")
        if s.get("exit_codes"):
            for code, meaning in s["exit_codes"].items():
                line = "- exit `" + str(code) + "` — " + meaning
                route = (s.get("on_failure") or {}).get(code)
                if route:
                    line += " → **" + route + "**"
                A(line)
            A("")
        if s.get("coupling"):
            A("> **Also required: `" + s["coupling"] + "`.**")
            A("")
        if s["executor"] == "none":
            A("> **GAP.** " + " ".join(s.get("gap", "unassigned").split()))
            A("")
        if s.get("note"):
            A("*" + " ".join(s["note"].split()) + "*")
            A("")
        if s.get("authority"):
            A("<sub>" + s["authority"] + "</sub>")
            A("")

    trig = (cell.get("procedure") or {}).get("trigger")
    if trig:
        A("## What fires this")
        A("")
        A(trig["do"].strip() + " — executor: " + EXECUTOR_GLOSS.get(trig["executor"], trig["executor"]))
        A("")
        if trig["executor"] == "none":
            A("> **GAP.** " + " ".join(trig.get("gap", "").split()))
            A("")

    if cell.get("couplings"):
        A("## Couplings")
        A("")
        for c in cell["couplings"]:
            other = c.get("to") or c.get("from")
            A("- **`" + str(other) + "`** — " + " ".join(c["text"].split()))
        A("")
    return "\n".join(L) + "\n"


def gaps(cells: dict, fragments: dict) -> list[tuple[str, str, str]]:
    found = []
    for name, cell in sorted(cells.items()):
        if cell.get("null_ruling"):
            continue
        for s in flatten(cell, fragments):
            if s["executor"] == "none":
                found.append((name, s["id"], " ".join(s.get("gap", "").split())))
        trig = (cell.get("procedure") or {}).get("trigger")
        if trig and trig["executor"] == "none":
            found.append((name, "trigger", " ".join(trig.get("gap", "").split())))
    return found


def main() -> int:
    classes, intents, fragments, cells = load_all()
    if "--gaps" in sys.argv:
        rows = gaps(cells, fragments)
        print(str(len(rows)) + " steps have executor `none` — filed by construction (premise 9)\n")
        for cell, step, why in rows:
            print("  " + cell.ljust(30) + step.ljust(22) + why)
        return 0
    OUT.mkdir(exist_ok=True)
    for name, cell in sorted(cells.items()):
        text = render(name, cell, classes, intents, fragments)
        (OUT / (name + ".md")).write_text(text, encoding="utf-8")
        print("wrote out/" + name + ".md  (" + str(len(text.splitlines())) + " lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
