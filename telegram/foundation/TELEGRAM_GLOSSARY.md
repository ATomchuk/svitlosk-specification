# TELEGRAM_GLOSSARY.md

Document ID: TJS-000A

Title: Telegram Glossary

Document Class: Foundational

Status: Stable

Author: SvitloSk Project

---

# 1. Purpose

This document defines the canonical terminology of the Telegram Publishing System.

All Telegram specifications SHALL use the terminology defined here.

This document SHALL NOT define workflows, implementation, algorithms, architecture, or processing logic.

---

# 2. Normative Authority

TELEGRAM_GLOSSARY.md is the authoritative semantic source for every Telegram specification.

This document is the single source of truth for Telegram terminology. No other document MAY define, redefine, or override the terms defined here.

When terminology conflicts arise between this glossary and any other document, this glossary SHALL prevail.

---

# 3. Canonical Definition Rule

Each semantic concept SHALL have exactly one canonical definition.

Specifications SHALL reference that definition.

Specifications SHALL NOT redefine it.

If a specification needs to use a term defined in this glossary, it SHALL reference this glossary. It SHALL NOT create an alternative definition for the same term.

---

# 4. Specification Rule

Specifications SHALL use glossary terminology.

Specifications SHALL NOT introduce alternative semantic definitions.

If a new concept is required for a specification, the Glossary SHALL be updated first. Only after the Glossary has been updated with the new term and definition MAY the specification use it.

No specification MAY define a term that is not present in this glossary.

---

# 5. Glossary Governance

All future Telegram specifications must inherit terminology from this document.

No Telegram specification MAY introduce, redefine, or override any term defined in this glossary.

Changes to this glossary SHALL follow the repository governance process:

1. A new term or modified definition SHALL be proposed through the RFC process.
2. The proposal SHALL be reviewed against existing terminology.
3. Approval SHALL be recorded in this document.
4. Specifications SHALL be updated to reference the new or modified term.

This glossary is the semantic foundation of the Telegram documentation subsystem. It governs all terminology used by every Telegram specification.

---

# 6. Semantic Relationships

The following statements describe relationships between semantic concepts. These relationships define the structure of the Telegram Publishing System.

---

## Core Hierarchy

Journal owns Issue.

Issue owns Publication.

Publication belongs to Issue.

Journal is delivered through Telegram.

---

## Publication Relationships

Graphic Publication IS A Publication.

Text Publication IS A Publication.

Temporary Publication IS A Publication.

Permanent Publication IS A Publication.

City Today IS A Publication.

District Today IS A Publication.

City Tomorrow IS A Publication.

District Tomorrow IS A Publication.

---

## Package Relationships

Publication Package contains Publications.

Today's Package IS A Publication Package.

Tomorrow Package IS A Publication Package.

---

## Lifecycle Relationships

Publication Lifecycle governs Publication.

Lifecycle State describes Publication.

Generated IS A Lifecycle State.

Published IS A Lifecycle State.

Updated IS A Lifecycle State.

Archived IS A Lifecycle State.

Removed IS A Lifecycle State.

---

## Component Relationships

Publication Engine implements Publisher.

Publisher creates Publication.

Parser retrieves data for Publication Engine.

Telegram Publisher implements Publisher for Telegram.

---

## Platform Relationships

Channel delivers Publication.

Telegram Message ID identifies Publication on Telegram.

Subscribers receive Publication.

Administrators manage Channel.

---

# 7. How to Use this Glossary

This glossary is the single authoritative source for Telegram terminology.

When writing a Telegram specification:

- Use ONLY the canonical English terms listed in this glossary.
- Use ONLY the approved Ukrainian translations listed in this glossary.
- Do NOT use forbidden terms — use their canonical replacements.
- Derived terms MAY be used only in the context of their parent concept.
- Platform terms MAY appear only when describing Telegram behaviour.
- Architectural terms are NOT part of business semantics.

---

# 8. Core Concepts

## Journal

**Ukrainian:** Журнал

**Definition:** The continuous informational publication of the SvitloSk project. The Journal exists independently from any publication platform.

**Referenced by:** TJS-001, TJS-002, TJS-003, TJS-004, TJS-005, TJS-007, TJS-008

---

## Issue

**Ukrainian:** Випуск журналу

**Definition:** One editorial edition of the Journal for a single calendar day.

