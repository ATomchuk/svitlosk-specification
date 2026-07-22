# SYS001_OBJECTS

**Document ID:** CASE-SYS-001-OBJ

**Title:** System Objects

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies ALL system-level objects.

NOT publication objects. SYSTEM objects.

---

# 2. System Objects

## 2.1 Information Domain Objects

### Domain A — Queue Schedule

| Object | Type | Evidence |
|--------|------|----------|
| Official Queue Schedule | External | DSO publishes |
| Queue Schedule Information | Internal | Parser A produces |
| Queue Information | Internal | Part of Queue Schedule |
| Subqueue Information | Internal | Part of Queue |
| Schedule Information | Internal | Part of Subqueue |
| Queue Timetable | Internal | Aggregation of Schedules |
| Tomorrow Queue Graph | Internal | Temporary, expires |

### Domain B — Planned Outages

| Object | Type | Evidence |
|--------|------|----------|
| Official Planned Outages | External | DSO publishes |
| Planned Outage Information | Internal | Parser B produces |
| Address Information (Planned) | Internal | Part of Planned Outage |

### Domain C — Emergency Outages

| Object | Type | Evidence |
|--------|------|----------|
| Official Emergency Outages | External | DSO publishes |
| Emergency Outage Information | Internal | Parser B produces |
| Address Information (Emergency) | Internal | Part of Emergency Outage |

---

## 2.2 Territorial Objects

| Object | Type | Evidence |
|--------|------|----------|
| Community | Reference | TERRITORIAL_MODEL |
| Administrative Centre | Reference | TERRITORIAL_MODEL |
| Starosta District | Reference | TERRITORIAL_MODEL |
| Settlement | Reference | TERRITORIAL_MODEL |
| Street | Reference | TERRITORIAL_MODEL |
| Address | Reference | TERRITORIAL_MODEL |

---

## 2.3 Journal Objects

| Object | Type | Evidence |
|--------|------|----------|
| Journal | Ongoing Service | CHARTER §10 |
| Journal Edition | Composite | Daily instance |
| Publication | Atomic | GLOSSARY §3 |

---

## 2.4 Publishing Objects

| Object | Type | Evidence |
|--------|------|----------|
| Publishing Subsystem | Service | Architect Intent |
| Telegram Adapter | Component | Architect Intent |
| Facebook Adapter | Component | Architect Intent |
| Telegram Post | Representation | Channel-specific |
| Facebook Post | Representation | Channel-specific |

---

## 2.5 PWA Objects

| Object | Type | Evidence |
|--------|------|----------|
| PWA Application | Application | Architect Intent |
| Main Screen | Interface | Architect Intent |
| Archive Screen | Interface | Architect Intent |
| Address Lookup Screen | Interface | Architect Intent |
| Personal Cabinet Screen | Interface | Architect Intent |
| Timeline | Representation | Domain A |
| Tomorrow Graph | Representation | Domain A |
| Push Notification | Representation | Domain A only |

---

## 2.6 System Infrastructure Objects

| Object | Type | Evidence |
|--------|------|----------|
| Parser A | Component | Architect Intent |
| Parser B | Component | Architect Intent |
| Data Storage | Component | GLOSSARY §2 |
| Historical Archive | Component | GLOSSARY §2 |

---

# 3. Object Inventory

## 3.1 Total Count

| Category | Count |
|----------|-------|
| Information Domain | 9 |
| Territorial | 6 |
| Journal | 3 |
| Publishing | 5 |
| PWA | 8 |
| Infrastructure | 4 |
| **Total** | **35** |

## 3.2 Object Types

| Type | Count | Examples |
|------|-------|----------|
| External | 3 | Official Queue Schedule, Official Outages |
| Internal | 15 | Information objects, Data objects |
| Reference | 6 | Territorial objects |
| Service | 2 | Journal, Publishing Subsystem |
| Component | 6 | Parser A/B, Adapters, Storage |
| Application | 1 | PWA |
| Interface | 4 | PWA Screens |
| Representation | 5 | Posts, Timeline, Graph, Notification |

---

# 4. Findings

## 4.1 Finding OBJ-001

**There are 35 system-level objects.**

Across 6 categories.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 4.2 Finding OBJ-002

**There are 3 EXTERNAL objects.**

Official Queue Schedule, Official Planned Outages, Official Emergency Outages.

These are the ONLY objects that originate outside the system.

**Evidence:** Architect Intent, GLOSSARY §2.

**Confidence:** HIGH.

## 4.3 Finding OBJ-003

**There are 6 REFERENCE objects.**

All territorial objects are reference data that changes infrequently.

**Evidence:** TERRITORIAL_MODEL.

**Confidence:** HIGH.

## 4.4 Finding OBJ-004

**There are 5 REPRESENTATION objects.**

These are channel-specific renderings of information.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OBJ-001 | Analysis of all evidence sources |
| OBJ-002 | Architect Intent, GLOSSARY §2 |
| OBJ-003 | TERRITORIAL_MODEL |
| OBJ-004 | Architect Intent |

---

**End of System Objects**
