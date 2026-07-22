# INF001_HEARING

**Document ID:** CASE-INF-001

**Title:** Information Ontology Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-INF-001: reconstruction of the Information Model of SvitloSk.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The INFORMATION MODEL of SvitloSk — what information actually exists inside the system.

NOT software objects.

NOT architecture.

ONLY information.

## 2.2 What This Case Does NOT Investigate

- Software objects
- Architecture
- Implementation
- Telegram
- Facebook
- PWA
- Publishing channels

## 2.3 Investigation Constraint

This investigation is about INFORMATION.

Think like an ontologist, not like a software architect.

The objective is to discover the informational universe from which every future publication, adapter, parser and interface will naturally emerge.

---

# 3. Primary Sources

## 3.1 Repository Documentation

| Document | Relevance |
|----------|-----------|
| CHARTER.md | Project mission, information service definition |
| GLOSSARY.md | Canonical terminology, information model |
| DATA_MODEL.md | Logical data entities |
| TERRITORIAL_MODEL.md | Territorial structure |

## 3.2 Architect Intent

### Mission

SvitloSk is an information service.

It exists to provide residents of the Starokostiantyniv Territorial Community with understandable information about the state of electricity supply.

The project is NOT centered around Telegram.

The project is NOT centered around Facebook.

The project is NOT centered around the PWA.

Those are only representations.

### Three Independent Information Domains

#### Domain A — Queue Schedule

- official queue schedule
- 6 queues
- 12 subqueues
- hourly
- not address based

#### Domain B — Planned Outages

- address based
- settlements
- streets
- houses
- planned maintenance

#### Domain C — Emergency Outages

- address based
- emergency events
- independent from queue schedule

### PWA

The PWA visualizes primarily Domain A.

It additionally provides:
- address lookup
- push notification configuration
- archive
- personal cabinet

### Journal

The Public Information Journal contains information from Domains A, B and C.

One daily edition may include:
- planned outages (today)
- emergency outages (today)
- planned outages (tomorrow)
- emergency outages (tomorrow)
- tomorrow queue graph
- technical messages
- future project announcements

### Publication

Telegram and Facebook DO NOT own information.

They receive prepared representations.

Publishing is channel-independent.

---

# 4. Conceptual Separation

This investigation MUST separate:

1. **Information** — what exists
2. **Knowledge** — what is understood
3. **Data** — how it is represented
4. **Representation** — how it is presented

These four concepts MUST NOT be mixed.

---

# 5. Research Tasks

## PART 1 — Information Objects

Identify every INFORMATION OBJECT that exists inside SvitloSk.

Do NOT identify software objects. Only information objects.

## PART 2 — Information/Knowledge/Data/Representation

Separate these four concepts. Determine which is which.

## PART 3 — Information Lifecycle

Determine the lifecycle of INFORMATION.

Not Publication. Not Journal. Information itself.

## PART 4 — Information Persistence

Determine which information is:
- transient
- temporary
- persistent
- historical
- canonical

## PART 5 — Identity Dimensions

Determine identity dimensions of information.

## PART 6 — Information Relationships

Determine relationships between information objects.

## PART 7 — Competing Models

Construct at least FIVE competing information models.

## PART 8 — Hidden Assumptions

Identify hidden assumptions.

## PART 9 — Contradictions

Identify contradictions between repository, previous investigations, and architect intent.

## PART 10 — Information Dependency Graph

Construct complete Information Dependency Graph.

## PART 11 — Candidate Glossary

Produce Candidate Glossary.

## PART 12 — Open Questions

Produce Open Questions.

## PART 13 — Certificate

Produce Investigation Certificate.

---

# 6. Deliverables

| Document | Purpose |
|----------|---------|
| INF001_HEARING.md | Case scope and research questions |
| INF001_PART1_OBJECTS.md | Information objects |
| INF001_PART2_SEPARATION.md | Information/Knowledge/Data/Representation |
| INF001_PART3_LIFECYCLE.md | Information lifecycle |
| INF001_PART4_PERSISTENCE.md | Information persistence |
| INF001_PART5_IDENTITY.md | Identity dimensions |
| INF001_PART6_RELATIONSHIPS.md | Information relationships |
| INF001_PART7_MODELS.md | Competing models |
| INF001_PART8_ASSUMPTIONS.md | Hidden assumptions |
| INF001_PART9_CONTRADICTIONS.md | Contradictions |
| INF001_PART10_DEPENDENCY.md | Information dependency graph |
| INF001_PART11_GLOSSARY.md | Candidate glossary |
| INF001_PART12_QUESTIONS.md | Open questions |
| INF001_PART13_CERTIFICATE.md | Investigation certificate |

---

# 7. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
