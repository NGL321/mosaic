"""
PROTOTYPE (ticket #5) — the portable bit.

QUESTION BEING PROTOTYPED
-------------------------
What is the physical form of Mosaic's record: how a Provenance Tier attaches to a
claim, where Verification Debt is written down, and what tree they live in?

The prototype's premise is that this is NOT a greenfield question. The practice
already exists in the repository, in three mutually incompatible forms, none of
which any tool can read:

  1. CONTEXT.md lines 171-172 and 232-245 — tiers and debt as HTML comments.
     Invisible to a reader of the rendered file. This is where Mosaic's entire
     current debt load actually lives.
  2. docs/research/2026-07-28-*.md — a bold-key header block with the tier as a
     prose paragraph. Visible, human-readable, unparseable.
  3. Nowhere — there is no ledger file, and CONTEXT.md's Curriculum entry says
     debt is "logged against the Curriculum", which does not exist either.

So the five debt items below are real, are load-bearing, and are currently
retrievable only by reading an HTML comment in the middle of a 252-line file.

THE AXIS THAT MATTERS
---------------------
Not notation. The load-bearing choice is *where the truth lives*, because that
decides what can go stale:

  A  ANNOTATION-PRIMARY  truth at the claim site; the ledger is generated.
                         Cannot drift. Costs a build step and a scanner.
  B  LEDGER-PRIMARY      truth in ledger/; the claim carries an id reference.
                         Queryable by hand. Two places, so it can drift.
  C  TRACKER-PRIMARY     truth is a GitHub issue; the claim carries #n.
                         Zero new machinery. Leaves the repo incomplete alone.

Each is rendered below over the same real data, so the comparison is concrete
rather than architectural.

Drive it with prototype_tui.py. Nothing here is written anywhere.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


# ---------------------------------------------------------------------------
# Tier vocabulary
# ---------------------------------------------------------------------------


class Tier(Enum):
    """
    The three tiers CONTEXT.md defines, plus the one the record already needs.

    CONTEXT.md's *Provenance Tier* entry names exactly three. Within four days of
    that definition landing, CONTEXT.md line 232 wrote a fourth by hand:

        "Provenance Tier: machine-produced, checked against primary sources."

    That is not T3 (it was checked) and not T2 (Noah did not verify it — an agent
    did, in #13). The vocabulary was under-specified on contact with its first
    real case. Whether T2_AGENT is a genuine tier or a defect to be collapsed is
    the first thing this prototype wants an answer on.
    """

    T1_UNAIDED = ("T1", "derived unaided", "Noah reached it without assistance")
    T2_VERIFIED = ("T2", "assisted, personally verified", "agent-assisted; Noah checked it himself")
    T2_AGENT = ("T2*", "agent-verified against primary sources", "a *different* agent read the sources back")
    T3_UNVERIFIED = ("T3", "machine-produced, unverified", "no one has checked it")

    def __init__(self, code: str, label: str, gloss: str) -> None:
        self.code = code
        self.label = label
        self.gloss = gloss


# ---------------------------------------------------------------------------
# Real data, lifted verbatim from the repository as it stands today
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Claim:
    """A real claim in the current record that carries (or needs) a tier."""

    site: str  # file:line where it lives
    term: str  # the vocabulary entry it belongs to
    text: str  # the claim, abbreviated
    tier: Tier
    debt: tuple[str, ...] = ()  # ids of debt blocking a tier promotion
    current_form: str = ""  # how it is written down TODAY


@dataclass(frozen=True)
class Debt:
    """
    A real Verification Debt item. Every one of these is currently logged only
    inside an HTML comment in CONTEXT.md.
    """

    id: str
    what: str  # the step Noah cannot yet defend unaided
    blocks: tuple[str, ...]  # which terms/claims it holds down
    discharge: str  # what discharging it actually requires
    curriculum: str  # the learning it schedules
    source: str  # where it is written down today


DEBT: tuple[Debt, ...] = (
    Debt(
        id="VD-001",
        what="Mountcastle (1957; 1978) has not been read in the original.",
        blocks=("Schema Dynamics",),
        discharge="Read both; confirm Mountcastle offered columnar organisation as an "
        "organising principle rather than a result, which is what the hedge claims.",
        curriculum="Cortical neuroanatomy — primary literature",
        source="CONTEXT.md:242 (HTML comment)",
    ),
    Debt(
        id="VD-002",
        what="Piaget's 1929 Limnaea paper was not reached; the malacology work's "
        "relation to his thesis is unresolved.",
        blocks=("Schema",),
        discharge="Obtain the 1929 paper. Resolve whether the mollusc work was the thesis.",
        curriculum="History of developmental psychology — primary sources, French",
        source="CONTEXT.md:243 (HTML comment); research doc §11 item 2",
    ),
    Debt(
        id="VD-003",
        what="Piaget's own distinct use of *schéma* (as against *schème*) is "
        "unconfirmed from primary French.",
        blocks=("Schema",),
        discharge="Read Piaget in French; establish whether he draws the distinction "
        "the _Departs_ line relies on.",
        curriculum="Reading French primary sources",
        source="CONTEXT.md:244 (HTML comment)",
    ),
    Debt(
        id="VD-004",
        what="The derivation of Still et al. (2012) Eq. (14), and its no-feedback "
        "assumption, is not defensible unaided.",
        blocks=("Least Action", "Representation"),
        discharge="Rederive Eq. (14) from the paper; state where the no-feedback "
        "assumption enters and what it costs Mosaic if it fails.",
        curriculum="Stochastic thermodynamics; nonequilibrium statistical mechanics",
        source="CONTEXT.md:245 (HTML comment)",
    ),
    Debt(
        id="VD-005",
        what="Legg & Hutter, Chollet, Bertschinger et al., and Kemeny & Snell are "
        "cited from recall, not from warrant.",
        blocks=("Extraction", "Closure"),
        discharge="Read each; confirm the departures claimed against them are real. "
        "This is the same job #13 did for the other half of the file.",
        curriculum="Information theory; Markov chain lumpability",
        source="CONTEXT.md:171-172 (HTML comment)",
    ),
)


CLAIMS: tuple[Claim, ...] = (
    Claim(
        site="CONTEXT.md:106",
        term="Extraction",
        text="Achieved predictive information as a fraction of the ceiling set by the "
        "observed process — a ratio, so it compares across environments.",
        tier=Tier.T3_UNVERIFIED,
        debt=("VD-005",),
        current_form="<!-- Provenance Tier for Extraction and Closure: machine-produced, unverified. -->",
    ),
    Claim(
        site="CONTEXT.md:150",
        term="Closure",
        text="How much of the environment's influence on a schema's observations is "
        "accounted for by those observations. Graded, not binary.",
        tier=Tier.T3_UNVERIFIED,
        debt=("VD-005",),
        current_form="<!-- (same comment as Extraction, 20 lines away) -->",
    ),
    Claim(
        site="CONTEXT.md:221",
        term="Least Action",
        text="Information transformation is thermodynamic, so inference is subject to "
        "a variational principle. Held as Hard Core by disciplinary declaration.",
        tier=Tier.T2_AGENT,
        debt=("VD-004",),
        current_form="<!-- Provenance Tier: machine-produced, checked against primary sources. -->",
    ),
    Claim(
        site="CONTEXT.md:201",
        term="Schema Dynamics",
        text="General cognitive capacity is a property of the relations between "
        "schemas rather than of any single engine.",
        tier=Tier.T2_AGENT,
        debt=("VD-001",),
        current_form="<!-- (covered by the same block comment at :232) -->",
    ),
    Claim(
        site="CONTEXT.md:135",
        term="Schema",
        text="A coherent set of representations carrying its own metric space; "
        "schemas addressing different problems are not commensurable by default.",
        tier=Tier.T2_AGENT,
        debt=("VD-002", "VD-003"),
        current_form="<!-- (covered by the same block comment at :232) -->",
    ),
)


# ---------------------------------------------------------------------------
# The shared tree spine — identical across all three schemes
# ---------------------------------------------------------------------------

SPINE = """\
mosaic/
├── README.md                        entry point                    · tooling
├── CHARTER.md                       the founding charter (#12)     · AUTHORED
├── CONTEXT.md                       vocabulary                     · AUTHORED
├── PROTOCOL.md                      working protocol               · tooling
├── LICENSE
├── docs/
│   ├── SYSTEM-BRIEF.md              Drive-first storage protocol   · ⚠ MISSING
│   ├── adr/
│   │   ├── README.md
│   │   └── 0001-private-transcript-archive.md            (#10)
│   ├── research/                    EVIDENCE layer  (#26 governs the format)
│   │   └── 2026-07-28-verifying-cited-influences.md
│   └── prototypes/                  throwaway; explicitly NOT the record
│       ├── custody-predicate/                            (#23)
│       └── record-form/                                  (#5, this)
├── notebook/                        NARRATIVE layer (#11 governs)
│   ├── README.md                    how to read a generated vs annotated entry
│   └── 2026-07-28-vocabulary-lands.md
├── experiments/                     RESEARCH TRACK — silent change falsifies results
│   └── 001-eca-grokking/
│       ├── README.md                the claim this serves, and its falsifier
│       ├── config.yaml              seeds + config live here
│       ├── src/
│       └── runs/
│           └── 2026-08-04-a3f1.md   MANIFEST ONLY — sha256 + Drive pointer;
│                                    bytes live at Desk/mosaic/runs/<run-id>/
├── curriculum/
│   ├── README.md                    scheduled off debt, never off a syllabus
│   └── open.md
└── """


@dataclass
class Scheme:
    key: str
    name: str
    thesis: str
    truth_lives: str
    tree_tail: str
    claim_render: str
    ledger_render: str
    costs: tuple[str, ...] = field(default_factory=tuple)
    buys: tuple[str, ...] = field(default_factory=tuple)
    kills_it: str = ""


def _fmt_debt_b(d: Debt) -> str:
    return f"""\
---
id: {d.id}
status: open
blocks: [{", ".join(d.blocks)}]
curriculum: {d.curriculum}
opened: 2026-07-28
---

# {d.id} — {d.what}

**Discharged by.** {d.discharge}

**Evidence required.** A note in `docs/research/` that does the reading, plus the
edit to the claim site promoting its tier. Discharge is not a checkbox; it lands
a document or it did not happen."""


SCHEME_A = Scheme(
    key="A",
    name="ANNOTATION-PRIMARY",
    thesis="The claim site is the only source of truth. The ledger is a build artifact.",
    truth_lives="At the claim, in visible markup.",
    tree_tail="""ledger/
    ├── README.md                    "DO NOT EDIT debt.md — it is generated"
    └── debt.md                      ⚙ GENERATED by tools/scan-debt.py""",
    claim_render="""\
**Extraction**:                                                    `⟦T3⟧`
How much of the predictive structure available in what an engine observes the
engine actually captures — its achieved predictive information as a fraction of
the ceiling set by the observed process itself.

> **⚠ Verification Debt — VD-005.** Legg & Hutter, Chollet, Bertschinger et al.
> and Kemeny & Snell are cited from recall, not warrant.
> *Discharged by:* reading each, and confirming the claimed departures are real.
> *Curriculum:* information theory; Markov chain lumpability.""",
    ledger_render="""\
<!-- GENERATED by tools/scan-debt.py — do not edit. Source of truth is the claim site. -->

# Verification Debt — 5 open, 0 discharged

| id | blocks | what | curriculum |
|---|---|---|---|
| VD-001 | Schema Dynamics | Mountcastle not read in original | Cortical neuroanatomy |
| VD-002 | Schema | Piaget 1929 Limnaea unreached | Hist. dev. psych (French) |
| VD-003 | Schema | *schéma* vs *schème* unconfirmed | Reading French primaries |
| VD-004 | Least Action, Representation | Still Eq. (14) not defensible | Stochastic thermo |
| VD-005 | Extraction, Closure | four citations from recall | Info theory; lumpability |

## Tier census
T1 unaided 0 · T2 verified 0 · T2* agent-verified 3 · T3 unverified 2""",
    buys=(
        "Cannot drift. There is one place to write it, and it is the place a reader is already looking.",
        "The debt is visible in the rendered file — which is the single biggest change from today, where it is an HTML comment.",
        "A tier promotion is a one-line diff at the claim, and the ledger updates itself.",
    ),
    costs=(
        "Needs a scanner and a CI check that the generated file is current. That is real tooling, and it is tooling before the first experiment.",
        "Long debt callouts interrupt CONTEXT.md, which is currently a clean read.",
    ),
    kills_it="If the callouts make CONTEXT.md unreadable, Noah will stop writing them.",
)

SCHEME_B = Scheme(
    key="B",
    name="LEDGER-PRIMARY",
    thesis="ledger/ is the source of truth. The claim carries a reference to it.",
    truth_lives="In ledger/debt/, one file per item.",
    tree_tail="""ledger/
    ├── README.md
    ├── tiers.md                     the tier vocabulary, normative
    └── debt/
        ├── VD-001-mountcastle-primary.md
        ├── VD-002-piaget-limnaea.md
        ├── VD-003-schema-schème.md
        ├── VD-004-still-eq14.md
        └── VD-005-extraction-citations.md""",
    claim_render="""\
**Extraction**:                                              `⟦T3 · VD-005⟧`
How much of the predictive structure available in what an engine observes the
engine actually captures — its achieved predictive information as a fraction of
the ceiling set by the observed process itself.

  (the claim site says nothing more; VD-005 is a link into ledger/debt/)""",
    ledger_render=_fmt_debt_b(DEBT[4]),
    buys=(
        "Debt is a first-class document with room to grow — evidence, partial progress, a reading list.",
        "The Curriculum can be assembled by listing a directory, which is exactly what CONTEXT.md promises.",
        "CONTEXT.md stays a clean read.",
    ),
    costs=(
        "Two places. A tier promoted at the claim and not in the ledger is a silent lie, and nothing detects it without the same CI check scheme A needs anyway.",
        "`⟦T3 · VD-005⟧` tells a reader nothing without a second file open.",
    ),
    kills_it="The first time the ledger and the claim disagree, the ledger stops being believed.",
)

SCHEME_C = Scheme(
    key="C",
    name="TRACKER-PRIMARY",
    thesis="Debt is an issue. The repo carries no ledger at all.",
    truth_lives="On the GitHub issue tracker, labelled `debt:open`.",
    tree_tail="""(no ledger/ directory)

    Debt is issues labelled `debt:open` / `debt:discharged`.
    The Curriculum is a milestone. `curriculum/open.md` is generated
    from the tracker, or omitted entirely.""",
    claim_render="""\
**Extraction**:                                                `⟦T3 · #31⟧`
How much of the predictive structure available in what an engine observes the
engine actually captures — its achieved predictive information as a fraction of
the ceiling set by the observed process itself.""",
    ledger_render="""\
gh issue list --label debt:open

#31  [debt] Extraction/Closure citations are recall, not warrant   blocks: Extraction, Closure
#32  [debt] Mountcastle (1957; 1978) not read in original          blocks: Schema Dynamics
#33  [debt] Piaget 1929 Limnaea unreached                          blocks: Schema
#34  [debt] schéma vs schème unconfirmed from French               blocks: Schema
#35  [debt] Still et al. Eq. (14) not defensible unaided           blocks: Least Action

  Discharge = close the issue, citing the SHA that promoted the tier.
  Wayfinder already lives here; blocking edges are native; #24's pipeline
  already has to read and write issues.""",
    buys=(
        "Zero new machinery, and it reuses the one system Noah has already proved he keeps current — the tracker has 27 issues and a wired dependency graph.",
        "Debt gets threaded discussion, native blocking against the tickets it holds down, and assignment, for free.",
        "It is the only scheme with no drift surface inside the repo, because there is nothing in the repo to drift.",
    ),
    costs=(
        "A clone of the repository no longer contains the programme's debt. For a project whose entire pitch is an auditable public record, that is a real amputation.",
        "The tracker is not versioned. `git log` cannot show what the programme owed in March.",
        "Tiers still need somewhere to live, so this is only half a scheme.",
    ),
    kills_it="The first time someone asks 'what did the programme not know when it wrote this?' and the answer needs an API call.",
)

SCHEMES: tuple[Scheme, ...] = (SCHEME_A, SCHEME_B, SCHEME_C)


def tree_for(s: Scheme) -> str:
    return SPINE + s.tree_tail
