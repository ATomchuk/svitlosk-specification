# MIGRATION_IMPACT_ESTIMATE

**Document ID:** NAM-005

**Title:** Migration Impact Estimate

**Document Class:** Impact Estimate

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. If Renamed to "Publication Coordinator"

| Impact Area | Affected | Details |
|-------------|----------|---------|
| TELEGRAM_GLOSSARY.md | YES | Term name, definition, relationships |
| TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | YES | ~20 occurrences |
| TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md | YES | ~2 occurrences |
| TTDR-001 | YES | Entry update |
| Working documents | YES | ~120 occurrences |
| SSP documents | YES | SSP-003 references |
| **Total affected** | **~150+ files/occurrences** | |

---

# 2. If Renamed to "Publication Orchestrator"

Same impact as "Publication Coordinator" — ~150+ affected occurrences.

---

# 3. Migration Complexity

| Factor | Assessment |
|--------|-----------|
| File moves | NONE — same location |
| Content changes | ~150 occurrences across ~20+ documents |
| Glossary update | REQUIRED |
| TTDR update | REQUIRED |
| SSP references | REQUIRED |
| Working doc updates | REQUIRED |
| Git history | POLLUTED — renames tracked |
| Risk of broken references | MEDIUM — cross-document references |
| Timeline | WEEKS of careful editing |

---

# 4. Impact Verdict

**Renaming from "Publication Engine" to any alternative would affect 150+ occurrences across 20+ documents.** The migration cost is CATASTROPHIC relative to the marginal architectural improvement.

---

**End of Migration Impact Estimate**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
