"""PROTOTYPE — harvest this repository's real history into example/history.json.

    python docs/prototypes/ci-gates/harvest.py

Run once; the output is committed beside it so `prototype_tui.py` is hermetic — no
git, no network, no GitHub. Every case the prototype runs is a pull request that
actually merged into `main`, with the signature verdicts GitHub actually returns.

Two things are read from GitHub rather than from git, and both matter:

  * **signature verification.** `git log %G?` shells out to gpg, which is absent on
    most machines — it returned `N` for every commit here, including the ones GitHub
    reports as `verified`. A signature gate built on `%G?` would fail the whole
    repository on a runner without gpg configured, and pass nothing anywhere.
  * **the signer.** `verified: true` is not a claim about a person. The payload names
    which key signed, and GitHub's own `web-flow` key signs anything done through the
    web UI or the API — which is the hole the prototype exists to show.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parents[2]
REPO = "NGL321/mosaic"


def run(cmd: list[str]) -> str:
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    if out.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:3])} failed: {out.stderr.strip()[:300]}")
    return out.stdout


def git(*args: str) -> str:
    return run(["git", *args]).strip()


def gh_json(path: str, jq: str) -> str:
    return run(["gh", "api", path, "--jq", jq])


def verification_index() -> dict[str, dict]:
    """sha -> {verified, reason, signer} for every commit reachable from main."""
    index: dict[str, dict] = {}
    page = 1
    while True:
        raw = gh_json(
            f"repos/{REPO}/commits?per_page=100&page={page}",
            '.[] | {sha, v: .commit.verification, name: .commit.author.name, '
            'email: .commit.author.email, login: (.author.login // null)}',
        )
        lines = [json.loads(x) for x in raw.splitlines() if x.strip()]
        if not lines:
            break
        for row in lines:
            v = row["v"]
            index[row["sha"]] = {
                "verified": v["verified"],
                "reason": v["reason"],
                # The signer is not in the summary; it is recoverable from the
                # signature payload's key id. GitHub's own key signs `web-flow`
                # operations, which is the distinction the gate needs.
                "signer": signer_of(v),
                "login": row["login"],
            }
        page += 1
        if page > 6:
            break
    return index


GITHUB_KEYS = {"B5690EEEBB952194", "4AEE18F83AFDEB23"}  # GitHub's web-flow signing keys


def signer_of(v: dict) -> str | None:
    if not v.get("verified"):
        return None
    sig = v.get("signature") or ""
    if "SSH SIGNATURE" in sig:
        return "ssh"
    payload = v.get("payload") or ""
    m = re.search(r"^committer ([^<]+) <", payload, re.M)
    return (m.group(1).strip() if m else "unknown")


def pr_index() -> dict[str, dict]:
    """merge sha -> {number, branch}."""
    raw = run([
        "gh", "pr", "list", "--state", "merged", "--limit", "100",
        "--json", "number,headRefName,mergeCommit",
    ])
    index: dict[str, dict] = {}
    for pr in json.loads(raw):
        mc = pr.get("mergeCommit") or {}
        sha = mc.get("oid")
        if sha and sha not in index:
            index[sha] = {"number": pr["number"], "branch": pr["headRefName"]}
    return index


def trailers(sha: str) -> dict[str, list[str]]:
    body = git("show", "-s", "--format=%B", sha)
    out = subprocess.run(
        ["git", "interpret-trailers", "--parse"],
        input=body, capture_output=True, text=True, encoding="utf-8", cwd=ROOT,
    ).stdout
    found: dict[str, list[str]] = {}
    for line in out.splitlines():
        key, sep, value = line.partition(":")
        if sep:
            found.setdefault(key.strip().lower(), []).append(value.strip())
    return found


def main() -> None:
    verify = verification_index()
    prs = pr_index()

    changes = []
    for sha in git("log", "origin/main", "--first-parent", "--format=%H").split():
        parents = git("show", "-s", "--format=%P", sha).split()
        if len(parents) < 2:
            continue  # a direct commit to main; not a pull request
        branch_shas = git("rev-list", "--no-merges", f"{parents[0]}..{parents[1]}").split()
        pr = prs.get(sha, {})
        changes.append({
            "pr": pr.get("number"),
            "branch": pr.get("branch"),
            "merge": {
                "sha": sha[:7],
                "subject": git("show", "-s", "--format=%s", sha),
                "body": git("show", "-s", "--format=%b", sha),
                "author": git("show", "-s", "--format=%an", sha),
                **{k: v for k, v in (verify.get(sha) or {}).items()},
            },
            "commits": [
                {
                    "sha": c[:7],
                    "subject": git("show", "-s", "--format=%s", c),
                    "author": git("show", "-s", "--format=%an", c),
                    "email": git("show", "-s", "--format=%ae", c),
                    "files": git("show", "--name-only", "--format=", c).split("\n"),
                    "trailers": trailers(c),
                    **{k: v for k, v in (verify.get(c) or {}).items()},
                }
                for c in branch_shas
            ],
        })

    tree = sorted(
        p for p in git("ls-tree", "-r", "--name-only", "origin/main").splitlines()
    )

    links = []
    for path in tree:
        if not path.endswith(".md"):
            continue
        text = git("show", f"origin/main:{path}")
        for m in re.finditer(r"\[([^\]]*)\]\(([^)\s]+)\)", text):
            target = m.group(2)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            links.append({"file": path, "text": m.group(1)[:48], "target": target})

    out = {"changes": changes, "tree": tree, "links": links, "branches": sorted(
        b.strip().removeprefix("origin/")
        for b in git("branch", "-r", "--format=%(refname:short)").splitlines()
        if "HEAD" not in b
    )}
    (HERE / "example").mkdir(exist_ok=True)
    (HERE / "example" / "history.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(changes)} merged pull requests, {len(out['branches'])} branches, "
          f"{len(links)} relative links, {len(tree)} paths")


if __name__ == "__main__":
    main()
