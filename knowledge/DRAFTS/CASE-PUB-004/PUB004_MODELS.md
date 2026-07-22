# PUB004_MODELS

**Document ID:** CASE-PUB-004-MDL

**Title:** Competing Models

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs competing models for decision making.

---

# 2. Competing Models

## 2.1 Model A: Decision Inside Publisher

### Structure

```
Publisher
    ├── Decides
    │   ├── When to create
    │   ├── When to update
    │   ├── When to remove
    │   └── When to archive
    └── Executes
        ├── Create
        ├── Update
        ├── Remove
        └── Archive
```

### Description

Publisher both DECIDES and EXECUTES.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | HIGH — single component |
| Separation | LOW — decision mixed with execution |
| Testability | LOW — hard to test decisions independently |

---

## 2.2 Model B: Decision Inside Lifecycle

### Structure

```
Lifecycle
    ├── Decides
    │   ├── When to create
    │   ├── When to update
    │   ├── When to remove
    │   └── When to archive
    ↓
Publisher
    └── Executes
        ├── Create
        ├── Update
        ├── Remove
        └── Archive
```

### Description

Lifecycle DECIDES, Publisher EXECUTES.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — two components |
| Separation | HIGH — clear separation |
| Testability | HIGH — decisions testable independently |

---

## 2.3 Model C: Separate Decision Engine

### Structure

```
Decision Engine
    ├── Rules
    │   ├── Temporal rules
    │   ├── Data rules
    │   └── Channel rules
    ↓
Publisher
    └── Executes
        ├── Create
        ├── Update
        ├── Remove
        └── Archive
```

### Description

Separate engine owns all decision rules.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | LOW — extra component |
| Separation | HIGHEST — complete separation |
| Testability | HIGHEST — rules testable independently |

---

## 2.4 Model D: Event-Driven

### Structure

```
Events
    ├── TIME → Lifecycle Handler
    ├── INFORMATION → Parser Handler
    ├── CHANNEL → Adapter Handler
    ↓
Publisher
    └── Executes based on events
```

### Description

Events drive decisions through handlers.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — event-driven |
| Separation | HIGH — handlers separate |
| Testability | HIGH — handlers testable |

---

## 2.5 Model E: Rule Engine

### Structure

```
Rule Engine
    ├── Rule: IF time=midnight THEN remove tomorrow
    ├── Rule: IF data changed THEN update publication
    ├── Rule: IF channel unavailable THEN pause
    ↓
Publisher
    └── Executes matched rules
```

### Description

Explicit rules drive decisions.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | LOW — rule management |
| Separation | HIGHEST — rules explicit |
| Testability | HIGHEST — rules testable |

---

# 3. Model Comparison Matrix

| Criterion | A | B | C | D | E |
|-----------|---|---|---|---|---|
| Simplicity | HIGH | MEDIUM | LOW | MEDIUM | LOW |
| Separation | LOW | HIGH | HIGHEST | HIGH | HIGHEST |
| Testability | LOW | HIGH | HIGHEST | HIGH | HIGHEST |

---

# 4. Findings

## 4.1 Finding MDL-001

**5 competing models were constructed.**

Each has different strengths and weaknesses.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 4.2 Finding MDL-002

**Model C (Separate Decision Engine) and Model E (Rule Engine) have HIGHEST separation.**

But they are also most complex.

**Evidence:** Analysis of model comparison.

**Confidence:** HIGH.

## 4.3 Finding MDL-003

**Model B (Decision Inside Lifecycle) has BEST balance.**

Good separation, good simplicity.

**Evidence:** Analysis of model comparison.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| MDL-001 | Analysis of all evidence sources |
| MDL-002 | Analysis of model comparison |
| MDL-003 | Analysis of model comparison |

---

**End of Competing Models**
