# Telegram Migration Matrix

**Date:** 2026-07-13
**Purpose:** Complete knowledge transfer map — every section of every existing document
**Source:** TELEGRAM_ARCHITECTURE_DECISION.md (Approved)

---

## Migration Operations Summary

| Operation | Count |
|-----------|-------|
| KEEP | 4 |
| MOVE | 1 |
| MERGE | 3 |
| ABSORB | 12 |
| REMOVE | 4 |
| **Total operations** | **24** |

---

## TJS-001 — Journal Concept

**Destination:** TJS-001 (RETAIN)
**Action:** UPDATE metadata + update §12

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-001 §1 | Purpose | TJS-001 | §1 Purpose | KEEP |
| TJS-001 §2 | Scope | TJS-001 | §2 Scope | KEEP |
| TJS-001 §3 | Official Definition | TJS-001 | §3 Official Definition | KEEP |
| TJS-001 §4 | Mission | TJS-001 | §4 Mission | KEEP |
| TJS-001 §5 | Vision | TJS-001 | §5 Vision | KEEP |
| TJS-001 §6 | Editorial Philosophy | TJS-001 | §6 Editorial Philosophy | KEEP |
| TJS-001 §7 | Core Principles | TJS-001 | §7 Core Principles | KEEP |
| TJS-001 §8 | Audience | TJS-001 | §8 Audience | KEEP |
| TJS-001 §9 | Journal Identity | TJS-001 | §9 Journal Identity | KEEP |
| TJS-001 §10 | Role within SvitloSk | TJS-001 | §10 Role within SvitloSk | KEEP |
| TJS-001 §11 | Historical Archive | TJS-001 | §11 Historical Archive | KEEP |
| TJS-001 §12 | Future Specifications | TJS-001 | §12 Future Specifications | KEEP (UPDATE content) |
| TJS-001 metadata | Status, ID, Author | TJS-001 | Metadata | KEEP (ADD Document Class, References) |
| TJS-001 line 83 | "shall prioritize" (lowercase) | TJS-001 | §8 | KEEP (FIX to "SHALL") |

**TJS-001 §12 Updated Content:**

```markdown
# 12. Future Specifications

This document serves as the foundation for:

- TJS-002 — Editorial Policy
- TJS-003 — Message Templates
- TJS-004 — Rendering Rules
- TJS-005 — Publication Lifecycle
- TJS-006 — Channel Management
- TJS-007 — Graphic Rendering
```

---

## TJS-002 — Publication Lifecycle

**Destination:** TJS-005 (MERGED from TJS-002 + TJS-007 + TJS-008)
**Action:** MERGE + REMOVE file

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-002 §1 | Purpose | TJS-005 | §1 Purpose (unified) | MERGE |
| TJS-002 §2 | Scope | TJS-005 | §2 Scope (unified) | MERGE |
| TJS-002 §3 | Lifecycle Overview (6 states) | TJS-005 | §3 Lifecycle State Model (unified) | MERGE |
| TJS-002 §4 | Publication Types (7 categories) | TJS-005 | §4 Publication Types | ABSORB |
| TJS-002 §5 | Daily Schedule Lifecycle | TJS-005 | §5 Daily Schedule Lifecycle | ABSORB |
| TJS-002 §6 | Emergency Publications | TJS-005 | §6 Emergency Publications | ABSORB |
| TJS-002 §7 | Temporary Publications | TJS-005 | §7 Temporary Publications (unified) | MERGE |
| TJS-002 §8 | Update Rules (3 conditions) | TJS-005 | §8 Update Rules (unified) | MERGE |
| TJS-002 §9 | Archive Policy | TJS-005 | §9 Archive Policy | ABSORB |
| TJS-002 §10 | Deletion Policy | TJS-005 | §10 Deletion Policy | ABSORB |
| TJS-002 §11 | Traceability | TJS-005 | §11 Traceability | ABSORB |
| TJS-002 §12 | Reliability | TJS-005 | §12 Reliability | ABSORB |
| TJS-002 §13 | Future Specifications | TJS-005 | §13 References (corrected) | REMOVE (outdated) |
| TJS-002 metadata | Status, ID, Author | TJS-005 | Metadata | REMOVE (new file) |