**Referenced by:** TJS-000 §4

---

## Publication

**Ukrainian:** Публікація

**Definition:** One independent publication belonging to an Issue. A Publication represents a discrete unit of information delivered to readers through the publication channel.

**Referenced by:** TJS-000 §4, TJS-002, TJS-003, TJS-004, TJS-005, TJS-006, TJS-007, TJS-008

---

## Telegram

**Ukrainian:** Телеграм

**Definition:** The primary publication channel used to deliver Publications to readers. Telegram is the platform, not the Journal itself.

**Referenced by:** TJS-000 §4, all TJS documents

---

## Publication Engine

**Ukrainian:** Движок публікацій

**Definition:** The architectural Component implementing the Publisher Role. The Publication Engine is responsible for generating and distributing Publications.

**Referenced by:** TJS-001 §10, TJS-010 §4.1, TTDR-001

**Category:** A — Architecture Terms

---

## Publisher

**Ukrainian:** Видавець

**Definition:** The logical Role responsible for preparing, generating and distributing Publications. The Publisher is an implementation-independent concept.

**Referenced by:** GLOSSARY.md, TJS-005

---

## Parser

**Ukrainian:** Парсер

**Definition:** The architectural Component responsible for retrieving Open Data from approved Data Sources. The Parser preserves data integrity without interpretation.

**Referenced by:** GLOSSARY.md, TJS-007

---

## SvitloSk

**Ukrainian:** СвітлоСк

**Definition:** The project name. SvitloSk is a public information service that analyses, interprets, archives and distributes officially published open data related to power outages.

**Referenced by:** TJS-001 §1

---

# 9. Derived Concepts

Derived concepts inherit meaning from an APPROVED parent concept. They MAY be used only in the context of their parent concept.

---

## Text Publication

**Ukrainian:** Текстова публікація

**Parent Concept:** Publication

**Definition:** A Publication containing text only, as opposed to Image Publications.

---

## Graphic Publication

**Ukrainian:** Графічна публікація

**Parent Concept:** Publication

**Definition:** A Publication containing graphics. Overlaps with Image Publications (platform behaviour).

---

## City Today

**Ukrainian:** Місто сьогодні

**Parent Concept:** Publication

**Definition:** Template A type — publishes today's information for the Administrative Centre.

---

## District Today

**Ukrainian:** Округ сьогодні

**Parent Concept:** Publication

**Definition:** Template B type — publishes today's information for one Starosta District.

---

## City Tomorrow

**Ukrainian:** Місто завтра

**Parent Concept:** Publication

**Definition:** Template C type — publishes tomorrow's planned outages for the Administrative Centre.

---

## District Tomorrow

**Ukrainian:** Округ завтра

**Parent Concept:** Publication

**Definition:** Template D type — publishes tomorrow's planned outages for one Starosta District.

---

## Today's Package

**Ukrainian:** Пакет сьогодні

**Parent Concept:** Publication Package

**Definition:** All today's publications for the current reporting day.

---

## Tomorrow Package

**Ukrainian:** Пакет завтра

**Parent Concept:** Publication Package

**Definition:** All tomorrow's publications for the next reporting day.

---

## Publication Package

**Ukrainian:** Пакет публікацій

**Parent Concept:** —

**Definition:** Collection of publications for a territory during one reporting period.

---

# 10. Platform Concepts

Platform concepts describe Telegram-specific technical concepts. They MAY appear only when describing Telegram behaviour, NOT when describing the Journal's semantic model.

---

## Channel

**Ukrainian:** Канал

**Definition:** The communication medium through which Publications are delivered. In the Telegram context, this refers to the Telegram channel.

---

## Telegram Message ID

**Ukrainian:** Ідентифікатор повідомлення Telegram

**Definition:** The platform identifier assigned to a published message in Telegram. This is a technical identifier, not a semantic concept.

---

## Telegram Bot API

**Ukrainian:** Telegram Bot API

**Definition:** The Telegram Bot interface used for automated publication delivery.

---

## Rate Limiting

**Ukrainian:** Обмеження частоти

**Definition:** Telegram API constraints that limit the frequency of automated operations.

---

## Message Editing

**Ukrainian:** Редагування повідомлень

**Definition:** The Telegram-specific mechanism for modifying published messages.

---

## Channel Administration

**Ukrainian:** Адміністрування каналу

