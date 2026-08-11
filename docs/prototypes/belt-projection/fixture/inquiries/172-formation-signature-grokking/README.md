---
# Fixture charter, trimmed to the fields the projection reads. The full shape is in
# docs/prototypes/inquiry-charter/example/. Frozen at open — nothing is appended here,
# which is why the axiom's life is in axiom.md beside it.
inquiry: 172
slug: formation-signature-grokking
opened: 2026-08-13

# A LIST. The first entry is the triggering conjecture, whose budget pays.
# This Inquiry serves TWO conjectures — the case #90 turns on.
conjectures:
  - conjectures/043-formation-is-an-object
  - conjectures/051-topology-carries-no-content

question: >
  Does the formation of a representation carry structure the formed
  representation does not?

axiom_if_carried: >
  The signature is present in the training trajectory and absent from
  final-checkpoint representations.

domain: ml

adequacy:
  probe: probes/planted_cycle_recovery.py
  decides: planted_cycle_recovered
  threshold: ">= 0.90"
  hazards:
    testable:
      - name: subsampling_artefact
        probe: probes/hazard_subsample_stability.py
    untestable:
      - name: layer_choice_is_unprincipled
        statement: >
          No theory selects which layer's activations carry a formation
          signature. Any leg this Inquiry earns is held by an instrument whose
          layer was chosen because it worked, and that travels with the claim.

discriminating:
  metric: probes/h1_lifetime_trajectory.py
  decision_rule: >
    Peak H1 lifetime exceeds the 95th percentile of the label-shuffled control
    by a factor of 2 or more, in at least 8 of 10 seeds.
  seeds: 10
---

# Inquiry 172 — fixture
