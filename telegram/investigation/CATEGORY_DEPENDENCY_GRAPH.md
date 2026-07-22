# CATEGORY_DEPENDENCY_GRAPH

**Document ID:** META002-DEPENDENCY

**Title:** Category Dependency Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Meta-Ontology Investigation

---

# Purpose

This document draws the dependency graph between categories.

---

# Category Dependency Graph

```text
LAYER 0: REALITY
    │
    ▼
LAYER 1: ONTOLOGICAL
    │
    ├──→ Object ←── Identity (Layer 2)
    │         │
    │         ├──→ Event
    │         ├──→ Process ←── Lifecycle (Layer 7)
    │         └──→ State
    │
    ├──→ Relationship (Layer 5)
    ├──→ Collection (Layer 5)
    ├──→ Boundary (Layer 5)
    └──→ Context (Layer 5)
           │
           ▼
LAYER 2: EPISTEMOLOGICAL
    │
    ├──→ Knowledge
    │         │
    │         ▼
    │      Information (Layer 3)
    │         │
    │         ▼
    │      Meaning (Layer 3)
    │
    └──→ Identity
           │
           ▼
LAYER 3: SEMANTIC
    │
    ├──→ Evidence
    │
    └──→ Information
           │
           ▼
LAYER 4: COMMUNICATIVE
    │
    ├──→ Representation
    │         │
    │         ▼
    │      Carrier
    │         │
    │         ▼
    │      Communication
    │
    └──→ Signal
           │
           ▼
LAYER 5: STRUCTURAL
    │
    ├──→ Relationship
    ├──→ Collection
    ├──→ Boundary
    └──→ Context
           │
           ▼
LAYER 6: SOCIAL
    │
    └──→ Role
           │
           ▼
LAYER 7: TEMPORAL
    │
    └──→ Lifecycle
```

---

# Dependency Matrix

| Category | Depends On | Depended By |
|----------|------------|-------------|
| Reality | None | Object, Event, Process, State, Information |
| Object | Reality, Identity | Event, Process, State, Relationship, Collection, Boundary, Context |
| Event | Object | Process |
| Process | Object, Event | Lifecycle, State |
| State | Process | Object |
| Identity | None | Object, Knowledge |
| Knowledge | Reality, Identity | Information, Communication |
| Information | Reality, Knowledge | Meaning, Representation, Evidence |
| Meaning | Information | Communication |
| Evidence | Reality | Communication |
| Representation | Information | Carrier, Communication |
| Carrier | Representation | Communication |
| Communication | Knowledge, Carrier, Evidence | None |
| Signal | Reality | Carrier |
| Relationship | Object | Collection, Boundary |
| Collection | Object, Relationship | None |
| Boundary | Object, Relationship | None |
| Context | Object | None |
| Role | Object | None |
| Lifecycle | Process, Object | None |

---

# Dependency Properties

| Property | Value |
|----------|-------|
| Root categories | 2 (Reality, Identity) |
| Leaf categories | 4 (Communication, Role, Lifecycle, Collection) |
| Central categories | 3 (Object, Information, Representation) |
| Total dependencies | 38 |

---

# Key Insight

**Reality and Identity are the ROOTS — they depend on nothing.**

**Object is the CENTRAL category — most categories depend on it.**

**Communication is the LEAF — it depends on many categories but nothing depends on it.**

---

# End of Category Dependency Graph
