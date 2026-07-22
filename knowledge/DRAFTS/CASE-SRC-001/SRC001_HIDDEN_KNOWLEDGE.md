# SRC001_HIDDEN_KNOWLEDGE

**Document ID:** CASE-SRC-001-HK

**Title:** Hidden Publisher Knowledge

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document searches for Publisher knowledge that exists ONLY in Telegram implementation, archived files, or historical documentation.

---

# 2. Hidden Knowledge

## 2.1 Telegram Implementation Knowledge

### HK-001: Message Formatting Rules

**Location:** Telegram Bot Code (external)

**Knowledge:** Specific rules for formatting Telegram messages.

**Why hidden:** Not documented in current specifications.

**Evidence:** Architect confirmation — Telegram implementation contains largest amount of practical Publisher knowledge.

---

### HK-002: Image Generation Logic

**Location:** Telegram Bot Code (external)

**Knowledge:** Logic for generating images for Telegram.

**Why hidden:** Not documented in current specifications.

**Evidence:** OP-009: Generate Queue Graph is Telegram-specific.

---

### HK-003: Message Editing Mechanics

**Location:** Telegram Bot Code (external)

**Knowledge:** Mechanics for editing existing Telegram messages.

**Why hidden:** Not documented in current specifications.

**Evidence:** OP-018: Edit Channel Message is Telegram-specific.

---

### HK-004: Channel State Management

**Location:** Telegram Bot Code (external)

**Knowledge:** How Telegram channel state is managed.

**Why hidden:** Not documented in current specifications.

**Evidence:** OP-020: Get Channel State is Telegram-specific.

---

## 2.2 Archived Materials Knowledge

### HK-005: Historical Publishing Model

**Location:** archive/knowledge/PROJECT_PUBLISHING_CORE_MODEL.md

**Knowledge:** Historical publishing model from earlier project versions.

**Why hidden:** Archived, not in current specifications.

**Evidence:** Archive contains historical architectural knowledge.

---

### HK-006: Historical Knowledge Register

**Location:** archive/knowledge/PROJECT_PUBLISHING_KNOWLEDGE_REGISTER.md

**Knowledge:** Historical register of publishing knowledge.

**Why hidden:** Archived, not in current specifications.

**Evidence:** Archive contains historical knowledge inventory.

---

## 2.3 Research Findings Knowledge

### HK-007: Publisher Skeleton

**Location:** CASE-PUB-002/PUB002_PUBLISHER_SKELETON.md

**Knowledge:** Extracted Publisher responsibilities and interfaces.

**Why hidden:** Research finding, not yet canonical.

**Evidence:** CASE-PUB-002 reverse engineering.

---

### HK-008: Telegram Remainder

**Location:** CASE-PUB-002/PUB002_TELEGRAM_REMAINDER.md

**Knowledge:** What remains in Telegram after Publisher extraction.

**Why hidden:** Research finding, not yet canonical.

**Evidence:** CASE-PUB-002 reverse engineering.

---

### HK-009: Lifecycle Operations

**Location:** CASE-LC-001/LC001_RESEARCH2_OPERATIONS.md

**Knowledge:** Lifecycle operations and ownership.

**Why hidden:** Research finding, not yet canonical.

**Evidence:** CASE-LC-001 lifecycle investigation.

---

### HK-010: Publisher Thickness Analysis

**Location:** CASE-LC-001/LC001_RESEARCH10_PUBLISHER.md

**Knowledge:** Analysis of Publisher thickness.

**Why hidden:** Research finding, not yet canonical.

**Evidence:** CASE-LC-001 lifecycle investigation.

---

# 3. Hidden Knowledge Summary

| ID | Knowledge | Location | Why Hidden |
|----|-----------|----------|------------|
| HK-001 | Message Formatting Rules | Telegram Bot Code | Not documented |
| HK-002 | Image Generation Logic | Telegram Bot Code | Not documented |
| HK-003 | Message Editing Mechanics | Telegram Bot Code | Not documented |
| HK-004 | Channel State Management | Telegram Bot Code | Not documented |
| HK-005 | Historical Publishing Model | Archive | Archived |
| HK-006 | Historical Knowledge Register | Archive | Archived |
| HK-007 | Publisher Skeleton | CASE-PUB-002 | Research finding |
| HK-008 | Telegram Remainder | CASE-PUB-002 | Research finding |
| HK-009 | Lifecycle Operations | CASE-LC-001 | Research finding |
| HK-010 | Publisher Thickness Analysis | CASE-LC-001 | Research finding |

---

# 4. Findings

## 4.1 Finding HK-001

**10 pieces of hidden Publisher knowledge were identified.**

4 in Telegram implementation, 2 in archives, 4 in research findings.

**Evidence:** Analysis of hidden knowledge sources.

**Confidence:** HIGH.

## 4.2 Finding HK-002

**Telegram implementation contains 4 pieces of hidden knowledge.**

Message formatting, image generation, editing mechanics, channel state.

**Evidence:** Architect confirmation.

**Confidence:** HIGH.

## 4.3 Finding HK-003

**Research findings contain 4 pieces of hidden knowledge.**

Publisher skeleton, Telegram remainder, lifecycle operations, publisher thickness.

**Evidence:** Analysis of research findings.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| HK-001 | Analysis of hidden knowledge sources |
| HK-002 | Architect confirmation |
| HK-003 | Analysis of research findings |

---

**End of Hidden Publisher Knowledge**