**File operation:** REMOVE `TJS-002-Publication-Lifecycle.md`

---

## TJS-003 — Post Structure

**Destination:** TJS-003 Message Templates (ABSORB) + TJS-002 Editorial Policy (MOVE §9)
**Action:** ABSORB + MOVE + REMOVE file

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-003 §1 | Purpose | TJS-003 (Message Templates) | §1 Purpose (updated) | ABSORB |
| TJS-003 §2 | General Principles | TJS-003 (Message Templates) | §2 Design Goals (existing) | ABSORB (merge principles) |
| TJS-003 §3 | Standard Publication Structure | TJS-003 (Message Templates) | §17 Publication Structure (new) | ABSORB |
| TJS-003 §4 | Header | TJS-003 (Message Templates) | §18 Header (new) | ABSORB |
| TJS-003 §5 | Main Information | TJS-003 (Message Templates) | §19 Main Information (new) | ABSORB |
| TJS-003 §6 | Graphic Block | TJS-003 (Message Templates) | §20 Graphic Block (new) | ABSORB |
| TJS-003 §7 | Additional Information | TJS-003 (Message Templates) | §21 Additional Information (new) | ABSORB |
| TJS-003 §8 | Footer | TJS-003 (Message Templates) | §22 Footer (new) | ABSORB |
| TJS-003 §9 | Formatting Rules | TJS-002 (Editorial Policy) | §11 Formatting (existing) | MOVE |
| TJS-003 §10 | Editing Rules | TJS-003 (Message Templates) | §23 Editing Rules (new) | ABSORB |
| TJS-003 §11 | Future Specifications | TJS-003 (Message Templates) | §24 References (new) | ABSORB (corrected) |
| TJS-003 metadata | Status, ID, Author | TJS-003 (Message Templates) | Metadata | REMOVE (new file) |

**File operation:** REMOVE `TJS-003-Post-Structure.md`

---

## TJS-004 — Editorial Policy

**Destination:** TJS-002 (RETAIN — note: ID stays TJS-004 in current architecture, but Architecture Decision says TJS-002 is Editorial Policy)

**Correction:** The Architecture Decision keeps TJS-004 as Editorial Policy (AD-007: no renumbering). The current TJS-004 IS the Editorial Policy.

**Destination:** TJS-004 (RETAIN)
**Action:** UPDATE metadata + absorb TJS-003 §9

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-004 line 1-8 | Metadata (Status, ID, Component, Author) | TJS-004 | Metadata | KEEP (REMOVE Component field, ADD Document Class) |
| TJS-004 Purpose | Purpose | TJS-004 | Purpose | KEEP |
| TJS-004 Editorial Principles | Editorial Principles | TJS-004 | Editorial Principles | KEEP |
| TJS-004 Territory | Territory | TJS-004 | Territory | KEEP |
| TJS-004 Publication Package | Publication Package | TJS-004 | Publication Package | KEEP |
| TJS-004 Message Categories | Message Categories | TJS-004 | Message Categories | KEEP |
| TJS-004 Category Titles | Category Titles | TJS-004 | Category Titles | KEEP |
| TJS-004 Publications For Tomorrow | Publications For Tomorrow | TJS-004 | Publications For Tomorrow | KEEP |
| TJS-004 Time Format | Time Format | TJS-004 | Time Format | KEEP |
| TJS-004 Settlements | Settlements | TJS-004 | Settlements | KEEP |
| TJS-004 Addresses | Addresses | TJS-004 | Addresses | KEEP |
| TJS-004 Formatting | Formatting (permitted types) | TJS-004 | Formatting | KEEP |
| TJS-003 §9 | Formatting Rules (general principles) | TJS-004 | Formatting (extended) | MOVE |
| TJS-004 Update Information | Update Information | TJS-004 | Update Information | KEEP |
| TJS-004 Branding | Branding | TJS-004 | Branding | KEEP |
| TJS-004 Terminology | Terminology | TJS-004 | Terminology | KEEP |
| TJS-004 Automatic Generation | Automatic Generation | TJS-004 | Automatic Generation | KEEP |
| TJS-004 Compliance | Compliance | TJS-004 | Compliance | KEEP |
| TJS-004 line 7 | "Component: Editorial Policy" | TJS-004 | Metadata | REMOVE (non-standard field) |

