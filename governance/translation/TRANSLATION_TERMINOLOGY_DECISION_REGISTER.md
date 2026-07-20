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

# 2. Translation Rendering Model

Every translation term SHALL be defined using four layers.

| Layer | Definition | Mutability |
|-------|-----------|-----------|
| Semantic Layer | The MEANING of the term within SvitloSk | NEVER changes |
| Identifier Layer | The CANONICAL ENGLISH term used in specifications | NEVER changes |
| Rendering Layer | The UKRAINIAN translation of the term for documentation | Changes only through TTDR revision |
| Presentation Layer | The DISPLAYED form in specific contexts | MAY vary only when TTDR explicitly permits |

## Normative Rules

| Rule | Statement |
|------|-----------|
| TRM-R1 | Identifiers SHALL remain English in all contexts |
| TRM-R2 | Semantic meaning SHALL remain invariant across languages |
| TRM-R3 | Approved rendering SHALL be used in Ukrainian translations |
| TRM-R4 | Presentation MAY vary only when TTDR explicitly permits |
| TRM-R5 | Every term entry SHALL specify all four layers |

---

# 3. Terminology Categories

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

# 4. Decision Template

Every approved term SHALL be documented using the following template.

| Field | Description |
|-------|-------------|
| English term | The canonical English term |
| Category | A (Architecture), B (Deterministic), or C (Public Communication) |
| Semantic Layer | What this term means within SvitloSk specifically |
| Identifier Layer | The canonical English identifier |
| Rendering Layer | The approved Ukrainian translation |
| Presentation Layer | The displayed form (same as Rendering unless TTDR permits variation) |
| Rejected alternatives | Other translations that were considered |
| Reason for rejection | Why each alternative was rejected |
| Owner Decision | The owner's final decision |
| Decision Date | Date of owner approval |
| Decision Authority | Name or role of approver |
| Repository Baseline | Baseline version at time of approval |
| Repository Status | Repository status at time of approval |
| Status | APPROVED |

---

# 5. Decision Rules

| Rule | Statement |
|------|-----------|
| TTDR-R1 | Every translation term SHALL belong to exactly one category |
| TTDR-R2 | No term may be used in a translated document without approval in this register |
| TTDR-R3 | Category C terms MAY have context-dependent Presentation Layers |
| TTDR-R4 | Category A and B terms SHALL have identical Rendering and Presentation Layers |
| TTDR-R5 | Rejected alternatives SHALL be documented with rejection reasons |
| TTDR-R6 | Term updates require a new entry with version history |
| TTDR-R7 | Terminology changes require Architecture Decision, TTDR revision, Glossary update, and Owner approval |

---

# 6. Registered Terms — Category A (Architecture)

## Publication Engine

| Field | Value |
|-------|-------|
| English term | Publication Engine |
| Category | A — Architecture Terms |
| Semantic Layer | Architectural Component implementing the Publisher Role. Responsible for generating and distributing Publications. One of 8 primary components. |
| Identifier Layer | Publication Engine |
| Rendering Layer | Движок публікацій |
| Presentation Layer | Движок публікацій |
| Rejected alternatives | Компонент публікацій (too generic), Механізм публікацій (less natural), Система публікацій (too broad) |
| Reason for rejection | Компонент публікацій would make the term generic. Publication Engine is a proper architectural name. |
| Owner Decision | APPROVED |
| Decision Date | 2026-07-13 |
| Decision Authority | Project Owner |
| Repository Baseline | v3.0 |
| Repository Status | Repository Engineering COMPLETE |
| Status | **APPROVED** |

---

# 7. Registered Terms — Category B (Deterministic)

## Canonical Equality

| Field | Value |
|-------|-------|
| English term | Canonical Equality |
| Category | B — Deterministic Terms |
| Semantic Layer | Byte-for-byte identical output from identical input. Two publications generated from identical datasets SHALL be identical. |
| Identifier Layer | Canonical Equality |
| Rendering Layer | Канонічна рівність |
| Presentation Layer | Канонічна рівність |
| Rejected alternatives | Канонічна тотожність (not established, 0 occurrences), Канонічна ідентичність (not established, 0 occurrences) |
| Reason for rejection | Канонічна рівність is already in the Glossary with 35 occurrences. Consistency outweighs marginal semantic improvement. |
| Owner Decision | APPROVED |
| Decision Date | 2026-07-13 |
| Decision Authority | Project Owner |
| Repository Baseline | v3.0 |
| Repository Status | Repository Engineering COMPLETE |
| Status | **APPROVED** |

