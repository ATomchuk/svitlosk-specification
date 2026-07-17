# Telegram Editorial Principle Duplication

**Date:** 2026-07-13
**Scope:** All semantic overlaps between editorial principles
**Status:** REVIEW COMPLETE

---

# Duplication Analysis

## DU-001: EP-002 (Editorial Truth) vs EP-003 (Editorial Silence)

| Field | EP-002 | EP-003 |
|-------|--------|--------|
| Statement | "Every publication must increase clarity without changing the meaning of the official source. The journal does not interpret, predict or alter official information." | "SvitloSk does not modify open data. SvitloSk does not create new facts. SvitloSk does not produce forecasts. SvitloSk does not alter the meaning of officially published information." |
| Overlap | Both address integrity of official information |
| Distinction | EP-002 focuses on what IS said (truth). EP-003 focuses on what is NOT said (silence). |
| Classification | Partially duplicated |

**Recommendation:** KEEP both. They address the same topic from different angles: "Truth" = accuracy of what we say; "Silence" = restraint in what we don't say.

---

## DU-002: EP-002 (Editorial Truth) vs EP-006 (Source Fidelity)

| Field | EP-002 | EP-006 |
|-------|--------|--------|
| Statement | "Every publication must increase clarity without changing the meaning of the official source." | "Every publication must increase clarity without changing the meaning of the official source. The project interprets data without changing their factual meaning." |
| Overlap | Nearly identical opening sentences |
| Distinction | EP-006 adds "No assumptions, forecasts or predictions SHALL be presented as facts." |
| Classification | Partially duplicated |

**Recommendation:** MERGE EP-006 into EP-002. The additional constraint ("no assumptions") strengthens EP-002 without adding a separate principle.

---

## DU-003: EP-003 (Editorial Silence) vs EP-006 (Source Fidelity)

| Field | EP-003 | EP-006 |
|-------|--------|--------|
| Statement | "SvitloSk does not modify open data. SvitloSk does not create new facts." | "The project interprets data without changing their factual meaning." |
| Overlap | Both address not modifying official information |
| Distinction | EP-003 is absolute (does NOT). EP-006 is relative (without changing meaning). |
| Classification | Partially duplicated |

**Recommendation:** KEEP both. EP-003 is absolute restraint; EP-006 is relative faithfulness.

---

## DU-004: EP-007 (Deterministic Editorial Behaviour) vs EP-010 (Consistency)

| Field | EP-007 | EP-010 |
|-------|--------|--------|
| Statement | "Two identical normalized Datasets SHALL always generate identical Telegram Journals." | "The objective is to ensure that every publication is consistent, easy to read, predictable and automatically generated." |
| Overlap | Both address consistency/predictability |
| Distinction | EP-007 is technical (deterministic output). EP-009 is editorial (consistent experience). |
| Classification | Partially duplicated |

**Recommendation:** KEEP both. EP-007 is a technical guarantee; EP-010 is an editorial goal.

---

## DU-005: EP-001 (Reader First) vs EP-012 (Community-First)

| Field | EP-001 | EP-012 |
|-------|--------|--------|
| Statement | "The primary audience is the residents of the Starokostiantyniv Territorial Community. All editorial decisions shall prioritize the informational needs of this community." | "Although the journal is publicly accessible, all editorial decisions shall prioritize the informational needs of the Starokostiantyniv Community." |
| Overlap | Nearly identical — both prioritize the community |
| Distinction | EP-001 is more precise ("Reader First"); EP-012 is more general ("Community-First") |
| Classification | Fully duplicated |

**Recommendation:** MERGE EP-012 into EP-001. "Reader First" is more precise for a publication system.

---

# Duplication Summary

| # | Principle A | Principle B | Overlap Level | Recommendation |
|---|-----------|-----------|---------------|----------------|
| DU-001 | EP-002 | EP-003 | Partial | KEEP both |
| DU-002 | EP-002 | EP-006 | Partial | MERGE EP-006 into EP-002 |
| DU-003 | EP-003 | EP-006 | Partial | KEEP both |
| DU-004 | EP-007 | EP-010 | Partial | KEEP both |
| DU-005 | EP-001 | EP-012 | Full | MERGE EP-012 into EP-001 |

---

# After Deduplication

| Principle | Status |
|-----------|--------|
| EP-001 (Reader First) | RETAINED (absorbs EP-012) |
| EP-002 (Editorial Truth) | RETAINED (absorbs EP-006) |
| EP-003 (Editorial Silence) | RETAINED |
| EP-004 (Minimal Editorial Intervention) | RETAINED |
| EP-005 (Issue Integrity) | RETAINED |
| EP-006 (Source Fidelity) | MERGED into EP-002 |
| EP-007 (Deterministic Editorial Behaviour) | RETAINED |
| EP-008 (Accuracy Before Speed) | MOVE to PROJECT_PRINCIPLES |
| EP-009 (Territory-First) | RETAINED |
| EP-010 (Consistency) | RETAINED |
| EP-011 (Transparency) | MOVE to PROJECT_PRINCIPLES |
| EP-012 (Community-First) | MERGED into EP-001 |
| MP-001 (Accessibility) | ADD as EP-013 |
| MP-002 (Timeliness) | ADD as EP-014 |

**Total editorial principles after deduplication:** 10

---

**End of Duplication Analysis**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
