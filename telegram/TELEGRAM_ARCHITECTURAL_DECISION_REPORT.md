# Telegram Architectural Decision Report

**Date:** 2026-07-13
**Source:** TELEGRAM_ARCHITECTURAL_EVIDENCE_AUDIT.md + EVIDENCE_FINDINGS.md
**Scope:** Architectural decisions based on verified evidence

---

## Decision Framework

Every decision is based on:
1. Documentary evidence (exact quotes from source documents)
2. Verification status (CONFIRMED / PARTIALLY CONFIRMED / REJECTED)
3. Confidence level (HIGH / MEDIUM / LOW)
4. Architectural principles (PROJECT_PRINCIPLES, GLOSSARY, ARCHITECTURE)

---

## Decision D-001: Publication Lifecycle Ownership

**Question:** Which document SHALL own the "Publication Lifecycle" responsibility?

**Evidence:**
- TJS-002 §1: "defines the complete lifecycle" — CONFIRMED (EB-001)
- TJS-007 §1: "defines the complete lifecycle" — CONFIRMED (EB-001)
- TJS-008 §1: "defines the lifecycle" — CONFIRMED (EB-001)
- All three define lifecycle state models with DIFFERENT state counts and names

**Analysis:**
- TJS-002 has 6 unique sections (publication types, daily schedule flow, emergency flow, archive policy, deletion policy, traceability, reliability)
- TJS-007 has 7 unique sections (creation rules, canonical equality, ordering, ownership, non-destructive channel, diagram, error handling)
- TJS-008 has 12 unique sections (daily cycle, packages, windows, event-driven, stable journal, deterministic, non-destructive update, manual/image, session, diagrams)

**Decision:** The merged document SHALL be created as a NEW document (proposed TJS-005) containing ALL content from TJS-002 + TJS-007 + TJS-008.

**Justification:**
- No single existing document contains the COMPLETE lifecycle
- TJS-008 has the most unique content but lacks ownership and error handling
- TJS-007 has important operational content but lacks daily cycle and windows
- TJS-002 has important conceptual content but is orphaned
- A merged document restores SSOT for the lifecycle responsibility

**Confidence:** HIGH

---

## Decision D-002: Publication Structure Ownership

**Question:** Which document SHALL own the "Publication Structure" responsibility?

**Evidence:**
- TJS-003 §1: "defines the official structure" — CONFIRMED (EB-005)
- TJS-005 §1: "establishes the normative structure, hierarchy" — CONFIRMED (EB-005)
- TJS-003 defines 5 sections with conceptual names
- TJS-005 defines a grammar tree with different section names

**Analysis:**
- TJS-003 is 140 lines, conceptual, Draft status
- TJS-005 is 405 lines, normative, Draft status, includes 4 canonical templates
- TJS-005 is strictly MORE DETAILED and MORE AUTHORITATIVE
- TJS-003's unique content (Graphic block §6, Additional information §7, Footer §8, Editing rules §10) can be absorbed

**Decision:** TJS-003 (Post Structure) SHALL be absorbed into TJS-005 (Message Templates).

**Justification:**
- TJS-005 already covers all structural concepts in greater detail
- TJS-003 adds no information that TJS-005 does not already cover (except 4 minor sections)
- Absorption eliminates dual ownership of "publication structure"

**Confidence:** HIGH

---

## Decision D-003: Formatting Rules Ownership

**Question:** Which document SHALL own "formatting rules"?

**Evidence:**
- TJS-003 §9: General principles (spacing, typography) — CONFIRMED (EB-006)
- TJS-004 §11: Permitted types (bold + plain text) — CONFIRMED (EB-006)
- TJS-005 §15: Implementation (bold with HTML tag) — CONFIRMED (EB-006)
- TJS-004 is the ONLY Approved document
- TJS-005 explicitly depends on TJS-004 (declared in References)

**Analysis:**
- TJS-004 owns the POLICY (what is permitted)
- TJS-005 owns the IMPLEMENTATION (how to render in HTML)
- TJS-003's general principles are subsumed by TJS-004's policy
- The relationship is already declared: TJS-005 depends on TJS-004

**Decision:** TJS-004 SHALL own formatting POLICY. TJS-005 SHALL own formatting IMPLEMENTATION. TJS-003's formatting rules SHALL be absorbed into TJS-004.

**Justification:**
- TJS-004 is Approved — highest authority
- TJS-005 explicitly depends on TJS-004
- The policy/implementation split is architecturally sound
- Absorption of TJS-003 eliminates the triplication

**Confidence:** HIGH

---

## Decision D-004: Settlement Ordering Resolution

**Question:** What is the authoritative settlement ordering rule?

**Evidence:**
- TJS-005 §7: "Settlements SHALL appear in the canonical order defined by TERRITORIAL_MODEL.md. Alphabetical sorting is prohibited."
- TJS-006 §7: "Settlements SHALL be ordered alphabetically using the Ukrainian alphabet."
- MUTUALLY EXCLUSIVE — CONFIRMED (EB-007)

**Analysis:**
- TJS-005 defines the CONTENT order (what order settlements appear in the data)
- TJS-006 defines the RENDERING order (how settlements are sorted in the output)
- These could be DIFFERENT scopes if TERRITORIAL_MODEL.md canonical order IS alphabetical
- If TERRITORIAL_MODEL.md canonical order is NOT alphabetical, the rules are truly contradictory

**Decision:** An ADR is REQUIRED to resolve this conflict. The resolution options are:

