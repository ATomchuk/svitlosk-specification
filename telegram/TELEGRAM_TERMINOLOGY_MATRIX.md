# Telegram Terminology Matrix

**Date:** 2026-07-13
**Purpose:** One row per semantic concept
**Source:** TELEGRAM_TERMINOLOGY_HARVEST.md

---

## Core Concepts

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 1 | Journal | Журнал | Telegram Journal, SvitloSk Telegram Journal, Telegram Publishing System | Continuous informational publication of SvitloSk | TJS-000 §4 | TJS-001, TJS-002, TJS-003, TJS-004, TJS-005, TJS-007, TJS-008 | TJS-000 | Foundational | Core | NO | NO | NO | Journal |
| 2 | Issue | Випуск журналу | Daily edition, Reporting day | One editorial edition for a single calendar day | TJS-000 §4 | — | TJS-000 | Foundational | Candidate | NO | NO | NO | Issue |
| 3 | Publication | Публікація | Telegram Publication, Message, Post, Telegram Message | One independent publication belonging to an Issue | TJS-000 §4 | TJS-002, TJS-003, TJS-004, TJS-005, TJS-006, TJS-007, TJS-008 | TJS-000 | Foundational | Core | YES (see Duplication #1) | YES | NO | Publication |
| 4 | Telegram | Платформа публікації | Publication platform, Channel | Primary publication channel | TJS-000 §4 | All TJS | TJS-000 | Foundational | Core | NO | NO | NO | Telegram |
| 5 | Publication Engine | — | Publisher (Role) | Component implementing Publisher Role | TJS-001 §10 | TJS-005, TJS-006, TJS-008 | TJS-000 | Foundational | Core | NO | NO | NO | Publication Engine |
| 6 | Publisher | — | Telegram Publisher | Logical role for creating/distributing publications | TJS-005 §4 | TJS-006, TJS-007, TJS-008 | TJS-000 | Foundational | Core | YES (see Duplication #2) | YES | NO | Publisher |
| 7 | Parser | — | — | Component retrieving Open Data | TJS-007 §4 | TJS-008 | GLOSSARY | Normative | Core | NO | NO | NO | Parser |
| 8 | SvitloSk | — | — | Project name | TJS-001 §1 | All TJS | TJS-001 | Normative | Core | NO | NO | NO | SvitloSk |

---

## Supporting Concepts — Lifecycle

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 9 | Publication Lifecycle | — | Lifecycle, Publication Lifecycle States | Complete lifecycle from creation to archival | TJS-002 §1 | TJS-007, TJS-008 | TJS-005 (merged) | Normative | Core | YES (see Duplication #3) | YES | NO | Publication Lifecycle |
| 10 | Lifecycle State Model | — | Lifecycle States, Publication States | States a publication passes through | TJS-002 §3 | TJS-007 §3, TJS-008 §3 | TJS-005 | Normative | Core | YES (see Duplication #4) | YES | NO | Lifecycle State Model |
| 11 | Generated | — | — | State: publication created | TJS-002 §3 | TJS-007, TJS-008 | TJS-005 | Normative | Supporting | NO | NO | NO | Generated |
| 12 | Published | — | — | State: publication live | TJS-002 §3 | TJS-007, TJS-008 | TJS-005 | Normative | Supporting | NO | NO | NO | Published |
| 13 | Updated | — | — | State: publication modified | TJS-002 §3 | TJS-007, TJS-008 | TJS-005 | Normative | Supporting | NO | NO | NO | Updated |
| 14 | Archived | — | — | State: publication preserved | TJS-002 §3 | TJS-007 | TJS-005 | Normative | Supporting | NO | NO | NO | Archived |
| 15 | Removed | — | — | State: publication deleted (temporary only) | TJS-002 §3 | TJS-007, TJS-008 | TJS-005 | Normative | Supporting | NO | NO | NO | Removed |
| 16 | Temporary Publication | — | Tomorrow Publication, Removable Publication | Publication that may be removed | TJS-002 §7 | TJS-007 §8, TJS-008 §12 | TJS-005 | Normative | Supporting | YES (see Duplication #5) | YES | NO | Temporary Publication |
| 17 | Permanent Publication | — | Historical Publication, Current-day Publication | Publication that remains forever | TJS-007 §9 | TJS-002 §9, TJS-008 | TJS-005 | Normative | Supporting | YES (see Duplication #6) | YES | NO | Permanent Publication |
| 18 | Update Rules | — | Update Policy | When publications may be edited | TJS-002 §8 | TJS-007 §5, TJS-008 §11 | TJS-005 | Normative | Supporting | YES (see Duplication #7) | YES | NO | Update Rules |
| 19 | Archive Policy | — | — | Rules for preserving historical publications | TJS-002 §9 | TJS-007 §9 | TJS-005 | Normative | Supporting | YES (see Duplication #8) | YES | NO | Archive Policy |
| 20 | Deletion Policy | — | — | Rules for removing publications | TJS-002 §10 | TJS-008 §12 | TJS-005 | Normative | Supporting | NO | NO | NO | Deletion Policy |
| 21 | Publication Ownership | — | Ownership Model | Who owns what publications | TJS-007 §10 | TJS-008 | TJS-005 | Normative | Supporting | NO | NO | NO | Publication Ownership |
| 22 | Non-destructive Channel Principle | — | — | Don't modify others' content | TJS-007 §11 | TJS-008 §10 | TJS-005 | Normative | Supporting | YES (see Duplication #9) | YES | NO | Non-destructive Channel Principle |
| 23 | Non-destructive Update Principle | — | — | Update in place, don't recreate | TJS-008 §10 | — | TJS-005 | Normative | Supporting | YES (see Duplication #9) | YES | NO | Non-destructive Update Principle |
| 24 | Publication Session | — | — | One execution producing one complete state | TJS-008 §15 | — | TJS-005 | Normative | Supporting | NO | NO | NO | Publication Session |
| 25 | Daily Publication Cycle | — | Publication Cycle | Daily operational cycle | TJS-008 §3 | TJS-002 §5, TJS-007 | TJS-005 | Normative | Supporting | NO | NO | NO | Daily Publication Cycle |
| 26 | Publication Windows | — | — | Time windows for operations | TJS-008 §6 | — | TJS-005 | Normative | Supporting | NO | NO | NO | Publication Windows |
| 27 | Traceability | — | — | Source dataset, timestamp, generator version | TJS-002 §11 | — | TJS-005 | Normative | Supporting | NO | NO | NO | Traceability |
| 28 | Reliability | — | — | No duplicates, order preserved, correct targeting | TJS-002 §12 | — | TJS-005 | Normative | Supporting | NO | NO | NO | Reliability |
| 29 | Canonical Equality | — | — | Byte-for-byte identical comparison | TJS-007 §6 | TJS-006 §3 | TJS-005 | Normative | Supporting | NO | NO | NO | Canonical Equality |
| 30 | Error Handling | — | — | Failure recovery rules | TJS-007 §13 | TJS-006 §15 | TJS-005 | Normative | Supporting | NO | NO | NO | Error Handling |

---

## Supporting Concepts — Templates & Structure

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 31 | Publication Structure | — | Standard Publication Structure, Post Structure | Structural format of publications | TJS-003 §3 | TJS-005 §4 | TJS-003 | Normative | Supporting | YES (see Duplication #10) | YES | NO | Publication Structure |
| 32 | Publication Grammar | — | Structural Grammar, Grammar Tree | Hierarchical structure rules | TJS-005 §4 | TJS-003 | TJS-003 | Normative | Supporting | NO | NO | NO | Publication Grammar |
| 33 | Canonical Templates | — | Template A, B, C, D | Definitive publication templates | TJS-005 §13 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Canonical Templates |
| 34 | Template A: City Today | — | — | For Administrative Centre, today | TJS-005 §13 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Template A: City Today |
| 35 | Template B: District Today | — | — | For Starosta District, today | TJS-005 §13 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Template B: District Today |
| 36 | Template C: City Tomorrow | — | — | For Administrative Centre, tomorrow | TJS-005 §13 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Template C: City Tomorrow |
| 37 | Template D: District Tomorrow | — | — | For Starosta District, tomorrow | TJS-005 §13 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Template D: District Tomorrow |
| 38 | Territory Header | — | — | Beginning of publication (uppercase territory name) | TJS-005 §5 | TJS-004 §3 | TJS-003 | Normative | Supporting | NO | NO | NO | Territory Header |
| 39 | Publication Sections | — | — | Planned Outages, Emergency Outages | TJS-005 §6 | TJS-004 §5 | TJS-003 | Normative | Supporting | NO | NO | NO | Publication Sections |
| 40 | Header | — | — | Top section of publication | TJS-003 §4 | TJS-005 §5 | TJS-003 | Normative | Supporting | YES (see Duplication #11) | YES | NO | Header |
| 41 | Main Information | — | — | Core content section | TJS-003 §5 | TJS-005 §6 | TJS-003 | Normative | Supporting | NO | NO | NO | Main Information |
| 42 | Graphic Block | — | — | Optional graphic section | TJS-003 §6 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Graphic Block |
| 43 | Additional Information | — | — | Optional supplementary section | TJS-003 §7 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Additional Information |
| 44 | Footer | — | — | Bottom section of publication | TJS-003 §8 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Footer |
| 45 | Validation Rules | — | — | Prohibitions list for publications | TJS-005 §14 | TJS-006 §14 | TJS-003 | Normative | Supporting | NO | NO | NO | Validation Rules |

---

## Supporting Concepts — Formatting

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 46 | Formatting Rules | — | Formatting Policy, Formatting Implementation | Rules for text presentation | TJS-003 §9 | TJS-004 §11, TJS-005 §15 | TJS-004 (policy) + TJS-005 (implementation) | Normative | Supporting | YES (see Duplication #12) | YES | NO | Formatting Rules |
| 47 | Editorial Policy | — | — | Editorial standards for all text publications | TJS-004 §1 | — | TJS-004 | Approved | Core | NO | NO | NO | Editorial Policy |
| 48 | Editorial Principles | — | — | Territory-first, One post — one territory, etc. | TJS-004 §2 | — | TJS-004 | Approved | Supporting | NO | NO | NO | Editorial Principles |
| 49 | Territory Presentation | — | Territory Rules | How territories are displayed | TJS-004 §3 | TJS-005 §5 | TJS-004 | Approved | Supporting | NO | NO | NO | Territory Presentation |
| 50 | Message Categories | — | — | Planned outages, Emergency outages | TJS-004 §5 | TJS-005 §6 | TJS-004 | Approved | Supporting | NO | NO | NO | Message Categories |
| 51 | Time Format | — | Time Format Rules | How time is displayed | TJS-004 §8 | TJS-005 §9 | TJS-004 | Approved | Supporting | NO | NO | NO | Time Format |
| 52 | Settlement Formatting | — | Settlement Formatting Policy | How settlements are displayed | TJS-004 §9 | TJS-005 §10 | TJS-004 | Approved | Supporting | NO | NO | NO | Settlement Formatting |
| 53 | Address Formatting | — | Address Formatting Policy | How addresses are displayed | TJS-004 §10 | TJS-005 §11-12 | TJS-004 | Approved | Supporting | NO | NO | NO | Address Formatting |
| 54 | Branding | — | Branding Rules | No signatures, no separators, no icons | TJS-004 §13 | — | TJS-004 | Approved | Supporting | NO | NO | NO | Branding |
| 55 | Editing Rules | — | — | Post-publication corrections permitted | TJS-003 §10 | — | TJS-003 | Normative | Supporting | NO | NO | NO | Editing Rules |

---

## Supporting Concepts — Rendering

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 56 | Rendering Pipeline | — | Canonical Rendering Process | Sequence: Validation→Sorting→Grouping→Duplicate Removal→Formatting→HTML Escaping→Length Validation→Telegram HTML | TJS-006 §4 | — | TJS-004 | Normative | Core | NO | NO | NO | Rendering Pipeline |
| 57 | Deterministic Rendering | — | — | Same input = same output | TJS-006 §3 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Deterministic Rendering |
| 58 | Stable Ordering | — | — | Deterministic element ordering | TJS-006 §3 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Stable Ordering |
| 59 | Source Fidelity | — | — | No reinterpretation of data | TJS-006 §3 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Source Fidelity |
| 60 | Territory Ordering | — | — | Administrative Centre first, then Starosta Districts | TJS-006 §5 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Territory Ordering |
| 61 | Time Ordering | — | — | Sorted by start time | TJS-006 §6 | TJS-005 §8 | TJS-004 | Normative | Supporting | NO | NO | NO | Time Ordering |
| 62 | Settlement Ordering | — | — | Alphabetical using Ukrainian alphabet | TJS-006 §7 | TJS-005 §7 | TJS-004 | Normative | Supporting | YES (CONFLICT with TJS-005 §7) | RESTRUCTURE | YES | Settlement Ordering |
| 63 | Street Ordering | — | — | Natural Sort | TJS-006 §8 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Street Ordering |
| 64 | Duplicate Removal | — | — | No duplicate addresses | TJS-006 §9 | TJS-005 §12 | TJS-004 | Normative | Supporting | NO | NO | NO | Duplicate Removal |
| 65 | Long Publication Split | — | — | Split between complete Settlement blocks | TJS-006 §10 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Long Publication Split |
| 66 | HTML Rendering Rules | — | — | Allowed tags: `<b>`, `<br>` | TJS-006 §11 | — | TJS-004 | Normative | Supporting | NO | NO | NO | HTML Rendering Rules |
| 67 | Stable Output Rule | — | — | No cosmetic changes | TJS-006 §12 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Stable Output Rule |
| 68 | Empty Block Rule | — | — | No empty sections | TJS-006 §13 | — | TJS-004 | Normative | Supporting | NO | NO | NO | Empty Block Rule |

---

## Platform Concepts

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 69 | Channel | — | Telegram Channel, Publication Channel | Communication medium | TJS-001 §10 | TJS-007 §11 | TJS-000 | Foundational | Platform | NO | NO | NO | Channel |
| 70 | Telegram Message ID | — | Message ID | Identifier for published message | TJS-007 §10 | TJS-008 | TJS-005 | Normative | Platform | NO | NO | NO | Telegram Message ID |
| 71 | Telegram Bot API | — | Bot API, API | Telegram Bot interface | TJS-006 (proposed) | — | TJS-006 (new) | Normative | Platform | NO | NO | NO | Telegram Bot API |
| 72 | Rate Limiting | — | API Constraints | Telegram API limits | TJS-006 (proposed) | — | TJS-006 (new) | Normative | Platform | NO | NO | NO | Rate Limiting |
| 73 | Message Editing | — | Message Editing Rules | Telegram-specific editing | TJS-006 (proposed) | — | TJS-006 (new) | Normative | Platform | NO | NO | NO | Message Editing |
| 74 | Channel Administration | — | — | Admin interaction with channel | TJS-006 (proposed) | — | TJS-006 (new) | Normative | Platform | NO | NO | NO | Channel Administration |
| 75 | subscribers | — | readers, Users | End consumers | TJS-001 §10 | TJS-000 §4 | TJS-001 | Normative | Platform | NO | NO | NO | subscribers |
| 76 | administrators | — | admin, Admin | Channel administrators | TJS-007 §11 | TJS-008 §13 | TJS-005 | Normative | Platform | NO | NO | NO | administrators |
| 77 | Manual Publications | — | Administrator Posts, Manual Posts | Non-automated publications | TJS-008 §13 | TJS-007 §11 | TJS-005 | Normative | Platform | NO | NO | NO | Manual Publications |
| 78 | Image Publications | — | Graphical Publications, Promotional Graphics | Visual publications | TJS-008 §14 | TJS-007 §11 | TJS-005 | Normative | Platform | NO | NO | NO | Image Publications |

---

## Derived Concepts

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 79 | Graphic Rendering | — | Graphic Generation | Visual output generation | TJS-007 (proposed) | — | TJS-007 (new) | Normative | Derived | NO | NO | NO | Graphic Rendering |
| 80 | Text Publication | — | — | Publication with text only | Implicit | — | TJS-003 | Normative | Derived | NO | NO | NO | Text Publication |
| 81 | System Publication | — | Automated Publication | Publication generated by system | Implicit | — | TJS-005 | Normative | Derived | NO | NO | NO | System Publication |
| 82 | City Today | — | — | Template A type | TJS-005 §13 | TJS-008 §4 | TJS-003 | Normative | Derived | NO | NO | NO | City Today |
| 83 | District Today | — | — | Template B type | TJS-005 §13 | TJS-008 §4 | TJS-003 | Normative | Derived | NO | NO | NO | District Today |
| 84 | City Tomorrow | — | — | Template C type | TJS-005 §13 | TJS-008 §5 | TJS-003 | Normative | Derived | NO | NO | NO | City Tomorrow |
| 85 | District Tomorrow | — | — | Template D type | TJS-005 §13 | TJS-008 §5 | TJS-003 | Normative | Derived | NO | NO | NO | District Tomorrow |
| 86 | Today's Package | — | Daily Publication Package | All today's publications | TJS-008 §4 | TJS-007 | TJS-005 | Normative | Derived | NO | NO | NO | Today's Package |
| 87 | Tomorrow Package | — | Tomorrow Publication Package | All tomorrow's publications | TJS-008 §5 | — | TJS-005 | Normative | Derived | NO | NO | NO | Tomorrow Package |
| 88 | Publication Package | — | — | Collection of publications for a territory | TJS-004 §4 | TJS-005, TJS-008 | TJS-004 | Approved | Derived | NO | NO | NO | Publication Package |

---

## Administrative Concepts

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 89 | Settlement | — | — | Populated place within a territory | TJS-005 §10 | TJS-004 §9 | GLOSSARY | Normative | Administrative | NO | NO | NO | Settlement |
| 90 | Starosta District | SO | Starosta Okruh, Starosta District | Territorial subdivision | TJS-005 §7 | TJS-004 §3 | GLOSSARY | Normative | Administrative | NO | NO | NO | Starosta District |
| 91 | Community | — | Territorial Community | Primary territorial scope | TJS-001 §8 | TJS-000 | GLOSSARY | Normative | Administrative | NO | NO | NO | Community |
| 92 | Administrative Centre | — | City, City Today | Principal territorial unit | TJS-006 §5 | TJS-005 §13 | GLOSSARY | Normative | Administrative | NO | NO | NO | Administrative Centre |
| 93 | Territory | — | — | Publication unit (Centre or District) | TJS-004 §3 | TJS-005 §5 | GLOSSARY | Normative | Administrative | NO | NO | NO | Territory |
| 94 | Street | — | — | Road name in address | TJS-005 §11 | TJS-004 §10 | GLOSSARY | Normative | Administrative | NO | NO | NO | Street |
| 95 | Address | — | — | Physical location | TJS-005 §12 | TJS-004 §10 | GLOSSARY | Normative | Administrative | NO | NO | NO | Address |
| 96 | Time Interval | — | — | Duration of outage | TJS-005 §8 | TJS-004 §8 | TJS-003 | Normative | Administrative | NO | NO | NO | Time Interval |

---

## Architectural Concepts

| # | Canonical Term | Ukrainian | Variants | Meaning | Introduced In | Referenced By | Owner | Owner Class | Status | Duplicate? | Merge? | Violates 1C1T? | Recommended |
|---|---------------|-----------|----------|---------|--------------|---------------|-------|-------------|--------|-----------|--------|----------------|-----------|
| 97 | SSOT | — | Single Source of Truth | One authoritative definition per concept | GLOSSARY | All audit docs | GLOSSARY | Normative | Architectural | NO | NO | NO | SSOT |
| 98 | SRP | — | Single Responsibility Principle | One responsibility per document | PROJECT_PRINCIPLES | Audit docs | PROJECT_PRINCIPLES | Normative | Architectural | NO | NO | NO | SRP |
| 99 | Separation of Concerns | — | — | Policy vs Implementation separation | ARCHITECTURE | Audit docs | ARCHITECTURE | Normative | Architectural | NO | NO | NO | Separation of Concerns |
| 100 | Semantic Ownership Principle | — | — | TJS-000 is single semantic authority | TJS-000 §6 | Foundation audit | TJS-000 | Foundational | Architectural | NO | NO | NO | Semantic Ownership Principle |
| 101 | One Document — One Subject | — | P-10 | Each document defines one subject | PROJECT_PRINCIPLES | Audit docs | PROJECT_PRINCIPLES | Normative | Architectural | NO | NO | NO | One Document — One Subject |
| 102 | Dependency Direction | — | — | Dependencies flow from TJS-001 downward | ARCHITECTURE | Audit docs | ARCHITECTURE | Normative | Architectural | NO | NO | NO | Dependency Direction |
| 103 | Metadata Compliance | — | — | Document Class, References, RFC 2119 | AUDIT | All audit docs | ARCHITECTURE | Normative | Architectural | NO | NO | NO | Metadata Compliance |

---

**End of Terminology Matrix**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
