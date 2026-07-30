"""
PROTOTYPE (ticket #26) — the research-output document contract, as a checkable object.

Pure module. No I/O, no terminal codes: callers hand in (name, text) and get back a
Report. `prototype_tui.py` is the throwaway shell over it; this file is the bit that
would lift into `tools/check_research_doc.py` if the contract survives review.

The question it exists to answer: what must a research-track document contain to be
mergeable, and which of those requirements can a machine check?

Each RULE carries `checked_by` — `ci` if the check below IS the check, `human` if the
predicate here is a proxy at best and a reviewer owns it. A contract whose rules are
all `human` has mechanised nothing; one whose rules are all `ci` is checking shape and
calling it quality. The split is the finding, so it is data, not a comment.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# --------------------------------------------------------------------------------------
# Parsing. Deliberately dumb: regex over Markdown, no dependencies. A real checker would
# not need more, because everything the contract requires is either a fenced front-matter
# key or a heading.
# --------------------------------------------------------------------------------------

FRONT_MATTER_KEYS = ["ticket", "map", "date", "kind", "tier", "session", "sources"]
KINDS = {"survey", "verification", "question", "revision"}

# The verdict vocabulary claims are marked with, at the claim site.
VERDICTS = ["Supported", "Refuted", "Loose", "Unresolved", "Established", "Contested", "Open"]

RE_FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$", re.M)
RE_VERDICT = re.compile(r"\*\*(" + "|".join(VERDICTS) + r")\b[^*]*\*\*")
RE_TIER_BADGE = re.compile(r"⟦\s*T([123])\s*(?:·\s*(#\d+(?:\s*,\s*#\d+)*))?\s*⟧")
RE_LINK = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
RE_ISSUE = re.compile(r"#(\d+)")
RE_HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.S)
RE_RETRIEVED = re.compile(r"retrieved\s+\d{4}-\d{2}-\d{2}", re.I)


@dataclass
class Section:
    level: int
    title: str
    body: str

    @property
    def verdicts(self) -> list[str]:
        return RE_VERDICT.findall(self.body) + RE_VERDICT.findall(self.title)

    @property
    def links(self) -> list[str]:
        return RE_LINK.findall(self.body)

    @property
    def slug(self) -> str:
        # "## 4. Implications for the first rung" -> "implications for the first rung"
        return re.sub(r"^\d+(\.\d+)*\.?\s*", "", self.title).strip().lower()


@dataclass
class Doc:
    name: str
    text: str
    front: dict[str, str] = field(default_factory=dict)
    front_raw: str = ""
    sections: list[Section] = field(default_factory=list)

    @property
    def top_sections(self) -> list[Section]:
        return [s for s in self.sections if s.level == 2]

    def section_like(self, *needles: str) -> Section | None:
        for s in self.sections:
            if any(n in s.slug for n in needles):
                return s
        return None

    @property
    def comments(self) -> list[str]:
        return RE_HTML_COMMENT.findall(self.text)

    @property
    def badges(self) -> list[tuple[str, str]]:
        return RE_TIER_BADGE.findall(self.text)

    @property
    def links(self) -> list[str]:
        return RE_LINK.findall(self.text)


def parse(name: str, text: str) -> Doc:
    text = text.replace("\r\n", "\n")
    doc = Doc(name=name, text=text)

    m = RE_FRONT.match(text)
    if m:
        doc.front_raw = m.group(1)
        for line in doc.front_raw.split("\n"):
            if ":" in line and not line.startswith((" ", "-", "#")):
                k, _, v = line.partition(":")
                doc.front[k.strip().lower()] = v.strip()
        body = text[m.end() :]
        offset = m.end()
    else:
        body, offset = text, 0

    heads = list(RE_HEADING.finditer(body))
    for i, h in enumerate(heads):
        level = len(h.group(1))
        # A section owns everything up to the next heading at its own level or higher, so
        # a `##` section's body includes its `###` subsections. Getting this wrong made
        # every top-level section look uncited on the first run of this prototype.
        end = len(body)
        for j in range(i + 1, len(heads)):
            if len(heads[j].group(1)) <= level:
                end = heads[j].start()
                break
        doc.sections.append(
            Section(level=level, title=h.group(2).strip(), body=body[h.end() : end])
        )
    _ = offset
    return doc


# --------------------------------------------------------------------------------------
# The contract. Each rule is a predicate over a Doc returning (passed, evidence).
# --------------------------------------------------------------------------------------


@dataclass
class Rule:
    id: str
    title: str
    severity: str  # "blocking" | "advisory"
    checked_by: str  # "ci" | "human"
    why: str
    check: object  # Callable[[Doc], tuple[bool, str]]
    enabled: bool = True


@dataclass
class Result:
    rule: Rule
    passed: bool
    evidence: str


@dataclass
class Report:
    doc: Doc
    results: list[Result]

    @property
    def blocking_failures(self) -> list[Result]:
        return [r for r in self.results if not r.passed and r.rule.severity == "blocking"]

    @property
    def advisory_failures(self) -> list[Result]:
        return [r for r in self.results if not r.passed and r.rule.severity == "advisory"]

    @property
    def ci_failures(self) -> list[Result]:
        return [r for r in self.blocking_failures if r.rule.checked_by == "ci"]

    @property
    def passes_ci(self) -> bool:
        """CI can clear shape. It cannot clear the argument — that is R14/R15's point."""
        return not self.ci_failures


