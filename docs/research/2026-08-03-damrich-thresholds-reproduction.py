#!/usr/bin/env python3
"""Reproduce the three failure thresholds the #4 survey read off Damrich, Berens &
Kobak (NeurIPS 2024), and check whether they hold at the n a Mosaic ECA study would
have rather than at the paper's n = 1000. Discharges #47.

The paper's own code is https://github.com/berenslab/eff-ph. It is used as the
specification, not as a library: `utils/dist_utils.py` imports `umap`, `openTSNE`
and the authors' `vis_utils` package at module scope for distances this script does
not need, and `utils/utils.py` shells out to a *modified* Ripser build (the
interval-matching fork) for representative cocycles this script does not need
either. So the three data/distance functions are transcribed verbatim below with
their source line numbers, and persistence is computed with the `ripser` PyPI
package.

**What is transcribed, and from where** (eff-ph @ 5ecd52a, the current head of
`main` at the time of writing):

    get_circle             utils/toydata_utils.py:8
    add_gaussian           utils/toydata_utils.py:236
    get_toy_data (circle)  utils/toydata_utils.py:315
    get_fermat_dist        utils/dist_utils.py:177
    get_dtm                utils/dist_utils.py:158
    get_dtm_weights        utils/dist_utils.py:115
    get_features_above_gap utils/pd_utils.py:452
    wide_gap_score         utils/pd_utils.py:479

Hyperparameters are `scripts/compute_ph.py`'s defaults: `toy_circle`, n = 1000,
seeds [0, 1, 2], `max_dim` = 1.

    python docs/research/2026-08-03-damrich-thresholds-reproduction.py
"""

from __future__ import annotations

import argparse
import json
import sys
import time

import numpy as np
import scipy.sparse as sp
from ripser import ripser
from scipy.spatial.distance import pdist, squareform

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass


# ---------------------------------------------------------------------------
# Data — utils/toydata_utils.py
# ---------------------------------------------------------------------------


def get_circle(n=1000, r=1.0):
    """utils/toydata_utils.py:8, verbatim."""
    theta = np.linspace(0, 2 * np.pi, n)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.stack([x, y], axis=1)


def add_gaussian(x, sigma=0.1, seed=0):
    """utils/toydata_utils.py:236, verbatim."""
    np.random.seed(seed)
    return x + np.random.normal(0, sigma, size=x.shape)


def get_orthonormal_basis(out_d=50, in_d=2, seed=0):
    """utils/toydata_utils.py:288, verbatim. Gram-Schmidt on random vectors."""
    assert out_d >= in_d
    np.random.seed(seed)
    basis = np.random.randn(in_d, out_d)
    for i, _ in enumerate(basis):
        basis[i] /= np.linalg.norm(basis[i])
        for j, _ in enumerate(basis):
            if j <= i:
                continue
            basis[j] = basis[j] - np.dot(basis[i], basis[j]) * basis[i]
            assert np.allclose(np.dot(basis[i], basis[j]), 0)
    return basis


def toy_circle(n, d, sigma, seed):
    """utils/toydata_utils.py:315 `get_toy_data`, narrowed to `toy_circle` + gaussian.

    The embedding is the paper's: the 2-d circle is mapped through a *random
    orthonormal* basis into the ambient dimension d, and the noise is then added in
    **all** d dimensions. That is the whole point of the experiment — noise off the
    manifold, in every direction. The basis and the noise share a seed, exactly as
    `get_toy_data` does it.
    """
    data = get_circle(n, r=1.0)
    basis = get_orthonormal_basis(out_d=d, in_d=2, seed=seed)
    data = np.dot(data, basis)
    return add_gaussian(data, sigma=sigma, seed=seed)


# ---------------------------------------------------------------------------
# Distances — utils/dist_utils.py
# ---------------------------------------------------------------------------


def get_fermat_dist(x, p, input_distance="euclidean"):
    """utils/dist_utils.py:177, verbatim."""
    d_input = squareform(pdist(x, metric=input_distance))
    return sp.csgraph.shortest_path(d_input**p, directed=False)


