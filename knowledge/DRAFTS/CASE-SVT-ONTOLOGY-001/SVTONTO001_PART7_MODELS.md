# SVTONTO001_PART7_MODELS

**Document ID:** CASE-SVT-ONTOLOGY-001-P7

**Title:** Competing Ontological Models

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs at least FIVE competing ontological models for SvitloSk.

Following Research Method V1.0 Principle 2: "Multiple Models Before Selection."

---

# 2. Competing Models

## 2.1 Model A: Three-Domain Service Model

### Ontology

```
SvitloSk (Service)
    │
    ├── Domain A: Queue Schedule Service
    │   ├── Queue
    │   ├── Subqueue
    │   ├── Schedule
    │   ├── Timeline
    │   └── Tomorrow Graph
    │
    ├── Domain B: Planned Outage Service
    │   ├── Planned Outage
    │   ├── Address
    │   └── Time Interval
    │
    └── Domain C: Emergency Outage Service
        ├── Emergency Outage
        ├── Address
        └── Emergency Information
```

### Description

SvitloSk is a SERVICE composed of THREE INDEPENDENT domain services.

Each domain service operates independently.

### Characteristics

- Three independent services
- Domain isolation
- No shared objects between domains

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | HIGH — clear separation |
| Consistency | HIGH — matches Architect Intent |
| Semantic completeness | MEDIUM — does not explain Journal |
| CHARTER compatibility | MEDIUM — CHARTER does not mention three domains |

---

## 2.2 Model B: Service-Plus-Journal Model

### Ontology

```
SvitloSk (Service)
    │
    ├── Domain A: Queue Schedule Service
    │
    ├── Domain B: Planned Outage Service
    │
    ├── Domain C: Emergency Outage Service
    │
    └── Journal Service
        ├── Journal Edition
        │   ├── Publication (per Territory)
        │   └── Publication (per Territory)
        └── Journal Edition
```

### Description

SvitloSk is a SERVICE composed of THREE domain services PLUS a Journal Service.

The Journal Service publishes information from all three domains.

### Characteristics

- Three domain services
- One Journal Service
- Journal publishes from all domains

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — four services |
| Consistency | HIGH — matches Architect Intent |
| Semantic completeness | HIGH — explains Journal |
| CHARTER compatibility | HIGH — CHARTER mentions Journal |

---

## 2.3 Model C: Domain-First Model

### Ontology

```
SvitloSk (Service)
    │
    ├── Domain A: Queue Schedule
    │   ├── Queue
    │   ├── Subqueue
    │   ├── Schedule
    │   └── PWA (Main, Archive, Address Lookup, Personal Cabinet)
    │
    ├── Domain B: Planned Outages
    │   ├── Planned Outage
    │   ├── Address
    │   └── Journal Publication
    │
    └── Domain C: Emergency Outages
        ├── Emergency Outage
        ├── Address
        └── Journal Publication
```

### Description

SvitloSk is a SERVICE organized by THREE domains.

Domain A is primarily served by PWA.

Domains B and C are primarily served by Journal.

### Characteristics

- Domain-first organization
- PWA for Queue Schedule
- Journal for Outages

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | HIGH — clear domain ownership |
| Consistency | HIGH — matches Architect Intent |
| Semantic completeness | HIGH — explains PWA and Journal |
| CHARTER compatibility | HIGH — CHARTER mentions Journal |

---

## 2.4 Model D: Channel-First Model

### Ontology

```
SvitloSk (Service)
    │
    ├── PWA Channel
    │   ├── Queue Schedule Display
    │   ├── Timeline
    │   ├── Tomorrow Graph
    │   ├── Address Lookup
    │   └── Push Notifications
    │
    └── Publishing Channel
        ├── Telegram Adapter
        ├── Facebook Adapter
        └── Journal
            ├── Journal Edition
            └── Publication
```

### Description

SvitloSk is a SERVICE organized by CHANNELS.

PWA is one channel (primarily for Queue Schedule).

Publishing is another channel (for Journal via Telegram/Facebook).

### Characteristics

- Channel-first organization
- PWA and Publishing as peers
- Journal within Publishing channel

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — two channels |
| Consistency | HIGH — matches Architect Intent |
| Semantic completeness | HIGH — explains all components |
| CHARTER compatibility | MEDIUM — CHARTER does not mention channels |