**Definition:** Administrative interaction with the Telegram channel, including configuration and moderation.

---

## Subscribers

**Ukrainian:** Підписники

**Definition:** End consumers who receive Publications through the Telegram channel.

---

## Administrators

**Ukrainian:** Адміністратори

**Definition:** Channel administrators who manage the Telegram channel configuration and permissions.

---

## Manual Publications

**Ukrainian:** Ручні публікації

**Definition:** Publications created manually by administrators, outside the automated lifecycle.

---

## Image Publications

**Ukrainian:** Зображення публікацій

**Definition:** Visual publications published manually, outside the automatic lifecycle.

---

## Telegram Publisher

**Ukrainian:** Telegram Видавець

**Definition:** The Telegram-specific implementation of the Publisher Role. Handles Telegram Bot API interaction.

---

# 11. Lifecycle Concepts

---

## Publication Lifecycle

**Ukrainian:** Життєвий цикл публікації

**Definition:** The complete lifecycle of a Publication from creation through rendering, publication, update, retention and removal.

---

## Lifecycle State

**Ukrainian:** Стан життєвого циклу

**Definition:** One of the states a Publication passes through during its lifecycle.

---

## Generated

**Ukrainian:** Згенеровано

**Definition:** The state in which a Publication has been created but not yet published.

---

## Published

**Ukrainian:** Опубліковано

**Definition:** The state in which a Publication is live and visible to readers.

---

## Updated

**Ukrainian:** Оновлено

**Definition:** The state in which a Publication has been modified after initial publication.

---

## Archived

**Ukrainian:** Архівовано

**Definition:** The state in which a Publication is preserved as part of the historical record.

---

## Removed

**Ukrainian:** Видалено

**Definition:** The state in which a temporary Publication has been deleted. Only temporary Publications MAY reach this state.

---

## Temporary Publication

**Ukrainian:** Тимчасова публікація

**Definition:** A Publication that may be removed after becoming irrelevant. Temporary Publications are excluded from the permanent archive.

---

## Permanent Publication

**Ukrainian:** Постійна публікація

**Definition:** A Publication that remains in the Journal permanently. Permanent Publications form the historical record.

---

## Update Rules

**Ukrainian:** Правила оновлення

**Definition:** The conditions under which a published Publication MAY be edited. Updates are permitted only when the normalized dataset or rendering rules change.

---

## Archive Policy

**Ukrainian:** Політика архівування

**Definition:** The rules governing preservation of historical Publications. Archive entries shall not be modified except to correct verified technical errors.

---

## Deletion Policy

**Ukrainian:** Політика видалення

**Definition:** The rules governing removal of Publications. Only temporary Publications MAY be deleted.

---

## Publication Ownership

**Ukrainian:** Власність публікації

**Definition:** The model determining which component owns which Publications. Ownership is determined by the stored Telegram Message ID.

---

## Non-destructive Channel Principle

**Ukrainian:** Принцип недеструктивного каналу

**Definition:** The Publisher SHALL modify only Publications that it owns. The Publisher SHALL NOT modify, delete or reorder Publications created by other publishers or administrators.

---

## Non-destructive Update Principle

**Ukrainian:** Принцип недеструктивного оновлення

**Definition:** Updates SHOULD modify existing Publications instead of replacing them. Replacing an existing Publication SHALL be considered a last resort.

---

## Publication Session

**Ukrainian:** Сесія публікації

**Definition:** One execution of the Publication Engine producing a complete Telegram Journal state from one normalized Dataset.

---

## Daily Publication Cycle

**Ukrainian:** Щоденний цикл публікацій

**Definition:** The daily operational cycle of the Telegram Journal, including generation, publication, monitoring, updating, and removal of obsolete Publications.

---

## Publication Windows

**Ukrainian:** Вікна публікацій

**Definition:** The time windows during which the Publication Engine operates, including daily generation, tomorrow generation, continuous updates, and cleanup.

---

## Traceability

**Ukrainian:** Простежуваність

**Definition:** The ability to identify the origin of every Publication, including source dataset, publication timestamp, generator version and generated graphic.

---

## Reliability

**Ukrainian:** Надійність

**Definition:** The guarantee that publications are not duplicated, publication order is preserved, updates target the correct Telegram message, and archived publications remain accessible.

---

## Canonical Equality

