#!/usr/bin/env python3
"""
Check research-track documents against the output contract in docs/research/README.md.

The contract exists to remove a revision tax: three research tickets each produced a
document invented from scratch, shaped differently, and at least one needed a follow-up
commit to apply review feedback. An agent that knows the required shape before it starts
produces work that lands in one pass.

Twelve checks are here. Two are not, and are named in the contract anyway so that a green
run is not mistaken for a merge decision: whether the argument survives an adversarial
read, and whether the recommendation is actionable. Those are the reviewer's, and this
tool exists so their attention is spent there instead of on shape.

Usage:
    python tools/check_research_doc.py                       # every doc in docs/research/
    python tools/check_research_doc.py path/to/doc.md ...    # named documents
    python tools/check_research_doc.py --quiet               # failures only
    python tools/check_research_doc.py --help                # this, on stdout, exit 0

Exit codes (distinct so CI can tell "fix the document" from "the tool is broken"):
    0  every document satisfies the contract
    1  at least one blocking check failed
    2  the tool could not run — no such file, nothing to check

Advisory failures are reported and do not affect the exit code.

Settled in #26; the prototype it came from, including the two rules that did not survive
and the reasoning, is on `prototype/research-output-contract`. Hardened in #53, where review
found two checks that passed falsely — a commented `sources:` turned R9's count comparison off
in silence, and a document's own ticket read as a filed debt issue — which is the failure this
tool exists to prevent, in the tool itself.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

# Findings carry em dashes and §; a cp1252 console would mangle them in the CI log.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "research"

EXIT_OK, EXIT_FAILED, EXIT_TOOL = 0, 1, 2

FRONT_MATTER_KEYS = ["ticket", "map", "date", "kind", "tier", "session", "sources"]
KINDS = {"survey", "verification", "question", "revision"}

# The closed vocabulary a sub-question's verdict is stated in.
VERDICTS = ["Supported", "Refuted", "Loose", "Unresolved", "Established", "Contested", "Open"]

RE_FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$", re.M)
RE_VERDICT = re.compile(r"\*\*(" + "|".join(VERDICTS) + r")\b[^*]*\*\*")
RE_LINK = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
RE_ISSUE = re.compile(r"#(\d+)")
RE_HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.S)
RE_RETRIEVED = re.compile(r"retrieved\s+\d{4}-\d{2}-\d{2}", re.I)
# A full digest, either case. The archive identifies sessions the way DATA-PROTOCOL §2
# identifies everything else — by content hash — and half a hash is not one, so a truncation
# a reader cannot resolve is rejected rather than quietly accepted.
RE_SESSION = re.compile(r"^(sha256:[0-9a-f]{64}|unrecorded)$", re.I)
# A YAML value's trailing comment. Whitespace-anchored so a `#` inside a value survives:
# `supersedes: docs/x.md#anchor` is a path, `sources: 44   # must match` is not.
RE_YAML_COMMENT = re.compile(r"\s+#.*$")
# A table's rule row, matched as a rule rather than by containing `---`, which a
# sub-question is entitled to contain.
RE_TABLE_RULE = re.compile(r"[|\s:-]+")
# A list item at column zero, ordered or unordered. Indentation-blind matching made a
# sub-bullet elaborating on a debt item into a second, unfiled debt item.
RE_ITEM = re.compile(r"^(\d+\.|[-*])\s+\S")
RE_FENCE = re.compile(r"^\s*(```+|~~~+)")

# Sources that move. A paper is fixed by its DOI; a pricing page, a rate-limit table or a
# `latest` docs URL is a claim about today. Needles are deliberately few: R10 is advisory, so
# a miss costs a reminder and a false hit costs a reviewer's patience.
VOLATILE = ("pricing", "/plans", "plans-and-", "rate-limit", "quota", "billing", "/status",
            "changelog", "release-notes", "/blog", "/wiki", "dashboard", "/terms", "/latest")


# ---------------------------------------------------------------------------------------
# Parsing. Deliberately dumb: regex over Markdown, no dependencies. Everything the contract
# requires is either a front-matter key or a heading.
# ---------------------------------------------------------------------------------------


@dataclass
class Section:
    level: int
    title: str
    body: str

    @property
    def links(self) -> list[str]:
        return RE_LINK.findall(self.body)

    @property
    def slug(self) -> str:
        """`## 4. Implications for the rung` -> `implications for the rung`."""
        return re.sub(r"^\d+(\.\d+)*\.?\s*", "", self.title).strip().lower()

    @property
    def subsections(self) -> list[Section]:
        """The headings one level down, with their own bodies."""
        return [s for s in split_sections(self.body) if s.level == self.level + 1]


@dataclass
class Doc:
    path: Path
    text: str
    front: dict[str, str] = field(default_factory=dict)
    sections: list[Section] = field(default_factory=list)

    @property
    def name(self) -> str:
        try:
            return str(self.path.relative_to(ROOT)).replace("\\", "/")
        except ValueError:
            return str(self.path)

    @property
    def top_sections(self) -> list[Section]:
        return [s for s in self.sections if s.level == 2]

    def section_like(self, *needles: str) -> Section | None:
        for s in self.sections:
            if any(n in s.slug for n in needles):
                return s
        return None

    @property
    def verdict_rows(self) -> list[str]:
        """
        The body rows of §0's verdict table, header and rule excluded.

        Both exclusions are positional. Dropping rows that contain `---` deleted any table
        with a sub-question like `Is A --- B?` in it, and naming the header by its `Verdict`
        column scored the header as a body row for a table whose column is called `Finding`.
        The first row of a Markdown table is its header; the rule is a rule.

        Per table, not per section: a run of `|` lines is a table, and a §0 carrying two of
        them would otherwise leak the second one's header into R4 and R12 as a verdictless
        row. No document does this today, which is the cheapest time to fix it.
        """
        if not self.top_sections:
            return []
        rows: list[str] = []
        run: list[str] = []
        for ln in self.top_sections[0].body.split("\n"):
            if ln.strip().startswith("|"):
                run.append(ln)
            else:
                rows.extend(run[1:])
                run = []
        rows.extend(run[1:])
        return [r for r in rows if not RE_TABLE_RULE.fullmatch(r.strip())]


def split_sections(body: str) -> list[Section]:
    heads = list(RE_HEADING.finditer(body))
    out = []
    for i, h in enumerate(heads):
        level = len(h.group(1))
        # A section owns everything up to the next heading at its own level or higher, so a
        # `##` section's body includes its `###` subsections. Getting this wrong made every
        # top-level section look uncited on the prototype's first run.
        end = len(body)
        for j in range(i + 1, len(heads)):
            if len(heads[j].group(1)) <= level:
                end = heads[j].start()
                break
        out.append(Section(level, h.group(2).strip(), body[h.end() : end]))
    return out


def strip_fenced_code(text: str) -> str:
    """
    Fenced blocks quote; they do not assert. A document explaining R7 is not violating it.

    Two rules, both CommonMark's, and both load-bearing for a check that would otherwise be
    switched off by a formatting accident — the shape of the R9 bug this file was hardened
    against, and worth not reintroducing in the fix for it.

    A closing fence is the same character and *at least as long* as the one that opened it,
    so a four-backtick block quoting a three-backtick example — the standard way to document
    Markdown, which is the case this function exists to serve — is one block and not three.

    An unterminated fence strips nothing. Everything after a stray ``` would otherwise be
    invisible to R7, silently, and a check that goes quiet on malformed input is worse than
    one that complains: a document that flags a comment it did not intend to hide gets read,
    while one that hides a comment nobody sees does not.
    """
    out: list[str] = []
    opener: str | None = None
    for line in text.split("\n"):
        m = RE_FENCE.match(line)
        if opener is None:
            if m:
                opener = m.group(1)
                continue
            out.append(line)
        elif m and m.group(1)[0] == opener[0] and len(m.group(1)) >= len(opener):
            opener = None
    if opener is not None:
        return text
    return "\n".join(out)


def parse(path: Path, text: str) -> Doc:
    text = text.replace("\r\n", "\n")
    doc = Doc(path=path, text=text)

    m = RE_FRONT.match(text)
    body = text
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line and not line.startswith((" ", "-", "#")):
                k, _, v = line.partition(":")
                # The template in §1 of the contract comments every key, so a document that
                # copies it was checked against `unrecorded          # no transcript`. R2
                # said so loudly; R9 read a commented `sources:` as non-numeric and skipped
                # its count comparison in silence, which is the worse half by far.
                doc.front[k.strip().lower()] = RE_YAML_COMMENT.sub("", v).strip()
        body = text[m.end() :]

    doc.sections = split_sections(body)
    return doc


