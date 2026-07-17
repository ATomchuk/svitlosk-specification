# Telegram Term Approval Register

**Date:** 2026-07-13
**Purpose:** Official semantic decision for every Telegram concept
**Status:** APPROVED — semantic language frozen

---

# Approval Authority

This document constitutes the official semantic approval for all Telegram terminology. Every term receives ONE final status. No further semantic decisions are required before glossary creation.

---

# Approval Register

## Core Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 1 | Journal | Журнал | APPROVED | Core | TJS-000 | — | — | Core semantic concept. Defined in TJS-000 §4. | TJS-000 §4, TJS-001 |
| 2 | Issue | Випуск журналу | APPROVED | Core | TJS-000 | — | — | Core semantic concept. Defined in TJS-000 §4. | TJS-000 §4 |
| 3 | Publication | Публікація | APPROVED | Core | TJS-000 | — | — | Core semantic concept. Defined in TJS-000 §4. | TJS-000 §4, all TJS |
| 4 | Telegram | Телеграм | APPROVED | Core | TJS-000 | — | — | Core semantic concept. Defined in TJS-000 §4. | TJS-000 §4, all TJS |
| 5 | Publication Engine | Публікаційний движок | APPROVED | Core | TJS-000 | — | — | Architectural Component. Defined in GLOSSARY.md. | TJS-001 §10, GLOSSARY |
| 6 | Publisher | Видавець | APPROVED | Core | TJS-000 | — | — | Logical Role. Defined in GLOSSARY.md. | GLOSSARY, TJS-005 |
| 7 | Parser | Парсер | APPROVED | Core | GLOSSARY | — | — | Architectural Component. Defined in GLOSSARY.md. | GLOSSARY, TJS-007 |
| 8 | SvitloSk | СвітлоСк | APPROVED | Core | TJS-001 | — | — | Project name. Used consistently. | TJS-001 §1 |

---

## Lifecycle Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 9 | Publication Lifecycle | Життєвий цикл публікації | APPROVED | Lifecycle | TJS-005 | — | — | Complete lifecycle concept. Will be unified in TJS-005. | TJS-002 §1, TJS-007 §1, TJS-008 §1 |
| 10 | Lifecycle State | Стан життєвого циклу | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | One of the states a publication passes through. | TJS-002 §3, TJS-007 §3 |
| 11 | Generated | Згенеровано | APPROVED | Lifecycle | TJS-005 | Lifecycle State | — | State: publication created. | TJS-002 §3 |
| 12 | Published | Опубліковано | APPROVED | Lifecycle | TJS-005 | Lifecycle State | — | State: publication live. | TJS-002 §3 |
| 13 | Updated | Оновлено | APPROVED | Lifecycle | TJS-005 | Lifecycle State | — | State: publication modified. | TJS-002 §3 |
| 14 | Archived | Архівовано | APPROVED | Lifecycle | TJS-005 | Lifecycle State | — | State: publication preserved. | TJS-002 §3 |
| 15 | Removed | Видалено | APPROVED | Lifecycle | TJS-005 | Lifecycle State | — | State: publication deleted (temporary only). | TJS-002 §3 |
| 16 | Temporary Publication | Тимчасова публікація | APPROVED | Lifecycle | TJS-005 | Publication | — | Publication that may be removed. | TJS-002 §7, TJS-007 §8 |
| 17 | Permanent Publication | Постійна публікація | APPROVED | Lifecycle | TJS-005 | Publication | — | Publication that remains forever. | TJS-007 §9 |
| 18 | Update Rules | Правила оновлення | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | When publications may be edited. | TJS-002 §8, TJS-007 §5 |
| 19 | Archive Policy | Політика архівування | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Rules for preserving historical publications. | TJS-002 §9 |
| 20 | Deletion Policy | Політика видалення | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Rules for removing publications. | TJS-002 §10 |
| 21 | Publication Ownership | Власність публікації | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Who owns what publications. | TJS-007 §10 |
| 22 | Non-destructive Channel Principle | Принцип недеструктивного каналу | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Don't modify others' content. | TJS-007 §11 |
| 23 | Non-destructive Update Principle | Принцип недеструктивного оновлення | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Update in place, don't recreate. | TJS-008 §10 |
| 24 | Publication Session | Сесія публікації | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | One execution producing one complete state. | TJS-008 §15 |
| 25 | Daily Publication Cycle | Щоденний цикл публікацій | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Daily operational cycle. | TJS-008 §3 |
| 26 | Publication Windows | Вікна публікацій | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Time windows for operations. | TJS-008 §6 |
| 27 | Traceability | Простежуваність | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Source dataset, timestamp, generator version. | TJS-002 §11 |
| 28 | Reliability | Надійність | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | No duplicates, order preserved, correct targeting. | TJS-002 §12 |
| 29 | Canonical Equality | Канонічна рівність | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Byte-for-byte identical comparison. | TJS-007 §6 |
| 30 | Error Handling | Обробка помилок | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | Failure recovery rules. | TJS-007 §13 |
| 31 | Archive | Архів | APPROVED | Lifecycle | TJS-005 | Publication Lifecycle | — | State of preserved historical publications. | TJS-002 §9 |

