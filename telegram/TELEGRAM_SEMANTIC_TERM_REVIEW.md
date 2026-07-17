# Telegram Semantic Term Review

**Date:** 2026-07-13
**Scope:** Every candidate term from the Terminology Harvest
**Source:** TELEGRAM_GLOSSARY_CANDIDATE.md + TELEGRAM_TERMINOLOGY_MATRIX.md

---

# Purpose

For each candidate term, determine: Canonical English, Ukrainian Translation, Category, Owner, Status (APPROVED/DERIVED/MERGE/REMOVE/DEPRECATED), and merge/remove/deprecated details.

---

# Special Attention Terms

## Journal

| Field | Value |
|-------|-------|
| Canonical English | Journal |
| Ukrainian | Журнал |
| Category | Core |
| Owner | TJS-000 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Defined in TJS-002 §4 as "continuous informational publication of the SvitloSk project." Used consistently across all TJS documents. No conflicts detected.

---

## Issue

| Field | Value |
|-------|-------|
| Canonical English | Issue |
| Ukrainian | Випуск журналу |
| Category | Core |
| Owner | TJS-000 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Defined in TJS-000 §4 as "one editorial edition of the Journal for a single calendar day." Defined but NOT used by any TJS specification. The concept exists semantically but has no operational adoption.

---

## Publication

| Field | Value |
|-------|-------|
| Canonical English | Publication |
| Ukrainian | Публікація |
| Category | Core |
| Owner | TJS-000 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Defined in TJS-000 §4 as "one independent publication belonging to an Issue." Used by all TJS documents. Has hidden synonyms (Message, Post) that should be deprecated.

---

## Text Publication

| Field | Value |
|-------|-------|
| Canonical English | Text Publication |
| Ukrainian | Текстова публікація |
| Category | Derived |
| Owner | Implicit |
| Status | **DERIVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | Publication |
| Replacement | — |

**Analysis:** Implicit concept — a Publication containing text only (as opposed to Image Publications). Not explicitly defined in any TJS document but used implicitly.

---

## Graphic Publication

| Field | Value |
|-------|-------|
| Canonical English | Graphic Publication |
| Ukrainian | Графічна публікація |
| Category | Derived |
| Owner | Implicit |
| Status | **DERIVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | Publication |
| Replacement | — |

**Analysis:** Implicit concept — a Publication containing graphics. Overlaps with "Image Publications" (TJS-008 §14) and "Graphic Rendering" (TJS-007 proposed). Should be unified with "Image Publications."

---

## System Publication

| Field | Value |
|-------|-------|
| Canonical English | System Publication |
| Ukrainian | Системна публікація |
| Category | Derived |
| Owner | Implicit |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | Redundant — all system-generated publications are simply "Publications." The "System" qualifier adds no semantic value. |
| Parent Term | — |
| Replacement | Publication |

**Analysis:** Not used in any TJS document. The concept of "automatically generated publication" is already covered by the lifecycle model.

---

## Publisher

| Field | Value |
|-------|-------|
| Canonical English | Publisher |
| Ukrainian | Видавець |
| Category | Core |
| Owner | TJS-000 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Logical Role defined in GLOSSARY.md. Used in TJS-005, TJS-006, TJS-007, TJS-008. Has related concept "Telegram Publisher" (platform-specific) and "Publication Engine" (architectural Component). All three are distinct and should coexist.

---

## Telegram Publisher

| Field | Value |
|-------|-------|
| Canonical English | Telegram Publisher |
| Ukrainian | Telegram Видавець |
| Category | Platform |
| Owner | TJS-006 (proposed) |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | Publisher |
| Replacement | — |

**Analysis:** Telegram-specific implementation of the Publisher Role. Distinct from "Publisher" (Role) and "Publication Engine" (Component). Should remain as a platform-specific term.

---

## Coordinator

| Field | Value |
|-------|-------|
| Canonical English | Coordinator |
| Ukrainian | Координатор |
| Category | — |
| Owner | — |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | NOT USED in any Telegram document. Not part of the Telegram subsystem vocabulary. |
| Parent Term | — |
| Replacement | — |

**Analysis:** This term does not appear in any Telegram document. It should not be in the terminology inventory.