# -- individual checks ------------------------------------------------------------------


def _front_matter(d: Doc) -> tuple[bool, str]:
    if not d.front:
        return False, "no YAML front matter"
    missing = [k for k in FRONT_MATTER_KEYS if k not in d.front or not d.front[k]]
    if missing:
        return False, "missing: " + ", ".join(missing)
    if d.front.get("kind") not in KINDS:
        return False, f"kind={d.front.get('kind')!r} not in {sorted(KINDS)}"
    return True, ", ".join(f"{k}={d.front[k]}" for k in ("ticket", "kind", "tier"))


def _session(d: Doc) -> tuple[bool, str]:
    s = d.front.get("session", "")
    if not s:
        return False, "no session id — the work is untraceable to a transcript"
    if not re.match(r"^(sha256:[0-9a-f]{8,64}|unrecorded)$", s):
        return False, f"session={s!r} is not sha256:<digest> or the literal `unrecorded`"
    if s == "unrecorded":
        return True, "unrecorded — declared, which is the point"
    return True, s


def _verdict_first(d: Doc) -> tuple[bool, str]:
    tops = d.top_sections
    if not tops:
        return False, "no `##` sections at all"
    first = tops[0]
    if "verdict" not in first.slug and "summary" not in first.slug and "conclud" not in first.slug:
        return False, f"first section is {first.title!r}, not a verdict"
    has_table = "|---" in first.body or "|--" in first.body
    has_blockquote = re.search(r"^>\s+\*\*", first.body, re.M) is not None
    if not (has_table or has_blockquote):
        return False, "verdict section carries neither a verdict table nor a stated verdict"
    return True, f"{first.title!r}" + (" + table" if has_table else "") + (
        " + one-line verdict" if has_blockquote else ""
    )


def _per_claim_verdicts(d: Doc) -> tuple[bool, str]:
    """Every evidence section argues something, and says what."""
    skip = ("verdict", "summary", "conclud", "appendix", "primary sources", "debt", "proposal",
            "does not establish", "revision log")
    ev = [s for s in d.top_sections if not any(k in s.slug for k in skip)]
    if not ev:
        return False, "no evidence sections"
    bare = [s.title for s in ev if not s.verdicts]
    if bare:
        return False, f"{len(bare)}/{len(ev)} evidence sections carry no verdict token: " + \
            "; ".join(t[:44] for t in bare[:3])
    return True, f"all {len(ev)} evidence sections carry a verdict"


def _negative_space(d: Doc) -> tuple[bool, str]:
    s = d.section_like("does not establish", "not established", "what this leaves open")
    if s is None:
        return False, "no `What this does not establish` section"
    want = {
        "sources not reached": ("not reached", "could not reach", "unreached"),
        "open gaps": ("open gap", "gap", "opened"),
        "load-bearing ifs": ("would change the verdict", "load-bearing", "if false"),
    }
    body = (s.body + " " + " ".join(x.title + x.body for x in d.sections
                                    if x.level == 3 and s.title in d.text)).lower()
    missing = [k for k, needles in want.items() if not any(n in body for n in needles)]
    if missing:
        return False, "section present but missing: " + ", ".join(missing)
    return True, "sources not reached + open gaps + load-bearing ifs"


