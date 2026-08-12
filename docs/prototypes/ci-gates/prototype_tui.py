"""PROTOTYPE — run #176's gate suite over this repository's real history.

    python docs/prototypes/ci-gates/prototype_tui.py

Nothing here is synthetic. Every case is a pull request that merged into `main`,
replayed through the five gates as if they had been required at the time. The
census (`a`) is the honest answer to *what would this cost on the day it lands*,
and it is the first thing to look at.

CASE `133` IS THE ONE THE SUITE EXISTS FOR. Two `core:` commits — the Hard Core —
landed under a merge commit stating `Bump: research PATCH`, whose own body reads
`Resolve #89 (core)` two lines above it. §6 promised that a mistyped commit would
"show up as a visible contradiction". It did. It was written out twice in one
commit message, and nothing read it.

THE WAIVER CASES (`w*`) are the design question. The suite is easy; a waiver
nobody can forge, that expires, and that cannot accumulate in silence, is not.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Output carries § and em dashes; a cp1252 console would mangle them.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

import gates  # noqa: E402

ALL = gates.changes()
BY_PR = {c.pr: c for c in ALL if c.pr}


def show(ch: gates.Change, waivers: list[gates.Waiver] | None = None) -> list[gates.Finding]:
    findings = gates.run_gates(ch)
    gates.resolve(ch, findings, waivers or [])
    print(gates.render(ch, findings))
    return findings


# ---------------------------------------------------------------------------
# The census — what the suite costs against history as it stands
# ---------------------------------------------------------------------------

def census() -> None:
    print("\n" + "=" * 78)
    print("CENSUS — the five gates, required, against all 21 merged pull requests")
    print("=" * 78)
    tally: dict[str, int] = {}
    blocked = 0
    for ch in ALL:
        findings = gates.run_gates(ch)
        code, _ = gates.verdict(findings)
        blocked += code != 0
        for f in findings:
            tally[f.code] = tally.get(f.code, 0) + 1
        marks = "".join(sorted({f.code[0] for f in findings}))
        print(f"  {'BLOCK' if code else '  ok '}  #{str(ch.pr):<4} {ch.merge['sha']}  "
              f"{marks:<6} {ch.merge['subject'][:48]}")
    print(f"\n  {blocked}/{len(ALL)} pull requests would not have merged.\n")
    for code, n in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"    {code:<7} {n:>3}  {EXPLAIN.get(code, '')}")
    print("\n  Branch classes across all 45 branches:")
    bad = [b for b in gates.HISTORY["branches"]
           if b != "main" and b.split("/")[0] not in gates.CLASSES]
    print(f"    {len(bad)} outside §4: {', '.join(bad)}")


EXPLAIN = {
    "C1": "unsigned — every branch commit in the repository",
    "C2": "signed by GitHub's key under a human login — every merge commit",
    "C3": "an agent identity committed an authored file",
    "T1": "a commit type outside §3's set",
    "T2": "merge subject lower than the branch's highest type",
    "T3": "no `Bump:` line at all",
    "T4": "`Bump:` outside any grammar — the field has never had one",
    "T5": "stated bump contradicts the computed one",
    "T6": "one branch, two tracks — one of the bumps goes nowhere",
    "T7": "merge subject does not name its pull request",
    "L1": "a relative link resolving to nothing",
    "L2": "`CHARTER.md` — declared in advance by §5, deliberately absent",
    "B1": "a branch class §4 never declared — `record/`, five of them",
    "D:R1": "a research document with no front matter",
    "D:R2": "no Transcript Archive session id",
    "D:R4": "a verdict row carrying no closed-set verdict",
    "D:R5": "no `What this does not establish` section",
    "D:R6": "debt items naming no issue",
    "D:R8": "no `Proposals` section",
    "D:R9": "appendix count absent or disagreeing",
    "D:R12": "verdict rows naming no section",
    "D:R13": "a substantial section with no inline citation",
}


# ---------------------------------------------------------------------------
# Waiver cases. One real finding, four homes, two granters.
# ---------------------------------------------------------------------------

def waiver_case(model: str, granted_by: str, code: str = "T5") -> None:
    ch = BY_PR[133]
    w = gates.Waiver(
        code=code,
        subject=ch.merge["sha"],
        reason="the two core: commits are pre-charter corrections, not a Hard Core revision",
        model=model,
        granted_by=granted_by,
        expires="1.0.0" if model == "issue" else None,
    )
    attributable, durable, countable, expiring, in_ci = gates.MODELS[model]
    print("\n" + "=" * 78)
    print(f"WAIVER — model `{model}`, granted by {granted_by}, against {code}")
    print("=" * 78)
    print(f"  {gates.MODEL_NOTES[model]}\n")
    print(f"    attributable {attributable!s:<6} durable {durable!s:<6} countable "
          f"{countable!s:<6} expiring {expiring!s:<6} readable-offline {in_ci}")
    if not attributable:
        print("\n  NOTE — CI cannot tell who granted this. `granted_by` below is a claim,")
        print("  not a fact, and the prototype is being generous by honouring it.")
    print()
    show(ch, [w])


def model_table() -> None:
    print("\n" + "=" * 78)
    print("THE FOUR CANDIDATE HOMES")
    print("=" * 78)
    print(f"  {'model':<10} {'attrib':<7} {'durable':<8} {'count':<7} {'expires':<8} offline")
    for m, (a, d, c, e, o) in gates.MODELS.items():
        print(f"  {m:<10} {a!s:<7} {d!s:<8} {c!s:<7} {e!s:<8} {o}")
    print()
    for m, note in gates.MODEL_NOTES.items():
        print(f"  {m}\n    {note}\n")
    print("  Nothing scores five. `file` and `issue` differ on exactly one axis each,")
    print("  and it is the axis the other one needs.")


def unwaivable() -> None:
    print("\n" + "=" * 78)
    print("WAIVER REFUSED — custody is not waivable, however it is granted")
    print("=" * 78)
    ch = BY_PR[133]
    w = gates.Waiver("C1", "*", "the App does not exist yet (#175)", "file", "human", None)
    show(ch, [w])
    print("\n  This is the case the suite most needs and least wants. C1 is unwaivable")
    print("  and unsatisfiable at the same time: #175 has not run, so no commit in this")
    print("  repository can be signed by an identity the check would accept. A gate")
    print("  that is both mandatory and impossible is not a gate — it is a red mark")
    print("  everyone learns to click past.")


CASES = [
    ("a", "the census — all 21 pull requests, all five gates", census),
    ("133", "the Hard Core landing as a PATCH  ← the headline", lambda: show(BY_PR[133])),
    ("28", "an evidence: branch merged as chore:, with no Bump: at all", lambda: show(BY_PR[28])),
    ("85", "one branch, two tracks — the tooling bump goes nowhere", lambda: show(BY_PR[85])),
    ("25", "a commit typed `research:` — outside §3's set entirely", lambda: show(BY_PR[25])),
    ("20", "the research documents, against #26's contract", lambda: show(BY_PR[20])),
    ("171", "a clean-looking modern pull request", lambda: show(BY_PR[171])),
    ("t", "the whole tree's links — one dangling, and it is deliberate",
     lambda: print(gates.render(
         gates.Change(None, None, {"sha": "-", "subject": "the tree as it stands", "body": ""}, []),
         gates.gate_link(None)))),
    ("m", "the four candidate waiver homes, side by side", model_table),
    ("w1", "waive T5 by trailer, granted by Noah", lambda: waiver_case("trailer", "human")),
    ("w2", "waive T5 by trailer, granted by an agent", lambda: waiver_case("trailer", "agent")),
    ("w3", "waive T5 in the pull request body — granter unknowable",
     lambda: waiver_case("pr-body", "undecidable")),
    ("w4", "waive T5 as a custody:deferred-style issue", lambda: waiver_case("issue", "human")),
    ("x", "waive the custody gate — refused", unwaivable),
]


def main() -> None:
    print(__doc__)
    while True:
        print("\n" + "-" * 78)
        for k, label, _ in CASES:
            print(f"  {k:<4} {label}")
        print("  all  run every case      q  quit")
        choice = input("\n> ").strip()
        if choice.lower() in ("q", "quit", ""):
            return
        if choice.lower() == "all":
            for _, _, fn in CASES:
                fn()
            continue
        match = next((c for c in CASES if c[0] == choice), None)
        if match:
            match[2]()
        else:
            print("  ?")


if __name__ == "__main__":
    main()
