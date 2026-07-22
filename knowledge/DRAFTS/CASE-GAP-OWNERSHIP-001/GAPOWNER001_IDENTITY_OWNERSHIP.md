# Identity Gap Ownership

**Document Class:** Gap Ownership Analysis

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines ownership for every identity gap from CASE-GAP-001.

---

# Identity Gap Ownership

## GAP-ID-001: Publication ID

**Owner:** Publisher

**Reason:** Publication ID is a PUBLICATION identity.

**Decision Maker:** Publisher (defines ID scheme)

**Executor:** Publisher (generates IDs)

**Close Before Publisher Spec?** YES — core Publisher concept.

**Move Outside?** NO — Publisher scope.

**Evidence:** CASE-PUB-001, CASE-INFPROD-001

---

## GAP-ID-002: Telegram Message ID

**Owner:** Telegram Adapter

**Reason:** Telegram Message ID is a TELEGRAM-SPECIFIC identifier.

**Decision Maker:** Telegram Bot API (generates IDs)

**Executor:** Telegram Adapter (manages IDs)

**Close Before Publisher Spec?** NO — Telegram Adapter scope.

**Move Outside?** YES — belongs to Telegram Adapter.

**Evidence:** Telegram Bot API

---

## GAP-ID-003: Edition ID

**Owner:** Publisher

**Reason:** Edition ID is a PUBLICATION identity.

**Decision Maker:** Publisher (defines ID scheme)

**Executor:** Publisher (generates IDs)

**Close Before Publisher Spec?** YES — core Publisher concept.

**Move Outside?** NO — Publisher scope.

**Evidence:** CASE-JRN-001, CASE-INFPROD-001

---

## GAP-ID-004: Territory ID

**Owner:** Infrastructure (or Territorial Model)

**Reason:** Territory ID is a REFERENCE identity.

**Decision Maker:** Territorial Model (defines IDs)

**Executor:** Territorial Model (manages IDs)

**Close Before Publisher Spec?** NO — Reference data.

**Move Outside?** YES — belongs to Territorial Model.

**Evidence:** GLOSSARY §4, TERRITORIAL_MODEL.md

---

## GAP-ID-005: Schedule ID

**Owner:** Parser (or Schedule Generator)

**Reason:** Schedule ID is a DATA PROCESSING identity.

**Decision Maker:** Parser (defines ID scheme)

**Executor:** Schedule Generator (generates IDs)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Parser or Schedule Generator.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.5

---

## GAP-ID-006: Graphic ID

**Owner:** Adapter (or Rendering Engine)

**Reason:** Graphic ID is a RENDERING identity.

**Decision Maker:** Publisher (determines when to generate)

**Executor:** Graphic Generator (generates IDs)

**Close Before Publisher Spec?** NO — outside Publisher scope.

**Move Outside?** YES — belongs to Adapter or Rendering Engine.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.6

---

## GAP-ID-007: Hash for Change Detection

**Owner:** Lifecycle

**Reason:** Hash for change detection is a LIFECYCLE mechanism.

**Decision Maker:** Lifecycle (determines when to hash)

**Executor:** Lifecycle (generates hashes)

**Close Before Publisher Spec?** YES — core Lifecycle behavior.

**Move Outside?** NO — Lifecycle scope.

**Evidence:** CASE-LC-001

---

## GAP-ID-008: Temporary Identifiers

**Owner:** Publisher

**Reason:** Temporary identifiers are PUBLICATION lifecycle artifacts.

**Decision Maker:** Publisher (manages temporary IDs)

**Executor:** Publisher (generates temporary IDs)

**Close Before Publisher Spec?** YES — core Publisher behavior.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md

---

# Identity Gap Ownership Summary

| Gap ID | Identity | Owner | Close Before Spec? | Move Outside? |
|--------|----------|-------|-------------------|---------------|
| GAP-ID-001 | Publication ID | Publisher | YES | NO |
| GAP-ID-002 | Telegram Message ID | Telegram Adapter | NO | YES |
| GAP-ID-003 | Edition ID | Publisher | YES | NO |
| GAP-ID-004 | Territory ID | Territorial Model | NO | YES |
| GAP-ID-005 | Schedule ID | Parser | NO | YES |
| GAP-ID-006 | Graphic ID | Adapter/Rendering | NO | YES |
| GAP-ID-007 | Hash for Change Detection | Lifecycle | YES | NO |
| GAP-ID-008 | Temporary Identifiers | Publisher | YES | NO |

---

# Traceability

| Gap | Source |
|-----|--------|
| GAP-ID-001 to GAP-ID-008 | CASE-GAP-001, TELEGRAM_PUBLICATION_LIFECYCLE.md, TELEGRAM_PUBLISHING_CANONICAL_MODEL.md |

---

**End of Identity Gap Ownership**