---

## 2.5 Model E: Information-Flow Model

### Ontology

```
DSO (Data Source)
    │
    ├── Parser A → Queue Timetable → PWA
    │
    └── Parser B → Address Information → Journal → Telegram/Facebook
```

### Description

SvitloSk is organized by INFORMATION FLOW.

Data flows from DSO through parsers to consumers.

PWA consumes Queue Timetable directly.

Journal consumes Address Information and distributes via Telegram/Facebook.

### Characteristics

- Flow-first organization
- Two independent flows
- PWA and Journal as consumers

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | HIGH — clear data flow |
| Consistency | HIGH — matches Architect Intent |
| Semantic completeness | MEDIUM — does not explain all components |
| CHARTER compatibility | MEDIUM — CHARTER does not mention flows |

---

## 2.6 Model F: Hybrid Model

### Ontology

```
SvitloSk (Service)
    │
    ├── Domain Layer
    │   ├── Queue Schedule Domain
    │   ├── Planned Outage Domain
    │   └── Emergency Outage Domain
    │
    ├── Channel Layer
    │   ├── PWA Channel
    │   └── Publishing Channel
    │       ├── Telegram Adapter
    │       └── Facebook Adapter
    │
    └── Journal Layer
        ├── Journal Edition
        └── Publication
```

### Description

SvitloSk is organized by LAYERS.

Domain Layer contains the three independent domains.

Channel Layer contains PWA and Publishing.

Journal Layer contains the Journal.

### Characteristics

- Layered organization
- Domains, Channels, and Journal as separate layers
- Clear separation of concerns

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | LOW — three layers |
| Consistency | HIGH — matches all evidence |
| Semantic completeness | HIGH — explains everything |
| CHARTER compatibility | HIGH — CHARTER mentions Journal |

---

# 3. Model Comparison Matrix

| Criterion | Model A | Model B | Model C | Model D | Model E | Model F |
|-----------|---------|---------|---------|---------|---------|---------|
| Simplicity | HIGH | MEDIUM | HIGH | MEDIUM | HIGH | LOW |
| Consistency | HIGH | HIGH | HIGH | HIGH | HIGH | HIGH |
| Semantic completeness | MEDIUM | HIGH | HIGH | HIGH | MEDIUM | HIGH |
| CHARTER compatibility | MEDIUM | HIGH | HIGH | MEDIUM | MEDIUM | HIGH |

---

# 4. Cross-Examination

## 4.1 Model A vs Model B

**Model A** has three domain services only.

**Model B** has three domain services PLUS Journal Service.

**Contradiction:** Model A does not explain Journal. Model B does.

**Resolution:** Model B is more complete than Model A.

## 4.2 Model C vs Model D

**Model C** is domain-first (Queue Schedule → PWA, Outages → Journal).

**Model D** is channel-first (PWA, Publishing).

**Contradiction:** Different organizational principles.

**Resolution:** These are complementary perspectives, not contradictions.

## 4.3 Model E vs All Others

**Model E** is flow-first (data flows from DSO to consumers).

**All others** are structure-first (services, domains, channels).

**Contradiction:** Different organizational principles.

**Resolution:** Model E is a valid alternative perspective.

## 4.4 Model F vs All Others

**Model F** is layered (Domains, Channels, Journal).

**All others** are flat or hierarchical.

**Contradiction:** Different organizational principles.

**Resolution:** Model F is the most comprehensive but most complex.

---

# 5. Findings

## 5.1 Finding MODELS-001

**Six competing ontological models were constructed.**

Each model has different strengths and weaknesses.

**Evidence:** Analysis of CHARTER, GLOSSARY, Architect Intent.

**Confidence:** HIGH.

## 5.2 Finding MODELS-002

**Model F (Hybrid Model) is most comprehensive.**

It explains all components: domains, channels, and journal.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 5.3 Finding MODELS-003

**Model C (Domain-First) is most aligned with Architect Intent.**

It explicitly separates Queue Schedule (PWA) from Outages (Journal).

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| MODELS-001 | CHARTER, GLOSSARY, Architect Intent |
| MODELS-002 | Analysis of all evidence sources |
| MODELS-003 | Architect Intent |

---

**End of Competing Models**
