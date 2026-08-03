#!/usr/bin/env python3
"""
Is there any sample size n that makes the significance bolding in Tang et al.
(2026), "Topological Signatures of Grokking" (arXiv:2605.06352v1), Tables 1
and 2, internally consistent?

Companion to docs/research/2026-08-02-tang-p-values-and-sample-size.md, which
discharges verification-debt ticket #111.

The setting. Each table cell reports a Spearman rank correlation rho between a
persistent-homology statistic and test accuracy, taken ACROSS TRAINING
CHECKPOINTS within a run and then averaged over five seeds (46-50), with the
+/- being a standard deviation across those seeds. Both captions declare that
bolded cells have p < 0.05. The paper never states how many checkpoints enter
a rho: section 3 says weights and metrics are "checkpointed every 500 steps"
over 6e4 gradient steps -- which would be 121 checkpoints counting step 0 --
but that persistent homology is computed only "at selected checkpoints", and
never says which or how many. So n is unstated and 121 is a hard ceiling.

The test this script runs. For a Spearman rho at fixed n, EVERY standard
two-sided test -- the t-approximation, the Fisher-z/normal approximation, and
the exact permutation distribution alike -- rejects exactly when |rho| exceeds
a critical value rho_crit(n) that decreases in n. So under any single n, and
in fact under any per-cell test of this family with a common n, the bolded
cells must be an upward-closed set in |rho|: no bolded cell may have a smaller
|rho| than any unbolded cell in the same table.

That gives a two-sided bracket which needs no assumption about which test was
used:

    rho_crit(n) <= min |rho| over BOLDED cells        (so the bolding is earned)
    rho_crit(n) >  max |rho| over UNBOLDED cells      (so the non-bolding is earned)

If those two intervals in n are disjoint, no single n reconciles the table and
the p-values are not reconstructable -- not merely unstated.

What is computed, per table:

  1. rho_crit(n) for the candidate n the training schedule admits (every-500
     cadence and its coarsenings), by the t-approximation for n >= 11 and by
     exact enumeration of all n! rank permutations for n <= 10, where the
     t-approximation is known to be poor and where the "small n" branch of the
     argument lives.
  2. n_min: the smallest n at which the weakest bolded cell clears threshold.
     n_max: the largest n at which the strongest unbolded cell does not.
  3. The full inversion set: every (bolded, unbolded) pair in the same table
     with |rho_bold| < |rho_unbold|. Each such pair is a witness that no n works.
  4. The same monotonicity check against |rho| / SD, i.e. against a one-sample
     t-test on the five per-seed rho values -- the obvious alternative rule,
     which uses the printed SD rather than n.
  5. The best-fitting n anyway: the n minimising the number of cells whose bold
     status disagrees with |rho| >= rho_crit(n), and the residual error count.

Requires numpy and scipy. Deterministic; no RNG. ASCII output.

    python docs/research/2026-08-02-tang-p-value-reconstruction.py
"""

from __future__ import annotations

import itertools
import math
import sys
from functools import lru_cache

import numpy as np
from scipy import stats

ALPHA = 0.05          # the alpha both table captions declare
N_SEEDS = 5           # seeds 46-50, per section 3
TOTAL_STEPS = 60_000  # "6e4 gradient steps", section 3
CADENCE = 500         # "checkpointed every 500 steps", section 3
EXACT_MAX_N = 10      # exact permutation critical values are enumerated to here

# ---------------------------------------------------------------------------
# The tables. Values transcribed from the arXiv HTML of v1 and re-checked
# cell for cell against the PDF text layer of the same version. The bold flag
# is recovered from the HTML's ltx_font_bold spans, since bold does not
# survive PDF text extraction; True == the paper marks the cell p < 0.05.
# ---------------------------------------------------------------------------

