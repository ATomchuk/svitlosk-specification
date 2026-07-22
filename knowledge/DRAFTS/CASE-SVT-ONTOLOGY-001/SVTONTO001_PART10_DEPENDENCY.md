# SVTONTO001_PART10_DEPENDENCY

**Document ID:** CASE-SVT-ONTOLOGY-001-P10

**Title:** Dependency Graph

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs the complete dependency graph of SvitloSk concepts.

---

# 2. Root Concepts

Concepts with NO upstream dependencies:

| Concept | Source |
|---------|--------|
| DSO (Data Source) | GLOSSARY |
| Official Schedule | Architect Intent |
| Official Planned Outages | Architect Intent |
| Official Emergency Outages | Architect Intent |
| Community | TERRITORIAL |
| Administrative Centre | TERRITORIAL |
| Starosta District | TERRITORIAL |
| Settlement | TERRITORIAL |
| Street | TERRITORIAL |
| Address | TERRITORIAL |

---

# 3. Domain A Dependencies

## 3.1 Queue Schedule Flow

```
DSO
    ↓ publishes
Official Schedule
    ↓ collected by
Parser A
    ↓ produces
Queue Timetable
    ↓ contains
Queue (1-6)
    ↓ contains
Subqueue (1.1-6.2)
    ↓ has
Schedule (hourly)
    ↓ displayed as
Timeline
    ↓ or
Tomorrow Graph
    ↓ consumed by
PWA (Main Screen)
    ↓ triggers
Push Notification
```

## 3.2 Queue Schedule Dependencies

| Concept | Depends On |
|---------|------------|
| Queue Timetable | Official Schedule, Parser A |
| Queue | Queue Timetable |
| Subqueue | Queue |
| Schedule | Subqueue, Time |
| Timeline | Schedule (multiple) |
| Tomorrow Graph | Schedule (12 subqueues) |
| Push Notification | Schedule, Subqueue |

---

# 4. Domain B Dependencies

## 4.1 Planned Outage Flow

```
DSO
    ↓ publishes
Official Planned Outages
    ↓ collected by
Parser B
    ↓ produces
Address Information
    ↓ contains
Settlement
    ↓ contains
Street
    ↓ contains
House
    ↓ with
Planned Time Interval
```

## 4.2 Planned Outage Dependencies

| Concept | Depends On |
|---------|------------|
| Address Information | Official Planned Outages, Parser B |
| Planned Outage | Address, Planned Time Interval |

---

# 5. Domain C Dependencies

## 5.1 Emergency Outage Flow

```
DSO
    ↓ publishes
Official Emergency Outages
    ↓ collected by
Parser B
    ↓ produces
Address Information
    ↓ contains
Settlement
    ↓ contains
Street
    ↓ contains
House
    ↓ with
Emergency Information
```

## 5.2 Emergency Outage Dependencies

| Concept | Depends On |
|---------|------------|
| Address Information | Official Emergency Outages, Parser B |
| Emergency Outage | Address, Emergency Information |

---

# 6. Journal Dependencies

## 6.1 Journal Flow

```
Journal (Service)
    ↓ produces
Journal Edition (one per day)
    ↓ contains
Publication (per Territory)
    ↓ organized by
Territory (Starosta District)
    ↓ delivered via
Publishing Subsystem
    ↓ uses
Telegram Adapter / Facebook Adapter
    ↓ delivers to
Channel (Telegram / Facebook)
```

## 6.2 Journal Dependencies

| Concept | Depends On |
|---------|------------|
| Journal Edition | Journal, Date |
| Publication | Journal Edition, Territory, Content |
| Territory | Community, Starosta District |

---

# 7. Publishing Dependencies

## 7.1 Publishing Flow

```
Publishing Subsystem (Service)
    ↓ uses
Telegram Adapter
    ↓ or
Facebook Adapter
    ↓ delivers
Publication
    ↓ rendered as
Representation
    ↓ to
Channel
```

## 7.2 Publishing Dependencies

| Concept | Depends On |
|---------|------------|
| Telegram Adapter | Publishing Subsystem |
| Facebook Adapter | Publishing Subsystem |
| Representation | Publication, Channel |

---

# 8. PWA Dependencies

## 8.1 PWA Flow

```
PWA Application
    ↓ contains
Screen (Main, Archive, Address Lookup, Personal Cabinet)
    ↓ Main Screen contains
Timeline
Tomorrow Graph
    ↓ Address Lookup Screen contains
Address → Subqueue mapping
    ↓ Personal Cabinet contains
Configuration items
```

## 8.2 PWA Dependencies

| Concept | Depends On |
|---------|------------|
| Main Screen | Timeline, Tomorrow Graph |
| Archive Screen | Historical Schedules |
| Address Lookup Screen | Address, Subqueue |
| Personal Cabinet | User Configuration |

---

# 9. Dependency Graph

## 9.1 Visual Representation

```
                    ┌─────────────┐
                    │     DSO     │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    Official Schedule  Official Planned  Official Emergency
           │               │               │
           ▼               ▼               ▼
       Parser A         Parser B         Parser B
           │               │               │
           ▼               ▼               ▼
    Queue Timetable  Address Info    Address Info
           │               │               │
           ▼               │               │
    ┌──────┴──────┐        │               │
    ▼             ▼        │               │
  Queue       Subqueue     │               │
    │             │        │               │
    ▼             ▼        ▼               ▼
  Schedule    Schedule  Planned Outage  Emergency Outage
    │             │        │               │
    ▼             ▼        │               │
  Timeline    Tomorrow    │               │
    │         Graph       │               │
    │             │        │               │
    └──────┬──────┘        │               │
           ▼               │               │
         PWA               │               │
                           │               │
           ┌───────────────┴───────────────┘
           ▼
      Journal Edition
           │
           ▼
       Publication
           │
           ▼
    Publishing Subsystem
           │
    ┌──────┴──────┐
    ▼             ▼
  Telegram    Facebook
  Adapter     Adapter
    │             │
    ▼             ▼
  Channel     Channel
```

---

# 10. Root Concepts

| Root Concept | Domain |
|--------------|--------|
| DSO | All |
| Official Schedule | Queue Schedule |
| Official Planned Outages | Planned Outages |
| Official Emergency Outages | Emergency Outages |
| Community | Territorial |
| Administrative Centre | Territorial |
| Starosta District | Territorial |

---

# 11. Leaf Concepts

| Leaf Concept | Domain |
|--------------|--------|
| Push Notification | Queue Schedule |
| Timeline | Queue Schedule |
| Tomorrow Graph | Queue Schedule |
| Publication | Journal |
| Representation | Publishing |
| Channel | Publishing |

---

# 12. Findings

## 12.1 Finding DEP-001

**The dependency graph has SEVEN root concepts.**

DSO, Official Schedule, Official Planned Outages, Official Emergency Outages, Community, Administrative Centre, Starosta District.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 12.2 Finding DEP-002

**There are THREE independent dependency chains.**

Queue Schedule chain, Planned Outage chain, Emergency Outage chain.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 12.3 Finding DEP-003

**The Journal chain depends on Territory (Starosta District).**

Journal Editions are organized by Territory.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 12.4 Finding DEP-004

**The Publishing chain depends on Journal.**

Publishing Subsystem delivers Publications from Journal.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 13. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| DEP-001 | Analysis of all evidence sources |
| DEP-002 | Architect Intent |
| DEP-003 | Architect Intent |
| DEP-004 | Architect Intent |

---

**End of Dependency Graph**