# ---------------------------------------------------------------------------------------
# The checks. Each returns (passed, evidence).
# ---------------------------------------------------------------------------------------


def _front_matter(d: Doc) -> tuple[bool, str]:
    if not d.front:
        return False, "no YAML front matter"
    missing = [k for k in FRONT_MATTER_KEYS if not d.front.get(k)]
    if missing:
        return False, "missing: " + ", ".join(missing)
    if d.front["kind"] not in KINDS:
        return False, f"kind={d.front['kind']!r} not in {sorted(KINDS)}"
    return True, ", ".join(f"{k}={d.front[k]}" for k in ("ticket", "kind", "tier"))


def _session(d: Doc) -> tuple[bool, str]:
    s = d.front.get("session", "")
    if not s:
        return False, "no session id — the work is untraceable to a transcript"
    if not RE_SESSION.match(s):
        # Naming the rule, not the shape: the README showed `sha256:9f2c…` until #53, so the
        # reader most likely to see this has a truncated digest and needs to be told that the
        # length is what is wrong with it.
        return False, (f"session={s!r} is not `sha256:` + 64 hex digits or the literal "
                       f"`unrecorded`")
    if s == "unrecorded":
        return True, "unrecorded — declared, which is the point"
    return True, s


def _verdict_first(d: Doc) -> tuple[bool, str]:
    tops = d.top_sections
    if not tops:
        return False, "no `##` sections at all"
    first = tops[0]
    if not any(k in first.slug for k in ("verdict", "summary", "conclud")):
        return False, f"first section is {first.title!r}, not a verdict"
    has_table = any(
        ln.strip().startswith("|") and RE_TABLE_RULE.fullmatch(ln.strip())
        for ln in first.body.split("\n")
    )
    has_line = re.search(r"^>\s+\*\*", first.body, re.M) is not None
    if not (has_table or has_line):
        return False, "verdict section carries neither a verdict table nor a stated verdict"
    return True, f"{first.title!r}" + (" + table" if has_table else "") + (
        " + one-line verdict" if has_line else ""
    )