---

## Workflow

| Field | Value |
|-------|-------|
| Canonical English | Workflow |
| Ukrainian | Робочий процес |
| Category | — |
| Owner | — |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | NOT USED as a semantic concept in Telegram documents. "Daily Publication Cycle" and "Processing Flow" cover the workflow concept. |
| Parent Term | — |
| Replacement | Daily Publication Cycle |

---

## Rendering

| Field | Value |
|-------|-------|
| Canonical English | Rendering |
| Ukrainian | Рендеринг |
| Category | Rendering |
| Owner | TJS-004 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** The process of converting an Interpretation Result into a presentation-ready Publication. Defined in GLOSSARY.md. Used in TJS-004 (Rendering Rules) and TJS-006.

---

## Formatting

| Field | Value |
|-------|-------|
| Canonical English | Formatting |
| Ukrainian | Форматування |
| Category | Formatting |
| Owner | TJS-004 (policy) + TJS-005 (implementation) |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Rules for text presentation. Split between TJS-004 (policy) and TJS-005 (implementation). This is a correct policy/implementation separation.

---

## Rendering Rules

| Field | Value |
|-------|-------|
| Canonical English | Rendering Rules |
| Ukrainian | Правила рендерингу |
| Category | Rendering |
| Owner | TJS-004 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** The canonical rendering pipeline and rules. Defined in TJS-006 (current) which maps to TJS-004 in the approved architecture. Unique responsibility.

---

## Publication Lifecycle

| Field | Value |
|-------|-------|
| Canonical English | Publication Lifecycle |
| Ukrainian | Життєвий цикл публікації |
| Category | Lifecycle |
| Owner | TJS-005 (merged) |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** The complete lifecycle from creation to archival. Currently defined in THREE documents (TJS-002, TJS-007, TJS-008). Should be unified in TJS-005. The term itself is canonical.

---

## Lifecycle State

| Field | Value |
|-------|-------|
| Canonical English | Lifecycle State |
| Ukrainian | Стан життєвого циклу |
| Category | Lifecycle |
| Owner | TJS-005 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | Publication Lifecycle |
| Replacement | — |

**Analysis:** One of the states a publication passes through (Generated, Published, Updated, Archived, Removed). Used in all three lifecycle documents.

---

## Temporary Publication

| Field | Value |
|-------|-------|
| Canonical English | Temporary Publication |
| Ukrainian | Тимчасова публікація |
| Category | Lifecycle |
| Owner | TJS-005 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | Publication |
| Replacement | — |

**Analysis:** Publication that may be removed after becoming irrelevant. Currently defined with different scopes in TJS-002 (3 types) and TJS-007/008 (1 type). Should be unified.

---

## Permanent Publication

| Field | Value |
|-------|-------|
| Canonical English | Permanent Publication |
| Ukrainian | Постійна публікація |
| Category | Lifecycle |
| Owner | TJS-005 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | Publication |
| Replacement | — |

**Analysis:** Publication that remains in the Journal forever. Currently overlaps with "Historical Publication" and "Current-day Publication." Should be the single canonical term for non-removable publications.

---

## Working Repository

| Field | Value |
|-------|-------|
| Canonical English | Working Repository |
| Ukrainian | Робочий репозиторій |
| Category | — |
| Owner | — |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | NOT USED in Telegram documents. This is a repository governance concept, not a Telegram semantic concept. |
| Parent Term | — |
| Replacement | — |

---

## Historical Storage

| Field | Value |
|-------|-------|
| Canonical English | Historical Storage |
| Ukrainian | Історичне сховище |
| Category | — |
| Owner | — |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | NOT USED as a semantic concept in Telegram documents. "Archive" and "Historical Archive" cover this concept. |
| Parent Term | — |
| Replacement | Archive |

---

## Journal Finality

| Field | Value |
|-------|-------|
| Canonical English | Journal Finality |
| Ukrainian | Фіналізація журналу |
| Category | — |
| Owner | — |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | NOT USED in any Telegram document. Not a semantic concept. |
| Parent Term | — |
| Replacement | — |

---

## Repository

