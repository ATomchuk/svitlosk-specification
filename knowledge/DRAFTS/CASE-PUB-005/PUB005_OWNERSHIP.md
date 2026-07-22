# PUB005_OWNERSHIP

**Document ID:** CASE-PUB-005-OW

**Title:** Rule Ownership

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines who owns each rule.

---

# 2. Rule Ownership

## 2.1 Parser-Owned Rules

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-001 | Publication Created on New Data | Parser detects new data |
| RULE-002 | Publication Updated on Data Change | Parser detects data change |
| RULE-003 | Publication Replaced on Structure Change | Parser detects structure change |
| RULE-004 | Publication Removed on Data Disappearance | Parser detects data disappearance |

---

## 2.2 Lifecycle-Owned Rules

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-007 | Tomorrow Publication Expires at Day End | Temporal rule |
| RULE-009 | Graph Expires at Day End | Temporal rule |
| RULE-011 | Emergency Outage Does NOT Expire | Temporal rule |
| RULE-012 | Technical Publication Does NOT Expire | Temporal rule |
| RULE-025 | Publication Follows Lifecycle States | Lifecycle rule |
| RULE-026 | Archived Publication Cannot Be Removed | Lifecycle rule |
| RULE-027 | Temporary Publication Can Be Removed | Lifecycle rule |

---

## 2.3 Publisher-Owned Rules

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-005 | Publication Archived at Period End | Publisher executes |
| RULE-006 | Publication Preserved Permanently | Publisher executes |
| RULE-008 | Tomorrow Publication Disappears | Publisher executes |
| RULE-010 | Graph Disappears | Publisher executes |
| RULE-013 | Graph Replaced on Data Change | Publisher executes |
| RULE-014 | Graph Generated from Schedule Data | Publisher executes |
| RULE-015 | Graph is Single Product | Publisher executes |
| RULE-016 | Technical Message Updated In-Place | Publisher executes |
| RULE-017 | Technical Message Shows Latest Timestamp | Publisher executes |
| RULE-018 | Publications Grouped by Territory | Publisher executes |
| RULE-019 | Territory Order Follows Territorial Model | Publisher executes |
| RULE-020 | Emergency Before Planned | Publisher executes |

---

## 2.4 Adapter-Owned Rules

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-021 | Telegram Message is Text | Channel-specific |
| RULE-022 | Telegram Graph is Image | Channel-specific |
| RULE-023 | Channel Message Edited In-Place | Channel-specific |
| RULE-024 | Channel Message Deleted on Expiry | Channel-specific |

---

## 2.5 System-Owned Rules

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-006 | Publication Preserved Permanently | System ensures persistence |

---

## 2.6 Community-Owned Rules

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-018 | Publications Grouped by Territory | Community structure |
| RULE-019 | Territory Order Follows Territorial Model | Community structure |

---

## 2.7 Time-Owned Rules

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-007 | Tomorrow Publication Expires at Day End | Time trigger |
| RULE-009 | Graph Expires at Day End | Time trigger |
| RULE-011 | Emergency Outage Does NOT Expire | Time trigger |
| RULE-012 | Technical Publication Does NOT Expire | Time trigger |

---

## 2.8 Ambiguous Ownership

| Rule | Description | Ambiguity |
|------|-------------|-----------|
| RULE-005 | Publication Archived at Period End | Publisher executes, but Lifecycle decides |
| RULE-013 | Graph Replaced on Data Change | Publisher executes, but Lifecycle decides |
| RULE-025 | Publication Follows Lifecycle States | Lifecycle defines, Publisher executes |

---

# 3. Ownership Summary

| Owner | Rules | Count |
|-------|-------|-------|
| Parser | 001, 002, 003, 004 | 4 |
| Lifecycle | 007, 009, 011, 012, 025, 026, 027 | 7 |
| Publisher | 005, 006, 008, 010, 013, 014, 015, 016, 017, 018, 019, 020 | 12 |
| Adapter | 021, 022, 023, 024 | 4 |
| System | 006 | 1 |
| Community | 018, 019 | 2 |
| Time | 007, 009, 011, 012 | 4 |

---

# 4. Findings

## 4.1 Finding OW-001

**7 owners identified.**

Parser, Lifecycle, Publisher, Adapter, System, Community, Time.

**Evidence:** Analysis of rule ownership.

**Confidence:** HIGH.

## 4.2 Finding OW-002

**Publisher has MOST ownership.**

12 out of 27 rules.

**Evidence:** Analysis of ownership summary.

**Confidence:** HIGH.

## 4.3 Finding OW-003

**3 rules have AMBIGUOUS ownership.**

RULE-005, RULE-013, RULE-025.

**Evidence:** Analysis of ambiguous ownership.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OW-001 | Analysis of rule ownership |
| OW-002 | Analysis of ownership summary |
| OW-003 | Analysis of ambiguous ownership |

---

**End of Rule Ownership**