def _sub_question_verdicts(d: Doc) -> tuple[bool, str]:
    """
    Every sub-question carries a verdict from the closed set.

    Attached to the sub-question, not the section. The prototype's first draft required a
    verdict token on every top-level section and produced headings like "Computational
    cost — **Refuted** as a binding constraint" — a verdict wrapped around a sub-clause to
    satisfy a checker. A sub-question has a verdict; a section is where one is argued, and
    `_claims_traceable` is what ties the two together.
    """
    rows = d.verdict_rows
    if not rows:
        return False, "no verdict table — the sub-questions and their verdicts are not stated"
    bare = [r for r in rows if not RE_VERDICT.search(r)]
    if bare:
        return False, f"{len(bare)}/{len(rows)} verdict rows carry no closed-set verdict"
    return True, f"all {len(rows)} sub-questions carry a verdict from the closed set"


# A subsection's body has to be a sentence rather than a token. `None.` against `sources not
# reached` is a claim worth making — "every source in the appendix was opened" — and worth
# making in words, because the bare word is what a document writes when it has not looked.
MIN_SUBSECTION = 20


def _negative_space(d: Doc) -> tuple[bool, str]:
    """
    The three subsections, as headings with something under each.

    Structural, not keyword. The prototype searched the lowercased body for needles as loose
    as `gap`, so the single sentence *"We could not reach the original; that gap is open, and
    if false it would change the verdict"* satisfied all three. This is the contract's one
    real addition (§4) and the section #50 says an agent cannot honestly retrofit; a check it
    can pass by ceremony is worse than no check at all.
    """
    s = d.section_like("does not establish", "not established")
    if s is None:
        return False, "no `What this does not establish` section"
    want = {
        "sources not reached": ("not reached", "sources not", "unreached"),
        "open gaps": ("open gap", "gaps"),
        "load-bearing ifs": ("load-bearing", "load bearing", "ifs"),
    }
    # Claimed subsections leave the pool. Searching it independently for each of the three
    # let one heading — `### Open gaps and load-bearing ifs` — satisfy two of them, which is
    # two subsections where §4 says three, and the ceremony this check went structural to
    # stop, in a smaller size.
    pool = list(s.subsections)
    missing, thin = [], []
    for name, needles in want.items():
        found = next((x for x in pool if any(n in x.slug for n in needles)), None)
        if found is None:
            missing.append(name)
            continue
        pool.remove(found)
        if len(found.body.strip()) < MIN_SUBSECTION:
            thin.append(name)
    if missing:
        return False, "section present but missing: " + ", ".join(missing)
    if thin:
        return False, "heading with nothing under it: " + ", ".join(thin)
    return True, "sources not reached + open gaps + load-bearing ifs, each argued"


