# TRANSLATION_WORKFLOW

**Document ID:** TW-002

**Title:** Translation Workflow

**Document Class:** Normative Translation Process Document

**Status:** Stable

**Author:** SvitloSk Project

---

# 1. Purpose

This document defines the deterministic operational workflow for translating every future canonical document in the SvitloSk repository.

This is the authoritative operational workflow for bilingual documentation.

No additional translation process documents SHALL be created unless introduced through ADR.

---

# 2. Scope

This workflow applies to:

- All LEVEL 1 documents (TJS-000, TJS-000A, TJS-010, TJS-020, TJS-021, TJS-022)
- All LEVEL 2 documents (Architecture Decision, Specification Standard, Alignment Process)
- Future canonical specifications

---

# 3. References

This workflow integrates with but does NOT duplicate:

| Document | Reference |
|----------|-----------|
| CHARTER.md | Project identity |
| PROJECT_PRINCIPLES.md | Engineering principles |
| RFC_PROCESS.md | Change governance |
| DOCUMENTATION_TRANSLATION_STANDARD.md (DTS-001) | Translation standard |
| TRANSLATION_STYLE_GUIDE.md | Editorial rules |
| TRANSLATION_QA_CHECKLIST.md | Quality checklist |
| TRANSLATION_TERMINOLOGY_DECISION_REGISTER.md (TTDR-001) | Terminology decisions |
| TERMINOLOGY_FREEZE.md | Terminology freeze |

---

# 4. Workflow Model

The workflow defines exactly six sequential phases.

## Workflow Diagram

`	ext
Phase 1 — Preparation
    |
    v
Phase 2 — Draft Translation
    |
    v
Phase 3 — Translation QA
    |
    v
Phase 4 — Owner Review
    |
    v
Phase 5 — Publication
    |
    v
Phase 6 — Freeze
    |
    v
Next Document
`

---

## Phase 1 — Preparation

**Purpose:** Prepare the translation package.

**CLI SHALL:**

1. Read the English canonical document
2. Load TTDR-001 (terminology register)
3. Load TELEGRAM_GLOSSARY.md
4. Load TRANSLATION_STYLE_GUIDE.md
5. Identify unresolved terminology
6. Identify all tables
7. Identify all diagrams
8. Identify all RFC 2119 keywords (SHALL, SHOULD, MAY)
9. Produce a Preparation Report

**Rules:**

- No translation is produced in this phase
- Preparation Report SHALL list every element requiring attention

**Output:** Preparation Report

---

## Phase 2 — Draft Translation

**Purpose:** Produce the complete Ukrainian draft.

**Rules:**

- Deterministic translation — same input produces same output
- No terminology invention — TTDR-001 is mandatory
- Glossary is mandatory — every term MUST match
- Preserve document structure exactly — same sections, same order
- Preserve identifiers exactly — Document IDs, SSP IDs, TJS IDs remain English
- RFC 2119 keywords remain English — SHALL, SHOULD, MAY are NOT translated
- Tables translated but structure preserved
- Code blocks NOT translated
- File paths NOT translated
- Quotation marks use Ukrainian style: " "

**Output:** <document>.uk.md

---

## Phase 3 — Translation QA

**Purpose:** Technical verification only. No editorial rewriting.

**CLI SHALL verify (using TRANSLATION_QA_CHECKLIST.md):**

1. Terminology consistency — every term matches TTDR-001
2. RFC keyword consistency — all SHALL/SHOULD/MAY preserved
3. Section parity — same number of sections as English
4. Table parity — same number of tables as English
5. Figure parity — same number of figures as English
6. Identifier parity — all Document IDs preserved
7. Internal references — all cross-references valid
8. Formatting — markdown structure identical

**Rules:**

- No editorial rewriting
- QA passes or fails — binary result
- If FAIL: return to Phase 2 with specific corrections

**Output:** QA Report (PASS/FAIL)

---

## Phase 4 — Owner Review

**Purpose:** Human review for readability and quality.

**Owner SHALL review:**

1. Readability — natural Ukrainian text
2. Ukrainian language quality — grammar, style, clarity
3. Clarity — meaning is immediately understandable
4. Natural wording — no awkward translations

**Owner SHALL NOT:**

- Change canonical meaning
- Introduce new terminology
- Modify document structure
- Alter identifiers or RFC keywords

**Rules:**

- Owner approves or requests revision
- If revision requested: return to Phase 2

**Output:** Owner Approval (APPROVED/REVISION REQUESTED)

---

## Phase 5 — Publication

**Purpose:** Publish the approved translation.

**CLI SHALL:**

1. Update DOCUMENT_INDEX.md if required
2. Update README.md only if navigation changes
3. Create exactly one Git commit
4. Push to GitHub

**Rules:**

- Exactly one commit per document
- Commit message format: docs(translation): publish <document>.uk.md
- No other files modified in the same commit

**Output:** Git commit + push

---

## Phase 6 — Freeze

**Purpose:** Mark translation as permanent.

**CLI SHALL:**

1. Mark translation status as Official Translation
2. Close the translation task
3. Prohibit further editing except through ADR or revision process

**Rules:**

- Once frozen, the translation SHALL NOT be modified without ADR
- Future English changes trigger Translation Audit (per DTS-001)
- Translation Requires Synchronization status applied if English changes

**Output:** Translation frozen

---

# 5. Deterministic Rules

| Rule | Statement |
|------|-----------|
| TW-R1 | No phases may be skipped |
| TW-R2 | No phases may run in parallel |
| TW-R3 | No direct publication without QA |
| TW-R4 | No terminology changes during translation |
| TW-R5 | One document at a time |
| TW-R6 | Each document SHALL complete the full workflow before the next begins |
| TW-R7 | Phase 1 MUST complete before Phase 2 begins |
| TW-R8 | Phase 3 MUST complete with PASS before Phase 4 begins |
| TW-R9 | Phase 4 MUST result in APPROVED before Phase 5 begins |
| TW-R10 | Phase 5 produces exactly one commit |
| TW-R11 | Phase 6 freezes translation permanently |

---

# 6. First Translation

**First translation target:** TJS-000.uk.md

No other translation SHALL begin before TJS-000.uk.md completes the full workflow.

---

# 7. Revision Process

If a frozen translation requires updates:

1. English source changes
2. Translation Audit triggered (per DTS-001)
3. If identical: Official Translation remains
4. If different: Translation Requires Synchronization
5. Phase 2 begins with updated English source
6. Full workflow executed again
7. Translation frozen again

---

**End of Workflow**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
