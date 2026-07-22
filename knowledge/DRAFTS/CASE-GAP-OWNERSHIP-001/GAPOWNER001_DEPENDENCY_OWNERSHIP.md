# Dependency Gap Ownership

**Document Class:** Gap Ownership Analysis

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines ownership for every dependency gap from CASE-GAP-001.

---

# Dependency Gap Ownership

## GAP-DEP-001: Parser → Publication Engine Dependency

**Owner:** Publisher

**Reason:** This is a PUBLISHER INPUT dependency.

**Decision Maker:** Publisher (determines when to receive data)

**Executor:** Parser (provides data)

**Close Before Publisher Spec?** YES — core Publisher input.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-002: Publication Engine → Adapter Dependency

**Owner:** Publisher

**Reason:** This is a PUBLISHER OUTPUT dependency.

**Decision Maker:** Publisher (determines when to distribute)

**Executor:** Adapter (receives publication)

**Close Before Publisher Spec?** YES — core Publisher output.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-003: Publication Engine → Schedule Generator Dependency

**Owner:** Publisher

**Reason:** This is a PUBLISHER REQUEST dependency.

**Decision Maker:** Publisher (determines when to request schedule)

**Executor:** Schedule Generator (provides schedule)

**Close Before Publisher Spec?** YES — Publisher interface.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-004: Publication Engine → Graphic Generator Dependency

**Owner:** Publisher

**Reason:** This is a PUBLISHER REQUEST dependency.

**Decision Maker:** Publisher (determines when to request graphic)

**Executor:** Graphic Generator (provides graphic)

**Close Before Publisher Spec?** YES — Publisher interface.

**Move Outside?** NO — Publisher scope.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-005: Publication Engine → Data Storage Dependency

**Owner:** Infrastructure

**Reason:** This is a PERSISTENCE dependency.

**Decision Maker:** System (determines when to store)

**Executor:** Data Storage (stores)

**Close Before Publisher Spec?** NO — Infrastructure.

**Move Outside?** YES — belongs to Infrastructure.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-006: Parser → Data Storage Dependency

**Owner:** Infrastructure

**Reason:** This is a PERSISTENCE dependency.

**Decision Maker:** System (determines when to store)

**Executor:** Data Storage (stores)

**Close Before Publisher Spec?** NO — Infrastructure.

**Move Outside?** YES — belongs to Infrastructure.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-007: Adapter → Channel Dependency

**Owner:** Telegram Adapter

**Reason:** This is a TELEGRAM-SPECIFIC dependency.

**Decision Maker:** Adapter (determines when to deliver)

**Executor:** Channel (receives)

**Close Before Publisher Spec?** NO — Telegram Adapter scope.

**Move Outside?** YES — belongs to Telegram Adapter.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-008: Channel → Subscribers Dependency

**Owner:** Telegram Adapter (or Channel)

**Reason:** This is a TELEGRAM-SPECIFIC dependency.

**Decision Maker:** Channel (manages subscribers)

**Executor:** Channel (delivers to subscribers)

**Close Before Publisher Spec?** NO — Channel scope.

**Move Outside?** YES — belongs to Channel.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-009: Administrators → Channel Dependency

**Owner:** Telegram Adapter (or Channel)

**Reason:** This is a TELEGRAM-SPECIFIC dependency.

**Decision Maker:** Administrator (interacts)

**Executor:** Channel (handles interaction)

**Close Before Publisher Spec?** NO — Channel scope.

**Move Outside?** YES — belongs to Channel.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5.1

---

## GAP-DEP-010: Circular Dependency Prevention

**Owner:** Publisher (or Architect)

**Reason:** Circular dependency prevention is an ARCHITECTURAL rule.

**Decision Maker:** Architect (defines rules)

**Executor:** Publisher (follows rules)

**Close Before Publisher Spec?** NO — Architectural governance.

**Move Outside?** YES — belongs to Architect governance.

**Evidence:** TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §6.18

---

# Dependency Gap Ownership Summary

| Gap ID | Dependency | Owner | Close Before Spec? | Move Outside? |
|--------|------------|-------|-------------------|---------------|
| GAP-DEP-001 | Parser → Publisher | Publisher | YES | NO |
| GAP-DEP-002 | Publisher → Adapter | Publisher | YES | NO |
| GAP-DEP-003 | Publisher → Schedule Generator | Publisher | YES | NO |
| GAP-DEP-004 | Publisher → Graphic Generator | Publisher | YES | NO |
| GAP-DEP-005 | Publisher → Data Storage | Infrastructure | NO | YES |
| GAP-DEP-006 | Parser → Data Storage | Infrastructure | NO | YES |
| GAP-DEP-007 | Adapter → Channel | Telegram Adapter | NO | YES |
| GAP-DEP-008 | Channel → Subscribers | Channel | NO | YES |
| GAP-DEP-009 | Administrators → Channel | Channel | NO | YES |
| GAP-DEP-010 | Circular Dependency Prevention | Architect | NO | YES |

---

# Traceability

| Gap | Source |
|-----|--------|
| GAP-DEP-001 to GAP-DEP-010 | CASE-GAP-001, TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §5, §6 |

---

**End of Dependency Gap Ownership**