def _debt_itemised(d: Doc) -> tuple[bool, str]:
    s = d.section_like("verification debt", "debt")
    if s is None:
        return False, "no Verification Debt section"
    items = [ln for ln in s.body.split("\n") if re.match(r"^\s*(\d+\.|[-*])\s+\S", ln)]
    if not items:
        return False, "debt section present but nothing itemised"
    unfiled = [ln for ln in items if not RE_ISSUE.search(ln) and "unfiled" not in ln.lower()]
    if unfiled:
        return False, f"{len(unfiled)}/{len(items)} debt items cite neither an issue nor `unfiled`"
    return True, f"{len(items)} items, all filed or explicitly unfiled"


def _no_hidden_record(d: Doc) -> tuple[bool, str]:
    """#5's finding, mechanised: debt logged inside an HTML comment is logged nowhere."""
    bad = [c for c in d.comments
           if re.search(r"debt|tier|unverified|provenance|todo", c, re.I)]
    if bad:
        return False, f"{len(bad)} HTML comment(s) carry record content: " + \
            repr(bad[0].strip()[:60])
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
    lines = [ln for ln in s.body.split("\n") if re.match(r"^\s*[-*]\s+\S", ln)]
    if not lines:
        return False, "appendix present but lists nothing"
    unlinked = [ln for ln in lines if "http" not in ln]
    n = len(lines)
    declared = d.front.get("sources", "")
    if declared.isdigit() and abs(int(declared) - n) > 0:
        return False, f"front matter declares sources={declared}, appendix lists {n}"
    if unlinked:
        return False, f"{len(unlinked)}/{n} appendix entries carry no link"
    return True, f"{n} sources, all linked"


def _volatile_dated(d: Doc) -> tuple[bool, str]:
    """Facts that rot need a retrieval date. #27 got this right; nobody else did."""
    if d.front.get("kind") == "survey":
        return True, "n/a — surveys cite papers, which do not move"
    s = d.section_like("appendix", "primary sources")
    if s is None:
        return False, "no appendix to date"
    if RE_RETRIEVED.search(s.title) or RE_RETRIEVED.search(s.body[:400]):
        return True, "retrieval date stated"
    return False, "no `retrieved YYYY-MM-DD` on a document citing volatile sources"


def _no_inline_tier_badges(d: Doc) -> tuple[bool, str]:
    """
    The finding this prototype was built to test.

    #5 settled that an agent's reading never promotes a tier. So every claim in an
    agent-written document is T3 by construction, and a per-claim badge inside one
    carries zero bits. The badge belongs where the claim lands — CONTEXT.md — and is
    typed by Noah. A document that badges its own claims is either lying or padding.
    """
    if d.badges:
        return False, f"{len(d.badges)} inline tier badge(s) — all necessarily T3, so 0 bits"
    return True, "tier declared once in front matter, badges left to the destination"


def _claims_traceable(d: Doc) -> tuple[bool, str]:
    """Every row of the verdict table points at the section that argues it."""
    tops = d.top_sections
    if not tops:
        return False, "no sections"
    rows = [ln for ln in tops[0].body.split("\n") if ln.strip().startswith("|")]
    rows = [r for r in rows if "---" not in r and not re.search(r"\|\s*Verdict\s*\|", r)]
    if not rows:
        return True, "no verdict table to trace (blockquote verdict only)"
    def traced(row: str) -> bool:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        # A section reference is either an explicit § or a cell that is nothing but a
        # section number. Ranges and sub-labels (§1.2–1.3, §3.2(c)) count.
        return any(c.startswith("§") or re.fullmatch(r"\d+(\.\d+)*", c) for c in cells)

    untraced = [r for r in rows if not traced(r)]
    if untraced:
        return False, f"{len(untraced)}/{len(rows)} verdict rows name no section"
    return True, f"{len(rows)} verdict rows, each naming its section"


def _link_density(d: Doc) -> tuple[bool, str]:
    """Borrowed frames are cited in place — the map's standing preference, mechanised."""
    skip = ("verdict", "summary", "appendix", "proposal", "debt", "does not establish")
    ev = [s for s in d.top_sections if not any(k in s.slug for k in skip)]
    dry = [s.title for s in ev if not s.links and len(s.body) > 400]
    if dry:
        return False, f"{len(dry)} substantial section(s) with no inline citation: " + \
            "; ".join(t[:40] for t in dry[:2])
    return True, f"{len(d.links)} inline citations across {len(ev)} evidence sections"


def _argument_survives(d: Doc) -> tuple[bool, str]:
    return False, "reviewer judgement — no predicate exists, and none is coming"


