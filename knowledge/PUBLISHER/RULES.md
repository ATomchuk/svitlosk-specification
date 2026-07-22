# Publisher Rules

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the business rules that govern Publisher behavior.

---

# Fundamental Rules

## RULE-001: Publication Never Modifies Official Information

**Statement:** Publication SHALL NOT modify the factual meaning of official information.

**Evidence:** GLOSSARY §3, CHARTER §7

---

## RULE-002: Publisher Executes Decisions

**Statement:** Publisher EXECUTES decisions but does NOT OWN business decisions.

**Evidence:** CASE-PUB-004, CASE-PUB-005

---

## RULE-003: Lifecycle Governs Temporal Behaviour

**Statement:** Lifecycle governs temporal behaviour, not Publisher.

**Evidence:** CASE-LC-001, CASE-PUB-004

---

## RULE-004: Emergency Publications Are Persistent

**Statement:** Emergency outage Publications are archived permanently.

**Evidence:** CASE-INFPROD-001, CASE-PUB-005

---

## RULE-005: Domains Are Independent

**Statement:** Queue Schedule, Planned Outages, and Emergency Outages are independent domains that MUST NOT be merged.

**Evidence:** CASE-SVT-ONTOLOGY-001, Architect Intent

---

# Publication Rules

## RULE-006: Publication Created on New Data

**Statement:** When new information appears, a Publication is created.

**Evidence:** CASE-PUB-005, CASE-TG-CORE-001

---

## RULE-007: Publication Updated on Data Change

**Statement:** When information changes, the existing Publication is updated.

**Evidence:** CASE-PUB-005, CASE-TG-CORE-001

---

## RULE-008: Publication Removed on Data Disappearance

**Statement:** When information disappears, the Publication is removed.

**Evidence:** CASE-PUB-005, CASE-TG-CORE-001

---

## RULE-009: Publication Archived at Period End

**Statement:** When Reporting Period ends, Publications are archived.

**Evidence:** CASE-PUB-005, TELEGRAM_LIFECYCLE.md

---

## RULE-010: Archived Publications Preserved Permanently

**Statement:** Archived Publications are preserved permanently.

**Evidence:** CASE-PUB-005, TELEGRAM_LIFECYCLE.md

---

# Temporal Rules

## RULE-011: Temporary Publications Expire

**Statement:** Temporary Publications expire at the end of their validity period.

**Evidence:** CASE-PUB-005, CASE-INFPROD-001

---

## RULE-012: Tomorrow Publications Disappear

**Statement:** Tomorrow's planned outage Publications disappear at end of current day.

**Evidence:** CASE-INFPROD-001, Architect Intent

---

## RULE-013: Emergency Outages Do NOT Expire

**Statement:** Emergency outage Publications do NOT expire.

**Evidence:** CASE-INFPROD-001, CASE-PUB-005

---

# Territorial Rules

## RULE-014: Publications Grouped by Territory

**Statement:** Publications are grouped by Territory.

**Evidence:** CASE-INFPROD-001, CASE-TG-CORE-001

---

## RULE-015: Territory Order Follows Model

**Statement:** Territory order follows the Territorial Model hierarchy.

**Evidence:** CASE-TG-CORE-001, TERRITORIAL_MODEL.md

---

# Channel Rules

## RULE-016: Publisher Distributes Through Adapters

**Statement:** Publisher distributes Publications through channel Adapters.

**Evidence:** CASE-PUB-002, CASE-SVT-ONTOLOGY-001

---

## RULE-017: Adapters Are Channel-Specific

**Statement:** Adapters handle channel-specific concerns.

**Evidence:** CASE-SVT-ONTOLOGY-001, CASE-TG-CORE-001

---

# Rule Count

| Category | Rules | Count |
|----------|-------|-------|
| Fundamental | 001-005 | 5 |
| Publication | 006-010 | 5 |
| Temporal | 011-013 | 3 |
| Territorial | 014-015 | 2 |
| Channel | 016-017 | 2 |
| **Total** | | **17** |

---

# Evidence

| Rule | Source |
|------|--------|
| RULE-001 | GLOSSARY §3, CHARTER §7 |
| RULE-002 | CASE-PUB-004, CASE-PUB-005 |
| RULE-003 | CASE-LC-001, CASE-PUB-004 |
| RULE-004 | CASE-INFPROD-001, CASE-PUB-005 |
| RULE-005 | CASE-SVT-ONTOLOGY-001, Architect Intent |
| RULE-006 | CASE-PUB-005, CASE-TG-CORE-001 |
| RULE-007 | CASE-PUB-005, CASE-TG-CORE-001 |
| RULE-008 | CASE-PUB-005, CASE-TG-CORE-001 |
| RULE-009 | CASE-PUB-005, TELEGRAM_LIFECYCLE.md |
| RULE-010 | CASE-PUB-005, TELEGRAM_LIFECYCLE.md |
| RULE-011 | CASE-PUB-005, CASE-INFPROD-001 |
| RULE-012 | CASE-INFPROD-001, Architect Intent |
| RULE-013 | CASE-INFPROD-001, CASE-PUB-005 |
| RULE-014 | CASE-INFPROD-001, CASE-TG-CORE-001 |
| RULE-015 | CASE-TG-CORE-001, TERRITORIAL_MODEL.md |
| RULE-016 | CASE-PUB-002, CASE-SVT-ONTOLOGY-001 |
| RULE-017 | CASE-SVT-ONTOLOGY-001, CASE-TG-CORE-001 |

---

**End of Rules**
