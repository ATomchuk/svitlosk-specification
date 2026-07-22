# SVTONTO001_PART5_ELECTRICITY

**Document ID:** CASE-SVT-ONTOLOGY-001-P5

**Title:** Electricity Ontology

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines the ontology of Queue, Subqueue, Schedule, Planned Outage, and Emergency Outage.

---

# 2. Concept Analysis

## 2.1 Queue

### Repository Evidence

> "Queue: An official electricity distribution queue published by the Distribution System Operator." (GLOSSARY.md §5)

### Architect Intent Evidence

> "consists of 6 queues"

> "Queue 1, Queue 2, ... Queue 6"

### Ontological Status

**Queue is an ATOMIC OBJECT.**

It is a discrete entity representing an official electricity distribution queue.

### Evidence

- GLOSSARY defines it as "an official electricity distribution queue"
- Architect Intent confirms 6 queues
- Cannot be decomposed into smaller units

---

## 2.2 Subqueue

### Repository Evidence

> "Subqueue: A subdivision of an official Queue." (GLOSSARY.md §5)

> "The current SvitloSk implementation supports twelve Subqueues." (GLOSSARY.md §5)

### Architect Intent Evidence

> "consists of 12 subqueues"

> "Subqueue 1.1, Subqueue 1.2, ... Subqueue 6.2"

### Ontological Status

**Subqueue is an ATOMIC OBJECT.**

It is a discrete entity representing a subdivision of a Queue.

### Evidence

- GLOSSARY defines it as "a subdivision of an official Queue"
- Architect Intent confirms 12 subqueues
- Cannot be decomposed into smaller units

---

## 2.3 Schedule

### Repository Evidence

> "Schedule: Logical representation of electricity availability for one operational period." (DATA_MODEL.md)

> "Schedules SHALL reference one Subqueue." (DATA_MODEL.md)

### Architect Intent Evidence

> "schedule changes by hour"

> "Timeline" displays schedules

### Ontological Status

**Schedule is an ATOMIC OBJECT.**

It is a discrete time slot representing electricity availability for one Subqueue.

### Evidence

- DATA_MODEL defines it as "logical representation of electricity availability"
- Architect Intent confirms hourly changes
- Cannot be decomposed into smaller units

---

## 2.4 Planned Outage

### Repository Evidence

> "Planned Power Outage: An officially announced scheduled interruption of electricity supply." (GLOSSARY.md §5)

> "Planned Power Outages originate exclusively from an approved Data Source." (GLOSSARY.md §5)

### Architect Intent Evidence

> "Planned Outages: Address-based. Official planned maintenance."

> "Contains: settlements, streets, houses, planned time intervals"

### Ontological Status

**Planned Outage is an ATOMIC OBJECT.**

It is a discrete event representing an officially announced scheduled interruption.

### Evidence

- GLOSSARY defines it as "an officially announced scheduled interruption"
- Architect Intent confirms address-based nature
- Cannot be decomposed into smaller units

---

## 2.5 Emergency Outage

### Repository Evidence

> "Emergency Power Outage: An unplanned interruption of electricity supply published by the official Data Source." (GLOSSARY.md §5)

> "Emergency Power Outages SHALL be treated as authoritative immediately after publication." (GLOSSARY.md §5)

### Architect Intent Evidence

> "Emergency Outages: Address-based. Unexpected outages."

> "Contains: settlements, streets, houses, emergency information"

### Ontological Status

**Emergency Outage is an ATOMIC OBJECT.**

It is a discrete event representing an unplanned interruption.

### Evidence

- GLOSSARY defines it as "an unplanned interruption"
- Architect Intent confirms address-based nature
- Cannot be decomposed into smaller units

---

# 3. Domain Relationships

## 3.1 Queue Schedule Domain

```
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

## 3.2 Planned Outage Domain

```
Planned Outage
    ↓ references
Address (Settlement + Street + House)
    ↓ with
Planned Time Interval
```

## 3.3 Emergency Outage Domain

```
Emergency Outage
    ↓ references
Address (Settlement + Street + House)
    ↓ with
Emergency Information
```

---

# 4. Domain Independence

## 4.1 Queue Schedule Independence

Queue Schedule is:
- NOT address-based
- Based on official Oblenergo schedule
- 6 queues, 12 subqueues
- Changes by hour
- Independent from Planned Outages
- Independent from Emergency Outages

## 4.2 Planned Outage Independence

Planned Outages is:
- Address-based
- Official planned maintenance
- Contains settlements, streets, houses
- Independent from Queue Schedule
- Independent from Emergency Outages

## 4.3 Emergency Outage Independence

Emergency Outages is:
- Address-based
- Unexpected outages
- Contains settlements, streets, houses
- Independent from Queue Schedule
- Independent from Planned Outages

---

# 5. Findings

## 5.1 Finding ELEC-001

**Queue, Subqueue, Schedule, Planned Outage, Emergency Outage are all ATOMIC OBJECTS.**

They cannot be decomposed into smaller meaningful units.

**Evidence:** GLOSSARY.md §5, DATA_MODEL.md, Architect Intent.

**Confidence:** HIGH.

## 5.2 Finding ELEC-002

**There are THREE independent electricity domains.**

Queue Schedule, Planned Outages, and Emergency Outages are different ontological objects.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.3 Finding ELEC-003

**Queue Schedule is NOT address-based.**

It is based on official Oblenergo schedule with 6 queues and 12 subqueues.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.4 Finding ELEC-004

**Planned Outages and Emergency Outages ARE address-based.**

They contain settlements, streets, houses, and time information.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| ELEC-001 | GLOSSARY.md §5, DATA_MODEL.md, Architect Intent |
| ELEC-002 | Architect Intent |
| ELEC-003 | Architect Intent |
| ELEC-004 | Architect Intent |

---

**End of Electricity Ontology**