---

## Template Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 32 | Publication Structure | Структура публікації | APPROVED | Template | TJS-003 | — | — | Structural format of publications. | TJS-003 §3 |
| 33 | Publication Grammar | Граматика публікації | APPROVED | Template | TJS-003 | — | — | Hierarchical structure rules. | TJS-005 §4 |
| 34 | Canonical Templates | Канонічні шаблони | APPROVED | Template | TJS-003 | — | — | Definitive publication templates. | TJS-005 §13 |
| 35 | Territory Header | Заголовок території | APPROVED | Template | TJS-003 | — | — | Beginning of publication (uppercase territory name). | TJS-005 §5 |
| 36 | Publication Sections | Розділи публікації | APPROVED | Template | TJS-003 | — | — | Planned Outages, Emergency Outages. | TJS-005 §6 |
| 37 | Validation Rules | Правила валідації | APPROVED | Template | TJS-003 | — | — | Prohibitions list for publications. | TJS-005 §14 |

---

## Formatting Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 38 | Formatting Rules | Правила форматування | APPROVED | Formatting | TJS-004 + TJS-005 | — | — | Rules for text presentation. Policy (TJS-004) + Implementation (TJS-005). | TJS-004 §11, TJS-005 §15 |
| 39 | Editorial Policy | Редакційна політика | APPROVED | Formatting | TJS-004 | — | — | Editorial standards for all text publications. | TJS-004 §1 |
| 40 | Editorial Principles | Редакційні принципи | APPROVED | Formatting | TJS-004 | — | — | Territory-first, One post — one territory, etc. | TJS-004 §2 |
| 41 | Territory Presentation | Представлення території | APPROVED | Formatting | TJS-004 | — | — | How territories are displayed. | TJS-004 §3 |
| 42 | Message Categories | Категорії повідомлень | APPROVED | Formatting | TJS-004 | — | — | Planned outages, Emergency outages. | TJS-004 §5 |
| 43 | Time Format | Формат часу | APPROVED | Formatting | TJS-004 | — | — | How time is displayed. | TJS-004 §8 |
| 44 | Settlement Formatting | Форматування населених пунктів | APPROVED | Formatting | TJS-004 | — | — | How settlements are displayed. | TJS-004 §9 |
| 45 | Address Formatting | Форматування адрес | APPROVED | Formatting | TJS-004 | — | — | How addresses are displayed. | TJS-004 §10 |
| 46 | Branding | Брендинг | APPROVED | Formatting | TJS-004 | — | — | No signatures, no separators, no icons. | TJS-004 §13 |
| 47 | Editing Rules | Правила редагування | APPROVED | Formatting | TJS-003 | — | — | Post-publication corrections permitted. | TJS-003 §10 |
| 48 | Formatting | Форматування | APPROVED | Formatting | TJS-004 | — | — | Rules for text presentation. | TJS-004 §11 |

