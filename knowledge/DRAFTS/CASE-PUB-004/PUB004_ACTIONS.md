# PUB004_ACTIONS

**Document ID:** CASE-PUB-004-AC

**Title:** Action Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines what action follows every decision.

---

# 2. Action Inventory

## 2.1 Data Events

### EV-001: New Information Appears

**Action:** Create Publication

**Executor:** Publisher

**Evidence:** New data requires new publication.

---

### EV-002: Information Changes

**Action:** Update Publication

**Executor:** Publisher

**Evidence:** Changed data requires publication update.

---

### EV-003: Information Disappears

**Action:** Remove Publication

**Executor:** Publisher

**Evidence:** Removed data requires publication removal.

---

## 2.2 Publication Events

### EV-004: Publication Expires

**Action:** Remove Publication

**Executor:** Publisher

**Evidence:** Expired publications are removed.

---

### EV-005: Publication Becomes Obsolete

**Action:** Replace Publication

**Executor:** Publisher

**Evidence:** Obsolete publications are replaced.

---

### EV-006: Publication Needs Update

**Action:** Update Publication

**Executor:** Publisher

**Evidence:** Publications needing update are updated.

---

## 2.3 Graph Events

### EV-007: Graph Changes

**Action:** Replace Graph

**Executor:** Publisher

**Evidence:** Changed graphs are replaced entirely.

---

### EV-008: Graph Becomes Available

**Action:** Create Graph

**Executor:** Publisher

**Evidence:** New graphs are created.

---

### EV-009: Graph Expires

**Action:** Remove Graph

**Executor:** Publisher

**Evidence:** Expired graphs are removed.

---

## 2.4 Technical Events

### EV-010: Technical Message Changes

**Action:** Update Technical Message

**Executor:** Publisher

**Evidence:** Changed technical messages are updated.

---

### EV-011: Service Announcement Published

**Action:** Create Service Message

**Executor:** Publisher

**Evidence:** New service announcements are created.

---

## 2.5 Lifecycle Events

### EV-012: Reporting Period Ends

**Action:** Archive Publications

**Executor:** Publisher

**Evidence:** End of period triggers archival.

---

### EV-013: New Reporting Period Begins

**Action:** Create Journal Edition

**Executor:** Publisher

**Evidence:** New period triggers new edition.

---

### EV-014: Publication State Change

**Action:** Transition Publication State

**Executor:** Publisher

**Evidence:** State changes trigger transitions.

---

## 2.6 Channel Events

### EV-015: Channel Becomes Available

**Action:** Resume Distribution

**Executor:** Adapter

**Evidence:** Channel availability triggers distribution.

---

### EV-016: Channel Becomes Unavailable

**Action:** Pause Distribution

**Executor:** Adapter

**Evidence:** Channel unavailability pauses distribution.

---

### EV-017: Channel Message Delivered

**Action:** Record Delivery

**Executor:** Adapter

**Evidence:** Successful delivery is recorded.

---

### EV-018: Channel Message Failed

**Action:** Retry Delivery

**Executor:** Adapter

**Evidence:** Failed delivery triggers retry.

---

# 3. Action Classification

| Action | Count | Executor |
|--------|-------|----------|
| Create Publication | 1 | Publisher |
| Update Publication | 2 | Publisher |
| Remove Publication | 2 | Publisher |
| Replace Publication | 1 | Publisher |
| Replace Graph | 1 | Publisher |
| Create Graph | 1 | Publisher |
| Remove Graph | 1 | Publisher |
| Update Technical Message | 1 | Publisher |
| Create Service Message | 1 | Publisher |
| Archive Publications | 1 | Publisher |
| Create Journal Edition | 1 | Publisher |
| Transition Publication State | 1 | Publisher |
| Resume Distribution | 1 | Adapter |
| Pause Distribution | 1 | Adapter |
| Record Delivery | 1 | Adapter |
| Retry Delivery | 1 | Adapter |

---

# 4. Findings

## 4.1 Finding AC-001

**There are 16 actions.**

Across 2 executors: Publisher (14), Adapter (2).

**Evidence:** Analysis of action inventory.

**Confidence:** HIGH.

## 4.2 Finding AC-002

**Publisher executes MOST actions.**

14 out of 16.

**Evidence:** Analysis of action classification.

**Confidence:** HIGH.

## 4.3 Finding AC-003

**Adapter executes ONLY channel-specific actions.**

Resume, Pause, Record, Retry.

**Evidence:** Analysis of action classification.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| AC-001 | Analysis of action inventory |
| AC-002 | Analysis of action classification |
| AC-003 | Analysis of action classification |

---

**End of Action Inventory**
