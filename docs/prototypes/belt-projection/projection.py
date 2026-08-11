"""
PROTOTYPE (ticket #90) — the Protective Belt graph as a PROJECTION.

Throwaway. Nothing in the repo reads this and nothing regenerates from it.

The claim under test, decided by grilling on #90: **the belt graph has no store of its
own.** It is computed from three trees that already exist —

    conjectures/NNN-slug/README.md   the nodes           (#164)
    inquiries/NNN-slug/README.md     the edges + legs    (#60)
    CHARTER.md                       the admitted rungs  (PROTOCOL §5)

— plus exactly one record none of them can derive: `inquiries/NNN-slug/axiom.md`, the
append-only ledger of one axiom's life (carried, hazarded late, retracted).

This file is the projection. `prototype_tui.py` drives it with injectable events.

Read `README.md` beside this for what it found.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

import yaml

FIXTURE = Path(__file__).parent / "fixture"


# --------------------------------------------------------------------------
# Reading the trees
# --------------------------------------------------------------------------


def _frontmatter(path: Path) -> dict:
    """`---` block at the top of a README. The charter uses a fenced block instead,
    because it is prose a human reads first; both are just YAML."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        return yaml.safe_load(text.split("---", 2)[1]) or {}
    fenced = re.search(r"```yaml\n(.*?)```", text, re.S)
    return yaml.safe_load(fenced.group(1)) if fenced else {}


# --------------------------------------------------------------------------
# Model — everything below is DERIVED. Only `axiom.md` is stored.
# --------------------------------------------------------------------------


class Condition(Enum):
    CONJECTURE = "conjecture"
    ELIGIBLE = "eligible"
    BELT = "belt"


class LegKind(Enum):
    SURVIVAL = "survival"  # an Inquiry's axiom carried
    DERIVATION = "derivation"  # #163's proof bridging — no source exists yet


@dataclass
class Leg:
    """Not stored anywhere. A leg IS the pair (Inquiry, Conjecture) once the Inquiry's
    axiom has carried. Kind, domain, axiom text and declared hazards all come from the
    Inquiry's frozen charter; liveness comes from its axiom ledger."""

    inquiry: str
    conjecture: str
    kind: LegKind
    domain: str
    axiom: str
    hazards: list[str]  # declared (charter) + late (ledger)
    alive: bool
    died: str | None = None
    route: str | None = None  # "rule-dictated" | "discretionary"

    @property
    def hazardous(self) -> bool:
        return bool(self.hazards)


@dataclass
class Node:
    id: str
    statement: str
    legs: list[Leg] = field(default_factory=list)
    rung: dict | None = None  # the CHARTER.md entry, if admitted
    barred: str | None = None

    @property
    def live_legs(self) -> list[Leg]:
        return [leg for leg in self.legs if leg.alive]

    @property
    def condition(self) -> Condition:
        """DERIVED, and #62 owns the last word on it — see README finding 3."""
        if self.rung:
            return Condition.BELT
        return Condition.ELIGIBLE if self.live_legs else Condition.CONJECTURE

    @property
    def dead(self) -> bool:
        """Had legs, lost all of them. Retained in place — nothing is deleted."""
        return bool(self.legs) and not self.live_legs


@dataclass
class Projection:
    nodes: dict[str, Node]
    inquiries: dict[str, dict]
    releases: list[str]

    # -- the five readings ------------------------------------------------

    def readings(self) -> dict[str, Reading]:
        belt = [n for n in self.nodes.values() if n.rung]
        posted = list(self.nodes.values())
        legs = [leg for n in self.nodes.values() for leg in n.legs if leg.alive]

        predictive = [n for n in belt if n.rung["relevance"] == "predictive"]
        connective = [n for n in belt if n.rung["relevance"] == "connective"]
        inert = [n for n in belt if not self._downstream_live_conjecture(n.id)]
        hazarded = [leg for leg in legs if leg.hazardous]

        return {
            "predictive_to_connective": _ratio(len(predictive), len(connective)),
            "bridged_over_posted": Reading.unreachable(
                "needs the open gap; #165 has not built it. Graph reachability "
                "cannot answer it — #164 makes the whole core and belt inherited "
                "premises of every conjecture, so every node is trivially bridged."
            ),
            "inert_share": _ratio(len(inert), len(belt) - len(inert)),
            "hazarded_leg_share": _ratio(len(hazarded), len(legs) - len(hazarded)),
            "release_shape": Reading.unreachable(
                "needs each MINOR matched to the evidence: PATCHes underneath it; "
                "no declared way for an evidence: commit to name its rung (#82)."
            ),
        }

    def _downstream_live_conjecture(self, node_id: str) -> bool:
        """An admitted claim is *inert* if nothing live still rests on it. Reachable
        off the trees: a live conjecture rests on a rung when an Inquiry serving it
        also serves the rung's conjecture."""
        for other in self.nodes.values():
            if other.id == node_id or other.rung:
                continue
            if not other.live_legs:
                continue
            for leg in other.live_legs:
                served = self.inquiries[leg.inquiry]["conjectures"]
                if any(node_id.endswith(Path(c).name) for c in served):
                    return True
        return False

    def index(self) -> float | None:
        vals = [r.value for r in self.readings().values() if r.value is not None]
        return round(sum(vals) / len(vals), 3) if vals else None


