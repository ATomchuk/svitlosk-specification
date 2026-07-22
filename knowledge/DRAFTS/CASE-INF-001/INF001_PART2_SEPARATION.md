# INF001_PART2_SEPARATION

**Document ID:** CASE-INF-001-P2

**Title:** Information/Knowledge/Data/Representation Separation

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document separates four fundamental concepts that MUST NOT be mixed:

1. Information
2. Knowledge
3. Data
4. Representation

---

# 2. Concept Definitions

## 2.1 Information

### Definition

Information is WHAT EXISTS about the state of electricity supply.

It is the factual content that SvitloSk manages.

### Characteristics

- Factual
- Objective
- Derived from official sources
- NOT created by SvitloSk
- Only interpreted, not modified

### Examples

- "Queue 1, Subqueue 1.1 has no electricity from 8:00 to 12:00"
- "Planned outage on вул. Центральна 18 from 10:00 to 14:00"
- "Emergency outage on вул. Острозького 15"

---

## 2.2 Knowledge

### Definition

Knowledge is what is UNDERSTOOD about the information.

It is the interpretation and understanding that SvitloSk provides.

### Characteristics

- Interpretive
- Contextual
- Derived from information
- Created by SvitloSk through interpretation
- Improves understanding without changing facts

### Examples

- "Residents of Subqueue 1.1 will have no electricity this morning"
- "The planned maintenance on Центральна will affect 50 houses"
- "The emergency outage is spreading to adjacent streets"

---

## 2.3 Data

### Definition

Data is how information is REPRESENTED internally.

It is the structured format used by the system.

### Characteristics

- Structured
- Machine-readable
- Derived from information
- Created by parsers
- Preserves semantic equivalence with source

### Examples

- Queue timetable in JSON format
- Address database with coordinates
- Schedule records in database tables

---

## 2.4 Representation

### Definition

Representation is how information is PRESENTED to residents.

It is the visual or textual format used for delivery.

### Characteristics

- Visual or textual
- Human-readable
- Derived from information or knowledge
- Created by rendering processes
- Channel-specific (Telegram, Facebook, PWA)

### Examples

- Telegram message with outage information
- Facebook post with schedule
- PWA timeline visualization
- Push notification about electricity loss

---

# 3. Separation Matrix

## 3.1 Domain A — Queue Schedule

| Concept | What It Is | Example |
|---------|------------|---------|
| Information | The official queue schedule | Queue 1, Subqueue 1.1: no electricity 8:00-12:00 |
| Knowledge | Understanding of the schedule | Residents will have electricity at 12:00 |
| Data | Internal representation | JSON record with queue, subqueue, time, status |
| Representation | Visual presentation | Timeline graph showing availability |

## 3.2 Domain B — Planned Outages

| Concept | What It Is | Example |
|---------|------------|---------|
| Information | The official planned outage | Planned outage on Центральна 18, 10:00-14:00 |
| Knowledge | Understanding of the outage | 50 houses will be affected tomorrow morning |
| Data | Internal representation | JSON record with address, time, duration |
| Representation | Visual presentation | Telegram message listing affected addresses |

## 3.3 Domain C — Emergency Outages

| Concept | What It Is | Example |
|---------|------------|---------|
| Information | The official emergency outage | Emergency outage on Острозького 15 |
| Knowledge | Understanding of the outage | Power is out unexpectedly in that area |
| Data | Internal representation | JSON record with address, timestamp, status |
| Representation | Visual presentation | Push notification about electricity loss |

---

# 4. Separation Rules

## 4.1 Information ≠ Knowledge

Information is WHAT EXISTS.

Knowledge is WHAT IS UNDERSTOOD.

SvitloSk creates knowledge from information, but does NOT modify information.

## 4.2 Information ≠ Data

Information is the FACTUAL CONTENT.

Data is the STRUCTURED REPRESENTATION.

SvitloSk stores data, but the information it represents comes from official sources.

## 4.3 Information ≠ Representation

Information is the FACTUAL CONTENT.

Representation is the VISUAL OR TEXTUAL FORMAT.

SvitloSk delivers representations, but the information they contain comes from official sources.

## 4.4 Knowledge ≠ Data

Knowledge is the UNDERSTANDING.

Data is the STRUCTURE.

Knowledge is derived from data, but they are different concepts.

## 4.5 Knowledge ≠ Representation

Knowledge is the UNDERSTANDING.

Representation is the FORMAT.

Knowledge is delivered through representations, but they are different concepts.

## 4.6 Data ≠ Representation

Data is the INTERNAL STRUCTURE.

Representation is the EXTERNAL FORMAT.

Data is transformed into representations, but they are different concepts.

---

# 5. Channel Independence

## 5.1 Information is Channel-Independent

Information exists independently of any channel.

It comes from official sources and is not owned by any channel.

## 5.2 Knowledge is Channel-Independent

Knowledge is derived from information and is not owned by any channel.

## 5.3 Data is Channel-Independent

Data is the internal representation and is not owned by any channel.

## 5.4 Representation is Channel-Specific

Representation is how information is presented to residents.

Different channels may have different representations of the same information.

---

# 6. Findings

## 6.1 Finding SEP-001

**Information, Knowledge, Data, and Representation are FOUR DISTINCT CONCEPTS.**

They MUST NOT be mixed.

**Evidence:** Analysis of information characteristics.

**Confidence:** HIGH.

## 6.2 Finding SEP-002

**Information is WHAT EXISTS about electricity supply.**

It comes from official sources and is not created by SvitloSk.

**Evidence:** CHARTER.md §7, §8.

**Confidence:** HIGH.

## 6.3 Finding SEP-003

**Knowledge is WHAT IS UNDERSTOOD about the information.**

It is created by SvitloSk through interpretation.

**Evidence:** CHARTER.md §1, §2.

**Confidence:** HIGH.

## 6.4 Finding SEP-004

**Data is HOW INFORMATION IS REPRESENTED internally.**

It is the structured format used by the system.

**Evidence:** GLOSSARY.md §2 (Data Model).

**Confidence:** HIGH.

## 6.5 Finding SEP-005

**Representation is HOW INFORMATION IS PRESENTED to residents.**

It is channel-specific (Telegram, Facebook, PWA).

**Evidence:** Architect Intent ("Telegram and Facebook DO NOT own information").

**Confidence:** HIGH.

---

# 7. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| SEP-001 | Analysis of information characteristics |
| SEP-002 | CHARTER.md §7, §8 |
| SEP-003 | CHARTER.md §1, §2 |
| SEP-004 | GLOSSARY.md §2 |
| SEP-005 | Architect Intent |

---

**End of Information/Knowledge/Data/Representation Separation**
