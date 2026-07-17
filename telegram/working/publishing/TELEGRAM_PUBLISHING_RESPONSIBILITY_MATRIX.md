# Telegram Publishing Responsibility Matrix

**Date:** 2026-07-13
**Scope:** Map every responsibility to exactly one component
**Status:** HARVEST COMPLETE

---

| Responsibility | Owner Component | Source | Duplicate? | Missing? |
|---------------|----------------|--------|------------|----------|
| Journal identity | TJS-001 (Journal Concept) | TJS-001 §9 | NO | NO |
| Journal mission | TJS-001 (Journal Concept) | TJS-001 §4 | NO | NO |
| Journal principles | TJS-001 (Journal Concept) | TJS-001 §7 | NO | NO |
| Editorial policy | TJS-002 (Editorial Policy) | TJS-004 §Editorial | NO | NO |
| Formatting policy | TJS-002 (Editorial Policy) | TJS-004 §Formatting | NO | NO |
| Territory rules | TJS-002 (Editorial Policy) | TJS-004 §Territory | NO | NO |
| Publication templates | TJS-003 (Message Templates) | TJS-005 §13 | NO | NO |
| Publication structure | TJS-003 (Message Templates) | TJS-005 §4 | NO | NO |
| Formatting implementation | TJS-003 (Message Templates) | TJS-005 §15 | NO | NO |
| Validation rules | TJS-003 (Message Templates) | TJS-005 §14 | NO | NO |
| Rendering pipeline | TJS-004 (Rendering Rules) | TJS-006 §4 | NO | NO |
| Sorting algorithms | TJS-004 (Rendering Rules) | TJS-006 §5-8 | NO | NO |
| HTML generation | TJS-004 (Rendering Rules) | TJS-006 §11 | NO | NO |
| Lifecycle states | TJS-005 (Publication Lifecycle) | TJS-002 §3, TJS-007 §3, TJS-008 §3 | NO (after merge) | NO |
| Update rules | TJS-005 (Publication Lifecycle) | TJS-002 §8, TJS-007 §5, TJS-008 §11 | NO (after merge) | NO |
| Publication types | TJS-005 (Publication Lifecycle) | TJS-002 §4 | NO | NO |
| Ownership model | TJS-005 (Publication Lifecycle) | TJS-007 §10 | NO | NO |
| Non-destructive principles | TJS-005 (Publication Lifecycle) | TJS-007 §11, TJS-008 §10 | NO | NO |
| Daily cycle | TJS-005 (Publication Lifecycle) | TJS-008 §3 | NO | NO |
| Publication windows | TJS-005 (Publication Lifecycle) | TJS-008 §6 | NO | NO |
| Archive policy | TJS-005 (Publication Lifecycle) | TJS-002 §9 | NO | NO |
| Deletion policy | TJS-005 (Publication Lifecycle) | TJS-002 §10 | NO | NO |
| Traceability | TJS-005 (Publication Lifecycle) | TJS-002 §11 | NO | NO |
| Error handling | TJS-005 (Publication Lifecycle) | TJS-007 §13 | NO | NO |
| Channel management | TJS-006 (Channel Management) | TJS-006 (proposed) | NO | NO |
| Graphic rendering | TJS-007 (Graphic Rendering) | TJS-007 (proposed) | NO | NO |

---

## Duplicate Ownership Detection

| Responsibility | Component A | Component B | Duplicate? |
|---------------|-------------|-------------|------------|
| Lifecycle states | TJS-002 (before merge) | TJS-007 (before merge) | YES — resolved by AD-001 |
| Update rules | TJS-002 (before merge) | TJS-007 (before merge) | YES — resolved by AD-001 |
| Temporary publications | TJS-002 (before merge) | TJS-007 (before merge) | YES — resolved by AD-001 |
| Publication structure | TJS-003 (Post Structure) | TJS-005 (Message Templates) | YES — resolved by AD-002 |
| Formatting rules | TJS-003, TJS-004, TJS-005 | — | YES — resolved by AD-003 |

**All duplicate ownership issues have been resolved by approved Architecture Decisions.**

---

## Missing Ownership Detection

| Responsibility | Owner | Status |
|---------------|-------|--------|
| Journal identity | TJS-001 | OWNED |
| Editorial policy | TJS-002 | OWNED |
| Publication templates | TJS-003 | OWNED |
| Rendering pipeline | TJS-004 | OWNED |
| Publication lifecycle | TJS-005 | OWNED |
| Channel management | TJS-006 | OWNED |
| Graphic rendering | TJS-007 | OWNED |

**All responsibilities have exactly one owner. No missing ownership detected.**

---

**End of Responsibility Matrix**

**Harvester:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
