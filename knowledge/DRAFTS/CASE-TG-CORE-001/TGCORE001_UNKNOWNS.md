# TGCORE001_UNKNOWNS

**Document ID:** CASE-TG-CORE-001-UN

**Title:** Unknowns

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines which Telegram behavior cannot be explained from repository evidence.

---

# 2. Unknowns

## 2.1 UN-001: Exact Graph Generation Algorithm

### What We Know

Queue Graph is generated from queue schedule data.

### What We Don't Know

- Exact algorithm for SVG generation
- Exact algorithm for PNG conversion
- Image size and format specifications

### Evidence

> "Graph Generator → SVG → PNG" (Architect Context)

But exact algorithms are not documented.

### Status

UNKNOWN — implementation detail.

---

## 2.2 UN-002: Exact Formatting Rules

### What We Know

Messages are formatted for Telegram display.

### What We Don't Know

- Exact markdown/HTML rules
- Exact template specifications
- Exact message structure

### Evidence

> "Editorial Rules" (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md)

But exact formatting rules are not documented.

### Status

UNKNOWN — implementation detail.

---

## 2.3 UN-003: Exact Expiry Time

### What We Know

Temporary products expire at "end of day."

### What We Don't Know

- Exact time of expiry (midnight? other?)
- Exact mechanism for expiry

### Evidence

> "Tomorrow information disappears automatically before the end of the current day." (Architect Intent)

But exact time is not specified.

### Status

UNKNOWN — operational detail.

---

## 2.4 UN-004: Message Ordering Rules

### What We Know

Publications are grouped by territory.

### What We Don't Know

- Exact ordering of messages within territory
- Exact ordering of territories

### Evidence

> "Journal publications are grouped by Starosta Districts." (Architect Intent)

But exact ordering rules are not documented.

### Status

UNKNOWN — presentation detail.

---

## 2.5 UN-005: Error Handling

### What We Know

Telegram Bot API is used for delivery.

### What We Don't Know

- How errors are handled
- Retry logic
- Failure recovery

### Evidence

No documentation on error handling.

### Status

UNKNOWN — implementation detail.

---

## 2.6 UN-006: Rate Limiting

### What We Know

Messages are sent to Telegram channel.

### What We Don't Know

- Rate limiting rules
- Throttling mechanisms

### Evidence

No documentation on rate limiting.

### Status

UNKNOWN — implementation detail.

---

# 3. Unknown Summary

| ID | Unknown | Category | Priority |
|----|---------|----------|----------|
| UN-001 | Graph Generation Algorithm | Implementation | LOW |
| UN-002 | Formatting Rules | Implementation | MEDIUM |
| UN-003 | Expiry Time | Operational | LOW |
| UN-004 | Message Ordering | Presentation | LOW |
| UN-005 | Error Handling | Implementation | MEDIUM |
| UN-006 | Rate Limiting | Implementation | LOW |

---

# 4. Findings

## 4.1 Finding UN-001

**6 unknowns were identified.**

All are implementation or operational details.

**Evidence:** Analysis of unknowns.

**Confidence:** HIGH.

## 4.2 Finding UN-002

**No critical unknowns exist.**

All unknowns are implementation details, not architectural.

**Evidence:** Analysis of unknowns.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| UN-001 | Analysis of unknowns |
| UN-002 | Analysis of unknowns |

---

**End of Unknowns**
