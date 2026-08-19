#!/usr/bin/env python3
"""
How far do (h_mu, E) move when the (p, 1-p) Bernoulli map is symbolised under a
partition other than the one at its kink?

Companion to docs/research/2026-08-02-bernoulli-map-generating-partition.md,
which discharges verification-debt ticket #106.

The map (the "skew Bernoulli map": the two-branch, full-branch, piecewise-linear
map of the unit interval):

    T(x) = x / p              for x in [0, p)
    T(x) = (x - p) / (1 - p)  for x in [p, 1)

Claim under audit: symbolised by the partition at the kink,
xi_kink = {[0, p), [p, 1)}, the symbol stream is i.i.d. Bernoulli(p), so
h_mu = H(p) and the excess entropy E = 0 exactly.

What this script measures, for the kink partition and for four deliberately
wrong two-cell threshold partitions xi_c = {[0, c), [c, 1)} with c != p:

  1. Block entropies H(L), L = 1..LMAX, by plug-in, hence
         h_L = H(L) - H(L-1)            (entropy rate, bits/symbol)
         E   = intercept of a straight-line fit to H(L) over the last
               FIT_WINDOW values of L.
     h_L is non-increasing in L and converges to h_mu(T, xi) from ABOVE, so a
     measured h_L strictly below H(p) is an upper bound proving that partition
     loses entropy — i.e. that it is NOT generating (Kolmogorov-Sinai,
     contrapositive).

  2. A direct test of generation: the measure-weighted mean diameter of the
     atoms of xi ∨ T^-1 xi ∨ ... ∨ T^-(L-1) xi, estimated as the spread of the
     orbit points that produced each observed length-L block. A partition is
     generating exactly when these diameters go to zero. For the kink partition
     the atoms are the map's cylinders, whose mean diameter must fall like
     (p^2 + (1-p)^2)^L; for a non-generating partition the diameters plateau at
     something of order 1, because distinct points share an itinerary forever.

  3. The trivial one-cell partition, as the degenerate control: it reports
     h_mu = 0 and E = 0, the reminder that "E = 0" on its own is equally
     consistent with measuring nothing at all.

Requires numpy only. Deterministic: fixed x0, no RNG. ASCII output.

    python docs/research/2026-08-02-bernoulli-map-partitions.py
"""

from __future__ import annotations

import math
import sys
import time

import numpy as np

P = 0.110028          # the map's parameter, as used by the document under audit
N_ITER = 4_000_000    # symbols kept
N_BURN = 100_000      # discarded transient
LMAX = 14             # longest block for the plug-in block entropy
FIT_WINDOW = 5        # H(L) ~ E + h*L is fitted over the last FIT_WINDOW values
DIAM_L = (2, 4, 6, 8, 10, 12, 14)   # L values at which atom diameters are measured
X0 = 0.31415926535897932  # arbitrary; not a preimage of any threshold used below


def orbit(p: float, n: int, burn: int, x0: float) -> np.ndarray:
    """The forward orbit of the (p, 1-p) map, in float64, after a burn-in."""
    x = x0
    q = 1.0 - p
    for _ in range(burn):
        x = x / p if x < p else (x - p) / q
    out = np.empty(n, dtype=np.float64)
    for i in range(n):
        out[i] = x
        x = x / p if x < p else (x - p) / q
    return out


def block_codes(sym: np.ndarray, lmax: int, alphabet: int = 2):
    """
    Yield (L, codes) where codes[i] is the integer code of the length-L block of
    `sym` starting at i. Extended one symbol at a time, so no L-fold copy of the
    series is ever materialised.
    """
    sym = sym.astype(np.int64)
    cur = sym.copy()
    for L in range(1, lmax + 1):
        if L > 1:
            cur = cur[:-1] * alphabet + sym[L - 1:]
        yield L, cur


def plug_in_entropy(codes: np.ndarray, size: int) -> tuple[float, int]:
    """(plug-in entropy in bits, number of occupied blocks)."""
    counts = np.bincount(codes, minlength=size)
    counts = counts[counts > 0]
    q = counts / counts.sum()
    return float(-(q * np.log2(q)).sum()), int(len(counts))


