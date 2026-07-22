# INF001_PART6_RELATIONSHIPS

**Document ID:** CASE-INF-001-P6

**Title:** Information Relationships

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines the relationships between information objects.

---

# 2. Information Relationships

## 2.1 Domain A — Queue Schedule

```
Official Queue Schedule (DSO)
    ↓ source of
Queue Schedule Information
    ↓ contains
Queue Information (1-6)
    ↓ contains
Subqueue Information (1.1-6.2)
    ↓ contains
Schedule Information (hourly)
    ↓ aggregated into
Queue Timetable Information
    ↓ displayed as
Timeline Information
    ↓ or
Tomorrow Queue Graph Information
```

---

## 2.2 Domain B — Planned Outages

```
Official Planned Outages (DSO)
    ↓ source of
Planned Outage Information
    ↓ references
Address Information (Settlement + Street + House)
    ↓ with
Planned Time Interval
```

---

## 2.3 Domain C — Emergency Outages

```
Official Emergency Outages (DSO)
    ↓ source of
Emergency Outage Information
    ↓ references
Address Information (Settlement + Street + House)
    ↓ with
Emergency Event Information
```

---

## 2.4 Journal

```
Journal Information (ongoing)
    ↓ instantiated as
Journal Edition Information (daily)
    ↓ contains
Publication Information (per Territory)
    ↓ organized by
Territory Information
    ↓ contains
    ├── Planned Outage Information (today)
    ├── Emergency Outage Information (today)
    ├── Planned Outage Information (tomorrow)
    ├── Emergency Outage Information (tomorrow)
    ├── Tomorrow Queue Graph Information
    ├── Technical Message Information
    └── Future Project Announcement Information
```

---

## 2.5 Cross-Domain Relationships

```
Queue Schedule Information (Domain A)
    ↓ may be referenced by
Journal Edition Information
    ↓ as
Tomorrow Queue Graph Information

Planned Outage Information (Domain B)
    ↓ contained in
Journal Edition Information

Emergency Outage Information (Domain C)
    ↓ contained in
Journal Edition Information
```

---

## 2.6 Address Lookup Relationship

```
Address Information (Territorial)
    ↓ maps to
Subqueue Information (Domain A)
```

This is the BRIDGE between address-based domains (B, C) and queue-based domain (A).

---

# 3. Relationship Types

## 3.1 Source Relationship

**Definition:** Information originates from a source.

**Example:** Queue Schedule Information ← Official Queue Schedule (DSO)

**Direction:** Source → Information

---

## 3.2 Contains Relationship

**Definition:** One information object contains another.

**Example:** Queue Information contains Subqueue Information

**Direction:** Container → Content

---

## 3.3 References Relationship

**Definition:** One information object references another.

**Example:** Planned Outage Information references Address Information

**Direction:** Reference → Referent

---

## 3.4 Aggregates Relationship

**Definition:** Multiple information objects are aggregated into one.

**Example:** Multiple Schedule Information objects aggregate into Queue Timetable Information

**Direction:** Parts → Aggregate

---

## 3.5 Organizes Relationship

**Definition:** One information object organizes another.

**Example:** Territory Information organizes Publication Information

**Direction:** Organizer → Organized

---

## 3.6 Contains (Journal) Relationship

**Definition:** Journal Edition Information contains various information types.

**Example:** Journal Edition Information contains Planned Outage Information, Emergency Outage Information, etc.

**Direction:** Journal Edition → Content Types

---

# 4. Relationship Matrix

| From | To | Type | Evidence |
|------|----|------|----------|
| Official Queue Schedule | Queue Schedule Information | Source | GLOSSARY §2 |
| Queue Schedule Information | Queue Information | Contains | Architect Intent |
| Queue Information | Subqueue Information | Contains | GLOSSARY §5 |
| Subqueue Information | Schedule Information | Contains | GLOSSARY §5 |
| Schedule Information | Queue Timetable Information | Aggregates | Architect Intent |
| Queue Timetable Information | Timeline Information | Displays as | Architect Intent |
| Queue Timetable Information | Tomorrow Queue Graph Information | Displays as | Architect Intent |
| Official Planned Outages | Planned Outage Information | Source | GLOSSARY §2 |
| Planned Outage Information | Address Information | References | GLOSSARY §5 |
| Official Emergency Outages | Emergency Outage Information | Source | GLOSSARY §2 |
| Emergency Outage Information | Address Information | References | GLOSSARY §5 |
| Journal Information | Journal Edition Information | Instantiates as | CHARTER §10 |
| Journal Edition Information | Publication Information | Contains | GLOSSARY §3 |
| Publication Information | Territory Information | Organized by | GLOSSARY §4 |
| Address Information | Subqueue Information | Maps to | Architect Intent (Address Lookup) |

---

# 5. Findings

## 5.1 Finding REL-001

**There are SIX relationship types.**

Source, Contains, References, Aggregates, Organizes, Contains (Journal).

**Evidence:** Analysis of information relationships.

**Confidence:** HIGH.

## 5.2 Finding REL-002

**The primary relationship chain for Domain A is:**

Source → Queue Schedule → Queue → Subqueue → Schedule → Timetable → Timeline/Graph

**Evidence:** GLOSSARY §5, Architect Intent.

**Confidence:** HIGH.

## 5.3 Finding REL-003

**The primary relationship chain for Domains B/C is:**

Source → Outage → Address

**Evidence:** GLOSSARY §5.

**Confidence:** HIGH.

## 5.4 Finding REL-004

**The Journal aggregates information from all three domains.**

Journal Edition contains Planned Outages, Emergency Outages, and Tomorrow Queue Graph.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.5 Finding REL-005

**Address Lookup bridges address-based and queue-based domains.**

It maps Address Information to Subqueue Information.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| REL-001 | Analysis of information relationships |
| REL-002 | GLOSSARY §5, Architect Intent |
| REL-003 | GLOSSARY §5 |
| REL-004 | Architect Intent |
| REL-005 | Architect Intent |

---

**End of Information Relationships**
