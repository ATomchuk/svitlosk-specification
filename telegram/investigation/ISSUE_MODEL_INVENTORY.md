# ISSUE_MODEL_INVENTORY

**Document ID:** CASE002A-MODELS

**Title:** Issue — Model Inventory

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Investigation

---

# Purpose

This document provides a complete inventory of all Issue models found in the repository.

---

# Issue Models Found

## Model A: Issue as Container

**Definition:** Issue is a temporal container that holds Publications for one calendar day.

**Evidence:**

- TJS-021 §8.2: "An Issue is maintained through: Publication creation, updates, replacement, removal"
- CASE001: "Issue is the TEMPORAL CONTAINER for Publications"

**Characteristics:**

- Contains Publications
- Has no content of its own
- Exists only to group Publications
- Temporal scope: one calendar day

---

## Model B: Issue as Editorial Unit

**Definition:** Issue is one editorial edition of the Journal for a single calendar day.

**Evidence:**

- TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"
- TJS-000A §8: "One editorial edition of the Journal for a single calendar day"

**Characteristics:**

- Has editorial purpose
- Represents one day's editorial output
- Part of Journal hierarchy
- Has editorial integrity requirements

---

## Model C: Issue as Business Object

**Definition:** Issue is a business concept representing daily editorial output.

**Evidence:**

- TJS-000 §5: "Issue — Owns: Daily edition, date scope"
- TJS-020 §4.5: "The integrity of each daily edition SHALL be preserved"

**Characteristics:**

- Has business meaning
- Has ownership (Editorial System)
- Has lifecycle (Opens → Maintained → Closes)
- Has integrity requirements

---

## Model D: Issue as Time Slice

**Definition:** Issue is a temporal slice of the Journal's continuous publication.

**Evidence:**

- TJS-000 §4: "Journal represents the continuous informational publication"
- TJS-000 §4: "Issue represents one editorial edition... for a single calendar day"

**Characteristics:**

- Temporal boundary: one calendar day
- Part of continuous Journal
- Slice of ongoing publication
- Time-bounded

---

## Model E: Issue as Publication Collection

**Definition:** Issue is a collection of Publications for one reporting period.

**Evidence:**

- TJS-010 §6.5: "The daily publication package consists of: one post for Starokostiantyniv; one post for every starosta district"
- TJS-021 §8.2: "An Issue is maintained through: Publication creation, updates, replacement, removal"

**Characteristics:**

- Contains multiple Publications
- Grouped by calendar day
- Has composition rules
- Has completeness requirements

---

## Model F: Issue as Historical Record

**Definition:** Issue is a preserved daily edition for historical reference.

**Evidence:**

- TJS-021 §8.3: "The Issue remains available as part of the historical record after closing"
- TJS-020 §4.5: "The integrity of each daily edition SHALL be preserved for public accountability"

**Characteristics:**

- Permanent after closing
- Preserved for accountability
- Historical reference
- Immutable after archival

---

## Model G: Issue as Process

**Definition:** Issue is a daily editorial process that opens, fills, and closes.

**Evidence:**

- TJS-021 §8.1: "An Issue opens when..."
- TJS-021 §8.2: "An Issue is maintained through..."
- TJS-021 §8.3: "An Issue closes when..."

**Characteristics:**

- Has opening trigger
- Has maintenance activities
- Has closing conditions
- Temporal process

---

# Model Comparison Matrix

| Model | Definition | Evidence Strength | Fit |
|-------|------------|-------------------|-----|
| A | Container | STRONG | GOOD |
| B | Editorial Unit | STRONG | GOOD |
| C | Business Object | MEDIUM | GOOD |
| D | Time Slice | MEDIUM | GOOD |
| E | Publication Collection | MEDIUM | GOOD |
| F | Historical Record | STRONG | GOOD |
| G | Process | STRONG | GOOD |

---

# Key Insight

**No single model fully captures Issue.**

**Issue exhibits properties of ALL models simultaneously.**

**This suggests Issue is a multi-faceted concept that cannot be reduced to one model.**

---

# End of Model Inventory
