# DOCUMENT_INDEX

Project Specification

**Document ID:** DOC-002

**Document:** DOCUMENT_INDEX.md

**Project:** SvitloSk

**Status:** Stable (Стабільний)

**Class:** Normative

**Maintainer:** SvitloSk Project

---

# Purpose

This document defines the official structure of the SvitloSk Project Specification.

It establishes the canonical organization of project documentation, the recommended reading order, document categories and repository rules.

This document is normative.

---

# Why this document exists

As the SvitloSk specification grows, documentation becomes a system rather than a collection of independent files.

This document provides a single entry point into the specification and defines how documents are organized and maintained.

---

# Reading Order

New contributors SHOULD read the documents in the following order.

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
11. Component Specifications (SSP)
12. Telegram Journal Specifications (TJS)

---

# Repository Structure

The specification is organized into four logical groups.

## 1. Core Governance

Documents defining the project itself.

- CHARTER.md
- PROJECT_PRINCIPLES.md

---

## 2. Repository Governance

Documents defining repository rules and common terminology.

- DOCUMENT_INDEX.md
- EDITORIAL_STANDARDS.md
- GLOSSARY.md
- TERRITORIAL_MODEL.md
- RFC_PROCESS.md

---

## 3. System Architecture

Documents describing the overall architecture of SvitloSk.

- ARCHITECTURE.md
- DATA_MODEL.md

---

## 4. Component Specifications

Detailed specifications of individual system components.

Directory:

```
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

```
/telegram
```

Current specifications include:

- TJS-001 — Journal Concept
- TJS-002 — Publication Lifecycle
- TJS-003 — Post Structure
- TJS-004 — Editorial Policy
- TJS-005+ (future documents)

---

# Document Classes

The repository contains two classes of documents.

## Normative

Normative documents define mandatory project requirements.

Normative documents SHALL use RFC 2119 terminology where applicable.

Examples include:

- CHARTER
- PROJECT_PRINCIPLES
- GLOSSARY
- TERRITORIAL_MODEL
- ARCHITECTURE
- DATA_MODEL
- SSP Specifications
- TJS Specifications

---

## Informative

Informative documents provide explanations, examples and implementation guidance.

Informative documents SHALL NOT introduce mandatory requirements.

Examples include:

- ADR
- Tutorials
- Examples
- Migration Guides
- Design Notes

---

# Core Documents

| ID | Document | Class | Status | Purpose |
|----|----------|-------|--------|---------|
| DOC-000 | CHARTER.md | Normative | Stable | Project mission and governance |
| DOC-001 | PROJECT_PRINCIPLES.md | Normative | Stable | Fundamental engineering principles |
| DOC-002 | DOCUMENT_INDEX.md | Normative | Stable | Repository structure and navigation |
| DOC-003 | EDITORIAL_STANDARDS.md | Normative | Stable | Editorial and writing rules |
| DOC-004 | GLOSSARY.md | Normative | Stable | Official terminology |
| DOC-005 | TERRITORIAL_MODEL.md | Normative | Stable | Canonical territorial hierarchy |
| DOC-006 | RFC_PROCESS.md | Normative | Stable | RFC lifecycle |

---

# Specification Hierarchy

```
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
Component Specifications (SSP)
   │
   ▼
Telegram Journal Specifications (TJS)
```

---

# Repository Rules

Every normative document SHALL be registered in this index.

Document identifiers SHALL be unique.

Reading order SHALL be maintained by this document.

Normative documents SHALL belong to exactly one document group.

New specifications SHALL be placed in their designated repository directory.

---

# References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md

## Referenced by

All normative documents.