**Ukrainian:** Канонічна рівність

**Definition:** The comparison of two Publications generated from identical datasets to determine whether they are byte-for-byte identical. Equivalent Publications SHALL NOT generate Telegram edits.

---

## Error Handling

**Ukrainian:** Обробка помилок

**Definition:** The rules governing failure recovery. Publication lifecycle failures SHALL never corrupt existing Publications, never delete permanent Publications, and never modify administrator-created Publications.

---

## Powered

**Ukrainian:** Без знеструмлення

**Definition:** A state indicating that a territory is NOT currently experiencing an outage. In graphic publications, Powered is represented by the color Orange. The opposite of Powered is Outage (Dark Gray).

**Referenced by:** TJS-022 §8.3, TTDR-001

**Category:** C — Public Communication Terms

---

## Archive

**Ukrainian:** Архів

**Definition:** The state of preserved historical Publications. The Archive serves as the permanent public record of the Telegram Journal.

---

# 12. Template Concepts

---

## Publication Structure

**Ukrainian:** Структура публікації

**Definition:** The structural format of publications, consisting of Territory Header, Publication Sections, and Update Time.

---

## Publication Grammar

**Ukrainian:** Граматика публікації

**Definition:** The hierarchical structure rules governing how Publications are organized: Territory Header → Sections → Settlement → Time → Street → Addresses.

---

## Canonical Templates

**Ukrainian:** Канонічні шаблони

**Definition:** The definitive publication templates: City Today (A), District Today (B), City Tomorrow (C), District Tomorrow (D).

---

## Territory Header

**Ukrainian:** Заголовок території

**Definition:** The beginning of a Publication containing the territory name in uppercase.

---

## Publication Sections

**Ukrainian:** Розділи публікації

**Definition:** The content sections of a Publication: Planned Outages and Emergency Outages. Empty sections SHALL NOT be rendered.

---

## Validation Rules

**Ukrainian:** Правила валідації

**Definition:** The prohibitions list ensuring Publications conform to structural requirements.

---

# 13. Formatting Concepts

---

## Formatting Rules

**Ukrainian:** Правила форматування

**Definition:** The rules governing text presentation in Publications. Formatting policy is owned by TJS-004; formatting implementation is owned by TJS-005.

---

## Editorial Policy

**Ukrainian:** Редакційна політика

**Definition:** The editorial standards for all text publications in the Telegram Journal, ensuring consistency, readability and predictability.

---

## Editorial Principles

**Ukrainian:** Редакційні принципи

**Definition:** The foundational principles: Territory-first presentation, One post — one territory, Maximum readability, Minimal formatting, Consistent structure, No decorative elements, Automatic generation.

---

## Territory Presentation

**Ukrainian:** Представлення території

**Definition:** The rules governing how territories are displayed in Publications, including uppercase formatting and first-element positioning.

---

## Message Categories

**Ukrainian:** Категорії повідомлень

**Definition:** The content categories within Publications: Planned outages and Emergency outages. Categories without records are omitted.

---

## Time Format

**Ukrainian:** Формат часу

**Definition:** The rules governing how time intervals are displayed in Publications.

---

## Settlement Formatting

**Ukrainian:** Форматування населених пунктів

**Definition:** The rules governing how settlement names are displayed: bold, no administrative prefixes.

---

## Address Formatting

**Ukrainian:** Форматування адрес

**Definition:** The rules governing how addresses are displayed: preserve official abbreviations, display line by line.

---

## Branding

**Ukrainian:** Брендинг

**Definition:** The rules ensuring Publications contain no signatures, no decorative separators, and no location icons. The Telegram channel itself represents the SvitloSk identity.

---

## Editing Rules

**Ukrainian:** Правила редагування

**Definition:** The rules governing post-publication corrections. Factual and layout corrections are permitted; the meaning of official information shall never change.

---

## Formatting

**Ukrainian:** Форматування

**Definition:** The rules for text presentation in Publications. Only bold and plain text are permitted.

---

# 14. Rendering Concepts

---

## Rendering Pipeline

**Ukrainian:** Конвеєр рендерингу

**Definition:** The sequence of processing stages: Validation → Sorting → Grouping → Duplicate Removal → Formatting → HTML Escaping → Length Validation → Telegram HTML.

---

## Rendering

**Ukrainian:** Рендеринг

