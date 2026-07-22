# PUB005_RULE_INVENTORY

**Document ID:** CASE-PUB-005-RI

**Title:** Rule Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document lists every business rule that currently exists.

---

# 2. Rule Inventory

## 2.1 Publication Rules

### RULE-001: Publication Created on New Data

**Rule:** When new information appears, a Publication is created.

**Evidence:** CASE-TG-CORE-001 — OP-007, OP-008, OP-009, OP-011, OP-012

---

### RULE-002: Publication Updated on Data Change

**Rule:** When information changes, the existing Publication is updated.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md §6.2

---

### RULE-003: Publication Replaced on Structure Change

**Rule:** When information structure changes significantly, the Publication is replaced.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md §6.2

---

### RULE-004: Publication Removed on Data Disappearance

**Rule:** When information disappears, the Publication is removed.

**Evidence:** CASE-TG-CORE-001 — OP-021

---

### RULE-005: Publication Archived at Period End

**Rule:** When Reporting Period ends, Publications are archived.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md §6.3

---

### RULE-006: Publication Preserved Permanently

**Rule:** Archived Publications are preserved permanently.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md §6.3

---

## 2.2 Temporal Rules

### RULE-007: Tomorrow Publication Expires at Day End

**Rule:** Tomorrow's planned outage Publication expires at end of current day.

**Evidence:** Architect Intent — "tomorrow information disappears automatically"

---

### RULE-008: Tomorrow Publication Disappears

**Rule:** Tomorrow's planned outage Publication is removed, not archived.

**Evidence:** Architect Intent — "disappears automatically"

---

### RULE-009: Graph Expires at Day End

**Rule:** Tomorrow's queue graph expires at end of current day.

**Evidence:** Architect Intent — temporary nature

---

### RULE-010: Graph Disappears

**Rule:** Tomorrow's queue graph is removed, not archived.

**Evidence:** Architect Intent — temporary nature

---

### RULE-011: Emergency Outage Does NOT Expire

**Rule:** Emergency outage Publications do NOT expire.

**Evidence:** TELEGRAM_EDITORIAL — permanent record

---

### RULE-012: Technical Publication Does NOT Expire

**Rule:** Technical Publications do NOT expire.

**Evidence:** Architect Intent — permanent record

---

## 2.3 Graph Rules

### RULE-013: Graph Replaced on Data Change

**Rule:** When queue schedule data changes, the graph is replaced entirely.

**Evidence:** CASE-TG-CORE-001 — OP-010

---

### RULE-014: Graph Generated from Schedule Data

**Rule:** Graph is generated from queue schedule data.

**Evidence:** Architect Context — "Graph Generator → SVG → PNG"

---

### RULE-015: Graph is Single Product

**Rule:** Graph is a SINGLE product for all Territories.

**Evidence:** CASE-INFPROD-001 — Queue Graph is not territory-organized

---

## 2.4 Technical Rules

### RULE-016: Technical Message Updated In-Place

**Rule:** Technical messages are updated in place.

**Evidence:** CASE-TG-CORE-001 — technical message behavior

---

### RULE-017: Technical Message Shows Latest Timestamp

**Rule:** Technical messages always show latest update timestamp.

**Evidence:** Architect Intent — technical publication behavior

---

## 2.5 Ordering Rules

### RULE-018: Publications Grouped by Territory

**Rule:** Publications are grouped by Starosta District.

**Evidence:** Architect Intent — "Journal publications are grouped by Starosta Districts"

---

### RULE-019: Territory Order Follows Territorial Model

**Rule:** Territory order follows the Territorial Model hierarchy.

**Evidence:** TERRITORIAL_MODEL.md

---

### RULE-020: Emergency Before Planned

**Rule:** Emergency Publications appear before Planned Publications.

**Evidence:** Architect Intent — emergency outages are more urgent

---

## 2.6 Channel Rules

### RULE-021: Telegram Message is Text

**Rule:** Telegram messages are text-based.

**Evidence:** TELEGRAM_PUB — Telegram message format

---

### RULE-022: Telegram Graph is Image

**Rule:** Telegram graphs are image-based (PNG).

**Evidence:** Architect Context — "SVG → PNG"

---

### RULE-023: Channel Message Edited In-Place

**Rule:** Channel messages are edited in place when updated.

**Evidence:** TELEGRAM_LIFECYCLE.md §5.2

---

### RULE-024: Channel Message Deleted on Expiry

**Rule:** Channel messages are deleted when expired.

**Evidence:** TELEGRAM_LIFECYCLE.md §5.5

---

## 2.7 Lifecycle Rules

### RULE-025: Publication Follows Lifecycle States

**Rule:** Publications pass through Generated → Published → Updated → Archived/Removed.

**Evidence:** TELEGRAM_LIFECYCLE.md §4

---

### RULE-026: Archived Publication Cannot Be Removed

**Rule:** Archived Publications cannot be removed.

**Evidence:** TELEGRAM_LIFECYCLE.md §5.6

---

### RULE-027: Temporary Publication Can Be Removed

**Rule:** Only temporary Publications can be removed.

**Evidence:** TELEGRAM_LIFECYCLE.md §5.5

---

# 3. Rule Count

| Category | Count |
|----------|-------|
| Publication Rules | 6 |
| Temporal Rules | 6 |
| Graph Rules | 3 |
| Technical Rules | 2 |
| Ordering Rules | 3 |
| Channel Rules | 4 |
| Lifecycle Rules | 3 |
| **Total** | **27** |

---

# 4. Findings

## 4.1 Finding RI-001

**There are 27 business rules.**

Across 7 categories.

**Evidence:** Analysis of all sources.

**Confidence:** HIGH.

## 4.2 Finding RI-002

**Temporal rules are the LARGEST category.**

6 rules related to time-based behavior.

**Evidence:** Analysis of rule inventory.

**Confidence:** HIGH.

## 4.3 Finding RI-003

**Some rules are UNDOCUMENTED.**

Rules 018-020 (ordering) are implicit, not documented.

**Evidence:** Analysis of rule inventory.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| RI-001 | Analysis of all sources |
| RI-002 | Analysis of rule inventory |
| RI-003 | Analysis of rule inventory |

---

**End of Rule Inventory**
