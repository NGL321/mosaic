---
inquiry: 178
slug: trajectory-invariance
opened: 2026-08-14

# Serves 043 only. This is 043's SECOND leg — the one that keeps 043 standing when
# 172's axiom is retracted, while 051 falls.
conjectures:
  - conjectures/043-formation-is-an-object

question: >
  Is the trajectory signature invariant across architectures at matched task?

axiom_if_carried: >
  The trajectory signature appears at matched task across two architectures.

domain: ml

adequacy:
  probe: probes/matched_task_control.py
  decides: task_matched
  threshold: ">= 0.95"
  hazards:
    testable: []
    untestable: []

discriminating:
  metric: probes/signature_presence.py
  decision_rule: >
    Signature present in both architectures at matched task accuracy.
  seeds: 6
---

# Inquiry 178 — fixture