---

## TJS-005 — Message Templates

**Destination:** TJS-003 (RETAIN — note: ID stays TJS-005 in current file, but Architecture Decision says TJS-003 is Message Templates)

**Correction:** The Architecture Decision keeps TJS-005 as Message Templates (AD-007: no renumbering). The current TJS-005 IS the Message Templates.

**Destination:** TJS-005 (RETAIN)
**Action:** UPDATE metadata + absorb TJS-003 Post Structure content

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-005 line 1-9 | Metadata (Status, ID, Project, Class) | TJS-005 | Metadata | KEEP (FIX: replace "Project"/"Class" with standard fields) |
| TJS-005 §1 | Purpose | TJS-005 | §1 Purpose | KEEP |
| TJS-005 §2 | Scope | TJS-005 | §2 Scope | KEEP |
| TJS-005 §3 | Design Goals | TJS-005 | §3 Design Goals | KEEP |
| TJS-005 §4 | Publication Grammar | TJS-005 | §4 Publication Grammar | KEEP |
| TJS-005 §5 | Territory Header | TJS-005 | §5 Territory Header | KEEP |
| TJS-005 §6 | Publication Sections | TJS-005 | §6 Publication Sections | KEEP |
| TJS-005 §7 | Settlement Ordering | TJS-005 | §7 Settlement Ordering | KEEP |
| TJS-005 §8 | Time Interval Ordering | TJS-005 | §8 Time Interval Ordering | KEEP |
| TJS-005 §9 | Time Interval Formatting | TJS-005 | §9 Time Interval Formatting | KEEP |
| TJS-005 §10 | Settlement Formatting | TJS-005 | §10 Settlement Formatting | KEEP |
| TJS-005 §11 | Street Formatting | TJS-005 | §11 Street Formatting | KEEP |
| TJS-005 §12 | Address Rules | TJS-005 | §12 Address Rules | KEEP |
| TJS-005 §13 | Canonical Templates | TJS-005 | §13 Canonical Templates | KEEP |
| TJS-005 §14 | Validation Rules | TJS-005 | §14 Validation Rules | KEEP |
| TJS-005 §15 | Formatting Rules (implementation) | TJS-005 | §15 Formatting Rules | KEEP |
| TJS-005 §16 | References | TJS-005 | §16 References (updated) | KEEP |
| TJS-003 §3 | Standard Publication Structure | TJS-005 | §17 Publication Structure (new) | ABSORB |
| TJS-003 §4 | Header | TJS-005 | §18 Header (new) | ABSORB |
| TJS-003 §5 | Main Information | TJS-005 | §19 Main Information (new) | ABSORB |
| TJS-003 §6 | Graphic Block | TJS-005 | §20 Graphic Block (new) | ABSORB |
| TJS-003 §7 | Additional Information | TJS-005 | §21 Additional Information (new) | ABSORB |
| TJS-003 §8 | Footer | TJS-005 | §22 Footer (new) | ABSORB |
| TJS-003 §10 | Editing Rules | TJS-005 | §23 Editing Rules (new) | ABSORB |

---

## TJS-006 — Rendering Rules

**Destination:** TJS-004 (RETAIN — note: ID stays TJS-006 in current file, but Architecture Decision says TJS-004 is Rendering Rules)

**Correction:** The Architecture Decision keeps TJS-006 as Rendering Rules (AD-007: no renumbering). The current TJS-006 IS the Rendering Rules.

