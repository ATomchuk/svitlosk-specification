# PUB005_CLASSIFICATION

**Document ID:** CASE-PUB-005-CL

**Title:** Rule Classification

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document classifies rules into categories.

---

# 2. Rule Classification

## 2.1 Business Rules

Rules that define WHAT should happen from a business perspective.

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-001 | Publication Created on New Data | CASE-TG-CORE-001 |
| RULE-002 | Publication Updated on Data Change | TELEGRAM_LIFECYCLE.md |
| RULE-003 | Publication Replaced on Structure Change | TELEGRAM_LIFECYCLE.md |
| RULE-004 | Publication Removed on Data Disappearance | CASE-TG-CORE-001 |
| RULE-018 | Publications Grouped by Territory | Architect Intent |
| RULE-020 | Emergency Before Planned | Architect Intent |

---

## 2.2 Temporal Rules

Rules that depend on TIME.

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-007 | Tomorrow Publication Expires at Day End | Architect Intent |
| RULE-008 | Tomorrow Publication Disappears | Architect Intent |
| RULE-009 | Graph Expires at Day End | Architect Intent |
| RULE-010 | Graph Disappears | Architect Intent |
| RULE-011 | Emergency Outage Does NOT Expire | TELEGRAM_EDITORIAL |
| RULE-012 | Technical Publication Does NOT Expire | Architect Intent |

---

## 2.3 Publishing Rules

Rules that define how publications are created and maintained.

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-005 | Publication Archived at Period End | TELEGRAM_LIFECYCLE.md |
| RULE-006 | Publication Preserved Permanently | TELEGRAM_LIFECYCLE.md |
| RULE-013 | Graph Replaced on Data Change | CASE-TG-CORE-001 |
| RULE-014 | Graph Generated from Schedule Data | Architect Context |
| RULE-016 | Technical Message Updated In-Place | CASE-TG-CORE-001 |
| RULE-017 | Technical Message Shows Latest Timestamp | Architect Intent |

---

## 2.4 Channel Rules

Rules that depend on CHANNEL.

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-021 | Telegram Message is Text | TELEGRAM_PUB |
| RULE-022 | Telegram Graph is Image | Architect Context |
| RULE-023 | Channel Message Edited In-Place | TELEGRAM_LIFECYCLE.md |
| RULE-024 | Channel Message Deleted on Expiry | TELEGRAM_LIFECYCLE.md |

---

## 2.5 Formatting Rules

Rules that define how information is presented.

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-019 | Territory Order Follows Territorial Model | TERRITORIAL_MODEL.md |
| RULE-015 | Graph is Single Product | CASE-INFPROD-001 |

---

## 2.6 Archive Rules

Rules that define how information is preserved.

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-005 | Publication Archived at Period End | TELEGRAM_LIFECYCLE.md |
| RULE-006 | Publication Preserved Permanently | TELEGRAM_LIFECYCLE.md |
| RULE-011 | Emergency Outage Does NOT Expire | TELEGRAM_EDITORIAL |
| RULE-012 | Technical Publication Does NOT Expire | Architect Intent |

---

## 2.7 Lifecycle Rules

Rules that define lifecycle behavior.

| Rule | Description | Evidence |
|------|-------------|----------|
| RULE-025 | Publication Follows Lifecycle States | TELEGRAM_LIFECYCLE.md |
| RULE-026 | Archived Publication Cannot Be Removed | TELEGRAM_LIFECYCLE.md |
| RULE-027 | Temporary Publication Can Be Removed | TELEGRAM_LIFECYCLE.md |

---

# 3. Classification Summary

| Category | Rules | Count |
|----------|-------|-------|
| Business | 001, 002, 003, 004, 018, 020 | 6 |
| Temporal | 007, 008, 009, 010, 011, 012 | 6 |
| Publishing | 005, 006, 013, 014, 016, 017 | 6 |
| Channel | 021, 022, 023, 024 | 4 |
| Formatting | 015, 019 | 2 |
| Archive | 005, 006, 011, 012 | 4 |
| Lifecycle | 025, 026, 027 | 3 |

---

# 4. Findings

## 4.1 Finding CL-001

**Rules classified into 7 categories.**

Business, Temporal, Publishing, Channel, Formatting, Archive, Lifecycle.

**Evidence:** Analysis of rule classification.

**Confidence:** HIGH.

## 4.2 Finding CL-002

**Business, Temporal, and Publishing are LARGEST categories.**

6 rules each.

**Evidence:** Analysis of classification summary.

**Confidence:** HIGH.

## 4.3 Finding CL-003

**Some rules belong to MULTIPLE categories.**

RULE-005 and RULE-006 are both Publishing and Archive.

**Evidence:** Analysis of classification.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| CL-001 | Analysis of rule classification |
| CL-002 | Analysis of classification summary |
| CL-003 | Analysis of classification |

---

**End of Rule Classification**
