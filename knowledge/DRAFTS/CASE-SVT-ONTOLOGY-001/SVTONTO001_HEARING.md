# SVTONTO001_HEARING

**Document ID:** CASE-SVT-ONTOLOGY-001

**Title:** SvitloSk Ontology Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-SVT-ONTOLOGY-001: complete ontology reconstruction of SvitloSk.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The complete ontology of SvitloSk — all objects, services, processes, roles, data sources, representations, identity dimensions, channels and adapters.

## 2.2 What This Case Does NOT Investigate

- Software implementation
- Infrastructure
- Existing specification validity
- Previous investigation findings (CASE-PUB-001, CASE-JRN-001)

## 2.3 Investigation Constraint

This investigation reconciles TWO PRIMARY SOURCES:
1. Existing repository documentation
2. The Architect Intent described in this hearing

Neither source has higher priority.

---

# 3. Primary Sources

## 3.1 Repository Documentation

| Document | Relevance |
|----------|-----------|
| CHARTER.md | Project mission, Journal definition |
| GLOSSARY.md | Canonical terminology |
| ARCHITECTURE.md | Current architectural model |
| DATA_MODEL.md | Logical data entities |
| TERRITORIAL_MODEL.md | Territorial structure |

## 3.2 Architect Intent

### Mission

SvitloSk is a local public information service for residents of the Starokostiantyniv Territorial Community.

Its mission is to provide understandable, timely and structured information about the current state of electricity supply inside the community.

The project is intentionally designed as a SOCIAL INFORMATION SERVICE rather than a technical utility.

### Three Independent Information Domains

SvitloSk simultaneously operates with THREE different information domains.

These domains MUST NOT be merged.

#### Domain A — Queue Schedule (Critical Power Limitation)

Represents official emergency electricity limitation.

Characteristics:
- based on official Oblenergo schedule
- consists of 6 queues
- consists of 12 subqueues
- NOT address-based
- schedule changes by hour

Example:
```
Queue 1
  Subqueue 1.1
  Subqueue 1.2
  ...
Queue 6
  Subqueue 6.2
```

The PWA application is primarily built around this domain.

#### Domain B — Planned Outages

Address-based.

Official planned maintenance.

Contains:
- settlements
- streets
- houses
- planned time intervals

Independent from Queue Schedule.

#### Domain C — Emergency Outages

Address-based.

Unexpected outages.

Contains:
- settlements
- streets
- houses
- emergency information

Independent from Planned Outages.

Independent from Queue Schedule.

### IMPORTANT

Queue Schedule, Planned Outages, Emergency Outages are THREE DIFFERENT ONTOLOGICAL OBJECTS. Never merge them.

### Existing Parsers

#### Parser A

Purpose: Collect official Queue Schedule.

Produces: Queue timetable.

#### Parser B

Purpose: Collect planned and emergency outages.

Produces: Address-based outage information.

These parsers are independent.

### PWA Application

Current screens:

#### Main

Displays current Queue Schedule for one selected subqueue.

Upper information panel.

Timeline.

Tomorrow graph.

#### Archive

Displays historical Queue Schedules.

Calendar.

Historical timelines.

#### Address Lookup

Allows resident to determine which subqueue serves their address.

Search by:
- Settlement
- Street
- House

#### Personal Cabinet

Allows configuration of:
- Two independent locations
- Push notifications
- Silence mode
- Future schedule notifications
- About
- Feedback
- Sharing

### Push Notifications

Push notifications belong ONLY to Queue Schedule.

They notify about:
- electricity loss
- electricity restoration

for the selected subqueue.

NOT about planned outages.

NOT about emergency outages.

### Public Information Journal

The project also publishes a Public Information Journal.

One journal edition may contain:
- planned outages (today)
- emergency outages (today)
- planned outages (tomorrow)
- emergency outages (tomorrow)
- tomorrow queue graph
- technical project messages
- future project messages

Tomorrow information disappears after the current day ends.

Journal publications are grouped by Starosta Districts.

### Publishing Architecture

The project contains a Publishing Subsystem.

Its purpose is publication of the Journal.

NOT Telegram.

Architecture:
```
Publishing Subsystem
│
├── Telegram Adapter
│
└── Facebook Adapter
```

Telegram and Facebook are PEER adapters.

Neither is primary.

Future adapters may exist.

---

# 4. Reconciliation Task

This investigation must reconcile:

1. Repository documentation (CHARTER, GLOSSARY, ARCHITECTURE, DATA_MODEL)
2. Architect Intent (three domains, two parsers, PWA, publishing subsystem)

Where they conflict, BOTH are recorded.

Where they align, BOTH are recorded.

The investigation does NOT choose between them.

---

# 5. Research Tasks

## PART 1 — Ontology

Reconstruct the complete ontology of SvitloSk.

Identify:
- Objects
- Services
- Processes
- Roles
- Data Sources
- Representations
- Identity Dimensions
- Channels
- Adapters

## PART 2 — Atomic Objects

Determine which concepts are truly atomic.

Determine which concepts are composite.

## PART 3 — Journal

Determine ontological status of:
- Journal
- Journal Edition
- Publication
- Release
- Issue

Determine relationships between them.

## PART 4 — Publishing

Determine ontological status of:
- Publishing Subsystem
- Telegram Adapter
- Facebook Adapter
- Publication
- Representation

## PART 5 — Electricity

Determine ontology of:
- Queue
- Subqueue
- Schedule
- Planned Outage
- Emergency Outage

## PART 6 — PWA

Determine ontology of:
- Screen
- Timeline
- Tomorrow Graph
- Push Notification
- Address Lookup
- Personal Cabinet

## PART 7 — Competing Models

Construct at least FIVE competing ontological models.

Do NOT choose one.

## PART 8 — Contradictions

Identify contradictions between:
- repository
- previous investigations
- architect intent

## PART 9 — Hidden Assumptions

Identify every hidden assumption.

## PART 10 — Dependency Graph

Construct complete dependency graph.

## PART 11 — Candidate Glossary

Produce glossary candidate.

Do NOT promote.

## PART 12 — Open Questions

Produce unresolved questions.

## PART 13 — Certificate

Produce investigation certificate.

---

# 6. Deliverables

| Document | Purpose |
|----------|---------|
| SVTONTO001_HEARING.md | Case scope and research questions |
| SVTONTO001_PART1_ONTOLOGY.md | Complete ontology |
| SVTONTO001_PART2_ATOMIC.md | Atomic vs composite objects |
| SVTONTO001_PART3_JOURNAL.md | Journal ontology |
| SVTONTO001_PART4_PUBLISHING.md | Publishing ontology |
| SVTONTO001_PART5_ELECTRICITY.md | Electricity ontology |
| SVTONTO001_PART6_PWA.md | PWA ontology |
| SVTONTO001_PART7_MODELS.md | Competing models |
| SVTONTO001_PART8_CONTRADICTIONS.md | Contradictions |
| SVTONTO001_PART9_ASSUMPTIONS.md | Hidden assumptions |
| SVTONTO001_PART10_DEPENDENCY.md | Dependency graph |
| SVTONTO001_PART11_GLOSSARY.md | Candidate glossary |
| SVTONTO001_PART12_QUESTIONS.md | Open questions |
| SVTONTO001_PART13_CERTIFICATE.md | Investigation certificate |

---

# 7. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