def get_dtm(x, k, p=np.inf, input_distance="euclidean"):
    """utils/dist_utils.py:158. Distance to measure: aggregate of the k nearest
    neighbour distances under an `l_p` mean."""
    d = squareform(pdist(x, metric=input_distance))
    knn_d = np.sort(d, axis=1)[:, 1 : k + 1]
    if np.isinf(p):
        return knn_d.max(axis=1)
    return (knn_d**p).mean(axis=1) ** (1 / p)


def get_dtm_weights(x, k, p_dtm=np.inf, p_radius=np.inf, input_distance="euclidean"):
    """utils/dist_utils.py:115, verbatim below the `get_dtm` call."""
    dtm = get_dtm(x, k, p=p_dtm, input_distance=input_distance)
    d = squareform(pdist(x, metric=input_distance))
    dtm_x, dtm_y = np.meshgrid(dtm, dtm)

    if np.isinf(p_radius):
        dtm_diff = np.maximum(dtm_x, dtm_y)
    else:
        dtm_diff = np.abs(dtm_x**p_radius - dtm_y**p_radius) ** (1 / p_radius)

    mask_singleton = d <= dtm_diff

    if p_radius == 1:
        mixed_filt_val = (dtm_x + dtm_y + d) / 2
    elif p_radius == 2:
        mixed_filt_val = np.sqrt(
            ((dtm_x + dtm_y) ** 2 + d**2) * ((dtm_x - dtm_y) ** 2 + d**2)
        ) / (2 * d + np.eye(len(d)) + 1e-10)
    elif p_radius == np.inf:
        mixed_filt_val = np.stack([dtm_x, dtm_y, d / 2], axis=0).max(0)
    else:
        raise ValueError("p must be 1, 2 or np.inf")

    return np.maximum(dtm_x, dtm_y) * mask_singleton + mixed_filt_val * ~mask_singleton


def get_dist(x, distance, **kw):
    if distance == "euclidean":
        return squareform(pdist(x, metric="euclidean"))
    if distance == "fermat":
        return get_fermat_dist(x, **kw)
    if distance == "dtm":
        return get_dtm_weights(x, **kw)
    raise ValueError(distance)


# ---------------------------------------------------------------------------
# Detection — utils/pd_utils.py
# ---------------------------------------------------------------------------


def get_features_above_gap(dgm, n_gap=0):
    """utils/pd_utils.py:452, verbatim."""
    life_times = dgm[:, 1] - dgm[:, 0]
    if n_gap >= len(life_times):
        return dgm
    idx_sorted = np.argsort(life_times)[::-1]
    life_times_sorted = life_times[idx_sorted]
    gap_sizes = life_times_sorted - np.concatenate([life_times_sorted[1:], [0]])
    largest_gap_idx = np.argsort(gap_sizes)[::-1][n_gap]
    return dgm[idx_sorted[: largest_gap_idx + 1]]


def wide_gap_score(dgm, n_gap=0, n_features=1):
    """utils/pd_utils.py:479, `mode="classification"`. 1 iff the number of features
    above the largest life-time gap is exactly the ground truth — here, one loop."""
    if len(dgm) == 0:
        return int(0 == n_features)
    return int(len(get_features_above_gap(dgm, n_gap=n_gap)) == n_features)


def h1(dist):
    dgm = ripser(dist, maxdim=1, distance_matrix=True)["dgms"][1]
    dgm = dgm[np.isfinite(dgm[:, 1])]
    return dgm


def detect(dist):
    """Returns (detected, relative persistence of the top feature).

    The second number is reported alongside the binary because the binary alone
    cannot tell "the loop is gone" from "the loop is there and a second feature is
    tied with it". `rel` is the top life time over the second-longest, which is what
    the paper's own figures show as a margin.
    """
    dgm = h1(dist)
    detected = wide_gap_score(dgm)
    if len(dgm) == 0:
        return detected, 0.0
    lt = np.sort(dgm[:, 1] - dgm[:, 0])[::-1]
    rel = float(lt[0] / lt[1]) if len(lt) > 1 and lt[1] > 0 else float("inf")
    return detected, rel


# ---------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------

SEEDS = [0, 1, 2]


def pure_noise(n, d, sigma, seed):
    """The null control: the same isotropic Gaussian, with **no circle under it.**

    `wide_gap_score` asks whether exactly one H1 feature sits above the largest gap
    in life times. It never asks whether that feature is the planted loop. On sparse
    data the answer can be yes because there is nothing to be confused by, so a
    detection rate is only interpretable against the rate this returns.
    """
    np.random.seed(seed)
    return np.random.normal(0, sigma, size=(n, d))


