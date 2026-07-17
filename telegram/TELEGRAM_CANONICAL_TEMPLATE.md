# Telegram Canonical Template

**Document ID:** TJS-TEMPLATE-CANONICAL

**Title:** Telegram Canonical Specification Template

**Document Class:** Foundational

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document provides the canonical template for writing Telegram specifications. Every Telegram specification SHALL use this skeleton as its starting point.

---

# Template

```markdown
# [Document Title]

Document ID: TJS-XXX

Title: [Human-Readable Title]

Document Class: Normative

Status: Draft

Author: SvitloSk Project

---

# 1. Purpose

[2-3 sentences describing what this specification covers and what its authority is.]

---

# 2. Scope

- [What this specification covers]
- [What this specification does NOT cover]

---

# 3. [Domain Section 1: Mission/Concepts]

[Define the mission and core concepts of this specification.]

---

# 4. [Domain Section 2: Principles/Behaviour]

[Define the governing principles and expected behaviour.]

---

# 5. [Domain Section 3: Constraints/Boundaries]

[Define the mandatory constraints and boundaries.]

---

# 6. [Domain Section 4: Responsibilities]

[Define the responsibilities owned by this specification.]

---

# 7. [Domain Section 5: Guarantees]

[Define the architectural guarantees provided.]

---

# 8. [Domain Section 6: Interactions]

[Define how this specification interacts with other specifications.]

---

# 9. [Domain Section 7: Quality/Governance]

[Define the quality requirements and governance model.]

---

# 10. Constraints

[Repeat or reference the mandatory constraints.]

---

# 11. Out of Scope

- [Exclusion 1 — responsible document reference]
- [Exclusion 2 — responsible document reference]

---

# 12. Traceability

## Semantic Foundation

- [Reference to TELEGRAM_SEMANTIC_MODEL.md]
- [Reference to TELEGRAM_GLOSSARY.md]

## Architecture Decision

- [Reference to TELEGRAM_ARCHITECTURE_DECISION.md]

## Document ID

- TJS-XXX — [Title]

---

# 13. Change History

| Date | Version | Description |
|------|---------|-------------|
| YYYY-MM-DD | 1.0 | Initial publication |

---

# Depends on

- [Document 1 — TJS-XXX]
- [Document 2 — TJS-XXX]

---

# Referenced by

- [Document 3 — TJS-XXX]
- [Document 4 — TJS-XXX]

---

**End of Document**
```

---

# Template Usage Rules

## Rule 1: Do Not Remove Sections

All sections in the template SHALL appear in every Telegram specification. No section SHALL be removed.

## Rule 2: Add Domain Sections

The template includes placeholder domain sections (3-9). Every Telegram specification SHALL have at least 1 domain section. The exact number and titles depend on the specification's domain.

## Rule 3: Fill All Required Fields

Every required field (Document ID, Title, Document Class, Status, Author) SHALL be filled.

## Rule 4: Follow Writing Standard

All content SHALL follow TELEGRAM_CANONICAL_WRITING_STANDARD.md.

## Rule 5: Follow Quality Standard

All content SHALL satisfy TELEGRAM_CANONICAL_QUALITY_STANDARD.md.

---

# Depends on

- TELEGRAM_CANONICAL_SPECIFICATION_STANDARD.md (TJS-STD)
- TELEGRAM_CANONICAL_WRITING_STANDARD.md
- TELEGRAM_CANONICAL_QUALITY_STANDARD.md
- TELEGRAM_CANONICAL_SECTION_STANDARD.md

---

# Referenced by

- Every future Telegram specification

---

**End of Document**
