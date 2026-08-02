"""
PROTOTYPE (ticket #90) — the Protective Belt graph, in memory, with three
candidate physical stores rendered off one model.

Throwaway. Nothing in the repo reads this and nothing regenerates from it.

The model is #9's, transcribed rather than invented: nodes in three conditions
(conjecture / eligible / belt claim), eligibility held by *legs* carrying kind,
domain and untestable hazards, demotion per-leg, dead branches retained in place,
and a MAJOR demoting the whole belt blanket while the graph survives.

What the prototype is actually for is the three renderers at the bottom —
`as_issues`, `as_files`, `as_hybrid` — and `readings()`, which is the thing the
store has to be able to answer.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from enum import Enum

# --------------------------------------------------------------------------
# Model — #9's, not this prototype's
# --------------------------------------------------------------------------


class Stratum(Enum):
    AXIOM = "axiom"
    BOUND = "bound"
    THESIS = "thesis"


class Condition(Enum):
    CONJECTURE = "conjecture"  # posted, unattached, no warrant
    ELIGIBLE = "eligible"  # has a live leg
    BELT = "belt"  # admitted through PROTOCOL §5's gate


class LegKind(Enum):
    DERIVATION = "derivation"  # closed path of support to the core
    SURVIVAL = "survival"  # put at risk under a named falsifier, and stood


class Relevance(Enum):
    CONNECTIVE = "connective"
    PREDICTIVE = "predictive"
    ELIMINATIVE = "eliminative"
    INTUITION = "intuition"  # declared as intuition on the node, per #9


@dataclass
class Hazard:
    """An *untestable* hazard. Testable ones are Adequacy Criterion clauses and
    never reach the graph — that is #9's whole split."""

    text: str
    source: str  # issue or document that named it
    retroactive: bool = False  # attached after the freeze
    corroboration: str | None = None  # Inquiry opened to answer it


@dataclass
class Leg:
    kind: LegKind
    domain: str  # "ml", "neuro", "synthetic", "mathematics"
    inquiry: str | None  # the Inquiry that earned it; None for derivation
    through: str | None = None  # for derivation legs: the support node id
    hazards: list[Hazard] = field(default_factory=list)
    alive: bool = True
    died: str | None = None  # why, kept in place — nothing is deleted

    @property
    def hazardous(self) -> bool:
        return any(h for h in self.hazards)


@dataclass
class Node:
    id: str
    statement: str
    condition: Condition
    posted_in: str  # issue / commit that posted it
    falsifier: str | None = None  # required to be Inquiry-ready
    relevance: Relevance | None = None  # set at admission
    supports: list[str] = field(default_factory=list)  # ids this node rests on
    bridges_to: str | None = None  # the conjecture this node is bridging toward
    legs: list[Leg] = field(default_factory=list)
    admitted_at: str | None = None  # the MINOR release
    demoted: list[str] = field(default_factory=list)  # audit trail, append-only
    barred: str | None = None  # explicitly barred from admission, with reason

    @property
    def live_legs(self) -> list[Leg]:
        return [leg for leg in self.legs if leg.alive]

    @property
    def dead(self) -> bool:
        """A node that had legs and lost all of them. Retained in place."""
        return bool(self.legs) and not self.live_legs


@dataclass
class CoreMember:
    id: str
    statement: str
    stratum: Stratum


@dataclass
class Release:
    version: str
    kind: str  # "MAJOR" | "MINOR" | "PATCH"
    landed: str  # what it landed, one line
    evidence_for: str | None = None  # PATCH: the node id whose evidence it landed


