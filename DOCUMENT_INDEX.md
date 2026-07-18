# DOCUMENT_INDEX

Status: Stable (Стабільний)

Document ID: DOC-002

Document Class: Normative

Author: SvitloSk Project

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
7. TERRITORIAL_MODEL.md
8. RFC_PROCESS.md
9. ARCHITECTURE.md
10. DATA_MODEL.md
11. SYSTEM_OVERVIEW.md
12. SPECIFICATION_ENGINEERING_PROCESS.md
13. Component Specifications (SSP)
14. Telegram Journal Specifications (TJS)
15. REPOSITORY_CERTIFICATION.md
16. REPOSITORY_FREEZE.md

---

# Repository Structure

The Project Specification is organized into five logical groups.

## 1. Core Governance

Documents defining the mission, principles and governance of the project.

- CHARTER.md
- PROJECT_PRINCIPLES.md

---

## 2. Documentation Governance

Documents defining documentation governance, editorial standards, terminology and repository-wide rules.

- DOCUMENT_INDEX.md
- EDITORIAL_STANDARDS.md
- GLOSSARY.md
- TERRITORIAL_MODEL.md
- RFC_PROCESS.md
- SPECIFICATION_ENGINEERING_PROCESS.md (PROC-001) — Repository-wide engineering process

---

## 3. System Architecture

Documents defining the architecture, logical data model and overall system organization.

- ARCHITECTURE.md
- DATA_MODEL.md
- SYSTEM_OVERVIEW.md

---

## 4. Component Specifications

Normative specifications describing individual architectural components.

Directory:

```text
/specification
```

Current specifications include:

- SSP-001 — Data Pipeline
- SSP-002 — Parser
- SSP-003 — Publication Engine
- SSP-004 — Telegram Channel
- SSP-005 — Data Storage
- SSP-006 — Schedule Generator
- SSP-007 — Graphic Generator
- SSP-008 — API
- SSP-009 — Configuration
- SSP-010 — Logging
- SSP-011 — Monitoring
- SSP-012 — Security
- SSP-013 — Deployment

---

## 5. Telegram Journal Specifications

Normative specifications describing the Public Information Journal.

Directory:

```text
/telegram
```

Current specifications include:

- TJS-001 — Journal Concept
- TJS-002 — Publication Model
- TJS-003 — Post Structure
- TJS-004 — Editorial Policy
- TJS-005 — Message Templates
- TJS-006 — Rendering Rules
- TJS-007 — Publication Lifecycle
- TJS-008 — Publication Lifecycle

---

## 6. Meta Review Methodology

Normative documents defining the Meta Review methodology.

Directory:

```text
/audit/audit-2026-07/methodology-extension/
```

Current documents:

- META_REVIEW_PROTOCOL.md — Meta Review methodology
- META_REVIEW_CHECKLIST.md — Meta Review verification checklist
- META_REVIEW_OUTPUT_TEMPLATE.md — Meta Review output specification

---

# Architecture Decision Records (ADR)

Normative records documenting approved architectural decisions.

Directory:

```text
/adr
```

Current records:

| ADR | Title | Status | Class | Description |
|-----|-------|--------|-------|-------------|
| ADR-001 | Component vs Role | Stable | Normative | Defines the distinction between architectural components and logical roles used throughout the repository |

---

# Canonical SSP Specifications

| SSP | Status | Canonical Review | Current Baseline | Notes |
|-----|--------|------------------|------------------|-------|
| SSP-001 | Certified | review-v4 | Core + ADR-001 | Certified after repository canonicalization |
| SSP-002 | Certified | review-v2 | Core + ADR-001 | Certified against revised Core Documents |
| SSP-003 | Certified | review-v3 | Core + ADR-001 | Certified against ADR-001 and revised Core Documents |

Only the review version listed above SHALL be considered the current canonical certification of the corresponding SSP specification.

Earlier review versions remain archived exclusively for historical traceability.

---

# Meta Review Methodology

Normative documents defining the Meta Review methodology.

| ID | Document | Class | Status | Purpose |
|----|----------|-------|--------|---------|
| DOC-014 | META_REVIEW_PROTOCOL.md | Normative | Draft | Meta Review methodology |
| DOC-015 | META_REVIEW_CHECKLIST.md | Normative | Draft | Meta Review verification checklist |
| DOC-016 | META_REVIEW_OUTPUT_TEMPLATE.md | Normative | Draft | Meta Review output specification |

---

# Document Classes

The repository contains two document classes.

## Normative

Normative documents define mandatory project requirements.

Normative documents SHALL use RFC 2119 terminology where applicable.

Examples include:

- Core Governance documents;
- Documentation Governance documents;
- System Architecture documents;
- SSP Specifications;
- TJS Specifications;
- REPOSITORY_CERTIFICATION.md;
- REPOSITORY_FREEZE.md.

---

## Informative

Informative documents provide explanations, implementation guidance and supporting material.

Informative documents SHALL NOT introduce mandatory requirements.

Informative documents SHALL NOT supersede normative documents.

Examples include:

- ADR documents;
- tutorials;
- migration guides;
- examples;
- design notes.

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
| DOC-011 | REPOSITORY_CERTIFICATION.md | Normative | Stable | Repository certification |
| DOC-012 | REPOSITORY_FREEZE.md | Normative | Stable | Repository freeze policy |
| DOC-013 | REPOSITORY_CERTIFICATION_STATUS.md | Normative | Stable | Repository certification register |

---

# Specification Hierarchy

```text
README
   │
   ▼
CHARTER
   │
   ▼
PROJECT_PRINCIPLES
   │
   ▼
DOCUMENT_INDEX
   │
   ▼
EDITORIAL_STANDARDS
   │
   ▼
GLOSSARY
   │
   ▼
TERRITORIAL_MODEL
   │
   ▼
RFC_PROCESS
   │
   ▼
ARCHITECTURE
   │
   ▼
DATA_MODEL
   │
   ▼
SYSTEM_OVERVIEW
   │
   ▼
Component Specifications (SSP)
   │
   ▼
Telegram Journal Specifications (TJS)
   │
   ▼
REPOSITORY_CERTIFICATION
   │
   ▼
REPOSITORY_FREEZE
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