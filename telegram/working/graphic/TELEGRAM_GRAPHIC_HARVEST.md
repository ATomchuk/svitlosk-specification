# TELEGRAM_GRAPHIC_HARVEST

**Document ID:** TJS-G0-H1

**Title:** Graphic Publication Semantic Harvest

**Document Class:** Semantic Harvest

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

This document presents the complete semantic harvest for the future TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md. Every statement is traceable to existing project knowledge. No new concepts are invented.

---

# 1. Harvest Sources

| # | Document | Graphic Content Found |
|---|----------|----------------------|
| 1 | TELEGRAM_GLOSSARY.md | Graphic Publication (§6), Image Publications (§10), Traceability (§11) |
| 2 | TELEGRAM_CONCEPT_OWNERSHIP_MATRIX.md | 10 Graphic Model concepts assigned |
| 3 | TELEGRAM_DOCUMENT_BOUNDARIES.md | 10 Graphic Model concepts listed |
| 4 | TELEGRAM_SEMANTIC_DEPENDENCY_MAP.md | 10 Graphic Model concepts mapped |
| 5 | TELEGRAM_PUBLISHING_COMPONENT_MATRIX.md | Graphic Generator component |
| 6 | TELEGRAM_PUBLISHING_INTERACTION_MATRIX.md | Publication Engine → Graphic Generator interaction |
| 7 | TELEGRAM_PUBLISHING_RESPONSIBILITY_MATRIX.md | Graphic rendering responsibility |
| 8 | TELEGRAM_PUBLISHING_HARVEST.md | Graphic Publication as Publication type |
| 9 | TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | Graphic Generator in component lists |
| 10 | TELEGRAM_PUBLISHING_PRINCIPLES.md | P-015 Visual Stability, P-016 Deterministic Rendering, P-017 Source Fidelity |
| 11 | TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md | Excludes Graphic responsibilities (§7.2) |
| 12 | TELEGRAM_EDITORIAL_HARVEST.md | Visually consistent, visually stable |
| 13 | TELEGRAM_PUBLICATION_LIFECYCLE.md | Excludes Graphic rules (§2, §11.2, §14) |
| 14 | SSP-007 (Graphic Generator) | Complete implementation specification |
| 15 | SSP-006 (Schedule Generator) | Schedule data consumed by Graphic Generator |
| 16 | TJS-003-Post-Structure.md | §6 Graphic Block |
| 17 | TJS-008-Publication-Lifecycle.md | §14 Image Publications |
| 18 | TELEGRAM_LEGACY_SPECIFICATION_REVIEW.md | Graphic block (TJS-003 §6), Image publications (TJS-008 §14) |

---

# 2. Task A — Graphic Statements Harvested

## 2.1 From TELEGRAM_GLOSSARY.md

| Statement | Source | Type |
|-----------|--------|------|
| Graphic Publication IS A Publication | §6 | RELATIONSHIP |
| Graphic Publication is a Publication containing graphics | §6 | DEFINITION |
| Text Publication IS A Publication — as opposed to Image Publications | §6 | RELATIONSHIP |
| Image Publications are visual publications published manually, outside the automatic lifecycle | §10 | DEFINITION |
| Traceability includes "generated graphic" as part of origin identification | §11 | DEFINITION |

## 2.2 From TELEGRAM_CONCEPT_OWNERSHIP_MATRIX.md

| Concept | Owner | 10 concepts assigned to Graphic Model |
|---------|-------|---------------------------------------|
| Graphic Publication | Graphic Model | OWNED |
| Graphic Builder | Graphic Model | OWNED |
| Graphic Rendering | Graphic Model | OWNED |
| Graphic Template | Graphic Model | OWNED |
| Graphic Synchronization | Graphic Model | OWNED |
| Graphic Update | Graphic Model | OWNED |
| Graphic Publication Rules | Graphic Model | OWNED |
| JSON Graphic Source | Graphic Model | OWNED |
| SVG/PNG Generation | Graphic Model | OWNED |
| Graphic-specific Constraints | Graphic Model | OWNED |

## 2.3 From SSP-007 (Graphic Generator)

