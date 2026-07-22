# Vocabulary Gap Ownership

**Document Class:** Gap Ownership Analysis

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines ownership for every vocabulary gap from CASE-GAP-001.

---

# Vocabulary Gap Ownership

## GAP-VOC-001: Publication Package

**Owner:** Publisher

**Reason:** Publication Package is a PUBLISHER concept.

**Decision Maker:** Publisher (defines term)

**Executor:** Publisher (uses term)

**Close Before Publisher Spec?** YES — core Publisher terminology.

**Move Outside?** NO — Publisher scope.

**Evidence:** GLOSSARY §3, TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §3.1

---

## GAP-VOC-002: Normalized Dataset

**Owner:** Parser

**Reason:** Normalized Dataset is a PARSER output.

**Decision Maker:** Parser (defines term)

**Executor:** Parser (uses term)

**Close Before Publisher Spec?** NO — Parser scope.

**Move Outside?** YES — belongs to Parser.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §3.3

---

## GAP-VOC-003: Schedule Request

**Owner:** Publisher

**Reason:** Schedule Request is a PUBLISHER interface term.

**Decision Maker:** Publisher (defines interface)

**Executor:** Publisher (uses interface)

**Close Before Publisher Spec?** YES — Publisher interface.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-VOC-004: Graphic Request

**Owner:** Publisher

**Reason:** Graphic Request is a PUBLISHER interface term.

**Decision Maker:** Publisher (defines interface)

**Executor:** Publisher (uses interface)

**Close Before Publisher Spec?** YES — Publisher interface.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-VOC-005: Manual Publication

**Owner:** Telegram Adapter (or Administrator)

**Reason:** Manual Publication is a TELEGRAM-SPECIFIC concept.

**Decision Maker:** Administrator (creates manual publication)

**Executor:** Telegram Channel (creates)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Telegram Adapter.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-VOC-006: Image Publication

**Owner:** Telegram Adapter (or Administrator)

**Reason:** Image Publication is a TELEGRAM-SPECIFIC concept.

**Decision Maker:** Administrator (creates image publication)

**Executor:** Telegram Channel (creates)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Telegram Adapter.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-VOC-007: Subscriber

**Owner:** Telegram Adapter (or Channel)

**Reason:** Subscriber is a TELEGRAM-SPECIFIC entity.

**Decision Maker:** Channel (manages subscribers)

**Executor:** Channel (manages)

**Close Before Publisher Spec?** NO — Channel scope.

**Move Outside?** YES — belongs to Channel.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.8

---

## GAP-VOC-008: Administrator

**Owner:** Telegram Adapter (or Channel)

**Reason:** Administrator is a TELEGRAM-SPECIFIC entity.

**Decision Maker:** Administrator (interacts)

**Executor:** Channel (handles administrator)

**Close Before Publisher Spec?** NO — Channel scope.

**Move Outside?** YES — belongs to Channel.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.8

---

## GAP-VOC-009: Issue

**Owner:** Publisher

**Reason:** Issue is a PUBLISHER concept (daily edition).

**Decision Maker:** Publisher (defines issue)

**Executor:** Publisher (manages issues)

**Close Before Publisher Spec?** YES — core Publisher terminology.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md §8

---

## GAP-VOC-010: Channel

**Owner:** Telegram Adapter (or Infrastructure)

**Reason:** Channel is a TELEGRAM-SPECIFIC or INFRASTRUCTURE concept.

**Decision Maker:** Adapter (defines channel)

**Executor:** Adapter (uses channel)

**Close Before Publisher Spec?** NO — Adapter scope.

**Move Outside?** YES — belongs to Adapter.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.8

---

# Vocabulary Gap Ownership Summary

| Gap ID | Term | Owner | Close Before Spec? | Move Outside? |
|--------|------|-------|-------------------|---------------|
| GAP-VOC-001 | Publication Package | Publisher | YES | NO |
| GAP-VOC-002 | Normalized Dataset | Parser | NO | YES |
| GAP-VOC-003 | Schedule Request | Publisher | YES | NO |
| GAP-VOC-004 | Graphic Request | Publisher | YES | NO |
| GAP-VOC-005 | Manual Publication | Telegram Adapter | NO | YES |
| GAP-VOC-006 | Image Publication | Telegram Adapter | NO | YES |
| GAP-VOC-007 | Subscriber | Channel | NO | YES |
| GAP-VOC-008 | Administrator | Channel | NO | YES |
| GAP-VOC-009 | Issue | Publisher | YES | NO |
| GAP-VOC-010 | Channel | Adapter | NO | YES |

---

# Traceability

| Gap | Source |
|-----|--------|
| GAP-VOC-001 to GAP-VOC-010 | CASE-GAP-001, TELEGRAM_PUBLISHING_CANONICAL_MODEL.md, TELEGRAM_PUBLICATION_LIFECYCLE.md |

---

**End of Vocabulary Gap Ownership**
