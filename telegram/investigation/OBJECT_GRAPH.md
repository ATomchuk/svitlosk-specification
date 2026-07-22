# OBJECT_GRAPH

**Document ID:** CASE001E-GRAPH

**Title:** Object Existential Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Object Ontology Investigation

---

# Purpose

This document constructs the complete Object existential graph showing how objects exist in relation to each other.

---

# Existential Graph

## Layer 1: Reality (Pre-SvitloSk)

```text
REALITY
    │
    ├──→ Community (exists in reality)
    │       │
    │       ├──→ Administrative Centre
    │       └──→ Starosta District
    │               │
    │               └──→ Settlement
    │                       │
    │                       └──→ Street
    │                               │
    │                               └──→ Address
    │
    ├──→ Queue (exists in reality)
    │       │
    │       └──→ Subqueue
    │
    └──→ Outage (exists in reality)
            │
            ├──→ Planned Power Outage
            └──→ Emergency Power Outage
```

**Characteristics:**

- Objects exist independently of SvitloSk
- Official designation
- Stable
- Predate the system

---

## Layer 2: Business Domain (SvitloSk-Created)

```text
BUSINESS DOMAIN
    │
    ├──→ Journal (continuous publication)
    │       │
    │       └──→ Issue (one editorial edition)
    │               │
    │               └──→ Publication (one information unit)
    │                       │
    │                       ├──→ Territory (scope)
    │                       ├──→ Template (format)
    │                       └──→ Content (information)
    │
    └──→ Publication Package (collection)
            │
            └──→ Contains Publications
```

**Characteristics:**

- Created by SvitloSk business logic
- Business meaning
- Lifecycle management
- Identity management

---

## Layer 3: Information Domain (Data Processing)

```text
INFORMATION DOMAIN
    │
    ├──→ Open Data (external input)
    │       │
    │       └──→ Parser
    │               │
    │               └──→ Normalized Dataset
    │                       │
    │                       ├──→ Publication Engine
    │                       │       │
    │                       │       └──→ Publication
    │                       │
    │                       ├──→ Schedule Generator
    │                       │       │
    │                       │       └──→ Schedule
    │                       │
    │                       └──→ Graphic Generator
    │                               │
    │                               └──→ Graphic
    │
    └──→ Interpretation Result
            │
            └──→ Publication
```

**Characteristics:**

- Derived from data
- Processing-dependent
- Traceable
- Temporary or permanent

---

## Layer 4: Representation Domain (Projections)

```text
REPRESENTATION DOMAIN
    │
    ├──→ Telegram Message (platform projection)
    │       │
    │       └──→ References Publication
    │
    ├──→ Repository Object (storage projection)
    │       │
    │       └──→ References Publication
    │
    ├──→ Historical Record (archive projection)
    │       │
    │       └──→ Preserves Publication
    │
    └──→ Editorial Record (editorial projection)
            │
            └──→ Follows Publication standards
```

**Characteristics:**

- Borrow Identity from domain objects
- Context-specific
- May have own Identifiers
- Projections, not independent objects

---

## Layer 5: Architecture Domain (System Building Blocks)

```text
ARCHITECTURE DOMAIN
    │
    ├──→ Components
    │       │
    │       ├──→ Publication Engine (creates Publications)
    │       ├──→ Parser (retrieves data)
    │       ├──→ Schedule Generator (generates schedules)
    │       ├──→ Graphic Generator (generates graphics)
    │       ├──→ Telegram Publisher (delivers to Telegram)
    │       ├──→ Data Storage (persists data)
    │       └──→ Telegram Channel (displays to readers)
    │
    ├──→ Roles
    │       │
    │       ├──→ Publisher (logical responsibility)
    │       └──→ Interpreter (logical responsibility)
    │
    └──→ Interfaces
            │
            ├──→ Telegram Bot API
            └──→ Data Storage API
```

**Characteristics:**

- Implementation units
- Stable architectural identity
- NOT business concepts
- System design

---

# Cross-Layer Relationships

```text
REALITY
    │
    │ (traces to)
    ▼
BUSINESS DOMAIN
    │
    │ (derives from)
    ▼
INFORMATION DOMAIN
    │
    │ (projects to)
    ▼
REPRESENTATION DOMAIN
    │
    │ (implemented by)
    ▼
ARCHITECTURE DOMAIN
```

---

# Key Insight

**Objects exist in a hierarchical existential order:**

1. **Reality** — objects that exist independently
2. **Business Domain** — objects created by business logic
3. **Information Domain** — objects created by data processing
4. **Representation Domain** — projections of domain objects
5. **Architecture Domain** — system building blocks

**Each layer depends on the layers above it.**

**Reality is the foundation. Architecture is the implementation.**

---

# End of Object Existential Graph