@dataclass
class Graph:
    core: dict[str, CoreMember] = field(default_factory=dict)
    nodes: dict[str, Node] = field(default_factory=dict)
    releases: list[Release] = field(default_factory=list)
    log: list[str] = field(default_factory=list)
    # The index *as of* each release. This is not bookkeeping — a chart plotted
    # against releases needs the graph as it stood at each tag, which means the
    # store has to be readable at a past revision. Recorded here because the
    # prototype has no git; in Store B it is recomputed by checking out the tag,
    # and in Store A it cannot be obtained at all.
    snapshots: list[tuple[str, float | None]] = field(default_factory=list)

    def snapshot(self) -> None:
        if self.releases:
            self.snapshots.append((self.releases[-1].version, self.index()))

    # -- growth ----------------------------------------------------------

    def post(self, node: Node) -> None:
        self.nodes[node.id] = node
        self.log.append(f"posted conjecture {node.id}")

    def earn(self, node_id: str, leg: Leg) -> None:
        node = self.nodes[node_id]
        node.legs.append(leg)
        if node.condition is Condition.CONJECTURE:
            node.condition = Condition.ELIGIBLE
        self.log.append(f"{node_id} earned a {leg.kind.value} leg in {leg.domain}")

    def admit(self, node_id: str, relevance: Relevance, version: str) -> str:
        """PROTOCOL §5's gate, fired per node. The impedance boundary."""
        node = self.nodes[node_id]
        if node.barred:
            return f"REFUSED — {node.id} is barred: {node.barred}"
        if node.condition is not Condition.ELIGIBLE:
            return f"REFUSED — {node.id} is {node.condition.value}, not eligible"
        if not node.live_legs:
            return f"REFUSED — {node.id} has no live leg"
        node.condition = Condition.BELT
        node.relevance = relevance
        node.admitted_at = version
        self.releases.append(
            Release(version, "MINOR", f"admit {node.id} ({relevance.value})")
        )
        self.log.append(f"ADMITTED {node_id} at {version} — {relevance.value}")
        self.snapshot()
        return f"admitted {node.id} as {relevance.value} at {version}"

    # -- exit ------------------------------------------------------------

    def kill_leg(self, node_id: str, index: int, why: str) -> str:
        """Per-leg demotion. A node falls only on losing its last leg."""
        node = self.nodes[node_id]
        leg = node.legs[index]
        leg.alive = False
        leg.died = why
        node.demoted.append(f"{leg.kind.value} leg ({leg.domain}) died: {why}")
        if node.live_legs:
            return (
                f"{node.id} lost its {leg.kind.value} leg — still held by "
                f"{len(node.live_legs)} live leg(s); condition unchanged"
            )
        was = node.condition
        node.condition = Condition.CONJECTURE
        self.log.append(f"{node_id} demoted to conjecture (last leg lost)")
        return f"{node.id} lost its LAST leg — {was.value} → conjecture (belt: MINOR)"

    def major(self, version: str, what: str) -> str:
        """A Hard Core revision demotes EVERY belt claim to conjecture, blanket.
        The graph survives entire — that is what makes the rebuild affordable."""
        hit = [n for n in self.nodes.values() if n.condition is Condition.BELT]
        for node in hit:
            node.condition = Condition.CONJECTURE
            node.demoted.append(f"blanket demotion at {version} ({what})")
            node.relevance = None
        self.releases.append(Release(version, "MAJOR", f"core revision: {what}"))
        self.log.append(f"MAJOR {version} — blanket demotion of {len(hit)} claims")
        self.snapshot()
        legs = sum(len(n.legs) for n in self.nodes.values())
        return (
            f"{len(hit)} belt claim(s) demoted to conjecture. "
            f"{len(self.nodes)} nodes and {legs} legs retained in place — "
            f"re-earning is a re-validation, not a re-run."
        )

    def attach_hazard(self, node_id: str, index: int, hazard: Hazard) -> str:
        """A late untestable hazard never retires the claim; it obliges a
        corroboration Inquiry, which only Noah may open."""
        node = self.nodes[node_id]
        node.legs[index].hazards.append(hazard)
        note = f"retroactive hazard on {node.id} leg {index}: {hazard.text}"
        self.log.append(note)
        if node.condition is Condition.BELT:
            return note + " — claim STANDS; corroboration Inquiry owed (Noah opens it)"
        return note

    # -- the five readings ------------------------------------------------

    def readings(self) -> dict[str, object]:
        """#9's five, all ratios or shapes, never counts. #88 owns the formula;
        this exists only to show the numbers are reachable off the store."""
        belt = [n for n in self.nodes.values() if n.condition is Condition.BELT]
        posted = [n for n in self.nodes.values() if n.bridges_to is None]
        bridged = [n for n in posted if self._has_path_to_core(n.id)]
        survival = [
            leg
            for n in self.nodes.values()
            for leg in n.legs
            if leg.kind is LegKind.SURVIVAL and leg.alive
        ]
        hazardous = [leg for leg in survival if leg.hazardous]
        inert = [n for n in belt if not self._downstream_live_conjecture(n.id)]
        predictive = [n for n in belt if n.relevance is Relevance.PREDICTIVE]
        connective = [n for n in belt if n.relevance is Relevance.CONNECTIVE]

        return {
            "predictive_to_connective": _ratio(len(predictive), len(connective)),
            "bridged_over_posted": _ratio(len(bridged), len(posted)),
            "inert_share": _ratio(len(inert), len(belt)),
            "hazarded_leg_share": _ratio(len(hazardous), len(survival)),
            "release_shape": self._release_shape(),
        }

    def _has_path_to_core(self, node_id: str) -> bool:
        seen, stack = set(), [node_id]
        while stack:
            cur = stack.pop()
            if cur in self.core:
                return True
            if cur in seen or cur not in self.nodes:
                continue
            seen.add(cur)
            node = self.nodes[cur]
            stack.extend(node.supports)
            stack.extend(
                leg.through
                for leg in node.live_legs
                if leg.kind is LegKind.DERIVATION and leg.through
            )
        return False

    def _downstream_live_conjecture(self, node_id: str) -> bool:
        for other in self.nodes.values():
            if node_id in other.supports and other.condition is Condition.CONJECTURE:
                return True
        return False

    def _release_shape(self) -> float | None:
        """Two-sided by design: PATCH with no MINOR is evidence going nowhere;
        MINOR with no PATCH underneath is ad hoc absorption."""
        minors = [r for r in self.releases if r.kind == "MINOR"]
        patches = [r for r in self.releases if r.kind == "PATCH"]
        if not minors and not patches:
            return None
        supported = 0
        for minor in minors:
            i = self.releases.index(minor)
            prior = [
                r for r in self.releases[:i] if r.kind == "PATCH" and r.evidence_for
            ]
            if any(p.evidence_for and p.evidence_for in minor.landed for p in prior):
                supported += 1
        if not minors:
            return -1.0  # accumulating evidence, committing to nothing
        if not patches:
            return -1.0  # commitments with nothing underneath
        return round(2 * (supported / len(minors)) - 1, 3)

    def index(self) -> float | None:
        """A single number on [-1, +1]. #88 owns the real weighting — this one is
        a flat mean, deliberately naive, so nobody mistakes it for the formula."""
        vals = [v for v in self.readings().values() if isinstance(v, float)]
        return round(sum(vals) / len(vals), 3) if vals else None


