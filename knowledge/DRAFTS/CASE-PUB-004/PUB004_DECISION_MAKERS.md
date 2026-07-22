# PUB004_DECISION_MAKERS

**Document ID:** CASE-PUB-004-DM

**Title:** Decision Makers

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines who decides for every event.

---

# 2. Decision Makers

## 2.1 Data Events

### EV-001: New Information Appears

**Decision Maker:** Parser

**Reason:** Parser detects new data from DSO.

**Evidence:** Parser is the only component that retrieves external data.

---

### EV-002: Information Changes

**Decision Maker:** Parser

**Reason:** Parser detects data changes from DSO.

**Evidence:** Parser is the only component that detects data changes.

---

### EV-003: Information Disappears

**Decision Maker:** Parser

**Reason:** Parser detects data removal from DSO.

**Evidence:** Parser is the only component that detects data removal.

---

## 2.2 Publication Events

### EV-004: Publication Expires

**Decision Maker:** Lifecycle

**Reason:** Expiry is a temporal rule managed by Lifecycle.

**Evidence:** CASE-LC-001 — Lifecycle owns temporal rules.

---

### EV-005: Publication Becomes Obsolete

**Decision Maker:** Lifecycle

**Reason:** Obsolescence is determined by data comparison.

**Evidence:** CASE-LC-001 — Lifecycle detects information changes.

---

### EV-006: Publication Needs Update

**Decision Maker:** Lifecycle

**Reason:** Update need is determined by data comparison.

**Evidence:** CASE-LC-001 — Lifecycle detects update need.

---

## 2.3 Graph Events

### EV-007: Graph Changes

**Decision Maker:** Lifecycle

**Reason:** Graph change is a data change event.

**Evidence:** CASE-LC-001 — Lifecycle detects data changes.

---

### EV-008: Graph Becomes Available

**Decision Maker:** Lifecycle

**Reason:** Graph availability is determined by data presence.

**Evidence:** CASE-LC-001 — Lifecycle detects data availability.

---

### EV-009: Graph Expires

**Decision Maker:** Lifecycle

**Reason:** Graph expiry is a temporal rule.

**Evidence:** CASE-LC-001 — Lifecycle owns temporal rules.

---

## 2.4 Technical Events

### EV-010: Technical Message Changes

**Decision Maker:** System

**Reason:** Technical messages are system-generated.

**Evidence:** Architect Intent — technical messages are system content.

---

### EV-011: Service Announcement Published

**Decision Maker:** System

**Reason:** Service announcements are system-generated.

**Evidence:** Architect Intent — service announcements are system content.

---

## 2.5 Lifecycle Events

### EV-012: Reporting Period Ends

**Decision Maker:** Lifecycle

**Reason:** Reporting Period is a temporal boundary.

**Evidence:** GLOSSARY §2 — Reporting Period definition.

---

### EV-013: New Reporting Period Begins

**Decision Maker:** Lifecycle

**Reason:** New Reporting Period is a temporal boundary.

**Evidence:** GLOSSARY §2 — Reporting Period definition.

---

### EV-014: Publication State Change

**Decision Maker:** Lifecycle

**Reason:** State changes are lifecycle transitions.

**Evidence:** TELEGRAM_LIFECYCLE.md — lifecycle states.

---

## 2.6 Channel Events

### EV-015: Channel Becomes Available

**Decision Maker:** Adapter

**Reason:** Channel availability is channel-specific.

**Evidence:** CASE-TG-CORE-001 — channel operations.

---

### EV-016: Channel Becomes Unavailable

**Decision Maker:** Adapter

**Reason:** Channel unavailability is channel-specific.

**Evidence:** CASE-TG-CORE-001 — channel operations.

---

### EV-017: Channel Message Delivered

**Decision Maker:** Adapter

**Reason:** Message delivery is channel-specific.

**Evidence:** CASE-TG-CORE-001 — channel operations.

---

### EV-018: Channel Message Failed

**Decision Maker:** Adapter

**Reason:** Message failure is channel-specific.

**Evidence:** CASE-TG-CORE-001 — channel operations.

---

# 3. Decision Maker Summary

| Decision Maker | Events | Count |
|----------------|--------|-------|
| Parser | EV-001, EV-002, EV-003 | 3 |
| Lifecycle | EV-004, EV-005, EV-006, EV-007, EV-008, EV-009, EV-012, EV-013, EV-014 | 9 |
| System | EV-010, EV-011 | 2 |
| Adapter | EV-015, EV-016, EV-017, EV-018 | 4 |

---

# 4. Findings

## 4.1 Finding DM-001

**There are 4 decision makers.**

Parser, Lifecycle, System, Adapter.

**Evidence:** Analysis of decision makers.

**Confidence:** HIGH.

## 4.2 Finding DM-002

**Lifecycle is the PRIMARY decision maker.**

9 out of 18 events.

**Evidence:** Analysis of decision maker summary.

**Confidence:** HIGH.

## 4.3 Finding DM-003

**Publisher is NOT a decision maker.**

Publisher EXECUTES decisions, but does not MAKE them.

**Evidence:** Analysis of decision makers.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| DM-001 | Analysis of decision makers |
| DM-002 | Analysis of decision maker summary |
| DM-003 | Analysis of decision makers |

---

**End of Decision Makers**
