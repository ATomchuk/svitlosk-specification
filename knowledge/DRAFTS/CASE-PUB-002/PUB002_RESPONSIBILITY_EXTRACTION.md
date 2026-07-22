# PUB002_RESPONSIBILITY_EXTRACTION

**Document ID:** CASE-PUB-002-RE

**Title:** Responsibility Extraction

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document extracts responsibilities from Telegram operations and classifies them.

---

# 2. Responsibility Classification

## 2.1 Publication Operations

### OP-001: Create Publication

**Responsibility:** Create publication from interpretation result.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Creation logic is channel-independent |
| Publisher | HIGH | Publication generation is Publisher responsibility |
| Lifecycle | LOW | Lifecycle detects need, but doesn't create |
| Journal | LOW | Journal is service, not creator |

**Classification:** PUBLISHER

---

### OP-002: Update Publication

**Responsibility:** Update publication with new information.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Update logic is channel-independent |
| Publisher | HIGH | Publication update is Publisher responsibility |
| Lifecycle | MEDIUM | Lifecycle detects need, but doesn't update |
| Journal | LOW | Journal is service, not updater |

**Classification:** PUBLISHER

---

### OP-003: Replace Publication

**Responsibility:** Replace publication when structure changes.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Replacement logic is channel-independent |
| Publisher | HIGH | Publication replacement is Publisher responsibility |
| Lifecycle | MEDIUM | Lifecycle detects need, but doesn't replace |
| Journal | LOW | Journal is service, not replacer |

**Classification:** PUBLISHER

---

### OP-004: Archive Publication

**Responsibility:** Preserve publication as historical record.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Archival is channel-independent |
| Publisher | MEDIUM | Publisher coordinates, but doesn't archive |
| Lifecycle | HIGH | Archival is lifecycle responsibility |
| Journal | LOW | Journal is service, not archiver |

**Classification:** LIFECYCLE

---

### OP-005: Remove Publication

**Responsibility:** Remove temporary publication.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | MEDIUM | Removal mechanism is Telegram-specific |
| Publisher | HIGH | Publication removal is Publisher responsibility |
| Lifecycle | MEDIUM | Lifecycle detects need, but doesn't remove |
| Journal | LOW | Journal is service, not remover |

**Classification:** PUBLISHER

---

## 2.2 Content Operations

### OP-006: Format Emergency Outages

**Responsibility:** Format emergency information for publication.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | MEDIUM | Text format is Telegram-specific |
| Publisher | HIGH | Formatting is Publisher responsibility |
| Lifecycle | LOW | Lifecycle doesn't format |
| Journal | LOW | Journal is service, not formatter |

**Classification:** PUBLISHER

---

### OP-007: Format Planned Outages

**Responsibility:** Format planned information for publication.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | MEDIUM | Text format is Telegram-specific |
| Publisher | HIGH | Formatting is Publisher responsibility |
| Lifecycle | LOW | Lifecycle doesn't format |
| Journal | LOW | Journal is service, not formatter |

**Classification:** PUBLISHER

---

### OP-008: Format Tomorrow Outages

**Responsibility:** Format tomorrow's information.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | MEDIUM | Text format is Telegram-specific |
| Publisher | HIGH | Formatting is Publisher responsibility |
| Lifecycle | LOW | Lifecycle doesn't format |
| Journal | LOW | Journal is service, not formatter |

**Classification:** PUBLISHER

---

### OP-009: Generate Queue Graph

**Responsibility:** Generate visual graph.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | HIGH | Image generation is Telegram-specific |
| Publisher | MEDIUM | Publisher coordinates, but doesn't generate |
| Lifecycle | LOW | Lifecycle doesn't generate |
| Journal | LOW | Journal is service, not generator |

**Classification:** TELEGRAM ADAPTER

---

### OP-010: Format Technical Message

**Responsibility:** Format technical message.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | MEDIUM | Text format is Telegram-specific |
| Publisher | HIGH | Formatting is Publisher responsibility |
| Lifecycle | LOW | Lifecycle doesn't format |
| Journal | LOW | Journal is service, not formatter |

**Classification:** PUBLISHER

---

## 2.3 Territorial Operations

### OP-011: Group by Territory

**Responsibility:** Organize publications geographically.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Organization is channel-independent |
| Publisher | HIGH | Organization is Publisher responsibility |
| Lifecycle | LOW | Lifecycle doesn't organize |
| Journal | MEDIUM | Journal is organized, but doesn't do organizing |

**Classification:** PUBLISHER

---

### OP-012: Identify Territory

