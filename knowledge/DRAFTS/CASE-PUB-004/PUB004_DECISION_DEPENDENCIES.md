# PUB004_DECISION_DEPENDENCIES

**Document ID:** CASE-PUB-004-DD

**Title:** Decision Dependencies

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines which decisions depend on TIME, INFORMATION, or CHANNEL.

---

# 2. Decision Dependencies

## 2.1 TIME-DEPENDENT Decisions

### DD-001: Publication Expiry

**Depends on:** TIME

**Reason:** Expiry is determined by time boundary (end of day).

**Evidence:** EV-004 — temporal trigger.

---

### DD-002: Graph Expiry

**Depends on:** TIME

**Reason:** Graph expiry is determined by time boundary.

**Evidence:** EV-009 — temporal trigger.

---

### DD-003: Reporting Period End

**Depends on:** TIME

**Reason:** Reporting Period is a temporal boundary.

**Evidence:** EV-012 — temporal trigger.

---

### DD-004: New Reporting Period

**Depends on:** TIME

**Reason:** New Reporting Period is a temporal boundary.

**Evidence:** EV-013 — temporal trigger.

---

## 2.2 INFORMATION-DEPENDENT Decisions

### DD-005: New Information Appears

**Depends on:** INFORMATION

**Reason:** Decision based on presence of new data.

**Evidence:** EV-001 — data trigger.

---

### DD-006: Information Changes

**Depends on:** INFORMATION

**Reason:** Decision based on data comparison.

**Evidence:** EV-002 — data trigger.

---

### DD-007: Information Disappears

**Depends on:** INFORMATION

**Reason:** Decision based on data absence.

**Evidence:** EV-003 — data trigger.

---

### DD-008: Publication Becomes Obsolete

**Depends on:** INFORMATION

**Reason:** Decision based on data relevance.

**Evidence:** EV-005 — data trigger.

---

### DD-009: Publication Needs Update

**Depends on:** INFORMATION

**Reason:** Decision based on data comparison.

**Evidence:** EV-006 — data trigger.

---

### DD-010: Graph Changes

**Depends on:** INFORMATION

**Reason:** Decision based on data change.

**Evidence:** EV-007 — data trigger.

---

### DD-011: Graph Becomes Available

**Depends on:** INFORMATION

**Reason:** Decision based on data presence.

**Evidence:** EV-008 — data trigger.

---

### DD-012: Technical Message Changes

**Depends on:** INFORMATION

**Reason:** Decision based on system status.

**Evidence:** EV-010 — data trigger.

---

### DD-013: Service Announcement Published

**Depends on:** INFORMATION

**Reason:** Decision based on announcement content.

**Evidence:** EV-011 — external trigger.

---

## 2.3 CHANNEL-DEPENDENT Decisions

### DD-014: Channel Becomes Available

**Depends on:** CHANNEL

**Reason:** Decision based on channel state.

**Evidence:** EV-015 — channel trigger.

---

### DD-015: Channel Becomes Unavailable

**Depends on:** CHANNEL

**Reason:** Decision based on channel state.

**Evidence:** EV-016 — channel trigger.

---

### DD-016: Channel Message Delivered

**Depends on:** CHANNEL

**Reason:** Decision based on channel response.

**Evidence:** EV-017 — channel trigger.

---

### DD-017: Channel Message Failed

**Depends on:** CHANNEL

**Reason:** Decision based on channel response.

**Evidence:** EV-018 — channel trigger.

---

# 3. Decision Dependency Summary

| Dependency | Decisions | Count |
|------------|-----------|-------|
| TIME | DD-001, DD-002, DD-003, DD-004 | 4 |
| INFORMATION | DD-005, DD-006, DD-007, DD-008, DD-009, DD-010, DD-011, DD-012, DD-013 | 9 |
| CHANNEL | DD-014, DD-015, DD-016, DD-017 | 4 |

---

# 4. Findings

## 4.1 Finding DD-001

**There are 17 decision dependencies.**

TIME (4), INFORMATION (9), CHANNEL (4).

**Evidence:** Analysis of decision dependencies.

**Confidence:** HIGH.

## 4.2 Finding DD-002

**INFORMATION is the MOST COMMON dependency.**

9 out of 17 decisions.

**Evidence:** Analysis of decision dependency summary.

**Confidence:** HIGH.

## 4.3 Finding DD-003

**TIME and CHANNEL have EQUAL dependency count.**

4 each.

**Evidence:** Analysis of decision dependency summary.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| DD-001 | Analysis of decision dependencies |
| DD-002 | Analysis of decision dependency summary |
| DD-003 | Analysis of decision dependency summary |

---

**End of Decision Dependencies**
