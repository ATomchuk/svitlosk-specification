# PROJECT_BASELINE_CLARIFICATION

**Document ID:** PROJ-BL-C1

**Title:** Project Baseline Clarification

**Document Class:** Baseline Clarification

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Clarify the boundary between Phase 1 (Documentation Platform) and Phase 2 (Publishing Platform).

---

# 1. Task A — Review Baseline Logic

## Does TJS-010 belong to Phase 1 or Phase 2?

**TJS-010 belongs to Phase 2 — Telegram Publishing Platform.**

## Architectural Justification

| Dimension | Phase 1 | Phase 2 |
|-----------|---------|---------|
| Mission | Establish the documentation platform | Specify the operational platform |
| Scope | HOW to document | WHAT the system does |
| Specifications | Semantic, Glossary, Editorial, Lifecycle, Graphic | Publishing Model |
| TJS-010 | NOT included | INCLUDED |

**Reasoning:**

Phase 1 (Documentation Platform) establishes the infrastructure for writing specifications:
- Semantic Foundation (TJS-000, TJS-000A)
- Alignment Framework (TJS-000B, TJS-000C, TJS-000D, TJS-TEMPLATE)
- Canonical Specification Standard
- Documentation Architecture

Phase 1 also includes the specifications that describe the documentation architecture itself:
- Editorial System (TJS-020) — describes HOW editorial decisions are made
- Publication Lifecycle (TJS-021) — describes HOW publications evolve
- Graphic Publication Model (TJS-022) — describes HOW graphic publications work

TJS-010 (Publishing Model) describes the OPERATIONAL Publishing Platform — HOW the system actually delivers publications to Telegram. This is Phase 2 work.

---

# 2. Task B — Define Phase Boundary

## Phase 1: Telegram Documentation Platform

| Dimension | Definition |
|-----------|-----------|
| Scope | Documentation infrastructure + documentation specifications |
| Completion criteria | All canonical specifications for the DOCUMENTATION platform are complete |
| Deliverables | Semantic Foundation, Glossary, Alignment Framework, Editorial System, Publication Lifecycle, Graphic Publication Model, Canonical Specification Standard, Documentation Architecture |
| Architecture status | FROZEN |
| Canonical specifications | TJS-000, TJS-000A, TJS-020, TJS-021, TJS-022 |

## Phase 2: Telegram Publishing Platform

| Dimension | Definition |
|-----------|-----------|
| Mission | Specify the operational Publishing Platform |
| Entry point | TJS-010 — TELEGRAM_PUBLISHING_CANONICAL_MODEL.md |
| First canonical specification | TJS-010 — TELEGRAM_PUBLISHING_MODEL.md |
| Expected deliverables | Publishing Model, Channel Management, Rendering Rules, all operational specifications |

---

# 3. Task C — Canonical Specification Register

## Phase 1 Canonical Specifications (5)

| Document ID | Filename | Status | Purpose |
|------------|----------|--------|---------|
| TJS-000 | TELEGRAM_SEMANTIC_MODEL.md | COMPLETE | Semantic foundation |
| TJS-000A | TELEGRAM_GLOSSARY.md | COMPLETE | Canonical terminology |
| TJS-020 | TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md | COMPLETE | Editorial system |
| TJS-021 | TELEGRAM_PUBLICATION_LIFECYCLE.md | COMPLETE | Publication lifecycle |
| TJS-022 | TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md | COMPLETE | Graphic publication model |

**Phase 1 completion: 5/5 — COMPLETE**

## Phase 2 Canonical Specifications (Future)

| Document ID | Filename | Status | Purpose |
|------------|----------|--------|---------|
| TJS-010 | TELEGRAM_PUBLISHING_MODEL.md | PENDING | Publishing platform |
| Future | Channel Management | PENDING | Telegram channel |
| Future | Rendering Rules | TJS-006 | Text rendering |
| Future | Graphic Rendering | Future | Graphic rendering |

**Phase 2 status: NOT STARTED**

---

# 4. Architectural Clarification

**"5/5" is architecturally correct for Phase 1.**

TJS-010 is intentionally excluded from the Phase 1 completion count because it specifies the operational Publishing Platform rather than the Documentation Platform.

Phase 1 = Documentation Platform = the infrastructure + specifications needed to DOCUMENT the system.
Phase 2 = Publishing Platform = the specifications that DESCRIBE how the system actually works.

---

**End of Baseline Clarification**

**Clarifier:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