@dataclass
class Reading:
    """Three-valued, and the third value is the point. #88 inherits this distinction.

    - a number
    - NO READING — the denominator is empty. Honest silence about a real question.
    - UNREACHABLE — the question cannot be computed off the store at all, and says
      which ticket owes the mechanism. An unreachable reading must never be allowed
      to read as a no-reading, or a missing instrument looks like a quiet programme.
    """

    value: float | None
    blocked: str | None = None

    @classmethod
    def unreachable(cls, why: str) -> Reading:
        return cls(None, why)

    def __str__(self) -> str:
        if self.value is not None:
            return f"{self.value:+.2f}"
        return "unreachable" if self.blocked else "no reading"


def _ratio(a: int, b: int) -> Reading:
    if a + b == 0:
        return Reading(None)
    return Reading(round(2 * (a / (a + b)) - 1, 3))


# --------------------------------------------------------------------------
# Building the projection
# --------------------------------------------------------------------------


def build(root: Path = FIXTURE, ledgers: dict[str, list] | None = None) -> Projection:
    """Read three trees, compute the graph. `ledgers` lets the TUI inject axiom.md
    events without writing files — in the real thing they are committed."""
    charter = _frontmatter(root / "CHARTER.md")
    rungs = {r["from_conjecture"]: r for r in charter.get("rungs", [])}

    nodes: dict[str, Node] = {}
    for path in sorted((root / "conjectures").iterdir()):
        meta = _frontmatter(path / "README.md")
        cid = f"conjectures/{path.name}"
        nodes[cid] = Node(
            id=cid,
            statement=" ".join(meta["statement"].split()),
            rung=rungs.get(cid),
            barred=meta.get("barred"),
        )

    inquiries: dict[str, dict] = {}
    for path in sorted((root / "inquiries").iterdir()):
        meta = _frontmatter(path / "README.md")
        iid = f"inquiries/{path.name}"
        inquiries[iid] = meta

        events = (
            ledgers.get(iid, [])
            if ledgers is not None
            else _frontmatter(path / "axiom.md").get("events", [])
            if (path / "axiom.md").exists()
            else []
        )

        carried = next((e for e in events if e["event"] == "carried"), None)
        if not carried:
            continue  # Searching, or never returned — no leg exists
        retracted = next((e for e in events if e["event"] == "retracted"), None)

        declared = [
            h["name"]
            for h in (meta["adequacy"]["hazards"].get("untestable") or [])
        ]
        late = [e["name"] for e in events if e["event"] == "hazard"]

        # ONE axiom, MANY legs — one per conjecture the Inquiry serves. Retraction
        # is written once, here, and kills every leg it fed. That is the whole
        # argument for putting the ledger in the Inquiry rather than the conjecture.
        for cid in meta["conjectures"]:
            if cid not in nodes:
                continue
            nodes[cid].legs.append(
                Leg(
                    inquiry=iid,
                    conjecture=cid,
                    kind=LegKind.SURVIVAL,
                    domain=meta["domain"],
                    axiom=" ".join(meta["axiom_if_carried"].split()),
                    hazards=declared + late,
                    alive=retracted is None,
                    died=retracted["why"] if retracted else None,
                    route=retracted["route"] if retracted else None,
                )
            )

    return Projection(nodes, inquiries, releases=charter.get("releases", []))


# --------------------------------------------------------------------------
# The chart — recomputed from scratch, never appended to
# --------------------------------------------------------------------------

BLOCKS = "▁▂▃▄▅▆▇█"


def chart(series: list[tuple[str, float | None]]) -> str:
    """Plotted against releases, never wall-clock, and rebuilt in full every time:
    the tag list is walked, the projection rebuilt at each tag, the whole block
    rewritten. A correction dated into the past corrects the past chart."""
    lines = ["Programme health — index on [-1, +1], against releases", ""]
    if not series:
        return "\n".join(lines + ["  (no releases yet — nothing to plot)"])
    spark = "".join(
        " " if v is None else BLOCKS[min(7, int((v + 1) / 2 * 7.999))] for _, v in series
    )
    lines.append(f"  +1 │ {spark}")
    lines.append(f"  -1 └{'─' * (len(spark) + 1)}")
    lines.append(f"     {series[0][0]} → {series[-1][0]}")
    return "\n".join(lines)
