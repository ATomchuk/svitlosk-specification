# INF001_PART11_GLOSSARY

**Document ID:** CASE-INF-001-P11

**Title:** Candidate Glossary

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document produces a candidate glossary from the information ontology investigation.

This is NOT a canonical glossary. This is a RESEARCH ARTIFACT.

---

# 2. Candidate Glossary

## 2.1 Core Concepts

### Information

WHAT EXISTS about the state of electricity supply.

Factual content derived from official sources.

NOT created by SvitloSk. Only interpreted, not modified.

**Source:** CHARTER §1, §2, §7, §8

---

### Knowledge

WHAT IS UNDERSTOOD about the information.

Interpretation and understanding created by SvitloSk.

Improves understanding without changing facts.

**Source:** CHARTER §1, §2

---

### Data

HOW INFORMATION IS REPRESENTED internally.

Structured format used by the system.

Preserves semantic equivalence with source.

**Source:** GLOSSARY §2 (Data Model)

---

### Representation

HOW INFORMATION IS PRESENTED to residents.

Visual or textual format used for delivery.

Channel-specific (Telegram, Facebook, PWA).

**Source:** Architect Intent

---

## 2.2 Information Domains

### Domain A — Queue Schedule

Official emergency electricity limitation based on the official Oblenergo schedule.

Consists of 6 queues and 12 subqueues.

NOT address-based. Changes by hour.

**Source:** Architect Intent

---

### Domain B — Planned Outages

Address-based official planned maintenance.

Contains settlements, streets, houses, and planned time intervals.

Independent from Queue Schedule.

**Source:** Architect Intent

---

### Domain C — Emergency Outages

Address-based unexpected outages.

Contains settlements, streets, houses, and emergency information.

Independent from Queue Schedule and Planned Outages.

**Source:** Architect Intent

---

## 2.3 Information Objects

### Queue Schedule Information

The official schedule of electricity distribution queues published by the DSO.

Contains queue, subqueue, and schedule information.

**Source:** GLOSSARY §5, Architect Intent

---

### Queue Information

Information about one specific queue (Queue 1, Queue 2, ... Queue 6).

**Source:** GLOSSARY §5, Architect Intent

---

### Subqueue Information

Information about one specific subqueue (Subqueue 1.1, Subqueue 1.2, ... Subqueue 6.2).

**Source:** GLOSSARY §5, Architect Intent

---

### Schedule Information

Information about electricity availability for one subqueue during one time interval.

**Source:** GLOSSARY §5, Architect Intent

---

### Queue Timetable Information

The complete collection of schedule information for all queues and subqueues.

**Source:** Architect Intent

---

### Tomorrow Queue Graph Information

Information about the planned queue schedule for tomorrow.

Temporary. Expires after current day ends.

**Source:** Architect Intent

---

### Planned Outage Information

Information about officially announced scheduled interruptions of electricity supply.

Address-based. Temporary.

**Source:** GLOSSARY §5, Architect Intent

---

### Emergency Outage Information

Information about unplanned interruptions of electricity supply.

Address-based. Persistent.

**Source:** GLOSSARY §5

---

### Journal Information

The ongoing stream of information published by SvitloSk.

Contains information from all three domains.

**Source:** CHARTER §10

---

### Journal Edition Information

One daily instance of the Journal.

Contains multiple information types organized by Territory.

**Source:** Architect Intent

---

### Publication Information

One piece of information prepared for distribution.

Atomic object. Cannot be decomposed.

**Source:** GLOSSARY §3

---

## 2.4 Identity Dimensions

### Time

Temporal identity — WHEN information is valid or when it was created.

Includes: Reporting Period, Creation Timestamp, Validity Interval, Hour.

**Source:** GLOSSARY §2, Architect Intent

---

### Territory

Spatial identity — WHERE information applies.

Includes: Community, Administrative Centre, Starosta District, Settlement, Street, Address.

**Source:** TERRITORIAL_MODEL

---

### Queue

Queue identity — WHICH queue information applies to.

Includes: Queue Number (1-6), Subqueue Number (1.1-6.2).

**Source:** GLOSSARY §5, Architect Intent

---

### Source

Source identity — WHERE information came from.

Includes: Data Source, DSO, Processing Cycle.

**Source:** GLOSSARY §2

---

### Domain

Domain identity — WHICH information domain information belongs to.

Includes: Domain A, Domain B, Domain C.

**Source:** Architect Intent

---

### Validity

Validity identity — WHETHER information is currently valid.

Includes: Active, Expired, Temporary.

**Source:** Architect Intent

---

## 2.5 Persistence Types

### Transient

Information that exists only briefly and is not preserved.

**Source:** Analysis of information characteristics

---

### Temporary

Information that exists for a limited time and then expires.

**Source:** Architect Intent, GLOSSARY §3

---

### Persistent

Information that is preserved indefinitely.

**Source:** GLOSSARY §5, TERRITORIAL_MODEL

---

### Historical

Information that has been archived and is no longer active.

**Source:** GLOSSARY §5, CHARTER §10

---

### Canonical

Information that is the authoritative source of truth.

**Source:** CHARTER §8, TERRITORIAL_MODEL

---

# 3. Candidate Status

This glossary candidate is:

- A RESEARCH ARTIFACT
- NOT canonical
- NOT promoted
- Subject to Architect decision

---

# 4. Traceability

All terms traced to:
- GLOSSARY.md
- CHARTER.md
- DATA_MODEL.md
- TERRITORIAL_MODEL.md
- Architect Intent

---

**End of Candidate Glossary**