**Option A:** TERRITORIAL_MODEL.md canonical order IS the rendering order. TJS-005 is correct. TJS-006 §7 SHALL be updated to reference TJS-005's canonical order.

**Option B:** Alphabetical order IS the rendering order. TJS-006 is correct. TJS-005 §7 SHALL be updated to allow alphabetical sorting.

**Option C:** Different scopes. TJS-005 defines content order (for data). TJS-006 defines rendering order (for display). TJS-006 §7 SHALL clarify its scope as "rendering order within the Telegram output."

**Justification:** The conflict is CONFIRMED with HIGH confidence. An ADR is the only way to resolve contradictory normative rules.

**Confidence:** HIGH (the conflict is confirmed; the resolution requires an ADR)

---

## Decision D-005: TJS-002 Absorption

**Question:** What happens to TJS-002's unique content?

**Evidence:**
- TJS-002 is not referenced by any other TJS document — CONFIRMED (EB-011)
- TJS-002's unique content: publication types (§4), daily schedule flow (§5), emergency flow (§6), archive policy (§9), deletion policy (§10), traceability (§11), reliability (§12)
- TJS-002's overlapping content: lifecycle states (§3), update rules (§8), temporary publications (§7)

**Analysis:**
- TJS-002's unique content has NO owner if TJS-002 is removed
- The unique content is IMPORTANT (publication types, traceability, reliability)
- The overlapping content is ALREADY duplicated in TJS-007 and TJS-008

**Decision:** TJS-002's unique content SHALL be absorbed into the merged TJS-005 (Publication Lifecycle).

**Justification:**
- Publication types belong in the lifecycle document
- Archive policy and deletion policy belong in the lifecycle document
- Traceability and reliability belong in the lifecycle document
- Absorption ensures no content is lost

**Confidence:** HIGH

---

## Decision D-006: 8 → 7 Architecture Validation

**Question:** Does the proposed 8 → 7 architecture remain justified?

**Evidence:**
- 8 SSOT violations CONFIRMED (EB-001 through EB-008, EB-011)
- 1 CONFLICT CONFIRMED (EB-007)
- 2 overlaps REJECTED as not violations (EB-009, EB-010)
- 1 classification changed (EB-004: SSOT → Required Evidence)

**Analysis:**
The original proposal recommended:
1. MERGE TJS-002 + TJS-007 + TJS-008 → TJS-005 ✓ CONFIRMED
2. ABSORB TJS-003 into TJS-005 (Message Templates) ✓ CONFIRMED
3. RENUMBER TJS-004 → TJS-002, TJS-005 → TJS-003, TJS-006 → TJS-004 ⚠ NOT recommended
4. CREATE TJS-006 (Channel Management) ✓ CONFIRMED
5. CREATE TJS-007 (Graphic Rendering) ✓ CONFIRMED

**Decision:** The 8 → 7 architecture is JUSTIFIED with one modification: NO RENUMBERING of existing documents.

**Revised Architecture:**

| # | Document ID | Name | Responsibility | Origin |
|---|------------|------|---------------|--------|
| 1 | TJS-001 | Journal Concept | Identity, mission, principles | RETAIN |
| 2 | TJS-002 | Editorial Policy | Editorial rules, formatting policy | RETAIN (current ID) |
| 3 | TJS-003 | Message Templates | Templates, structure, formatting implementation | RETAIN (absorb TJS-003 Post Structure) |
| 4 | TJS-004 | Rendering Rules | Rendering pipeline, HTML, sorting | RETAIN (current ID) |
| 5 | TJS-005 | Publication Lifecycle | Complete lifecycle | MERGED from TJS-002 + TJS-007 + TJS-008 |
| 6 | TJS-006 | Channel Management | Telegram Bot API, rate limits | NEW |
| 7 | TJS-007 | Graphic Rendering | Graphics for Telegram | NEW |

**Justification:**
- All SSOT violations are resolved
- The settlement ordering conflict is flagged for ADR
- No unnecessary renumbering
- All unique content is preserved
- Missing areas are addressed

**Confidence:** HIGH

---

## Decision Summary

| Decision | Status | Confidence |
|----------|--------|------------|
| D-001: Lifecycle ownership → merged TJS-005 | DECIDED | HIGH |
| D-002: Structure ownership → TJS-005 absorbs TJS-003 | DECIDED | HIGH |
| D-003: Formatting ownership → TJS-004 = policy, TJS-005 = implementation | DECIDED | HIGH |
| D-004: Settlement ordering → ADR REQUIRED | PENDING | HIGH (conflict confirmed) |
| D-005: TJS-002 absorption → into merged TJS-005 | DECIDED | HIGH |
| D-006: 8 → 7 architecture → JUSTIFIED (no renumbering) | DECIDED | HIGH |

---

## Architectural Principles Compliance

| Principle | Current | After Decisions |
|-----------|---------|----------------|
| P-10: One Document — One Subject | VIOLATED | COMPLIANT |
| P-09: Stable Terminology | COMPLIANT | COMPLIANT |
| P-06: Transparency | PARTIALLY | COMPLIANT |
| P-08: Organic Growth | VIOLATED | COMPLIANT |
| GLOSSARY: Publication Lifecycle | VIOLATED (3 definitions) | COMPLIANT (1 definition) |
| ARCHITECTURE: Separation of Responsibilities | VIOLATED | COMPLIANT |

---

**End of Decision Report**

**Architect:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
