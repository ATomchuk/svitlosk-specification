# SYS001_MODELS

**Document ID:** CASE-SYS-001-MDL

**Title:** Competing Whole-System Models

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document builds at least five competing whole-system models.

NOT Publisher models. ENTIRE system models.

---

# 2. Competing Models

## 2.1 Model A: Three-Product Model

### Structure

```
SvitloSk
    ├── PWA Product (Queue Schedule)
    ├── Journal Product (Domains A,B,C via Telegram/Facebook)
    └── Archive Product (Historical records)
```

### Description

SvitloSk is THREE independent products.

PWA for Queue Schedule.

Journal for multi-domain publication.

Archive for historical records.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | HIGH — clear product separation |
| Consistency | HIGH — matches Architect Intent |
| Completeness | MEDIUM — does not explain shared infrastructure |

---

## 2.2 Model B: Domain-First Model

### Structure

```
SvitloSk
    ├── Domain A: Queue Schedule
    │   ├── Parser A
    │   ├── PWA
    │   └── Journal (tomorrow graph)
    │
    ├── Domain B: Planned Outages
    │   ├── Parser B
    │   └── Journal
    │
    └── Domain C: Emergency Outages
        ├── Parser B
        └── Journal
```

### Description

SvitloSk is organized by DOMAINS.

Each domain has its own parser and consumers.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | HIGH — clear domain separation |
| Consistency | HIGH — matches Architect Intent |
| Completeness | MEDIUM — does not explain shared Publisher |

---

## 2.3 Model C: Flow-First Model

### Structure

```
SvitloSk
    ├── Information Flow (DSO → Parser → Storage)
    ├── Knowledge Flow (Parser → Interpretation → Publisher)
    ├── Publication Flow (Publisher → Adapter → Channel)
    ├── Presentation Flow (Channel → Resident)
    ├── Update Flow (DSO change → System update)
    ├── Temporal Flow (Lifecycle → Expiry/Replacement)
    └── Notification Flow (Queue Schedule → Push)
```

### Description

SvitloSk is organized by FLOWS.

Each flow is a distinct concern.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — seven flows |
| Consistency | HIGH — matches information model |
| Completeness | HIGH — explains all behavior |

---

## 2.4 Model D: Layered Model

### Structure

```
SvitloSk
    ├── Data Layer (Parser, Storage)
    ├── Information Layer (Interpretation, Lifecycle)
    ├── Publication Layer (Publisher, Adapters)
    ├── Presentation Layer (Telegram, Facebook, PWA)
    └── Archive Layer (Historical records)
```

### Description

SvitloSk is organized by LAYERS.

Each layer has a specific responsibility.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — five layers |
| Consistency | HIGH — matches architectural principles |
| Completeness | HIGH — explains all components |

---

## 2.5 Model E: Event-Driven Model

### Structure

```
SvitloSk
    ├── Events
    │   ├── Data Changed → Parser Handler
    │   ├── Information Changed → Lifecycle Handler
    │   ├── Update Needed → Publisher Handler
    │   ├── Publication Ready → Adapter Handler
    │   ├── Temporal Event → Lifecycle Handler
    │   └── Resident Interaction → PWA Handler
    │
    └── Handlers
        ├── Parser Handler
        ├── Lifecycle Handler
        ├── Publisher Handler
        ├── Adapter Handler
        └── PWA Handler
```

### Description

SvitloSk is organized by EVENTS.

Each event has a designated handler.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | LOW — many handlers |
| Consistency | HIGH — matches update behavior |
| Completeness | HIGHEST — explains all interactions |

---

## 2.6 Model F: Hybrid Model

### Structure

```
SvitloSk
    │
    ├── Domain Layer
    │   ├── Domain A: Queue Schedule
    │   ├── Domain B: Planned Outages
    │   └── Domain C: Emergency Outages
    │
    ├── Product Layer
    │   ├── PWA
    │   ├── Journal
    │   └── Archive
    │
    ├── Flow Layer
    │   ├── Information Flow
    │   ├── Knowledge Flow
    │   ├── Publication Flow
    │   └── Representation Flow
    │
    └── Component Layer
        ├── Parsers
        ├── Publisher
        ├── Adapters
        └── Storage
```

### Description

SvitloSk is organized by MULTIPLE LAYERS.

Each layer provides a different perspective.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | LOW — four layers |
| Consistency | HIGHEST — matches all evidence |
| Completeness | HIGHEST — explains everything |

---

# 3. Model Comparison Matrix

| Criterion | A | B | C | D | E | F |
|-----------|---|---|---|---|---|---|
| Simplicity | HIGH | HIGH | MEDIUM | MEDIUM | LOW | LOW |
| Consistency | HIGH | HIGH | HIGH | HIGH | HIGH | HIGHEST |
| Completeness | MEDIUM | MEDIUM | HIGH | HIGH | HIGHEST | HIGHEST |

---

# 4. Findings

## 4.1 Finding MDL-001

**Six competing whole-system models were constructed.**

Each has different strengths and weaknesses.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 4.2 Finding MDL-002

**Model F (Hybrid) is most comprehensive.**

It explains all aspects: domains, products, flows, components.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 4.3 Finding MDL-003

**Model A (Three-Product) is most aligned with Architect Intent.**

It explicitly separates PWA, Journal, and Archive.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| MDL-001 | Analysis of all evidence sources |
| MDL-002 | Analysis of all evidence sources |
| MDL-003 | Architect Intent |

---

**End of Competing Whole-System Models**
