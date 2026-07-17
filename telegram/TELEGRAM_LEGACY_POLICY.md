# Telegram Legacy Policy

**Date:** 2026-07-13
**Scope:** Normative policy governing the use of legacy Telegram specifications
**Status:** POLICY DEFINED

---

# Purpose

This document defines the normative policy governing the use of legacy Telegram specifications (TJS-001 through TJS-008).

---

# Legacy Knowledge Policy

## Why Legacy Specifications Are Preserved

Legacy specifications are preserved because:

1. They contain the original design exploration that led to the current architecture
2. They serve as historical records of the project's evolution
3. They provide context for understanding architectural decisions
4. They may contain original wording that captures design intent
5. They demonstrate the progression from exploration to normative documentation

## Why Legacy Specifications Are NOT Normative

Legacy specifications are NOT normative because:

1. Their semantic content has been harvested into the Semantic Foundation
2. They contain SSOT violations (triple lifecycle duplication)
3. They contain metadata non-compliance
4. They contain incorrect cross-references
5. They were not designed as permanent normative documents

## How Legacy Specifications MAY Be Used

Legacy specifications MAY be used:

1. As historical references for understanding design decisions
2. As sources for tracing the evolution of concepts
3. As references for verifying that harvested knowledge is complete
4. As evidence in architectural reviews and audits
5. As context for future specification development

## How Legacy Specifications SHALL NOT Be Used

Legacy specifications SHALL NOT be used:

1. As authoritative sources for terminology (use TELEGRAM_GLOSSARY.md)
2. As authoritative sources for architecture (use TELEGRAM_ARCHITECTURE_DECISION.md)
3. As authoritative sources for editorial policy (use TELEGRAM_EDITORIAL_* documents)
4. As authoritative sources for publishing model (use TELEGRAM_PUBLISHING_* documents)
5. As Alignment targets (use TELEGRAM_*.md documents)
6. As normative references in new specifications
7. As the basis for implementation decisions

---

# Legacy Knowledge Status

| Document | Status | Normative? |
|----------|--------|------------|
| TJS-001 | Legacy Knowledge Source | NO |
| TJS-002 | Legacy Knowledge Source | NO |
| TJS-003 | Legacy Knowledge Source | NO |
| TJS-004 | Legacy Knowledge Source | NO |
| TJS-005 | Legacy Knowledge Source | NO |
| TJS-006 | Legacy Knowledge Source | NO |
| TJS-007 | Legacy Knowledge Source | NO |
| TJS-008 | Legacy Knowledge Source | NO |

---

# Policy Compliance

All future Telegram documentation SHALL:

1. Reference TELEGRAM_*.md documents as authoritative sources
2. NOT reference TJS-001 through TJS-008 as authoritative sources
3. Use the Semantic Foundation (TELEGRAM_SEMANTIC_MODEL.md + TELEGRAM_GLOSSARY.md) for terminology
4. Use the Architecture Decision (TELEGRAM_ARCHITECTURE_DECISION.md) for architecture
5. Use the Alignment Framework for specification alignment

---

**End of Legacy Policy**

**Policy Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
