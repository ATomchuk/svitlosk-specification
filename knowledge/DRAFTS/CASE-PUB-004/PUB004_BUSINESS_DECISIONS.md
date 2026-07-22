# PUB004_BUSINESS_DECISIONS

**Document ID:** CASE-PUB-004-BD

**Title:** Business Decisions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies decisions that are PURELY BUSINESS decisions.

---

# 2. Business Decisions

## 2.1 BD-001: Should Tomorrow Publication Disappear at Midnight?

### Question

Should tomorrow's planned outage publication disappear at exactly midnight?

### Decision Type

BUSINESS — temporal boundary.

### Evidence

> "Tomorrow information disappears automatically before the end of the current day." (Architect Intent)

### Current Behavior

Yes — disappears at end of day.

### Status

BUSINESS DECISION — not technical.

---

## 2.2 BD-002: Should Publication Be Regenerated After Parser Update?

### Question

Should a publication be regenerated when parser provides new data?

### Decision Type

BUSINESS — data freshness.

### Evidence

> "Publications MAY be updated only when the normalized dataset changes." (TELEGRAM_PUBLICATION_LIFECYCLE.md)

### Current Behavior

Yes — regenerated on data change.

### Status

BUSINESS DECISION — not technical.

---

## 2.3 BD-003: Should Graph Be Replaced?

### Question

Should the queue graph be replaced entirely when new data arrives?

### Decision Type

BUSINESS — presentation strategy.

### Evidence

> Queue Graph is replaced, not edited. (CASE-TG-CORE-001)

### Current Behavior

Yes — replaced entirely.

### Status

BUSINESS DECISION — not technical.

---

## 2.4 BD-004: Should Unchanged Publication Remain?

### Question

Should a publication remain unchanged if the underlying data hasn't changed?

### Decision Type

BUSINESS — efficiency strategy.

### Evidence

> "Two identical normalized Datasets SHALL always generate identical Telegram Journals." (GLOSSARY §3)

### Current Behavior

Yes — unchanged publications remain.

### Status

BUSINESS DECISION — not technical.

---

## 2.5 BD-005: Should Emergency Outages Be Permanent?

### Question

Should emergency outage publications be archived permanently?

### Decision Type

BUSINESS — historical preservation.

### Evidence

> "Emergency outages SHALL remain available as part of the historical record." (TELEGRAM_EDITORIAL)

### Current Behavior

Yes — permanently archived.

### Status

BUSINESS DECISION — not technical.

---

## 2.6 BD-006: Should Technical Messages Be Updated In-Place?

### Question

Should technical messages be updated in place or replaced?

### Decision Type

BUSINESS — presentation strategy.

### Evidence

> Technical messages show latest update timestamp. (CASE-TG-CORE-001)

### Current Behavior

Updated in place.

### Status

BUSINESS DECISION — not technical.

---

# 3. Business Decision Summary

| ID | Question | Current Behavior |
|----|----------|------------------|
| BD-001 | Tomorrow publication disappears at midnight? | YES |
| BD-002 | Publication regenerated after parser update? | YES |
| BD-003 | Graph replaced on new data? | YES |
| BD-004 | Unchanged publication remains? | YES |
| BD-005 | Emergency outages permanent? | YES |
| BD-006 | Technical messages updated in-place? | YES |

---

# 4. Findings

## 4.1 Finding BD-001

**6 business decisions were identified.**

All relate to temporal, data, or presentation strategy.

**Evidence:** Analysis of business decisions.

**Confidence:** HIGH.

## 4.2 Finding BD-002

**All current behaviors are YES.**

The system currently implements all these decisions.

**Evidence:** Analysis of business decision summary.

**Confidence:** HIGH.

## 4.3 Finding BD-003

**Business decisions are NOT technical.**

They define WHAT should happen, not HOW.

**Evidence:** Analysis of business decisions.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| BD-001 | Analysis of business decisions |
| BD-002 | Analysis of business decision summary |
| BD-003 | Analysis of business decisions |

---

**End of Business Decisions**
