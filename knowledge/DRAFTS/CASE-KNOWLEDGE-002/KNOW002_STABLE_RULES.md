# KNOW002_STABLE_RULES

**Document ID:** CASE-KNOWLEDGE-002-SR

**Title:** Stable Rules

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document extracts business rules that appear stable.

---

# 2. Stable Rules

## 2.1 Fundamental Rules

### RULE-001: Publication never modifies official information

**Evidence:** GLOSSARY §3, CHARTER §7

**Confidence:** HIGH

---

### RULE-002: Publisher executes decisions but does not own business decisions

**Evidence:** CASE-PUB-004, CASE-PUB-005

**Confidence:** HIGH

---

### RULE-003: Lifecycle governs temporal behaviour

**Evidence:** CASE-LC-001, CASE-PUB-004

**Confidence:** HIGH

---

### RULE-004: Emergency publications are persistent

**Evidence:** CASE-INFPROD-001, CASE-PUB-005

**Confidence:** HIGH

---

### RULE-005: Domains are independent

**Evidence:** CASE-SVT-ONTOLOGY-001, Architect Intent

**Confidence:** HIGH

---

## 2.2 Publication Rules

### RULE-006: Publication is created when new information appears

**Evidence:** CASE-PUB-005, CASE-TG-CORE-001

**Confidence:** HIGH

---

### RULE-007: Publication is updated when information changes

**Evidence:** CASE-PUB-005, CASE-TG-CORE-001

**Confidence:** HIGH

---

### RULE-008: Publication is removed when information disappears

**Evidence:** CASE-PUB-005, CASE-TG-CORE-001

**Confidence:** HIGH

---

### RULE-009: Publication is archived at period end

**Evidence:** CASE-PUB-005, TELEGRAM_LIFECYCLE.md

**Confidence:** HIGH

---

### RULE-010: Archived publications are preserved permanently

**Evidence:** CASE-PUB-005, TELEGRAM_LIFECYCLE.md

**Confidence:** HIGH

---

## 2.3 Temporal Rules

### RULE-011: Temporary publications expire at end of validity period

**Evidence:** CASE-PUB-005, CASE-INFPROD-001

**Confidence:** HIGH

---

### RULE-012: Tomorrow publications disappear at end of day

**Evidence:** CASE-INFPROD-001, Architect Intent

**Confidence:** HIGH

---

### RULE-013: Emergency outages do NOT expire

**Evidence:** CASE-INFPROD-001, CASE-PUB-005

**Confidence:** HIGH

---

## 2.4 Territorial Rules

### RULE-014: Publications are grouped by Territory

**Evidence:** CASE-INFPROD-001, CASE-TG-CORE-001

**Confidence:** HIGH

---

### RULE-015: Territory order follows Territorial Model

**Evidence:** CASE-TG-CORE-001, TERRITORIAL_MODEL.md

**Confidence:** HIGH

---

## 2.5 Channel Rules

### RULE-016: Publisher distributes through Adapters

**Evidence:** CASE-PUB-002, CASE-SVT-ONTOLOGY-001

**Confidence:** HIGH

---

### RULE-017: Adapters are channel-specific

**Evidence:** CASE-SVT-ONTOLOGY-001, CASE-TG-CORE-001

**Confidence:** HIGH

---

# 3. Stable Rules Summary

| Category | Rules | Count |
|----------|-------|-------|
| Fundamental | 001-005 | 5 |
| Publication | 006-010 | 5 |
| Temporal | 011-013 | 3 |
| Territorial | 014-015 | 2 |
| Channel | 016-017 | 2 |
| **Total** | | **17** |

---

# 4. Findings

## 4.1 Finding ST-001

**17 stable rules identified.**

Across 5 categories.

**Evidence:** Analysis of stable rules.

**Confidence:** HIGH.

## 4.2 Finding ST-002

**Fundamental and Publication rules are MOST stable.**

10 rules with HIGH confidence.

**Evidence:** Analysis of rules summary.

**Confidence:** HIGH.

## 4.3 Finding ST-003

**All rules have STRONG evidence.**

Each traces to multiple investigations or canonical documents.

**Evidence:** Analysis of stable rules.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| ST-001 | Analysis of stable rules |
| ST-002 | Analysis of rules summary |
| ST-003 | Analysis of stable rules |

---

**End of Stable Rules**