**Definition:** The process of converting normalized data into a presentation-ready Publication.

---

## Deterministic Rendering

**Ukrainian:** Детермінований рендеринг

**Definition:** The principle that the same normalized dataset SHALL always produce identical output.

---

## Stable Ordering

**Ukrainian:** Стабільне сортування

**Definition:** The principle that every rendered element SHALL follow deterministic ordering rules.

---

## Source Fidelity

**Ukrainian:** Вірність джерелу

**Definition:** The principle that rendering SHALL NOT modify or reinterpret official information.

---

## Territory Ordering

**Ukrainian:** Сортування територій

**Definition:** Publications SHALL be generated in the following order: Administrative Centre first, then Starosta Districts alphabetically.

---

## Time Ordering

**Ukrainian:** Сортування часу

**Definition:** Time intervals SHALL always be sorted by their start time.

---

## Settlement Ordering

**Ukrainian:** Сортування населених пунктів

**Definition:** Settlements SHALL be ordered alphabetically using the Ukrainian alphabet. NOTE: This term has a known conflict with TJS-005 §7 requiring ADR resolution.

---

## Street Ordering

**Ukrainian:** Сортування вулиць

**Definition:** Street entries SHALL be ordered alphabetically using Natural Sort.

---

## Duplicate Removal

**Ukrainian:** Видалення дублікатів

**Definition:** Duplicate addresses SHALL NOT appear in publications. Only one instance of a duplicate record SHALL be rendered.

---

## Long Publication Split

**Ukrainian:** Розбиття довгої публікації

**Definition:** If a publication exceeds Telegram limits, it SHALL be divided automatically between complete Settlement blocks. Settlement information SHALL NEVER be divided.

---

## HTML Rendering Rules

**Ukrainian:** Правила HTML рендерингу

**Definition:** Allowed HTML tags: `<b>` and `<br>`. All other HTML tags are prohibited unless explicitly approved by future specifications.

---

## Stable Output Rule

**Ukrainian:** Правило стабільного виводу

**Definition:** Publisher SHALL NOT introduce cosmetic formatting changes. Formatting MAY change only when the normalized dataset or rendering specification changes.

---

## Empty Block Rule

**Ukrainian:** Правило порожнього блоку

**Definition:** Publisher SHALL NOT generate empty sections. Only sections containing information SHALL be rendered.

---

## Rendering Rules

**Ukrainian:** Правила рендерингу

**Definition:** The canonical rendering pipeline and rules governing how normalized data is transformed into deterministic Telegram HTML output.

---

# 15. Administrative Concepts

---

## Settlement

**Ukrainian:** Населений пункт

**Definition:** A populated place within a territory. Settlements are organized hierarchically within Starosta Districts.

---

## Starosta District

**Ukrainian:** Старостинський округ

**Definition:** A territorial subdivision of the Community. The abbreviation SO is normative.

---

## Community

**Ukrainian:** Територіальна громада

**Definition:** The primary territorial scope served by the project. The Community represents the complete territorial coverage.

---

## Administrative Centre

**Ukrainian:** Адміністративний центр

**Definition:** The principal territorial unit of the Community. The Administrative Centre represents the primary settlement.

---

## Territory

**Ukrainian:** Територія

**Definition:** A publication unit representing either the Administrative Centre or one Starosta District.

---

## Street

**Ukrainian:** Вулиця

**Definition:** A road name within an address. Official Ukrainian abbreviations are preserved.

---

## Address

**Ukrainian:** Адреса

**Definition:** A geographical location published by the official Data Source. Addresses are treated exactly as officially published.

---

## Time Interval

**Ukrainian:** Часовий інтервал

**Definition:** A continuous time interval during which electricity is expected to be available or unavailable.

---

# 16. Architectural Concepts

**NOT PART OF BUSINESS SEMANTICS**

The following terms describe HOW the system is organized and governed. They are NOT semantic concepts of the Telegram Publishing System and SHALL NOT be used when describing what the Journal publishes.

---

## SSOT

**Ukrainian:** Єдине джерело правди

**Definition:** Single Source of Truth — one authoritative definition per concept.

---

## SRP

**Ukrainian:** Принцип єдиної відповідальності

**Definition:** Single Responsibility Principle — one responsibility per document.

---

## Separation of Concerns

**Ukrainian:** Розділення відповідальності

