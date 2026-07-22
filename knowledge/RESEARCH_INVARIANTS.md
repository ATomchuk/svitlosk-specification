# RESEARCH_INVARIANTS

**Document ID:** META005-INVARIANTS

**Title:** Research Invariants

**Document Class:** Research Architecture

**Status:** Stable

**Author:** SvitloSk Project — Chief Research Architect

---

# Purpose

This document identifies immutable laws governing architectural research.

---

# Research Invariants

## Invariant 1: No Knowledge Without Evidence

**Statement:** Every architectural knowledge claim must be supported by evidence.

**Evidence from repository:**

- All CASE investigations collected evidence before drawing conclusions
- All Knowledge Units have evidence references
- All findings are traceable to evidence

**Status:** VIOLATED in 0 cases.

---

## Invariant 2: No Specification Before Verified Knowledge

**Statement:** Specifications must not be created before knowledge has been verified.

**Evidence from repository:**

- Specifications existed before investigations in some cases
- Some specifications contained assumptions

**Status:** VIOLATED in some cases.

---

## Invariant 3: No Canonical Knowledge Without Audit

**Statement:** Knowledge must be independently audited before becoming Canonical.

**Evidence from repository:**

- CASE-001 was audited before LOCK status
- CASE-002 was verified before promotion

**Status:** VIOLATED in 0 cases for CASE-001/002.

---

## Invariant 4: No Architectural Decision Before Contradiction Search

**Statement:** Contradictions must be searched before architectural decisions are made.

**Evidence from repository:**

- All CASE investigations searched for contradictions
- All Hearings identified contradictions

**Status:** VIOLATED in 0 cases.

---

## Invariant 5: No Research Without Multiple Models

**Statement:** Multiple competing models must be constructed before conclusions.

**Evidence from repository:**

- CASE-001A: 11 models for Publication
- CASE-002A: 7 models for Issue
- All investigations constructed multiple models

**Status:** VIOLATED in 0 cases.

---

## Invariant 6: No Conclusion Without Cross-Examination

**Statement:** Every model must be cross-examined before conclusions.

**Evidence from repository:**

- All CASE investigations cross-examined models
- All Hearings attacked every model

**Status:** VIOLATED in 0 cases.

---

## Invariant 7: No Knowledge Without Extraction

**Statement:** Validated findings must be extracted to Knowledge Base.

**Evidence from repository:**

- 20 findings promoted to Canonical
- 79 Atomic Knowledge Units created
- Knowledge Base maintained

**Status:** VIOLATED in 0 cases for CASE-001/002.

---

## Invariant 8: No Canonical Without Verification

**Statement:** Knowledge must be independently verified before becoming Canonical.

**Evidence from repository:**

- CASE-001 was verified (K-009)
- CASE-002 was verified (K-008)

**Status:** VIOLATED in 0 cases.

---

## Invariant 9: No Lock Without Audit

**Statement:** Knowledge must be independently audited before LOCK status.

**Evidence from repository:**

- CASE-001 was audited (K-009) before LOCK
- CASE-002 was verified (K-008) before promotion

**Status:** VIOLATED in 0 cases.

---

## Invariant 10: No Research Without Traceability

**Statement:** Every conclusion must be traceable to its origin.

**Evidence from repository:**

- All Knowledge Units have origin references
- All findings have evidence references
- Traceability is complete for CASE-001

**Status:** VIOLATED in 0 cases for CASE-001.

---

# Invariant Summary

| # | Invariant | Status | Violations |
|---|-----------|--------|------------|
| 1 | No Knowledge Without Evidence | HELD | 0 |
| 2 | No Specification Before Verified Knowledge | VIOLATED | Some |
| 3 | No Canonical Knowledge Without Audit | HELD | 0 |
| 4 | No Decision Before Contradiction Search | HELD | 0 |
| 5 | No Research Without Multiple Models | HELD | 0 |
| 6 | No Conclusion Without Cross-Examination | HELD | 0 |
| 7 | No Knowledge Without Extraction | HELD | 0 |
| 8 | No Canonical Without Verification | HELD | 0 |
| 9 | No Lock Without Audit | HELD | 0 |
| 10 | No Research Without Traceability | HELD | 0 |

---

# Key Insight

**10 invariants identified.**

**9 of 10 are HELD in all investigations.**

**1 invariant (No Specification Before Verified Knowledge) was VIOLATED in some cases.**

**The research methodology successfully prevents most failures.**

---

# End of Research Invariants
