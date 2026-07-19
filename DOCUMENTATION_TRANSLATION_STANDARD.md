# DOCUMENTATION_TRANSLATION_STANDARD

**Document ID:** DTS-001

**Title:** Documentation Translation Standard

**Document Class:** Normative Foundation Document

**Status:** Stable

**Author:** SvitloSk Project

---

# 1. Purpose

This document defines the normative translation standard for the entire SvitloSk repository. It establishes the rules, conventions, lifecycle, and governance for bilingual documentation.

The English version of every specification SHALL always be considered the canonical specification. Translations exist to serve Ukrainian users while preserving the authority of the English source.

This document is normative. All translated documents SHALL conform to this standard.

---

# 2. Scope

This standard applies to:

- All LEVEL 1 documents (canonical specifications): TJS-000, TJS-000A, TJS-010, TJS-020, TJS-021, TJS-022
- All LEVEL 2 documents (core platform documents): Architecture Decision, Specification Standard, Alignment Process
- Future canonical specifications

This standard does NOT apply to:

- LEVEL 3 documents (optional reference)
- LEVEL 4 documents (engineering artifacts)
- Legacy specifications (TJS-001 through TJS-008)

---

# 3. Canonical Source Rule

The English version SHALL always be considered the canonical specification.

Every translated document SHALL reference its English source.

No translated document may redefine normative requirements.

When terminology conflicts arise between the English version and a Ukrainian translation, the English version SHALL prevail.

Translations exist to serve Ukrainian users. They do NOT modify, override, or extend the canonical English specification.

---

# 4. Translation Status Block

Every translated document SHALL include a mandatory Translation Status block at the top of the file, after the document title and before the first content section.

## 4.1 Status Block Format

`yaml
---
translation_status: [status]
original_document: [English filename]
canonical_version: [version]
translation_version: [version]
last_synchronization: [YYYY-MM-DD]
---
`

## 4.2 Translation Status Values

| Status | Description | When to Use |
|--------|-------------|------------|
| Official Translation | Translation has been reviewed and approved | After successful review and approval |
| Translation Draft | Translation is being created | During initial translation |
| Translation Review | Translation is being reviewed | During review process |
| Translation Requires Synchronization | Ukrainian translation no longer matches canonical English | When English source has been updated |
| Archived Translation | Translation is archived | When English source is archived |

## 4.3 Translation Requires Synchronization

The status Translation Requires Synchronization SHALL be used whenever the Ukrainian translation no longer matches the canonical English specification.

This status replaces any wording such as "does not correspond to canonical interpretation" which SHALL NOT be used.

When the English source is updated, the Ukrainian translation SHALL receive the status Translation Requires Synchronization until synchronization is complete. After successful review, the status SHALL become Official Translation.

---

# 5. Translation Metadata

The following elements SHALL remain identical between English and Ukrainian versions:

| Element | Translates? | Justification |
|---------|------------|--------------|
| Document ID | NO | Permanent identifier, language-independent |
| Status | NO | Architectural status, not language-specific |
| Category | NO | Architectural classification |
| RFC 2119 keywords | NO | International standard (SHALL, SHOULD, MAY) |
| KB IDs | NO | Knowledge Base identifiers |
| Requirement IDs | NO | Requirement identifiers |
| Component IDs | NO | Component identifiers |
| Interaction IDs | NO | Interaction identifiers |
| Principle IDs | NO | Principle identifiers (P-001→P-020, GP-001, GP-002) |
| ADR IDs | NO | Architecture Decision identifiers |
| PROC IDs | NO | Process identifiers |
| Section numbering | NO | Language-independent |

Everything else SHALL be translated.

---

# 6. Terminology Lock

The Translation Terminology Matrix defines approved Ukrainian equivalents for every canonical English term.

One English term SHALL map to exactly one Ukrainian term.

No synonyms are permitted unless explicitly approved through the repository governance process.

When a new term is added to the Glossary, its Ukrainian translation SHALL be defined simultaneously.

The Translation Terminology Matrix is the single authoritative source for translation terminology. No translated document may introduce alternative translations.

---

# 7. Translation Lifecycle

The translation lifecycle is independent from PROC-001.

`
English Stable
    ↓
Translation Draft
    ↓
Translation Review
    ↓
Translation Stable
    ↓
Translation Updated
    ↓
Translation Archived
`