def _ratio(a: int, b: int) -> float | None:
    """On [-1, +1]. None where the denominator is empty — an honest 'no reading'
    rather than a zero, which would read as a verdict."""
    if a + b == 0:
        return None
    return round(2 * (a / (a + b)) - 1, 3)


# --------------------------------------------------------------------------
# Store A — the issue tracker, extending #5's ruling to the graph
# --------------------------------------------------------------------------


def as_issues(g: Graph) -> str:
    """One issue per node, condition as a label, support edges as GitHub's native
    dependency relationship. Rendered as the API calls it would actually take."""
    out: list[str] = []
    out.append("# Store A — issues + native dependency edges\n")
    for node in g.nodes.values():
        label = f"belt:{node.condition.value}"
        out.append(f"gh issue create --title {node.statement[:48]!r} --label {label!r}")
        for support in node.supports:
            out.append(
                f"  gh api -X POST repos/:o/:r/issues/<{node.id}>/dependencies/"
                f"blocked_by -F issue_id=<{support}>   # 'blocked by' ≠ 'rests on'"
            )
        for i, leg in enumerate(node.legs):
            out.append(
                f"  # leg {i}: {leg.kind.value}/{leg.domain} — no field for this; "
                f"goes in the body as YAML anyway"
            )
    out.append("")
    out.append(f"# blanket demotion = {len(g.nodes)} label edits, non-atomic, no diff")
    out.append("# chart build = N API calls at build time, rate-limited, undiffable")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Store B — committed files, custody split at the file boundary
