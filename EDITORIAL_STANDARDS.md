# EDITORIAL STANDARDS

Status: Stable (Стабільний)

Document ID: DOC-003

Document Class: Normative

Author: SvitloSk Project

---

# Purpose

This document establishes the normative editorial standard for all documentation maintained within the SvitloSk Project Specification repository.

Its purpose is to ensure that every document remains consistent, understandable, maintainable and suitable for long-term engineering development.

All normative documentation within the repository SHALL comply with this standard.

---

# Why this document matters

Documentation is an engineering asset.

Consistent documentation improves maintainability, reduces ambiguity, simplifies architectural evolution and preserves institutional knowledge throughout the lifetime of the project.

---

# 1. General Editorial Principles

Documentation SHALL prioritize clarity over creativity.

Documentation SHALL prioritize precision over verbosity.

Documentation SHALL preserve consistency across the repository.

Documentation SHALL use stable terminology.

Documentation SHALL avoid ambiguity whenever possible.

Every document SHALL describe one complete subject.

---

# 2. Canonical Language

English SHALL be the canonical language of the repository.

Official Ukrainian translations MAY be maintained.

Translations SHALL preserve the meaning of the canonical documentation rather than its literal wording.

Architectural changes SHALL always be introduced into the canonical English documentation before being reflected in translated versions.

---

# 3. One Subject — One Document

Each normative document SHALL define one primary subject.

Each document SHALL have a clearly defined responsibility.

Documents SHOULD complement one another rather than overlap.

Cross-references SHALL be used instead of duplicated explanations.

---

# 4. Stable Terminology

Each approved technical term SHALL have exactly one meaning.

Approved terminology SHALL remain stable throughout the repository.

Changing established terminology requires an approved Architecture Decision Record (ADR).

Terminology SHALL remain consistent across all documents.

---

# 5. Normative Language

Normative documents SHALL use RFC 2119 terminology where applicable.

The following keywords have normative meaning:

- SHALL
- SHALL NOT
- SHOULD
- SHOULD NOT
- MAY

These keywords SHALL always be interpreted according to RFC 2119.

---

# 6. Document Structure

Every normative document SHALL contain the following sections where applicable:

- Title
- Status
- Document ID
- Document Class
- Author
- Purpose
- Why this document matters
- Normative Content
- References

Documents SHOULD follow a consistent logical structure.

---

# 7. Minimum Required Content

Every normative document SHALL clearly define:

- what the document governs;
- why the document exists;
- its scope of responsibility;
- dependencies on other documents;
- relationships with other repository documents.

Normative requirements SHALL be stated explicitly.

---

# 8. Markdown Standard

Markdown SHALL be used for all repository documentation.

Markdown SHALL remain readable without rendering.

Headings SHALL follow a consistent hierarchy.

Lists SHALL use a consistent style.

Tables SHOULD be used only when they improve readability.

Code blocks SHALL be used only where appropriate.

---

# 9. References

Normative documents SHOULD reference authoritative sources whenever applicable.

References MAY include:

- project documents;
- RFCs;
- international standards;
- official legislation;
- Architecture Decision Records (ADR).

Cross-references SHALL remain valid throughout the repository.

---

# 10. Document Lifecycle

Every normative document SHALL have exactly one lifecycle status.

Allowed statuses are:

- Draft (Чернетка)
- Review (На розгляді)
- Stable (Стабільний)
- Deprecated (Застарілий)
- Archived (Архівний)

Lifecycle status SHALL accurately reflect the maturity of the document.

---

# 11. Metadata Standard

Every normative document SHALL use the canonical metadata model.

Metadata SHALL appear in the following order:

- Status
- Document ID
- Document Class
- Author

Additional metadata fields SHALL NOT be introduced without repository-wide approval.

Metadata formatting SHALL remain consistent across the repository.

---

# 12. Repository Documentation Principles

The canonical repository SHALL contain approved documentation only.

Temporary drafts, experimental materials and personal working notes SHALL NOT become part of the canonical repository.

Audit artifacts SHALL remain isolated from the canonical documentation.

Documentation SHALL evolve through controlled engineering processes.

---

# 13. Editorial Responsibility

Every accepted commit becomes part of the permanent engineering history of the project.

Editors SHOULD improve existing documentation before introducing new documents.

Quality SHALL always take precedence over quantity.

Editorial quality is a long-term engineering responsibility.

---

# 14. Repository Consistency

Repository documentation SHALL remain internally consistent.

Every document SHALL comply with:

- the canonical terminology;
- the canonical metadata model;
- the approved repository structure;
- the approved editorial standard.

Repository-wide inconsistencies SHOULD be resolved before introducing new documentation.

---

# References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md

## Referenced by

All normative repository documents.

---

**End of Document**