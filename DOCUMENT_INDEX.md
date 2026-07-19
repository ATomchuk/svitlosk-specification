# DOCUMENT_INDEX

**Document ID:** DOC-002

**Title:** Document Index

**Document Class:** Normative Foundation Document

**Status:** STABLE

**Author:** SvitloSk Project

---

# Purpose

This document defines the official structure of the SvitloSk Project Specification.

It establishes the canonical organization of project documentation, the recommended reading order, document categories, repository governance and repository rules.

This document is the authoritative entry point to the Project Specification.

---

# Why this document exists

As the SvitloSk Project evolves, its documentation becomes an engineering system rather than a collection of independent documents.

This document defines how documentation is organized, maintained and governed throughout the project lifecycle.

---

# Reading Order

New contributors SHOULD read the documentation in the following order.

1. README.md
2. CHARTER.md
3. PROJECT_PRINCIPLES.md
4. DOCUMENT_INDEX.md
5. EDITORIAL_STANDARDS.md
6. GLOSSARY.md
7. DOCUMENTATION_TRANSLATION_STANDARD.md
8. TERRITORIAL_MODEL.md
9. RFC_PROCESS.md
10. ARCHITECTURE.md
11. DATA_MODEL.md
12. SYSTEM_OVERVIEW.md
13. SPECIFICATION_ENGINEERING_PROCESS.md
14. Component Specifications (SSP)
15. Telegram Canonical Specifications (TJS)
16. Architecture Decision Records (ADR)

---

# Repository Structure

The Project Specification is organized into seven logical groups.

---

## 1. Core Governance

Documents defining the mission, principles and governance of the project.

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| DOC-000 | Charter | CHARTER.md | root/ | Stable | Project mission and governance |
| DOC-001 | Project Principles | PROJECT_PRINCIPLES.md | root/ | Stable | Engineering principles |

---

## 2. Documentation Governance

Documents defining documentation governance, editorial standards, terminology and repository-wide rules.

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| DOC-002 | Document Index | DOCUMENT_INDEX.md | root/ | Stable | Repository governance and navigation |
| DOC-003 | Editorial Standards | EDITORIAL_STANDARDS.md | root/ | Stable | Editorial and documentation standards |
| DOC-004 | Glossary | GLOSSARY.md | root/ | Stable | Canonical project terminology |
| DOC-006 | RFC Process | RFC_PROCESS.md | root/ | Stable | Specification change governance |
| DTS-001 | Documentation Translation Standard | DOCUMENTATION_TRANSLATION_STANDARD.md | root/ | Stable | Normative translation standard |

---

## 3. Engineering Process

Repository-wide engineering process governing all future canonical specifications.

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| PROC-001 | Specification Engineering Process | SPECIFICATION_ENGINEERING_PROCESS.md | root/ | Stable | Normative engineering process for all canonical specifications |

---

## 4. System Architecture

Documents defining the architecture, logical data model and overall system organization.

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| DOC-007 | Architecture | ARCHITECTURE.md | root/ | Stable | Canonical system architecture |
| DOC-008 | Data Model | DATA_MODEL.md | root/ | Stable | Canonical logical data model |
| DOC-009 | Territorial Model | TERRITORIAL_MODEL.md | root/ | Stable | Canonical territorial hierarchy |
| DOC-010 | System Overview | SYSTEM_OVERVIEW.md | root/ | Stable | High-level system overview |

---

## 5. Component Specifications (SSP)

Normative specifications describing individual architectural components.

Directory: specification/

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| SSP-001 | Data Pipeline | SSP-001-Data-Pipeline.md | specification/ | Stable | Data pipeline architecture |
| SSP-002 | Parser | SSP-002-Parser.md | specification/ | Stable | Parser component |
| SSP-003 | Publication Engine | SSP-003-Publication-Engine.md | specification/ | Stable | Publication engine |
| SSP-004 | Telegram Channel | SSP-004-Telegram-Channel.md | specification/ | Stable | Telegram channel integration |
| SSP-005 | Data Storage | SSP-005-Data-Storage.md | specification/ | Stable | Data storage layer |
| SSP-006 | Schedule Generator | SSP-006-Schedule-Generator.md | specification/ | Stable | Schedule generation |
| SSP-007 | Graphic Generator | SSP-007-Graphic-Generator.md | specification/ | Stable | Graphic generation |
| SSP-008 | API | SSP-008-API.md | specification/ | Stable | API layer |
| SSP-009 | Configuration | SSP-009-Configuration.md | specification/ | Stable | Configuration management |
| SSP-010 | Logging | SSP-010-Logging.md | specification/ | Stable | Logging infrastructure |
| SSP-011 | Monitoring | SSP-011-Monitoring.md | specification/ | Stable | Monitoring and alerting |
| SSP-012 | Security | SSP-012-Security.md | specification/ | Stable | Security model |
| SSP-013 | Deployment | SSP-013-Deployment.md | specification/ | Stable | Deployment and operations |

