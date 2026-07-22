# PUB005_TRIGGERS

**Document ID:** CASE-PUB-005-TR

**Title:** Rule Triggers

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies trigger, condition, executor, affected object, result for every rule.

---

# 2. Rule Triggers

## 2.1 RULE-001: Publication Created on New Data

| Element | Description |
|---------|-------------|
| Trigger | Parser detects new data |
| Condition | Data is valid and complete |
| Executor | Publisher |
| Affected Object | Publication |
| Result | New Publication created |

---

## 2.2 RULE-002: Publication Updated on Data Change

| Element | Description |
|---------|-------------|
| Trigger | Parser detects data change |
| Condition | Publication exists and data changed |
| Executor | Publisher |
| Affected Object | Publication |
| Result | Publication updated |

---

## 2.3 RULE-003: Publication Replaced on Structure Change

| Element | Description |
|---------|-------------|
| Trigger | Parser detects structure change |
| Condition | Publication exists and structure changed significantly |
| Executor | Publisher |
| Affected Object | Publication |
| Result | Publication replaced |

---

## 2.4 RULE-004: Publication Removed on Data Disappearance

| Element | Description |
|---------|-------------|
| Trigger | Parser detects data disappearance |
| Condition | Publication exists and data no longer available |
| Executor | Publisher |
| Affected Object | Publication |
| Result | Publication removed |

---

## 2.5 RULE-005: Publication Archived at Period End

| Element | Description |
|---------|-------------|
| Trigger | Reporting Period ends |
| Condition | Publication is active |
| Executor | Publisher |
| Affected Object | Publication |
| Result | Publication archived |

---

## 2.6 RULE-006: Publication Preserved Permanently

| Element | Description |
|---------|-------------|
| Trigger | Publication archived |
| Condition | Publication is permanent type |
| Executor | System |
| Affected Object | Publication |
| Result | Publication preserved forever |

---

## 2.7 RULE-007: Tomorrow Publication Expires at Day End

| Element | Description |
|---------|-------------|
| Trigger | End of current day |
| Condition | Publication is tomorrow type |
| Executor | Lifecycle |
| Affected Object | Publication |
| Result | Publication expires |

---

## 2.8 RULE-008: Tomorrow Publication Disappears

| Element | Description |
|---------|-------------|
| Trigger | Publication expires |
| Condition | Publication is temporary |
| Executor | Publisher |
| Affected Object | Publication |
| Result | Publication removed (not archived) |

---

## 2.9 RULE-009: Graph Expires at Day End

| Element | Description |
|---------|-------------|
| Trigger | End of current day |
| Condition | Graph is active |
| Executor | Lifecycle |
| Affected Object | Graph |
| Result | Graph expires |

---

## 2.10 RULE-010: Graph Disappears

| Element | Description |
|---------|-------------|
| Trigger | Graph expires |
| Condition | Graph is temporary |
| Executor | Publisher |
| Affected Object | Graph |
| Result | Graph removed (not archived) |

---

## 2.11 RULE-011: Emergency Outage Does NOT Expire

| Element | Description |
|---------|-------------|
| Trigger | End of Reporting Period |
| Condition | Publication is emergency type |
| Executor | Lifecycle |
| Affected Object | Publication |
| Result | Publication archived (not expired) |

---

## 2.12 RULE-012: Technical Publication Does NOT Expire

| Element | Description |
|---------|-------------|
| Trigger | End of Reporting Period |
| Condition | Publication is technical type |
| Executor | Lifecycle |
| Affected Object | Publication |
| Result | Publication archived (not expired) |

---

## 2.13 RULE-013: Graph Replaced on Data Change

| Element | Description |
|---------|-------------|
| Trigger | Queue schedule data changes |
| Condition | Graph exists |
| Executor | Publisher |
| Affected Object | Graph |
| Result | Graph replaced entirely |

---

## 2.14 RULE-014: Graph Generated from Schedule Data

| Element | Description |
|---------|-------------|
| Trigger | Tomorrow's schedule available |
| Condition | Schedule data valid |
| Executor | Publisher/Adapter |
| Affected Object | Graph |
| Result | Graph generated |

---

## 2.15 RULE-015: Graph is Single Product

| Element | Description |
|---------|-------------|
| Trigger | Graph generation |
| Condition | Always |
| Executor | Publisher |
| Affected Object | Graph |
| Result | Single graph for all Territories |

