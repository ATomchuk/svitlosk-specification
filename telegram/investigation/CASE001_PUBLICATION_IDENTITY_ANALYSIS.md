# CASE001_PUBLICATION_IDENTITY_ANALYSIS

**Document ID:** CASE001B-IDENTITY

**Title:** Publication — Identity Investigation

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document determines what exactly makes Publication remain the same object through time.

---

# Identity Candidates

## Candidate 1: Publication ID (Internal)

**What it is:** An internal identifier assigned by the system.

**Evidence:**

- DATA_MODEL.md: "Every logical entity SHALL be uniquely identifiable"
- No explicit Publication ID is defined in any specification
- Legacy TJS-007 §10 mentions Telegram Message ID as ownership determinant

**Classification:** **NOT DEFINED** — no internal Publication ID exists in the repository.

---

## Candidate 2: Issue Membership

**What it is:** Publication belongs to an Issue for one calendar day.

**Evidence:**

- TJS-000 §4: "Publication represents one independent publication belonging to an Issue"
- TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated"

**Classification:** **RELATIONSHIP** — Issue membership is a relationship, not identity. Multiple Publications can belong to the same Issue.

---

## Candidate 3: Telegram Message ID

**What it is:** The platform identifier assigned by Telegram when Publication is delivered.

**Evidence:**

- Legacy TJS-007 §10: "Ownership SHALL be determined by the stored Telegram Message ID"
- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message in Telegram"
- TJS-010 §5.1: "Publication Engine → Telegram Channel: Publication (owned)"

**Classification:** **EXTERNAL REFERENCE** — Telegram Message ID is a platform-specific reference, not intrinsic identity. Publication exists before Telegram Message ID is assigned (Generated state).

---

## Candidate 4: Publication Package

**What it is:** The collection of Publications for one Reporting Period.

**Evidence:**

- GLOSSARY.md §3: "The complete collection of Publications generated during one Reporting Period"
- TJS-010 §4.1: Publication Engine produces Publication Package

**Classification:** **RELATIONSHIP** — Publication Package is a collection, not identity. Multiple Publications can belong to the same Package.

---

## Candidate 5: Lifecycle

**What it is:** The state sequence (Generated → Published → Updated → Archived → Removed).

**Evidence:**

- TJS-021 §4: "Every Publication SHALL pass through one or more of the following states"
- TJS-021 §5: Lifecycle transitions

**Classification:** **STATE** — Lifecycle is the state sequence, not identity. Identity persists across state changes.

---

## Candidate 6: Content

**What it is:** The rendered Telegram HTML containing territorial information.

**Evidence:**

- TJS-005: Publication Grammar defines content structure
- TJS-006: Rendering Rules define content transformation
- Legacy TJS-007 §6: Canonical Equality compares content

**Classification:** **STATE** — Content can change (when data changes). Identity persists across content changes.

---

## Candidate 7: Metadata

**What it is:** Timestamps, version numbers, source references.

**Evidence:**

- TJS-022 §6.4: Graphic Publication metadata (generation timestamp, publication timestamp, territory, source dataset, version, publication identity)
- DATA_MODEL.md: "timestamped where applicable"

**Classification:** **METADATA** — Metadata describes Publication but is not identity.

---

## Candidate 8: Temporal Continuity

**What it is:** Publication persists through time, maintaining continuity.

**Evidence:**

- TJS-021 §4.4: "Archived Publications remain available in the Telegram Journal permanently"
- TJS-021 §9: "Every Publication SHALL follow the defined lifecycle states"

**Classification:** **IDENTITY CHARACTERISTIC** — Temporal continuity is a characteristic of identity, not identity itself.

---

## Candidate 9: Territory + Date + Template

**What it is:** The combination of Territory, Date, and Template that uniquely identifies a Publication.

**Evidence:**

- TJS-005: Canonical Templates (A, B, C, D)
- TJS-006: Territory Ordering (Administrative Centre first, then Starosta Districts)
- Legacy TJS-007 §4: "Every Publication SHALL represent exactly one Territory"
- TJS-010 §6.3: "Deterministic Publishing" — same input produces same output

**Classification:** **IDENTITY** — Territory + Date + Template uniquely identifies a Publication. Two Publications with the same Territory, Date, and Template are the same Publication.

---

# Identity Classification Summary

| Candidate | Classification | Evidence |
|-----------|---------------|----------|
| Publication ID | NOT DEFINED | No internal ID exists |
| Issue Membership | RELATIONSHIP | Multiple Publications per Issue |
| Telegram Message ID | EXTERNAL REFERENCE | Assigned after creation |
| Publication Package | RELATIONSHIP | Multiple Publications per Package |
| Lifecycle | STATE | Identity persists across states |
| Content | STATE | Content can change |
| Metadata | METADATA | Describes but is not identity |
| Temporal Continuity | IDENTITY CHARACTERISTIC | Characteristic, not identity itself |
| Territory + Date + Template | **IDENTITY** | Uniquely identifies Publication |

---

# Identity Model

## Primary Identity: Territory + Date + Template

**Definition:** A Publication is uniquely identified by its Territory, Date, and Template.

**Evidence:**

- TJS-005: Canonical Templates define the format
- TJS-006: Territory Ordering defines the structure
- Legacy TJS-007 §4: "Every Publication SHALL represent exactly one Territory"
- TJS-010 §6.3: "Deterministic Publishing"

**Example:**

- Territory: Starokostiantyniv
- Date: 2026-07-21
- Template: A (City Today)
- **Identity:** Publication for Starokostiantyniv on 2026-07-21 using Template A

---

## External Reference: Telegram Message ID

**Definition:** Telegram Message ID is a platform-specific reference assigned after delivery.

**Evidence:**

- Legacy TJS-007 §10: "Ownership SHALL be determined by the stored Telegram Message ID"
- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message"

**Note:** Telegram Message ID is NOT identity. It is a reference. Publication exists before Telegram Message ID is assigned (Generated state).

---

# Identity Continuity Through Lifecycle

| State | Identity | External Reference |
|-------|----------|-------------------|
| Generated | Territory + Date + Template | None |
| Published | Territory + Date + Template | Telegram Message ID |
| Updated | Territory + Date + Template | Telegram Message ID |
| Archived | Territory + Date + Template | Telegram Message ID |
| Removed | Territory + Date + Template | Released |

**Identity persists across all states. External reference is added and released.**

---

# End of Identity Analysis