| Field | Value |
|-------|-------|
| Canonical English | Repository |
| Ukrainian | Репозиторій |
| Category | — |
| Owner | — |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | NOT a Telegram semantic concept. This is a Git repository concept. |
| Parent Term | — |
| Replacement | — |

---

## Telegram

| Field | Value |
|-------|-------|
| Canonical English | Telegram |
| Ukrainian | Телеграм |
| Category | Core |
| Owner | TJS-000 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Primary publication channel. Defined in TJS-000 §4. Used consistently.

---

## Settlement

| Field | Value |
|-------|-------|
| Canonical English | Settlement |
| Ukrainian | Населений пункт |
| Category | Administrative |
| Owner | GLOSSARY |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Populated place within a territory. Defined in GLOSSARY.md. Used in TJS-004, TJS-005.

---

## Starostyn District

| Field | Value |
|-------|-------|
| Canonical English | Starosta District |
| Ukrainian | Старостинський округ |
| Category | Administrative |
| Owner | GLOSSARY |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Territorial subdivision. Defined in GLOSSARY.md. Note: "Starostyn" is a variant spelling — "Starosta" is the canonical form.

---

## Community

| Field | Value |
|-------|-------|
| Canonical English | Community |
| Ukrainian | Територіальна громада |
| Category | Administrative |
| Owner | GLOSSARY |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Primary territorial scope. Defined in GLOSSARY.md. Used in TJS-001.

---

## Channel

| Field | Value |
|-------|-------|
| Canonical English | Channel |
| Ukrainian | Канал |
| Category | Platform |
| Owner | TJS-000 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | — |
| Replacement | — |

**Analysis:** Communication medium. Defined in TJS-000 §5. Used in TJS-001, TJS-007.

---

## Archive

| Field | Value |
|-------|-------|
| Canonical English | Archive |
| Ukrainian | Архів |
| Category | Lifecycle |
| Owner | TJS-005 |
| Status | **APPROVED** |
| Merge Into | — |
| Reason | — |
| Parent Term | Publication Lifecycle |
| Replacement | — |

**Analysis:** The state of preserved historical publications. Related to "Archive Policy" (rules) and "Archived" (state).

---

## History

| Field | Value |
|-------|-------|
| Canonical English | History |
| Ukrainian | Історія |
| Category | — |
| Owner | — |
| Status | **REMOVE** |
| Merge Into | — |
| Reason | NOT USED as a semantic concept in Telegram documents. "Archive" and "Historical Archive" cover this concept. |
| Parent Term | — |
| Replacement | Archive |

---

# Complete Term Status Summary

| # | Term | Status | Action Required |
|---|------|--------|----------------|
| 1 | Journal | APPROVED | None |
| 2 | Issue | APPROVED | None |
| 3 | Publication | APPROVED | None |
| 4 | Text Publication | DERIVED | Document as derived from Publication |
| 5 | Graphic Publication | DERIVED | Merge with Image Publications |
| 6 | System Publication | REMOVE | Redundant — use Publication |
| 7 | Publisher | APPROVED | None |
| 8 | Telegram Publisher | APPROVED | None |
| 9 | Coordinator | REMOVE | Not used |
| 10 | Workflow | REMOVE | Not used |
| 11 | Rendering | APPROVED | None |
| 12 | Formatting | APPROVED | None |
| 13 | Rendering Rules | APPROVED | None |
| 14 | Publication Lifecycle | APPROVED | None (unify in TJS-005) |
| 15 | Lifecycle State | APPROVED | None |
| 16 | Temporary Publication | APPROVED | None (unify scope) |
| 17 | Permanent Publication | APPROVED | None (unify with Historical) |
| 18 | Working Repository | REMOVE | Not Telegram concept |
| 19 | Historical Storage | REMOVE | Use Archive |
| 20 | Journal Finality | REMOVE | Not used |
| 21 | Repository | REMOVE | Not Telegram concept |
| 22 | Telegram | APPROVED | None |
| 23 | Settlement | APPROVED | None |
| 24 | Starostyn District | APPROVED | Note spelling variant |
| 25 | Community | APPROVED | None |
| 26 | Channel | APPROVED | None |
| 27 | Archive | APPROVED | None |
| 28 | History | REMOVE | Use Archive |

---

**End of Semantic Term Review**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
