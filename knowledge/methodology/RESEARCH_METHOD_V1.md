# RESEARCH_METHOD_V1

**Document ID:** METH-V1-001

**Title:** Architectural Research Methodology Version 1.0

**Document Class:** Methodology

**Status:** Frozen

**Author:** SvitloSk Project

---

# 1. Purpose

The purpose of this methodology is preservation of architectural knowledge through repeatable scientific investigation.

This methodology governs ONLY research. It does NOT govern specifications, implementation, ADRs, or software architecture.

---

# 2. Scope

This methodology governs:

- How architectural investigations are conducted
- How knowledge is extracted from investigations
- How knowledge is preserved in the repository
- How knowledge is verified and audited

This methodology does NOT govern:

- Specifications
- Implementation
- ADRs
- Software architecture
- Knowledge governance
- Knowledge promotion
- Repository governance
- Specification management

---

# 3. Research Pipeline

The research pipeline consists of six stages:

**Stage 1: CASE**

A CASE is a bounded investigation of a specific architectural subject. Each CASE has an identifier (e.g., CASE-001, CASE-002). A CASE begins with a research question and ends with findings.

**Stage 2: Research**

Research is the systematic inquiry that produces evidence and findings. Research follows the methodology principles and produces Knowledge Units.

**Stage 3: Knowledge**

Knowledge is the extracted, validated, and preserved understanding. Knowledge exists in the Knowledge Base as atomic Knowledge Units.

**Stage 4: Audit**

Audit is independent verification of Knowledge. Audit confirms that findings are supported by evidence and that no hidden knowledge remains.

**Stage 5: Complete**

Complete means that every architectural statement from the CASE has been extracted and preserved. Nothing remains hidden in investigation documents.

**Stage 6: LOCK**

LOCK means permanent closure. LOCKed knowledge cannot be changed without formal governance through a new CASE.

---

# 4. Research Principles

The following principles are operational rules for all research:

**Principle 1: Evidence Before Conclusion**

Every architectural conclusion must be supported by evidence from repository documents.

**Principle 2: Multiple Models Before Selection**

Multiple competing models must be constructed before any conclusion is reached.

**Principle 3: Cross-Examination Before Acceptance**

Every model must be attacked and defended before acceptance.

**Principle 4: Contradiction Search Before Acceptance**

Every contradiction must be identified before acceptance.

**Principle 5: Independent Verification Before Canonical**

Knowledge must be verified by independent investigation before becoming Canonical.

**Principle 6: Audit Before LOCK**

Knowledge must be independently audited before receiving LOCK status.

**Principle 7: LOCK Is Immutable**

LOCKed knowledge cannot be changed without a new CASE.

**Principle 8: Evidence Must Be Traceable**

Every Knowledge Unit must trace to its origin investigation.

**Principle 9: No Recommendations During Research**

Research produces evidence, not recommendations. The Architect decides.

**Principle 10: Scope Defines Completeness**

Research is "complete" only within a defined scope.

---

# 5. Research Objects

The following objects are used in research:

**CASE:** A bounded investigation of a specific architectural subject. Identified by CASE-XXX.

**Investigation:** A systematic inquiry that produces evidence and findings.

**Evidence:** Proof supporting or contradicting a claim.

**Finding:** A validated conclusion from investigation.

**Knowledge Unit:** An atomic piece of architectural knowledge.

**Audit:** Independent examination of Knowledge.

**LOCK:** Permanent closure of Knowledge.

---

# 6. Research States

The following states govern research objects:

| State | Description |
|-------|-------------|
| UNKNOWN | No inquiry exists |
| INVESTIGATING | Investigation in progress |
| RESEARCHED | Investigation complete, findings produced |
| AUDITED | Independent verification complete |
| COMPLETE | All statements extracted and preserved |
| LOCKED | Permanently closed |

---

## Transition Rules

| From | To | Trigger |
|------|----|---------|
| UNKNOWN | INVESTIGATING | CASE begins |
| INVESTIGATING | RESEARCHED | Investigation complete |
| RESEARCHED | AUDITED | Audit complete |
| AUDITED | COMPLETE | All statements extracted |
| COMPLETE | LOCKED | Formal LOCK granted |

---

# 7. Modification Rule

**Research Methodology Version 1.0 MUST NOT be edited directly.**

This methodology may ONLY change through:

1. New CASE identifies gap in methodology
2. Research investigates the gap
3. Audit confirms the gap
4. New version is created

**Evolution mechanism:**

```
V1.0
  ↓
CASE
  ↓
Research
  ↓
Audit
  ↓
V1.1
```

---

# 8. Version Policy

**Version:** 1.0

**Status:** Frozen

**Evolution mechanism:**

- V1.0 → CASE → Audit → V1.1
- Each version is frozen after creation
- Previous versions are preserved as historical evidence

---

# 9. Out of Scope

The following are intentionally excluded from this methodology:

- Knowledge Governance
- Knowledge Promotion
- Repository Governance
- Specification Management
- Future methodology improvements
- Software architecture
- Implementation details
- ADR management

These belong to future investigations.

---

# 10. Certificate

**Research Methodology Version 1.0**

**Status:** Frozen

**Purpose:** Operational research standard

**Date:** 2026-07-21

**Author:** SvitloSk Project

---

**End of Research Methodology V1.0**
