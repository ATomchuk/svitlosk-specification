# INF001_PART1_OBJECTS

**Document ID:** CASE-INF-001-P1

**Title:** Information Objects

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every INFORMATION OBJECT that exists inside SvitloSk.

NOT software objects. ONLY information objects.

---

# 2. Information Objects

## 2.1 Domain A — Queue Schedule Information

### Queue Schedule Information

**What it is:** The official schedule of electricity distribution queues published by the DSO.

**Characteristics:**
- 6 queues
- 12 subqueues
- hourly granularity
- NOT address-based

**Source:** Official Oblenergo schedule

**Persistence:** Changes hourly. Historical records preserved.

---

### Queue Information

**What it is:** Information about one specific queue (Queue 1, Queue 2, ... Queue 6).

**Characteristics:**
- Queue number (1-6)
- Contains subqueues
- Part of the queue schedule

**Persistence:** Persistent within reporting period.

---

### Subqueue Information

**What it is:** Information about one specific subqueue (Subqueue 1.1, Subqueue 1.2, ... Subqueue 6.2).

**Characteristics:**
- Queue number + Subqueue number
- Contains schedules
- Part of the queue

**Persistence:** Persistent within reporting period.

---

### Schedule Information

**What it is:** Information about electricity availability for one subqueue during one time interval.

**Characteristics:**
- Subqueue reference
- Time interval
- Availability status (available/unavailable)

**Persistence:** Changes hourly. Historical records preserved.

---

### Queue Timetable Information

**What it is:** The complete collection of schedule information for all queues and subqueues.

**Characteristics:**
- Contains all queue information
- Contains all subqueue information
- Contains all schedule information

**Persistence:** Changes hourly. Historical records preserved.

---

### Tomorrow Queue Graph Information

**What it is:** Information about the planned queue schedule for tomorrow.

**Characteristics:**
- All 12 subqueues
- Tomorrow's date
- Planned availability

**Persistence:** Temporary. Disappears after current day ends.

---

## 2.2 Domain B — Planned Outage Information

### Planned Outage Information

**What it is:** Information about officially announced scheduled interruptions of electricity supply.

**Characteristics:**
- Address-based
- Settlement
- Street
- House
- Planned time interval
- Official source

