---
conjecture: 58
slug: reconciliation-not-voting
posted: 2026-08-12
statement: >
  Schemas reconcile rather than vote.
falsifier: >
  A consensus mechanism accounts for every observed cross-schema settlement.
formal_rendering: >
  forall S . settle(S) -> reconcile(S) and not vote(S)
governor:
  token_allocation: 5_000_000
  spend_ceiling_usd: 5
  stall_tolerance_tokens: 2_000_000

# #16 barred this from admission: it distinguishes Mosaic from someone else's theory.
barred: >
  Distinguishes Mosaic from someone else's theory (#16). May earn legs; may never
  become a rung.
---

# Conjecture 058 — reconciliation, not voting

Fixture. Posted, no Inquiry bridges toward it — the unbridged case.
