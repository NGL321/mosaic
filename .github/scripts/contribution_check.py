#!/usr/bin/env python3
"""Check §8's mechanical obligations over the commits a fork pull request adds.

§8's merge checklist has four items. Three are facts a runner can read, and only
those are checked here:

  EXTERNAL   the contribution arrives as a fork pull request.
  SIGN-OFF   every commit it adds carries `Signed-off-by:` (the DCO).
  AUTHORED   it touches no authored file.

The fourth — review — is Noah's, always, and is not CI's to judge.

**This check runs unconditionally and skips internally.** That is what lets it be
a *required* check on `main`, and it is the trap `custody.yml`'s header already
documents: a path-filtered workflow never runs on pull requests that touch
nothing in `paths:`, so a required check that never runs sits *expected* forever
and blocks the merge. Here there is no filter and no early exit — an internal
pull request reports a skip and exits 0.

**External is the fork boundary, and nothing else** (§8). Work arriving through
this repo's own branch flow is internal whoever or whatever held the pen; work
arriving from a fork is external. The workflow hands this script both repository
names and it compares them, so the rule keys on a fact rather than on a
judgement about authorship.

**The authored set is imported from `custody_check.py`, never re-declared.** That
script cross-checks its set against the workflow that invokes it and exits 2 on
drift; a second copy of the list here would unlearn that lesson, and a file
present in one copy but not the other is exactly the unchecked file both checks
exist to catch.

Usage:  contribution_check.py <base-sha> <head-sha> <base-repo> <head-repo>

Exit codes (distinct so CI can tell a violation from a broken tool):
    0  no violations, or the pull request is internal and was skipped
    1  a §8 violation
    2  the tool could not run — bad refs, vacuous authored set, drifted config
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from custody_check import (  # noqa: E402  (path must be set before this import)
    AUTHORED,
    EXIT_OK,
    EXIT_TOOL,
    EXIT_VIOLATION,
    GitError,
    authored_files_touched,
    commits,
    git,
    trailers,
    validate_authored_set,
)

# Output carries § and em dashes; a cp1252 console would mangle them.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass


def sign_offs(tr: dict[str, list[str]]) -> list[str]:
    """The commit's `Signed-off-by:` trailers.

    Read through `git interpret-trailers` like every other trailer in this
    repository (§5 pins the mechanism): a `Signed-off-by:` quoted in a commit
    body, or inside a pasted diff, must not satisfy the DCO.
    """
    return tr.get("signed-off-by", [])


def main() -> int:
    if len(sys.argv) != 5:
        print(
            "usage: contribution_check.py <base-sha> <head-sha> <base-repo> <head-repo>",
            file=sys.stderr,
        )
        return EXIT_TOOL

    base, head, base_repo, head_repo = sys.argv[1:5]

    # EXTERNAL — decided first, because everything below only binds external work.
    if not base_repo or not head_repo:
        print(
            "contribution check could not run: the workflow passed an empty "
            "repository name, so the fork boundary is undecidable",
            file=sys.stderr,
        )
        return EXIT_TOOL

    if base_repo.lower() == head_repo.lower():
        print(
            f"SKIPPED — internal pull request (head is {head_repo}, the base "
            f"repository itself). §8 binds work arriving across the fork "
            f"boundary; §5's custody trailers govern this one."
        )
        return EXIT_OK

    print(f"External pull request: {head_repo} → {base_repo}. §8 applies.\n")

    problems: list[str] = []
    notes: list[str] = []

    try:
        # A pass must mean something: if the authored set is vacuous or has
        # drifted from the workflow that declares it, AUTHORED below would be
        # checking nothing. Borrowed whole from custody_check, along with the set.
        notes.extend(validate_authored_set())
        added = commits(base, head)
    except GitError as e:
        print(f"contribution check could not run: {e}", file=sys.stderr)
        return EXIT_TOOL

    if notes:
        print("NOTES — about what this run covers:")
        print("\n".join(f"  {n}" for n in notes), "\n")

    if not added:
        print(
            "contribution check could not run: the pull request adds no commits "
            "relative to its merge base, so there is nothing to certify",
            file=sys.stderr,
        )
        return EXIT_TOOL

    observations: list[str] = []

    try:
        for sha in added:
            short = git("show", "-s", "--format=%h %s", sha)
            author = git("show", "-s", "--format=%an <%ae>", sha)
            tr = trailers(sha)

            # SIGN-OFF
            signed = sign_offs(tr)
            if not signed:
                problems.append(
                    f"{short}\n    no Signed-off-by: trailer — the DCO is unmet (§8). "
                    f"`git commit --amend -s` on a single commit, or "
                    f"`git rebase --signoff <base>` across the branch, then force-push "
                    f"your fork's branch"
                )
            elif not any(s.strip().lower() == author.strip().lower() for s in signed):
                # Not a violation: §8 requires the trailer, and a contributor may
                # legitimately sign off on a commit they are carrying for someone
                # else. Reported so the reviewer can ask.
                observations.append(
                    f"{short}\n    signed off by {', '.join(signed)}, authored by "
                    f"{author} — not a violation, but worth a question on the thread"
                )

            # AUTHORED
            touched = authored_files_touched(sha)
            if touched:
                problems.append(
                    f"{short}\n    touches {', '.join(touched)}, which is authored "
                    f"(§5) — human-only means Noah, and an external contributor sits "
                    f"where an agent sits. Revert the change and propose the exact "
                    f"replacement text in this pull request instead; it will be "
                    f"applied by hand"
                )
    except GitError as e:
        print(f"contribution check could not run: {e}", file=sys.stderr)
        return EXIT_TOOL

    if observations:
        print("FOR THE REVIEWER — recorded, not failed:")
        print("\n".join(f"  {o}" for o in observations), "\n")

    if problems:
        print("§8 VIOLATIONS:")
        print("\n".join(f"  {p}" for p in problems))
        print(
            "\nThe fourth checklist item — review — is not CI's to judge, and is "
            "unaffected by the above."
        )
        return EXIT_VIOLATION

    print(
        f"{len(added)} commit(s) checked: every one signed off, none touching an "
        f"authored file. Review is the remaining checklist item, and is Noah's (§8)."
    )
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
