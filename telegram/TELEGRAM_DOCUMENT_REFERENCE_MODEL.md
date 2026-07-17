# Telegram Document Reference Model

**Date:** 2026-07-13
**Scope:** Canonical reference model for Telegram documentation
**Status:** MODEL DESIGNED

---

# Purpose

This document defines the canonical approach for referencing Telegram documents.

---

# Reference Model

## Recommended Reference Format

When one document references another, the reference SHALL use:

```
TJS-XXX — Document Title
```

**Example:**
```
TJS-001 — Journal Concept
TJS-004 — Editorial Policy
TJS-005 — Message Templates
TJS-006 — Rendering Rules
```

---

## Why Document ID + Title?

| Criterion | Document ID Only | Title Only | ID + Title |
|-----------|-----------------|------------|------------|
| Permanent | YES | NO | YES |
| Human-readable | NO | YES | YES |
| Unique | YES | MAYBE | YES |
| Stable | YES | NO | YES |
| Traceable | YES | NO | YES |

**Document ID + Title** provides:
- Permanence (ID)
- Readability (Title)
- Uniqueness (ID)
- Stability (ID)
- Traceability (ID + Title)

---

## Reference Rules

### Rule R-REF-01: Primary Reference Uses Document ID

**Statement:** When one document references another, the primary reference SHALL use the Document ID.

**Format:** `TJS-XXX`

**Example:** `TJS-001`

---

### Rule R-REF-02: Extended Reference Uses ID + Title

**Statement:** For human-readable references, the Document ID SHALL be followed by the Document Title.

**Format:** `TJS-XXX — Document Title`

**Example:** `TJS-001 — Journal Concept`

---

### Rule R-REF-03: Foundational References Use Full Name

**Statement:** Foundational documents SHALL be referenced by their full file name when the context requires clarity.

**Format:** `TELEGRAM_SEMANTIC_MODEL.md (TJS-000)`

**Example:** `TELEGRAM_SEMANTIC_MODEL.md (TJS-000)`

---

### Rule R-REF-04: Dependency Graph Uses Document ID

**Statement:** The dependency graph SHALL use Document IDs for all nodes.

**Format:** `TJS-001 → TJS-002 → TJS-003`

**Example:** `TJS-001 → TJS-004 → TJS-005`

---

### Rule R-REF-05: Section References Use § Notation

**Statement:** References to specific sections SHALL use the § notation.

**Format:** `TJS-001 §4`

**Example:** `TJS-001 §4 (Mission)`

---

# Reference Format Summary

| Context | Format | Example |
|---------|--------|---------|
| Formal reference | `TJS-XXX — Title` | `TJS-001 — Journal Concept` |
| Dependency graph | `TJS-XXX → TJS-YYY` | `TJS-001 → TJS-004` |
| Section reference | `TJS-XXX §N` | `TJS-001 §4` |
| Foundational reference | `FILENAME.md (TJS-XXX)` | `TELEGRAM_GLOSSARY.md (TJS-000A)` |
| Informal reference | `TJS-XXX` | `TJS-001` |

---

# Reference Anti-Patterns

The following reference patterns SHALL NOT be used:

| Anti-Pattern | Reason |
|-------------|--------|
| `TJS-002 — Editorial Policy` (when current is Publication Lifecycle) | Wrong ID for current state |
| `TJS-003 — Message Templates` (when current is Post Structure) | Wrong ID for current state |
| `TJS-004 — Rendering Rules` (when current is Editorial Policy) | Wrong ID for current state |
| `TJS-005 — Publication Lifecycle` (when current is Message Templates) | Wrong ID for current state |
| `TJS-006 — Channel Management` (when current is Rendering Rules) | Wrong ID for current state |
| `TJS-007 — Graphic Rendering` (when current is Publication Lifecycle) | Wrong ID for current state |

---

# Reference Model Summary

| Principle | Statement |
|-----------|-----------|
| Primary identifier | Document ID (TJS-XXX) |
| Human-readable identifier | Document Title |
| Permanent reference | Document ID |
| Cross-reference format | `TJS-XXX — Title` |
| Dependency format | `TJS-XXX → TJS-YYY` |
| Section format | `TJS-XXX §N` |

---

**End of Reference Model**

**Designer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
