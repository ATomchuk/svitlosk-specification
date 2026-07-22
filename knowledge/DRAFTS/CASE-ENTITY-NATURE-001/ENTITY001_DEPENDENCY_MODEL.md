# Dependency Model

**Document Class:** Entity Nature Investigation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity dependency model.

---

# Dependency Model

## Root Entities (No Dependencies)

| Entity | Nature | Evidence |
|--------|--------|----------|
| DSO | EXTERNAL | GLOSSARY §2 |
| Open Data | CONCEPT | GLOSSARY §2 |
| Territory | REFERENCE | GLOSSARY §4 |
| Information | CONCEPT | CASE-INF-001 |
| Knowledge | CONCEPT | CASE-INF-001 |

---

## First-Level Dependencies

| Entity | Depends On | Nature | Evidence |
|--------|------------|--------|----------|
| Parser | Open Data | SERVICE | GLOSSARY §2 |
| Parsed Data | Parser | ARTIFACT | GLOSSARY §2 |
| Normalized Dataset | Parser | ARTIFACT | TELEGRAM_PUBLISHING_CANONICAL_MODEL.md |

---

## Second-Level Dependencies

| Entity | Depends On | Nature | Evidence |
|--------|------------|--------|----------|
| Publisher | Normalized Dataset | SERVICE + ROLE | GLOSSARY §7 |
| Publication | Publisher | ARTIFACT | GLOSSARY §3 |
| Publication Package | Publisher | COLLECTION | GLOSSARY §3 |
| Journal Edition | Publisher | INSTANCE | CASE-JRN-001 |

---

## Third-Level Dependencies

| Entity | Depends On | Nature | Evidence |
|--------|------------|--------|----------|
| Journal | Journal Edition | SERVICE | CHARTER §10 |
| Representation | Publication | ARTIFACT | CASE-INF-001 |
| Channel | Adapter | SERVICE | GLOSSARY §3 |
| Adapter | Publisher | SERVICE + ROLE | CASE-SVT-ONTOLOGY-001 |

---

# Dependency Graph

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
                    │ Publisher   │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │Publication  │ │Publication  │ │Journal      │
    │             │ │ Package     │ │ Edition     │
    └──────┬──────┘ └─────────────┘ └──────┬──────┘
           │                               │
           ▼                               ▼
    ┌─────────────┐                 ┌─────────────┐
    │Representation│                 │   Journal   │
    └──────┬──────┘                 └─────────────┘
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

# Dependency Summary

| Dependency Level | Entities | Count |
|------------------|----------|-------|
| Level 0 (Root) | DSO, Open Data, Territory, Information, Knowledge | 5 |
| Level 1 | Parser, Parsed Data, Normalized Dataset | 3 |
| Level 2 | Publisher, Publication, Publication Package, Journal Edition | 4 |
| Level 3 | Journal, Representation, Channel, Adapter | 4 |
| **Total** | | **16** |

---

# Traceability

| Dependency Model | Source |
|------------------|--------|
| All dependencies | Analysis of entity nature and domain knowledge |

---

**End of Dependency Model**
