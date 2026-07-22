# PUB005_HIDDEN_RULES

**Document ID:** CASE-PUB-005-HR

**Title:** Hidden Rules

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document looks for rules that exist in implementation but are never documented.

---

# 2. Hidden Rules

## 2.1 HR-001: Timer-Based Expiry

### Evidence

> "Tomorrow information disappears automatically before the end of the current day." (Architect Intent)

### Hidden Rule

There is a TIMER that triggers expiry at end of day.

### Documentation Status

UNDOCUMENTED — timer mechanism not specified.

---

## 2.2 HR-002: Graph Replacement Strategy

### Evidence

> Queue Graph is replaced entirely, not edited. (CASE-TG-CORE-001)

### Hidden Rule

Graphs are REPLACED, not EDITED.

### Documentation Status

UNDOCUMENTED — replacement strategy not specified.

---

## 2.3 HR-003: Archive Timing

### Evidence

> Publications are archived at period end. (TELEGRAM_LIFECYCLE.md)

### Hidden Rule

Archival occurs at EXACT end of Reporting Period.

### Documentation Status

UNDOCUMENTED — exact timing not specified.

---

## 2.4 HR-004: Message Edit Strategy

### Evidence

> Channel messages are edited in place. (TELEGRAM_LIFECYCLE.md §5.2)

### Hidden Rule

Messages are EDITED, not replaced.

### Documentation Status

UNDOCUMENTED — edit strategy not specified.

---

## 2.5 HR-005: Territory Ordering Algorithm

### Evidence

> "Journal publications are grouped by Starosta Districts." (Architect Intent)

### Hidden Rule

Territories are ordered by TERRITORIAL_MODEL hierarchy.

### Documentation Status

UNDOCUMENTED — ordering algorithm not specified.

---

## 2.6 HR-006: Publication Ordering Within Territory

### Evidence

> Emergency publications appear before planned. (Implicit in implementation)

### Hidden Rule

Within a Territory, emergency publications appear BEFORE planned publications.

### Documentation Status

UNDOCUMENTED — ordering rule not specified.

---

## 2.7 HR-007: Graph Generation Timing

### Evidence

> Graph is generated when tomorrow's schedule is available. (CASE-TG-CORE-001)

### Hidden Rule

Graph generation occurs IMMEDIATELY when schedule data arrives.

### Documentation Status

UNDOCUMENTED — timing not specified.

---

## 2.8 HR-008: Technical Message Update Frequency

### Evidence

> Technical messages show latest timestamp. (Architect Intent)

### Hidden Rule

Technical messages are updated whenever system status changes.

### Documentation Status

UNDOCUMENTED — frequency not specified.

---

# 3. Hidden Rules Summary

| ID | Rule | Documentation Status |
|----|------|---------------------|
| HR-001 | Timer-Based Expiry | UNDOCUMENTED |
| HR-002 | Graph Replacement Strategy | UNDOCUMENTED |
| HR-003 | Archive Timing | UNDOCUMENTED |
| HR-004 | Message Edit Strategy | UNDOCUMENTED |
| HR-005 | Territory Ordering Algorithm | UNDOCUMENTED |
| HR-006 | Publication Ordering Within Territory | UNDOCUMENTED |
| HR-007 | Graph Generation Timing | UNDOCUMENTED |
| HR-008 | Technical Message Update Frequency | UNDOCUMENTED |

---

# 4. Findings

## 4.1 Finding HR-001

**8 hidden rules were identified.**

All exist in implementation but are not documented.

**Evidence:** Analysis of hidden rules.

**Confidence:** HIGH.

## 4.2 Finding HR-002

**Most hidden rules relate to TIMING.**

When things happen, not what happens.

**Evidence:** Analysis of hidden rules.

**Confidence:** HIGH.

## 4.3 Finding HR-003

**Hidden rules are IMPLEMENTATION details.**

They describe HOW, not WHAT.

**Evidence:** Analysis of hidden rules.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| HR-001 | Analysis of hidden rules |
| HR-002 | Analysis of hidden rules |
| HR-003 | Analysis of hidden rules |

---

**End of Hidden Rules**
