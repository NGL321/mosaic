"""
PROTOTYPE (ticket #11) — throwaway TUI shell over entry.py.

Run:  python docs/prototypes/notebook-entry/prototype_tui.py

One real entry, generated from one real session, rendered four ways. Switch the
rendering with [1]-[4], turn the volume dial with [d], add or drop the annotation
layer, and watch the word count and the human share move. [w] writes the current
rendering to out/ so it can be read as GitHub renders it — that is the only thing
this prototype puts on disk, and it is git-ignored nowhere: look at it, then delete it.

Everything except that write is in memory. The entry is never written to notebook/.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from entry import (  # noqa: E402
    VARIANTS,
    Annotation,
    Volume,
    measure,
    select,
    should_emit,
)
from harvest import load  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

B, D, R, Y, G, C, M = ("\x1b[1m", "\x1b[2m", "\x1b[0m", "\x1b[33m", "\x1b[32m",
                       "\x1b[36m", "\x1b[35m")
SESSION = "f0900d60-77d7-4a8b-ace4-6041f764656b"
OUT = Path(__file__).parent / "out"


def getkey() -> str:
    try:
        import msvcrt
        ch = msvcrt.getwch()
        return ch
    except ImportError:
        return (sys.stdin.readline() or "q").strip()[:1] or "\n"


def readline(prompt: str) -> str:
    print(prompt, end="", flush=True)
    return sys.stdin.readline().rstrip("\n")


class App:
    def __init__(self) -> None:
        self.entry = load(SESSION)
        self.samples = [
            Annotation(a["anchor"], a["text"])
            for a in json.loads(
                (Path(__file__).parent / f"pass-{SESSION[:8]}.json").read_text(encoding="utf-8")
            )["sample_annotations"]
        ]
        self.variant = 0
        self.volume = Volume.FULL
        self.budget = 320
        self.focus = 0
        self.scroll = 0

    # ------------------------------------------------------------------ state
    @property
    def sel(self):
        return select(self.entry, self.volume, self.budget)

    @property
    def variant_name(self) -> str:
        return list(VARIANTS)[self.variant]

    def rendered(self) -> str:
        return VARIANTS[self.variant_name](self.entry, self.sel)

    # ----------------------------------------------------------------- render
    def frame(self) -> None:
        cols, rows = shutil.get_terminal_size((100, 40))
        sel = self.sel
        text = self.rendered()
        m = measure(self.entry, sel, text)
        emit, why = should_emit(self.entry, sel)
        s = self.entry.sessions[0]

        print("\x1b[2J\x1b[H", end="")
        print(f"{B}PROTOTYPE #11 — one real entry, four renderings{R}"
              f"   {D}{self.entry.path}{R}")
        print(f"{D}session{R} sha256:{s.short}…  {D}{s.prompts} prompts / {s.events} events, "
              f"skill={s.skill or '—'}, scrubbed={s.scrubbed}{R}")
        print("─" * min(cols, 110))

        print(f"{B}rendering{R} {C}{self.variant_name}{R}"
              f"   {B}volume{R} {Y}{self.volume.value}{R}"
              f"   {B}budget{R} {self.budget}w"
              f"   {B}annotations{R} {G if self.entry.annotations else D}"
              f"{len(self.entry.annotations)}{R}")

        gate = f"{G}emit{R}" if emit else f"{Y}no entry — {why}{R}"
        print(f"{B}gate{R} {gate}"
              f"   {B}shown{R} {m.shown}  {B}ledger{R} {m.ledgered}"
              f"  {B}dropped{R} {m.dropped}"
              f" {D}({len(sel.dropped_uncited)} uncited, {len(sel.dropped_volume)} by volume){R}")
        print(f"{B}words{R} {m.total_words} {D}(generated {m.generated_words}, "
              f"Noah {m.annotated_words} = {m.human_share:.0%}){R}"
              f"   {B}read{R} ~{m.seconds}s"
              f"   {B}annotated lines{R} {m.annotated_notes}/{m.shown}")

        print("─" * min(cols, 110))
        lines = text.splitlines()
        window = max(rows - 16, 8)
        for line in lines[self.scroll:self.scroll + window]:
            print(self._paint(line[: cols - 1]))
        if len(lines) > self.scroll + window:
            print(f"{D}… {len(lines) - self.scroll - window} more lines — [j]/[k] to scroll{R}")

        print("─" * min(cols, 110))
        notes = sel.kept
        if notes:
            f = notes[self.focus % len(notes)]
            mark = "◆" if self.entry.annotated(f.id) else "·"
            print(f"{B}focus{R} {mark} {f.kind.value:9} {f.text[:cols - 30]}")
        print(f"{B}[1-4]{R}{D} rendering {R}{B}[d]{R}{D} volume {R}{B}[+/-]{R}{D} budget "
              f"{R}{B}[s]{R}{D} sample annotations {R}{B}[x]{R}{D} clear {R}{B}[n/p]{R}{D} focus "
              f"{R}{B}[a]{R}{D} annotate focus {R}{B}[j/k]{R}{D} scroll {R}{B}[w]{R}{D} write "
              f"{R}{B}[q]{R}{D} quit{R}")

    def _paint(self, line: str) -> str:
        if line.startswith("<!--") or line.startswith("     "):
            return f"{D}{line}{R}"
        if line.startswith("#"):
            return f"{B}{line}{R}"
        if "Noah —" in line or line.startswith("> ") or line.startswith("  > "):
            return f"{M}{line}{R}"
        if line.startswith("<details") or line.startswith("</details") or line.startswith("<sub"):
            return f"{D}{line}{R}"
        if line.startswith("|"):
            return f"{C}{line}{R}"
        return line

    # ------------------------------------------------------------------ input
    def step(self, k: str) -> bool:
        sel = self.sel
        if k in "1234":
            self.variant = int(k) - 1
            self.scroll = 0
        elif k == "d":
            order = list(Volume)
            self.volume = order[(order.index(self.volume) + 1) % len(order)]
        elif k in "+=":
            self.budget += 80
        elif k in "-_":
            self.budget = max(80, self.budget - 80)
        elif k == "s":
            for a in self.samples:
                if a not in self.entry.annotations:
                    self.entry.annotations.append(a)
        elif k == "x":
            self.entry.annotations.clear()
        elif k == "n":
            self.focus += 1
        elif k == "p":
            self.focus -= 1
        elif k == "a" and sel.kept:
            note = sel.kept[self.focus % len(sel.kept)]
            print(f"\n{D}annotating:{R} {note.text[:90]}")
            text = readline(f"{M}Noah — {R}")
            if text.strip():
                self.entry.annotations.append(Annotation(note.id, text.strip()))
        elif k == "j":
            self.scroll += 5
        elif k == "k":
            self.scroll = max(0, self.scroll - 5)
        elif k == "w":
            OUT.mkdir(exist_ok=True)
            name = self.variant_name.split(" ")[0]
            p = OUT / f"{self.entry.date}-{self.entry.slug}--{name}.md"
            p.write_text(self.rendered() + "\n", encoding="utf-8")
            print(f"\n{G}wrote{R} {p.relative_to(Path(__file__).parents[3])}  — press any key")
            getkey()
        elif k in ("q", "\x03", "\x1b"):
            return False
        return True

    def run(self) -> None:
        while True:
            self.frame()
            if not self.step(getkey()):
                break
        print()


if __name__ == "__main__":
    App().run()
