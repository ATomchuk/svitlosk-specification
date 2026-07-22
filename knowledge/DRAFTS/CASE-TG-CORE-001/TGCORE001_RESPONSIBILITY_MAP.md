# TGCORE001_RESPONSIBILITY_MAP

**Document ID:** CASE-TG-CORE-001-RM

**Title:** Responsibility Map

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines where responsibilities currently exist.

---

# 2. Responsibility Map

## 2.1 Data Acquisition

| Responsibility | Location | Telegram-Only? | Generic? | Unknown? |
|----------------|----------|----------------|----------|----------|
| Receive Queue Schedule | Telegram | NO | YES | — |
| Receive Planned Outages | Telegram | NO | YES | — |
| Receive Emergency Outages | Telegram | NO | YES | — |

---

## 2.2 Data Processing

| Responsibility | Location | Telegram-Only? | Generic? | Unknown? |
|----------------|----------|----------------|----------|----------|
| Organize by Territory | Telegram | NO | YES | — |
| Detect Changes | Telegram | NO | YES | — |
| Detect Expiry | Telegram | NO | YES | — |

---

## 2.3 Publication Generation

| Responsibility | Location | Telegram-Only? | Generic? | Unknown? |
|----------------|----------|----------------|----------|----------|
| Generate Emergency Publication | Telegram | NO | YES | — |
| Generate Planned Publication (Today) | Telegram | NO | YES | — |
| Generate Planned Publication (Tomorrow) | Telegram | NO | YES | — |
| Generate Queue Graph | Telegram | PARTIALLY | PARTIALLY | — |
| Generate Technical Message | Telegram | NO | YES | — |
| Generate Service Message | Telegram | NO | YES | — |

---

## 2.4 Formatting

| Responsibility | Location | Telegram-Only? | Generic? | Unknown? |
|----------------|----------|----------------|----------|----------|
| Format Emergency Message | Telegram | PARTIALLY | PARTIALLY | — |
| Format Planned Message | Telegram | PARTIALLY | PARTIALLY | — |
| Format Technical Message | Telegram | PARTIALLY | PARTIALLY | — |

---

## 2.5 Channel Delivery

| Responsibility | Location | Telegram-Only? | Generic? | Unknown? |
|----------------|----------|----------------|----------|----------|
| Send Message | Telegram | YES | NO | — |
| Edit Message | Telegram | YES | NO | — |
| Delete Message | Telegram | YES | NO | — |
| Get Channel State | Telegram | YES | NO | — |

---

## 2.6 Lifecycle

| Responsibility | Location | Telegram-Only? | Generic? | Unknown? |
|----------------|----------|----------------|----------|----------|
| Archive Publication | Telegram | NO | YES | — |
| Remove Temporary Publication | Telegram | PARTIALLY | PARTIALLY | — |

---

# 3. Responsibility Summary

| Category | Telegram-Only | Generic | Unknown |
|----------|---------------|---------|---------|
| Data Acquisition | 0 | 3 | 0 |
| Data Processing | 0 | 3 | 0 |
| Publication Generation | 0 | 5 | 0 |
| Formatting | 0 | 3 | 0 |
| Channel Delivery | 4 | 0 | 0 |
| Lifecycle | 0 | 2 | 0 |
| **Total** | **4** | **16** | **0** |

---

# 4. Findings

## 4.1 Finding RM-001

**16 responsibilities are GENERIC.**

They could belong to any channel.

**Evidence:** Analysis of responsibility map.

**Confidence:** HIGH.

## 4.2 Finding RM-002

**4 responsibilities are TELEGRAM-ONLY.**

Send, Edit, Delete, Get Channel State.

**Evidence:** Analysis of responsibility map.

**Confidence:** HIGH.

## 4.3 Finding RM-003

**No responsibilities are UNKNOWN.**

All responsibilities are classified.

**Evidence:** Analysis of responsibility map.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| RM-001 | Analysis of responsibility map |
| RM-002 | Analysis of responsibility map |
| RM-003 | Analysis of responsibility map |

---

**End of Responsibility Map**