def _debt_filed(d: Doc) -> tuple[bool, str]:
    """
    Every debt item is a filed `debt:open` issue, and the front matter mirrors the numbers.

    The prototype accepted the word `unfiled` and a document passed by writing it five
    times, which is the gate PROTOCOL.md §5 argues is worse than none. There is no escape
    hatch: an agent that finds debt can open the issue, so a document reporting unfiled
    debt has left work undone rather than hit a limitation. This is also what keeps the
    tracker the only place debt is ever checked — the front matter mirrors, never adds.

    The hatch stayed open under a different spelling for one more round: any `#\\d+` counted,
    including the document's own ticket, so *"someone should re-read the #4 survey"* in a
    document resolving #4 read as filed. A document's own ticket is excluded here. What is
    still not checked is the semantic half — that the number is an issue, that it is open,
    that it carries `debt:open` — and §5 of the contract now says so rather than implying CI
    covers it.
    """
    s = d.section_like("verification debt", "debt")
    if s is None:
        return False, "no Verification Debt section (write `None.` if there is none)"
    items = [ln for ln in s.body.split("\n") if RE_ITEM.match(ln)]
    declared = sorted(int(n) for n in re.findall(r"\d+", d.front.get("debt", "")))
    own = {int(n) for n in re.findall(r"\d+", d.front.get("ticket", ""))}

    def filed(line: str) -> set[int]:
        return {int(n) for n in RE_ISSUE.findall(line)} - own

    if not items:
        if "none." in s.body.strip().lower()[:32] and not declared:
            return True, "no debt, declared"
        return False, "debt section present but nothing itemised"
    unfiled = [ln for ln in items if not filed(ln)]
    if unfiled:
        # Two causes, two messages. #50 retrofits the three documents on `main`, none of
        # which cite an issue at all, and telling their author about a ticket they never
        # mentioned is a diagnostic that sends them looking for the wrong thing.
        self_only = [ln for ln in unfiled if RE_ISSUE.search(ln)]
        if not self_only:
            why = "name no issue"
        elif len(self_only) == len(unfiled):
            why = f"name only this document's own ticket (#{d.front.get('ticket', '')})"
        else:
            why = "name no issue other than this document's own ticket"
        return False, f"{len(unfiled)}/{len(items)} debt items {why} — file them first"
    cited = sorted(set().union(*(filed(ln) for ln in items)))
    if declared != cited:
        return False, f"front matter debt={declared or '[]'} does not mirror the section {cited}"
    return True, f"{len(items)} items, all filed: {cited}"


def _no_hidden_record(d: Doc) -> tuple[bool, str]:
    """#5's finding, mechanised: debt logged inside an HTML comment is logged nowhere."""
    # Word-bounded: an unbounded `tier` matches the `tier` inside `prettier`, which is how
    # a lint directive became a custody finding on the first run of these tests.
    bad = [c for c in RE_HTML_COMMENT.findall(strip_fenced_code(d.text))
           if re.search(r"\b(debts?|tiers?|unverified|provenance|todo)\b", c, re.I)]
    if bad:
        return False, f"{len(bad)} HTML comment(s) carry record content: {bad[0].strip()[:60]!r}"
    return True, "no record content hidden in comments"


def _proposals(d: Doc) -> tuple[bool, str]:
    s = d.section_like("proposal", "proposed amendment", "proposed edits")
    if s is None:
        return False, "no Proposals section (write `None.` if there are none)"
    if len(s.body.strip()) < 5:
        return False, "Proposals section is empty rather than saying `None.`"
    return True, "present"


