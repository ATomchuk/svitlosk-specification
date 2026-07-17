# Telegram Canonical Document Policy

**Date:** 2026-07-13
**Scope:** Define canonical vs legacy Telegram documentation
**Status:** POLICY DEFINED

---

# Purpose

This document clearly defines the distinction between Canonical Telegram documentation and Legacy Telegram documentation.

---

# Canonical Telegram Documentation

## Definition

Canonical Telegram documentation consists of the TELEGRAM_*.md documents that form the permanent normative documentation of the Telegram subsystem.

## Characteristics

- **Normative** — defines mandatory requirements
- **Semantic Foundation** — owns semantic definitions
- **Architecture Decision** — owns architectural decisions
- **Active governance** — subject to change through governance process
- **Alignment target** — new specifications align to these documents

## Canonical Documents

| Document | Role |
|----------|------|
| TELEGRAM_SEMANTIC_MODEL.md (TJS-000) | Semantic foundation |
| TELEGRAM_GLOSSARY.md (TJS-000A) | Canonical terminology |
| TELEGRAM_SPECIFICATION_ALIGNMENT_PROCESS.md (TJS-000B) | Alignment process |
| TELEGRAM_ALIGNMENT_PIPELINE.md (TJS-000C) | Alignment pipeline |
| TELEGRAM_ALIGNMENT_GOVERNANCE.md (TJS-000D) | Alignment governance |
| TJS_ALIGNMENT_TEMPLATE.md (TJS-TEMPLATE) | Specification template |
| TELEGRAM_ARCHITECTURE_DECISION.md | Approved architecture |
| TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | Publishing blueprint |
| TELEGRAM_EDITORIAL_SYSTEM_BLUEPRINT.md | Editorial blueprint |

---

# Legacy Telegram Documentation

## Definition

Legacy Telegram documentation consists of the TJS-001 through TJS-008 specifications that served as knowledge exploration documents during the design phase.

## Characteristics

- **Historical** — records of original design exploration
- **Knowledge harvested** — semantic content incorporated into Foundation
- **Not normative** — not used for active governance
- **Not alignment targets** — new specifications do not align to these
- **Preserved** — retained as historical references

## Legacy Documents

| Document | Role |
|----------|------|
| TJS-001 | Legacy Knowledge Source (Journal Concept) |
| TJS-002 | Legacy Knowledge Source (Publication Lifecycle) |
| TJS-003 | Legacy Knowledge Source (Post Structure) |
| TJS-004 | Legacy Knowledge Source (Editorial Policy) |
| TJS-005 | Legacy Knowledge Source (Message Templates) |
| TJS-006 | Legacy Knowledge Source (Rendering Rules) |
| TJS-007 | Legacy Knowledge Source (Publication Lifecycle) |
| TJS-008 | Legacy Knowledge Source (Publication Lifecycle) |

---

# Distinction Summary

| Aspect | Canonical | Legacy |
|--------|-----------|--------|
| Documents | TELEGRAM_*.md | TJS-001 through TJS-008 |
| Status | Normative | Historical |
| Semantic authority | YES | NO |
| Architecture authority | YES | NO |
| Active governance | YES | NO |
| Alignment target | YES | NO |
| Future use | Active specification | Historical reference |
| Modification | Via governance | Prohibited |

---

**End of Canonical Document Policy**

**Policy Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
