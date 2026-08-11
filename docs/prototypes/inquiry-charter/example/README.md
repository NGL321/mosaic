---
# THE FILE THAT FREEZES.
#
# Nothing here is signed. After #164 the Inquiry charter carries no human hand at all:
# the Question is agent-drafted, the Adequacy Criterion is apparatus, and both are frozen
# by ANCESTRY rather than by signature. Noah's hand is one level up, on the Conjecture.
#
# Everything above the closing `---` is what the dispatch gate reads. Everything below it
# is prose for a reader — including the reader who arrives months later, at a stall.

inquiry: 172                       # = this Inquiry's issue number. See "Numbering" below.
slug: formation-signature-grokking
opened: 2026-08-11

# What this bridges toward. A LIST, never a scalar: one Inquiry may serve many
# Conjectures, because an axiom is not owned by the system that bought it (#164).
# The first entry is the TRIGGERING conjecture — the one whose budget pays.
conjectures:
  - conjectures/043-formation-is-an-object

question: >
  Does the formation of a representation carry structure that the formed
  representation does not — that is, is there something to measure in the
  transition itself rather than in its endpoints?

# Agent-drafted, and the agent must say why it drafted this one. Not a gate: #164 made
# it a RECORDING requirement, surfaced to Noah at acknowledgement, where #9's relevance
# test asks whether the thing answered was worth answering.
question_rationale: >
  Conjecture 043 asserts that formation is a distinct object. The cheapest place to
  look for a formation-only signature is a system with a sharp, reproducible transition
  and a network small enough to instrument exhaustively; grokking on modular addition
  is the standard such system.

# Optional. Agent-drafted like the Question. An Inquiry may run without one — and when
# one is a promotion of an earlier exploratory result, that promotion is Noah's act
# (premise 3) and is recorded on the Conjecture, not here.
hypothesis:
  committed: 2026-08-11
  statement: >
    In a small transformer trained past memorisation to generalisation on modular
    addition, the hidden-state point cloud carries a transient first-homology
    feature that rises and falls across the generalisation transition, and is
    absent from both the memorising and the generalised network.

# The sentence this Inquiry will contribute to its Conjectures' systems if the
# discriminating measurement carries. Rendered formally once #166 fixes the language;
# prose placeholder until then, and #165 is what checks it.
axiom_if_carried: >
  The signature is present in the training trajectory and absent from
  final-checkpoint representations.

# ---------------------------------------------------------------------------
# ADEQUACY. Hypothesis-blind by SCOPE, not by inspection: the gate refuses any name
# here that also appears under `hypothesis`, `axiom_if_carried` or `discriminating`.
# Agents tune anything reachable from here, freely, until it passes. Passing ends the
# search and freezes the config. Frozen at OPEN, so the agents that search against it
# are not the agent that wrote it — which is what #61's open-gap measure rests on.
# ---------------------------------------------------------------------------
adequacy:
  probe: probes/planted_cycle_recovery.py
  decides: planted_cycle_recovered
  threshold: ">= 0.90"
  over: 20 synthetic activation sets

  # #9, via #61: a mandatory clause, not an optional one. A novel measure must show
  # predictive content the cheapest available measure does not already carry, with the
  # confound set named before the data exists. Hypothesis-blind, so it fires DURING
  # search — discarding an instrument that was measuring weight norm all along while
  # agents are still free to try others.
  reduction_check:
    against:
      - probes/baseline_weight_norm.py
      - probes/baseline_logit_margin.py
      - probes/baseline_pca_variance.py
    requires: >
      Residual predictive content over the union of the baselines, at the same
      threshold, on the same synthetic sets.

  # #9: testable hazards become further adequacy clauses; untestable hazards are
  # DECLARED and attach permanently to every leg this Inquiry earns. A hazard you must
  # test is a cost; a hazard you must name is not, which is what keeps naming truthful.
  hazards:
    testable:
      - name: subsampling_artefact
        probe: probes/hazard_subsample_stability.py
        requires: "Verdict stable across 3 disjoint subsamples."
    untestable:
      - name: layer_choice_is_unprincipled
        statement: >
          No theory selects which layer's activations carry a formation signature.
          Any leg this Inquiry earns is held by an instrument whose layer was chosen
          because it worked, and that travels with the claim.

  # PROSE, and the gate does not read it. This is the field Noah actually reads — see
  # "What this field is for" below. It is not decoration and it is not the rationale
  # for the hypothesis.
  rationale: >
    A positive control on the instrument alone. Synthetic activations are built with a
    circle planted in them at the dimensionality and noise level the real network
    produces; the instrument is adequate if it recovers the planted circle nine times
    in ten, and if it does so for reasons the three baselines do not already supply.
    This says nothing about whether the network has such structure — only whether the
    apparatus could see it if it did. If it could not, a null from this Inquiry is
    evidence about the apparatus and about nothing else.

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