# --------------------------------------------------------------------------


def as_files(g: Graph) -> str:
    """`belt/nodes/<id>.md` is Noah's hand: statement, falsifier, relevance.
    `belt/legs/<id>.jsonl` is the agents' hand: append-only, one leg per line.

    The split is the point. PROTOCOL §5 splits custody by *file*, so putting the
    machine-rate half in its own file makes the impedance boundary a path in the
    tree rather than a convention inside a document."""
    out: list[str] = []
    out.append("# Store B — committed files, custody split at the file boundary\n")
    for node in g.nodes.values():
        out.append(f"── belt/nodes/{node.id}.md " + "─" * max(0, 46 - len(node.id)))
        out.append("---")
        out.append(f"condition: {node.condition.value}")
        out.append(f"posted_in: {node.posted_in}")
        if node.falsifier:
            out.append(f"falsifier: {node.falsifier!r}")
        if node.relevance:
            out.append(f"relevance: {node.relevance.value}")
        if node.admitted_at:
            out.append(f"admitted_at: {node.admitted_at}")
        if node.supports:
            out.append(f"supports: {node.supports}")
        if node.bridges_to:
            out.append(f"bridges_to: {node.bridges_to}")
        if node.barred:
            out.append(f"barred: {node.barred!r}")
        out.append("---")
        out.append(node.statement)
        if node.demoted:
            out.append("")
            out.append("<!-- retained in place, nothing deleted:")
            for line in node.demoted:
                out.append(f"     - {line}")
            out.append("-->")
        if node.legs:
            out.append("")
            out.append(f"── belt/legs/{node.id}.jsonl (agent-written, append-only) ──")
            for leg in node.legs:
                out.append(
                    json.dumps(
                        {
                            "kind": leg.kind.value,
                            "domain": leg.domain,
                            "inquiry": leg.inquiry,
                            "through": leg.through,
                            "hazards": [
                                {
                                    "text": h.text,
                                    "source": h.source,
                                    "retroactive": h.retroactive,
                                }
                                for h in leg.hazards
                            ],
                            "alive": leg.alive,
                            "died": leg.died,
                        }
                    )
                )
        out.append("")
    out.append("# blanket demotion = one commit touching N files, atomic, reviewable")
    out.append("# chart build = read the tree at a tag; offline, deterministic")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Store C — hybrid: files canonical, an issue minted per belt claim
# --------------------------------------------------------------------------


def as_hybrid(g: Graph) -> str:
    out: list[str] = []
    out.append("# Store C — files canonical; issues minted only where §5 fires\n")
    out.append("Files exactly as Store B, plus:\n")
    for node in g.nodes.values():
        if node.condition is Condition.BELT:
            out.append(
                f"  gh issue create --label 'belt:gate' "
                f"--title 'Gate: {node.statement[:40]}'   # the grilling lives here"
            )
        elif node.condition is Condition.ELIGIBLE:
            out.append(f"  (no issue — {node.id} is eligible, nothing to discuss yet)")
    out.append("")
    out.append("# the issue is the *conversation* about admission, not the record")
    out.append("# of the claim — generated from the file, never the other way round")
    return "\n".join(out)


# --------------------------------------------------------------------------
# The chart — a build artifact rendered into README.md, unconditionally
# --------------------------------------------------------------------------

BLOCKS = "▁▂▃▄▅▆▇█"


