# Telegram Glossary Editorial Review

**Date:** 2026-07-13
**Scope:** Final editorial verification before TELEGRAM_GLOSSARY.md creation
**Methodology:** Editorial review only — no new semantic decisions

---

# Purpose

This document performs the final editorial verification of the approved Telegram terminology. It checks internal consistency, translation quality, naming conventions and style compliance.

---

# Editorial Issues Detected

## Issue E-001: Count Discrepancy Between Documents

| Field | Value |
|-------|-------|
| Term | (all terms) |
| Issue | TELEGRAM_CANONICAL_SEMANTIC_MODEL.md lists 82 APPROVED terms. TELEGRAM_TERM_APPROVAL_REGISTER.md lists 91 APPROVED terms. The difference is 9 terms (Platform concepts listed in Register but not in Canonical Model). |
| Recommended Correction | Update TELEGRAM_CANONICAL_SEMANTIC_MODEL.md to include all 91 APPROVED terms, or clarify that the Canonical Model lists only semantic concepts (excluding Platform terms). |
| Reason | Internal inconsistency between approved documents. |
| Severity | MAJOR |

---

## Issue E-002: "subscribers" and "administrators" Lowercase

| Field | Value |
|-------|-------|
| Term | subscribers, administrators |
| Issue | These terms use lowercase in the Canonical Model and Register. All other terms use Title Case. |
| Recommended Correction | Capitalize to "Subscribers" and "Administrators" for consistency. |
| Reason | English capitalization should be consistent across all glossary entries. |
| Severity | MINOR |

---

## Issue E-003: "Telegram Bot API" Translation Redundancy

