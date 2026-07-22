# TGCORE001_OPERATION_GRAPH

**Document ID:** CASE-TG-CORE-001-OG

**Title:** Operation Graph

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document lists every operation performed by Telegram subsystem.

---

# 2. Operation Graph

## 2.1 Data Acquisition Operations

### OP-001: Receive Queue Schedule

**Input:** Queue Schedule JSON

**Output:** Normalized queue data

**Trigger:** Parser A completes

**Dependencies:** Parser A

---

### OP-002: Receive Planned Outages

**Input:** Planned Outages JSON

**Output:** Normalized planned outage data

**Trigger:** Parser B completes

**Dependencies:** Parser B

---

### OP-003: Receive Emergency Outages

**Input:** Emergency Outages JSON

**Output:** Normalized emergency outage data

**Trigger:** Parser B completes

**Dependencies:** Parser B

---

## 2.2 Data Processing Operations

### OP-004: Organize by Territory

**Input:** Normalized data

**Output:** Territory-organized data

**Trigger:** Data received

**Dependencies:** Territory Structure

---

### OP-005: Detect Changes

**Input:** New data, Current publications

**Output:** Change signals

**Trigger:** Data received

**Dependencies:** Current publication state

---

### OP-006: Detect Expiry

**Input:** Current publications, Current time

**Output:** Expiry signals

**Trigger:** Time-based

**Dependencies:** Reporting Period

---

## 2.3 Publication Generation Operations

### OP-007: Generate Emergency Outage Publication

**Input:** Emergency outage data, Territory

**Output:** Emergency outage publication

**Trigger:** Emergency outage data available

**Dependencies:** OP-004

---

### OP-008: Generate Planned Outage Publication (Today)

**Input:** Planned outage data, Territory

**Output:** Planned outage publication (today)

**Trigger:** Planned outage data available

**Dependencies:** OP-004

---

### OP-009: Generate Planned Outage Publication (Tomorrow)

**Input:** Planned outage data, Territory

**Output:** Planned outage publication (tomorrow)

**Trigger:** Tomorrow's planned outage data available

**Dependencies:** OP-004

---

### OP-010: Generate Queue Graph

**Input:** Queue schedule data

**Output:** Queue graph image

**Trigger:** Tomorrow's queue schedule available

**Dependencies:** OP-001

---

### OP-011: Generate Technical Message

**Input:** System status, Update timestamp

**Output:** Technical message publication

**Trigger:** System update

**Dependencies:** System status

---

### OP-012: Generate Service Message

**Input:** Service announcement

**Output:** Service message publication

**Trigger:** Service announcement available

**Dependencies:** Service announcement

---

## 2.4 Formatting Operations

### OP-013: Format Emergency Outage Message

**Input:** Emergency outage publication

**Output:** Formatted Telegram message

**Trigger:** Publication generated

**Dependencies:** Editorial Rules

---

### OP-014: Format Planned Outage Message

**Input:** Planned outage publication

**Output:** Formatted Telegram message

**Trigger:** Publication generated

**Dependencies:** Editorial Rules

---

### OP-015: Format Technical Message

**Input:** Technical message publication

**Output:** Formatted Telegram message

**Trigger:** Publication generated

**Dependencies:** Editorial Rules

---

## 2.5 Channel Operations

### OP-016: Send Message to Channel

**Input:** Formatted message

**Output:** Telegram message ID

**Trigger:** Message ready

**Dependencies:** Telegram Bot API

---

### OP-017: Edit Channel Message

**Input:** Message ID, Updated content

**Output:** Updated message

**Trigger:** Publication updated

**Dependencies:** Telegram Bot API

---

### OP-018: Delete Channel Message

**Input:** Message ID

**Output:** Message deleted

**Trigger:** Publication expired

**Dependencies:** Telegram Bot API

---

### OP-019: Get Channel State

**Input:** Channel ID

**Output:** Channel state

**Trigger:** On demand

**Dependencies:** Telegram Bot API

---

## 2.6 Lifecycle Operations

### OP-020: Archive Publication

**Input:** Publication, Timestamp

**Output:** Archived record

**Trigger:** Reporting period ends

**Dependencies:** OP-016

---

### OP-021: Remove Temporary Publication

**Input:** Temporary publication

**Output:** Publication removed

**Trigger:** Expiry detected

**Dependencies:** OP-006

---

# 3. Operation Graph Visualization

```
                    ┌─────────────┐
                    │  Parser A   │
                    └──────┬──────┘
                           │
                           ▼
                    OP-001: Receive Queue Schedule
                           │
                           ▼
                    OP-004: Organize by Territory
                           │
                    ┌──────┴──────┐
                    ▼             ▼
             OP-007: Generate   OP-010: Generate
             Emergency Outage   Queue Graph
                    │             │
                    ▼             ▼
             OP-013: Format     OP-016: Send
             Emergency Message  Image to Channel
                    │             │
                    ▼             ▼
             OP-016: Send       Message ID
             Message to Channel
                    │
                    ▼
             Message ID

                    ┌─────────────┐
                    │  Parser B   │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    OP-002: Receive   OP-003: Receive
    Planned Outages   Emergency Outages
           │               │
           ▼               ▼
    OP-004: Organize by Territory
           │
    ┌──────┴──────┐
    ▼             ▼
OP-008: Generate  OP-009: Generate
Planned (Today)  Planned (Tomorrow)
    │             │
    ▼             ▼
OP-014: Format   OP-014: Format
Planned Message  Planned Message
    │             │
    ▼             ▼
OP-016: Send     OP-016: Send
Message          Message
```

---

# 4. Findings

## 4.1 Finding OG-001

**There are 21 operations.**

Across 6 categories: Data Acquisition (3), Data Processing (3), Publication Generation (6), Formatting (3), Channel (4), Lifecycle (2).

**Evidence:** Analysis of Telegram operations.

**Confidence:** HIGH.

## 4.2 Finding OG-002

**Operations form a SEQUENTIAL FLOW.**

Data Acquisition → Processing → Generation → Formatting → Channel → Lifecycle.

**Evidence:** Analysis of operation graph.

**Confidence:** HIGH.

## 4.3 Finding OG-003

**Channel operations are TELEGRAM-SPECIFIC.**

Send, Edit, Delete, Get State.

**Evidence:** Analysis of operation graph.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OG-001 | Analysis of Telegram operations |
| OG-002 | Analysis of operation graph |
| OG-003 | Analysis of operation graph |

---

**End of Operation Graph**
