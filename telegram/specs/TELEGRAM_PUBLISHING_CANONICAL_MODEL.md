# TELEGRAM_PUBLISHING_CANONICAL_MODEL

**Document ID:** TJS-010

**Title:** Telegram Publishing Model

**Document Class:** Normative Specification

**Status:** Stable

**Author:** SvitloSk Project

---

# 1. Purpose

This specification defines the publishing model of the Telegram Publishing System. It establishes the publishing architecture, component responsibilities, component interactions, publishing principles, constraints, boundaries, data flow, quality requirements, and governance rules for the Telegram Journal.

This document is normative. All Telegram publishing specifications SHALL conform to the publishing model defined herein.

---

# 2. Scope

This specification covers:

- Publishing architecture
- Component responsibilities
- Component interactions
- Publishing principles (20 principles)
- Publishing constraints
- Publishing boundaries
- Publishing lifecycle overview
- Publishing data flow
- Publishing quality
- Publishing governance
- Semantic boundaries
- Traceability

This specification does NOT define:

- Editorial decisions (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md owns this)
- Lifecycle mechanics (TELEGRAM_PUBLICATION_LIFECYCLE.md owns this)
- Graphic publication rules (TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md owns this)
- Telegram API integration
- Rendering algorithms
- Infrastructure
- Implementation details
- Algorithms

---

# 3. Publishing Architecture

The Telegram Publishing System transforms normalized outage data into deterministic Telegram Journals. The system comprises eight architectural components that collaborate to deliver publications to readers.

## 3.1 Architectural Components

The Publishing System contains the following components:

- **Publication Engine** — Transforms normalized dataset into deterministic Publication Package. Implements the Publisher Role.
- **Parser** — Retrieves Open Data from approved Data Sources. Only component authorized to transform external data.
- **Publisher (Role)** — Logical role for preparing, generating and distributing Publications. Implementation-independent concept.
- **Telegram Publisher** — Telegram-specific implementation of Publisher Role. Handles Telegram Bot API interaction and message delivery.
- **Schedule Generator** — Transforms normalized outage data into deterministic schedules.
- **Graphic Generator** — Produces visual materials based on normalized outage schedules.
- **Data Storage** — Preserving normalized data, publications, schedules, and historical records.
- **Telegram Channel** — Primary public information journal delivering Publications to subscribers.

## 3.2 Architectural Relationships

The Publication Engine implements the Publisher Role. The Parser produces data for the Publication Engine. The Schedule Generator produces schedules for the Publication Engine. The Graphic Generator produces graphics for the Publication Engine. The Data Storage stores data from the Parser and Publication Engine. The Telegram Channel delivers publications from the Publication Engine to Subscribers.

## 3.3 Data Flow

External Data Sources → Parser → Normalized Dataset → Publication Engine → Publication Package → Telegram Publisher → Telegram Channel → Subscribers.

The Schedule Generator receives normalized data and produces schedules. The Graphic Generator receives normalized data and produces graphics. Both feed into the Publication Engine.

---

# 4. Component Responsibilities

## 4.1 Publication Engine

**Purpose:** Transforms normalized dataset into deterministic Publication Package.

**Owns:**
- Publication generation
- Distribution
- Ownership model
- Daily cycle
- Publication windows

**Does NOT own:**
- Editorial content
- Telegram Bot API
- Graphic generation

## 4.2 Parser

**Purpose:** Retrieves Open Data from approved Data Sources.

**Owns:**
- Data retrieval
- Data validation
- Data normalization

**Does NOT own:**
- Interpretation
- Publication
- Rendering

## 4.3 Publisher (Role)

**Purpose:** Logical role for preparing, generating and distributing Publications.

**Owns:**
- Publication preparation
- Generation
- Distribution

**Does NOT own:**
- Data retrieval
- Parsing
- Reinterpretation

## 4.4 Telegram Publisher

**Purpose:** Telegram-specific implementation of Publisher Role.

**Owns:**
- Telegram Bot API interaction
- Message delivery

**Does NOT own:**
- Data retrieval
- Parsing
- Editorial content

## 4.5 Schedule Generator

**Purpose:** Transforms normalized outage data into deterministic schedules.

**Owns:**
- Schedule generation
- Outage period calculation
- Daily schedules
- Change detection

**Does NOT own:**
- Publication rendering
- Telegram delivery

## 4.6 Graphic Generator

