# TGCORE001_CORE_BOUNDARY

**Document ID:** CASE-TG-CORE-001-CB

**Title:** Core Boundary

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document separates Telegram-specific behavior from generic behavior.

---

# 2. Core Boundary

## 2.1 Generic Core (Channel-Independent)

### Data Acquisition

- Receive Queue Schedule
- Receive Planned Outages
- Receive Emergency Outages

### Data Processing

- Organize by Territory
- Detect Changes
- Detect Expiry

### Publication Generation

- Generate Emergency Publication
- Generate Planned Publication (Today)
- Generate Planned Publication (Tomorrow)
- Generate Technical Message
- Generate Service Message

### Lifecycle Management

- Archive Publication
- Remove Temporary Publication

---

## 2.2 Telegram-Specific (Channel-Dependent)

### Graph Generation

- Generate Queue Graph (SVG/PNG)

### Formatting

- Format Emergency Message (Telegram format)
- Format Planned Message (Telegram format)
- Format Technical Message (Telegram format)

### Channel Delivery

- Send Message (Telegram Bot API)
- Edit Message (Telegram Bot API)
- Delete Message (Telegram Bot API)
- Get Channel State (Telegram Bot API)

---

## 2.3 Boundary Visualization

```
┌─────────────────────────────────────────────────────────────┐
│                    GENERIC CORE                              │
├─────────────────────────────────────────────────────────────┤
│ Data Acquisition                                            │
│ Data Processing                                             │
│ Publication Generation                                      │
│ Lifecycle Management                                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                TELEGRAM-SPECIFIC                             │
├─────────────────────────────────────────────────────────────┤
│ Graph Generation (SVG/PNG)                                  │
│ Formatting (Telegram format)                                │
│ Channel Delivery (Telegram Bot API)                         │
└─────────────────────────────────────────────────────────────┘
```

---

# 3. Boundary Analysis

## 3.1 What Could Be Extracted to Publisher

| Component | Evidence |
|-----------|----------|
| Data Acquisition | Generic |
| Data Processing | Generic |
| Publication Generation | Generic |
| Lifecycle Management | Generic |

## 3.2 What Must Stay in Telegram Adapter

| Component | Evidence |
|-----------|----------|
| Graph Generation | Telegram-specific image format |
| Formatting | Telegram-specific text format |
| Channel Delivery | Telegram Bot API |

---

# 4. Findings

## 4.1 Finding CB-001

**Generic core contains 10 responsibilities.**

Data Acquisition (3), Data Processing (3), Publication Generation (5), Lifecycle Management (2).

**Evidence:** Analysis of core boundary.

**Confidence:** HIGH.

## 4.2 Finding CB-002

**Telegram-specific contains 7 responsibilities.**

Graph Generation (1), Formatting (3), Channel Delivery (4).

**Evidence:** Analysis of core boundary.

**Confidence:** HIGH.

## 4.3 Finding CB-003

**The boundary is CLEAR.**

Generic core is channel-independent.

Telegram-specific is channel-dependent.

**Evidence:** Analysis of core boundary.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| CB-001 | Analysis of core boundary |
| CB-002 | Analysis of core boundary |
| CB-003 | Analysis of core boundary |

---

**End of Core Boundary**
