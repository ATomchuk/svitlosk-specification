# Telegram Semantic Responsibility Decision Matrix

**Date:** 2026-07-13
**Source:** TELEGRAM_SEMANTIC_RESPONSIBILITY_AUDIT.md + FINDINGS.md
**Scope:** Architectural decisions for every detected overlap

---

## Decision Matrix

For every overlap, the matrix answers:
1. Do both documents own the same responsibility?
2. Would merging improve the architecture?
3. Would merging violate Separation of Concerns?
4. Would merging reduce clarity?
5. Recommended decision + justification

---

## Lifecycle Overlaps (TJS-002, TJS-007, TJS-008)

### M-001: Lifecycle State Model

| | TJS-002 §3 | TJS-007 §3 | TJS-008 §3 |
|---|-----------|-----------|-----------|
| States | 6 (Generated, Scheduled, Published, Updated, Archived, Removed) | 5 (Dataset → Render → Publish → Update → Retain/Remove) | 6 steps (generation, publication, monitoring, updating, Tomorrow generation, Tomorrow removal) |
| Model type | State-based | Flow-based | Cycle-based |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** |
| Would merging improve the architecture? | **YES** — eliminates three conflicting state models |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** |

**Justification:** Three documents defining three different lifecycle state models is a critical architectural violation. A single document must own the authoritative lifecycle state model. The merged document would present ONE unified model that incorporates the best aspects of all three: the state-based clarity of TJS-002, the operational flow of TJS-007, and the temporal cycle of TJS-008.

---

### M-002: Update Rules

| | TJS-002 §8 | TJS-007 §5 | TJS-008 §11 |
|---|-----------|-----------|-----------|
| Conditions | 3 (source change, formatting correction, graphic regeneration) | 2 (dataset change, rendering change) | 2 (dataset change, rendering change) |
| Scope | Broad (includes formatting) | Narrow (dataset/rendering only) | Narrow (dataset/rendering only) |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** |
| Would merging improve the architecture? | **YES** — eliminates conflicting update conditions |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** |

**Justification:** The discrepancy between 3 conditions (TJS-002) and 2 conditions (TJS-007/008) creates architectural ambiguity. Can formatting corrections trigger updates? The merged document would define the complete, authoritative set of update conditions.

---

### M-003: Temporary Publications

| | TJS-002 §7 | TJS-007 §8 | TJS-008 §12 |
|---|-----------|-----------|-----------|
| Types | 3 (Tomorrow schedule, Upcoming notice, Technical maintenance) | 1 (Tomorrow Publications) | 1 (Tomorrow Publications) |
| Scope | Broad | Narrow | Narrow |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** |
| Would merging improve the architecture? | **YES** — eliminates conflicting definitions |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** |

---

### M-004: Archive/Permanent Rules

| | TJS-002 §9 | TJS-007 §9 |
|---|-----------|-----------|
| Concept | Archive Policy (historical preservation) | Permanent Publications (current-day preservation) |
| Scope | Historical records | Current-day posts |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **PARTIALLY** — related preservation concepts |
| Would merging improve the architecture? | **YES** — one document owns all preservation rules |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** |

**Justification:** Archive policy and permanent classification are both preservation rules at different lifecycle stages. One document should own all preservation rules: what is permanent, what is temporary, what is archived, and what may be deleted.

---

### M-005: Temporary vs Permanent Classification

| | TJS-002 §5,§9 | TJS-007 §8,§9 | TJS-008 §12 |
|---|-----------|-----------|-----------|
| Permanent | Daily schedule never deleted; emergency remains available | Current-day Publications remain | — |
| Temporary | Tomorrow, Upcoming, Technical maintenance | Tomorrow Publications only | Tomorrow Publications only |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** |
| Would merging improve the architecture? | **YES** |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** |

---

### M-006: Lifecycle Diagrams

| | TJS-007 §12 | TJS-008 §16-17 |
|---|-----------|-----------|
| Diagram type | Operational flow | Temporal cycle + Architecture |
| Content | Parser → Engine → Publisher → Create/Update/Delete | 00:00 → 05:00 → Generate → Publish → Monitor → Update → Tomorrow |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **PARTIALLY** — different diagram purposes |
| Would merging improve the architecture? | **YES** — all lifecycle diagrams in one place |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** |

