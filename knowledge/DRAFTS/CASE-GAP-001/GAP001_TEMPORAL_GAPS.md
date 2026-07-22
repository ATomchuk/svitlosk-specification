# Temporal Gaps

**Document Class:** Knowledge Gap Discovery

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document identifies temporal behavior that is missing from Publisher Knowledge Base.

---

# Temporal Gaps

## GAP-TEMP-001: Timer Mechanism

### Evidence

TELEGRAM_PUBLICATION_LIFECYCLE.md describes expiry but not the timer mechanism.

### Knowledge Base Status

NOT DOCUMENTED.

Timer mechanism for expiry is not described in Publisher Knowledge Base.

### Gap Type

Temporal mechanism not captured.

---

## GAP-TEMP-002: Expiry Timing

### Evidence

Architect Intent: "Tomorrow information disappears automatically before the end of the current day."

### Knowledge Base Status

PARTIALLY DOCUMENTED.

Expiry timing is mentioned but exact timing is not specified.

### Gap Type

Temporal detail not captured.

---

## GAP-TEMP-003: Scheduling Mechanism

### Evidence

TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §4.5: "Schedule Generator — Transforms normalized outage data into deterministic schedules."

### Knowledge Base Status

NOT DOCUMENTED.

Scheduling mechanism is not described in Publisher Knowledge Base.

### Gap Type

Temporal mechanism not captured.

---

## GAP-TEMP-004: Replacement Timing

### Evidence

TELEGRAM_PUBLICATION_LIFECYCLE.md §6.2: "Publications MAY be updated only when the normalized dataset changes."

### Knowledge Base Status

PARTIALLY DOCUMENTED.

Replacement timing is mentioned but exact timing is not specified.

### Gap Type

Temporal detail not captured.

---

## GAP-TEMP-005: Ordering Timing

### Evidence

TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md §4.7: "Information SHALL always be organized according to the territorial structure."

### Knowledge Base Status

PARTIALLY DOCUMENTED.

Ordering is mentioned but timing of ordering is not specified.

### Gap Type

Temporal detail not captured.

---

## GAP-TEMP-006: Archive Timing

### Evidence

TELEGRAM_PUBLICATION_LIFECYCLE.md §5.4: "A Published Publication becomes Archived when the reporting period ends."

### Knowledge Base Status

PARTIALLY DOCUMENTED.

Archive timing is mentioned but exact timing is not specified.

### Gap Type

Temporal detail not captured.

---

## GAP-TEMP-007: Graph Generation Timing

### Evidence

Architect Context: "Graph Generator → SVG → PNG"

### Knowledge Base Status

NOT DOCUMENTED.

Graph generation timing is not described in Publisher Knowledge Base.

### Gap Type

Temporal mechanism not captured.

---

## GAP-TEMP-008: Technical Message Update Timing

### Evidence

Architect Intent: "Technical messages always show latest update timestamp."

### Knowledge Base Status

NOT DOCUMENTED.

Technical message update timing is not described in Publisher Knowledge Base.

### Gap Type

Temporal mechanism not captured.

---

# Temporal Gap Summary

| Gap ID | Temporal Aspect | Gap Type | Priority |
|--------|-----------------|----------|----------|
| GAP-TEMP-001 | Timer Mechanism | Temporal mechanism | HIGH |
| GAP-TEMP-002 | Expiry Timing | Temporal detail | MEDIUM |
| GAP-TEMP-003 | Scheduling Mechanism | Temporal mechanism | MEDIUM |
| GAP-TEMP-004 | Replacement Timing | Temporal detail | MEDIUM |
| GAP-TEMP-005 | Ordering Timing | Temporal detail | LOW |
| GAP-TEMP-006 | Archive Timing | Temporal detail | MEDIUM |
| GAP-TEMP-007 | Graph Generation Timing | Temporal mechanism | MEDIUM |
| GAP-TEMP-008 | Technical Message Update Timing | Temporal mechanism | LOW |

---

# Traceability

| Gap | Source |
|-----|--------|
| GAP-TEMP-001 to GAP-TEMP-008 | TELEGRAM_PUBLICATION_LIFECYCLE.md, TELEGRAM_PUBLISHING_CANONICAL_MODEL.md, Architect Intent |

---

**End of Temporal Gaps**