| Statement | Section | Type |
|-----------|---------|------|
| Graphic Generator produces visual materials based on normalized outage schedules | §1 | DEFINITION |
| Graphics SHALL be clear, minimalistic, readable, accessible, deterministic, brand consistent | §3 | PRINCIPLE |
| Same input SHALL always produce identical output | §3 | PRINCIPLE |
| Every generated graphic SHALL contain official SvitloSk branding | §4 | RULE |
| Mandatory branding: logo, project name, publication date, generation timestamp | §4 | RULE |
| Supported formats: PNG, SVG | §5 | CONSTRAINT |
| Graphic types: Tomorrow Schedule, Emergency Card, Information Card, Statistics Card | §6 | DEFINITION |
| Timeline represents 00:00–24:00, states: Powered/Outage | §7 | RULE |
| Intervals SHALL always be proportional to time | §7 | RULE |
| Colors SHALL always represent state | §8 | RULE |
| Powered = Orange, Outage = Dark Gray | §8 | RULE |
| No additional semantic colors SHALL NOT be introduced | §8 | CONSTRAINT |
| Graphics SHALL be optimized for Telegram, Mobile, Desktop | §9 | CONSTRAINT |
| Graphics SHALL be generated without manual editing | §10 | RULE |
| Generation SHALL be triggered automatically after successful schedule generation | §10 | RULE |
| Before publication every generated graphic SHALL be validated | §11 | RULE |
| Invalid graphics SHALL never be published | §11 | RULE |
| Graphics SHALL remain readable on light/dark displays, small mobile screens | §12 | PRINCIPLE |
| Future: animated graphics, interactive SVG, multi-language, regional themes | §13 | INFORMATIVE |

## 2.4 From TJS-003-Post-Structure.md

| Statement | Section | Type |
|-----------|---------|------|
| Publication structure includes Graphic block (optional) | §3 | DEFINITION |
| Graphic shall match the published information | §6 | RULE |
| Graphic shall follow the official SvitloSk visual identity | §6 | RULE |
| Graphic shall be generated automatically | §6 | RULE |

## 2.5 From TJS-008-Publication-Lifecycle.md

| Statement | Section | Type |
|-----------|---------|------|
| Journal SHALL remain visually stable throughout the reporting day | §8 | PRINCIPLE |
| Image Publications published manually SHALL remain outside the automatic lifecycle | §14 | RULE |
| Image Publications include: outage charts, schedule graphics, announcements, promotional graphics | §14 | DEFINITION |
| Publication Engine SHALL NOT modify or remove Image Publications | §14 | CONSTRAINT |

## 2.6 From TELEGRAM_PUBLISHING_PRINCIPLES.md

| Statement | Principle | Type |
|-----------|-----------|------|
| Journal SHALL remain visually stable throughout the reporting day | P-015 | PRINCIPLE |
| Deterministic Rendering — same input produces identical output | P-016 | PRINCIPLE |
| Rendering SHALL NOT modify or reinterpret official information | P-017 | PRINCIPLE |

## 2.7 From TELEGRAM_PUBLISHING_COMPONENT_MATRIX.md

| Statement | Component | Type |
|-----------|-----------|------|
| Graphic Generator produces visual materials based on normalized outage schedules | Component | DEFINITION |
| Graphic Generator input: Parser (normalized data), SSP-003 | Data Flow | RELATIONSHIP |
| Graphic Generator output: Data → Graphic → Publication | Data Flow | RELATIONSHIP |
| Graphic Generator class: Architectural Component | Classification | DEFINITION |

## 2.8 From TELEGRAM_PUBLISHING_INTERACTION_MATRIX.md

| Statement | Interaction | Type |
|-----------|------------|------|
| Publication Engine → Graphic Generator: Graphic Request | Interaction | RELATIONSHIP |
| Administrators → Telegram Channel: Image Publication | Interaction | RELATIONSHIP |
| Publication Engine → Image Publications: ILLEGAL | Constraint | CONSTRAINT |
| Engine SHALL NOT modify image publications | Constraint | CONSTRAINT |

## 2.9 From TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

| Statement | Section | Type |
|-----------|---------|------|
| Editorial System SHALL NOT duplicate Graphic Publication responsibilities | §7.2 | CONSTRAINT |
| Graphic publication rules owned by TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md | §7.2 | OWNERSHIP |
| Journal SHALL remain visually stable throughout the reporting day | §9 | PRINCIPLE |
| Every publication SHALL be visually consistent | §9 | PRINCIPLE |

## 2.10 From TELEGRAM_PUBLICATION_LIFECYCLE.md

| Statement | Section | Type |
|-----------|---------|------|
| Graphic publication rules owned by TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md | §2, §11.2, §14 | OWNERSHIP |
| Journal SHALL remain visually stable throughout the reporting day | §9 | PRINCIPLE |

---

# 3. Task B — Semantic Concepts Harvested

