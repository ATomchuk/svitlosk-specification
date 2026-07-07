# DOCUMENT_INDEX

Project Specification

---

Document ID: DOC-002

Document: DOCUMENT_INDEX.md

Project: SvitloSk

Status: Stable (Стабільний)

Class: Normative

Maintainer: SvitloSk Project

---

## Purpose

This document defines the official structure of the SvitloSk Specification repository.

It provides a single authoritative index of all specification documents, their purpose, status, identifiers and relationships.

Every normative document in the repository SHALL be listed here.

---

# Why this document exists

The Specification repository is expected to evolve for many years.

Without a single authoritative index it becomes difficult to understand

- which documents exist;
- which documents are normative;
- which documents are informative;
- which documents supersede older versions;
- where new contributors should begin reading.

DOCUMENT_INDEX.md solves this problem.

---

# Reading Order

New contributors SHOULD read documents in the following order.

1. README.md
2. CHARTER.md
3. PROJECT_PRINCIPLES.md
4. DOCUMENT_INDEX.md
5. EDITORIAL_STANDARDS.md
6. RFC Process
7. Architecture Specifications
8. Component Specifications

---

# Document Classes

The repository contains two classes of documents.

## Normative

Normative documents define mandatory project rules.

Normative documents use RFC 2119 terminology.

Examples:

- CHARTER
- PROJECT_PRINCIPLES
- EDITORIAL_STANDARDS
- ARCHITECTURE
- DATA_MODEL
- API
- RFC

---

## Informative

Informative documents explain ideas, examples, historical information or implementation notes.

They never introduce mandatory requirements.

Examples:

- ADR
- Examples
- Diagrams
- Tutorials
- Migration Guides

---

# Current Specification Documents

| ID | Document | Class | Status | Purpose |
|----|----------|--------|---------|----------|
| DOC-000 | CHARTER.md | Normative | Stable | Defines project mission and governance |
| DOC-001 | PROJECT_PRINCIPLES.md | Normative | Stable | Defines fundamental project principles |
| DOC-002 | DOCUMENT_INDEX.md | Normative | Stable | Defines repository document index |

---

# Planned Documents

The following documents are planned.

| Planned ID | Document |
|------------|----------|
| DOC-003 | EDITORIAL_STANDARDS.md |
| DOC-004 | GLOSSARY.md |
| DOC-005 | RFC_PROCESS.md |
| DOC-006 | ARCHITECTURE.md |
| DOC-007 | DATA_MODEL.md |
| DOC-008 | TELEGRAM_PUBLICATION.md |
| DOC-009 | PARSER_SPECIFICATION.md |
| DOC-010 | PUBLISHER_SPECIFICATION.md |
| DOC-011 | GRAPH_SPECIFICATION.md |
| DOC-012 | DESIGN_SYSTEM.md |
| DOC-013 | ENGINEERING.md |

Document identifiers SHALL NEVER be reused.

Reserved identifiers SHALL remain reserved permanently.

---

# Document Dependencies

```
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
Architecture Specifications
      │
      ▼
Implementation Specifications
```

---

# Repository Rule

Every new normative document MUST be added to this index before it becomes Stable.

---

# References

Depends on:

- CHARTER.md
- PROJECT_PRINCIPLES.md

Referenced by:

- all future specification documents