**Definition:** The principle that Policy and Implementation are separated across documents.

---

## Semantic Ownership Principle

**Ukrainian:** Принцип семантичної власності

**Definition:** TELEGRAM_SEMANTIC_MODEL.md is the single semantic authority for all Telegram terminology.

---

## One Document — One Subject

**Ukrainian:** Один документ — одна тема

**Definition:** Every normative document defines one complete subject area.

---

## Dependency Direction

**Ukrainian:** Напрямок залежностей

**Definition:** Dependencies flow from TJS-001 downward. No circular dependencies are permitted.

---

## Metadata Compliance

**Ukrainian:** Відповідність метаданих

**Definition:** Every TJS document SHALL have: Document Class, References section, uppercase RFC 2119 keywords.

---

# 17. Forbidden Terminology

The following terms SHALL NOT be used in any Telegram specification. Each forbidden term has a canonical replacement.

---

## Message

**Replacement:** Publication (for semantic meaning); Telegram Message ID (for platform identifier)

**Reason:** Hidden synonym for Publication. Conflates platform implementation with semantic model.

---

## Post

**Replacement:** Publication

**Reason:** Social media connotation that conflicts with the Journal's identity as an official automated public information journal.

---

## Telegram Message

**Replacement:** Publication (for semantic meaning); Telegram Message ID (for platform identifier)

**Reason:** Conflates the semantic concept Publication with the platform concept Telegram Message.

---

## Daily Page

**Replacement:** Issue (for semantic concept); Today's Package (for operational concept)

**Reason:** Not used. Web/print concept that conflicts with the Journal's identity.

---

## Publication Set

**Replacement:** Publication Package

**Reason:** Not used. Mathematical concept that doesn't match the Journal's terminology.

---

## Feed

**Replacement:** Journal

**Reason:** Social media concept that conflicts with the Journal's identity.

---

## Page

**Replacement:** Publication (for individual items); Issue (for daily editions)

**Reason:** Web/print concept. The Journal is a Telegram publication, not a web page.

---

## Coordinator

**Replacement:** —

**Reason:** Not used. Not part of the Telegram subsystem vocabulary.

---

## Workflow

**Replacement:** Daily Publication Cycle (for temporal); Processing Flow (for operational)

**Reason:** Not used as a semantic concept. The Journal has specific terms for operational cycles.

---

## Working Repository

**Replacement:** —

**Reason:** Not a Telegram semantic concept. This is a Git repository governance concept.

---

## Historical Storage

**Replacement:** Archive

**Reason:** Technical implementation term, not a semantic concept.

---

## Journal Finality

**Replacement:** —

**Reason:** Not used. Not a semantic concept.

---

## Repository

**Replacement:** —

**Reason:** Not a Telegram semantic concept. This is a Git/version control concept.

---

## History

**Replacement:** Archive

**Reason:** Imprecise term that conflicts with the specific Archive concept.

---

## System Publication

**Replacement:** Publication

**Reason:** Redundant qualifier. All publications in the Journal are system-generated.

---

## Starostyn District

**Replacement:** Starosta District

**Reason:** Misspelling. The correct term is Starosta District.

---

# 18. Editorial Notes

This glossary was compiled exclusively from approved semantic sources:

- TELEGRAM_SEMANTIC_MODEL.md (TJS-000)
- TELEGRAM_TERM_APPROVAL_REGISTER.md
- TELEGRAM_CANONICAL_SEMANTIC_MODEL.md
- TELEGRAM_DERIVED_TERMS.md
- TELEGRAM_ARCHITECTURAL_TERMS.md
- TELEGRAM_PLATFORM_TERMS.md
- TELEGRAM_FORBIDDEN_TERMS.md
- TELEGRAM_GLOSSARY_READY.md
- TELEGRAM_TRANSLATION_CONSISTENCY.md
- TELEGRAM_GLOSSARY_PUBLICATION_DECISION.md

No semantic decisions were introduced during compilation. All definitions originate from approved sources.

---

# Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- GLOSSARY.md
- TELEGRAM_SEMANTIC_MODEL.md

---

# Referenced by

- TELEGRAM_ARCHITECTURE_DECISION.md
- TJS-001
- TJS-002
- TJS-003
- TJS-004
- TJS-005
- TJS-006
- TJS-007

---

**End of Document**
