# PUB004_DECISION_GRAPH

**Document ID:** CASE-PUB-004-DG

**Title:** Decision Graph

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs the decision graph.

---

# 2. Decision Graph

## 2.1 Visual Representation

```
                    ┌─────────────┐
                    │    Input    │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │    TIME     │ │ INFORMATION │ │   CHANNEL   │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  Lifecycle  │ │   Parser    │ │   Adapter   │
    │   (Decide)  │ │   (Decide)  │ │   (Decide)  │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           └───────────────┼───────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Publisher  │
                    │  (Execute)  │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │   Create    │ │   Update    │ │   Remove    │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │ Publication │ │ Publication │ │ Publication │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           └───────────────┼───────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Channel   │
                    │ (Deliver)   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Resident  │
                    └─────────────┘
```

---

## 2.2 Decision Flow

### Step 1: Input

Events arrive from:
- TIME (temporal triggers)
- INFORMATION (data changes)
- CHANNEL (channel state)

### Step 2: Decision

Decision makers determine action:
- Lifecycle (TIME decisions)
- Parser (INFORMATION decisions)
- Adapter (CHANNEL decisions)

### Step 3: Execution

Publisher executes the decided action:
- Create
- Update
- Remove
- Replace
- Archive

### Step 4: Affected Object

Action affects:
- Publication
- Graph
- Journal Edition

### Step 5: Delivery

Channel delivers to:
- Resident

---

# 3. Decision Graph Summary

| Stage | Components | Count |
|-------|------------|-------|
| Input | TIME, INFORMATION, CHANNEL | 3 |
| Decision | Lifecycle, Parser, Adapter | 3 |
| Execution | Publisher | 1 |
| Affected Object | Publication, Graph, Journal Edition | 3 |
| Delivery | Channel, Resident | 2 |

---

# 4. Findings

## 4.1 Finding DG-001

**The decision graph has 5 stages.**

Input → Decision → Execution → Affected Object → Delivery.

**Evidence:** Analysis of decision graph.

**Confidence:** HIGH.

## 4.2 Finding DG-002

**Publisher is in the EXECUTION stage, not DECISION stage.**

Publisher executes decisions made by others.

**Evidence:** Analysis of decision graph.

**Confidence:** HIGH.

## 4.3 Finding DG-003

**Decision makers are SEPARATE from execution.**

Lifecycle, Parser, Adapter decide. Publisher executes.

**Evidence:** Analysis of decision graph.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| DG-001 | Analysis of decision graph |
| DG-002 | Analysis of decision graph |
| DG-003 | Analysis of decision graph |

---

**End of Decision Graph**
