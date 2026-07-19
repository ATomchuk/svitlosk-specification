# NAVIGATION_REACHABILITY_MATRIX

**Document ID:** TJS-N1.1-E6

**Title:** Navigation Reachability Matrix

**Document Class:** Reachability

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Verify reachability of every normative document.

---

# 1. Reachable Documents

| # | Document | Location | Reachable via INDEX? |
|---|----------|----------|---------------------|
| 1 | CHARTER.md | root/ | YES — Section 3.1 |
| 2 | PROJECT_PRINCIPLES.md | root/ | YES — Section 3.1 |
| 3 | DOCUMENT_INDEX.md | root/ | YES — self |
| 4 | EDITORIAL_STANDARDS.md | root/ | YES — Section 3.2 |
| 5 | GLOSSARY.md | root/ | YES — Section 3.2 |
| 6 | TERRITORIAL_MODEL.md | root/ | YES — Section 3.2 |
| 7 | RFC_PROCESS.md | root/ | YES — Section 3.2 |
| 8 | ARCHITECTURE.md | root/ | YES — Section 3.5 |
| 9 | DATA_MODEL.md | root/ | YES — Section 3.5 |
| 10 | SYSTEM_OVERVIEW.md | root/ | YES — Section 3.5 |
| 11 | SPECIFICATION_ENGINEERING_PROCESS.md | root/ | YES — Section 3.2 |
| 12 | SSP-001 through SSP-013 | specification/ | PARTIAL — only 001-003 in INDEX |
| 13 | ADR-001 | adr/ | YES — Section 3.8 |

---

# 2. Unreachable Documents

| # | Document | Location | Issue |
|---|----------|----------|-------|
| 1 | DOCUMENTATION_TRANSLATION_STANDARD.md | root/ | NOT in INDEX at all |
| 2 | TELEGRAM_SEMANTIC_MODEL.md (TJS-000) | telegram/foundation/ | NOT in INDEX |
| 3 | TELEGRAM_GLOSSARY.md (TJS-000A) | telegram/foundation/ | NOT in INDEX |
| 4 | TELEGRAM_PUBLISHING_CANONICAL_MODEL.md (TJS-010) | telegram/specs/ | NOT in INDEX |
| 5 | TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md (TJS-020) | telegram/specs/ | NOT in INDEX |
| 6 | TELEGRAM_PUBLICATION_LIFECYCLE.md (TJS-021) | telegram/specs/ | NOT in INDEX |
| 7 | TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md (TJS-022) | telegram/specs/ | NOT in INDEX |
| 8 | TELEGRAM_CANONICAL_PLATFORM_RELEASE_v2.0.md | telegram/ | NOT in INDEX |
| 9 | SSP-004 through SSP-013 (10 files) | specification/ | NOT in INDEX table |

---

# 3. Duplicated Navigation Paths

| # | Path | Issue |
|---|------|-------|
| 1 | Meta Review section 6 + section 12 | Duplicate sections in INDEX |

---

# 4. Missing Navigation Paths

| # | Missing Path | Impact |
|---|-------------|--------|
| 1 | No path to canonical Telegram specs | 6 Stable specs unreachable |
| 2 | No path to DTS-001 | Foundation doc unreachable |
| 3 | No path to 10 SSPs | 10 of 13 SSPs unreachable |

---

# 5. Reachability Summary

| Metric | Value |
|--------|-------|
| Total normative documents | ~25 |
| Reachable | 13 |
| Unreachable | 9+ |
| Reachability rate | ~56% |

---

**End of Reachability Matrix**

**Auditor:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
