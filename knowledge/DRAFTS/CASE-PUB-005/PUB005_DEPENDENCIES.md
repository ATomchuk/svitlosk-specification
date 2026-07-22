# PUB005_DEPENDENCIES

**Document ID:** CASE-PUB-005-DE

**Title:** Rule Dependencies

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document builds the rule dependency graph.

---

# 2. Rule Dependencies

## 2.1 Root Rules

Rules with NO upstream dependencies:

| Rule | Description |
|------|-------------|
| RULE-001 | Publication Created on New Data |
| RULE-007 | Tomorrow Publication Expires at Day End |
| RULE-011 | Emergency Outage Does NOT Expire |
| RULE-014 | Graph Generated from Schedule Data |
| RULE-018 | Publications Grouped by Territory |
| RULE-021 | Telegram Message is Text |

---

## 2.2 Dependent Rules

| Rule | Depends On | Relationship |
|------|------------|--------------|
| RULE-002 | RULE-001 | Update requires creation first |
| RULE-003 | RULE-001 | Replace requires creation first |
| RULE-004 | RULE-001 | Remove requires creation first |
| RULE-005 | RULE-001 | Archive requires creation first |
| RULE-006 | RULE-005 | Preservation requires archival first |
| RULE-008 | RULE-007 | Disappearance requires expiry first |
| RULE-009 | RULE-007 | Graph expiry follows same pattern |
| RULE-010 | RULE-009 | Graph disappearance requires expiry first |
| RULE-012 | RULE-011 | Technical follows emergency pattern |
| RULE-013 | RULE-014 | Replace requires generation first |
| RULE-015 | RULE-014 | Single product requires generation first |
| RULE-016 | RULE-002 | Update in-place requires update |
| RULE-017 | RULE-016 | Latest timestamp requires update |
| RULE-019 | RULE-018 | Territory order requires grouping |
| RULE-020 | RULE-018 | Emergency before planned requires grouping |
| RULE-022 | RULE-021 | Image follows text pattern |
| RULE-023 | RULE-002 | Edit requires update |
| RULE-024 | RULE-007 | Delete requires expiry |
| RULE-025 | RULE-001 | Lifecycle requires creation |
| RULE-026 | RULE-025 | Archived protection requires lifecycle |
| RULE-027 | RULE-025 | Temporary removal requires lifecycle |

---

# 3. Dependency Graph

```
                    ┌─────────────┐
                    │  RULE-001   │
                    │ (Creation)  │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  RULE-002   │ │  RULE-003   │ │  RULE-004   │
    │  (Update)   │ │ (Replace)   │ │  (Remove)   │
    └──────┬──────┘ └─────────────┘ └─────────────┘
           │
           ▼
    ┌─────────────┐
    │  RULE-005   │
    │  (Archive)  │
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │  RULE-006   │
    │(Preserve)   │
    └─────────────┘

                    ┌─────────────┐
                    │  RULE-007   │
                    │ (Expiry)    │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  RULE-008   │ │  RULE-009   │ │  RULE-024   │
    │(Disappear)  │ │(Graph Exp.) │ │(Delete)     │
    └─────────────┘ └──────┬──────┘ └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  RULE-010   │
                    │(Graph Disp.)│
                    └─────────────┘

                    ┌─────────────┐
                    │  RULE-014   │
                    │ (Generate)  │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  RULE-013   │ │  RULE-015   │ │  RULE-022   │
    │ (Replace)   │ │ (Single)    │ │ (Image)     │
    └─────────────┘ └─────────────┘ └─────────────┘
```

---

# 4. Dependency Analysis

## 4.1 Root Rules

| Rule | Description | Why Root |
|------|-------------|----------|
| RULE-001 | Creation | Foundation of all publication rules |
| RULE-007 | Expiry | Foundation of all temporal rules |
| RULE-011 | Emergency Permanent | Foundation of permanent rules |
| RULE-014 | Graph Generation | Foundation of graph rules |
| RULE-018 | Territory Grouping | Foundation of ordering rules |
| RULE-021 | Text Format | Foundation of channel rules |

## 4.2 Leaf Rules

| Rule | Description | Why Leaf |
|------|-------------|----------|
| RULE-006 | Preserve Permanently | Terminal archival |
| RULE-010 | Graph Disappear | Terminal graph |
| RULE-017 | Latest Timestamp | Terminal technical |
| RULE-020 | Emergency Before Planned | Terminal ordering |
| RULE-022 | Graph Image | Terminal channel |
| RULE-026 | Archived Protection | Terminal lifecycle |

---

# 5. Findings

## 5.1 Finding DE-001

**6 root rules exist.**

RULE-001, RULE-007, RULE-011, RULE-014, RULE-018, RULE-021.

**Evidence:** Analysis of dependency graph.

**Confidence:** HIGH.

## 5.2 Finding DE-002

**6 leaf rules exist.**

RULE-006, RULE-010, RULE-017, RULE-020, RULE-022, RULE-026.

**Evidence:** Analysis of dependency graph.

**Confidence:** HIGH.

## 5.3 Finding DE-003

**RULE-001 (Creation) is the MOST DEPENDED-ON rule.**

12 rules depend on it.

**Evidence:** Analysis of dependency graph.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| DE-001 | Analysis of dependency graph |
| DE-002 | Analysis of dependency graph |
| DE-003 | Analysis of dependency graph |

---

**End of Rule Dependencies**
