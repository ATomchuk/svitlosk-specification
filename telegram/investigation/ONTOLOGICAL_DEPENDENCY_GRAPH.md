# ONTOLOGICAL_DEPENDENCY_GRAPH

**Document ID:** META001-DEPENDENCY

**Title:** Ontological Dependency Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Ontological Types Investigation

---

# Purpose

This document draws the dependency graph for ontological types.

---

# Ontological Dependency Graph

```text
                    REALITY
                       │
                       ▼
                    Object ←── Identity
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Event       Process ←── Lifecycle
          │            │
          │            ▼
          │          State
          │
          ▼
       Relationship
          │
          ▼
       Collection
          │
          ▼
       Boundary
          │
          ▼
       Context
          │
          ▼
    Information ←── Knowledge
          │
          ▼
    Representation ←── Meaning
          │
          ▼
       Carrier ←── Signal
          │
          ▼
    Communication ←── Evidence
```

---

# Dependency Analysis

| Type | Depends On | Depended By |
|------|------------|-------------|
| Reality | None | Object, Event, Process, State, Information |
| Object | Reality | Event, Process, State, Relationship, Collection, Boundary, Context |
| Identity | None | Object |
| Event | Object | Process |
| Process | Object, Event | Lifecycle, State |
| State | Process | Object |
| Role | Object | — |
| Relationship | Object | Collection, Boundary |
| Collection | Object, Relationship | — |
| Boundary | Object, Relationship | — |
| Context | Object | — |
| Information | Reality, Object | Knowledge, Representation |
| Knowledge | Reality, Information | Communication |
| Representation | Information | Carrier, Communication |
| Carrier | Representation | Communication |
| Communication | Knowledge, Carrier, Evidence | — |
| Meaning | Information | Representation |
| Signal | Reality | Carrier |
| Evidence | Reality | Communication |
| Lifecycle | Process, Object | — |

---

# Dependency Properties

| Property | Value |
|----------|-------|
| Root types | 2 (Reality, Identity) |
| Leaf types | 4 (Communication, Role, Lifecycle, Context) |
| Central types | 3 (Object, Information, Representation) |
| Total dependencies | 38 |

---

# Key Insight

**Reality and Identity are the ROOTS of the ontology.**

**Object is the CENTRAL type — most types depend on it.**

**Communication is the LEAF — it depends on many types but nothing depends on it.**

---

# End of Ontological Dependency Graph
