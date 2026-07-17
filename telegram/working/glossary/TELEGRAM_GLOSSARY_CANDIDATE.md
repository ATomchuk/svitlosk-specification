# Telegram Glossary Candidate

**Date:** 2026-07-13
**Purpose:** Candidate glossary for future TELEGRAM_GLOSSARY.md
**Status:** CANDIDATE — NOT YET APPROVED

---

# Important Notice

This is NOT the final glossary. This is a candidate document prepared during Stage G-0 (Terminology Harvest). The final TELEGRAM_GLOSSARY.md will be created in a future stage.

---

## Core Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 1 | Journal | Журнал | Continuous informational publication of SvitloSk | TJS-000 | Core | Candidate |
| 2 | Issue | Випуск журналу | One editorial edition for a single calendar day | TJS-000 | Core | Candidate |
| 3 | Publication | Публікація | One independent publication belonging to an Issue | TJS-000 | Core | Candidate |
| 4 | Telegram | Телеграм | Primary publication channel | TJS-000 | Core | Candidate |
| 5 | Publication Engine | Публікаційний движок | Component implementing Publisher Role | TJS-000 | Core | Candidate |
| 6 | Publisher | Видавець | Logical role for creating/distributing publications | TJS-000 | Core | Candidate |
| 7 | Parser | Парсер | Component retrieving Open Data | GLOSSARY | Core | Candidate |
| 8 | SvitloSk | СвітлоСк | Project name | TJS-001 | Core | Candidate |

---

## Lifecycle Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 9 | Publication Lifecycle | Життєвий цикл публікації | Complete lifecycle from creation to archival | TJS-005 | Lifecycle | Candidate |
| 10 | Lifecycle State Model | Модель станів життєвого циклу | States a publication passes through | TJS-005 | Lifecycle | Candidate |
| 11 | Generated | Згенеровано | State: publication created | TJS-005 | Lifecycle | Candidate |
| 12 | Published | Опубліковано | State: publication live | TJS-005 | Lifecycle | Candidate |
| 13 | Updated | Оновлено | State: publication modified | TJS-005 | Lifecycle | Candidate |
| 14 | Archived | Архівовано | State: publication preserved | TJS-005 | Lifecycle | Candidate |
| 15 | Removed | Видалено | State: publication deleted (temporary only) | TJS-005 | Lifecycle | Candidate |
| 16 | Temporary Publication | Тимчасова публікація | Publication that may be removed | TJS-005 | Lifecycle | Candidate |
| 17 | Permanent Publication | Постійна публікація | Publication that remains forever | TJS-005 | Lifecycle | Candidate |
| 18 | Update Rules | Правила оновлення | When publications may be edited | TJS-005 | Lifecycle | Candidate |
| 19 | Archive Policy | Політика архівування | Rules for preserving historical publications | TJS-005 | Lifecycle | Candidate |
| 20 | Deletion Policy | Політика видалення | Rules for removing publications | TJS-005 | Lifecycle | Candidate |
| 21 | Publication Ownership | Власність публікації | Who owns what publications | TJS-005 | Lifecycle | Candidate |
| 22 | Non-destructive Channel Principle | Принцип недеструктивного каналу | Don't modify others' content | TJS-005 | Lifecycle | Candidate |
| 23 | Non-destructive Update Principle | Принцип недеструктивного оновлення | Update in place, don't recreate | TJS-005 | Lifecycle | Candidate |
| 24 | Publication Session | Сесія публікації | One execution producing one complete state | TJS-005 | Lifecycle | Candidate |
| 25 | Daily Publication Cycle | Щоденний цикл публікацій | Daily operational cycle | TJS-005 | Lifecycle | Candidate |
| 26 | Publication Windows | Вікна публікацій | Time windows for operations | TJS-005 | Lifecycle | Candidate |
| 27 | Traceability | простежуваність | Source dataset, timestamp, generator version | TJS-005 | Lifecycle | Candidate |
| 28 | Reliability | Надійність | No duplicates, order preserved, correct targeting | TJS-005 | Lifecycle | Candidate |
| 29 | Canonical Equality | Канонічна рівність | Byte-for-byte identical comparison | TJS-005 | Lifecycle | Candidate |
| 30 | Error Handling | Обробка помилок | Failure recovery rules | TJS-005 | Lifecycle | Candidate |

