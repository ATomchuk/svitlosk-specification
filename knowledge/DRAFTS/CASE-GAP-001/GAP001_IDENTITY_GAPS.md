# Identity Gaps

**Document Class:** Knowledge Gap Discovery

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document identifies identifiers, keys, hashes, and temporary IDs that have never been described.

---

# Identity Gaps

## GAP-ID-001: Publication ID

### Evidence

TELEGRAM_PUBLICATION_LIFECYCLE.md references Publications but no explicit ID scheme.

### Knowledge Base Status

PARTIALLY DOCUMENTED.

Publication identity is mentioned but ID scheme is not described.

### Gap Type

Identity scheme not captured.

---

## GAP-ID-002: Telegram Message ID

### Evidence

Telegram Bot API returns message IDs for published messages.

### Knowledge Base Status

NOT DOCUMENTED.

Telegram Message ID is a channel-specific identifier not described in Publisher Knowledge Base.

### Gap Type

Channel-specific identity not captured.

---

## GAP-ID-003: Edition ID

### Evidence

TELEGRAM_PUBLICATION_LIFECYCLE.md §8: "An Issue opens when the first Publication for a calendar day is generated."

### Knowledge Base Status

NOT DOCUMENTED.

Edition/Issue ID is not described in Publisher Knowledge Base.

### Gap Type

Identity not captured.

---

## GAP-ID-004: Territory ID

### Evidence

TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md §4.7: "Information SHALL always be organized according to the territorial structure."

### Knowledge Base Status

PARTIALLY DOCUMENTED.

Territory identity is mentioned but ID scheme is not described.

### Gap Type

Identity scheme not captured.

---

## GAP-ID-005: Schedule ID

### Evidence

TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.5: "Schedule Generator — Transforms normalized outage data into deterministic schedules."

### Knowledge Base Status

NOT DOCUMENTED.

Schedule ID is not described in Publisher Knowledge Base.

### Gap Type

Identity not captured.

---

## GAP-ID-006: Graphic ID

### Evidence

TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.6: "Graphic Generator — Produces visual materials based on normalized outage schedules."

### Knowledge Base Status

NOT DOCUMENTED.

Graphic ID is not described in Publisher Knowledge Base.

### Gap Type

Identity not captured.

---

## GAP-ID-007: Hash for Change Detection

### Evidence

Implied by change detection mechanism.

### Knowledge Base Status

NOT DOCUMENTED.

Hash mechanism for change detection is not described in Publisher Knowledge Base.

### Gap Type

Identity mechanism not captured.

---

## GAP-ID-008: Temporary Identifiers

### Evidence

Implied by lifecycle transitions (Generated, Published, etc.).

### Knowledge Base Status

NOT DOCUMENTED.

Temporary identifiers during lifecycle are not described.

### Gap Type

Temporary identity not captured.

---

# Identity Gap Summary

| Gap ID | Identity | Gap Type | Priority |
|--------|----------|----------|----------|
| GAP-ID-001 | Publication ID | Identity scheme | MEDIUM |
| GAP-ID-002 | Telegram Message ID | Channel-specific identity | MEDIUM |
| GAP-ID-003 | Edition ID | Identity | MEDIUM |
| GAP-ID-004 | Territory ID | Identity scheme | LOW |
| GAP-ID-005 | Schedule ID | Identity | LOW |
| GAP-ID-006 | Graphic ID | Identity | LOW |
| GAP-ID-007 | Hash for Change Detection | Identity mechanism | MEDIUM |
| GAP-ID-008 | Temporary Identifiers | Temporary identity | LOW |

---

# Traceability

| Gap | Source |
|-----|--------|
| GAP-ID-001 to GAP-ID-008 | TELEGRAM_PUBLICATION_LIFECYCLE.md, TELEGRAM_PUBLISHING_CANONICAL_MODEL.md, TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md |

---

**End of Identity Gaps**