def chart(g: Graph, history: list[tuple[str, float | None]]) -> str:
    """Plotted against releases, never wall-clock. A quiet month is not a stalled
    one. Generated whether or not the number flatters the programme."""
    lines = ["```", "Programme health — index on [-1, +1], against releases", ""]
    if not history:
        lines += ["  (no reading yet — the belt is empty)", "```"]
        return "\n".join(lines)
    spark = "".join(
        " " if v is None else BLOCKS[min(7, int((v + 1) / 2 * 7.999))]
        for _, v in history
    )
    lines.append(f"  +1 │ {spark}")
    lines.append(f"  -1 └{'─' * (len(spark) + 1)}")
    lines.append("     " + f"{history[0][0]} → {history[-1][0]}")
    lines.append("")
    for name, value in g.readings().items():
        bar = "  no reading" if value is None else _bar(value)
        shown = "—" if value is None else f"{value:+.2f}"
        lines.append(f"  {name:<26} {shown:>6}  {bar}")
    idx = g.index()
    lines.append("")
    lines.append(f"  {'INDEX':<26} {'—' if idx is None else f'{idx:+.2f}':>6}")
    lines.append("```")
    return "\n".join(lines)


def _bar(value: float) -> str:
    slot = int((value + 1) / 2 * 20)
    return "[" + "·" * slot + "●" + "·" * (20 - slot) + "]"


# --------------------------------------------------------------------------
# Seed — the programme's actual graph as of #17, not invented content
# --------------------------------------------------------------------------


def seed() -> Graph:
    g = Graph()
    for cid, statement, stratum in [
        ("core.least-action", "Least Action", Stratum.AXIOM),
        ("core.scale-corollary", "The Scale Corollary", Stratum.AXIOM),
        ("core.structural-realisation", "Structural Realisation", Stratum.AXIOM),
        ("core.inference", "The inference perspective", Stratum.BOUND),
        ("core.dynamical", "Dynamical-systems modelability", Stratum.BOUND),
        ("core.edge-of-chaos", "The Edge of Chaos", Stratum.BOUND),
        ("core.single-scale", "Single-scale evaluation", Stratum.BOUND),
        ("core.window", "The computational window", Stratum.BOUND),
        ("core.schema-thesis", "The schema thesis", Stratum.THESIS),
        ("core.bridge", "The cross-field bridge", Stratum.THESIS),
    ]:
        g.core[cid] = CoreMember(cid, statement, stratum)

    # Every real node the record has posted. The honest census: the belt is
    # empty, and no node has a leg — the first Inquiry has not run.
    g.post(
        Node(
            "obstruction-useful",
            "Cognitive systems have to do something useful with Obstruction.",
            Condition.CONJECTURE,
            posted_in="#9",
        )
    )
    g.post(
        Node(
            "reconciliation-not-voting",
            "Schemas reconcile rather than vote — the surviving content "
            "objection to Thousand Brains.",
            Condition.CONJECTURE,
            posted_in="#16",
            barred="distinguishes Mosaic from someone else's theory (#16)",
        )
    )
    g.post(
        Node(
            "scaling-thesis",
            "Scaling increases Extraction and not Closure; bounded bandwidth "
            "between subsystems forces closure structurally.",
            Condition.CONJECTURE,
            posted_in="#15",
        )
    )
    g.post(
        Node(
            "single-level",
            "Cognition concentrates at a single level.",
            Condition.CONJECTURE,
            posted_in="#6 → #7",
        )
    )
    g.post(
        Node(
            "rules-invariances",
            "Rules ≡ invariances ≡ compressions.",
            Condition.CONJECTURE,
            posted_in="#6 → #7",
        )
    )
    g.post(
        Node(
            "individuation",
            "A system's schemas can be recovered from its data non-arbitrarily.",
            Condition.CONJECTURE,
            posted_in="#17",
            falsifier="Recovered schema sets are unstable across seeds and "
            "hyperparameters at matched ground truth.",
        )
    )
    g.releases += [
        Release("0.4.0", "PATCH", "record: land the delegated-inquiry vocabulary"),
        Release("0.5.0", "PATCH", "record: name the first Inquiry (#17)"),
    ]
    return g


def config_sha(g: Graph) -> str:
    """Only here so the TUI can show that a file store is content-addressable and
    an issue store is not."""
    payload = json.dumps(
        {n.id: n.condition.value for n in sorted(g.nodes.values(), key=lambda x: x.id)},
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode()).hexdigest()[:12]