---

## 6. Telegram Canonical Specifications

Normative specifications defining the Telegram Public Information Journal.

Directory: telegram/

### 6.1 Telegram Foundation

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| TJS-000 | Telegram Semantic Model | TELEGRAM_SEMANTIC_MODEL.md | telegram/foundation/ | Stable | Semantic foundation for the Telegram subsystem |
| TJS-000A | Telegram Glossary | TELEGRAM_GLOSSARY.md | telegram/foundation/ | Stable | Canonical Telegram terminology |

### 6.2 Telegram Canonical Specifications

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| TJS-010 | Publishing Model | TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | telegram/specs/ | Stable | Publishing architecture and responsibilities |
| TJS-020 | Editorial System Model | TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md | telegram/specs/ | Stable | Editorial system architecture |
| TJS-021 | Publication Lifecycle | TELEGRAM_PUBLICATION_LIFECYCLE.md | telegram/specs/ | Stable | Publication lifecycle management |
| TJS-022 | Graphic Publication Model | TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md | telegram/specs/ | Stable | Graphic publication architecture |

---

## 7. Architecture Decision Records (ADR)

Normative records documenting approved architectural decisions.

Directory: adr/

| Document ID | Document | Filename | Location | Status | Purpose |
|------------|----------|----------|----------|--------|---------|
| ADR-001 | Component vs Role | ADR-001-Component-vs-Role.md | adr/ | Stable | Distinction between architectural components and logical roles |

---

# Core Documents

| ID | Document | Class | Status | Purpose |
|----|----------|-------|--------|---------|
| DOC-000 | CHARTER.md | Normative | Stable | Project mission and governance |
| DOC-001 | PROJECT_PRINCIPLES.md | Normative | Stable | Engineering principles |
| DOC-002 | DOCUMENT_INDEX.md | Normative | Stable | Repository governance and navigation |
| DOC-003 | EDITORIAL_STANDARDS.md | Normative | Stable | Editorial and documentation standards |
| DOC-004 | GLOSSARY.md | Normative | Stable | Canonical project terminology |
| DOC-006 | RFC_PROCESS.md | Normative | Stable | Specification change governance |
| DOC-007 | ARCHITECTURE.md | Normative | Stable | Canonical system architecture |
| DOC-008 | DATA_MODEL.md | Normative | Stable | Canonical logical data model |
| DOC-009 | TERRITORIAL_MODEL.md | Normative | Stable | Canonical territorial hierarchy |
| DOC-010 | SYSTEM_OVERVIEW.md | Normative | Stable | High-level system overview |
| PROC-001 | SPECIFICATION_ENGINEERING_PROCESS.md | Normative | Stable | Normative engineering process |
| DTS-001 | DOCUMENTATION_TRANSLATION_STANDARD.md | Normative | Stable | Normative translation standard |

---

# Specification Hierarchy

```text
README
   |
   v
CHARTER
   |
   v
PROJECT_PRINCIPLES
   |
   v
DOCUMENT_INDEX
   |
   v
EDITORIAL_STANDARDS
   |
   v
GLOSSARY
   |
   v
DOCUMENTATION_TRANSLATION_STANDARD
   |
   v
TERRITORIAL_MODEL
   |
   v
RFC_PROCESS
   |
   v
ARCHITECTURE
   |
   v
DATA_MODEL
   |
   v
SYSTEM_OVERVIEW
   |
   v
SPECIFICATION_ENGINEERING_PROCESS
   |
   v
Component Specifications (SSP)
   |
   v
Telegram Canonical Specifications (TJS)
   |
   v
Architecture Decision Records (ADR)
```

---

# Repository Rules

Every normative document SHALL be registered in this index.

Document identifiers SHALL be unique.

Reading order SHALL be maintained by this document.

Normative documents SHALL belong to exactly one logical group.

New specifications SHALL be placed in their designated repository directory.

Implementation details SHALL reside in SSP specifications and SHALL NOT be introduced into Core Documents.

English documentation SHALL be treated as the canonical source of the repository.

Translations SHALL always be derived from the canonical English documentation.

Repository-wide modifications SHALL follow the approved governance process.

---

# References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- EDITORIAL_STANDARDS.md

## Referenced by

All normative repository documents.

---

**End of Document**