**Purpose:** Produces visual materials based on normalized outage schedules.

**Owns:**
- Graphic generation
- Image format
- Size constraints

**Does NOT own:**
- Text publication
- Lifecycle management

## 4.7 Data Storage

**Purpose:** Preserving normalized data, publications, schedules, and historical records.

**Owns:**
- Persistent storage
- Historical preservation
- Metadata

**Does NOT own:**
- Publication rendering
- Telegram delivery

## 4.8 Telegram Channel

**Purpose:** Primary public information journal delivering Publications.

**Owns:**
- Channel delivery
- Subscriber management
- Admin interaction

**Does NOT own:**
- Editorial content
- Lifecycle rules
- Publication generation

---

# 5. Component Interactions

## 5.1 Approved Interactions

| Caller | Callee | Transferred Object | Allowed | Reason |
|--------|--------|-------------------|---------|--------|
| Parser | Publication Engine | Normalized Dataset | YES | Parser produces data for Publication Engine |
| Parser | Data Storage | Normalized Dataset | YES | Parser stores normalized data |
| Publication Engine | Telegram Publisher | Publication Package | YES | Publication Engine produces packages for Telegram delivery |
| Publication Engine | Data Storage | Publication | YES | Publication Engine stores generated publications |
| Publication Engine | Schedule Generator | Schedule Request | YES | Publication Engine requests schedules |
| Publication Engine | Graphic Generator | Graphic Request | YES | Publication Engine requests graphics |
| Telegram Publisher | Telegram Channel | Publication | YES | Telegram Publisher delivers publications to channel |
| Telegram Channel | Subscribers | Publication | YES | Channel delivers publications to readers |
| Administrators | Telegram Channel | Manual Publication | YES | Administrators can create manual publications |
| Administrators | Telegram Channel | Image Publication | YES | Administrators can create image publications |
| Publication Engine | Telegram Channel | Publication (owned) | YES | Engine manages its own publications |

## 5.2 Illegal Interactions

| Interaction | Status | Reason |
|-------------|--------|--------|
| Publication Engine → Manual Publications | ILLEGAL | Engine SHALL NOT modify manual publications |
| Publication Engine → Image Publications | ILLEGAL | Engine SHALL NOT modify image publications |
| Publication Engine → Other publisher's Publications | ILLEGAL | Engine SHALL NOT modify others' publications |
| Parser → Publication Engine (reinterpretation) | ILLEGAL | Parser SHALL NOT interpret data |
| Publication Engine → Parser | ILLEGAL | Engine SHALL NOT retrieve data |
| Subscribers → Telegram Channel (write) | ILLEGAL | Subscribers read only |
| Any component → Glossary (modify) | ILLEGAL | Glossary is read-only semantic authority |

---

# 6. Publishing Principles

The Publishing System is governed by the following twenty canonical principles. These principles are frozen and SHALL NOT change without formal governance.

## 6.1 Repository Authority

TELEGRAM_GLOSSARY.md is the authoritative semantic source for every Telegram specification. When terminology conflicts arise, the Glossary SHALL prevail.

*Source:* TELEGRAM_GLOSSARY.md

## 6.2 Publishing Synchronization

Publication updates SHALL occur only after a new normalized Dataset becomes available. Time alone SHALL NOT trigger Publication updates.

*Source:* TELEGRAM_PUBLICATION_LIFECYCLE.md

## 6.3 Deterministic Publishing

Two identical normalized Datasets SHALL always generate identical Telegram Journals. Publication order, formatting and content SHALL remain deterministic.

*Source:* TELEGRAM_PUBLICATION_LIFECYCLE.md

## 6.4 Editorial Neutrality

Every publication must increase clarity without changing the meaning of the official source. The journal does not interpret, predict or alter official information. It reorganizes and presents it in a form that is easier to understand.

*Source:* TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

## 6.5 Complete Issue

The daily publication package consists of: one post for Starokostiantyniv; one post for every starosta district with available information; separate posts containing information for the following day. Posts without information are not created.

*Source:* TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

## 6.6 Appropriate Complexity

Every new component SHALL solve an existing problem. Complexity SHALL grow only when justified by real project needs. Features SHALL never be added solely because they may become useful.

*Source:* PROJECT_PRINCIPLES.md

## 6.7 Local First Architecture

The Journal exists independently from any publication platform. Telegram itself SHALL NOT be considered the Journal. Telegram SHALL only be considered the publication platform.

