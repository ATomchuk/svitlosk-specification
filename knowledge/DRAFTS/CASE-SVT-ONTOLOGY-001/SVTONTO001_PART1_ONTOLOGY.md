# SVTONTO001_PART1_ONTOLOGY

**Document ID:** CASE-SVT-ONTOLOGY-001-P1

**Title:** Complete Ontology

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document reconstructs the complete ontology of SvitloSk, identifying all objects, services, processes, roles, data sources, representations, identity dimensions, channels and adapters.

---

# 2. Ontological Categories

## 2.1 Objects

Discrete, identifiable entities that exist in the system.

| Object | Source | Atomic? |
|--------|--------|---------|
| Queue | GLOSSARY, Architect Intent | YES |
| Subqueue | GLOSSARY, Architect Intent | YES |
| Schedule | GLOSSARY, Architect Intent | YES |
| Planned Outage | GLOSSARY, Architect Intent | YES |
| Emergency Outage | GLOSSARY, Architect Intent | YES |
| Address | GLOSSARY, TERRITORIAL | YES |
| Publication | GLOSSARY | YES |
| Journal Edition | Architect Intent | NO (composite) |
| Publication Package | GLOSSARY | NO (composite) |
| Timeline | Architect Intent | NO (composite) |
| Tomorrow Graph | Architect Intent | NO (composite) |

## 2.2 Services

Continuous activities performed by the system.

| Service | Source | Description |
|---------|--------|-------------|
| SvitloSk | CHARTER | Local public information service |
| Publishing Subsystem | Architect Intent | Publication of Journal |

## 2.3 Processes

Discrete activities that transform data.

| Process | Source | Input | Output |
|---------|--------|-------|--------|
| Data Retrieval | GLOSSARY | Open Data | Parsed Data |
| Parsing | GLOSSARY | Raw Data | Normalized Data |
| Interpretation | GLOSSARY | Normalized Data | Interpretation Result |
| Publication Generation | GLOSSARY | Interpretation Result | Publication |
| Rendering | GLOSSARY | Interpretation Result | Publication |
| Distribution | GLOSSARY | Publication | Channel |
| Queue Collection | Architect Intent | Official Schedule | Queue Timetable |
| Address Collection | Architect Intent | Official Outages | Address Information |

## 2.4 Roles

Logical responsibilities performed within the system.

| Role | Source | Responsibility |
|------|--------|----------------|
| Publisher | GLOSSARY | Preparing and distributing Publications |
| Interpreter | GLOSSARY | Transforming structured information into understandable information |
| Parser | GLOSSARY | Retrieving Open Data |

## 2.5 Data Sources

Official organizations publishing Open Data.

| Data Source | Source | Domain |
|-------------|--------|--------|
| Distribution System Operator (DSO) | GLOSSARY | Queue Schedule, Planned Outages, Emergency Outages |

## 2.6 Representations

How information is presented to residents.

| Representation | Source | Domain |
|----------------|--------|--------|
| Timeline | Architect Intent | Queue Schedule |
| Tomorrow Graph | Architect Intent | Queue Schedule |
| Address Information | Architect Intent | Planned/Emergency Outages |
| Publication | GLOSSARY | Journal |

## 2.7 Identity Dimensions

Dimensions that identify entities.

| Dimension | Source | Type |
|-----------|--------|------|
| Queue Number | Architect Intent | Spatial (queue hierarchy) |
| Subqueue Number | Architect Intent | Spatial (queue hierarchy) |
| Address | TERRITORIAL | Spatial (geographic) |
| Territory | GLOSSARY | Spatial (publication unit) |
| Reporting Period | GLOSSARY | Temporal |
| Time Interval | GLOSSARY | Temporal |

## 2.8 Channels

Communication media through which information is delivered.

| Channel | Source | Status |
|---------|--------|--------|
| Telegram | GLOSSARY, Architect Intent | Active |
| Facebook | Architect Intent | Planned |
| PWA | ARCHITECTURE, Architect Intent | Active |

## 2.9 Adapters

Channel-specific implementations.

| Adapter | Source | Channel |
|---------|--------|---------|
| Telegram Adapter | Architect Intent | Telegram |
| Facebook Adapter | Architect Intent | Facebook |

---

# 3. Ontological Relationships

## 3.1 Domain A — Queue Schedule

```
DSO (Data Source)
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
```

## 3.2 Domain B — Planned Outages

```
DSO (Data Source)
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

## 3.3 Domain C — Emergency Outages

```
DSO (Data Source)
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

## 3.4 Journal

```
Journal (ongoing)
    ↓ instantiated as
Journal Edition (one per day)
    ↓ contains
Publication (per Territory)
    ↓ delivered via
Channel (Telegram/Facebook)
```

## 3.5 Publishing Subsystem

```
Publishing Subsystem
    ↓ uses
Telegram Adapter
    ↓ or
Facebook Adapter
    ↓ delivers to
Channel
```

---

# 4. Domain Independence

## 4.1 Domain A Independence

Queue Schedule is:
- NOT address-based
- Based on official Oblenergo schedule
- 6 queues, 12 subqueues
- Changes by hour
- Primary domain for PWA
- Primary domain for Push Notifications

## 4.2 Domain B Independence

Planned Outages is:
- Address-based
- Official planned maintenance
- Contains settlements, streets, houses
- Independent from Queue Schedule
- Independent from Emergency Outages

## 4.3 Domain C Independence

Emergency Outages is:
- Address-based
- Unexpected outages
- Contains settlements, streets, houses
- Independent from Queue Schedule
- Independent from Planned Outages

---

# 5. Findings

## 5.1 Finding ONT-001

**SvitloSk operates with THREE independent information domains.**

Queue Schedule, Planned Outages, and Emergency Outages are different ontological objects.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.2 Finding ONT-002

**There are TWO independent parsers.**

Parser A collects Queue Schedule.

Parser B collects Planned and Emergency Outages.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.3 Finding ONT-003

**The PWA application is primarily built around Queue Schedule.**

It displays Queue Schedules, Timelines, Tomorrow Graphs, and Address Lookups.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.4 Finding ONT-004

**Push Notifications belong ONLY to Queue Schedule.**

They notify about electricity loss/restoration for the selected subqueue.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.5 Finding ONT-005

**The Publishing Subsystem has PEER adapters.**

Telegram and Facebook are equal adapters, neither is primary.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| ONT-001 | Architect Intent |
| ONT-002 | Architect Intent |
| ONT-003 | Architect Intent |
| ONT-004 | Architect Intent |
| ONT-005 | Architect Intent |

---

**End of Complete Ontology**
