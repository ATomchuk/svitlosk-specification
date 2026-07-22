# PUB002_OPERATION_INVENTORY

**Document ID:** CASE-PUB-002-OI

**Title:** Telegram Operation Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every operation currently performed by Telegram.

---

# 2. Telegram Operations

## 2.1 Publication Operations

### OP-001: Create Publication

**Description:** Create a new Telegram message with outage information.

**Input:** Interpretation Result, Territory

**Output:** Telegram message (published)

**Frequency:** Multiple times per day

---

### OP-002: Update Publication

**Description:** Edit an existing Telegram message with new information.

**Input:** Updated Interpretation Result, Existing message ID

**Output:** Updated Telegram message

**Frequency:** When data changes

---

### OP-003: Replace Publication

**Description:** Delete old message and create new one.

**Input:** New Interpretation Result, Territory

**Output:** New Telegram message (old one deleted)

**Frequency:** When structure changes significantly

---

### OP-004: Archive Publication

**Description:** Preserve publication as historical record.

**Input:** Published message, Timestamp

**Output:** Archived record

**Frequency:** End of reporting period

---

### OP-005: Remove Publication

**Description:** Delete temporary publication from channel.

**Input:** Temporary message ID

**Output:** Message removed from channel

**Frequency:** When temporary information expires

---

## 2.2 Content Operations

### OP-006: Format Emergency Outages

**Description:** Format emergency outage information for publication.

**Input:** Emergency Outage Information

**Output:** Formatted text for Telegram

**Frequency:** When emergency outages exist

---

### OP-007: Format Planned Outages

**Description:** Format planned outage information for publication.

**Input:** Planned Outage Information

**Output:** Formatted text for Telegram

**Frequency:** When planned outages exist

---

### OP-008: Format Tomorrow Outages

**Description:** Format tomorrow's planned outage information.

**Input:** Tomorrow Planned Outage Information

**Output:** Formatted text for Telegram

**Frequency:** When tomorrow outages exist

---

### OP-009: Generate Queue Graph

**Description:** Generate visual graph of tomorrow's queue schedule.

**Input:** Tomorrow Queue Schedule

**Output:** Image for Telegram

**Frequency:** When tomorrow schedule exists

---

### OP-010: Format Technical Message

**Description:** Format technical system message.

**Input:** Technical Message Content

**Output:** Formatted text for Telegram

**Frequency:** When technical updates exist

---

## 2.3 Territorial Operations

### OP-011: Group by Territory

**Description:** Group publications by Starosta District.

**Input:** Publications, Territory Structure

**Output:** Territory-organized publications

**Frequency:** Always

---

### OP-012: Identify Territory

**Description:** Determine which territory a publication belongs to.

**Input:** Address, Territory Structure

**Output:** Territory assignment

**Frequency:** Per publication

---

## 2.4 Lifecycle Operations

### OP-013: Detect Expiry

**Description:** Detect when temporary information should expire.

**Input:** Publication, Current Time

**Output:** Expiry signal

**Frequency:** Continuous

---

### OP-014: Execute Expiry

**Description:** Remove expired publications from channel.

**Input:** Expired publications

**Output:** Publications removed

**Frequency:** When expiry detected

---

### OP-015: Detect Update

**Description:** Detect when information has changed.

**Input:** New Data, Current Publications

**Output:** Update signal

**Frequency:** When data changes

---

### OP-016: Execute Update

**Description:** Update publications with new information.

**Input:** Updated publications

**Output:** Publications updated on channel

**Frequency:** When update detected

---

## 2.5 Channel Operations

### OP-017: Send to Channel

**Description:** Deliver publication to Telegram channel.

**Input:** Publication, Channel

**Output:** Message published

**Frequency:** Per publication

---

### OP-018: Edit Channel Message

**Description:** Edit existing message on Telegram channel.

**Input:** Message ID, Updated content

**Output:** Message edited

**Frequency:** Per update

---

### OP-019: Delete Channel Message

**Description:** Delete message from Telegram channel.

**Input:** Message ID

**Output:** Message deleted

**Frequency:** Per removal

---

### OP-020: Get Channel State

**Description:** Retrieve current state of Telegram channel.

**Input:** Channel ID

**Output:** Channel state (messages, timestamps)

**Frequency:** On demand

---

# 3. Operation Inventory

| ID | Operation | Category | Frequency |
|----|-----------|----------|-----------|
| OP-001 | Create Publication | Publication | Multiple/day |
| OP-002 | Update Publication | Publication | When data changes |
| OP-003 | Replace Publication | Publication | When structure changes |
| OP-004 | Archive Publication | Publication | End of period |
| OP-005 | Remove Publication | Publication | When expires |
| OP-006 | Format Emergency Outages | Content | When outages exist |
| OP-007 | Format Planned Outages | Content | When outages exist |
| OP-008 | Format Tomorrow Outages | Content | When tomorrow outages exist |
| OP-009 | Generate Queue Graph | Content | When schedule exists |
| OP-010 | Format Technical Message | Content | When updates exist |
| OP-011 | Group by Territory | Territorial | Always |
| OP-012 | Identify Territory | Territorial | Per publication |
| OP-013 | Detect Expiry | Lifecycle | Continuous |
| OP-014 | Execute Expiry | Lifecycle | When detected |
| OP-015 | Detect Update | Lifecycle | When data changes |
| OP-016 | Execute Update | Lifecycle | When detected |
| OP-017 | Send to Channel | Channel | Per publication |
| OP-018 | Edit Channel Message | Channel | Per update |
| OP-019 | Delete Channel Message | Channel | Per removal |
| OP-020 | Get Channel State | Channel | On demand |

---

# 4. Findings

## 4.1 Finding OI-001

**There are 20 Telegram operations.**

Across 5 categories: Publication, Content, Territorial, Lifecycle, Channel.

**Evidence:** Analysis of Telegram specifications.

**Confidence:** HIGH.

## 4.2 Finding OI-002

**Publication operations are the core.**

Create, Update, Replace, Archive, Remove.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md.

**Confidence:** HIGH.

## 4.3 Finding OI-003

**Channel operations are Telegram-specific.**

Send, Edit, Delete, Get State.

**Evidence:** Analysis of channel operations.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OI-001 | Analysis of Telegram specifications |
| OI-002 | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| OI-003 | Analysis of channel operations |

---

**End of Telegram Operation Inventory**
