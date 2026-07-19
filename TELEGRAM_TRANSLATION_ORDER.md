# TELEGRAM_TRANSLATION_ORDER

**Document ID:** TJS-L1-A4

**Title:** Telegram Translation Order

**Document Class:** Translation Order

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Define the optimal translation order to minimize future maintenance.

---

# 1. Translation Order

| Order | Document | Level | Justification |
|-------|----------|-------|--------------|
| 1 | TELEGRAM_SEMANTIC_MODEL.md (TJS-000) | LEVEL 1 | Foundation — all other translations depend on terminology |
| 2 | TELEGRAM_GLOSSARY.md (TJS-000A) | LEVEL 1 | Glossary — all translations use these terms |
| 3 | TELEGRAM_PUBLISHING_CANONICAL_MODEL.md (TJS-010) | LEVEL 1 | Core spec — references semantic foundation |
| 4 | TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md (TJS-020) | LEVEL 1 | Core spec — references semantic foundation |
| 5 | TELEGRAM_PUBLICATION_LIFECYCLE.md (TJS-021) | LEVEL 1 | Core spec — references semantic foundation |
| 6 | TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md (TJS-022) | LEVEL 1 | Core spec — references semantic foundation |
| 7 | TELEGRAM_ARCHITECTURE_DECISION.md | LEVEL 2 | Architecture — developers need this |
| 8 | TELEGRAM_CANONICAL_SPECIFICATION_STANDARD.md | LEVEL 2 | Standard — writers need this |
| 9 | TELEGRAM_SPECIFICATION_ALIGNMENT_PROCESS.md | LEVEL 2 | Process — engineers need this |

---

# 2. Translation Order Rationale

| Phase | Documents | Why This Order |
|-------|-----------|---------------|
| Phase 1 | TJS-000, TJS-000A | Foundation — all other translations depend on these terms |
| Phase 2 | TJS-010, TJS-020, TJS-021, TJS-022 | Core specs — reference foundation terms |
| Phase 3 | Architecture, Standard, Process | Supporting docs — reference foundation terms |

---

# 3. Maintenance Minimization

| Principle | Explanation |
|-----------|------------|
| Foundation first | Translating glossary first ensures all terms are available for subsequent translations |
| Core specs second | Translating core specs after foundation means terminology is already translated |
| Supporting docs last | These reference foundation terms, which are already translated |

**This order minimizes future maintenance because:**
1. Glossary translations provide the term foundation for all subsequent work
2. Core spec translations reference already-translated glossary terms
3. Supporting doc translations reference already-translated foundation terms

---

# 4. Translation Order Summary

| Phase | Documents | Priority |
|-------|-----------|----------|
| Phase 1 | TJS-000, TJS-000A | HIGHEST |
| Phase 2 | TJS-010, TJS-020, TJS-021, TJS-022 | HIGH |
| Phase 3 | Architecture, Standard, Process | MEDIUM |

---

**End of Translation Order**

**Planner:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