| # | Concept | Ukrainian | Source | Status |
|---|---------|-----------|--------|--------|
| 1 | Graphic Publication | Графічна публікація | TG §6 | EXISTS |
| 2 | Graphic Builder | Графічний конструктор | Concept Ownership Matrix | EXISTS |
| 3 | Graphic Rendering | Графічне відображення | Concept Ownership Matrix | EXISTS |
| 4 | Graphic Template | Графічний шаблон | Concept Ownership Matrix | EXISTS |
| 5 | Graphic Synchronization | Графічна синхронізація | Concept Ownership Matrix | EXISTS |
| 6 | Graphic Update | Графічне оновлення | Concept Ownership Matrix | EXISTS |
| 7 | Graphic Publication Rules | Правила графічних публікацій | Concept Ownership Matrix | EXISTS |
| 8 | JSON Graphic Source | JSON-джерело графіки | Concept Ownership Matrix | EXISTS |
| 9 | SVG/PNG Generation | Генерація SVG/PNG | Concept Ownership Matrix | EXISTS |
| 10 | Graphic-specific Constraints | Специфічні обмеження графіки | Concept Ownership Matrix | EXISTS |
| 11 | Image Publications | Зображення публікацій | TG §10 | EXISTS |
| 12 | Graphic Generator | Графічний генератор | SSP-007, Component Matrix | EXISTS |
| 13 | Graphic Request | Графічний запит | Interaction Matrix | EXISTS |
| 14 | Tomorrow Schedule | Розклад завтра | SSP-007 §6 | EXISTS |
| 15 | Emergency Card | Картка термінова | SSP-007 §6 | EXISTS |
| 16 | Information Card | Інформаційна картка | SSP-007 §6 | EXISTS |
| 17 | Statistics Card | Картка статистики | SSP-007 §6 | EXISTS |
| 18 | Timeline Representation | Представлення таймлайну | SSP-007 §7 | EXISTS |
| 19 | Graphic Branding | Брендування графіки | SSP-007 §4 | EXISTS |
| 20 | Graphic Validation | Валідація графіки | SSP-007 §11 | EXISTS |
| 21 | Visual Identity | Візуальна ідентичність | TJS-003 §6, §8 | EXISTS |
| 22 | Visual Stability | Візуальна стабільність | TJS-008 §8, P-015 | EXISTS |
| 23 | Visual Consistency | Візуальна послідовність | Editorial §9 | EXISTS |

**Total concepts harvested: 23** (all exist in project knowledge)

---

# 4. Task C — Responsibilities Harvested

| # | Responsibility | Owner | Source |
|---|---------------|-------|--------|
| 1 | Create graphics | Graphic Generator | SSP-007 §10 |
| 2 | Update graphics | Graphic Generator | Concept Ownership Matrix |
| 3 | Replace graphics | Graphic Generator | Concept Ownership Matrix |
| 4 | Archive graphics | Graphic Generator | Concept Ownership Matrix |
| 5 | Validate graphics | Graphic Generator | SSP-007 §11 |
| 6 | Brand graphics | Graphic Generator | SSP-007 §4 |
| 7 | Render graphics | Graphic Generator | SSP-007 §8 |
| 8 | Synchronize graphics | Graphic Generator | Concept Ownership Matrix |
| 9 | Ensure visual stability | Publishing System | P-015, Lifecycle §9 |
| 10 | Ensure visual consistency | Editorial System | Editorial §9 |
| 11 | NOT make editorial decisions | Graphic Generator | Boundary analysis |
| 12 | NOT own lifecycle | Graphic Generator | Boundary analysis |
| 13 | NOT modify source data | Graphic Generator | SSP-007 §10 |
| 14 | NOT become source of truth | Graphic Generator | Repository Authority §3.1 |
| 15 | NOT modify Image Publications | Publication Engine | TJS-008 §14 |

---

# 5. Task D — Architectural Principles Harvested

| # | Principle | Source | Type |
|---|-----------|--------|------|
| 1 | Graphics SHALL be clear, minimalistic, readable, accessible, deterministic, brand consistent | SSP-007 §3 | Design principle |
| 2 | Same input SHALL always produce identical output | SSP-007 §3 | Deterministic principle |
| 3 | Graphics SHALL be generated without manual editing | SSP-007 §10 | Automation principle |
| 4 | Generation SHALL be triggered automatically after schedule generation | SSP-007 §10 | Automation principle |
| 5 | Colors SHALL always represent state | SSP-007 §8 | Visual rule |
| 6 | No additional semantic colors SHALL NOT be introduced | SSP-007 §8 | Visual constraint |
| 7 | Intervals SHALL always be proportional to time | SSP-007 §7 | Visual rule |
| 8 | Graphics SHALL remain readable on light/dark displays, small screens | SSP-007 §12 | Accessibility principle |
| 9 | Journal SHALL remain visually stable throughout the reporting day | P-015, TJS-008 §8 | Stability principle |
| 10 | Rendering SHALL NOT modify or reinterpret official information | P-017 | Source fidelity |
| 11 | Deterministic Rendering — same input produces identical output | P-016 | Deterministic principle |