**Persistence:** Temporary (today's outages). Tomorrow's outages disappear after current day ends.

---

### Address Information (Planned)

**What it is:** Information about a specific address affected by planned outages.

**Characteristics:**
- Settlement name
- Street name
- House number
- Planned outage schedule

**Persistence:** Tied to planned outage information.

---

## 2.3 Domain C — Emergency Outage Information

### Emergency Outage Information

**What it is:** Information about unplanned interruptions of electricity supply.

**Characteristics:**
- Address-based
- Settlement
- Street
- House
- Emergency event
- Official source

**Persistence:** Persistent (historical record).

---

### Address Information (Emergency)

**What it is:** Information about a specific address affected by emergency outages.

**Characteristics:**
- Settlement name
- Street name
- House number
- Emergency information

**Persistence:** Tied to emergency outage information.

---

## 2.4 Territorial Information

### Community Information

**What it is:** Information about the Starokostiantyniv Territorial Community.

**Characteristics:**
- Community name
- Administrative centre
- Starosta districts

**Persistence:** Persistent (reference data).

---

### Territory Information

**What it is:** Information about a publication unit (Administrative Centre or Starosta District).

**Characteristics:**
- Territory name
- Type (Administrative Centre or Starosta District)
- Contained settlements

**Persistence:** Persistent (reference data).

---

### Settlement Information

**What it is:** Information about a populated place.

**Characteristics:**
- Settlement name
- Parent territory
- Streets

**Persistence:** Persistent (reference data).

---

### Address Information (Territorial)

**What it is:** Information about a specific geographical location.

**Characteristics:**
- Settlement
- Street
- House number

**Persistence:** Persistent (reference data).

---

## 2.5 Journal Information

### Journal Information

**What it is:** The ongoing stream of information published by SvitloSk.

**Characteristics:**
- Contains information from all three domains
- Published daily
- Organized by territory

**Persistence:** Continuous. Historical records preserved.

---

### Journal Edition Information

**What it is:** Information about one daily edition of the Journal.

**Characteristics:**
- Date
- Contains planned outage information
- Contains emergency outage information
- Contains queue graph information
- Contains technical messages
- Organized by territory

**Persistence:** Persistent (historical record).

---

### Publication Information

**What it is:** One piece of information prepared for distribution.

**Characteristics:**
- Territory reference
- Content
- Source domain (A, B, or C)
- Timestamp

**Persistence:** Persistent (historical record).

---

## 2.6 System Information

### Technical Message Information

**What it is:** Information about system status and technical announcements.

**Characteristics:**
- Message content
- Timestamp
- Category

**Persistence:** Persistent (historical record).

---

### Future Project Announcement Information

**What it is:** Information about future project developments.

**Characteristics:**
- Announcement content
- Timestamp
- Category

**Persistence:** Temporary (until replaced or archived).

---

# 3. Information Object Inventory

## 3.1 Domain A Objects

| Object | Atomic? | Persistence |
|--------|---------|-------------|
| Queue Schedule Information | NO (composite) | Changes hourly |
| Queue Information | YES | Persistent within period |
| Subqueue Information | YES | Persistent within period |
| Schedule Information | YES | Changes hourly |
| Queue Timetable Information | NO (composite) | Changes hourly |
| Tomorrow Queue Graph Information | NO (composite) | Temporary |

## 3.2 Domain B Objects

| Object | Atomic? | Persistence |
|--------|---------|-------------|
| Planned Outage Information | YES | Temporary |
| Address Information (Planned) | NO (composite) | Tied to outage |

## 3.3 Domain C Objects

| Object | Atomic? | Persistence |
|--------|---------|-------------|
| Emergency Outage Information | YES | Persistent |
| Address Information (Emergency) | NO (composite) | Tied to outage |

## 3.4 Territorial Objects

| Object | Atomic? | Persistence |
|--------|---------|-------------|
| Community Information | NO (composite) | Persistent |
| Territory Information | YES | Persistent |
| Settlement Information | YES | Persistent |
| Address Information (Territorial) | YES | Persistent |

## 3.5 Journal Objects

| Object | Atomic? | Persistence |
|--------|---------|-------------|
| Journal Information | NO (continuous) | Continuous |
| Journal Edition Information | NO (composite) | Persistent |
| Publication Information | YES | Persistent |

## 3.6 System Objects

| Object | Atomic? | Persistence |
|--------|---------|-------------|
| Technical Message Information | YES | Persistent |
| Future Project Announcement Information | YES | Temporary |

---

# 4. Findings

## 4.1 Finding OBJ-001

**There are 20 distinct information objects in SvitloSk.**

Across 6 categories: Domain A, Domain B, Domain C, Territorial, Journal, System.

**Evidence:** Analysis of CHARTER, GLOSSARY, Architect Intent.

**Confidence:** HIGH.

## 4.2 Finding OBJ-002

**7 information objects are atomic.**

Queue, Subqueue, Schedule, Planned Outage, Emergency Outage, Territory, Settlement, Address, Publication, Technical Message, Future Announcement.

**Evidence:** Analysis of information characteristics.

**Confidence:** HIGH.

## 4.3 Finding OBJ-003

**13 information objects are composite.**

Queue Schedule, Queue Timetable, Tomorrow Graph, Address Information, Community, Journal, Journal Edition, etc.

**Evidence:** Analysis of information characteristics.

**Confidence:** HIGH.

## 4.4 Finding OBJ-004

**Information persistence varies significantly.**

Some information changes hourly (Schedule).

Some is temporary (Tomorrow Graph, Planned Outages).

Some is persistent (Emergency Outages, Territory).

Some is continuous (Journal).

**Evidence:** Analysis of information lifecycle.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OBJ-001 | CHARTER, GLOSSARY, Architect Intent |
| OBJ-002 | Analysis of information characteristics |
| OBJ-003 | Analysis of information characteristics |
| OBJ-004 | Analysis of information lifecycle |

---

**End of Information Objects**
