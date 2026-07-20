# CANONICAL_IDENTIFIER_RECOMMENDATION

**Document ID:** NAM-004

**Title:** Canonical Identifier Recommendation

**Document Class:** Recommendation

**Status:** COMPLETE

**Author:** Independent Architect

---

# 1. Translation-Independent Analysis

Assume NO Ukrainian translation exists.

Choose the best English canonical identifier.

---

# 2. Ranking

| Rank | Identifier | Architectural Precision | Long-term Stability | Migration Cost | Net Assessment |
|------|-----------|------------------------|--------------------| ---------------| --------------- |
| 1 | Publication Coordinator | 10/10 | HIGH | VERY HIGH — 149 occurrences | BEST ARCHITECTURALLY, WORST FOR MIGRATION |
| 2 | Publication Engine | 7/10 | HIGH | ZERO — already established | ACCEPTABLE — good enough for long-term |
| 3 | Publication Orchestrator | 8/10 | HIGH | VERY HIGH | GOOD BUT UNNECESSARY |
| 4 | Publication Dispatcher | 7/10 | MEDIUM | VERY HIGH | ACCEPTABLE BUT UNNECESSARY |

---

# 3. The Dilemma

**"Publication Coordinator" is architecturally superior to "Publication Engine."**

Evidence:
- It accurately describes the primary role (assembling from producers)
- It aligns with Martin Fowler's enterprise architecture patterns
- It distinguishes from generators (Schedule Generator, Graphic Generator)
- It clarifies that this component orchestrates, not generates

**However:**

"Publication Engine" is already:
- Established in the Glossary
- Used 149 times across the repository
- Understood by all stakeholders
- Aligned with IT industry terminology ("Engine" is standard)
- Zero migration cost

---

# 4. Recommendation

**Keep "Publication Engine." Do NOT rename to "Publication Coordinator."**

The architectural improvement of "Coordinator" does NOT justify:
- 149 occurrences to change
- Glossary entry to update
- TTDR entry to update
- SSP references to update
- Working document references to update
- Git history pollution
- Stakeholder confusion

"Publication Engine" is 80% architecturally precise. "Publication Coordinator" would be 100% but at catastrophic migration cost.

**The best architecture is one that works, not one that is theoretically perfect.**

---

**End of Recommendation**

**Auditor:** Independent Architect
**Date:** 2026-07-13
**Status:** COMPLETE — Keep "Publication Engine"
