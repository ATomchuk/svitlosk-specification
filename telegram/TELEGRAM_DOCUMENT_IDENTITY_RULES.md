# Telegram Document Identity Rules

**Date:** 2026-07-13
**Scope:** Normative identity rules for Telegram documentation
**Status:** RULES DEFINED

---

# Purpose

This document defines the normative rules governing document identity in the Telegram documentation system.

---

# Identity Rules

## Rule 1: Document ID is Permanent

**Statement:** The Document ID SHALL NOT change without an approved Architecture Decision Record (ADR).

**Rationale:** The Document ID is the stable reference used by all documents, dependency graphs, and cross-references. Changing it would break all references.

**Exception:** An ADR MAY reassign a Document ID when:
- The original document is removed (not just renamed)
- The ID is needed for a new document with a clearly different purpose

---

## Rule 2: File Name Follows Document ID

**Statement:** The file name SHALL be derived from the Document ID and Document Title using the pattern: `{Document ID}-{Document Title}.md`

**Rationale:** The file name provides a human-readable identifier that can be derived from the Document ID.

**Exception:** Foundational documents may use alternative naming (e.g., TELEGRAM_SEMANTIC_MODEL.md for TJS-000).

---

## Rule 3: Document Title is Human-Readable

**Statement:** The Document Title SHALL be descriptive and human-readable. It SHALL NOT be changed without justification.

**Rationale:** The Document Title provides human-readable context for the document.

**Change Process:** Title changes require:
1. Justification
2. Approval from the Architect
3. Update to all cross-references

---

## Rule 4: Document Class is Metadata

**Statement:** The Document Class SHALL be declared in the document metadata. It SHALL NOT change without approval.

**Rationale:** The Document Class determines how the document is governed and validated.

**Change Process:** Class changes require:
1. Justification
2. Approval from the Architect
3. Update to document metadata

---

## Rule 5: Document Location is Flexible

**Statement:** The Document Location (directory) MAY change during restructuring. The Document ID SHALL remain stable.

**Rationale:** Documents may be reorganized into subdirectories for better structure. The Document ID provides stability.

**Change Process:** Location changes require:
1. Backup of all affected files
2. File move operation
3. Update to dependency references

---

## Rule 6: Cross-References Use Document ID

**Statement:** When one document references another, it SHALL use the Document ID as the primary reference.

**Rationale:** The Document ID is the permanent, stable identifier. File names and titles MAY change.

**Format:** `TJS-XXX — Document Title`

**Example:** `TJS-001 — Journal Concept`

---

## Rule 7: Dependency Graph Uses Document ID

**Statement:** The dependency graph SHALL use Document IDs for all nodes and edges.

**Rationale:** The dependency graph must remain stable across restructuring.

**Format:** `TJS-001 → TJS-002 → TJS-003`

---

## Rule 8: Version Tracking Uses Document ID

**Statement:** Version history SHALL be tracked by Document ID, not file name.

**Rationale:** The Document ID is the permanent identifier. File names MAY change.

**Format:** `TJS-XXX v1.0.0`

---

# Identity Rule Summary

| Rule | Statement | Exception |
|------|-----------|-----------|
| R-001 | Document ID is permanent | ADR required for change |
| R-002 | File name follows Document ID | Foundational docs may differ |
| R-003 | Document Title is human-readable | Change with justification |
| R-004 | Document Class is metadata | Change with approval |
| R-005 | Document Location is flexible | Restructuring allowed |
| R-006 | Cross-references use Document ID | — |
| R-007 | Dependency graph uses Document ID | — |
| R-008 | Version tracking uses Document ID | — |

---

**End of Identity Rules**

**Definer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
