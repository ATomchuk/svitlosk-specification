# Ontology Graph

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document constructs the ontology graph.

---

# Ontology Graph

## Visual Representation

```
                    ┌─────────────┐
                    │     DSO     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Open Data  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Parser    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │Parsed Data  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │Normalized   │
                    │ Dataset     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │Interpreter  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │Interpretation│
                    │ Result      │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Publisher   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │Publication  │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  Journal    │ │Information  │ │Territory    │
    │  Edition    │ │  Product    │ │             │
    └──────┬──────┘ └──────┬──────┘ └─────────────┘
           │               │
           └───────┬───────┘
                   │
                   ▼
            ┌─────────────┐
            │ Representation│
            └──────┬──────┘
                   │
                   ▼
            ┌─────────────┐
            │   Adapter   │
            └──────┬──────┘
                   │
                   ▼
            ┌─────────────┐
            │   Channel   │
            └──────┬──────┘
                   │
                   ▼
            ┌─────────────┐
            │  Residents  │
            └─────────────┘
```

---

# Graph Analysis

## Root Objects

| Object | Why Root |
|--------|----------|
| DSO | External source |
| Open Data | External data |

## Leaf Objects

| Object | Why Leaf |
|--------|----------|
| Residents | End consumer |
| Channel | End delivery |

## Central Objects

| Object | Why Central |
|--------|-------------|
| Parser | Data processing hub |
| Publisher | Publication hub |
| Adapter | Channel hub |

---

# Traceability

| Graph | Source |
|-------|--------|
| All graph elements | Analysis of entity classification and architectural levels |

---

**End of Ontology Graph**
