# ROOT_VS_FOUNDATION_ANALYSIS

**Document ID:** TJS-R4.2-P4

**Title:** Root vs Foundation Analysis

**Document Class:** Analysis

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Determine whether Foundation should move to foundation/.

---

# 1. Current State

| Document | Current Location | Future Blueprint |
|----------|-----------------|-----------------|
| CHARTER.md | Root | Root |
| PROJECT_PRINCIPLES.md | Root | Root |
| DOCUMENT_INDEX.md | Root | Root |
| EDITORIAL_STANDARDS.md | Root | Root |
| GLOSSARY.md | Root | Root |
| RFC_PROCESS.md | Root | Root |
| ARCHITECTURE.md | Root | Root |
| DATA_MODEL.md | Root | Root |
| SYSTEM_OVERVIEW.md | Root | Root |
| TERRITORIAL_MODEL.md | Root | Root |
| DOCUMENTATION_TRANSLATION_STANDARD.md | Root | Root |
| SPECIFICATION_ENGINEERING_PROCESS.md | Root | Root |
| README.md | Root | Root |

---

# 2. Analysis

| Option | Pros | Cons |
|--------|------|------|
| OPTION A: Keep Foundation at root | Maximum visibility. GitHub convention. New contributors see governance first. | Root has 13 files. |
| OPTION B: Move Foundation into foundation/ | Cleaner root. All governance in one place. | Foundation less visible. Root becomes minimal navigation only. |

---

# 3. Engineering Assessment

| Criterion | Root | foundation/ |
|-----------|------|-------------|
| Visibility | HIGH — first thing visitors see | MEDIUM — one click deeper |
| Professional practice | YES — many repos keep governance at root | YES — many repos use docs/ |
| Scalability | 13 files — manageable | Grows with future Foundation docs |
| Navigation | Direct | Requires directory traversal |

---

# 4. Analysis Verdict

**OPTION A is architecturally superior for this repository.** Foundation documents at root maximizes visibility and follows the GitHub convention for governance-first repositories. 13 files is manageable.

---

**End of Root vs Foundation Analysis**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