def _appendix_sources(d: Doc) -> tuple[bool, str]:
    s = d.section_like("appendix", "primary sources")
    if s is None:
        return False, "no primary-source appendix"
    # Dashes or numbers: `_debt_filed` accepted both, so a document numbering its sources was
    # told its appendix listed nothing while its numbered debt list was read fine.
    lines = [ln for ln in s.body.split("\n") if RE_ITEM.match(ln)]
    if not lines:
        return False, "appendix present but lists nothing"
    declared = d.front.get("sources", "")
    if not declared.isdigit():
        # Never silently: an unreadable count used to skip the comparison without a word, and
        # this is the one check whose whole job is catching a count that has drifted.
        if not declared:
            return False, f"front matter declares no source count; the appendix lists {len(lines)}"
        return False, f"front matter declares sources={declared!r}, which is not a count"
    if int(declared) != len(lines):
        return False, f"front matter declares sources={declared}, appendix lists {len(lines)}"
    unlinked = [ln for ln in lines if "http" not in ln]
    if unlinked:
        return False, f"{len(unlinked)}/{len(lines)} appendix entries carry no link"
    return True, f"{len(lines)} sources, all linked"


def _volatile_dated(d: Doc) -> tuple[bool, str]:
    """
    Facts that rot need a retrieval date. A paper does not move; a pricing page does.

    Per entry, and no longer per `kind`. Exempting `kind: survey` wholesale assumed surveys
    cite only papers, and #27 is the counter-example the exemption would have waved through:
    a document whose sources are pricing tables and live docs URLs. What decides is the
    source, which is knowable from the line, not the document's kind, which is not.
    """
    s = d.section_like("appendix", "primary sources")
    if s is None:
        return False, "no appendix to date"
    lines = s.body.split("\n")
    entries = [ln for ln in lines if RE_ITEM.match(ln)]
    if not entries:
        return True, "nothing in the appendix to date — R9 blocks on that already"
    # One date on the heading or in the preamble covers everything under it, which is how #27
    # writes it: `## Appendix: primary sources, all retrieved 2026-07-29`.
    preamble = "\n".join(lines[: lines.index(entries[0])])
    if RE_RETRIEVED.search(s.title) or RE_RETRIEVED.search(preamble):
        return True, "one retrieval date covers the appendix"
    stale = [ln for ln in entries
             if any(n in ln.lower() for n in VOLATILE) and not RE_RETRIEVED.search(ln)]
    if stale:
        return False, (f"{len(stale)}/{len(entries)} entries cite a source that moves and carry "
                       f"no `retrieved YYYY-MM-DD`: {stale[0].strip()[:48]!r}")
    return True, f"{len(entries)} entries, none citing an undated source that moves"


def _claims_traceable(d: Doc) -> tuple[bool, str]:
    """A summary table that cannot be walked back into the argument is a press release."""
    rows = d.verdict_rows
    if not rows:
        return True, "no verdict table — the verdict check blocks on that already"

    def traced(row: str) -> bool:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        # An explicit §, a cell that is only a section number, or a cell that opens with
        # one. Ranges and sub-labels (§1.2–1.3, §3.2(c)) count.
        return any(
            c.startswith("§")
            or re.fullmatch(r"\d+(\.\d+)*", c)
            or re.match(r"\**\d+(\.\d+)*\**\s", c)
            for c in cells
        )

    untraced = [r for r in rows if not traced(r)]
    if untraced:
        return False, f"{len(untraced)}/{len(rows)} verdict rows name no section"
    return True, f"{len(rows)} verdict rows, each naming its section"


def _link_density(d: Doc) -> tuple[bool, str]:
    """Borrowed frames are cited in place — the map's standing preference, mechanised."""
    skip = ("verdict", "summary", "conclud", "appendix", "primary sources", "proposal",
            "debt", "does not establish", "revision")
    ev = [s for s in d.top_sections if not any(k in s.slug for k in skip)]
    dry = [s.title for s in ev if not s.links and len(s.body) > 400]
    if dry:
        return False, (f"{len(dry)} substantial section(s) with no inline citation: "
                       + "; ".join(t[:40] for t in dry[:2]))
    return True, f"{len(RE_LINK.findall(d.text))} inline citations across {len(ev)} sections"