# (metric, layer, [(rho, sd, bold) per permutation column])
TABLE1_COLS = ["0%", "1%", "5%", "10%", "20%"]
TABLE1 = [
    ("H0 Max",   "Embed",   [(-0.78, 0.04, True),  (-0.72, 0.07, True),
                             (-0.84, 0.07, True),  (-0.86, 0.06, True),
                             (-0.10, 0.32, False)]),
    ("H0 Max",   "Layer 1", [(-0.55, 0.08, True),  (-0.70, 0.06, True),
                             (-0.89, 0.03, True),  (-0.85, 0.07, True),
                             (-0.05, 0.20, False)]),
    ("H0 Max",   "Layer 2", [(-0.47, 0.10, True),  (-0.52, 0.14, True),
                             (-0.56, 0.16, True),  (-0.67, 0.08, True),
                             (+0.00, 0.08, False)]),
    ("H0 Total", "Embed",   [(-0.75, 0.03, True),  (-0.71, 0.10, True),
                             (-0.87, 0.06, True),  (-0.91, 0.03, True),
                             (-0.20, 0.36, False)]),
    ("H0 Total", "Layer 1", [(-0.49, 0.08, True),  (-0.67, 0.09, True),
                             (-0.90, 0.03, True),  (-0.88, 0.06, True),
                             (-0.14, 0.29, False)]),
    ("H0 Total", "Layer 2", [(-0.06, 0.27, False), (-0.47, 0.14, True),
                             (-0.59, 0.17, True),  (-0.82, 0.08, True),
                             (-0.03, 0.10, False)]),
    ("H1 Max",   "Embed",   [(+0.77, 0.03, True),  (+0.71, 0.06, True),
                             (+0.80, 0.06, True),  (+0.69, 0.10, True),
                             (+0.08, 0.10, False)]),
    ("H1 Max",   "Layer 1", [(+0.49, 0.08, True),  (+0.70, 0.07, True),
                             (+0.81, 0.05, True),  (+0.68, 0.14, True),
                             (+0.09, 0.17, False)]),
    ("H1 Max",   "Layer 2", [(-0.23, 0.23, False), (+0.53, 0.10, True),
                             (+0.59, 0.13, True),  (+0.65, 0.11, True),
                             (+0.05, 0.05, False)]),
    ("H1 Total", "Embed",   [(+0.60, 0.10, True),  (+0.42, 0.39, True),
                             (+0.24, 0.49, True),  (+0.14, 0.51, True),
                             (+0.10, 0.21, False)]),
    ("H1 Total", "Layer 1", [(+0.33, 0.16, False), (+0.71, 0.13, True),
                             (+0.74, 0.12, True),  (+0.71, 0.18, True),
                             (+0.10, 0.18, False)]),
    ("H1 Total", "Layer 2", [(+0.80, 0.04, True),  (+0.66, 0.10, True),
                             (+0.62, 0.06, True),  (+0.40, 0.31, True),
                             (+0.05, 0.09, False)]),
]

TABLE2_COLS = ["0%", "10%", "20%", "50%", "100%"]
TABLE2 = [
    ("H0 Max",   "Embed (L0)", [(-0.49, 0.45, True),  (-0.26, 0.37, False),
                                (+0.03, 0.26, False), (-0.12, 0.14, False),
                                (-0.08, 0.26, False)]),
    ("H0 Max",   "Hidden 1",   [(-0.55, 0.39, True),  (-0.30, 0.38, False),
                                (+0.05, 0.27, False), (-0.17, 0.15, False),
                                (-0.11, 0.16, False)]),
    ("H0 Max",   "Hidden 2",   [(-0.69, 0.27, True),  (-0.51, 0.23, True),
                                (-0.39, 0.17, True),  (-0.47, 0.25, False),
                                (+0.01, 0.22, False)]),
    ("H0 Max",   "Hidden 3",   [(-0.81, 0.07, True),  (-0.69, 0.16, True),
                                (-0.57, 0.08, True),  (-0.51, 0.11, True),
                                (+0.09, 0.16, False)]),
    ("H0 Total", "Embed (L0)", [(-0.54, 0.40, True),  (-0.30, 0.34, False),
                                (-0.00, 0.21, False), (-0.16, 0.15, False),
                                (-0.05, 0.27, False)]),
    ("H0 Total", "Hidden 1",   [(-0.61, 0.36, False), (-0.42, 0.30, False),
                                (-0.15, 0.23, False), (-0.29, 0.18, False),
                                (-0.04, 0.23, False)]),
    ("H0 Total", "Hidden 2",   [(-0.84, 0.10, True),  (-0.77, 0.08, True),
                                (-0.64, 0.11, True),  (-0.58, 0.24, True),
                                (+0.04, 0.22, False)]),
    ("H0 Total", "Hidden 3",   [(-0.86, 0.06, True),  (-0.84, 0.08, True),
                                (-0.80, 0.05, True),  (-0.72, 0.13, True),
                                (+0.11, 0.20, False)]),
    ("H1 Max",   "Embed (L0)", [(+0.49, 0.41, True),  (+0.30, 0.33, False),
                                (+0.01, 0.20, False), (+0.18, 0.17, False),
                                (+0.06, 0.27, False)]),
    ("H1 Max",   "Hidden 1",   [(+0.56, 0.39, True),  (+0.41, 0.30, False),
                                (+0.14, 0.21, False), (+0.24, 0.20, False),
                                (+0.13, 0.12, False)]),
    ("H1 Max",   "Hidden 2",   [(+0.79, 0.09, True),  (+0.74, 0.06, True),
                                (+0.62, 0.05, True),  (+0.50, 0.25, True),
                                (-0.01, 0.25, False)]),
    ("H1 Max",   "Hidden 3",   [(+0.76, 0.11, True),  (+0.73, 0.12, True),
                                (+0.62, 0.05, True),  (+0.56, 0.16, True),
                                (-0.05, 0.23, False)]),
    ("H1 Total", "Embed (L0)", [(-0.36, 0.31, False), (-0.08, 0.27, False),
                                (-0.30, 0.09, True),  (-0.09, 0.20, False),
                                (+0.11, 0.11, False)]),
    ("H1 Total", "Hidden 1",   [(-0.68, 0.16, True),  (-0.62, 0.18, True),
                                (-0.58, 0.10, True),  (-0.38, 0.27, True),
                                (+0.06, 0.27, False)]),
    ("H1 Total", "Hidden 2",   [(-0.69, 0.18, True),  (-0.67, 0.11, True),
                                (-0.58, 0.12, True),  (-0.53, 0.23, True),
                                (+0.07, 0.35, False)]),
    ("H1 Total", "Hidden 3",   [(-0.72, 0.16, True),  (-0.73, 0.14, True),
                                (-0.65, 0.06, True),  (-0.63, 0.19, True),
                                (-0.01, 0.33, False)]),
]