def atom_diameter(codes: np.ndarray, xs: np.ndarray) -> tuple[float, float]:
    """
    (measure-weighted mean, max) diameter of the observed atoms.

    codes[i] labels the length-L block starting at orbit point xs[i]; the atom
    of the refined partition carrying that label contains xs[i]. Sorting by code
    groups the orbit points by atom; the spread within a group estimates the
    diameter of the atom, and the group's share of the orbit estimates its
    measure.
    """
    order = np.argsort(codes, kind="stable")
    c = codes[order]
    v = xs[order]
    starts = np.flatnonzero(np.r_[True, c[1:] != c[:-1]])
    lo = np.minimum.reduceat(v, starts)
    hi = np.maximum.reduceat(v, starts)
    weight = np.diff(np.r_[starts, len(c)]) / len(c)
    d = hi - lo
    return float((weight * d).sum()), float(d.max())


def fit_rate_and_excess(hs: list[float], window: int) -> tuple[float, float]:
    """Least-squares fit of H(L) = E + h*L over the last `window` values of L."""
    L = np.arange(len(hs) - window + 1, len(hs) + 1, dtype=np.float64)
    H = np.asarray(hs[-window:], dtype=np.float64)
    h, e = np.polyfit(L, H, 1)
    return float(h), float(e)


def shannon(p: float) -> float:
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def flatness(x: np.ndarray, bins: int = 1000) -> float:
    """Max relative deviation of the orbit's histogram from a uniform density."""
    counts, _ = np.histogram(x, bins=bins, range=(0.0, 1.0))
    expected = len(x) / bins
    return float(np.abs(counts - expected).max() / expected)


def analyse(xs: np.ndarray, c: float | None, lmax: int, diam_at=()):
    """Block entropies (and optionally atom diameters) for one threshold."""
    if c is None:
        sym = np.zeros(len(xs), dtype=np.int8)
        alphabet = 1
    else:
        sym = (xs >= c).astype(np.int8)
        alphabet = 2
    hs, occ, diam = [], [], {}
    for L, codes in block_codes(sym, lmax, alphabet):
        h, m = plug_in_entropy(codes, alphabet ** L)
        hs.append(h)
        occ.append(m)
        if L in diam_at:
            diam[L] = atom_diameter(codes, xs[: len(codes)])
    return sym, hs, occ, diam


