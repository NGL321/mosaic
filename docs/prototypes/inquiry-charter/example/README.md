---
# THE FROZEN PART. Noah's hand, and nothing else's.
# Everything below the `---` is prose for a reader; everything above it is what the
# dispatch gate reads. No agent may write to this file — see `custody` below.

inquiry: 160
slug: formation-signature-grokking
opened: 2026-08-10
signed_by: NGL321

question: >
  Does the formation of a representation carry structure that the formed
  representation does not — that is, is there something to measure in the
  transition itself rather than in its endpoints?

hypothesis:
  committed: 2026-08-10
  statement: >
    In a small transformer trained past memorisation to generalisation on modular
    addition, the hidden-state point cloud carries a transient first-homology
    feature that rises and falls across the generalisation transition, and is
    absent from both the memorising and the generalised network.
  falsified_by: >
    A run reaching the generalisation transition in which H1 lifetime never leaves
    the noise band established by the label-shuffled control.

# ---------------------------------------------------------------------------
# ADEQUACY. Hypothesis-blind by SCOPE, not by inspection: the gate refuses any
# name here that also appears under `hypothesis` or `discriminating`. Agents tune
# anything reachable from here, freely, until it passes. Passing ends the search.
# ---------------------------------------------------------------------------
adequacy:
  probe: probes/planted_cycle_recovery.py
  decides: planted_cycle_recovered
  threshold: ">= 0.90"
  over: 20 synthetic activation sets
  rationale: >
    A positive control on the instrument alone. Synthetic activations are built
    with a circle planted in them at the dimensionality and noise level the real
    network produces; the instrument is adequate if it recovers the planted circle
    nine times in ten. This says nothing about whether the network has such
    structure — only whether the apparatus could see it if it did.

# ---------------------------------------------------------------------------
# THE DISCRIMINATING MEASUREMENT. Never run before the freeze.
# ---------------------------------------------------------------------------
discriminating:
  metric: probes/h1_lifetime_trajectory.py
  decision_rule: >
    Peak H1 lifetime, over the epochs spanning the generalisation transition,
    exceeds the 95th percentile of the label-shuffled control by a factor of 2 or
    more, in at least 8 of 10 seeds. Below that factor, or in fewer than 8 seeds,
    the hypothesis is refused for this instrument.
  seeds: 10

budget:
  experiments: 40          # instrument configurations tried during Searching
  gpu_hours: 25            # against the programme's $50/month ceiling
  wall_clock_days: 14

# A requirement, never a tier. The gate refuses the name of a runner.
environment_requirement:
  accelerator: "CUDA, >= 16 GB VRAM"
  network: allowed
  notes: "Single card. No multi-node, no interconnect requirement."

# The mechanism half of the DUA rule. An agent may never widen this.
placement:
  tier: open
  basis: >
    Synthetic data and a network trained from scratch. No human-subjects data, no
    third-party dataset, nothing under a DUA.

# Agent-drafted, human-signed. May name the Question and the declared metrics.
# May not name the Hard Core — the gate refuses it, so the Negative Heuristic
# holds by construction rather than by obedience. The mandatory Hard-Core return
# is deliberately NOT written here: it is loop behaviour, identical for every
# Inquiry, and a charter that restates it is making policy that is not its to make.
continue_return_retire:
  signed_by: NGL321
  continue: >
    While instruments remain untried in the declared family and the budget holds.
  return: >
    On the first instrument that passes adequacy — the freeze is a return, not a
    handover.
  retire: >
    On budget exhaustion with no instrument passing adequacy, returning a coverage
    report. Retirement is Noah's signature, never the loop's.

custody:
  frozen: this file
  agent_writable:
    - configs/
    - probes/
    - runs/
  # Dispatch state, search progress and reports live on the issue, not here.
  issue: https://github.com/NGL321/mosaic/issues/160
---

# Inquiry 160 — a formation signature in grokking

**This is a prototype's worked example, not a live Inquiry.** It exists to be reacted
to on [#60](https://github.com/NGL321/mosaic/issues/60). The phenomenon it names is
deliberately one of the two still open under
[#17](https://github.com/NGL321/mosaic/issues/17) and commits the programme to nothing.

## The claim this serves, and what would falsify it

Formation and structure are different objects, and the programme has to decide which
one it is studying. If the transition carries structure the endpoints do not, then
formation is measurable in its own right and is a legitimate object; if the only
signal is in the endpoints, the question collapses into the ordinary one about
learned representations, and this line retires.

The falsifier is stated above in machine-readable form, and it is stated as a
property of the *measurement* rather than of the theory, because that is the only
form the register check can be run against.

## What is not decided here

The **instrument** is not decided here, on purpose. Which persistence library, which
layer, which pooling, which subsampling, what dimensionality reduction before the
filtration, how many epochs to sample across the transition, what the noise band is
built from — all of it is reachable from `adequacy`, all of it is the agents' to
search, and none of it may be argued for from the hypothesis. That is the whole of
the delegation: the Question is frozen, the apparatus is free.

## The freeze

The search ends when `adequacy` passes. At that moment the winning configuration is
committed as `config.yaml` — the appearance of that file *is* the freeze, and its
position in git ancestry is what makes the discriminating result confirmatory.
Before it exists there is no frozen instrument; after it exists, changing it is a new
Inquiry, not an amendment to this one.