---

## Template Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 31 | Publication Structure | Структура публікації | Structural format of publications | TJS-003 | Template | Candidate |
| 32 | Publication Grammar | Граматика публікації | Hierarchical structure rules | TJS-003 | Template | Candidate |
| 33 | Canonical Templates | Канонічні шаблони | Definitive publication templates | TJS-003 | Template | Candidate |
| 34 | Territory Header | Заголовок території | Beginning of publication (uppercase territory name) | TJS-003 | Template | Candidate |
| 35 | Publication Sections | Розділи публікації | Planned Outages, Emergency Outages | TJS-003 | Template | Candidate |
| 36 | Validation Rules | Правила валідації | Prohibitions list for publications | TJS-003 | Template | Candidate |

---

## Formatting Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 37 | Formatting Rules | Правила форматування | Rules for text presentation | TJS-004 + TJS-005 | Formatting | Candidate |
| 38 | Editorial Policy | Редакційна політика | Editorial standards for all text publications | TJS-004 | Formatting | Candidate |
| 39 | Editorial Principles | Редакційні принципи | Territory-first, One post — one territory, etc. | TJS-004 | Formatting | Candidate |
| 40 | Territory Presentation | Представлення території | How territories are displayed | TJS-004 | Formatting | Candidate |
| 41 | Message Categories | Категорії повідомлень | Planned outages, Emergency outages | TJS-004 | Formatting | Candidate |
| 42 | Time Format | Формат часу | How time is displayed | TJS-004 | Formatting | Candidate |
| 43 | Settlement Formatting | Форматування населених пунктів | How settlements are displayed | TJS-004 | Formatting | Candidate |
| 44 | Address Formatting | Форматування адрес | How addresses are displayed | TJS-004 | Formatting | Candidate |
| 45 | Branding | Брендинг | No signatures, no separators, no icons | TJS-004 | Formatting | Candidate |
| 46 | Editing Rules | Правила редагування | Post-publication corrections permitted | TJS-003 | Formatting | Candidate |

---

## Rendering Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 47 | Rendering Pipeline | Конвеєр рендерингу | Sequence: Validation→Sorting→Grouping→Duplicate Removal→Formatting→HTML Escaping→Length Validation→Telegram HTML | TJS-004 | Rendering | Candidate |
| 48 | Deterministic Rendering | Детермінований рендеринг | Same input = same output | TJS-004 | Rendering | Candidate |
| 49 | Stable Ordering | Стабільне сортування | Deterministic element ordering | TJS-004 | Rendering | Candidate |
| 50 | Source Fidelity | Вірність джерелу | No reinterpretation of data | TJS-004 | Rendering | Candidate |
| 51 | Territory Ordering | Сортування територій | Administrative Centre first, then Starosta Districts | TJS-004 | Rendering | Candidate |
| 52 | Time Ordering | Сортування часу | Sorted by start time | TJS-004 | Rendering | Candidate |
| 53 | Settlement Ordering | Сортування населених пунктів | Alphabetical using Ukrainian alphabet | TJS-004 | Rendering | Candidate |
| 54 | Street Ordering | Сортування вулиць | Natural Sort | TJS-004 | Rendering | Candidate |
| 55 | Duplicate Removal | Видалення дублікатів | No duplicate addresses | TJS-004 | Rendering | Candidate |
| 56 | Long Publication Split | Розбиття довгої публікації | Split between complete Settlement blocks | TJS-004 | Rendering | Candidate |
| 57 | HTML Rendering Rules | Правила HTML рендерингу | Allowed tags: `<b>`, `<br>` | TJS-004 | Rendering | Candidate |
| 58 | Stable Output Rule | Правило стабільного виводу | No cosmetic changes | TJS-004 | Rendering | Candidate |
| 59 | Empty Block Rule | Правило порожнього блоку | No empty sections | TJS-004 | Rendering | Candidate |

---