| Field | Value |
|-------|-------|
| Term | Telegram Bot API |
| Issue | The Ukrainian translation is "Telegram Bot API" — identical to the English. This is technically correct (it's a proper noun) but should be noted as intentional. |
| Recommended Correction | No change needed. "Telegram Bot API" is a proper noun that retains its English form in Ukrainian. |
| Reason | Proper nouns are typically not translated. This is correct behavior. |
| Severity | OBSERVATION |

---

## Issue E-004: "Publication Package" Dual Status

| Field | Value |
|-------|-------|
| Term | Publication Package |
| Issue | Listed as DERIVED in TELEGRAM_DERIVED_TERMS.md (D-009) with "Parent Concept: —" (no parent). But DERIVED terms are supposed to have a parent concept. |
| Recommended Correction | Either: (a) Change status to APPROVED since it has no parent, or (b) Identify a parent concept (e.g., "Publication" or "Grouping"). |
| Reason | DERIVED status requires a parent concept. If no parent exists, the term should be APPROVED. |
| Severity | MINOR |

---

## Issue E-005: "Graphic Publication" Overlaps with "Image Publications"

| Field | Value |
|-------|-------|
| Term | Graphic Publication |
| Issue | DERIVED term "Graphic Publication" overlaps with APPROVED Platform term "Image Publications." The D-002 entry notes: "Should be unified with Image Publications." |
| Recommended Correction | Either: (a) Remove "Graphic Publication" as DERIVED and keep "Image Publications" as the sole term, or (b) Clarify that "Graphic Publication" is a semantic concept while "Image Publications" is a platform behaviour. |
| Reason | Two terms for the same concept create confusion. |
| Severity | MINOR |

---

## Issue E-006: "Archive" vs "Archived" Distinction

| Field | Value |
|-------|-------|
| Term | Archive, Archived |
| Issue | "Archive" (#31) is listed as a Lifecycle concept. "Archived" (#14) is also listed as a Lifecycle state. These are related but distinct: "Archive" is a concept/state; "Archived" is the past participle describing the state. |
| Recommended Correction | No change needed. Both are correct: "Archive" = the state; "Archived" = the action of entering that state. |
| Reason | These are linguistically distinct and serve different purposes. |
| Severity | OBSERVATION |

---

## Issue E-007: "Non-destructive" Hyphenation

| Field | Value |
|-------|-------|
| Term | Non-destructive Channel Principle, Non-destructive Update Principle |
| Issue | "Non-destructive" uses a hyphen. This is correct English. However, the Ukrainian translations use "недеструктивного" (no hyphen). This is correct Ukrainian. |
| Recommended Correction | No change needed. Both are correct in their respective languages. |
| Reason | Hyphenation rules differ between English and Ukrainian. |
| Severity | OBSERVATION |

---

## Issue E-008: "Traceability" Ukrainian Capitalization

| Field | Value |
|-------|-------|
| Term | Traceability |
| Issue | Ukrainian translation is "Простежуваність" (capital P). This is correct — it's a standalone term. |
| Recommended Correction | No change needed. |
| Reason | Correct Ukrainian capitalization for standalone terms. |
| Severity | OBSERVATION |

---

## Issue E-009: "SvitloSk" Capitalization

| Field | Value |
|-------|-------|
| Term | SvitloSk |
| Issue | The project name uses mixed case: "SvitloSk" (capital S, lowercase v, capital S, lowercase k). This is the established project name. |
| Recommended Correction | No change needed. This is the official project name. |
| Reason | Project names retain their established capitalization. |
| Severity | OBSERVATION |

---

## Issue E-010: Missing Core Concept Definitions

| Field | Value |
|-------|-------|
| Term | All Core Concepts |
| Issue | The Canonical Semantic Model lists 8 Core Concepts but does not include normative definitions (2-4 sentences each). The Semantic Model (TJS-000) defines Journal, Issue, Publication, and Telegram, but not Publication Engine, Publisher, Parser, or SvitloSk. |
| Recommended Correction | Add concise normative definitions for all 8 Core Concepts in the glossary. TJS-000 §4 provides definitions for Journal, Issue, Publication, and Telegram. GLOSSARY.md provides definitions for Publication Engine, Publisher, and Parser. SvitloSk is a proper noun. |
| Reason | Glossary entries should contain definitions. Core Concepts are the most important entries. |
| Severity | MAJOR |

---

## Issue E-011: "Processing Flow" Not in Canonical Model

| Field | Value |
|-------|-------|
| Term | Processing Flow |
| Issue | The forbidden term "Workflow" recommends replacement with "Processing Flow" (F-009). However, "Processing Flow" is NOT listed as an APPROVED term in the Canonical Model. |
| Recommended Correction | Either: (a) Add "Processing Flow" as an APPROVED term, or (b) Change the replacement to "Rendering Pipeline" (which IS approved). |
| Reason | Forbidden term replacements should reference APPROVED terms. |
| Severity | MINOR |

---

## Issue E-012: "Historical Archive" Not in Canonical Model

| Field | Value |
|-------|-------|
| Term | Historical Archive |
| Issue | The forbidden term "Historical Storage" recommends replacement with "Archive" (F-011). However, "Historical Archive" is defined in TJS-001 §11 and is a distinct concept from "Archive" (state). |
| Recommended Correction | Either: (a) Add "Historical Archive" as an APPROVED term, or (b) Clarify that "Archive" covers both the state and the concept. |
| Reason | TJS-001 §11 explicitly defines "Historical Archive" as a concept. |
| Severity | MINOR |

---

# Editorial Review Summary

| Severity | Count |
|----------|-------|
| MAJOR | 2 |
| MINOR | 4 |
| OBSERVATION | 5 |
| **Total Issues** | **11** |

---

# Special Attention Terms Review

| Term | Status | Editorial Assessment |
|------|--------|---------------------|
| Journal | APPROVED | OK — clear, consistent, unique |
| Issue | APPROVED | OK — clear, consistent, unique |
| Publication | APPROVED | OK — clear, consistent, unique |
| Publisher | APPROVED | OK — clear, consistent, unique |
| Telegram Publisher | APPROVED | OK — clear, consistent, unique |
| Text Publication | DERIVED | OK — clear parent relationship |
| Graphic Publication | DERIVED | MINOR — overlaps with Image Publications |
| System Publication | FORBIDDEN | OK — correctly rejected |
| Temporary Publication | APPROVED | OK — clear, consistent |
| Permanent Publication | APPROVED | OK — clear, consistent |
| Community Publication | NOT LISTED | N/A — not a term in the inventory |
| Settlement Publication | NOT LISTED | N/A — not a term in the inventory |
| Operational Repository | NOT LISTED | N/A — not a term in the inventory |
| Historical Repository | NOT LISTED | N/A — not a term in the inventory |
| Working Repository | FORBIDDEN | OK — correctly rejected |
| Journal Finality Principle | FORBIDDEN | OK — correctly rejected |
| Journal Publishing System | APPROVED | OK — used in TJS-000 §3 |
| Rendering | APPROVED | OK — clear, consistent |
| Formatting | APPROVED | OK — clear, consistent |
| Rendering Rules | APPROVED | OK — clear, consistent |
| Archive | APPROVED | OK — clear, consistent |
| History | FORBIDDEN | OK — correctly rejected |
| Telegram Channel | APPROVED | OK — "Channel" is the canonical term |

---

# Spelling Review

| Check | Result |
|-------|--------|
| English capitalization consistent? | NO — "subscribers" and "administrators" are lowercase (E-002) |
| Ukrainian terminology uses identical spelling? | YES — all Ukrainian terms are consistent |
| "Starosta District" spelling correct? | YES — "Starostyn" is correctly forbidden (F-016) |
| "SvitloSk" capitalization correct? | YES — established project name |

---

# Style Review

| Check | Result |
|-------|--------|
| Glossary entries describe meaning? | YES — all entries have semantic definitions |
| Glossary does NOT contain workflows? | YES — no workflow content in approved terms |
| Glossary does NOT contain algorithms? | YES — no algorithm content in approved terms |
| Glossary does NOT contain processing logic? | YES — no processing logic in approved terms |
| Glossary does NOT contain architecture? | YES — architectural concepts are separated (ARCHITECTURAL status) |
| Glossary does NOT contain technical procedures? | YES — no technical procedures in approved terms |

---

**End of Editorial Review**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