---

## 2.16 RULE-016: Technical Message Updated In-Place

| Element | Description |
|---------|-------------|
| Trigger | System status changes |
| Condition | Technical message exists |
| Executor | Publisher |
| Affected Object | Technical Publication |
| Result | Message updated in place |

---

## 2.17 RULE-017: Technical Message Shows Latest Timestamp

| Element | Description |
|---------|-------------|
| Trigger | Technical message displayed |
| Condition | Always |
| Executor | Publisher |
| Affected Object | Technical Publication |
| Result | Latest timestamp shown |

---

## 2.18 RULE-018: Publications Grouped by Territory

| Element | Description |
|---------|-------------|
| Trigger | Publication generation |
| Condition | Publication is territory-based |
| Executor | Publisher |
| Affected Object | Publication |
| Result | Publication grouped by Territory |

---

## 2.19 RULE-019: Territory Order Follows Territorial Model

| Element | Description |
|---------|-------------|
| Trigger | Territory ordering |
| Condition | Always |
| Executor | Publisher |
| Affected Object | Publication order |
| Result | Territories ordered by model |

---

## 2.20 RULE-020: Emergency Before Planned

| Element | Description |
|---------|-------------|
| Trigger | Publication ordering |
| Condition | Both emergency and planned exist |
| Executor | Publisher |
| Affected Object | Publication order |
| Result | Emergency before Planned |

---

## 2.21 RULE-021: Telegram Message is Text

| Element | Description |
|---------|-------------|
| Trigger | Telegram publication |
| Condition | Always |
| Executor | Adapter |
| Affected Object | Telegram Message |
| Result | Text format |

---

## 2.22 RULE-022: Telegram Graph is Image

| Element | Description |
|---------|-------------|
| Trigger | Telegram graph publication |
| Condition | Always |
| Executor | Adapter |
| Affected Object | Telegram Graph |
| Result | Image format (PNG) |

---

## 2.23 RULE-023: Channel Message Edited In-Place

| Element | Description |
|---------|-------------|
| Trigger | Publication updated |
| Condition | Message exists on channel |
| Executor | Adapter |
| Affected Object | Channel Message |
| Result | Message edited |

---

## 2.24 RULE-024: Channel Message Deleted on Expiry

| Element | Description |
|---------|-------------|
| Trigger | Publication expires |
| Condition | Publication is temporary |
| Executor | Adapter |
| Affected Object | Channel Message |
| Result | Message deleted |

---

## 2.25 RULE-025: Publication Follows Lifecycle States

| Element | Description |
|---------|-------------|
| Trigger | Publication creation |
| Condition | Always |
| Executor | Lifecycle |
| Affected Object | Publication |
| Result | States: Generated → Published → Updated → Archived/Removed |

---

## 2.26 RULE-026: Archived Publication Cannot Be Removed

| Element | Description |
|---------|-------------|
| Trigger | Attempt to remove archived publication |
| Condition | Publication is archived |
| Executor | Lifecycle |
| Affected Object | Publication |
| Result | Removal blocked |

---

## 2.27 RULE-027: Temporary Publication Can Be Removed

| Element | Description |
|---------|-------------|
| Trigger | Publication expires |
| Condition | Publication is temporary |
| Executor | Lifecycle |
| Affected Object | Publication |
| Result | Removal allowed |

---

# 3. Findings

## 4.1 Finding TR-001

**All 27 rules have COMPLETE trigger chains.**

Trigger → Condition → Executor → Affected Object → Result.

**Evidence:** Analysis of rule triggers.

**Confidence:** HIGH.

## 4.2 Finding TR-002

**Lifecycle is the most common EXECUTOR for temporal rules.**

Rules 007, 009, 011, 012, 025, 026, 027.

**Evidence:** Analysis of rule triggers.

**Confidence:** HIGH.

## 4.3 Finding TR-003

**Publisher is the most common EXECUTOR for publishing rules.**

Rules 001, 002, 003, 004, 005, 013, 016, 018, 019, 020.

**Evidence:** Analysis of rule triggers.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| TR-001 | Analysis of rule triggers |
| TR-002 | Analysis of rule triggers |
| TR-003 | Analysis of rule triggers |

---

**End of Rule Triggers**
