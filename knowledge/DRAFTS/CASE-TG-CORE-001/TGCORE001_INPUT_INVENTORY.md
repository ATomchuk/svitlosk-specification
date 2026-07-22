# TGCORE001_INPUT_INVENTORY

**Document ID:** CASE-TG-CORE-001-II

**Title:** Input Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every input consumed by Telegram subsystem.

---

# 2. Input Inventory

## 2.1 JSON Inputs

### IN-001: Queue Schedule JSON

**Source:** Queue Schedule Parser

**Content:**
- Queue numbers (1-6)
- Subqueue numbers (1.1-6.2)
- Hourly schedule
- Availability status

**Format:** JSON

**Evidence:** Architect Intent — "Queue Schedule Parser → Queue Schedule JSON"

---

### IN-002: Planned Outages JSON

**Source:** Parser B

**Content:**
- Address (Settlement, Street, House)
- Planned time interval
- Source (DSO)

**Format:** JSON

**Evidence:** Architect Intent — Parser B produces Planned + Emergency Outages

---

### IN-003: Emergency Outages JSON

**Source:** Parser B

**Content:**
- Address (Settlement, Street, House)
- Emergency event description
- Source (DSO)

**Format:** JSON

**Evidence:** Architect Intent — Parser B produces Planned + Emergency Outages

---

## 2.2 TXT Inputs

### IN-004: today.txt

**Source:** Upstream parsers

**Content:**
- Formatted text for today's publications

**Format:** TXT

**Evidence:** Architect Context — "One operational source already exists: today.txt"

**Note:** This file is continuously regenerated. Publisher does NOT create this information.

---

## 2.3 Generated Metadata

### IN-005: Territory Structure

**Source:** TERRITORIAL_MODEL

**Content:**
- Community
- Administrative Centre
- Starosta Districts
- Settlements

**Format:** Reference data

**Evidence:** TERRITORIAL_MODEL.md

---

### IN-006: Reporting Period

**Source:** System clock

**Content:**
- Current date
- Current time

**Format:** Timestamp

**Evidence:** GLOSSARY §2

---

## 2.4 Configuration

### IN-007: Telegram Bot Token

**Source:** Configuration

**Content:**
- Bot authentication token

**Format:** String

**Evidence:** Telegram Bot API requirement

---

### IN-008: Channel ID

**Source:** Configuration

**Content:**
- Target Telegram channel ID

**Format:** String

**Evidence:** Telegram Bot API requirement

---

### IN-009: Editorial Rules

**Source:** TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL

**Content:**
- Formatting rules
- Presentation rules

**Format:** Specification

**Evidence:** TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

---

## 2.5 Templates

### IN-010: Emergency Outage Template

**Source:** Editorial system

**Content:**
- Template for emergency outage messages

**Format:** Template

**Evidence:** TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

---

### IN-011: Planned Outage Template

**Source:** Editorial system

**Content:**
- Template for planned outage messages

**Format:** Template

**Evidence:** TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

---

### IN-012: Technical Message Template

**Source:** Editorial system

**Content:**
- Template for technical messages

**Format:** Template

**Evidence:** TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

---

## 2.6 Technical Information

### IN-013: System Status

**Source:** System

**Content:**
- System health
- Last update time

**Format:** Internal

**Evidence:** Technical publication requirement

---

### IN-014: Update Timestamp

**Source:** System clock

**Content:**
- When data was last updated

**Format:** Timestamp

**Evidence:** Technical publication requirement

---

# 3. Input Classification

| ID | Input | Category | Format |
|----|-------|----------|--------|
| IN-001 | Queue Schedule JSON | JSON | JSON |
| IN-002 | Planned Outages JSON | JSON | JSON |
| IN-003 | Emergency Outages JSON | JSON | JSON |
| IN-004 | today.txt | TXT | TXT |
| IN-005 | Territory Structure | Metadata | Reference |
| IN-006 | Reporting Period | Metadata | Timestamp |
| IN-007 | Telegram Bot Token | Configuration | String |
| IN-008 | Channel ID | Configuration | String |
| IN-009 | Editorial Rules | Configuration | Specification |
| IN-010 | Emergency Outage Template | Template | Template |
| IN-011 | Planned Outage Template | Template | Template |
| IN-012 | Technical Message Template | Template | Template |
| IN-013 | System Status | Technical | Internal |
| IN-014 | Update Timestamp | Technical | Timestamp |

---

# 4. Findings

## 4.1 Finding II-001

**There are 14 inputs.**

Across 6 categories: JSON (3), TXT (1), Metadata (2), Configuration (3), Templates (3), Technical (2).

**Evidence:** Analysis of Telegram inputs.

**Confidence:** HIGH.

## 4.2 Finding II-002

**JSON inputs are the PRIMARY data source.**

Queue Schedule, Planned Outages, Emergency Outages.

**Evidence:** Analysis of input inventory.

**Confidence:** HIGH.

## 4.3 Finding II-003

**Configuration inputs are CHANNEL-SPECIFIC.**

Telegram Bot Token, Channel ID, Editorial Rules.

**Evidence:** Analysis of input inventory.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| II-001 | Analysis of Telegram inputs |
| II-002 | Analysis of input inventory |
| II-003 | Analysis of input inventory |

---

**End of Input Inventory**