def cells(table, cols):
    """Flatten a table to (label, rho, sd, bold) records."""
    out = []
    for metric, layer, row in table:
        for col, (rho, sd, bold) in zip(cols, row):
            out.append((f"{metric} / {layer} / {col}", rho, sd, bold))
    return out


# ---------------------------------------------------------------------------
# Critical |rho| for a two-sided Spearman test at level alpha.
# ---------------------------------------------------------------------------

def rho_crit_t(n: int, alpha: float = ALPHA) -> float:
    """
    t-approximation: t = rho * sqrt((n-2)/(1-rho^2)) ~ t_{n-2} under the null.
    Inverting at the two-sided critical t gives rho_crit = sqrt(t^2/(t^2+n-2)).
    This is what scipy.stats.spearmanr reports for n above a handful.
    """
    if n < 3:
        return float("nan")
    t = stats.t.ppf(1 - alpha / 2, n - 2)
    return math.sqrt(t * t / (t * t + n - 2))


def rho_crit_fisher(n: int, alpha: float = ALPHA) -> float:
    """Fisher-z / normal approximation, as a second opinion on rho_crit_t."""
    if n < 4:
        return float("nan")
    z = stats.norm.ppf(1 - alpha / 2) * math.sqrt(1.06 / (n - 3))
    return math.tanh(z)


@lru_cache(maxsize=None)
def rho_crit_exact(n: int, alpha: float = ALPHA) -> float:
    """
    Exact two-sided critical value from the full null permutation distribution
    of Spearman's rho: the smallest attainable |rho| whose two-sided tail
    probability is <= alpha. Enumerates all n! rank orders, so n <= 10.
    """
    base = np.arange(1, n + 1, dtype=np.float64)
    denom = n * (n * n - 1) / 6.0
    vals = np.array([1.0 - ((base - np.asarray(p, dtype=np.float64)) ** 2).sum() / denom
                     for p in itertools.permutations(range(1, n + 1))])
    a = np.sort(np.abs(vals))
    total = len(a)
    # two-sided p for an observed |rho| = r is P(|rho_null| >= r)
    for r in np.unique(a):
        tail = float((a >= r - 1e-12).sum()) / total
        if tail <= alpha:
            return float(r)
    return float("inf")


def rho_crit(n: int) -> float:
    """Exact where enumeration is feasible, t-approximation above that."""
    return rho_crit_exact(n) if n <= EXACT_MAX_N else rho_crit_t(n)


# ---------------------------------------------------------------------------
# Analyses
# ---------------------------------------------------------------------------

