# SVTONTO001_PART2_ATOMIC

**Document ID:** CASE-SVT-ONTOLOGY-001-P2

**Title:** Atomic vs Composite Objects

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines which concepts are truly atomic and which are composite.

---

# 2. Atomic Objects

## 2.1 Definition

An atomic object is the smallest indivisible unit that:
- Cannot be decomposed into smaller meaningful units
- Has independent identity
- Can exist on its own

## 2.2 Atomic Candidates

### Queue

**Atomic?** YES

**Evidence:**
- Queue is a discrete entity (Queue 1, Queue 2, ...)
- Cannot be decomposed into smaller units
- Has independent identity (Queue Number)

**Source:** GLOSSARY, Architect Intent

### Subqueue

**Atomic?** YES

**Evidence:**
- Subqueue is a discrete entity (Subqueue 1.1, Subqueue 1.2, ...)
- Cannot be decomposed into smaller units
- Has independent identity (Queue Number + Subqueue Number)

**Source:** GLOSSARY, Architect Intent

### Schedule

**Atomic?** YES

**Evidence:**
- Schedule is a discrete time slot
- Cannot be decomposed into smaller units
- Has independent identity (Subqueue + Time)

**Source:** GLOSSARY, Architect Intent

### Planned Outage

**Atomic?** YES

**Evidence:**
- Planned Outage is a discrete event
- Cannot be decomposed into smaller units
- Has independent identity (Address + Time)

**Source:** GLOSSARY, Architect Intent

### Emergency Outage

**Atomic?** YES

**Evidence:**
- Emergency Outage is a discrete event
- Cannot be decomposed into smaller units
- Has independent identity (Address + Time)

**Source:** GLOSSARY, Architect Intent

### Address

**Atomic?** YES

**Evidence:**
- Address is a discrete location
- Cannot be decomposed into smaller units
- Has independent identity (Settlement + Street + House)

**Source:** GLOSSARY, TERRITORIAL

### Publication

**Atomic?** YES

**Evidence:**
- Publication is a discrete message
- Cannot be decomposed into smaller meaningful units
- Has independent identity (Territory + Content + Time)

**Source:** GLOSSARY

---

# 3. Composite Objects

## 3.1 Definition

A composite object is an entity that:
- Can be decomposed into smaller units
- Has identity derived from its parts
- Does not have independent existence without its parts

## 3.2 Composite Candidates

### Queue Timetable

**Composite?** YES

**Decomposition:**
- Queue Timetable = Queue + Subqueue + Schedule (multiple)

**Evidence:**
- A timetable contains multiple schedules for one queue
- Cannot exist without its schedules
- Identity derived from queue and time

**Source:** Architect Intent

### Address Information

**Composite?** YES

**Decomposition:**
- Address Information = Settlement + Street + House + Outage Type + Time

**Evidence:**
- Address information contains multiple address components
- Cannot exist without its address components
- Identity derived from address and outage type

**Source:** Architect Intent

### Timeline

**Composite?** YES

**Decomposition:**
- Timeline = Schedule (multiple) + Time Range

**Evidence:**
- Timeline displays multiple schedules over time
- Cannot exist without its schedules
- Identity derived from subqueue and time range

**Source:** Architect Intent

### Tomorrow Graph

**Composite?** YES

**Decomposition:**
- Tomorrow Graph = Schedule (12 subqueues) + Tomorrow Date

**Evidence:**
- Tomorrow graph displays schedules for all subqueues
- Cannot exist without its schedules
- Identity derived from date

**Source:** Architect Intent

### Journal Edition

**Composite?** YES

**Decomposition:**
- Journal Edition = Publication (multiple) + Territory (multiple) + Date

**Evidence:**
- Journal edition contains multiple publications
- Cannot exist without its publications
- Identity derived from date and territory

**Source:** Architect Intent

### Publication Package

**Composite?** YES

**Decomposition:**
- Publication Package = Publication (multiple) + Reporting Period

**Evidence:**
- Publication package contains multiple publications
- Cannot exist without its publications
- Identity derived from reporting period

**Source:** GLOSSARY

### Personal Cabinet

**Composite?** YES

**Decomposition:**
- Personal Cabinet = Location (2) + Push Notifications + Silence Mode + ...

**Evidence:**
- Personal cabinet contains multiple configuration items
- Cannot exist without its configuration items
- Identity derived from user

**Source:** Architect Intent

---

# 4. Atomic vs Composite Matrix

| Concept | Atomic? | Decomposition | Source |
|---------|---------|---------------|--------|
| Queue | YES | — | GLOSSARY, Architect Intent |
| Subqueue | YES | — | GLOSSARY, Architect Intent |
| Schedule | YES | — | GLOSSARY, Architect Intent |
| Planned Outage | YES | — | GLOSSARY, Architect Intent |
| Emergency Outage | YES | — | GLOSSARY, Architect Intent |
| Address | YES | — | GLOSSARY, TERRITORIAL |
| Publication | YES | — | GLOSSARY |
| Queue Timetable | NO | Queue + Subqueue + Schedule | Architect Intent |
| Address Information | NO | Settlement + Street + House + Outage | Architect Intent |
| Timeline | NO | Schedule + Time Range | Architect Intent |
| Tomorrow Graph | NO | Schedule (12) + Date | Architect Intent |
| Journal Edition | NO | Publication + Territory + Date | Architect Intent |
| Publication Package | NO | Publication + Reporting Period | GLOSSARY |
| Personal Cabinet | NO | Location + Notifications + ... | Architect Intent |

---

# 5. Findings

## 5.1 Finding ATOMIC-001

**Seven concepts are truly atomic.**

Queue, Subqueue, Schedule, Planned Outage, Emergency Outage, Address, Publication.

**Evidence:** Analysis of GLOSSARY, TERRITORIAL, Architect Intent.

**Confidence:** HIGH.

## 5.2 Finding ATOMIC-002

**Seven concepts are composite.**

Queue Timetable, Address Information, Timeline, Tomorrow Graph, Journal Edition, Publication Package, Personal Cabinet.

**Evidence:** Analysis of GLOSSARY, Architect Intent.

**Confidence:** HIGH.

## 5.3 Finding ATOMIC-003

**Publication is the atomic unit of the Journal.**

It cannot be decomposed into smaller meaningful units within the Journal context.

**Evidence:** GLOSSARY.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| ATOMIC-001 | GLOSSARY, TERRITORIAL, Architect Intent |
| ATOMIC-002 | GLOSSARY, Architect Intent |
| ATOMIC-003 | GLOSSARY |

---

**End of Atomic vs Composite**
