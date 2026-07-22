# CASE001_PUBLICATION_MUTATION_MODEL

**Document ID:** CASE001B-MUTATION

**Title:** Publication — Mutation Investigation

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document lists every attribute of Publication and classifies each as Immutable, Mutable, Derived, Calculated, External, Historical, or Temporary.

---

# Publication Attributes

## Attribute 1: Territory

**Classification:** IMMUTABLE

**Evidence:**

- TJS-021 §6.1: "Every Publication SHALL represent exactly one Territory"
- Legacy TJS-007 §4: "Every Publication SHALL represent exactly one Territory"
- No specification allows Territory to change after creation

**Justification:** Territory is fixed at creation and never changes.

---

## Attribute 2: Date

**Classification:** IMMUTABLE

**Evidence:**

- TJS-005: Templates define "Today" and "Tomorrow" variants
- TJS-021 §4: Lifecycle states reference "reporting period"
- No specification allows Date to change after creation

**Justification:** Date is fixed at creation and never changes.

---

## Attribute 3: Template

**Classification:** IMMUTABLE

**Evidence:**

- TJS-005: Canonical Templates (A, B, C, D)
- Legacy TJS-007 §4: "Every Publication SHALL use one Canonical Template"
- No specification allows Template to change after creation

**Justification:** Template is fixed at creation and never changes.

---

## Attribute 4: Content

**Classification:** MUTABLE

**Evidence:**

- TJS-021 §5.2: "A Published Publication becomes Updated when the normalized dataset changes"
- TJS-021 §6.2: "Publications MAY be updated only when the normalized dataset changes or rendering rules change"
- Legacy TJS-007 §5: "Updates SHALL be performed by editing the existing Telegram Message"

**Justification:** Content changes when underlying data changes.

---

## Attribute 5: Lifecycle State

**Classification:** MUTABLE

**Evidence:**

- TJS-021 §4: "Every Publication SHALL pass through one or more of the following states"
- TJS-021 §5: Lifecycle transitions define state changes

**Justification:** State changes through lifecycle transitions.

---

## Attribute 6: Telegram Message ID

**Classification:** EXTERNAL

**Evidence:**

- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message"
- Legacy TJS-007 §10: "Ownership SHALL be determined by the stored Telegram Message ID"

**Justification:** Telegram Message ID is assigned by external platform, not intrinsic to Publication.

---

## Attribute 7: Generation Timestamp

**Classification:** IMMUTABLE

**Evidence:**

- TJS-022 §6.4.1: "Generation Timestamp — The timestamp when the graphic was generated"
- No specification allows generation timestamp to change

**Justification:** Generation timestamp is set at creation and never changes.

---

## Attribute 8: Publication Timestamp

**Classification:** IMMUTABLE

**Evidence:**

- TJS-022 §6.4.2: "Publication Timestamp — The timestamp when the graphic was published to Telegram"
- No specification allows publication timestamp to change

**Justification:** Publication timestamp is set at delivery and never changes.

---

## Attribute 9: Source Dataset

**Classification:** IMMUTABLE

**Evidence:**

- TJS-022 §6.4.4: "Source Dataset — The normalized dataset used to generate this graphic"
- DATA_MODEL.md: "Each Publication SHALL be traceable to normalized operational data"

**Justification:** Source dataset is fixed at creation and never changes.

---

## Attribute 10: Version

**Classification:** DERIVED

**Evidence:**

- TJS-022 §6.4.5: "Version — The version identifier of this graphic"
- Version is derived from update count

**Justification:** Version is calculated from the number of updates.

---

## Attribute 11: Publication Identity

**Classification:** IMMUTABLE

**Evidence:**

- TJS-022 §6.4.6: "Publication Identity — The unique identifier for this graphic publication"
- Identity is fixed at creation

**Justification:** Publication Identity is set at creation and never changes.

---

## Attribute 12: Ownership

**Classification:** MUTABLE

**Evidence:**

- TJS-010 §4.1: Publication Engine owns Publications
- Legacy TJS-007 §10: "Manual Publications SHALL never become owned Publications"
- Ownership can change (manual vs automatic)

**Justification:** Ownership changes depending on creation method.

---

## Attribute 13: Ordering Position

**Classification:** DERIVED

**Evidence:**

- TJS-006 §5: "Publications SHALL be generated in the following order: Administrative Centre first, then Starosta Districts"
- Ordering is derived from Territory and Template

**Justification:** Ordering is calculated from Territory and Template.

---

## Attribute 14: Temporal Relevance

**Classification:** DERIVED

**Evidence:**

- TJS-022 §5.2: "T-001 is generated during the previous day. After the beginning of the corresponding calendar day, this publication automatically becomes the current valid schedule"
- Temporal relevance is derived from Date and current time

**Justification:** Temporal relevance is calculated from Date and current time.

---

## Attribute 15: Archive Status

**Classification:** MUTABLE

**Evidence:**

- TJS-021 §4.4: "The state in which a Publication is preserved as part of the historical record"
- TJS-021 §5.4: "A Published Publication becomes Archived when the reporting period ends"

**Justification:** Archive status changes when reporting period ends.

---

# Attribute Classification Summary

| Attribute | Classification | Evidence |
|-----------|---------------|----------|
| Territory | IMMUTABLE | Fixed at creation |
| Date | IMMUTABLE | Fixed at creation |
| Template | IMMUTABLE | Fixed at creation |
| Content | MUTABLE | Changes with data |
| Lifecycle State | MUTABLE | Changes through transitions |
| Telegram Message ID | EXTERNAL | Assigned by platform |
| Generation Timestamp | IMMUTABLE | Set at creation |
| Publication Timestamp | IMMUTABLE | Set at delivery |
| Source Dataset | IMMUTABLE | Fixed at creation |
| Version | DERIVED | Calculated from updates |
| Publication Identity | IMMUTABLE | Fixed at creation |
| Ownership | MUTABLE | Changes by creation method |
| Ordering Position | DERIVED | Calculated from Territory |
| Temporal Relevance | DERIVED | Calculated from Date |
| Archive Status | MUTABLE | Changes at archival |

---

# Attribute Classification Counts

| Classification | Count | Attributes |
|----------------|-------|------------|
| IMMUTABLE | 7 | Territory, Date, Template, Generation Timestamp, Publication Timestamp, Source Dataset, Publication Identity |
| MUTABLE | 4 | Content, Lifecycle State, Ownership, Archive Status |
| DERIVED | 3 | Version, Ordering Position, Temporal Relevance |
| EXTERNAL | 1 | Telegram Message ID |

---

# Key Insight

**7 of 15 attributes are IMMUTABLE.**

**This means Publication is largely immutable.**

**The 4 MUTABLE attributes (Content, Lifecycle State, Ownership, Archive Status) change in well-defined ways according to lifecycle rules.**

**The 3 DERIVED attributes are calculated from other attributes.**

**The 1 EXTERNAL attribute (Telegram Message ID) is assigned by the platform.**

---

# End of Mutation Model