---

# 8. Registered Terms — Category C (Public Communication)

## Powered

| Field | Value |
|-------|-------|
| English term | Powered |
| Category | C — Public Communication Terms |
| Semantic Layer | NOT currently experiencing an outage. The absence of a scheduled or emergency outage. Normal state. |
| Identifier Layer | Powered |
| Rendering Layer | Без знеструмлення |
| Presentation Layer | Без знеструмлення (universal across all contexts) |
| Rejected alternatives | Норма (too generic), Електропостачання (misleading), Забезпечення (incomplete), Відсутність відключення (awkward) |
| Reason for rejection | "Без знеструмлення" directly matches the project's linguistic model centered on "знеструмлення." Universal across all contexts. |
| Owner Decision | APPROVED |
| Decision Date | 2026-07-13 |
| Decision Authority | Project Owner |
| Repository Baseline | v3.0 |
| Repository Status | Repository Engineering COMPLETE |
| Status | **APPROVED** |

---

# 9. Pre-Approved Terms (LOW Ambiguity — 42 Terms)

The following 42 terms from the Translation Terminology Matrix are pre-approved at LOW ambiguity risk.

## Category A (Architecture)

| # | English | Ukrainian |
|---|---------|-----------|
| 1 | Journal | Журнал |
| 2 | Issue | Випуск журналу |
| 3 | Publication | Публікація |
| 4 | Telegram | Telegram |
| 5 | Graphic Publication | Графічна публікація |
| 6 | Text Publication | Текстова публікація |
| 7 | Temporary Publication | Тимчасова публікація |
| 8 | Permanent Publication | Постійна публікація |
| 9 | Publication Package | Пакет публікацій |
| 10 | Publisher | Видавець |
| 11 | Parser | Парсер |
| 12 | Telegram Publisher | Telegram Видавець |
| 13 | Channel | Канал |
| 14 | Subscribers | Підписники |
| 15 | Administrators | Адміністратори |
| 16 | Publication Identity | Ідентифікатор публікації |
| 17 | Archive | Архів |
| 18 | Repository | Репозиторій |

## Category B (Deterministic)

| # | English | Ukrainian |
|---|---------|-----------|
| 19 | Traceability | Простежуваність |
| 20 | Reliability | Надійність |

## Category C (Public Communication)

| # | English | Ukrainian |
|---|---------|-----------|
| 21 | City Today | Місто сьогодні |
| 22 | District Today | Округ сьогодні |
| 23 | City Tomorrow | Місто завтра |
| 24 | District Tomorrow | Округ завтра |
| 25 | Today's Package | Пакет сьогодні |
| 26 | Tomorrow Package | Пакет завтра |
| 27 | Publication Lifecycle | Життєвий цикл публікації |
| 28 | Lifecycle State | Стан життєвого циклу |
| 29 | Generated | Згенеровано |
| 30 | Published | Опубліковано |
| 31 | Updated | Оновлено |
| 32 | Archived | Заархівовано |
| 33 | Removed | Видалено |
| 34 | Error Handling | Обробка помилок |
| 35 | Territory | Територія |
| 36 | Address | Адреса |
| 37 | Outage | Відключення |
| 38 | Schedule | Розклад |
| 39 | Queue | Черга |
| 40 | Subqueue | Підчерга |
| 41 | Outage Interval | Інтервал відключення |
| 42 | Powered Interval | Інтервал без знеструмлення |

---

# 10. Terminology Registry Summary

| Metric | Value |
|--------|-------|
| Category A (Architecture) | 19 |
| Category B (Deterministic) | 2 |
| Category C (Public Communication) | 23 |
| **Total approved terms** | **45** |

---

# 11. Freeze Status

| Metric | Value |
|--------|-------|
| Terminology frozen | YES |
| Freeze date | 2026-07-13 |
| Freeze baseline | v3.0 |
| Unresolved terms | 0 |
| Future changes require | ADR + TTDR revision + Glossary update + Owner approval |

---

**End of Document**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable — Terminology Frozen
