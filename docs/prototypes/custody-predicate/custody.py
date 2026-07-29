"""
PROTOTYPE (ticket #23) — the portable bit.

QUESTION BEING PROTOTYPED
-------------------------
PROTOCOL.md §5 claims custody of authored files (CONTEXT.md, the charter) is
"human only", and offers `git log --format='%an' -- CONTEXT.md → one name` as its
mechanical check. That command does not work today, and #24 will make it *work*
without deciding *what it should say*. Three readings of what custody claims are
on the table, and they are not nested — each convicts commits the others acquit:

  A  TYPED       the human typed the text; an agent co-author trailer on an
                 authored file is a violation.
  B  AMANUENSIS  the human authored it with an agent as amanuensis; the trailer
                 is expected, and the violation is an *unattended* agent session
                 committing an authored file.
  C  ENDORSED    the human understood and endorsed it; custody collapses into
                 warrant (§5's second half) and the file-level rule is dropped.

This module is the decision procedure for all three, as pure predicates over one
commit. Drive it by hand with prototype_tui.py. It is written to be lifted: the
winning policy becomes the CI check, and the rest is thrown away.

Deliberately, each policy can return UNDECIDABLE or VACUOUS as well as
PASS/VIOLATION — because the interesting difference between the readings turns
out to be less about which commits they convict than about whether git carries
the facts they need at all.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum


class FileClass(Enum):
    """§5's custody categories. Custody follows the file, never the topic."""

    AUTHORED = "AUTHORED"  # CONTEXT.md, the charter
    RECORD = "RECORD"  # research docs, notebook, ledger, experiment output
    TOOLING = "TOOLING"  # PROTOCOL.md, README.md, CI, config


class Identity(Enum):
    """Who the commit's author field actually identifies."""

    HUMAN = "HUMAN"  # post-#24: a human identity means a human
    AGENT_BOT = "AGENT_BOT"  # post-#24: agents commit under a bot identity
    HUMAN_UNVERIFIED = "HUMAN_UNVERIFIED"  # today: agent worktrees inherit NGL321


class Session(Enum):
    """Whether a human was present when the commit was made."""

    ATTENDED = "ATTENDED"
    UNATTENDED = "UNATTENDED"
    UNKNOWN = "UNKNOWN"  # today's state: git carries no attendance signal


class Endorsement(Enum):
    """Whether a §5-warrant-style artifact accompanies the commit."""

    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    UNKNOWN = "UNKNOWN"


class Verdict(Enum):
    PASS = "PASS"
    VIOLATION = "VIOLATION"
    UNDECIDABLE = "UNDECIDABLE"  # the policy needs a fact git does not carry
    VACUOUS = "VACUOUS"  # the policy applies but demands nothing here


@dataclass(frozen=True)
class Commit:
    subject: str
    ctype: str  # record | evidence | belt | core | feat | fix | chore
    file_class: FileClass
    identity: Identity
    agent_co_author: bool
    session: Session = Session.UNKNOWN
    endorsement: Endorsement = Endorsement.UNKNOWN
    sha: str | None = None  # set when the case came from real history

    def with_(self, **kw) -> Commit:
        return replace(self, **kw)


@dataclass(frozen=True)
class Ruling:
    verdict: Verdict
    reason: str


# --------------------------------------------------------------------------
# Policy A — TYPED
# --------------------------------------------------------------------------

def typed(c: Commit) -> Ruling:
    """The human typed it. Agent participation in an authored file is a breach."""
    if c.file_class is not FileClass.AUTHORED:
        return Ruling(Verdict.VACUOUS, "custody's file rule bites only on authored files")
    if c.identity is Identity.AGENT_BOT:
        return Ruling(Verdict.VIOLATION, "an agent identity committed an authored file")
    if c.agent_co_author:
        return Ruling(Verdict.VIOLATION, "agent co-author trailer on an authored file")
    if c.identity is Identity.HUMAN_UNVERIFIED:
        return Ruling(
            Verdict.UNDECIDABLE,
            "human name, but agent sessions inherit it — nothing distinguishes them (pre-#24)",
        )
    return Ruling(Verdict.PASS, "human identity, no agent trailer")


# --------------------------------------------------------------------------
# Policy B — AMANUENSIS
# --------------------------------------------------------------------------

def amanuensis(c: Commit) -> Ruling:
    """The human authored it; an agent held the pen. Attendance is the claim."""
    if c.file_class is not FileClass.AUTHORED:
        return Ruling(Verdict.VACUOUS, "custody's file rule bites only on authored files")
    if c.identity is Identity.AGENT_BOT:
        return Ruling(Verdict.VIOLATION, "an agent identity committed an authored file")
    if c.session is Session.UNATTENDED:
        return Ruling(Verdict.VIOLATION, "an unattended session committed an authored file")
    if c.session is Session.UNKNOWN:
        return Ruling(
            Verdict.UNDECIDABLE,
            "attendance is the whole claim, and git carries no attendance signal",
        )
    if c.identity is Identity.HUMAN_UNVERIFIED:
        return Ruling(Verdict.UNDECIDABLE, "committing identity not distinguishable (pre-#24)")
    return Ruling(Verdict.PASS, "attended session under a human identity; trailer expected")


# --------------------------------------------------------------------------
# Policy C — ENDORSED
# --------------------------------------------------------------------------

def endorsed(c: Commit) -> Ruling:
    """Custody collapses into warrant. The file class stops mattering; the
    commit type starts mattering. Note what this does to vocabulary."""
    if c.ctype.rstrip(":") not in {"belt", "core"}:
        return Ruling(
            Verdict.VACUOUS,
            f"{c.ctype} demands nothing of the human under the warrant table",
        )
    if c.endorsement is Endorsement.ABSENT:
        return Ruling(Verdict.VIOLATION, "no falsifier / work product accompanies the claim")
    if c.endorsement is Endorsement.UNKNOWN:
        return Ruling(
            Verdict.UNDECIDABLE,
            "the artifact lives on a pull request, not in the commit",
        )
    return Ruling(Verdict.PASS, "warrant artifact present")


POLICIES = (
    ("A", "typed", typed),
    ("B", "amanuensis", amanuensis),
    ("C", "endorsed", endorsed),
)


# What an outside reader — the sceptic §5 exists to answer — can actually run.
STRANGER_CHECK = {
    "typed": "yes — one git command, once #24 gives agents their own identity",
    "amanuensis": "no — needs an attendance trailer that does not exist yet",
    "endorsed": "no — the artifact is on a PR thread, outside the history",
}