---

## Rendering Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 49 | Rendering Pipeline | Конвеєр рендерингу | APPROVED | Rendering | TJS-004 | — | — | Sequence: Validation→Sorting→Grouping→Duplicate Removal→Formatting→HTML Escaping→Length Validation→Telegram HTML. | TJS-006 §4 |
| 50 | Rendering | Рендеринг | APPROVED | Rendering | TJS-004 | — | — | The process of converting data into publications. | GLOSSARY |
| 51 | Deterministic Rendering | Детермінований рендеринг | APPROVED | Rendering | TJS-004 | Rendering | — | Same input = same output. | TJS-006 §3 |
| 52 | Stable Ordering | Стабільне сортування | APPROVED | Rendering | TJS-004 | Rendering | — | Deterministic element ordering. | TJS-006 §3 |
| 53 | Source Fidelity | Вірність джерелу | APPROVED | Rendering | TJS-004 | Rendering | — | No reinterpretation of data. | TJS-006 §3 |
| 54 | Territory Ordering | Сортування територій | APPROVED | Rendering | TJS-004 | Rendering | — | Administrative Centre first, then Starosta Districts. | TJS-006 §5 |
| 55 | Time Ordering | Сортування часу | APPROVED | Rendering | TJS-004 | Rendering | — | Sorted by start time. | TJS-006 §6 |
| 56 | Settlement Ordering | Сортування населених пунктів | APPROVED | Rendering | TJS-004 | Rendering | — | Alphabetical using Ukrainian alphabet. NOTE: conflicts with TJS-005 §7 — requires ADR. | TJS-006 §7 |
| 57 | Street Ordering | Сортування вулиць | APPROVED | Rendering | TJS-004 | Rendering | — | Natural Sort. | TJS-006 §8 |
| 58 | Duplicate Removal | Видалення дублікатів | APPROVED | Rendering | TJS-004 | Rendering | — | No duplicate addresses. | TJS-006 §9 |
| 59 | Long Publication Split | Розбиття довгої публікації | APPROVED | Rendering | TJS-004 | Rendering | — | Split between complete Settlement blocks. | TJS-006 §10 |
| 60 | HTML Rendering Rules | Правила HTML рендерингу | APPROVED | Rendering | TJS-004 | Rendering | — | Allowed tags: `<b>`, `<br>`. | TJS-006 §11 |
| 61 | Stable Output Rule | Правило стабільного виводу | APPROVED | Rendering | TJS-004 | Rendering | — | No cosmetic changes. | TJS-006 §12 |
| 62 | Empty Block Rule | Правило порожнього блоку | APPROVED | Rendering | TJS-004 | Rendering | — | No empty sections. | TJS-006 §13 |
| 63 | Rendering Rules | Правила рендерингу | APPROVED | Rendering | TJS-004 | — | — | The canonical rendering pipeline and rules. | TJS-006 §1 |

---