@dataclass
class Check:
    id: str
    title: str
    severity: str  # "blocking" | "advisory"
    run: Callable[[Doc], tuple[bool, str]]


CHECKS: list[Check] = [
    Check("R1", "Machine-readable front matter", "blocking", _front_matter),
    Check("R2", "Transcript Archive session id", "blocking", _session),
    Check("R3", "Verdict first, and stated", "blocking", _verdict_first),
    Check("R4", "Every sub-question carries a verdict", "blocking", _sub_question_verdicts),
    Check("R5", "What this does not establish", "blocking", _negative_space),
    Check("R6", "Every debt item is a filed issue", "blocking", _debt_filed),
    Check("R7", "No record content in HTML comments", "blocking", _no_hidden_record),
    Check("R8", "Proposals section, `None.` if none", "blocking", _proposals),
    Check("R9", "Primary-source appendix, all linked", "blocking", _appendix_sources),
    Check("R12", "Verdict rows name their section", "blocking", _claims_traceable),
    Check("R10", "Volatile sources carry a retrieval date", "advisory", _volatile_dated),
    Check("R13", "Citations in place, not only in the appendix", "advisory", _link_density),
]


def check(doc: Doc) -> list[tuple[Check, bool, str]]:
    return [(c, *c.run(doc)) for c in CHECKS]


def report(doc: Doc, results, quiet: bool) -> bool:
    """Print one document's results. Returns True if it passes every blocking check."""
    blocking = [(c, e) for c, ok, e in results if not ok and c.severity == "blocking"]
    advisory = [(c, e) for c, ok, e in results if not ok and c.severity == "advisory"]

    if blocking:
        print(f"FAIL  {doc.name}")
    elif advisory:
        print(f"warn  {doc.name}")
    elif not quiet:
        print(f"ok    {doc.name}")

    for c, e in blocking:
        print(f"        {c.id:<4} {c.title} — {e}")
    for c, e in advisory:
        print(f"        {c.id:<4} {c.title} — {e}  (advisory)")
    return not blocking


FLAGS = {"--quiet", "--help", "-h"}


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    flags = [a for a in sys.argv[1:] if a.startswith("-")]

    # `--quite` used to run verbose and say nothing about it, which is the wrong direction for
    # a tool whose output is the point. Asking for help is not that failure: it is a
    # successful invocation, so it goes to stdout and exits 0, and exit 2 keeps meaning what
    # the docstring says it means — the tool could not run.
    unknown = [f for f in flags if f not in FLAGS]
    if unknown or "--help" in flags or "-h" in flags:
        stream = sys.stderr if unknown else sys.stdout
        for f in unknown:
            print(f"unrecognised flag: {f}", file=sys.stderr)
        body = __doc__.split("Usage:", 1)[1].split("Exit codes")[0].strip()
        print("usage:", file=stream)
        for line in body.split("\n"):
            print("    " + line.strip(), file=stream)
        sys.exit(EXIT_TOOL if unknown else EXIT_OK)
    quiet = "--quiet" in flags

    paths = [Path(a) for a in args] if args else sorted(DOCS.glob("*.md"))
    paths = [p for p in paths if p.name.lower() != "readme.md"]
    if not paths:
        print("nothing to check", file=sys.stderr)
        sys.exit(EXIT_TOOL)

    missing = [p for p in paths if not p.is_file()]
    if missing:
        for p in missing:
            print(f"no such file: {p}", file=sys.stderr)
        sys.exit(EXIT_TOOL)

    passed = 0
    for p in paths:
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError as e:
            # Exit 2 is documented as "the tool could not run"; a traceback is not that.
            print(f"{p}: not UTF-8 ({e.reason} at byte {e.start})", file=sys.stderr)
            sys.exit(EXIT_TOOL)
        doc = parse(p, text)
        if report(doc, check(doc), quiet):
            passed += 1

    failed = len(paths) - passed
    print(f"\n{passed}/{len(paths)} documents satisfy the contract")
    if failed:
        print(
            "The contract is docs/research/README.md. Two checks are not here and are the "
            "reviewer's:\nwhether the argument survives an adversarial read, and whether "
            "the recommendation is actionable.",
            file=sys.stderr,
        )
        sys.exit(EXIT_FAILED)


if __name__ == "__main__":
    main()