*Source:* TELEGRAM_SEMANTIC_MODEL.md

## 6.8 Working Repository

The canonical repository SHALL contain approved knowledge only. Temporary audit artifacts SHALL remain isolated from the canonical documentation.

*Source:* PROJECT_PRINCIPLES.md

## 6.9 Journal Finality

The Telegram Journal SHALL be treated as a long-lived public information journal. The Publisher SHALL modify only Publications that it owns. The Publisher SHALL NOT modify, delete or reorder Publications created by other publishers or administrators.

*Source:* TELEGRAM_PUBLICATION_LIFECYCLE.md

## 6.10 Semantic Ownership

TELEGRAM_SEMANTIC_MODEL.md is the single semantic authority for all Telegram terminology. No Telegram specification SHALL redefine concepts owned by the Semantic Model.

*Source:* TELEGRAM_SEMANTIC_MODEL.md

## 6.11 Single Responsibility

One responsibility. One owner. No shared ownership. Every TJS document SHALL define one complete subject area.

*Source:* TELEGRAM_ARCHITECTURE_DECISION.md

## 6.12 Separation of Concerns

Policy and Implementation are separated across documents. Formatting POLICY is owned by one document; Formatting IMPLEMENTATION is owned by another.

*Source:* TELEGRAM_ARCHITECTURE_DECISION.md

## 6.13 Non-Destructive Channel

The Publisher SHALL modify only Publications that it owns. The Publisher SHALL NOT modify, delete or reorder Publications created by other publishers or administrators.

*Source:* TELEGRAM_PUBLICATION_LIFECYCLE.md

## 6.14 Non-Destructive Update

Updates SHOULD modify existing Publications instead of replacing them. Replacing an existing Publication SHALL be considered a last resort.

*Source:* TELEGRAM_PUBLICATION_LIFECYCLE.md

## 6.15 Stable Journal

The Telegram Journal SHALL remain visually stable throughout the reporting day. Existing Publications SHALL be updated in place whenever possible. Publications SHALL NOT be deleted and recreated solely because their content has changed.

*Source:* TELEGRAM_PUBLICATION_LIFECYCLE.md

## 6.16 Deterministic Rendering

The same normalized dataset SHALL always produce identical output. Two publications generated from identical datasets SHALL be byte-for-byte identical.

*Source:* TELEGRAM_PUBLISHING_PRINCIPLES.md

## 6.17 Source Fidelity

Rendering SHALL NOT modify or reinterpret official information.

*Source:* TELEGRAM_PUBLISHING_PRINCIPLES.md

## 6.18 Dependency Direction

Dependencies flow from the foundation downward. No circular dependencies are permitted.

*Source:* TELEGRAM_ARCHITECTURE_DECISION.md

## 6.19 One Document — One Subject

Every normative document defines one complete subject area. Documents SHOULD complement one another instead of overlapping.

*Source:* PROJECT_PRINCIPLES.md

## 6.20 Accuracy Before Speed

Publishing information quickly is important. Publishing accurate information is mandatory. Whenever these goals conflict, accuracy SHALL take priority.

*Source:* PROJECT_PRINCIPLES.md

---

# 7. Publishing Constraints

The Publishing System is subject to the following architectural and semantic constraints. These constraints are mandatory and SHALL NOT be violated.

## 7.1 Semantic Constraints

- Every Telegram specification SHALL use only Glossary-approved terminology.
- No Telegram specification SHALL redefine concepts owned by the Glossary.
- Every normative document SHALL reference the Glossary for every canonical term.

## 7.2 Architectural Constraints

- The Publishing System owns only publishing responsibilities.
- The Publishing System SHALL NOT duplicate Editorial responsibilities.
- The Publishing System SHALL NOT duplicate Lifecycle responsibilities.
- The Publishing System SHALL NOT duplicate Graphic Publication responsibilities.
- One responsibility. One owner. No shared ownership.
- Dependencies flow from the foundation downward. No circular dependencies.
- Policy and Implementation are separated across documents.

## 7.3 Repository Constraints

- The canonical repository SHALL contain approved knowledge only.
- Temporary audit artifacts SHALL remain isolated from the canonical documentation.
- TELEGRAM_GLOSSARY.md is the authoritative semantic source for every Telegram specification.
- TELEGRAM_SEMANTIC_MODEL.md is the single semantic authority for all Telegram terminology.