## Platform Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 64 | Channel | Канал | APPROVED | Platform | TJS-000 | — | — | Communication medium. | TJS-000 §5 |
| 65 | Telegram Message ID | Ідентифікатор повідомлення Telegram | APPROVED | Platform | TJS-005 | — | — | Identifier for published message. | TJS-007 §10 |
| 66 | Telegram Bot API | Telegram Bot API | APPROVED | Platform | TJS-006 (new) | — | — | Telegram Bot interface. | TJS-006 (proposed) |
| 67 | Rate Limiting | Обмеження частоти | APPROVED | Platform | TJS-006 (new) | — | — | Telegram API limits. | TJS-006 (proposed) |
| 68 | Message Editing | Редагування повідомлень | APPROVED | Platform | TJS-006 (new) | — | — | Telegram-specific editing. | TJS-006 (proposed) |
| 69 | Channel Administration | Адміністрування каналу | APPROVED | Platform | TJS-006 (new) | — | — | Admin interaction with channel. | TJS-006 (proposed) |
| 70 | subscribers | підписники | APPROVED | Platform | TJS-001 | — | — | End consumers. | TJS-001 §10 |
| 71 | administrators | адміністратори | APPROVED | Platform | TJS-005 | — | — | Channel administrators. | TJS-007 §11 |
| 72 | Manual Publications | Ручні публікації | APPROVED | Platform | TJS-005 | — | — | Non-automated publications. | TJS-008 §13 |
| 73 | Image Publications | Зображення публікацій | APPROVED | Platform | TJS-005 | — | — | Visual publications. | TJS-008 §14 |
| 74 | Telegram Publisher | Telegram Видавець | APPROVED | Platform | TJS-006 (new) | Publisher | — | Telegram-specific implementation of Publisher Role. | TJS-006 (proposed) |

---

## Administrative Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 75 | Settlement | Населений пункт | APPROVED | Administrative | GLOSSARY | — | — | Populated place within a territory. | GLOSSARY |
| 76 | Starosta District | Старостинський округ | APPROVED | Administrative | GLOSSARY | — | — | Territorial subdivision. | GLOSSARY |
| 77 | Community | Територіальна громада | APPROVED | Administrative | GLOSSARY | — | — | Primary territorial scope. | GLOSSARY |
| 78 | Administrative Centre | Адміністративний центр | APPROVED | Administrative | GLOSSARY | — | — | Principal territorial unit. | GLOSSARY |
| 79 | Territory | Територія | APPROVED | Administrative | GLOSSARY | — | — | Publication unit (Centre or District). | GLOSSARY |
| 80 | Street | Вулиця | APPROVED | Administrative | GLOSSARY | — | — | Road name in address. | GLOSSARY |
| 81 | Address | Адреса | APPROVED | Administrative | GLOSSARY | — | — | Physical location. | GLOSSARY |
| 82 | Time Interval | Часовий інтервал | APPROVED | Administrative | TJS-003 | — | — | Duration of outage. | TJS-005 §8 |

---

## Derived Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 83 | Text Publication | Текстова публікація | DERIVED | Derived | — | Publication | — | Publication containing text only. | Implicit |
| 84 | Graphic Publication | Графічна публікація | DERIVED | Derived | — | Publication | — | Publication containing graphics. | Implicit |
| 85 | City Today | Місто сьогодні | DERIVED | Derived | TJS-003 | Publication | — | Template A type. | TJS-005 §13 |
| 86 | District Today | Округ сьогодні | DERIVED | Derived | TJS-003 | Publication | — | Template B type. | TJS-005 §13 |
| 87 | City Tomorrow | Місто завтра | DERIVED | Derived | TJS-003 | Publication | — | Template C type. | TJS-005 §13 |
| 88 | District Tomorrow | Округ завтра | DERIVED | Derived | TJS-003 | Publication | — | Template D type. | TJS-005 §13 |
| 89 | Today's Package | Пакет сьогодні | DERIVED | Derived | TJS-005 | Publication Package | — | All today's publications. | TJS-008 §4 |
| 90 | Tomorrow Package | Пакет завтра | DERIVED | Derived | TJS-005 | Publication Package | — | All tomorrow's publications. | TJS-008 §5 |
| 91 | Publication Package | Пакет публікацій | DERIVED | Derived | TJS-004 | — | — | Collection of publications for a territory. | TJS-004 §4 |

---

## Architectural Concepts

