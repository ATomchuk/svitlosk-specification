# PUB003_AMBIGUITIES

**Document ID:** CASE-PUB-003-AM

**Title:** Ambiguities

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document finds ambiguous words.

---

# 2. Ambiguity Analysis

## 2.1 Publisher

### Ambiguity

Publisher can mean:
1. Logical Role (GLOSSARY)
2. Software Component (Publication Engine)
3. Human role (traditional publishing)

### Current Usage

Primarily used as Logical Role.

### Risk

May be confused with human Publisher.

### Severity

MEDIUM

---

## 2.2 Publication

### Ambiguity

Publication can mean:
1. Information message (GLOSSARY)
2. Information Product (CASE-INFPROD-001)
3. Channel-specific output (Telegram Post)
4. Act of publishing (process)

### Current Usage

Primarily used as information message.

### Risk

May be confused with Information Product or channel output.

### Severity

HIGH

---

## 2.3 Edition

### Ambiguity

Edition can mean:
1. Daily instance of Journal
2. Version of a document
3. Print run (traditional publishing)

### Current Usage

Used in Architect Intent for daily instance.

### Risk

May be confused with version or print run.

### Severity

MEDIUM

---

## 2.4 Issue

### Ambiguity

Issue can mean:
1. Daily instance of Journal (TELEGRAM_LIFECYCLE)
2. Problem or concern
3. Publication number (magazine)

### Current Usage

Used in Telegram lifecycle for daily instance.

### Risk

May be confused with problem or publication number.

### Severity

MEDIUM

---

## 2.5 Release

### Ambiguity

Release can mean:
1. Daily instance of Journal (CASE-PUB-001)
2. Software version release
3. Public disclosure

### Current Usage

Used in CASE-PUB-001 for daily instance.

### Risk

May be confused with software release.

### Severity

MEDIUM

---

## 2.6 Graph

### Ambiguity

Graph can mean:
1. Visual chart (Queue Graph)
2. Data structure (graph theory)
3. Plot (statistical)

### Current Usage

Used for visual chart of queue schedule.

### Risk

May be confused with data structure.

### Severity

LOW

---

## 2.7 Notification

### Ambiguity

Notification can mean:
1. Push notification (PWA)
2. General alert
3. Official notice

### Current Usage

Used for push notifications in PWA.

### Risk

May be confused with general alerts.

### Severity

LOW

---

## 2.8 Product

### Ambiguity

Product can mean:
1. Information Product (CASE-INFPROD-001)
2. Software product
3. Business product

### Current Usage

Used for information products.

### Risk

May be confused with software or business products.

### Severity

LOW

---

## 2.9 Information

### Ambiguity

Information can mean:
1. Factual content (information domain)
2. Data (technical)
3. Knowledge (interpreted)

### Current Usage

Used for factual content from DSO.

### Risk

May be confused with data or knowledge.

### Severity

MEDIUM

---

## 2.10 Message

### Ambiguity

Message can mean:
1. Telegram message (channel-specific)
2. Information message (general)
3. Communication (general)

### Current Usage

Used for Telegram-specific output.

### Risk

May be confused with general information message.

### Severity

MEDIUM

---

## 2.11 Entry

### Ambiguity

Entry can mean:
1. Record in a list
2. Data entry
3. Publication (not used in SvitloSk)

### Current Usage

NOT used in SvitloSk.

### Risk

LOW — not used.

### Severity

LOW

---

## 2.12 Record

### Ambiguity

Record can mean:
1. Historical record (archived)
2. Data record (technical)
3. Musical record

### Current Usage

Used for archived publications.

### Risk

May be confused with data records.

### Severity

LOW

---

## 2.13 Archive

### Ambiguity

Archive can mean:
1. Historical storage (SvitloSk)
2. Compression format (ZIP)
3. Collection of documents

### Current Usage

Used for historical storage.

### Risk

May be confused with compression format.

### Severity

LOW

---

## 2.14 State

### Ambiguity

State can mean:
1. Lifecycle state (Generated, Published, etc.)
2. Geographic state (US)
3. Condition

### Current Usage

Used for lifecycle states.

### Risk

May be confused with geographic state.

### Severity

LOW

---

# 3. Ambiguity Summary

| Term | Ambiguity | Severity |
|------|-----------|----------|
| Publisher | Role vs Component vs Human | MEDIUM |
| Publication | Message vs Product vs Process | HIGH |
| Edition | Daily instance vs Version vs Print run | MEDIUM |
| Issue | Daily instance vs Problem vs Number | MEDIUM |
| Release | Daily instance vs Software release | MEDIUM |
| Graph | Chart vs Data structure vs Plot | LOW |
| Notification | Push notification vs Alert vs Notice | LOW |
| Product | Information product vs Software vs Business | LOW |
| Information | Factual content vs Data vs Knowledge | MEDIUM |
| Message | Telegram message vs General message | MEDIUM |
| Entry | Not used | LOW |
| Record | Historical record vs Data record | LOW |
| Archive | Historical storage vs Compression | LOW |
| State | Lifecycle state vs Geographic state | LOW |

---

# 4. Findings

## 4.1 Finding AM-001

**14 ambiguous terms were identified.**

4 are HIGH/MEDIUM severity, 10 are LOW severity.

**Evidence:** Analysis of ambiguities.

**Confidence:** HIGH.

## 4.2 Finding AM-002

**Publication is the MOST AMBIGUOUS term.**

Can mean message, product, or process.

**Evidence:** Analysis of ambiguities.

**Confidence:** HIGH.

## 4.3 Finding AM-003

**Edition, Issue, Release are POTENTIALLY SYNONYMOUS.**

All refer to daily instance of Journal.

**Evidence:** Analysis of ambiguities.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| AM-001 | Analysis of ambiguities |
| AM-002 | Analysis of ambiguities |
| AM-003 | Analysis of ambiguities |

---

**End of Ambiguities**
