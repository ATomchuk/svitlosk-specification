# LC001_RESEARCH3_OWNERSHIP

**Document ID:** CASE-LC-001-R3

**Title:** Operation Ownership

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines which subsystem owns each lifecycle operation.

---

# 2. Ownership Models

## 2.1 Model A: Parser Owns All Input Operations

### Ownership

| Operation | Owner |
|-----------|-------|
| Create | Parser |
| Update | Parser |
| Replace | Parser |
| Merge | Parser |

### Description

Parser is responsible for ALL input operations.

Lifecycle and Publisher are passive — they receive information from Parser.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | HIGH — single owner |
| Consistency | MEDIUM — Parser may not know about expiry |
| Completeness | LOW — does not explain temporal operations |

---

## 2.2 Model B: Lifecycle Owns All Temporal Operations

### Ownership

| Operation | Owner |
|-----------|-------|
| Create | Parser |
| Update | Parser |
| Replace | Lifecycle |
| Merge | Lifecycle |
| Expire | Lifecycle |
| Archive | Lifecycle |

### Description

Parser handles input.

Lifecycle handles temporal behavior (replace, merge, expire, archive).

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — two owners |
| Consistency | HIGH — temporal operations belong to lifecycle |
| Completeness | MEDIUM — does not explain distribution |

---

## 2.3 Model C: Publisher Owns All Distribution Operations

### Ownership

| Operation | Owner |
|-----------|-------|
| Create | Parser |
| Update | Parser |
| Replace | Lifecycle |
| Merge | Lifecycle |
| Expire | Lifecycle |
| Archive | Lifecycle |
| Republish | Publisher |
| Hide | Publisher |
| Reveal | Publisher |

### Description

Parser handles input.

Lifecycle handles temporal behavior.

Publisher handles distribution and presentation.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | MEDIUM — three owners |
| Consistency | HIGH — clear separation |
| Completeness | HIGH — covers all operations |

---

## 2.4 Model D: Event-Driven Ownership

### Ownership

| Event | Handler |
|-------|---------|
| Data received | Parser |
| Data changed | Lifecycle |
| Data expired | Lifecycle |
| Data archived | Lifecycle |
| Distribution needed | Publisher |
| Channel update needed | Adapter |

### Description

Operations are triggered by EVENTS.

Each event has a designated HANDLER.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | LOW — many handlers |
| Consistency | HIGH — event-driven is natural |
| Completeness | HIGH — covers all scenarios |

---

## 2.5 Model E: Shared Ownership

### Ownership

| Operation | Primary Owner | Secondary Owner |
|-----------|---------------|-----------------|
| Create | Parser | — |
| Update | Parser | Lifecycle |
| Replace | Lifecycle | Publisher |
| Merge | Lifecycle | Parser |
| Expire | Lifecycle | Publisher |
| Archive | Lifecycle | Storage |
| Republish | Publisher | Adapter |
| Hide | Publisher | Adapter |
| Reveal | Publisher | Adapter |

### Description

Operations have PRIMARY and SECONDARY owners.

Both must coordinate for the operation to complete.

### Evaluation

| Criterion | Assessment |
|-----------|------------|
| Simplicity | LOW — complex ownership |
| Consistency | MEDIUM — shared ownership is ambiguous |
| Completeness | HIGH — covers all operations |

---

# 3. Ownership Matrix

| Operation | Model A | Model B | Model C | Model D | Model E |
|-----------|---------|---------|---------|---------|---------|
| Create | Parser | Parser | Parser | Parser | Parser |
| Update | Parser | Parser | Parser | Parser | Parser+Lifecycle |
| Replace | Parser | Lifecycle | Lifecycle | Lifecycle | Lifecycle+Publisher |
| Merge | Parser | Lifecycle | Lifecycle | Lifecycle | Lifecycle+Parser |
| Expire | — | Lifecycle | Lifecycle | Lifecycle | Lifecycle+Publisher |
| Archive | — | Lifecycle | Lifecycle | Lifecycle | Lifecycle+Storage |
| Republish | — | — | Publisher | Publisher | Publisher+Adapter |
| Hide | — | — | Publisher | Publisher | Publisher+Adapter |
| Reveal | — | — | Publisher | Publisher | Publisher+Adapter |

---

# 4. Findings

## 4.1 Finding OWN-001

**Five competing ownership models were constructed.**

Each model has different strengths and weaknesses.

**Evidence:** Analysis of operation ownership.

**Confidence:** HIGH.

## 4.2 Finding OWN-002

**Model C (Three-Owner Model) is most complete.**

Parser owns input, Lifecycle owns temporal, Publisher owns distribution.

**Evidence:** Analysis of ownership models.

**Confidence:** HIGH.

## 4.3 Finding OWN-003

**Model D (Event-Driven) is most natural for SvitloSk.**

Operations are triggered by events, each with a designated handler.

**Evidence:** Analysis of ownership models.

**Confidence:** HIGH.

## 4.4 Finding OWN-004

**No single subsystem can own ALL operations.**

Operations span multiple domains (input, temporal, distribution).

**Evidence:** Analysis of ownership models.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OWN-001 | Analysis of ownership models |
| OWN-002 | Analysis of ownership models |
| OWN-003 | Analysis of ownership models |
| OWN-004 | Analysis of ownership models |

---

**End of Operation Ownership**
