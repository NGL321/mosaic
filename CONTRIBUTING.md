# Contributing to Mosaic

Four things. The reasoning for all of them is in
[`PROTOCOL.md` §8](PROTOCOL.md) — this page is the checklist, not the policy.

1. **Open a fork pull request.** The fork boundary is what makes a contribution external,
   and it is what the CI check keys on.
2. **Sign off every commit** — `git commit -s`, which appends `Signed-off-by:`. This is a
   [DCO](https://developercertificate.org/), not a CLA: you are certifying you have the
   right to submit the work, not assigning anything.
3. **Touch no authored file, and nothing under `.github/`.** `CONTEXT.md` and
   `CHARTER.md` are the researcher's own hand; `.github/` holds the checks that judge
   your pull request. Propose the change in the thread instead — exact replacement text
   for an authored file, a description or an issue for the apparatus. Both are checked
   per commit, so reverting in a later commit does not clear a violation.
4. **Expect a reviewer.** Always, and always Noah. Research-track contributions also get a
   checker agent.

You licence each file you touch under whatever that file's path already carries — MIT for
code, CC BY 4.0 for the prose record. The table is in [`README.md`](README.md#licensing).

Contributions are credited in `git log` and by the licence's notice requirement. Where a
recorded result comes to depend on your apparatus, the record of the Run that produced it
cites the apparatus and you by name.