---

# 6. Task E — Architectural Constraints Harvested

| # | Constraint | Source | Type |
|---|-----------|--------|------|
| 1 | Graphics never modify source data | SSP-007 §10 | Constraint |
| 2 | Graphics never become source of truth | Repository Authority §3.1 | Constraint |
| 3 | Graphics always derived from Repository | Repository Authority §3.1 | Constraint |
| 4 | Graphics represent Journal state | Lifecycle §9 | Constraint |
| 5 | Graphics remain deterministic | SSP-007 §3, P-016 | Constraint |
| 6 | Supported formats: PNG, SVG only | SSP-007 §5 | Constraint |
| 7 | Every graphic SHALL contain branding | SSP-007 §4 | Constraint |
| 8 | Invalid graphics SHALL never be published | SSP-007 §11 | Constraint |
| 9 | Graphics SHALL NOT be animated (current) | SSP-007 §13 | Constraint |
| 10 | Graphics SHALL NOT be multi-language (current) | SSP-007 §13 | Constraint |
| 11 | Engine SHALL NOT modify Image Publications | TJS-008 §14 | Constraint |
| 12 | Image Publications remain outside automatic lifecycle | TJS-008 §14 | Constraint |

---

# 7. Task F — Boundaries Harvested

## 7.1 What Graphic Publication Owns

- Graphic Publication definition
- Graphic Builder responsibility
- Graphic Rendering rules
- Graphic Template definition
- Graphic Synchronization rules
- Graphic Update rules
- Graphic Publication Rules
- JSON Graphic Source format
- SVG/PNG Generation rules
- Graphic-specific Constraints
- Graphic Validation rules
- Graphic Branding rules
- Graphic Accessibility rules
- Graphic Timeline rules
- Graphic Color rules
- Graphic Layout rules

## 7.2 What Graphic Publication Does NOT Own

- Editorial decisions (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md)
- Publication Lifecycle (TELEGRAM_PUBLICATION_LIFECYCLE.md)
- Publishing Engine (TELEGRAM_PUBLISHING_MODEL.md)
- Telegram API
- Rendering algorithms (TJS-006)
- Source data authority (Repository Authority §3.1)
- Publication state (Lifecycle Model)
- Issue state (Lifecycle Model)
- Semantic terminology (Glossary)
- Image Publications (admin-managed, outside lifecycle)

---

# 8. Task G — Interactions Harvested

| # | From | To | Interaction | Source |
|---|------|----|-------------|--------|
| 1 | Publication Engine | Graphic Generator | Graphic Request | Interaction Matrix |
| 2 | Schedule Generator | Graphic Generator | Schedule Data | SSP-006 §6 |
| 3 | Graphic Generator | Publication Engine | Generated Graphic | Component Matrix |
| 4 | Graphic Generator | Telegram Channel | Image Publication (via Engine) | Interaction Matrix |
| 5 | Administrators | Telegram Channel | Image Publication (manual) | Interaction Matrix |
| 6 | Repository | Graphic Generator | Normalized Data | Repository Authority §3.1 |
| 7 | Graphic Generator | Archive | Archived Graphics | Lifecycle §9 |

---

# 9. Task H — Duplication Risks

| # | Risk | Documents Involved | Severity | Mitigation |
|---|------|-------------------|----------|------------|
| 1 | Visual Stability overlapping | P-015, Lifecycle §9, Editorial §9 | MEDIUM | Each owns different dimension: Publishing owns stability, Lifecycle guarantees it, Editorial ensures consistency |
| 2 | Graphic Generator ownership | SSP-007 (implementation), Graphic Model (semantic) | MEDIUM | SSP-007 = implementation spec; Graphic Model = semantic architecture. Different document classes. |
| 3 | Image Publications scope | TJS-008 §14 (lifecycle exclusion), Graphic Model (graphic scope) | LOW | Image Publications are admin-managed, outside lifecycle. Graphic Model governs automated graphics only. |
| 4 | Rendering overlap | TJS-006 (rendering rules), Graphic Model (graphic rendering) | LOW | TJS-006 owns text rendering; Graphic Model owns graphic rendering. Different domains. |
| 5 | Visual consistency | Editorial §9 (editorial consistency), Graphic Model (graphic consistency) | LOW | Editorial ensures editorial consistency; Graphic Model ensures graphic consistency. Different layers. |

---

**End of Semantic Harvest**

**Harvester:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