custody:
  frozen_at_open:
    - question
    - hypothesis
    - axiom_if_carried
    - adequacy
    - discriminating
    - placement
  agent_writable:
    - configs/
    - probes/
    - runs/
  # Dispatch state, search progress and reports live on the issue, not here.
  # Budget, stall tolerance and the continue/return/retire rule live on the
  # Conjecture, not here — the gate refuses a charter that declares any of them.
  issue: https://github.com/NGL321/mosaic/issues/172
---

# Inquiry 172 — a formation signature in grokking

**This is a prototype's worked example, not a live Inquiry.** It exists to be reacted
to on [#60](https://github.com/NGL321/mosaic/issues/60). The phenomenon it names is
deliberately one of the two still open under
[#17](https://github.com/NGL321/mosaic/issues/17) and commits the programme to nothing.

## What falsifies the claim this serves

`inquiries/README.md` asks for "the claim this serves, and what would falsify it." After
[#164](https://github.com/NGL321/mosaic/issues/164) the thing served is a **Conjecture**,
not a Belt claim, and the falsifier lives with it — conjecture falsifiers are
agent-drafted and Noah-signed at posting ([#9](https://github.com/NGL321/mosaic/issues/9),
[#61](https://github.com/NGL321/mosaic/issues/61)); rung falsifiers are his own words, much
later, at admission ([#59](https://github.com/NGL321/mosaic/issues/59)). What this charter
holds is the **decision rule**, which is the falsifier's local, machine-checkable shadow:
below the stated factor, the hypothesis is refused for this instrument.

## What the `adequacy.rationale` field is for

It is the only field here written for a human, and it carries more weight than its
position suggests.

[#61](https://github.com/NGL321/mosaic/issues/61) rules that accumulated instrument
failure is evidence about the **perspective**, that this inference is core-directed, and
that therefore **no agent may ever draw it**. The signal reaches Noah through coverage
reports and his own reading of them, or it reaches nobody. A stall return carries the
instrument-null accumulation *uninterpreted*, and at that moment somebody is comparing
twenty positive controls across a bridge that died.

So this field is written to be read **then** — months later, in aggregate, against
nineteen others — and not to be read now. That is a different requirement from
machine-decidability, and the two pull apart: `probe` + `threshold` is maximally decidable
and nearly useless to compare. Nothing in the gate can enforce this, which is the point at
which the format stops being able to help.

## The freeze

The search ends when `adequacy` passes. At that moment the winning configuration is
committed as `config.yaml` — the appearance of that file *is* the freeze, and its
position in git ancestry is what makes the discriminating result confirmatory. Before it
exists there is no frozen instrument; after it exists, changing it is a new Inquiry.

If the Adequacy Criterion turns out to be unsatisfiable, the Inquiry ends **`Exhausted`**
with a coverage report saying so — a real finding.
[#61](https://github.com/NGL321/mosaic/issues/61): agents may propose and may never amend.

## Numbering

`NNN` is the Inquiry's **issue number**, allocated by the tracker. This matters more than
it did before [#164](https://github.com/NGL321/mosaic/issues/164): agents now open
Inquiries themselves, under a posted Conjecture's authority, so two concurrent sessions
allocating a directory number is a live collision rather than a theoretical one. The
tracker is the only allocator both can see. Cost: the numbers are sparse.

Fan-out does not stress numbering at all — a fan-out is many Runs of one Inquiry, and
`conjectures/` numbers independently.
