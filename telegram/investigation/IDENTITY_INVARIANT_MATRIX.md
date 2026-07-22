# IDENTITY_INVARIANT_MATRIX

**Document ID:** CASE001C-INVARIANTS

**Title:** Identity — Invariant Matrix

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity Investigation

---

# Purpose

This document produces a complete invariant matrix showing what NEVER changes and what MAY change.

---

# Complete Invariant Matrix

## What NEVER Changes (Immutable)

| # | Invariant | Evidence | Reason |
|---|-----------|----------|--------|
| I-001 | Territory of a Publication | TJS-021 §6.1: "Every Publication SHALL represent exactly one Territory" | Fixed at creation |
| I-002 | Date of a Publication | TJS-005: Templates define "Today" and "Tomorrow" variants | Fixed at creation |
| I-003 | Template of a Publication | Legacy TJS-007 §4: "Every Publication SHALL use one Canonical Template" | Fixed at creation |
| I-004 | Document ID of a specification | DOCUMENT_INDEX.md: "Document identifiers SHALL be unique" | Assigned at registration |
| I-005 | ADR ID of an architecture decision | ADR-001: Document ID is stable | Assigned at creation |
| I-006 | Territory name | TERRITORIAL_MODEL.md: "All project components SHALL derive territorial information exclusively from this model" | Canonical definition |
| I-007 | Address (official) | GLOSSARY.md §4: "Addresses SHALL be treated exactly as officially published" | Official designation |
| I-008 | Queue identifier | GLOSSARY.md §5: "Queue identifiers SHALL preserve their official representation" | Official designation |
| I-009 | Subqueue identifier | GLOSSARY.md §5: "Subqueue identifiers SHALL preserve their official representation" | Official designation |
| I-010 | Generation Timestamp | TJS-022 §6.4.1: "Generation Timestamp — The timestamp when the graphic was generated" | Set at creation |
| I-011 | Publication Timestamp | TJS-022 §6.4.2: "Publication Timestamp — The timestamp when the graphic was published to Telegram" | Set at delivery |
| I-012 | Source Dataset | TJS-022 §6.4.4: "Source Dataset — The normalized dataset used to generate this graphic" | Fixed at creation |
| I-013 | Publication Identity | TJS-022 §6.4.6: "Publication Identity — The unique identifier for this graphic publication" | Fixed at creation |

## What MAY Change (Mutable)

| # | Mutable | Evidence | Reason |
|---|---------|----------|--------|
| M-001 | Publication content | TJS-021 §5.2: "A Published Publication becomes Updated when the normalized dataset changes" | Content follows data |
| M-002 | Publication lifecycle state | TJS-021 §5: Lifecycle transitions define state changes | State changes through transitions |
| M-003 | Publication ownership | TJS-010 §4.1 vs Legacy TJS-007 §10: Ownership can change | Ownership depends on creation method |
| M-004 | Publication archive status | TJS-021 §5.4: "A Published Publication becomes Archived when the reporting period ends" | Status changes at archival |
| M-005 | Telegram Message ID | Assigned at delivery, released at removal | External reference |
| M-006 | Version | TJS-022 §6.4.5: "Version — The version identifier of this graphic" | Derived from updates |
| M-007 | Ordering Position | TJS-006 §5: "Publications SHALL be generated in the following order" | Derived from Territory |
| M-008 | Temporal Relevance | TJS-022 §5.2: "After the beginning of the corresponding calendar day, this publication automatically becomes the current valid schedule" | Derived from Date and time |

---

# Invariant Classification Summary

| Classification | Count | Examples |
|----------------|-------|----------|
| IMMUTABLE | 13 | Territory, Date, Template, Document IDs, Timestamps, Identifiers |
| MUTABLE | 8 | Content, State, Ownership, Archive Status, Telegram Message ID, Version, Ordering, Temporal Relevance |

---

# Key Insight

**13 of 21 attributes are IMMUTABLE.**

**This means identity is largely immutable.**

**The 8 MUTABLE attributes change in well-defined ways according to lifecycle rules.**

---

# End of Invariant Matrix