---

## Structure Overlaps (TJS-003, TJS-005)

### M-007: Publication Structure

| | TJS-003 §3-8 | TJS-005 §4-12 |
|---|-----------|-----------|
| Level | Conceptual (5 sections) | Normative (grammar tree, canonical templates) |
| Detail | High-level overview | Detailed implementation rules |
| Templates | None | 4 canonical templates (A-D) |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** |
| Would merging improve the architecture? | **YES** — eliminates dual ownership |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** (absorb TJS-003 into TJS-005) |

**Justification:** TJS-005 is strictly more detailed and more authoritative. TJS-003's unique content (Graphic block concept, Additional information, Footer, Editing rules) can be absorbed as additional sections.

---

### M-008: Header Definition

| | TJS-003 §4 | TJS-005 §5 |
|---|-----------|-----------|
| Content | Publication type, date, affected schedule | Territory Header (uppercase) |
| Scope | What the header contains | How to render the header |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** |
| Would merging improve the architecture? | **YES** |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** |

---

## Formatting Overlaps (TJS-003, TJS-004, TJS-005)

### M-009: Formatting Rules

| | TJS-003 §9 | TJS-004 §11 | TJS-005 §15 |
|---|-----------|-----------|-----------|
| Level | General principles | Policy (permitted types) | Implementation (<b> tag) |
| Content | Short paragraphs, spacing, emoji, typography | Bold + plain text only | Bold (<b>), no other formatting |
| Authority | Conceptual | Approved (highest authority) | Draft |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** |
| Would merging improve the architecture? | **YES** — clear ownership hierarchy |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** (establish clear hierarchy: TJS-004 = policy, TJS-005 = implementation) |

**Justification:** The resolution is to establish: TJS-004 owns formatting POLICY (what is permitted). TJS-005 owns formatting IMPLEMENTATION (how to render in Telegram HTML). TJS-003's formatting rules are subsumed by TJS-004.

---

## Editorial vs Template Overlaps (TJS-004, TJS-005)

### M-010: Territory Presentation

| | TJS-004 §3 | TJS-005 §5 |
|---|-----------|-----------|
| Rule | Uppercase, first element | Uppercase Territory Header |
| Level | Policy | Implementation |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** — different abstraction levels |
| Would merging improve the architecture? | **NO** |
| Would merging violate Separation of Concerns? | **YES** — mixing policy and implementation |
| Would merging reduce clarity? | **YES** |
| Recommended decision | **KEEP SEPARATE** |

**Justification:** TJS-004 owns the editorial POLICY. TJS-005 IMPLEMENTS that policy in concrete templates. This is NORMAL cross-document cooperation. The relationship should be explicitly documented.

---

### M-011: Time Format

| | TJS-004 §8 | TJS-005 §9 |
|---|-----------|-----------|
| Rule | Emoji + HH:MM–HH:MM | Single-day: 🕘 HH:MM–HH:MM; Multi-day: dates |
| Level | Policy | Implementation (extended) |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** — different abstraction levels |
| Would merging improve the architecture? | **NO** |
| Would merging violate Separation of Concerns? | **YES** |
| Would merging reduce clarity? | **YES** |
| Recommended decision | **KEEP SEPARATE** |

---

### M-012: Settlement Formatting

| | TJS-004 §9 | TJS-005 §10 |
|---|-----------|-----------|
| Rule | Bold, no prefix | Bold, no prefix, <b> tag |
| Level | Policy | Implementation |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** |
| Would merging improve the architecture? | **NO** |
| Would merging violate Separation of Concerns? | **YES** |
| Would merging reduce clarity? | **YES** |
| Recommended decision | **KEEP SEPARATE** |

---

### M-013: Address Formatting

| | TJS-004 §10 | TJS-005 §11-12 |
|---|-----------|-----------|
| Rule | Preserve abbreviations, line by line | Preserve abbreviations, one line per street |
| Level | Policy | Implementation (more specific) |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** |
| Would merging improve the architecture? | **NO** |
| Would merging violate Separation of Concerns? | **YES** |
| Would merging reduce clarity? | **YES** |
| Recommended decision | **KEEP SEPARATE** |

---

### M-014: Category Titles

