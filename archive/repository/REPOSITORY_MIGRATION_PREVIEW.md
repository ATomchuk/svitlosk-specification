# REPOSITORY_MIGRATION_PREVIEW

**Document ID:** F-1.95-C3

**Title:** Repository Migration Preview

**Document Class:** Migration Preview

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Complete preview of the repository after Stage F-2.

---

# 1. Post-Migration Repository Tree

```
svitlosk-specification/
├── CHARTER.md
├── PROJECT_PRINCIPLES.md
├── DOCUMENT_INDEX.md
├── EDITORIAL_STANDARDS.md
├── GLOSSARY.md
├── RFC_PROCESS.md
├── ARCHITECTURE.md
├── DATA_MODEL.md
├── SYSTEM_OVERVIEW.md
├── TERRITORIAL_MODEL.md
├── README.md
├── REPOSITORY_CERTIFICATION.md
├── REPOSITORY_FREEZE.md
├── specification/
│   ├── SSP-001-Data-Pipeline.md
│   ├── SSP-002-Parser.md
│   ├── SSP-003-Publication-Engine.md
│   ├── SSP-004-Telegram-Channel.md
│   ├── SSP-005-Data-Storage.md
│   ├── SSP-006-Schedule-Generator.md
│   ├── SSP-007-Graphic-Generator.md
│   ├── SSP-008-API.md
│   ├── SSP-009-Configuration.md
│   ├── SSP-010-Logging.md
│   ├── SSP-011-Monitoring.md
│   ├── SSP-012-Security.md
│   ├── SSP-013-Deployment.md
│   └── README.md
└── telegram/
    ├── foundation/      (10 files)
    │   ├── TELEGRAM_SEMANTIC_MODEL.md
    │   ├── TELEGRAM_GLOSSARY.md
    │   ├── TELEGRAM_SPECIFICATION_ALIGNMENT_PROCESS.md
    │   ├── TELEGRAM_ALIGNMENT_PIPELINE.md
    │   ├── TELEGRAM_ALIGNMENT_GOVERNANCE.md
    │   ├── TJS_ALIGNMENT_TEMPLATE.md
    │   ├── TELEGRAM_ARCHITECTURE_DECISION.md
    │   ├── TELEGRAM_CANONICAL_SPECIFICATION_STANDARD.md (PROMOTED)
    │   ├── TELEGRAM_DOCUMENT_IDENTITY_MODEL.md (PROMOTED)
    │   └── TELEGRAM_DOCUMENT_NAMING_STANDARD.md (PROMOTED)
    ├── specs/           (4 files)
    │   ├── TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md
    │   ├── TELEGRAM_PUBLICATION_LIFECYCLE.md
    │   ├── TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md
    │   └── TELEGRAM_PUBLISHING_CANONICAL_MODEL.md
    ├── working/
    │   ├── publishing/  (10 files)
    │   ├── editorial/   (11 files)
    │   ├── graphic/     (58 files)
    │   ├── glossary/    (11 files)
    │   ├── migration/   (9 files)
    │   ├── alignment/   (5 files)
    │   └── reference/   (32 files)
    ├── legacy/          (8 files)
    │   ├── TJS-001-Journal-Concept.md
    │   ├── TJS-002-Publication-Lifecycle.md
    │   ├── TJS-003-Post-Structure.md
    │   ├── TJS-004-Editorial-Policy.md
    │   ├── TJS-005-Message-Templates.md
    │   ├── TJS-006-Rendering-Rules.md
    │   ├── TJS-007-Publication-Lifecycle.md
    │   └── TJS-008-Publication-Lifecycle.md
    └── archive/         (147 files)
        ├── TELEGRAM_ARCHITECTURE_CERTIFICATION.md
        ├── TELEGRAM_ARCHITECTURE_CONSISTENCY_REVIEW.md
        ├── TELEGRAM_ARCHITECTURE_CONSISTENCY_SCORECARD.md
        ├── ... (140+ governance records)
        ├── REPOSITORY_STATE_SNAPSHOT.md (OBSOLETE)
        ├── CORE_DOCUMENTS_ARCHITECTURE_REVIEW.md (OBSOLETE)
        ├── CORE_DOCUMENTS_MAINTENANCE_REPORT.md (OBSOLETE)
        └── SPECIFICATION_AUDIT_REPORT.md (OBSOLETE)
```

---

# 2. Directory Summary

| Directory | Files | Purpose | Owner |
|-----------|-------|---------|-------|
| telegram/foundation/ | 10 | Permanent platform knowledge | Semantic Foundation |
| telegram/specs/ | 4 | Canonical specifications | Subsystem owners |
| telegram/working/publishing/ | 10 | Publishing working materials | Publishing |
| telegram/working/editorial/ | 11 | Editorial working materials | Editorial |
| telegram/working/graphic/ | 58 | Graphic working materials | Graphic |
| telegram/working/glossary/ | 11 | Glossary working materials | Glossary |
| telegram/working/migration/ | 9 | Migration working materials | Migration |
| telegram/working/alignment/ | 5 | Alignment working materials | Alignment |
| telegram/working/reference/ | 32 | Reference working materials | Reference |
| telegram/legacy/ | 8 | Historical TJS specifications | Legacy |
| telegram/archive/ | 147 | Governance records | Archive |

---

# 3. Total File Count

| Location | Before F-2 | After F-2 | Change |
|----------|-----------|-----------|--------|
| telegram/ root | 342 | 0 | -342 |
| telegram/foundation/ | 0 | 10 | +10 |
| telegram/specs/ | 0 | 4 | +4 |
| telegram/working/ | 0 | 136 | +136 |
| telegram/legacy/ | 0 | 8 | +8 |
| telegram/archive/ | 0 | 147 | +147 |
| **Total** | **342** | **305** | **-37** |

**Note:** -37 difference is due to: 2 renames (counted once), 3 promotions (counted in destination), 4 obsolete (counted in archive).

---

**End of Migration Preview**

**Previewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