## 7.4 Publishing Constraints

- Every publication SHALL be deterministic for identical input.
- Every publication SHALL preserve the factual meaning of official data.
- Every publication SHALL be accessible to all residents.
- Every publication SHALL be delivered promptly.
- The Telegram Journal SHALL remain visually stable throughout the reporting day.
- Publication updates SHALL occur only after a new normalized Dataset becomes available.

## 7.5 Specification Constraints

- Every normative document SHALL define one complete subject area.
- Documents SHOULD complement one another instead of overlapping.
- The Canonical Specification Standard SHALL be followed.
- The Document Identity Model SHALL be followed.
- The Naming Standard SHALL be followed.

---

# 8. Publishing Boundaries

## 8.1 What the Publishing System Owns

| Component | Owns |
|-----------|------|
| Publication Engine | Publication generation, distribution, ownership model, daily cycle, publication windows |
| Parser | Data retrieval, data validation, data normalization |
| Publisher (Role) | Publication preparation, generation, distribution |
| Telegram Publisher | Telegram Bot API interaction, message delivery |
| Schedule Generator | Schedule generation, outage period calculation, daily schedules, change detection |
| Graphic Generator | Graphic generation, image format, size constraints |
| Data Storage | Persistent storage, historical preservation, metadata |
| Telegram Channel | Channel delivery, subscriber management, admin interaction |

## 8.2 What the Publishing System Does NOT Own

| Responsibility | Owner |
|---------------|-------|
| Editorial decisions | TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md |
| Publication lifecycle mechanics | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| Graphic publication rules | TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md |
| Semantic terminology | TELEGRAM_SEMANTIC_MODEL.md |
| Glossary definitions | TELEGRAM_GLOSSARY.md |
| Telegram API integration | Implementation |
| Rendering algorithms | Implementation |
| Infrastructure | Implementation |

---

# 9. Publishing Lifecycle Overview

The Publishing System interacts with the Publication Lifecycle defined in TELEGRAM_PUBLICATION_LIFECYCLE.md. This section provides a brief overview.

## 9.1 Lifecycle States

Publications pass through the following states: Generated, Published, Updated, Archived, Removed.

## 9.2 Lifecycle Transitions

Publications transition between states according to defined rules. The Repository Authority Principle governs all publication transitions: the Repository is the single authoritative source of truth for the publication state of the Telegram Journal.

## 9.3 Repository Authority

Repository SHALL be the single authoritative source of truth for the publication state of the Telegram Journal. Telegram SHALL only represent the current Repository state and SHALL never become an independent source of publication truth.

*For complete lifecycle mechanics, refer to TELEGRAM_PUBLICATION_LIFECYCLE.md.*

---

# 10. Publishing Data Flow

The Publishing System processes data through the following flow:

1. **External Data Sources** provide open data on electricity outages.
2. **Parser** retrieves, validates, and normalizes the data.
3. **Schedule Generator** transforms normalized data into deterministic schedules.
4. **Graphic Generator** produces visual materials from normalized data.
5. **Publication Engine** assembles the Publication Package.
6. **Telegram Publisher** delivers the package to the Telegram Channel.
7. **Telegram Channel** publishes to subscribers.

Data Storage persists normalized data, publications, schedules, and historical records throughout this flow.

---

# 11. Publishing Quality

The Publishing System maintains the following quality requirements:

- **Deterministic Output** — Two identical normalized Datasets SHALL always generate identical Telegram Journals. Publication order, formatting and content SHALL remain deterministic.
- **Canonical Equality** — Two publications generated from identical datasets SHALL be byte-for-byte identical. Equivalent publications SHALL NOT generate Telegram edits.
- **Source Fidelity** — Rendering SHALL NOT modify or reinterpret official information.
- **Accuracy Before Speed** — Publishing accurate information is mandatory. Whenever speed and accuracy conflict, accuracy SHALL take priority.

---

# 12. Publishing Governance

The Publishing System is governed by the following rules:

- The Canonical Specification Standard SHALL be followed for all Telegram specifications.
- The Document Identity Model SHALL be used for document identification.
- The Naming Standard SHALL be used for document naming.
- Changes to the Publishing System SHALL follow the approved ADR process.
- TELEGRAM_GLOSSARY.md is the authoritative semantic source for every Telegram specification.
- Dependencies flow from the foundation downward. No circular dependencies are permitted.

---

# 13. Semantic Boundaries