**Destination:** TJS-006 (RETAIN)
**Action:** UPDATE metadata + fix reference

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-006 line 1-6 | Metadata (Status, ID, Project, Class) | TJS-006 | Metadata | KEEP (FIX: replace "Project"/"Class" with standard fields) |
| TJS-006 §1 | Purpose | TJS-006 | §1 Purpose | KEEP |
| TJS-006 §2 | Scope | TJS-006 | §2 Scope | KEEP |
| TJS-006 §3 | Rendering Principles | TJS-006 | §3 Rendering Principles | KEEP |
| TJS-006 §4 | Rendering Pipeline | TJS-006 | §4 Rendering Pipeline | KEEP |
| TJS-006 §5 | Territory Ordering | TJS-006 | §5 Territory Ordering | KEEP |
| TJS-006 §6 | Time Ordering | TJS-006 | §6 Time Ordering | KEEP |
| TJS-006 §7 | Settlement Ordering | TJS-006 | §7 Settlement Ordering | KEEP (DEFERRED: subject to ADR) |
| TJS-006 §8 | Street Ordering | TJS-006 | §8 Street Ordering | KEEP |
| TJS-006 §9 | Duplicate Removal | TJS-006 | §9 Duplicate Removal | KEEP |
| TJS-006 §10 | Long Publication Split | TJS-006 | §10 Long Publication Split | KEEP |
| TJS-006 §11 | HTML Rendering Rules | TJS-006 | §11 HTML Rendering Rules | KEEP |
| TJS-006 §12 | Stable Output Rule | TJS-006 | §12 Stable Output Rule | KEEP |
| TJS-006 §13 | Empty Block Rule | TJS-006 | §13 Empty Block Rule | KEEP |
| TJS-006 §14 | Validation Rules | TJS-006 | §14 Validation Rules | KEEP |
| TJS-006 §15 | Error Handling | TJS-006 | §15 Error Handling | KEEP |
| TJS-006 §16 | Future Compatibility | TJS-006 | §16 Future Compatibility | KEEP |
| TJS-006 §17 | References | TJS-006 | §17 References | KEEP (FIX: "TJS-003 — Editorial Policy" → "TJS-004 — Editorial Policy") |

---

## TJS-007 — Publication Lifecycle

**Destination:** TJS-005 (MERGED from TJS-002 + TJS-007 + TJS-008)
**Action:** MERGE + REMOVE file

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-007 §1 | Purpose | TJS-005 | §1 Purpose (unified) | MERGE |
| TJS-007 §2 | Scope | TJS-005 | §2 Scope (unified) | MERGE |
| TJS-007 §3 | Publication Lifecycle (flow) | TJS-005 | §3 Lifecycle State Model (unified) | MERGE |
| TJS-007 §4 | Publication Creation | TJS-005 | §13 Publication Creation | ABSORB |
| TJS-007 §5 | Publication Updates | TJS-005 | §8 Update Rules (unified) | MERGE |
| TJS-007 §6 | Canonical Equality | TJS-005 | §14 Canonical Equality | ABSORB |
| TJS-007 §7 | Publication Ordering | TJS-005 | §15 Publication Ordering | ABSORB |
| TJS-007 §8 | Temporary Publications | TJS-005 | §7 Temporary Publications (unified) | MERGE |
| TJS-007 §9 | Permanent Publications | TJS-005 | §16 Permanent Publications | ABSORB |
| TJS-007 §10 | Publication Ownership | TJS-005 | §17 Publication Ownership | ABSORB |
| TJS-007 §11 | Non-destructive Channel Principle | TJS-005 | §18 Non-destructive Channel Principle | ABSORB |
| TJS-007 §12 | Publication Lifecycle Diagram | TJS-005 | §24 Lifecycle Diagrams (consolidated) | ABSORB |
| TJS-007 §13 | Error Handling | TJS-005 | §19 Error Handling | ABSORB |
| TJS-007 §14 | References | TJS-005 | §25 References (corrected) | REMOVE (corrected) |

**File operation:** REMOVE `TJS-007-Publication-Lifecycle.md`

---

## TJS-008 — Publication Lifecycle

**Destination:** TJS-005 (MERGED from TJS-002 + TJS-007 + TJS-008)
**Action:** MERGE + REMOVE file

