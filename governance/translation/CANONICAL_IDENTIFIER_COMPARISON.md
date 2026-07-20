# CANONICAL_IDENTIFIER_COMPARISON

**Document ID:** NAM-002

**Title:** Canonical Identifier Comparison

**Document Class:** Comparison

**Status:** COMPLETE

**Author:** Independent Architect

---

# 1. Candidate Evaluation

| # | Candidate | Semantic Precision | Architectural Precision | Ambiguity | Translation Friendliness | 10-Year Stability | Score |
|---|-----------|-------------------|------------------------|-----------|------------------------|-------------------|-------|
| 1 | Publication Engine | 7/10 — implies processing | 6/10 — misses coordination role | LOW | GOOD | GOOD | 30/50 |
| 2 | Publication Coordinator | 9/10 — assembles from producers | 9/10 — accurately describes role | LOW | GOOD | GOOD | 42/50 |
| 3 | Publication Orchestrator | 8/10 — implies control over flow | 8/10 — describes coordination | LOW | GOOD | GOOD | 40/50 |
| 4 | Publication Pipeline | 6/10 — implies sequential processing | 5/10 — misses assembly aspect | MEDIUM | GOOD | MEDIUM | 28/50 |
| 5 | Publication Processor | 7/10 — generic processing | 6/10 — misses coordination | LOW | GOOD | GOOD | 32/50 |
| 6 | Publication Manager | 6/10 — implies administration | 5/10 — wrong connotation | MEDIUM | GOOD | MEDIUM | 27/50 |
| 7 | Publication Dispatcher | 7/10 — implies sending | 7/10 — partially accurate | LOW | GOOD | GOOD | 34/50 |
| 8 | Publication Generator | 7/10 — implies creation | 6/10 — misses assembly | LOW | GOOD | GOOD | 32/50 |
| 9 | Publication Executor | 6/10 — implies running | 5/10 — misses coordination | LOW | GOOD | MEDIUM | 28/50 |
| 10 | Publication Core | 7/10 — implies centrality | 6/10 — generic | LOW | GOOD | GOOD | 32/50 |
| 11 | Publication Component | 5/10 — too generic | 4/10 — every component is a component | LOW | GOOD | MEDIUM | 22/50 |

---

# 2. External Architecture Comparison

| Pattern | Usage | Fit for SvitloSk? |
|---------|-------|-------------------|
| Martin Fowler — Coordinator | Coordinates multiple producers | GOOD FIT |
| Clean Architecture — Interactor | Contains business logic | PARTIAL FIT |
| DDD — Aggregate Root | Owns publication lifecycle | PARTIAL FIT |
| Microsoft — Orchestrator | Coordinates workflow | GOOD FIT |
| Google — Pipeline | Sequential processing | POOR FIT |
| AWS — Step Functions | Workflow coordination | GOOD FIT |
| CNCF — Controller | Manages desired state | PARTIAL FIT |

---

# 3. Key Insight

The Publication Engine's primary architectural pattern is **Coordinator** — it takes pre-produced outputs (data, schedules, graphics) from separate producers and assembles them into a final package. This is the classic Coordinator pattern from Martin Fowler's enterprise architecture.

---

**End of Canonical Identifier Comparison**

**Auditor:** Independent Architect
**Date:** 2026-07-13
**Status:** COMPLETE
