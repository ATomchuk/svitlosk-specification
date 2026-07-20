# TRANSLATION_TERMINOLOGY_DECISION_REGISTER

**Document ID:** TTDR-001

**Title:** Translation Terminology Decision Register

**Document Class:** Normative Translation Governance Document

**Status:** Stable

**Author:** SvitloSk Project

---

# 1. Purpose

This document defines how translation terminology decisions are made, approved, documented and preserved.

Every project translation term SHALL belong to exactly one category.

Every term SHALL be approved through this register before appearing in any translated document.

---

# 2. Terminology Categories

Every project translation term SHALL belong to exactly one of the following categories.

---

## Category A — Architecture Terms

Terms describing architectural objects, components, roles, and structural concepts.

Examples: Publication Engine, Publisher, Pipeline, Component, Role, Subsystem, Module, Engine, Parser, Channel.

These terms describe HOW the system is organized.

---

## Category B — Deterministic Terms

Terms describing repository and specification behaviour guarantees.

Examples: Canonical Equality, Deterministic, Stable, Reproducible, Immutable.

These terms describe WHAT the system guarantees about its behaviour.

---

## Category C — Public Communication Terms

Terms describing information presented to end users of the Telegram channel.

Examples: Powered, Outage, Emergency Outage, Planned Outage, Restoration, Queue, Subqueue.

These terms describe WHAT the Journal communicates to residents.

---

# 3. Decision Template

Every approved term SHALL be documented using the following template.

| Field | Description |
|-------|-------------|
| English term | The canonical English term |
| Category | A (Architecture), B (Deterministic), or C (Public Communication) |
| Meaning inside SvitloSk | What this term means within the project specifically |
| Approved Ukrainian equivalent | The single approved translation |
| Rejected alternatives | Other translations that were considered |
| Reason for rejection | Why each alternative was rejected |
| Rationale | Why the approved translation was selected |
| Date approved | Date of owner approval |
| Approved by | Name or role of approver |
| Status | APPROVED or PENDING OWNER APPROVAL |

---

# 4. Decision Rules

| Rule | Statement |
|------|-----------|
| TTDR-R1 | Every translation term SHALL belong to exactly one category |
| TTDR-R2 | No term may be used in a translated document without approval in this register |
| TTDR-R3 | Category C terms MAY have context-dependent translations (see Term 3 rules) |
| TTDR-R4 | Category A and B terms SHALL have exactly ONE approved translation |
| TTDR-R5 | Rejected alternatives SHALL be documented with rejection reasons |
| TTDR-R6 | Term updates require a new entry with version history |

---

# 5. Registered Terms

See TRANSLATION_TERMINOLOGY_DECISION_PACKAGE_v2.md for the current term registry.

---

**End of Document**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
