# SYS001_DEPENDENCY

**Document ID:** CASE-SYS-001-DEP

**Title:** System Dependency Graph

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document produces a System Dependency Graph.

Objects only. No implementation.

---

# 2. Root Objects

Objects with NO upstream dependencies:

| Object | Source |
|--------|--------|
| DSO | External |
| Community | TERRITORIAL_MODEL |
| Administrative Centre | TERRITORIAL_MODEL |
| Starosta District | TERRITORIAL_MODEL |
| Settlement | TERRITORIAL_MODEL |
| Street | TERRITORIAL_MODEL |
| Address | TERRITORIAL_MODEL |

---

# 3. Dependency Graph

## 3.1 Visual Representation

```
                    ┌─────────────┐
                    │     DSO     │
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
Official Queue       Official Planned    Official Emergency
   Schedule              Outages             Outages
         │                 │                 │
         ▼                 ▼                 ▼
    Parser A           Parser B           Parser B
         │                 │                 │
         ▼                 │                 │
Queue Schedule              │                 │
Information                 │                 │
         │                 │                 │
    ┌────┴────┐            │                 │
    ▼         ▼            │                 │
  Queue   Subqueue         │                 │
Information Information    │                 │
    │         │            │                 │
    ▼         ▼            │                 │
 Schedule  Schedule        │                 │
Information Information    │                 │
    │         │            │                 │
    └────┬────┘            │                 │
         ▼                 │                 │
Queue Timetable            │                 │
Information                │                 │
         │                 │                 │
    ┌────┴────┐            │                 │
    ▼         ▼            │                 │
Timeline  Tomorrow         │                 │
         Graph             │                 │
                           │                 │
         ┌─────────────────┴─────────────────┘
         ▼
    Journal Edition
    Information
         │
    ┌────┴────────────────────────────┐
    ▼                 ▼               ▼
Planned Outage  Emergency Outage  Tomorrow Queue
Information     Information       Graph Information
         │                 │               │
         └─────────────────┴───────────────┘
                           │
                           ▼
                    Publication
                    Information
                           │
                           ▼
                    Territory
                    Information
                           │
                           ▼
                    Publishing
                    Subsystem
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         Telegram      Facebook       PWA
         Adapter       Adapter     Application
              │            │            │
              ▼            ▼            ▼
         Telegram      Facebook     PWA Display
         Post          Post
              │            │
              └────────────┘
                     │
                     ▼
                Residents
```

---

# 4. Root Objects

| Root Object | Domain |
|-------------|--------|
| DSO | External |
| Community | Territorial |
| Administrative Centre | Territorial |
| Starosta District | Territorial |
| Settlement | Territorial |
| Street | Territorial |
| Address | Territorial |

---

# 5. Leaf Objects

| Leaf Object | Domain |
|-------------|--------|
| Timeline | Domain A |
| Tomorrow Graph | Domain A |
| Telegram Post | Publishing |
| Facebook Post | Publishing |
| PWA Display | PWA |
| Residents | External |

---

# 6. Findings

## 6.1 Finding DEP-001

**The dependency graph has 7 root objects.**

DSO and 6 Territorial objects.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 6.2 Finding DEP-002

**There are 6 leaf objects.**

Timeline, Tomorrow Graph, Telegram Post, Facebook Post, PWA Display, Residents.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 6.3 Finding DEP-003

**The graph has THREE main branches.**

Domain A (Queue Schedule), Domains B/C (Outages), and Territorial.

**Evidence:** Analysis of dependency structure.

**Confidence:** HIGH.

---

# 7. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| DEP-001 | Analysis of all evidence sources |
| DEP-002 | Analysis of all evidence sources |
| DEP-003 | Analysis of dependency structure |

---

**End of System Dependency Graph**
