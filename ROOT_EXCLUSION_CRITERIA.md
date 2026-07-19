# ROOT_EXCLUSION_CRITERIA

**Document ID:** TJS-R4.3-A3

**Title:** Root Exclusion Criteria

**Document Class:** Exclusion Criteria

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

Define what SHALL NOT appear in Repository Root.

---

# 1. Root Exclusion Criteria

The following categories of documents SHALL NOT exist in Repository Root:

| # | Category | Rationale |
|---|----------|-----------|
| EC-001 | Subsystem documentation | Belongs in subsystem directory |
| EC-002 | Subsystem specifications | Belongs in subsystem directory |
| EC-003 | Drafts | Not stable, not normative |
| EC-004 | Completed audits | Historical, belongs in archive/ |
| EC-005 | Completed certificates | Historical, belongs in archive/ |
| EC-006 | Completed reports | Historical, belongs in archive/ |
| EC-007 | Migration artifacts | Historical, belongs in archive/ |
| EC-008 | Working files | Active work, belongs in working/ |
| EC-009 | Temporary files | Temporary, belongs in Temp/ |
| EC-010 | Release-specific materials | Historical, belongs in archive/ |
| EC-011 | Audit results | Historical, belongs in archive/ |
| EC-012 | Blueprint documents | Historical, belongs in archive/ |
| EC-013 | Validation results | Historical, belongs in archive/ |
| EC-014 | Scorecards | Historical, belongs in archive/ |
| EC-015 | Root architecture analysis | Historical, belongs in archive/ |

---

# 2. Current Root Violations

The following documents currently in Root VIOLATE the exclusion criteria:

| # | Document | Violation | Correct Location |
|---|----------|-----------|-----------------|
| 1 | ~198 audit/certification/report files | EC-004, EC-005, EC-006, EC-010, EC-011, EC-012, EC-013, EC-014, EC-015 | archive/ |

**Note:** These violations will be resolved during Stage R-5 (Dry Run) when ~198 files are relocated to their architectural destinations per the approved Repository Blueprint.

---

# 3. Exclusion Verdict

**13 Foundation documents are COMPLIANT.** ~198 documents violate exclusion criteria — all scheduled for relocation according to the approved Repository Blueprint during R-5 migration.

---

**End of Root Exclusion Criteria**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