| Source Section | Source Content | Destination Document | Destination Section | Action |
|---------------|---------------|---------------------|-------------------|--------|
| TJS-008 §1 | Purpose | TJS-005 | §1 Purpose (unified) | MERGE |
| TJS-008 §2 | Scope | TJS-005 | §2 Scope (unified) | MERGE |
| TJS-008 §3 | Publication Cycle | TJS-005 | §20 Daily Publication Cycle | ABSORB |
| TJS-008 §4 | Daily Publication Package | TJS-005 | §21 Daily Publication Package | ABSORB |
| TJS-008 §5 | Tomorrow Publication Package | TJS-005 | §22 Tomorrow Publication Package | ABSORB |
| TJS-008 §6 | Publication Windows | TJS-005 | §23 Publication Windows | ABSORB |
| TJS-008 §7 | Event-driven Publication Principle | TJS-005 | §24 Event-driven Principle | ABSORB |
| TJS-008 §8 | Stable Journal Principle | TJS-005 | §25 Stable Journal Principle | ABSORB |
| TJS-008 §9 | Deterministic Daily Journal Principle | TJS-005 | §26 Deterministic Principle | ABSORB |
| TJS-008 §10 | Non-destructive Update Principle | TJS-005 | §27 Non-destructive Update Principle | ABSORB |
| TJS-008 §11 | Update Policy | TJS-005 | §8 Update Rules (unified) | MERGE |
| TJS-008 §12 | Tomorrow Publication Lifecycle | TJS-005 | §28 Tomorrow Lifecycle | ABSORB |
| TJS-008 §13 | Manual Publications | TJS-005 | §29 Manual Publications | ABSORB |
| TJS-008 §14 | Image Publications | TJS-005 | §30 Image Publications | ABSORB |
| TJS-008 §15 | Publication Session | TJS-005 | §31 Publication Session | ABSORB |
| TJS-008 §16 | Daily Lifecycle Diagram | TJS-005 | §24 Lifecycle Diagrams (consolidated) | ABSORB |
| TJS-008 §17 | Telegram Journal Architecture | TJS-005 | §24 Lifecycle Diagrams (consolidated) | ABSORB |
| TJS-008 §18 | References | TJS-005 | §25 References (corrected) | REMOVE (corrected) |

**File operation:** REMOVE `TJS-008-Publication-Lifecycle.md`

---

## New Documents

### TJS-006 — Channel Management (NEW)

| Section | Content | Action |
|---------|---------|--------|
| §1 | Purpose | CREATE |
| §2 | Scope | CREATE |
| §3 | Telegram Bot API Integration | CREATE |
| §4 | Rate Limiting | CREATE |
| §5 | Message Editing Rules | CREATE |
| §6 | Channel Administration | CREATE |
| §7 | Error Recovery | CREATE |
| §8 | References | CREATE |

### TJS-007 — Graphic Rendering (NEW)

| Section | Content | Action |
|---------|---------|--------|
| §1 | Purpose | CREATE |
| §2 | Scope | CREATE |
| §3 | Graphic Generation Rules | CREATE |
| §4 | Image Format Requirements | CREATE |
| §5 | Telegram Image Constraints | CREATE |
| §6 | Graphic-to-Text Pairing | CREATE |
| §7 | Graphic Validation | CREATE |
| §8 | References | CREATE |

---

## File Operations Summary

| Operation | Files |
|-----------|-------|
| KEEP (update) | TJS-001, TJS-004, TJS-005, TJS-006 |
| MOVE (section) | TJS-003 §9 → TJS-004 |
| MERGE (3→1) | TJS-002 + TJS-007 + TJS-008 → TJS-005 |
| ABSORB (12 sections) | TJS-003 Post Structure → TJS-005 Message Templates |
| REMOVE | TJS-002-Publication-Lifecycle.md, TJS-003-Post-Structure.md, TJS-007-Publication-Lifecycle.md, TJS-008-Publication-Lifecycle.md |
| CREATE | TJS-006-Channel-Management.md, TJS-007-Graphic-Rendering.md |

---

**End of Migration Matrix**

**Planner:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