**Responsibility:** Determine publication location.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Identification is channel-independent |
| Publisher | HIGH | Identification is Publisher responsibility |
| Lifecycle | LOW | Lifecycle doesn't identify |
| Journal | LOW | Journal is service, not identifier |

**Classification:** PUBLISHER

---

## 2.4 Lifecycle Operations

### OP-013: Detect Expiry

**Responsibility:** Detect when information expires.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Detection is channel-independent |
| Publisher | LOW | Publisher doesn't detect |
| Lifecycle | HIGH | Expiry detection is Lifecycle responsibility |
| Journal | LOW | Journal is service, not detector |

**Classification:** LIFECYCLE

---

### OP-014: Execute Expiry

**Responsibility:** Remove expired information.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | MEDIUM | Removal mechanism is Telegram-specific |
| Publisher | HIGH | Expiry execution is Publisher responsibility |
| Lifecycle | MEDIUM | Lifecycle detects, but doesn't execute |
| Journal | LOW | Journal is service, not executor |

**Classification:** PUBLISHER

---

### OP-015: Detect Update

**Responsibility:** Detect when information changes.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | LOW | Detection is channel-independent |
| Publisher | LOW | Publisher doesn't detect |
| Lifecycle | HIGH | Update detection is Lifecycle responsibility |
| Journal | LOW | Journal is service, not detector |

**Classification:** LIFECYCLE

---

### OP-016: Execute Update

**Responsibility:** Apply information changes.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | MEDIUM | Edit mechanism is Telegram-specific |
| Publisher | HIGH | Update execution is Publisher responsibility |
| Lifecycle | MEDIUM | Lifecycle detects, but doesn't execute |
| Journal | LOW | Journal is service, not executor |

**Classification:** PUBLISHER

---

## 2.5 Channel Operations

### OP-017: Send to Channel

**Responsibility:** Deliver publication to Telegram.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | HIGH | Telegram Bot API is Telegram-specific |
| Publisher | LOW | Publisher coordinates, but doesn't send |
| Lifecycle | LOW | Lifecycle doesn't send |
| Journal | LOW | Journal is service, not sender |

**Classification:** TELEGRAM ADAPTER

---

### OP-018: Edit Channel Message

**Responsibility:** Edit existing message.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | HIGH | Telegram Bot API is Telegram-specific |
| Publisher | LOW | Publisher coordinates, but doesn't edit |
| Lifecycle | LOW | Lifecycle doesn't edit |
| Journal | LOW | Journal is service, not editor |

**Classification:** TELEGRAM ADAPTER

---

### OP-019: Delete Channel Message

**Responsibility:** Delete message.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | HIGH | Telegram Bot API is Telegram-specific |
| Publisher | LOW | Publisher coordinates, but doesn't delete |
| Lifecycle | LOW | Lifecycle doesn't delete |
| Journal | LOW | Journal is service, not deleter |

**Classification:** TELEGRAM ADAPTER

---

### OP-020: Get Channel State

**Responsibility:** Retrieve channel state.

**Belongs to:**

| Component | fit | Evidence |
|-----------|-----|----------|
| Telegram Adapter | HIGH | Telegram Bot API is Telegram-specific |
| Publisher | LOW | Publisher doesn't get state |
| Lifecycle | LOW | Lifecycle doesn't get state |
| Journal | LOW | Journal is service, not state getter |

**Classification:** TELEGRAM ADAPTER

---

# 3. Responsibility Summary

| Component | Operations | Count |
|-----------|------------|-------|
| Publisher | OP-001, OP-002, OP-003, OP-005, OP-006, OP-007, OP-008, OP-010, OP-011, OP-012, OP-014, OP-016 | 12 |
| Lifecycle | OP-004, OP-013, OP-015 | 3 |
| Telegram Adapter | OP-009, OP-017, OP-018, OP-019, OP-020 | 5 |

---

# 4. Findings

## 4.1 Finding RE-001

**12 operations belong to Publisher.**

Publication generation, update, replacement, removal, formatting, organization, execution.

**Evidence:** Analysis of responsibility classification.

**Confidence:** HIGH.

## 4.2 Finding RE-002

**3 operations belong to Lifecycle.**

Archival, expiry detection, update detection.

**Evidence:** Analysis of responsibility classification.

**Confidence:** HIGH.

## 4.3 Finding RE-003

**5 operations belong to Telegram Adapter.**

Queue graph generation, send, edit, delete, get state.

**Evidence:** Analysis of responsibility classification.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| RE-001 | Analysis of responsibility classification |
| RE-002 | Analysis of responsibility classification |
| RE-003 | Analysis of responsibility classification |

---

**End of Responsibility Extraction**
