# Telegram Publishing Duplication

**Date:** 2026-07-13
**Scope:** Detect duplicated concepts, responsibilities, principles, conflicting wording
**Status:** HARVEST COMPLETE

---

# Duplicated Concepts

## DC-001: Publication Lifecycle (Triple)

| Variant | Document | States |
|---------|----------|--------|
| Lifecycle Overview | TJS-002 §3 | 6 states: Generated, Scheduled, Published, Updated, Archived, Removed |
| Publication Lifecycle | TJS-007 §3 | 5 states: Dataset → Render → Publish → Update → Retain/Remove |
| Publication Cycle | TJS-008 §3 | 6 steps: generation, publication, monitoring, updating, generation, removal |

**Status:** RESOLVED by AD-001 (merge into TJS-005)

---

## DC-002: Publication Structure (Dual)

| Variant | Document | Structure |
|---------|----------|-----------|
| Standard Publication Structure | TJS-003 §3 | 5 sections: Header, Main, Graphic, Additional, Footer |
| Publication Grammar | TJS-005 §4 | Grammar tree: Territory Header → Sections → Settlement → Time → Street → Addresses |

**Status:** RESOLVED by AD-002 (absorb TJS-003 into TJS-005)

---

## DC-003: Formatting Rules (Triple)

| Variant | Document | Level |
|---------|----------|-------|
| Formatting Rules | TJS-003 §9 | General principles (spacing, typography) |
| Formatting | TJS-004 §11 | Policy (permitted types: bold + plain text) |
| Formatting Rules | TJS-005 §15 | Implementation (bold with `<b>` tag) |

**Status:** RESOLVED by AD-003 (TJS-002 owns policy, TJS-005 owns implementation)

---

## DC-004: Update Rules (Triple)

| Variant | Document | Conditions |
|---------|----------|-----------|
| Update Rules | TJS-002 §8 | 3 conditions: source change, formatting, graphics |
| Publication Updates | TJS-007 §5 | 2 conditions: dataset change, rendering change |
| Update Policy | TJS-008 §11 | 2 conditions: dataset change, rendering change |

**Status:** RESOLVED by AD-001 (merge into TJS-005)

---

## DC-005: Temporary Publications (Triple)

| Variant | Document | Scope |
|---------|----------|-------|
| Temporary Publications | TJS-002 §7 | 3 types: Tomorrow, Upcoming notice, Technical maintenance |
| Tomorrow Publications | TJS-007 §8 | 1 type: Tomorrow only |
| Tomorrow Publications | TJS-008 §12 | 1 type: Tomorrow only |

**Status:** RESOLVED by AD-001 (merge into TJS-005)

---

# Duplicated Responsibilities

| Responsibility | Component A | Component B | Status |
|---------------|-------------|-------------|--------|
| Lifecycle states | TJS-002 (before merge) | TJS-007 (before merge) | RESOLVED by AD-001 |
| Update rules | TJS-002 (before merge) | TJS-007 (before merge) | RESOLVED by AD-001 |
| Publication structure | TJS-003 (Post Structure) | TJS-005 (Message Templates) | RESOLVED by AD-002 |
| Formatting rules | TJS-003, TJS-004, TJS-005 | — | RESOLVED by AD-003 |

**All duplicated responsibilities have been resolved by approved Architecture Decisions.**

---

# Duplicated Principles

| Principle | Document A | Document B | Status |
|-----------|-----------|-----------|--------|
| Deterministic Rendering | TG §14 | TJS-006 §3 | ACCEPTABLE — same principle, different abstraction levels |
| Non-destructive Update | TG §11 | TJS-008 §10 | ACCEPTABLE — same principle, different abstraction levels |
| Canonical Equality | TG §11 | TJS-006 §3 | ACCEPTABLE — same principle, different abstraction levels |

**No duplicated principles require resolution.** The duplicates are at different abstraction levels (Glossary definition vs specification implementation).

---

# Conflicting Wording

## CW-001: Settlement Ordering Conflict

| Document | Rule |
|----------|------|
| TJS-005 §7 | "Alphabetical sorting is prohibited" |
| TJS-006 §7 | "Settlements SHALL be ordered alphabetically" |

**Status:** UNRESOLVED — requires ADR (DD-001)

---

## CW-002: Lifecycle State Counts

| Document | Count |
|----------|-------|
| TJS-002 §3 | 6 states |
| TJS-007 §3 | 5 states |
| TJS-008 §3 | 6 steps |

**Status:** RESOLVED by AD-001 (merge into TJS-005)

---

## CW-003: Update Condition Counts

| Document | Count |
|----------|-------|
| TJS-002 §8 | 3 conditions |
| TJS-007 §5 | 2 conditions |
| TJS-008 §11 | 2 conditions |

**Status:** RESOLVED by AD-001 (merge into TJS-005)

---

# Duplication Summary

| Category | Detected | Resolved | Unresolved |
|----------|----------|----------|------------|
| Duplicated concepts | 5 | 5 | 0 |
| Duplicated responsibilities | 4 | 4 | 0 |
| Duplicated principles | 3 | 0 (acceptable) | 0 |
| Conflicting wording | 3 | 2 | 1 (CW-001) |

---

**End of Duplication Report**

**Harvester:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
