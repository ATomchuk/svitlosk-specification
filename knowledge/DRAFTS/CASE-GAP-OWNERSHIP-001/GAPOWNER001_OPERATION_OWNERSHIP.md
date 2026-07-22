# Operation Gap Ownership

**Document Class:** Gap Ownership Analysis

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines ownership for every operation gap from CASE-GAP-001.

---

# Operation Gap Ownership

## GAP-OP-001: Schedule Generation

**Owner:** Parser (or separate component)

**Reason:** Schedule generation is a DATA PROCESSING function.

**Decision Maker:** Parser (determines when schedule is needed)

**Executor:** Schedule Generator (generates schedule)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Parser or separate component.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.5

---

## GAP-OP-002: Graphic Generation

**Owner:** Adapter (or Rendering Engine)

**Reason:** Graphic generation is a RENDERING function.

**Decision Maker:** Publisher (determines when graphic is needed)

**Executor:** Graphic Generator (generates graphic)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Adapter or Rendering Engine.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.6

---

## GAP-OP-003: Data Storage

**Owner:** Infrastructure

**Reason:** Data storage is PERSISTENCE infrastructure.

**Decision Maker:** System (determines when to store)

**Executor:** Data Storage (stores data)

**Close Before Publisher Spec?** NO — Infrastructure.

**Move Outside?** YES — belongs to Infrastructure.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.7

---

## GAP-OP-004: Channel Delivery

**Owner:** Adapter

**Reason:** Channel delivery is CHANNEL-SPECIFIC.

**Decision Maker:** Adapter (determines when to deliver)

**Executor:** Adapter (delivers)

**Close Before Publisher Spec?** NO — Adapter scope.

**Move Outside?** YES — belongs to Adapter.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.8

---

## GAP-OP-005: Subscriber Management

**Owner:** Telegram Adapter (or Channel)

**Reason:** Subscriber management is CHANNEL-SPECIFIC.

**Decision Maker:** Channel (manages subscribers)

**Executor:** Channel (manages)

**Close Before Publisher Spec?** NO — Channel scope.

**Move Outside?** YES — belongs to Channel.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.8

---

## GAP-OP-006: Admin Interaction

**Owner:** Telegram Adapter (or Channel)

**Reason:** Admin interaction is CHANNEL-SPECIFIC.

**Decision Maker:** Administrator (interacts)

**Executor:** Channel (handles interaction)

**Close Before Publisher Spec?** NO — Channel scope.

**Move Outside?** YES — belongs to Channel.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.8

---

## GAP-OP-007: Manual Publication Creation

**Owner:** Telegram Adapter (or Administrator)

**Reason:** Manual publication is CREATED BY administrators.

**Decision Maker:** Administrator (decides to create)

**Executor:** Channel (creates)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Channel or Administrator.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-OP-008: Image Publication Creation

**Owner:** Telegram Adapter (or Administrator)

**Reason:** Image publication is CREATED BY administrators.

**Decision Maker:** Administrator (decides to create)

**Executor:** Channel (creates)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Channel or Administrator.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-OP-009: Outage Period Calculation

**Owner:** Parser (or Schedule Generator)

**Reason:** Outage period calculation is DATA PROCESSING.

**Decision Maker:** Parser (determines calculation)

**Executor:** Schedule Generator (calculates)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Parser or Schedule Generator.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.5

---

## GAP-OP-010: Change Detection

**Owner:** Lifecycle

**Reason:** Change detection is LIFECYCLE behavior.

**Decision Maker:** Lifecycle (detects changes)

**Executor:** Lifecycle (detects)

**Close Before Publisher Spec?** NO — Lifecycle scope.

**Move Outside?** YES — belongs to Lifecycle.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md

---

# Operation Gap Ownership Summary

| Gap ID | Operation | Owner | Close Before Spec? | Move Outside? |
|--------|-----------|-------|-------------------|---------------|
| GAP-OP-001 | Schedule Generation | Parser | NO | YES |
| GAP-OP-002 | Graphic Generation | Adapter/Rendering | NO | YES |
| GAP-OP-003 | Data Storage | Infrastructure | NO | YES |
| GAP-OP-004 | Channel Delivery | Adapter | NO | YES |
| GAP-OP-005 | Subscriber Management | Channel | NO | YES |
| GAP-OP-006 | Admin Interaction | Channel | NO | YES |
| GAP-OP-007 | Manual Publication | Adapter/Admin | NO | YES |
| GAP-OP-008 | Image Publication | Adapter/Admin | NO | YES |
| GAP-OP-009 | Outage Period Calculation | Parser | NO | YES |
| GAP-OP-010 | Change Detection | Lifecycle | NO | YES |

---

# Traceability

| Gap | Source |
|-----|--------|
| GAP-OP-001 to GAP-OP-010 | CASE-GAP-001, TELEGRAM_PUBLISHING_CANONICAL_MODEL.md |

---

**End of Operation Gap Ownership**