| # | English | Ukrainian | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|-----------|--------|----------|-------|--------|-------------|--------|-----------|
| 92 | SSOT | Єдине джерело правди | ARCHITECTURAL | Architectural | GLOSSARY | — | — | One authoritative definition per concept. Repository governance term. | GLOSSARY |
| 93 | SRP | Принцип єдиної відповідальності | ARCHITECTURAL | Architectural | PROJECT_PRINCIPLES | — | — | One responsibility per document. Engineering principle. | PROJECT_PRINCIPLES |
| 94 | Separation of Concerns | Розділення відповідальності | ARCHITECTURAL | Architectural | ARCHITECTURE | — | — | Policy vs Implementation separation. Engineering principle. | ARCHITECTURE |
| 95 | Semantic Ownership Principle | Принцип семантичної власності | ARCHITECTURAL | Architectural | TJS-000 | — | — | TJS-000 is single semantic authority. Governance rule. | TJS-000 §6 |
| 96 | One Document — One Subject | Один документ — одна тема | ARCHITECTURAL | Architectural | PROJECT_PRINCIPLES | — | — | Each document defines one subject. Engineering principle. | PROJECT_PRINCIPLES P-10 |
| 97 | Dependency Direction | Напрямок залежностей | ARCHITECTURAL | Architectural | ARCHITECTURE | — | — | Dependencies flow from TJS-001 downward. Governance rule. | ARCHITECTURE |
| 98 | Metadata Compliance | Відповідність метаданих | ARCHITECTURAL | Architectural | ARCHITECTURE | — | — | Document Class, References, RFC 2119. Governance rule. | ARCHITECTURE |

---

## Forbidden Terms

| # | English | Status | Category | Owner | Parent | Replacement | Reason | Reference |
|---|---------|--------|----------|-------|--------|-------------|--------|-----------|
| 99 | Message | FORBIDDEN | — | — | — | Publication | Hidden synonym for Publication. | TJS-007 §10 |
| 100 | Post | FORBIDDEN | — | — | — | Publication | Social media connotation. | TJS-003 filename |
| 101 | Telegram Message | FORBIDDEN | — | — | — | Publication / Telegram Message ID | Conflates platform and semantic levels. | TJS-007 §10 |
| 102 | Daily Page | FORBIDDEN | — | — | — | Issue / Today's Package | Not used. Web/print connotation. | — |
| 103 | Publication Set | FORBIDDEN | — | — | — | Publication Package | Not used. Mathematical connotation. | — |
| 104 | Feed | FORBIDDEN | — | — | — | Journal | Social media connotation. | — |
| 105 | Page | FORBIDDEN | — | — | — | Publication / Issue | Web/print connotation. | — |
| 106 | Coordinator | FORBIDDEN | — | — | — | — | Not used. Not Telegram concept. | — |
| 107 | Workflow | FORBIDDEN | — | — | — | Daily Publication Cycle | Not used as semantic concept. | — |
| 108 | Working Repository | FORBIDDEN | — | — | — | — | Not Telegram concept. | — |
| 109 | Historical Storage | FORBIDDEN | — | — | — | Archive | Implementation term, not semantic. | — |
| 110 | Journal Finality | FORBIDDEN | — | — | — | — | Not used. Not a semantic concept. | — |
| 111 | Repository | FORBIDDEN | — | — | — | — | Not Telegram concept. | — |
| 112 | History | FORBIDDEN | — | — | — | Archive | Imprecise — use Archive. | — |
| 113 | System Publication | FORBIDDEN | — | — | — | Publication | Redundant qualifier. | — |
| 114 | Starostyn District | FORBIDDEN | — | — | — | Starosta District | Misspelling. | — |

---

# Summary

| Status | Count |
|--------|-------|
| APPROVED | 91 |
| DERIVED | 9 |
| ARCHITECTURAL | 7 |
| FORBIDDEN | 16 |
| **Total Decisions** | **114** |

---

**End of Term Approval Register**

**Approver:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** APPROVED — Semantic language frozen
