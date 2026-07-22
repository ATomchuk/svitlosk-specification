# Entity Dependency Graph

**Document Class:** Domain Completeness Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document constructs the entity dependency graph.

---

# Entity Dependency Graph

## Visual Representation

```
                    ┌─────────────┐
                    │     DSO     │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │ Open Data   │ │ Schedule    │ │ Information │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           ▼               │               │
    ┌─────────────┐        │               │
    │   Parser    │        │               │
    └──────┬──────┘        │               │
           │               │               │
           ▼               │               │
    ┌─────────────┐        │               │
    │Parsed Data  │        │               │
    └──────┬──────┘        │               │
           │               │               │
           ▼               │               │
    ┌─────────────┐        │               │
    │Normalized   │        │               │
    │ Dataset     │        │               │
    └──────┬──────┘        │               │
           │               │               │
           └───────────────┼───────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Publisher   │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │Publication  │ │Publication  │ │Publication  │
    │  Engine     │ │  Package    │ │  State      │
    └─────────────┘ └─────────────┘ └─────────────┘
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
    └─────────────┘ └─────────────┘ └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Representation│
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

# Dependency Levels

## Level 0: Root Objects

| Object | Why Root |
|--------|----------|
| DSO | External source |
| Community | Territorial root |

## Level 1: First-Level Dependencies

| Object | Depends On |
|--------|------------|
| Open Data | DSO |
| Schedule | DSO |
| Information | DSO |
| Territory | Community |

## Level 2: Second-Level Dependencies

| Object | Depends On |
|--------|------------|
| Parser | Open Data |
| Parsed Data | Parser |
| Normalized Dataset | Parser |
| Administrative Centre | Community |
| Starosta District | Community |
| Settlement | Territory |

## Level 3: Third-Level Dependencies

| Object | Depends On |
|--------|------------|
| Publisher | Normalized Dataset, Schedule, Information |
| Publication Engine | Parser, Publisher |
| Publication Package | Publisher, Publication |
| Street | Settlement |
| Address | Street |

## Level 4: Fourth-Level Dependencies

| Object | Depends On |
|--------|------------|
| Publication | Publisher, Interpretation Result |
| Publication State | Publication |
| Publication Version | Publication |
| Publication History | Publication |
| Publication Identity | Publication |
| Publication Context | Publication |

## Level 5: Fifth-Level Dependencies

| Object | Depends On |
|--------|------------|
| Journal | Publication |
| Journal Edition | Publication, Territory |
| Information Product | Publication |
| Emergency Outage Publication | Emergency Outage |
| Planned Outage Publication | Planned Outage |
| Queue Graph Publication | Schedule |
| Technical Publication | System Status |
| Service Publication | Service Announcement |

## Level 6: Sixth-Level Dependencies

| Object | Depends On |
|--------|------------|
| Representation | Publication |
| Rendering | Publication |
| Channel | Adapter |
| Adapter | Publisher |
| Telegram Adapter | Adapter, Publisher |
| Facebook Adapter | Adapter, Publisher |

## Level 7: Seventh-Level Dependencies

| Object | Depends On |
|--------|------------|
| Archive | Publication |
| Historical Record | Archive |

---

# Traceability

| Dependency | Source |
|------------|--------|
| All dependencies | Analysis of entity inventory and relationships |

---

**End of Entity Dependency Graph**
