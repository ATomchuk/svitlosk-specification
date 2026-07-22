# PUBLICATION_LAYER_MODEL

**Document ID:** CASE001-PUB-LAYERS

**Title:** Publication — Layer Model

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Viewpoint Audit №001

---

# Purpose

This document maps Publication across all architectural layers and determines whether the same Publication appears differently on different layers.

---

# Layer Definitions

| Layer | Purpose | Focus |
|-------|---------|-------|
| Reality Layer | Physical/administrative world | What exists without software |
| Business Layer | Business stakeholders and value | What Publication means to the business |
| Domain Layer | Domain concepts and rules | What Publication IS in the domain |
| DDD Layer | Domain-Driven Design analysis | How Publication fits DDD patterns |
| Editorial Layer | Editorial standards and policy | How Publication follows editorial rules |
| Publication Layer | Publication-specific concepts | How Publication is generated and delivered |
| Integration Layer | External system interaction | How Publication interacts with Telegram |
| Telegram Layer | Telegram-specific behavior | How Publication appears on Telegram |
| Persistence Layer | Data storage | How Publication is stored |
| Repository Layer | Specification governance | How Publication is specified |
| Documentation Layer | Terminology and definitions | How Publication is defined |

---

# Publication Across Layers

## Reality Layer

**Publication appears as:** Information about power outages that residents need

**Characteristics:**

- Exists independently of SvitloSk
- Published by DSO
- Observable in reality
- Can be described without software

**Identity:** Content-based (the information itself)

---

## Business Layer

**Publication appears as:** Business artifact serving residents

**Characteristics:**

- Has stakeholders (residents, administrators)
- Has value (timely information)
- Has business rules (Editorial Policy)
- Has quality requirements (accuracy, timeliness)

**Identity:** Territory + Date + Purpose

---

## Domain Layer

**Publication appears as:** Domain entity with invariants

**Characteristics:**

- Has identity (internal ID)
- Has invariants (deterministic, traceable)
- Has lifecycle (Generated → Archived)
- Has relationships (Issue, Territory, Template)

**Identity:** Internal ID

---

## DDD Layer

**Publication appears as:** Aggregate Root

**Characteristics:**

- Owns its lifecycle
- Is referenced by all other concepts
- Has invariants that must be preserved
- Is the central entity in the domain

**Identity:** Internal ID (same as Domain)

---

## Editorial Layer

**Publication appears as:** Editorial product following standards

**Characteristics:**

- Follows Editorial Policy (TJS-020)
- Uses Canonical Templates (TJS-005)
- Follows Formatting Rules (TJS-006)
- Has territorial grammar

**Identity:** Territory + Date + Template

---

## Publication Layer

**Publication appears as:** Deterministic information unit

**Characteristics:**

- Generated from Normalized Dataset
- Rendered using Rendering Rules
- Distributed through Publication Channel
- Archived after Reporting Period

**Identity:** Territory + Date + Template (same as Editorial)

---

## Integration Layer

**Publication appears as:** Telegram message

**Characteristics:**

- Has Telegram Message ID
- Uses Telegram Bot API
- Delivered to Telegram Channel
- Subject to Rate Limiting

**Identity:** Telegram Message ID

---

## Telegram Layer

**Publication appears as:** Channel message

**Characteristics:**

- Visible to Subscribers
- Can be edited (Message Editing)
- Can be deleted (for temporary Publications)
- Has platform-specific formatting

**Identity:** Telegram Message ID (same as Integration)

---

## Persistence Layer

**Publication appears as:** Database record

**Characteristics:**

- Has internal ID
- Has creation timestamp
- Has update timestamp
- Has archive status

**Identity:** Internal ID + Database Key

---

## Repository Layer

**Publication appears as:** Specification artifact

**Characteristics:**

- Defined in GLOSSARY.md
- Referenced in TJS specifications
- Used in governance documents
- Part of the canonical vocabulary

**Identity:** Document ID (different from Publication identity)

---

## Documentation Layer

**Publication appears as:** Normative definition

**Characteristics:**

- Defined once in GLOSSARY.md
- Referenced by all normative documents
- Used consistently across repository
- Part of the ubiquitous language

**Identity:** Term name (different from Publication identity)

---

# Layer Analysis

## Same Object or Different Objects?

**SAME OBJECT.**

**Evidence:**

1. **Same content** — the information about power outages is the same across all layers
2. **Same lifecycle** — the state changes propagate across layers
3. **Same ownership** — the Publication Engine creates and manages it across layers
4. **Same relationships** — it belongs to Issue, contains Territory, etc.
5. **Transformation, not replacement** — each layer transforms the REPRESENTATION, not the CONCEPT

**What changes across layers:**

| What Changes | Examples |
|--------------|----------|
| Format | HTML, database record, specification text |
| Identity mechanism | Internal ID, Telegram Message ID |
| Available operations | read, update, archive |
| Visibility | residents, developers, auditors |

**What does NOT change:**

| What Does NOT Change | Evidence |
|----------------------|----------|
| Information content | Same outage information |
| Territorial scope | Same Territory |
| Temporal scope | Same Date |
| Business purpose | Same resident service |
| Editorial standards | Same formatting rules |

---

## Layer Transition Diagram

```text
Reality Layer (DSO publishes outage data)
    │
    ▼
Business Layer (Publication serves residents)
    │
    ▼
Domain Layer (Publication has identity and invariants)
    │
    ▼
DDD Layer (Publication is Aggregate Root)
    │
    ▼
Editorial Layer (Publication follows editorial standards)
    │
    ▼
Publication Layer (Publication is generated and rendered)
    │
    ▼
Integration Layer (Publication becomes Telegram message)
    │
    ▼
Telegram Layer (Publication is visible on Telegram)
    │
    ▼
Persistence Layer (Publication is stored in database)
    │
    ▼
Repository Layer (Publication is specified in documents)
    │
    ▼
Documentation Layer (Publication is defined in Glossary)
```

---

# End of Layer Model
