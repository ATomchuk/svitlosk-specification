# LC001_RESEARCH5_TEMPORAL

**Document ID:** CASE-LC-001-R5

**Title:** Temporal Behavior

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document investigates temporal behavior and determines which component owns it.

---

# 2. Temporal Scenarios

## 2.1 Scenario A: Tomorrow Planned Outages Disappear

**What happens:** Tomorrow's planned outages disappear at end of current day.

**Who owns this?**

| Candidate | Evidence For | Evidence Against |
|-----------|--------------|------------------|
| Parser | Detects new day | Does not know about publication state |
| Lifecycle | Knows temporal rules | Does not execute removal |
| Publisher | Executes removal | Does not know temporal rules |
| Adapter | Displays content | Does not know temporal rules |

**Most likely owner:** Lifecycle (knows temporal rules) + Publisher (executes removal).

---

## 2.2 Scenario B: Technical Message Shows Latest Timestamp

**What happens:** Technical message always shows latest update timestamp.

**Who owns this?**

| Candidate | Evidence For | Evidence Against |
|-----------|--------------|------------------|
| Parser | Provides new data | Does not know about publication state |
| Lifecycle | Knows update rules | Does not render content |
| Publisher | Renders content | Does not know update rules |
| Adapter | Displays content | Does not know update rules |

**Most likely owner:** Lifecycle (knows update rules) + Publisher (renders content).

---

## 2.3 Scenario C: Tomorrow Graph is Replaced

**What happens:** Tomorrow's queue graph is replaced when new data arrives.

**Who owns this?**

| Candidate | Evidence For | Evidence Against |
|-----------|--------------|------------------|
| Parser | Provides new graph data | Does not know about publication state |
| Lifecycle | Knows replacement rules | Does not execute replacement |
| Publisher | Executes replacement | Does not know replacement rules |
| Adapter | Displays content | Does not know replacement rules |

**Most likely owner:** Lifecycle (knows replacement rules) + Publisher (executes replacement).

---

## 2.4 Scenario D: Temporary Information Expires

**What happens:** Temporary information (tomorrow's outages) expires after reporting period.

**Who owns this?**

| Candidate | Evidence For | Evidence Against |
|-----------|--------------|------------------|
| Parser | Does not trigger expiry | — |
| Lifecycle | Knows expiry rules | Does not execute expiry |
| Publisher | Executes expiry | Does not know expiry rules |
| Adapter | Displays content | Does not know expiry rules |

**Most likely owner:** Lifecycle (knows expiry rules) + Publisher (executes expiry).

---

# 3. Temporal Ownership Pattern

## 3.1 Pattern

```
Lifecycle knows TEMPORAL RULES
    ↓
Lifecycle determines TEMPORAL EVENT occurred
    ↓
Lifecycle notifies Publisher
    ↓
Publisher executes TEMPORAL ACTION
    ↓
Publisher notifies Adapter
    ↓
Adapter updates channel
```

## 3.2 Separation

| Concern | Owner |
|---------|-------|
| Temporal rules | Lifecycle |
| Temporal event detection | Lifecycle |
| Temporal action execution | Publisher |
| Channel update | Adapter |

---

# 4. Findings

## 4.1 Finding TEMP-001

**Lifecycle owns TEMPORAL RULES.**

It knows when information should expire, be replaced, or be updated.

**Evidence:** Analysis of temporal scenarios.

**Confidence:** HIGH.

## 4.2 Finding TEMP-002

**Publisher executes TEMPORAL ACTIONS.**

It performs the actual removal, replacement, or update.

**Evidence:** Analysis of temporal scenarios.

**Confidence:** HIGH.

## 4.3 Finding TEMP-003

**Temporal behavior is SEPARATED from data acquisition.**

Parser does not own temporal behavior.

**Evidence:** Analysis of temporal scenarios.

**Confidence:** HIGH.

## 4.4 Finding TEMP-004

**Temporal behavior is SEPARATED from channel delivery.**

Adapter does not own temporal behavior.

**Evidence:** Analysis of temporal scenarios.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| TEMP-001 | Analysis of temporal scenarios |
| TEMP-002 | Analysis of temporal scenarios |
| TEMP-003 | Analysis of temporal scenarios |
| TEMP-004 | Analysis of temporal scenarios |

---

**End of Temporal Behavior**
