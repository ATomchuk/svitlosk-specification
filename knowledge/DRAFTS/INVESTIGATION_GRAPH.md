# Investigation Graph

**Document Class:** Knowledge Freeze

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document represents investigations as a dependency graph.

---

# Investigation Graph

## Visual Representation

```
                    ┌─────────────────┐
                    │ CASE-INF-001    │
                    │ (Information)   │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                 ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │ CASE-JRN-001│ │ CASE-LC-001 │ │ CASE-SYS-001│
    │ (Journal)   │ │ (Lifecycle) │ │ (System)    │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           └───────┬───────┴───────┬───────┘
                   │               │
                   ▼               │
            ┌─────────────┐        │
            │CASE-INFPROD-│        │
            │   001       │        │
            │(Info Product)│       │
            └──────┬──────┘        │
                   │               │
                   └───────┬───────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ CASE-PUB-001│
                    │(Publication)│
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │ CASE-PUB-002│ │ CASE-PUB-003│ │ CASE-PUB-004│
    │(Telegram)   │ │(Semantic)   │ │(Decision)   │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           └───────┬───────┴───────┬───────┘
                   │               │
                   ▼               │
            ┌─────────────┐        │
            │ CASE-PUB-005│        │
            │  (Rules)    │        │
            └──────┬──────┘        │
                   │               │
                   └───────┬───────┘
                           │
                           ▼
                    ┌─────────────┐
                    │CASE-TG-CORE-│
                    │    001      │
                    │(TG Core)    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │CASE-KNOWLEDGE│
                    │   -001      │
                    │(Persistence)│
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │CASE-KNOWLEDGE│
                    │   -002      │
                    │(Canonical)  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ CASE-GAP-001│
                    │   (Gaps)    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────────┐
                    │CASE-GAP-OWNERSHIP│
                    │     -001        │
                    │  (Ownership)    │
                    └──────┬──────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │CASE-HISTORY-│
                    │    001      │
                    │ (History)   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │CASE-DOCARCH-│
                    │    001      │
                    │(Doc Arch)   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────────┐
                    │CASE-KNOWLEDGE-  │
                    │   REUSE-001     │
                    │  (Reuse Audit)  │
                    └──────┬──────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │CASE-DOMAIN- │
                    │   AUDIT-001 │
                    │(Domain)     │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │CASE-ONTOLOGY│ │CASE-ENTITY- │ │CASE-SRC-001 │
    │-LEVELS-001  │ │NATURE-001   │ │ (Source)    │
    └──────┬──────┘ └──────┬──────┘ └─────────────┘
           │               │
           └───────┬───────┘
                   │
                   ▼
            ┌─────────────┐
            │CASE-META-   │
            │  MODEL-001  │
            └──────┬──────┘
                   │
                   ▼
            ┌─────────────┐
            │CASE-FALSIFI-│
            │CATION-001   │
            └─────────────┘
```

---

# Investigation Dependencies

| Investigation | Inputs | Outputs | Used By | Superseded By | Blocked By |
|---------------|--------|---------|---------|---------------|------------|
| CASE-INF-001 | — | Information ontology | CASE-JRN-001, CASE-LC-001, CASE-SYS-001 | — | — |
| CASE-JRN-001 | CASE-INF-001 | Journal ontology | CASE-INFPROD-001 | — | — |
| CASE-LC-001 | CASE-INF-001 | Lifecycle ontology | CASE-SYS-001 | — | — |
| CASE-SYS-001 | CASE-INF-001, CASE-LC-001 | System composition | — | — | — |
| CASE-INFPROD-001 | CASE-INF-001, CASE-JRN-001 | Information products | CASE-TG-CORE-001 | — | — |
| CASE-PUB-001 | — | Publication architecture | CASE-PUB-002, CASE-PUB-003, CASE-PUB-004 | — | — |
| CASE-PUB-002 | CASE-PUB-001 | Telegram operations | CASE-PUB-003, CASE-PUB-004, CASE-TG-CORE-001 | — | — |
| CASE-PUB-003 | CASE-PUB-001, CASE-PUB-002 | Terminology | — | — | — |
| CASE-PUB-004 | CASE-PUB-001, CASE-PUB-002 | Decision model | CASE-PUB-005 | — | — |
| CASE-PUB-005 | CASE-PUB-004 | Business rules | — | — | — |
| CASE-TG-CORE-001 | CASE-PUB-002, CASE-INFPROD-001 | Telegram core | — | — | — |
| CASE-SRC-001 | — | Source audit | — | — | — |
| CASE-KNOWLEDGE-001 | ALL previous | Knowledge persistence | CASE-KNOWLEDGE-002 | — | — |
| CASE-KNOWLEDGE-002 | CASE-KNOWLEDGE-001 | Canonical knowledge | — | — | — |
| CASE-GAP-001 | ALL previous | Gaps | CASE-GAP-OWNERSHIP-001 | — | — |
| CASE-GAP-OWNERSHIP-001 | CASE-GAP-001 | Gap ownership | — | — | — |
| CASE-HISTORY-001 | ALL previous | Historical evolution | — | — | — |
| CASE-DOCARCH-001 | ALL previous | Documentation architecture | — | — | — |
| CASE-KNOWLEDGE-REUSE-001 | ALL previous | Knowledge reuse | — | — | — |
| CASE-DOMAIN-AUDIT-001 | ALL previous | Domain completeness | CASE-ONTOLOGY-LEVELS-001, CASE-ENTITY-NATURE-001 | — | — |
| CASE-ONTOLOGY-LEVELS-001 | CASE-DOMAIN-AUDIT-001 | Architectural levels | CASE-METAMODEL-001 | — | — |
| CASE-ENTITY-NATURE-001 | CASE-DOMAIN-AUDIT-001 | Entity nature | CASE-METAMODEL-001 | — | — |
| CASE-METAMODEL-001 | ALL previous | Meta-model | CASE-FALSIFICATION-001 | — | — |
| CASE-FALSIFICATION-001 | CASE-METAMODEL-001 | Falsified ontology | — | — | — |

---

# Traceability

| Graph | Source |
|-------|--------|
| All dependencies | Analysis of all CASE investigations |

---

**End of Investigation Graph**
