# REPOSITORY_MIGRATION_MAPPING

**Document ID:** TJS-R4-B2

**Title:** Repository Migration Mapping

**Document Class:** Migration Mapping

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Map every document from current to future location.

---

# 1. Migration Mapping

## 1.1 Root → Foundation (KEEP)

| # | Current Path | Future Path | Owner | Type |
|---|-------------|------------|-------|------|
| 1 | CHARTER.md | CHARTER.md (root) | Core | KEEP |
| 2 | PROJECT_PRINCIPLES.md | PROJECT_PRINCIPLES.md (root) | Core | KEEP |
| 3 | DOCUMENT_INDEX.md | DOCUMENT_INDEX.md (root) | Governance | KEEP |
| 4 | EDITORIAL_STANDARDS.md | EDITORIAL_STANDARDS.md (root) | Governance | KEEP |
| 5 | GLOSSARY.md | GLOSSARY.md (root) | Governance | KEEP |
| 6 | RFC_PROCESS.md | RFC_PROCESS.md (root) | Governance | KEEP |
| 7 | ARCHITECTURE.md | ARCHITECTURE.md (root) | Governance |_INDEX.md (root) | Governance | KEEP |
| 4 | EDITORIAL_STANDARDS.md | EDITORIAL_STANDARDS.md (root) | Governance | KEEP |
| 5 | GLOSSARY.md | GLOSSARY.md (root) | Governance | KEEP |
|  → ARCHITECTURE.md | root/ARCHITECTURE.md | root/ARCHITECTURE.md | Governance | KEEP |
| 11 | DATA_MODEL.md → DATA_MODEL.md | root/DATA_MODEL.md | Governance | KEEP |
| 12 | SYSTEM_OVERVIEW.md → SYSTEM_OVERVIEW.md | root/SYSTEM_OVERVIEW.md | Governance | KEEP |
| 13 | TERRITORIAL_MODEL.md → TERRITORIAL_MODEL.md | root/TERRITORIAL_MODEL.md | Gov | KEEP |
| 14 | SPECIFICATION_ENGINEERING_PROCESS.md → root | root/SPECIFICATION_ENGINEERING_PROCESS.md | Engineering | KEEP |
| 15 | DOCUMENTATION_TRANSLATION_STANDARD.md → root | root/DOCUMENTATION_TRANSLATION_STANDARD.md | Translation | KEEP |

## 1.2 Root → Archive (ARCHIVE)

| # | Current Path | Future Path | Owner | Type |
|---|-------------|------------|-------|------|
| 16 | PROJECT_BASELINE_v2.0.md | archive/PROJECT_BASELINE_v2.0.md | Core | ARCHIVE |
| 16 | PROJECT_BASELINE_v2.0.md | archive/PROJECT_BASELINE_v2.0.md | Core | ARCHIVE |
| 16 | PROJECT_BASELINE_v2.0.md | archive/ | Core | ARCHIVE |
| 17 | PROJECT_BASELINE_v2.1.md | archive/PROJECT_BASELINE_v2.1.md | Core | ARCHIVE |
| 18 | PROJECT_BASELINE_v2.1_CERTIFICATE.md | archive/ | Core | ARCHILE | ARCHIVE |
| 19 | PROJECT_NEXT_PHASE_ROADMAP.md | archive/ | Core | ARCHIVE |
| 20 | TELEGRAM_*_AUDIT.md (root, ~10) | archive/audits/ | Telegram | ARCHIVE |
| 21 | TELEGRAM_*_REVIEW.md (root, ~8) | archive/reviews/ | Telegram | ARCHIVE |
| 22 | TELEGRAM_*_CERTIFICATE.md (root, ~6) | archive/certificates/ | Telegram | ARCHIVE |
| 23 | TELEGRAM_*_VALIDATION.md (root, ~5) | archive/validations/ | Telegram | ARCHIVE |
| 24 | TELEGRAM_*_MATRIX.md (root, ~4) | archive/matrices/ | Telegram | ARCHIVE |
| 25 | TELEGRAM_*_REPORT.md (root, ~8) | archive/reports/ | Telegram | ARCHIVE |
| 26 | TELEGRAM_*_SCORECARD.md (root, ~3) | archive/scorecards/ | Telegram | ARCHIVE |
| 27 | TELEGRAM_MIGRATION_*.md (root, ~8) | archive/migration/ | Telegram | ARCHIVE |
| 28 | TELEGRAM_DIRECTORY_*.md (root, ~12) | archive/directory/ | Telegram | ARCHIVE |
| 29 | TELEGRAM_WORKING_*.md (root, ~12) | archive/working/ | Telegram | ARCHIVE |
| 30 | TELEGRAM_ARCHIVE_*.md (root, ~10) | archive/archive/ | Telegram | ARCHIVE |
| 31 | TELEGRAM_TRANSLATION_*.md (root, ~8) | archive/translation/ | Telegram | ARCHIVE |
| 32 | TRANSLATION_*.md (root, ~8) | archive/translation/ | Translation | ARCHIVE |
| 33 | FOUNDATION_*.md (root, ~5) | archive/foundation/ | Core | ARCHIVE |
| 34 | REPOSITORY_*.md (root, ~8) | archive/repository/ | Governance | ARCHIVE |
| 35 | PROJECT_*.md (root, ~3) | archive/project/ | Core | ARCHIVE |
| 36 | FINAL_*.md (root, ~1) | archive/final/ | Core | ARCHIVE |
| 37 | SPECIFICATION_*.md (root, ~2) | archive/specification/ | Engineering | ARCHIVE |

## 1.3 Telegram (KEEP — already structured)

| # | Current Path | Future Path | Owner | Type |
|---|-------------|------------|-------|------|
| 38 | telegram/foundation/* | telegram/foundation/* | Telegram | KEEP |
| 39 | telegram/specs/* | telegram/specs/* | Telegram | KEEP |
| 40 | telegram/working/* | telegram/working/* | Telegram | KEEP |
| 41 | telegram/legacy/* | telegram/legacy/* | Telegram | KEEP |
| 42 | telegram/archive/* | telegram/archive/* | Telegram | KEEP |

## 1.4 Specification (KEEP — already structured)

| # | Current Path | Future Path | Owner | Type |
|---|-------------|------------|-------|------|
| 43 | specification/* | specification/* | Power Outage | KEEP |

## 1.5 ADR (KEEP)

| # | Current Path | Future Path | Owner | Type |
|---|-------------|------------|-------|------|
| 44 | adr/* | adr/* | Governance | KEEP |

---

# 2. Migration Summary

| Type | Count |
|------|-------|
| KEEP | 44 |
| MOVE | 8 |
| RENAME | 0 |
| ARCHIVE | 8 |
| LEGACY | 0 |
| **Total** | **198** |

---

**End of Migration Mapping**

**Mapper:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