## Platform Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 60 | Channel | Канал | Communication medium | TJS-000 | Platform | Candidate |
| 61 | Telegram Message ID | Ідентифікатор повідомлення Telegram | Identifier for published message | TJS-005 | Platform | Candidate |
| 62 | Telegram Bot API | Telegram Bot API | Telegram Bot interface | TJS-006 (new) | Platform | Candidate |
| 63 | Rate Limiting | Обмеження частоти | Telegram API limits | TJS-006 (new) | Platform | Candidate |
| 64 | Message Editing | Редагування повідомлень | Telegram-specific editing | TJS-006 (new) | Platform | Candidate |
| 65 | Channel Administration | Адміністрування каналу | Admin interaction with channel | TJS-006 (new) | Platform | Candidate |
| 66 | subscribers | підписники | End consumers | TJS-001 | Platform | Candidate |
| 67 | administrators | адміністратори | Channel administrators | TJS-005 | Platform | Candidate |
| 68 | Manual Publications | Ручні публікації | Non-automated publications | TJS-005 | Platform | Candidate |
| 69 | Image Publications | Зображення публікацій | Visual publications | TJS-005 | Platform | Candidate |

---

## Administrative Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 70 | Settlement | Населений пункт | Populated place within a territory | GLOSSARY | Administrative | Candidate |
| 71 | Starosta District | Старостинський округ | Territorial subdivision | GLOSSARY | Administrative | Candidate |
| 72 | Community | Територіальна громада | Primary territorial scope | GLOSSARY | Administrative | Candidate |
| 73 | Administrative Centre | Адміністративний центр | Principal territorial unit | GLOSSARY | Administrative | Candidate |
| 74 | Territory | Територія | Publication unit (Centre or District) | GLOSSARY | Administrative | Candidate |
| 75 | Street | Вулиця | Road name in address | GLOSSARY | Administrative | Candidate |
| 76 | Address | Адреса | Physical location | GLOSSARY | Administrative | Candidate |
| 77 | Time Interval | Часовий інтервал | Duration of outage | TJS-003 | Administrative | Candidate |

---

## Architectural Concepts

| # | Canonical English | Proposed Ukrainian | Meaning | Owner | Category | Status |
|---|------------------|-------------------|---------|-------|----------|--------|
| 78 | SSOT | Єдине джерело правди | One authoritative definition per concept | GLOSSARY | Architectural | Candidate |
| 79 | SRP | Принцип єдиної відповідальності | One responsibility per document | PROJECT_PRINCIPLES | Architectural | Candidate |
| 80 | Separation of Concerns | Розділення відповідальності | Policy vs Implementation separation | ARCHITECTURE | Architectural | Candidate |
| 81 | Semantic Ownership Principle | Принцип семантичної власності | TJS-000 is single semantic authority | TJS-000 | Architectural | Candidate |
| 82 | One Document — One Subject | Один документ — одна тема | Each document defines one subject | PROJECT_PRINCIPLES | Architectural | Candidate |
| 83 | Dependency Direction | Напрямок залежностей | Dependencies flow from TJS-001 downward | ARCHITECTURE | Architectural | Candidate |
| 84 | Metadata Compliance | Відповідність метаданих | Document Class, References, RFC 2119 | ARCHITECTURE | Architectural | Candidate |

---

## Deprecated Terms (NOT Recommended for Canonical Use)

| Term | Reason | Canonical Alternative |
|------|--------|---------------------|
| Message | Platform synonym for Publication | Publication |
| Post | Platform synonym for Publication | Publication |
| Telegram Message | Platform-specific reference | Publication (context: Telegram Message ID) |
| Daily Page | Not used | — |
| Publication Set | Not used | — |
| Feed | Not used | — |
| Page | Not used | — |

---

## Candidate Summary

| Category | Count |
|----------|-------|
| Core | 8 |
| Lifecycle | 22 |
| Template | 6 |
| Formatting | 10 |
| Rendering | 13 |
| Platform | 10 |
| Administrative | 8 |
| Architectural | 7 |
| **Total Candidates** | **84** |
| Deprecated | 5 |

---

**Status:** CANDIDATE — Pending approval in future glossary stage

**Prepared by:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
