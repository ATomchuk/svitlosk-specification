# Telegram Document Reference Update Plan

**Date:** 2026-07-13
**Scope:** Canonical strategy for updating references
**Status:** PLAN DESIGNED

---

# Purpose

This document defines the canonical strategy for updating references after file moves.

---

# Reference Update Strategy

## Strategy: Hybrid (After Each Phase)

References SHALL be updated in two stages:

1. **Immediate:** Update internal references within moved documents (during each phase)
2. **Comprehensive:** Update all cross-references after complete migration (Phase 9)

---

# Reference Update Rules

## Rule RU-001: Internal References Update Immediately

When a document is moved, its internal references (Depends on, Referenced by) SHALL be updated immediately to reflect the new location.

## Rule RU-002: Cross-References Update After Migration

References BETWEEN documents SHALL be updated after all documents have been moved (Phase 9).

## Rule RU-003: Legacy References Remain Stable

Legacy documents (TJS-001 through TJS-008) SHALL NOT have their references updated. They are historical references.

## Rule RU-004: Foundation References Are Permanent

Foundation documents (TJS-000, TJS-000A) SHALL NOT have their Document IDs changed. Only file locations change.

---

# Reference Update Sequence

```
Phase 3: Foundation moved
    ↓
    Update Foundation internal references
    ↓
Phase 4: Architecture moved
    ↓
    Update Architecture internal references
    ↓
Phase 5: Publishing moved
    ↓
    Update Publishing internal references
    ↓
Phase 6: Editorial moved
    ↓
    Update Editorial internal references
    ↓
Phase 7: Lifecycle and Legacy moved
    ↓
    Update Lifecycle internal references
    ↓
Phase 8: Processes and Reference moved
    ↓
    Update Process and Reference internal references
    ↓
Phase 9: Comprehensive cross-reference update
    ↓
    Update ALL cross-references between documents
    ↓
Phase 10: Verification
```

---

# Reference Format

| Context | Format | Example |
|---------|--------|---------|
| Depends on | `Document Name (Doc ID)` | `TELEGRAM_GLOSSARY.md (TJS-000A)` |
| Referenced by | `Document Name (Doc ID)` | `TELEGRAM_ARCHITECTURE_DECISION.md` |
| Section reference | `Document §Section` | `TJS-001 §4` |
| Dependency graph | `TJS-XXX → TJS-YYY` | `TJS-001 → TJS-004` |

---

# Reference Update Checklist

| Check | Phase | Status |
|-------|-------|--------|
| Foundation internal references updated | Phase 3 | PENDING |
| Architecture internal references updated | Phase 4 | PENDING |
| Publishing internal references updated | Phase 5 | PENDING |
| Editorial internal references updated | Phase 6 | PENDING |
| Lifecycle internal references updated | Phase 7 | PENDING |
| Process and Reference internal references updated | Phase 8 | PENDING |
| All cross-references updated | Phase 9 | PENDING |
| All references verified | Phase 10 | PENDING |

---

**End of Reference Update Plan**

**Planner:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