def candidate_ns() -> list[tuple[int, str]]:
    """
    The n values the reported schedule admits. Checkpoints exist every 500
    steps over 60,000, so 121 counting step 0 and 120 not; persistent homology
    is computed on some unstated subset, so any coarser regular cadence is a
    candidate and 121 is the ceiling.
    """
    out = []
    for k in (1, 2, 4, 5, 10, 20, 40, 60, 100, 120):
        stride = CADENCE * k
        n = TOTAL_STEPS // stride + 1
        out.append((n, f"PH every {stride:,} steps"))
    out.append((TOTAL_STEPS // CADENCE, "every 500 steps, step 0 not analysed"))
    out.append((N_SEEDS, "one point per seed (not the stated design)"))
    seen, uniq = set(), []
    for n, why in sorted(out, reverse=True):
        if n not in seen and n >= 4:
            seen.add(n)
            uniq.append((n, why))
    return uniq


def bracket(recs):
    """
    (n_min, n_max, weakest bolded, strongest unbolded).

    n_min = smallest n at which the weakest bolded cell reaches significance.
    n_max = largest n at which the strongest unbolded cell still does not.
    Any n consistent with the table's bolding must satisfy n_min <= n <= n_max.
    """
    bold = [r for r in recs if r[3]]
    plain = [r for r in recs if not r[3]]
    weakest = min(bold, key=lambda r: abs(r[1]))
    strongest = max(plain, key=lambda r: abs(r[1]))
    n_min = next((n for n in range(4, 5001) if rho_crit(n) <= abs(weakest[1])), None)
    n_max = None
    for n in range(4, 5001):
        if rho_crit(n) > abs(strongest[1]):
            n_max = n
    return n_min, n_max, weakest, strongest


def inversions(recs, key):
    """Every (bolded, unbolded) pair the given statistic orders the wrong way."""
    bold = [r for r in recs if r[3]]
    plain = [r for r in recs if not r[3]]
    return [(b, u) for b in bold for u in plain if key(b) < key(u)]


def best_n(recs, nmax=400):
    """The n minimising disagreement between the bolding and |rho| >= rho_crit(n)."""
    best = []
    for n in range(4, nmax + 1):
        c = rho_crit(n)
        err = sum(1 for _lab, rho, _sd, bold in recs if (abs(rho) >= c) != bold)
        best.append((err, n, c))
    best.sort()
    return best


def report(name, table, cols):
    recs = cells(table, cols)
    n_bold = sum(1 for r in recs if r[3])
    print("=" * 78)
    print(f"{name}: {len(recs)} cells, {n_bold} bolded p < 0.05, "
          f"{len(recs) - n_bold} not")
    print("=" * 78)

    n_min, n_max, weakest, strongest = bracket(recs)
    print()
    print("  weakest BOLDED cell     "
          f"{weakest[0]:<34} rho = {weakest[1]:+.2f} +/- {weakest[2]:.2f}")
    print("  strongest UNBOLDED cell "
          f"{strongest[0]:<34} rho = {strongest[1]:+.2f} +/- {strongest[2]:.2f}")
    print()
    print(f"  for the bolded cell to be significant:      n >= {n_min}")
    print(f"  for the unbolded cell to be insignificant:  n <= {n_max}")
    feasible = "NONE -- the two requirements are disjoint" if n_min > n_max else \
        f"{n_min}..{n_max}"
    print(f"  ==> single n consistent with both:          {feasible}")
    print(f"  (the schedule's ceiling is {TOTAL_STEPS // CADENCE + 1} checkpoints)")

    inv_rho = inversions(recs, lambda r: abs(r[1]))
    inv_t = inversions(recs, lambda r: abs(r[1]) / r[2] if r[2] > 0 else float("inf"))
    print()
    print(f"  inversions under |rho|        : {len(inv_rho)} pairs, "
          f"{len({b[0] for b, _u in inv_rho})} distinct bolded cells "
          f"(weaker than some unbolded cell)")
    print(f"  inversions under |rho| / SD   : {len(inv_t)} "
          f"(so a seed-level t-test does not order them either)")

    print()
    print("  rho_crit(n) at the n the reported schedule admits, and the number")
    print("  of the table's cells whose bold status it would contradict:")
    print(f"    {'n':>5}  {'rho_crit':>9}  {'wrong':>6}   note")
    for n, why in candidate_ns():
        c = rho_crit(n)
        err = sum(1 for _l, rho, _s, bold in recs if (abs(rho) >= c) != bold)
        print(f"    {n:>5}  {c:>9.4f}  {err:>6}   {why}")

    b = best_n(recs)
    err, n, c = b[0]
    ties = [x[1] for x in b if x[0] == err]
    print()
    print(f"  best-fitting n over 4..400: n = {n} (rho_crit = {c:.4f}), "
          f"{err} of {len(recs)} cells still wrong")
    print(f"  (n values achieving that minimum: {min(ties)}..{max(ties)})")
    print("  cells the best-fitting n gets wrong:")
    for lab, rho, sd, bold in recs:
        if (abs(rho) >= c) != bold:
            says = "bolded but |rho| < rho_crit" if bold else \
                   "not bolded but |rho| >= rho_crit"
            print(f"    {lab:<36} {rho:+.2f} +/- {sd:.2f}   {says}")

    # The one-sample t-test over the five per-seed rho values is the obvious
    # alternative rule, because it needs only the printed mean and SD.
    tcrit = stats.t.ppf(1 - ALPHA / 2, N_SEEDS - 1)
    thresh = tcrit / math.sqrt(N_SEEDS)
    err = sum(1 for _l, rho, sd, bold in recs
              if ((abs(rho) / sd >= thresh) if sd > 0 else True) != bold)
    print()
    print(f"  alternative rule: one-sample t over {N_SEEDS} seeds, "
          f"|rho|/SD >= t_.975,{N_SEEDS - 1}/sqrt({N_SEEDS}) = {thresh:.4f}")
    print(f"    disagrees with the bolding on {err} of {len(recs)} cells")
    print()
    return recs, inv_rho


def main() -> int:
    print(__doc__.split("What is computed")[0].strip())
    print()
    print(f"schedule: {TOTAL_STEPS:,} steps, checkpoint every {CADENCE} "
          f"=> at most {TOTAL_STEPS // CADENCE + 1} checkpoints per run")
    print(f"alpha = {ALPHA}, two-sided; exact permutation critical values "
          f"for n <= {EXACT_MAX_N}, t-approximation above")
    print()

    print("Reference: critical |rho| for a two-sided Spearman test at 0.05")
    print(f"  {'n':>5}  {'exact':>9}  {'t-approx':>9}  {'Fisher-z':>9}")
    for n in (5, 6, 7, 8, 9, 10, 13, 16, 21, 26, 31, 41, 61, 81, 101, 121, 200):
        ex = f"{rho_crit_exact(n):9.4f}" if n <= EXACT_MAX_N else f"{'-':>9}"
        print(f"  {n:>5}  {ex}  {rho_crit_t(n):9.4f}  {rho_crit_fisher(n):9.4f}")
    print()

    r1, inv1 = report("TABLE 1 (Transformer)", TABLE1, TABLE1_COLS)
    r2, inv2 = report("TABLE 2 (MLP)", TABLE2, TABLE2_COLS)

    print("=" * 78)
    print("BOTH TABLES")
    print("=" * 78)
    allr = r1 + r2
    print(f"  {len(allr)} correlation cells, "
          f"{sum(1 for r in allr if r[3])} marked p < 0.05, no correction for "
          f"multiplicity")
    print(f"  inversion pairs: {len(inv1)} in Table 1, {len(inv2)} in Table 2 "
          f"-- {len({b[0] for b, _u in inv1 + inv2})} distinct bolded cells are "
          f"weaker than some unbolded cell in the same table")
    print()
    print("  Table 1's ticketed pair, spelled out:")
    for lab, rho, sd, bold in r1:
        if lab.startswith("H1 Total / Embed / 10%") or \
           lab.startswith("H1 Total / Layer 1 / 0%"):
            mark = "BOLDED (p < 0.05)" if bold else "not bolded"
            need = next(n for n in range(4, 5001) if rho_crit(n) <= abs(rho))
            last = max(n for n in range(4, 5001) if rho_crit(n) > abs(rho))
            print(f"    {lab:<28} {rho:+.2f} +/- {sd:.2f}  {mark}")
            print(f"      significant only if n >= {need}; "
                  f"insignificant only if n <= {last}")
    print()
    jb = best_n(allr)
    err, n, c = jb[0]
    ties = [x[1] for x in jb if x[0] == err]
    print(f"  best single n for both tables at once: n = {n} "
          f"(rho_crit = {c:.4f}), {err} of {len(allr)} cells wrong "
          f"(minimum attained on n = {min(ties)}..{max(ties)})")
    print()
    print("  A cell can be bolded at SOME feasible n only if |rho| >= "
          f"rho_crit(121) = {rho_crit(121):.4f}.")
    impossible = [(lab, rho, sd) for lab, rho, sd, bold in allr
                  if bold and abs(rho) < rho_crit(121)]
    print(f"  Bolded cells below that ceiling (impossible at ANY n the "
          f"schedule allows): {len(impossible)}")
    for lab, rho, sd in impossible:
        print(f"    {lab:<36} {rho:+.2f} +/- {sd:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