def run(cases, label, generator=None):
    rows = []
    print(f"\n### {label}", flush=True)
    for case in cases:
        n, d, sigma, distance, kw = case
        det, rel = [], []
        t0 = time.time()
        for seed in SEEDS:
            x = (generator or toy_circle)(n, d, sigma, seed)
            dist = get_dist(x, distance, **kw)
            a, b = detect(dist)
            det.append(a)
            rel.append(b)
        name = distance + ("" if not kw else "(" + ",".join(f"{k}={v}" for k, v in kw.items()) + ")")
        row = {"n": n, "d": d, "sigma": sigma, "distance": name,
               "detected": sum(det), "of": len(SEEDS),
               "rel_median": float(np.median(rel)), "secs": round(time.time() - t0, 1)}
        rows.append(row)
        print(f"  n={n:<5} d={d:<5} sigma={sigma:<5} {name:<34} "
              f"detected {sum(det)}/{len(SEEDS)}  rel={np.median(rel):.2f}  "
              f"({row['secs']}s)", flush=True)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="docs/research/2026-08-03-damrich-reproduction.json")
    ap.add_argument("--quick", action="store_true", help="skip the Fermat sweep")
    ap.add_argument("--seeds", type=int, default=3)
    args = ap.parse_args()
    global SEEDS
    SEEDS = list(range(args.seeds))

    out = {}

    # Claim (a): "performance degrades noticeably from d ~ 20, and for d >~ 30 no
    # persistent loop is found at all using Euclidean distances" at sigma = 0.25.
    out["a_dimension_sweep"] = run(
        [(1000, d, 0.25, "euclidean", {}) for d in (2, 5, 10, 20, 30, 40, 50, 100)],
        "(a) Euclidean, sigma = 0.25, ambient dimension sweep, n = 1000",
    )

    # Claim (b): DTM "collapsed at sigma ~ 0.15" and did worse than Euclidean on the
    # R^50 noisy circle. Run the paper's own grid rather than one config, so that a
    # failure is a failure of DTM and not of a hyperparameter choice.
    dtm_cfgs = [
        {"k": 4, "p_dtm": np.inf, "p_radius": np.inf},
        {"k": 15, "p_dtm": np.inf, "p_radius": np.inf},
        {"k": 100, "p_dtm": np.inf, "p_radius": np.inf},
        {"k": 15, "p_dtm": 2, "p_radius": 1},
        {"k": 100, "p_dtm": 2, "p_radius": 1},
    ]
    sigmas = [0.05, 0.10, 0.15, 0.20, 0.25]
    cases = [(1000, 50, s, "euclidean", {}) for s in sigmas]
    for cfg in dtm_cfgs:
        cases += [(1000, 50, s, "dtm", cfg) for s in sigmas]
    out["b_dtm"] = run(cases, "(b) DTM vs Euclidean on the R^50 circle, n = 1000")

    # Claim (c): Fermat distances "did not have any effect".
    if not args.quick:
        cases = [(1000, 50, s, "fermat", {"p": p}) for p in (1, 2, 3, 5, 7)
                 for s in (0.10, 0.25)]
        out["c_fermat"] = run(cases, "(c) Fermat on the R^50 circle, n = 1000")

    # #47's second half: do the thresholds hold at the n a Mosaic ECA study would
    # have (O(10^2)-O(10^3) points) rather than at the paper's n = 1000?
    cases = [(n, d, 0.25, "euclidean", {})
             for n in (100, 200, 500, 1000, 2000) for d in (20, 30, 50)]
    out["d_sample_size"] = run(cases, "(d) Euclidean, sigma = 0.25, n sweep at Mosaic's scale")

    # (e) The null control for (d). Same n, d and sigma, no circle underneath. A
    # detection rate here is the rate at which the criterion fires on nothing.
    out["e_null_control"] = run(
        [(n, d, 0.25, "euclidean", {}) for n in (100, 200, 500, 1000) for d in (20, 30, 50)],
        "(e) NULL CONTROL: isotropic Gaussian, no circle, same sigma",
        generator=pure_noise,
    )

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