| Domain | The Publishing System Owns | The Publishing System Uses | The Publishing System References | The Publishing System Must NOT Define |
|--------|--------------------------|---------------------------|----------------------------------|--------------------------------------|
| Journal | — | Publication, Issue | Semantic Model | Journal definition |
| Publication | — | Publication Lifecycle | Lifecycle Model | Lifecycle states |
| Telegram | — | Telegram Channel | — | Telegram platform rules |
| Publishing Engine | Publication generation | — | — | Editorial content |
| Parser | Data retrieval | — | — | Interpretation |
| Publisher | Distribution | — | — | Data retrieval |

---

# 14. Out of Scope

This specification does NOT define:

- Editorial decisions (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md owns this)
- Publication lifecycle mechanics (TELEGRAM_PUBLICATION_LIFECYCLE.md owns this)
- Graphic publication rules (TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md owns this)
- Telegram API integration
- Rendering algorithms
- Infrastructure
- Implementation details
- Algorithms

---

# 15. Traceability

| Section | Source |
|---------|--------|
| §1 Purpose | TELEGRAM_SEMANTIC_MODEL.md, TELEGRAM_GLOSSARY.md |
| §2 Scope | TELEGRAM_SEMANTIC_MODEL.md, TELEGRAM_PUBLISHING_HARVEST.md |
| §3 Publishing Architecture | TELEGRAM_ARCHITECTURE_DECISION.md, TELEGRAM_PUBLISHING_COMPONENT_MATRIX.md |
| §4 Component Responsibilities | TELEGRAM_PUBLISHING_COMPONENT_MATRIX.md, TELEGRAM_PUBLISHING_RESPONSIBILITY_MATRIX.md |
| §5 Component Interactions | TELEGRAM_PUBLISHING_INTERACTION_MATRIX.md, TELEGRAM_PUBLISHING_COMPONENT_MATRIX.md |
| §6 Publishing Principles | TELEGRAM_PUBLISHING_PRINCIPLES.md, PROJECT_PRINCIPLES.md |
| §7 Publishing Constraints | TELEGRAM_ARCHITECTURE_DECISION.md, TELEGRAM_GLOSSARY.md |
| §8 Publishing Boundaries | TELEGRAM_SEMANTIC_MODEL.md, TELEGRAM_ARCHITECTURE_DECISION.md |
| §9 Publishing Lifecycle Overview | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| §10 Publishing Data Flow | TELEGRAM_PUBLISHING_COMPONENT_MATRIX.md, TELEGRAM_PUBLISHING_INTERACTION_MATRIX.md |
| §11 Publishing Quality | TELEGRAM_PUBLISHING_PRINCIPLES.md, PROJECT_PRINCIPLES.md |
| §12 Publishing Governance | TELEGRAM_ARCHITECTURE_DECISION.md, TELEGRAM_GLOSSARY.md |
| §13 Semantic Boundaries | TELEGRAM_SEMANTIC_MODEL.md, TELEGRAM_ARCHITECTURE_DECISION.md |
| §14 Out of Scope | TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md, TELEGRAM_PUBLICATION_LIFECYCLE.md, TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md |
| §15 Traceability | All referenced specifications |
| §16 Change History | — |
| §17 References | TELEGRAM_SEMANTIC_MODEL.md, TELEGRAM_GLOSSARY.md, TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md, TELEGRAM_PUBLICATION_LIFECYCLE.md, TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md |

---

# 16. Change History

| Date | Version | Description |
|------|---------|-------------|
| 2026-07-13 | 1.0 | Initial compilation from approved Blueprint and Knowledge Base |

---

# 17. References

## Depends on

- TELEGRAM_SEMANTIC_MODEL.md (TJS-000)
- TELEGRAM_GLOSSARY.md (TJS-000A)
- TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md (TJS-020)
- TELEGRAM_PUBLICATION_LIFECYCLE.md (TJS-021)
- TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md (TJS-022)
- PROJECT_PRINCIPLES.md
- TELEGRAM_ARCHITECTURE_DECISION.md
- TELEGRAM_CANONICAL_SPECIFICATION_STANDARD.md

## Referenced by

- TELEGRAM_PUBLISHING_MODEL.md (future working materials)
- TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md (TJS-020)
- TELEGRAM_PUBLICATION_LIFECYCLE.md (TJS-021)
- TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md (TJS-022)

---

**End of Specification**

**Compiler:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