## 7.1 Lifecycle States

| State | Description | Owner |
|-------|-------------|-------|
| English Stable | English source document is Stable | English author |
| Translation Draft | Ukrainian translation is being created | Translator |
| Translation Review | Ukrainian translation is being reviewed | Reviewer |
| Translation Stable | Ukrainian translation is approved and published | Maintainer |
| Translation Updated | Ukrainian translation is updated due to English changes | Translator |
| Translation Archived | Ukrainian translation is archived | Maintainer |

## 7.2 Lifecycle Transitions

| Transition | Trigger | Responsible |
|-----------|---------|-------------|
| English Stable → Translation Draft | English source reaches Stable | Translator |
| Translation Draft → Translation Review | Draft complete | Translator |
| Translation Review → Translation Stable | Review approved | Reviewer |
| Translation Stable → Translation Updated | English source updated | Translator |
| Translation Updated → Translation Stable | Update reviewed | Reviewer |
| Translation Stable → Translation Archived | English source archived | Maintainer |

---

# 8. Synchronization Policy

Whenever the canonical English specification changes, the Ukrainian translation SHALL receive the status Translation Requires Synchronization until synchronization is complete.

After successful review, the status SHALL become Official Translation.

The synchronization process:

1. English source is updated
2. Ukrainian translation receives status: Translation Requires Synchronization
3. Translator updates the Ukrainian translation
4. Reviewer reviews the updated translation
5. After approval, status becomes: Official Translation

---

# 9. Repository Structure

English documents are stored as:

`
filename.md
`

Ukrainian translations are stored as:

`
filename.uk.md
`

This convention was selected because:

1. It follows international GitHub/Open Source best practices
2. It preserves parallel files in the same directory
3. It enables easy cross-linking between versions
4. It maintains repository navigation simplicity
5. It is the standard approach for bilingual documentation

---

# 10. Translation Examples

## 10.1 What Is Translated

| Element | Translated? | Example |
|---------|------------|---------|
| Document title | YES | "Telegram Glossary" → "Телеграм Глосарій" |
| Section titles | YES | "Purpose" → "Призначення" |
| Content | YES | "This document defines..." → "Цей документ визначає..." |
| Examples | YES | Technical examples translated |

## 10.2 What Remains Identical

| Element | Remains Identical? | Example |
|---------|-------------------|---------|
| Document ID | YES | TJS-000A |
| Status | YES | Stable |
| RFC 2119 | YES | SHALL, SHOULD, MAY |
| Section numbers | YES | §1, §2, §3 |
| Principle IDs | YES | P-001→P-020, GP-001, GP-002 |
| Component IDs | YES | Publication Engine, Parser, etc. |

## 10.3 Translation Status Block Example

`yaml
---
translation_status: Official Translation
original_document: TELEGRAM_GLOSSARY.md
canonical_version: 1.0
translation_version: 1.0
last_synchronization: 2026-07-13
---
`

---

# 11. Governance

## 11.1 Who May Modify Translations

| Role | Permission |
|------|-----------|
| Translator | Create Translation Draft |
| Reviewer | Approve Translation Review |
| Maintainer | Update Translation, Archive Translation |
| Administrator | Override Translation Requires Synchronization |

## 11.2 How Reviews Occur

1. Translator creates Translation Draft
2. Translator submits for Translation Review
3. Reviewer compares against English canonical source
4. Reviewer verifies terminology against Translation Terminology Matrix
5. Reviewer approves or requests changes
6. After approval, status becomes Official Translation

## 11.3 How Future Terminology Changes Are Approved

1. New term proposed through RFC process
2. English definition added to Glossary
3. Ukrainian translation added to Translation Terminology Matrix
4. All affected translations receive status: Translation Requires Synchronization
5. Translations updated to include new term
6. After review, status becomes: Official Translation

---

# 12. References

- PROC-001 — Specification Engineering Process
- DOCUMENT_INDEX.md — Repository documentation structure
- Translation Terminology Matrix — Approved Ukrainian equivalents
- Translation Policy — Translation policy decisions
- Translation Lifecycle — Translation lifecycle model
- Translation Readiness Audit — Translation readiness assessment

---

**End of Standard**

**Compiler:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