def _recommendation_actionable(d: Doc) -> tuple[bool, str]:
    return False, "reviewer judgement — 'more research is needed' passes every rule above"


RULES: list[Rule] = [
    Rule("R1", "Machine-readable front matter", "blocking", "ci",
         "A dispatch pipeline (#24) has to route on ticket, kind and tier without an LLM.",
         _front_matter),
    Rule("R2", "Transcript Archive session id", "blocking", "ci",
         "The archive is private, so the id is the only handle on how the work was done. "
         "`unrecorded` is allowed and is a declaration, not a pass.",
         _session),
    Rule("R3", "Verdict first, and stated", "blocking", "ci",
         "Every one of the four existing documents opens with its answer. The convention "
         "already exists; the contract only has to stop it being optional.",
         _verdict_first),
    Rule("R4", "Every evidence section carries a verdict", "blocking", "ci",
         "This is the per-claim annotation that actually carries information, and it is "
         "what the tier badge cannot be inside an agent-written document.",
         _per_claim_verdicts),
    Rule("R5", "What this does not establish", "blocking", "ci",
         "The survey's most valuable output was a negative result plus a named gap. "
         "Required, not left to a good agent's instincts.",
         _negative_space),
    Rule("R6", "Verification Debt itemised and filed", "blocking", "ci",
         "The survey said its debt was 'logged against the Curriculum'. It was logged "
         "nowhere. An item names its issue or says `unfiled`.",
         _debt_itemised),
    Rule("R7", "No record content in HTML comments", "blocking", "ci",
         "#5 found Mosaic's entire debt load inside comments in CONTEXT.md, invisible in "
         "the rendered file. Cheap to check, and it already fired once.",
         _no_hidden_record),
    Rule("R8", "Proposals section, `None.` if none", "blocking", "ci",
         "Authored files are human-only (§5). Proposals must be collected in one place a "
         "human can apply, not scattered through the argument.",
         _proposals),
    Rule("R9", "Primary-source appendix, all linked", "blocking", "ci",
         "#13 found cited influences that did not survive checking. The appendix is the "
         "list a verifier works down.",
         _appendix_sources),
    Rule("R10", "Volatile sources carry a retrieval date", "advisory", "ci",
         "#27's figures were six weeks old and had already changed twice that year.",
         _volatile_dated),
    Rule("R11", "No inline tier badges", "advisory", "ci",
         "Agent verification is not verification (#5), so every claim here is T3 and a "
         "per-claim badge is noise. The badge belongs at the destination.",
         _no_inline_tier_badges),
    Rule("R12", "Verdict rows name their section", "advisory", "ci",
         "A summary table that cannot be walked back into the argument is a press release.",
         _claims_traceable),
    Rule("R13", "Citations in place, not only in the appendix", "advisory", "ci",
         "The map's standing preference: borrowed frames are cited where they are borrowed.",
         _link_density),
    Rule("R14", "The argument survives an adversarial read", "blocking", "human",
         "No predicate exists. Named so the checklist does not imply CI covers it.",
         _argument_survives),
    Rule("R15", "The recommendation is actionable", "blocking", "human",
         "Same. A document that concludes 'more research is needed' passes every rule above.",
         _recommendation_actionable),
]


def evaluate(doc: Doc, rules: list[Rule] | None = None) -> Report:
    out = []
    for r in rules if rules is not None else RULES:
        if not r.enabled:
            continue
        passed, evidence = r.check(doc)
        out.append(Result(rule=r, passed=passed, evidence=evidence))
    return Report(doc=doc, results=out)


# --------------------------------------------------------------------------------------
# Census helpers — what a document actually contains, independent of the rules. Used to
# check whether a constraint is describing the corpus or inventing a requirement.
# --------------------------------------------------------------------------------------


def census(d: Doc) -> dict[str, object]:
    verdict_counts: dict[str, int] = {}
    for v in RE_VERDICT.findall(d.text):
        verdict_counts[v] = verdict_counts.get(v, 0) + 1
    return {
        "lines": d.text.count("\n") + 1,
        "sections (##)": len(d.top_sections),
        "sections (all)": len(d.sections),
        "inline links": len(d.links),
        "verdict tokens": sum(verdict_counts.values()),
        "verdict spread": verdict_counts,
        "tier badges": len(d.badges),
        "html comments": len(d.comments),
        "front-matter keys": len(d.front),
    }
