---
inquiry: 181
slug: schema-count-stability
opened: 2026-08-15

conjectures:
  - conjectures/043-formation-is-an-object

question: >
  Is the recovered schema count stable across seeds at matched ground truth?

axiom_if_carried: >
  Recovered schema counts agree across seeds at matched synthetic ground truth.

domain: synthetic

adequacy:
  probe: probes/planted_count_recovery.py
  decides: count_recovered
  threshold: ">= 0.90"
  hazards:
    testable: []
    untestable:
      - name: generator_encodes_the_prior
        statement: >
          The synthetic generator's ground truth is itself a schema
          decomposition, so the instrument may be scoring its own prior.

discriminating:
  metric: probes/count_agreement.py
  decision_rule: >
    Counts agree in at least 9 of 10 seeds.
  seeds: 10
---

# Inquiry 181 — fixture. Opened, never carried: the Searching case.