| | TJS-004 §6 | TJS-005 §6 |
|---|-----------|-----------|
| Rule | Emoji indicators, bold | Emoji + Ukrainian labels |
| Level | Policy | Implementation |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** |
| Would merging improve the architecture? | **NO** |
| Would merging violate Separation of Concerns? | **YES** |
| Would merging reduce clarity? | **YES** |
| Recommended decision | **KEEP SEPARATE** |

---

## Rendering Overlaps (TJS-005, TJS-006)

### M-015: Settlement Ordering (CONFLICT)

| | TJS-005 §7 | TJS-006 §7 |
|---|-----------|-----------|
| Rule | Canonical TERRITORIAL_MODEL.md order | Alphabetical (Ukrainian alphabet) |
| Constraint | "Alphabetical sorting is PROHIBITED" | "SHALL be ordered alphabetically" |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** — directly conflicting |
| Would merging improve the architecture? | N/A — conflict resolution required first |
| Would merging violate Separation of Concerns? | N/A |
| Would merging reduce clarity? | N/A |
| Recommended decision | **RESTRUCTURE** |

**Justification:** This is a semantic CONFLICT, not just duplication. Two documents define mutually exclusive ordering rules. This requires an architectural decision:
- Option A: TERRITORIAL_MODEL.md canonical order is authoritative (TJS-005 is correct)
- Option B: Alphabetical order is authoritative (TJS-006 is correct)
- Option C: Different scopes (content order vs display order) — requires clarification

The resolution must be documented as an architectural decision.

---

### M-016: Time Ordering

| | TJS-005 §8 | TJS-006 §6 |
|---|-----------|-----------|
| Rule | Sorted by start time | Sorted by start time |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** — same fact, different context |
| Would merging improve the architecture? | **NO** |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **KEEP SEPARATE** (required evidence) |

---

### M-017: Duplicate Removal

| | TJS-005 §12 | TJS-006 §9 |
|---|-----------|-----------|
| Rule | No duplicate addresses | No duplicate addresses |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** — same fact, different context |
| Would merging improve the architecture? | **NO** |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **KEEP SEPARATE** (required evidence) |

---

## Non-Destructive Principles (TJS-007, TJS-008)

### M-018: Non-Destructive Channel vs Non-Destructive Update

| | TJS-007 §11 | TJS-008 §10 |
|---|-----------|-----------|
| Principle | Don't touch others' posts (channel ownership) | Update in place, don't recreate (update strategy) |
| Scope | WHAT you may touch | HOW you may change it |

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** — different principles |
| Would merging improve the architecture? | **YES** — both belong in lifecycle document |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** (into unified Publication Lifecycle) |

---

## Decision Summary

| Decision | Count | Findings |
|----------|-------|----------|
| **MERGE** | 12 | M-001, M-002, M-003, M-004, M-005, M-006, M-007, M-008, M-009, M-018 |
| **KEEP SEPARATE** | 6 | M-010, M-011, M-012, M-013, M-014, M-016, M-017 |
| **RESTRUCTURE** | 1 | M-015 |
| **SPLIT** | 0 | — |
| **RENAME** | 0 | — |

---

## Architectural Impact

### Documents Affected by MERGE Decisions

| Document | Action | Merges From |
|----------|--------|-------------|
| TJS-005 (Proposed) — Publication Lifecycle | CREATE (merged) | TJS-002 + TJS-007 + TJS-008 |
| TJS-003 (Proposed) — Message Templates | ABSORB | TJS-003 (current) |
| TJS-004 (Proposed) — Editorial Policy | RETAIN | TJS-004 (current) — absorbs TJS-003 formatting |

### Documents Affected by KEEP SEPARATE Decisions

| Document | Action | Rationale |
|----------|--------|-----------|
| TJS-004 (Proposed) — Editorial Policy | RETAIN | Policy-level ownership confirmed |
| TJS-005 (Proposed) — Message Templates | RETAIN | Implementation-level ownership confirmed |

### Documents Affected by RESTRUCTURE Decisions

| Document | Action | Issue |
|----------|--------|-------|
| TJS-005 (Proposed) vs TJS-006 (Proposed) | RESOLVE CONFLICT | Settlement ordering must be clarified |

---

**End of Decision Matrix**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