def main() -> int:
    t0 = time.time()
    p = P
    hp = shannon(p)
    print(f"(p, 1-p) Bernoulli map,  p = {p!r}")
    print(f"iterates kept = {N_ITER:,}   burn-in = {N_BURN:,}   Lmax = {LMAX}")
    print(f"H(p) = {hp:.8f} bits   (the h_mu the claim under audit asserts)")
    print()

    x = orbit(p, N_ITER, N_BURN, X0)

    # Lebesgue is asserted to be the invariant measure, so the orbit's histogram
    # should be flat and the time spent in [0, p) should be p.
    print("orbit diagnostics")
    print(f"  mean x                       {x.mean():.6f}   (uniform: 0.500000)")
    print(f"  fraction of time in [0, p)   {(x < p).mean():.6f}   (Lebesgue: {p:.6f})")
    print(f"  max deviation from uniform   {flatness(x) * 100:.2f}%  over 1000 bins")
    print()

    partitions: list[tuple[str, float | None]] = [
        ("kink       c = p", p),
        ("midpoint   c = 0.5", 0.5),
        ("quarter    c = 0.25", 0.25),
        ("near-kink  c = 0.15", 0.15),
        ("far        c = 0.90", 0.90),
        ("trivial    one cell", None),
    ]

    rows, per_L, per_D = [], {}, {}
    for name, c in partitions:
        sym, hs, occ, diam = analyse(x, c, LMAX, DIAM_L)
        h_fit, e_fit = fit_rate_and_excess(hs, FIT_WINDOW)
        # Miller-Madow: the plug-in H is biased low by about (m-1)/(2 N ln 2)
        # bits with m occupied blocks, so h_L = H(L)-H(L-1) is biased low by
        # about (m_L - m_{L-1})/(2 N ln 2). Correcting it makes the small gaps
        # between a partition's h_L and H(p) defensible rather than assumed.
        n_eff = N_ITER - LMAX + 1
        mm = (occ[-1] - occ[-2]) / (2 * n_eff * math.log(2))
        rows.append((name, hs[0], hs[-1] - hs[-2], hs[-1] - hs[-2] + mm,
                     h_fit, e_fit, float(sym.mean()), occ[-1]))
        per_L[name] = hs
        per_D[name] = diam

    print("Table 1. Coordinates under each partition")
    print("  h_L = H(14)-H(13); h_MM is h_L with the Miller-Madow bias correction;")
    print("  h_fit, E_fit from a %d-point fit of H(L)=E+h*L; m14 = occupied blocks."
          % FIT_WINDOW)
    print("  h_L (and h_MM) is an UPPER bound on h_mu for that partition, because")
    print("  L -> H(L)-H(L-1) is non-increasing and converges to h_mu from above.")
    print()
    hdr = (f"{'partition':<21}{'P(sym=1)':>10}{'H(1)':>9}{'h_L':>9}{'h_MM':>9}"
           f"{'h_fit':>9}{'E_fit':>9}{'h_MM-H(p)':>11}{'m14':>8}")
    print(hdr)
    print("-" * len(hdr))
    for name, h1, h_last, h_mm, h_fit, e_fit, freq, m14 in rows:
        print(f"{name:<21}{freq:>10.5f}{h1:>9.5f}{h_last:>9.5f}{h_mm:>9.5f}"
              f"{h_fit:>9.5f}{e_fit:>9.5f}{h_mm - hp:>11.5f}{m14:>8d}")
    print("-" * len(hdr))
    print(f"{'asserted: H(p), E=0':<21}{'':>10}{'':>9}{'':>9}{'':>9}"
          f"{hp:>9.5f}{0.0:>9.5f}")
    print()

    names = [n for n, _ in partitions]
    short = [n.split()[0] for n in names]

    print("Table 2. H(L), bits")
    print("  L  " + "".join(f"{s:>11}" for s in short))
    for i in range(LMAX):
        print(f" {i + 1:>2}  " + "".join(f"{per_L[n][i]:>11.5f}" for n in names))
    print()

    print("Table 3. H(L) - L*H(p)  -- flat at 0 iff the stream is exactly")
    print("         i.i.d. Bernoulli(p), which is what the claim asserts")
    print("  L  " + "".join(f"{s:>11}" for s in short))
    for i in range(LMAX):
        print(f" {i + 1:>2}  " + "".join(f"{per_L[n][i] - (i + 1) * hp:>11.5f}"
                                        for n in names))
    print()

    print("Table 4. Measure-weighted mean diameter of the atoms of the L-fold")
    print("         refinement. Generating <=> this goes to 0. The kink column's")
    print("         predicted value is (p^2 + (1-p)^2)^L, printed for comparison.")
    print("  L  " + "".join(f"{s:>11}" for s in short) + f"{'kink pred':>11}")
    for L in DIAM_L:
        pred = (p * p + (1 - p) ** 2) ** L
        cells = "".join(f"{per_D[n][L][0]:>11.5f}" for n in names)
        print(f" {L:>2}  " + cells + f"{pred:>11.5f}")
    print()

    # Plug-in block entropy is biased low by about (m-1)/(2 N ln 2) bits for m
    # occupied blocks. Quartering the sample shows how much of each reported E is
    # that bias rather than structure: a true E moves little, a bias artefact
    # moves a lot.
    print("Table 5. Finite-sample check: same estimates on the first quarter")
    print("         of the orbit (1,000,000 iterates)")
    hdr2 = f"{'partition':<21}{'h_fit(N/4)':>12}{'E_fit(N/4)':>12}{'E(N/4)-E(N)':>13}"
    print(hdr2)
    print("-" * len(hdr2))
    quarter = x[: N_ITER // 4]
    for (name, c), row in zip(partitions, rows):
        _s, hs, _o, _d = analyse(quarter, c, LMAX)
        h4, e4 = fit_rate_and_excess(hs, FIT_WINDOW)
        print(f"{name:<21}{h4:>12.5f}{e4:>12.5f}{e4 - row[5]:>13.5f}")
    print("-" * len(hdr2))
    print()
    print(f"[{time.time() - t0:.1f} s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
