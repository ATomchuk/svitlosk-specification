# TGCORE001_OUTPUT_INVENTORY

**Document ID:** CASE-TG-CORE-001-OI

**Title:** Output Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every output produced by Telegram subsystem.

---

# 2. Output Inventory

## 2.1 Telegram Posts

### OUT-001: Emergency Outage Post (per Territory)

**Content:**
- Territory name
- Emergency outage information
- Address details

**Format:** Telegram message (text)

**Destination:** Telegram channel

**Evidence:** Architect Intent — "emergency outages today"

---

### OUT-002: Planned Outage Post - Today (per Territory)

**Content:**
- Territory name
- Planned outage information
- Address details
- Time intervals

**Format:** Telegram message (text)

**Destination:** Telegram channel

**Evidence:** Architect Intent — "planned outages today"

---

### OUT-003: Planned Outage Post - Tomorrow (per Territory)

**Content:**
- Territory name
- Planned outage information
- Address details
- Time intervals

**Format:** Telegram message (text)

**Destination:** Telegram channel

**Evidence:** Architect Intent — "planned outages tomorrow"

---

### OUT-004: Queue Graph Post (Tomorrow)

**Content:**
- Visual graph of 12 subqueues
- Tomorrow's date
- Planned availability

**Format:** Telegram message (image)

**Destination:** Telegram channel

**Evidence:** Architect Intent — "queue graph tomorrow"

---

### OUT-005: Technical Message Post

**Content:**
- Technical system message
- Timestamp

**Format:** Telegram message (text)

**Destination:** Telegram channel

**Evidence:** Architect Intent — "technical update message"

---

### OUT-006: Service Message Post (Future)

**Content:**
- Future project announcement
- Timestamp

**Format:** Telegram message (text)

**Destination:** Telegram channel

**Evidence:** Architect Intent — "future technical notices"

---

## 2.2 Internal Outputs

### OUT-007: Publication Package

**Content:**
- Collection of all publications for one day

**Format:** Internal data structure

**Destination:** Telegram Publisher

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §3.1

---

### OUT-008: Rendered Messages

**Content:**
- Formatted messages ready for Telegram

**Format:** Internal data structure

**Destination:** Telegram Bot API

**Evidence:** Telegram subsystem processing

---

### OUT-009: Image Files

**Content:**
- Generated images (PNG)

**Format:** Binary

**Destination:** Telegram Bot API

**Evidence:** Queue Graph generation

---

## 2.3 Metadata Outputs

### OUT-010: Message IDs

**Content:**
- Telegram message IDs for tracking

**Format:** Integer

**Destination:** Internal storage

**Evidence:** Telegram Bot API response

---

### OUT-011: Publication State

**Content:**
- State of each publication (created, published, updated, archived)

**Format:** Internal data structure

**Destination:** Internal storage

**Evidence:** Lifecycle management

---

# 3. Output Classification

| ID | Output | Category | Format | Destination |
|----|--------|----------|--------|-------------|
| OUT-001 | Emergency Outage Post | Telegram Post | Text | Channel |
| OUT-002 | Planned Outage Post (Today) | Telegram Post | Text | Channel |
| OUT-003 | Planned Outage Post (Tomorrow) | Telegram Post | Text | Channel |
| OUT-004 | Queue Graph Post | Telegram Post | Image | Channel |
| OUT-005 | Technical Message Post | Telegram Post | Text | Channel |
| OUT-006 | Service Message Post | Telegram Post | Text | Channel |
| OUT-007 | Publication Package | Internal | Data | Telegram Publisher |
| OUT-008 | Rendered Messages | Internal | Data | Bot API |
| OUT-009 | Image Files | Internal | Binary | Bot API |
| OUT-010 | Message IDs | Metadata | Integer | Storage |
| OUT-011 | Publication State | Metadata | Data | Storage |

---

# 4. Findings

## 4.1 Finding OI-001

**There are 11 outputs.**

Across 3 categories: Telegram Posts (6), Internal (3), Metadata (2).

**Evidence:** Analysis of Telegram outputs.

**Confidence:** HIGH.

## 4.2 Finding OI-002

**6 outputs are Telegram Posts.**

These are the visible outputs to residents.

**Evidence:** Analysis of output inventory.

**Confidence:** HIGH.

## 4.3 Finding OI-003

**3 outputs are Internal.**

Publication Package, Rendered Messages, Image Files.

**Evidence:** Analysis of output inventory.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OI-001 | Analysis of Telegram outputs |
| OI-002 | Analysis of output inventory |
| OI-003 | Analysis of output inventory |

---

**End of Output Inventory**
