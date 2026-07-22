# PUB002_HIDDEN_COUPLINGS

**Document ID:** CASE-PUB-002-HC

**Title:** Hidden Couplings

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies hidden couplings — places where Telegram currently performs work that is actually unrelated to Telegram.

---

# 2. Hidden Couplings

## 2.1 COUPLING-001: Publication Generation

### Current Location

Telegram performs publication generation.

### Actual Owner

Publisher should own publication generation.

### Coupling Type

RESPONSIBILITY LEAKAGE.

### Evidence

> "Publication Engine — Transforms normalized dataset into deterministic Publication Package." (TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §3.1)

Publication generation is defined as Publication Engine responsibility, but Telegram currently performs it.

---

## 2.2 COUPLING-002: Territorial Organization

### Current Location

Telegram performs territorial organization.

### Actual Owner

Publisher should own territorial organization.

### Coupling Type

RESPONSIBILITY LEAKAGE.

### Evidence

> "Information SHALL always be organized according to the territorial structure of the community." (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md §4.7)

Territorial organization is an editorial principle, not a Telegram-specific concern.

---

## 2.3 COUPLING-003: Content Formatting

### Current Location

Telegram performs content formatting.

### Actual Owner

Publisher should own content formatting.

### Coupling Type

RESPONSIBILITY LEAKAGE.

### Evidence

> "Every publication SHALL be consistent, easy to read, and predictable in structure and presentation." (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md §4.8)

Consistency is an editorial principle, not a Telegram-specific concern.

---

## 2.4 COUPLING-004: Lifecycle Management

### Current Location

Telegram performs lifecycle management (expiry, archival).

### Actual Owner

Lifecycle should own lifecycle management.

### Coupling Type

RESPONSIBILITY LEAKAGE.

### Evidence

> "Publications become part of the historical record when the reporting period ends." (TELEGRAM_PUBLICATION_LIFECYCLE.md §6.3)

Archival is a lifecycle concern, not a Telegram-specific concern.

---

## 2.5 COUPLING-005: Update Detection

### Current Location

Telegram performs update detection.

### Actual Owner

Lifecycle should own update detection.

### Coupling Type

RESPONSIBILITY LEAKAGE.

### Evidence

> "Publications MAY be updated only when the normalized dataset changes." (TELEGRAM_PUBLICATION_LIFECYCL.md §6.2)

Update detection is a lifecycle concern, not a Telegram-specific concern.

---

# 3. Coupling Summary

| Coupling | Current Location | Actual Owner | Type |
|----------|------------------|--------------|------|
| COUPLING-001 | Telegram | Publisher | Responsibility Leakage |
| COUPLING-002 | Telegram | Publisher | Responsibility Leakage |
| COUPLING-003 | Telegram | Publisher | Responsibility Leakage |
| COUPLING-004 | Telegram | Lifecycle | Responsibility Leakage |
| COUPLING-005 | Telegram | Lifecycle | Responsibility Leakage |

---

# 4. Findings

## 4.1 Finding HC-001

**5 hidden couplings were identified.**

All are RESPONSIBILITY LEAKAGE — Telegram performs work that belongs to Publisher or Lifecycle.

**Evidence:** Analysis of Telegram specifications.

**Confidence:** HIGH.

## 4.2 Finding HC-002

**3 couplings are Publisher-related.**

Publication generation, territorial organization, content formatting.

**Evidence:** Analysis of Telegram specifications.

**Confidence:** HIGH.

## 4.3 Finding HC-003

**2 couplings are Lifecycle-related.**

Lifecycle management, update detection.

**Evidence:** Analysis of Telegram specifications.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| HC-001 | Analysis of Telegram specifications |
| HC-002 | Analysis of Telegram specifications |
| HC-003 | Analysis of Telegram specifications |

---

**End of Hidden Couplings**
