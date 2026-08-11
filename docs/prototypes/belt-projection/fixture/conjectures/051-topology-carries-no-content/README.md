---
conjecture: 51
slug: topology-carries-no-content
posted: 2026-08-12
statement: >
  Persistent homology on grokking representations carries no predictive content
  beyond effective rank.
falsifier: >
  A filtration whose residual beats effective rank at matched compute.
formal_rendering: >
  forall F . filtration(F) -> not residual_over(F, effective_rank)
governor:
  token_allocation: 15_000_000
  spend_ceiling_usd: 10
  stall_tolerance_tokens: 5_000_000
---

# Conjecture 051 — topology carries no content

Fixture. Shares Inquiry 172 with 043, and has no second leg — which is the case that
separates per-leg death from node death.
