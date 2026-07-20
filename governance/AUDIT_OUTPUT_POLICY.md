# AUDIT_OUTPUT_POLICY

**Document ID:** PR-AUD-001

**Title:** Audit Output Placement Principle

**Document Class:** Repository Engineering Principle

**Status:** Stable

**Author:** SvitloSk Project

---

# 1. Purpose

Define where audit artifacts SHALL be created.

This principle was adopted after repeated instances of audit deliverables being left in Repository Root during H-2 and H-2A.

---

# 2. Rules

| Rule | Statement |
|------|-----------|
| PR-AUD-001-R1 | Audit reports SHALL NEVER be created in Repository Root |
| PR-AUD-001-R2 | Every future audit artifact SHALL be written directly into its permanent directory |
| PR-AUD-001-R3 | Repository Root SHALL NEVER be used as temporary storage for audit deliverables |
| PR-AUD-001-R4 | Future audit stages SHALL comply with PR-ROOT-001 immediately upon creation |

---

# 3. Approved Output Locations

| Audit Type | Output Location |
|-----------|----------------|
| Repository architecture reviews | archive/review/ |
| Navigation audits | archive/navigation/ |
| Translation preparation | archive/translation-preparation/ |
| Engineering audits | archive/engineering/ or audit/ |
| Governance reviews | archive/review/ |
| Certification documents | archive/review/ |
| Migration reports | archive/migration/ or archive/repository/ |

---

# 4. Enforcement

Every future audit stage SHALL:

1. Create output files directly in the approved permanent directory.
2. NEVER create files in Root as a temporary step.
3. Verify PR-ROOT-001 compliance before completing.

---

# 5. Integration

This principle is part of Repository Engineering governance. It supplements:

- PR-ROOT-001 (Root Architecture Principle)
- PROC-001 (Specification Engineering Process)

---

**End of Audit Output Policy**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
