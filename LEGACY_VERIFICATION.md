# LEGACY_VERIFICATION

**Document ID:** TJS-N1.2-C4

**Title:** Legacy Verification

**Document Class:** Verification

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Verify Legacy document status.

---

# 1. Legacy Directory Verification

| Check | Result |
|-------|--------|
| telegram/legacy/ exists? | YES |
| Files located there | 8 TJS files |

---

# 2. Legacy Document Inventory

| # | Filename | Status | Archival | Should INDEX reference? |
|---|----------|--------|----------|------------------------|
| 1 | TJS-001-Journal-Concept.md | Legacy | Archived | NO |
| 2 | TJS-002-Publication-Lifecycle.md | Legacy | Archived | NO |
| 3 | TJS-003-Post-Structure.md | Legacy | Archived | NO |
| 4 | TJS-004-Editorial-Policy.md | Legacy | Archived | NO |
| 5 | TJS-005-Message-Templates.md | Legacy | Archived | NO |
| 6 | TJS-006-Rendering-Rules.md | Legacy | Archived | NO |
| 7 | TJS-007-Publication-Lifecycle.md | Legacy | Archived | NO |
| 8 | TJS-008-Publication-Lifecycle.md | Legacy | Archived | NO |

---

# 3. Legacy Verification

| Check | Result |
|-------|--------|
| All 8 legacy files physically exist | YES |
| All 8 are in telegram/legacy/ | YES |
| All 8 are superseded by canonical specs | YES |
| All 8 should NOT be in DOCUMENT_INDEX | YES |
| Current INDEX lists them as "current" | YES — INCORRECT |

---

# 4. Legacy Verdict

**DOCUMENT_INDEX currently lists TJS-001 through TJS-008 as "Current specifications."** This is INCORRECT. These are Legacy documents superseded by TJS-000 through TJS-022. They MUST be removed from DOCUMENT_INDEX and replaced with the canonical specifications.

---

**End of Legacy Verification**

**Verifier:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
