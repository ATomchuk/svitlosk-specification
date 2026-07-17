# TELEGRAM_GRAPHIC_PUBLICATION_MODEL

**Document ID:** TJS-022

**Title:** Telegram Graphic Publication Model

**Document Class:** Normative Specification

**Status:** Draft

**Author:** SvitloSk Project

---

# 1. Purpose

This specification defines the graphic publication system of the Telegram Publishing System. It establishes the graphic publication mission, principles, taxonomy, structure, semantics, composition, invariants, requirements, and constraints for graphic publications within the Telegram Journal.

This document is normative. All Telegram graphic specifications SHALL conform to the graphic publication model defined herein.

---

# 2. Scope

This specification covers:

- Graphic publication mission and purpose
- Graphic publication principles (2 canonical principles)
- Graphic publication taxonomy (5 publication types)
- Graphic publication structure (elements, branding, content, metadata)
- Graphic publication semantics (meaning, information hierarchy, territory)
- Graphic publication composition (rules, timeline, color, layout)
- Graphic publication invariants (identity, content, visual, temporal)
- Graphic publication requirements (generation, validation, delivery, archive)
- Graphic constraints (7 mandatory constraints)

This specification does NOT define:

- Publishing architecture (TELEGRAM_PUBLISHING_MODEL.md owns this)
- Editorial decision making (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md owns this)
- Publication lifecycle mechanics (TELEGRAM_PUBLICATION_LIFECYCLE.md owns this)
- Telegram API integration
- Rendering algorithms
- SVG generation algorithms
- PNG generation algorithms
- Layout coordinates
- Color implementation
- Font selection
- Implementation details
- Infrastructure

---

# 3. Graphic Publication Mission

The Graphic Publication Model defines how visual information is produced, structured, and maintained within the Telegram Journal. Graphic publications transform normalized outage data into clear, accessible visual formats that residents can understand at a glance.

Graphic publications serve the residents of the Starokostiantyniv Territorial Community. They communicate outage information through visual simplicity, using proportional timelines, consistent color coding, and clean layout.

Every graphic publication SHALL faithfully represent the official source data without alteration. The Graphic Publication Model increases clarity by reorganizing information into visual formats, but SHALL NOT change the factual meaning of officially published data.

---

# 4. Graphic Publication Principles

The Graphic Publication Model is governed by the following two canonical principles. These principles are frozen and SHALL NOT change without formal governance.

## 4.1 Graphic Automation

**Principle:** Графічна автоматизація

Graphics SHALL be generated automatically from normalized data without manual editing. The graphic generation process SHALL be triggered automatically after successful schedule generation. Manual intervention SHALL NOT be part of the standard graphic workflow.

This principle governs graphic decisions about automation and manual intervention. It defines the boundary between automatic generation and manual editing for graphic publications.

This principle SHALL NOT regulate: what data is used for graphics, how schedules are generated, what editorial decisions are made, or how the Telegram channel delivers graphics.

## 4.2 Graphic Clarity

**Principle:** Графічна ясність

Graphics SHALL be clear, minimalistic, and easy to understand at a glance. Graphic publications SHALL communicate outage information through visual simplicity, using proportional timelines, consistent color coding, and clean layout. Visual complexity SHALL NOT obscure the information.

This principle governs graphic decisions about visual design quality. It ensures that graphics communicate information effectively through visual simplicity.

This principle SHALL NOT regulate: what data is used for graphics, how graphics are generated, what branding elements are applied, or how the Telegram channel delivers graphics.

---

# 5. Graphic Publication Taxonomy

## 5.1 Publication Families

Publication Families are organizational categories for document readability. They group related publication types into logical categories: Scheduled, Informational, Statistical, and Administrative.

Publication Families do NOT participate in the architecture. They do NOT define behaviour. They do NOT own responsibilities. They do NOT introduce semantic concepts. They do NOT participate in traceability.

Publication Families are used ONLY for improving document readability. Every architectural decision is made at the Publication Type level, not at the Family level.

## 5.2 Tomorrow Schedule Graphic

**Type ID:** T-001

**Ukrainian:** Графік знеструмлень на завтра

**Family:** Scheduled

The Tomorrow Schedule Graphic is the primary public information card. It shows tomorrow's planned outages for one territory.

| Property | Value |
|----------|-------|
| Trigger | Automatic (after schedule generation) |
| Territory | One territory per graphic |
| Contains | Date, queues, subqueues, outage intervals, powered intervals, timestamp, branding |
| Timeline | 00:00–24:00, proportional |
| Colors | Powered=Orange, Outage=Dark Gray |
| Update | When data changes |
| Archive | When reporting period ends |

**Note:** T-001 is generated during the previous day. After the beginning of the corresponding calendar day, this publication automatically becomes the current valid schedule. The publication TYPE does NOT change — only its temporal relevance changes.

## 5.3 Emergency Information Card

**Type ID:** T-003

**Ukrainian:** Картка аварійного повідомлення

**Family:** Informational

The Emergency Information Card contains urgent information. It has priority over scheduled publications.

| Property | Value |
|----------|-------|
| Trigger | Emergency event |
| Territory | One territory per card |
| Contains | Emergency message, territory, timestamp, branding |
| Timeline | None |
| Colors | Emergency-specific |
| Update | When emergency status changes |
| Archive | When emergency resolved |

## 5.4 Information Card

**Type ID:** T-004

**Ukrainian:** Інформаційна картка

**Family:** Informational

The Information Card contains general informational messages without schedule timeline.

| Property | Value |
|----------|-------|
| Trigger | Administrative decision |
| Territory | One territory per card |
| Contains | Informational message, territory, timestamp, branding |
| Timeline | None |
| Colors | Standard |
| Update | When information changes |
| Archive | Permanent |

## 5.5 Statistics Card

**Type ID:** T-005

**Ukrainian:** Картка статистики

**Family:** Statistical

The Statistics Card contains generated statistics.

| Property | Value |
|----------|-------|
| Trigger | Automatic (daily/periodic) |
| Territory | One territory or community-wide |
| Contains | Powered percentage, outage percentage, total outage duration, timestamp, branding |
| Timeline | None |
| Colors | Standard |
| Update | When statistics change |
| Archive | Permanent |

## 5.6 Service Graphic

**Type ID:** T-006

**Ukrainian:** Службова графіка

**Family:** Administrative

The Service Graphic contains internal service messages.

| Property | Value |
|----------|-------|
| Trigger | Manual |
| Territory | Variable |
| Contains | Service message, timestamp, branding |
| Timeline | None |
| Colors | Standard |
| Update | When service message changes |
| Archive | Permanent |

---

# 6. Graphic Publication Structure

## 6.1 Common Elements

Every graphic publication SHALL contain the following structural elements:

- Header
- Main Information Block
- Service Information
- Footer

## 6.2 Branding Elements

Every graphic publication SHALL contain official SvitloSk branding:

- SvitloSk logo
- Project name
- Publication date
- Generation timestamp

Branding elements SHALL be consistently applied across all graphic types.

## 6.3 Content Elements

Content elements vary by publication type:

| Type | Content Elements |
|------|-----------------|
| T-001 Tomorrow Schedule | Date, queues, subqueues, outage intervals, powered intervals |
| T-003 Emergency Card | Emergency message, territory |
| T-004 Information Card | Informational message, territory |
| T-005 Statistics Card | Powered percentage, outage percentage, total outage duration |
| T-006 Service Graphic | Service message |

## 6.4 Graphic Publication Metadata

Every graphic publication SHALL carry the following metadata:

### 6.4.1 Generation Timestamp

The timestamp when the graphic was generated.

### 6.4.2 Publication Timestamp

The timestamp when the graphic was published to Telegram.

### 6.4.3 Territory

The territory this graphic represents.

### 6.4.4 Source Dataset

The normalized dataset used to generate this graphic.

### 6.4.5 Version

The version identifier of this graphic.

### 6.4.6 Publication Identity

The unique identifier for this graphic publication.

---

# 7. Graphic Publication Semantics

## 7.1 Semantic Meaning

Graphic publications are visual representations of normalized outage data. They communicate factual information about electricity outages through visual formats that residents can understand at a glance.

Every graphic publication SHALL faithfully represent the official source data without alteration. The graphic publication increases clarity by reorganizing information into visual formats, but SHALL NOT change the factual meaning of officially published data.

## 7.2 Information Hierarchy

Graphic publications follow a clear information hierarchy:

1. Territory name (primary)
2. Date (secondary)
3. Outage information (tertiary)
4. Branding (quaternary)

## 7.3 Territory Representation

Every graphic publication SHALL represent exactly one territory. The territory name SHALL always be the first element in the visual hierarchy.

---

# 8. Graphic Publication Composition

## 8.1 Composition Rules

| Rule | Statement |
|------|-----------|
| CR-001 | Every graphic SHALL be composed from normalized data |
| CR-002 | Every graphic SHALL be deterministic for identical input |
| CR-003 | Every graphic SHALL preserve the factual meaning of source data |
| CR-004 | Every graphic SHALL follow the approved layout structure |
| CR-005 | New composition rules MAY be added through ADR |

## 8.2 Timeline Composition

Timeline graphics (T-001) SHALL represent the full 24-hour period from 00:00 to 24:00. Intervals SHALL always be proportional to time. The timeline SHALL clearly distinguish between powered and outage states.

## 8.3 Color Composition

Colors SHALL always represent state:

| State | Color |
|-------|-------|
| Powered | Orange |
| Outage | Dark Gray |

No additional semantic colors SHALL be introduced.

## 8.4 Layout Composition

Every graphic publication SHALL follow the approved layout structure. The layout order SHALL be consistent across all graphic types. Layout elements SHALL NOT be rearranged.

## 8.5 Graphic Publication Layout

Every graphic publication SHALL contain the following layout elements:

### 8.5.1 Header

Territory name, date, project branding.

### 8.5.2 Main Information Block

Primary content varies by publication type.

### 8.5.3 Legend

Color coding explanation. Required for schedule graphics (T-001). Optional for other types.

### 8.5.4 Service Information

Generation timestamp, version.

### 8.5.5 Footer

SvitloSk branding.

---

# 9. Graphic Publication Invariants

## 9.1 Identity Invariants

- Every graphic publication SHALL have a unique publication identity
- Every graphic publication SHALL belong to exactly one type
- Every graphic publication SHALL belong to exactly one territory

## 9.2 Content Invariants

- Every graphic publication SHALL faithfully represent source data
- Every graphic publication SHALL NOT change the factual meaning of official data
- Every graphic publication SHALL contain all required metadata

## 9.3 Visual Invariants

- Every graphic publication SHALL follow the approved layout structure
- Every graphic publication SHALL contain official SvitloSk branding
- Every graphic publication SHALL use approved color semantics
- Every graphic publication SHALL remain readable on all display types

## 9.4 Temporal Invariants

- Every graphic publication SHALL be deterministic for identical input
- Every graphic publication SHALL be traceable to its source dataset
- Every graphic publication SHALL preserve its identity across updates

---

# 10. Graphic Publication Requirements

## 10.1 Generation Requirements

- Graphics SHALL be generated automatically from normalized data
- Graphics SHALL be triggered automatically after successful schedule generation
- Graphics SHALL NOT require manual editing
- Graphics SHALL be deterministic for identical input

## 10.2 Validation Requirements

- Before publication every generated graphic SHALL be validated
- Invalid graphics SHALL never be published
- Validation SHALL verify: date, timeline consistency, branding, queue count, subqueue count, image dimensions

## 10.3 Delivery Requirements

- Graphics SHALL be delivered to the Telegram channel
- Graphics SHALL be optimized for Telegram, mobile devices, and desktop viewing
- Graphics SHALL remain readable on light and dark displays

## 10.4 Archive Requirements

- Graphic publications SHALL be preserved as part of the historical record
- Graphic publications SHALL remain accessible after archival
- Graphic publications SHALL retain their metadata in archive

---

# 11. Graphic Constraints

## C-001: Graphic Branding

Every generated graphic SHALL contain official SvitloSk branding: SvitloSk logo, project name, publication date, and generation timestamp. Branding elements SHALL be consistently applied across all graphic types.

## C-002: Graphic Accessibility

Graphics SHALL remain readable on all display types, including light displays, dark displays, and small mobile screens. This constraint implements Editorial Accessibility (§4.9 of TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md) for graphic publications.

## C-003: Graphic Color

Colors SHALL always represent state. Powered = Orange. Outage = Dark Gray. No additional semantic colors SHALL be introduced.

## C-004: Graphic Automation Trigger

Graphic generation SHALL be triggered automatically after successful schedule generation. Manual triggering SHALL NOT be required.

## C-005: Graphic Format

The generator SHALL support PNG and SVG formats only. Other formats SHALL NOT be generated.

## C-006: Graphic Validation

Before publication every generated graphic SHALL be validated. Invalid graphics SHALL never be published.

## C-007: Graphic Timeline

Timeline intervals SHALL always be proportional to time. The timeline represents 00:00–24:00.

---

# 12. Out of Scope

This specification does NOT define:

- Publishing architecture (TELEGRAM_PUBLISHING_MODEL.md owns this)
- Editorial decision making (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md owns this)
- Publication lifecycle mechanics (TELEGRAM_PUBLICATION_LIFECYCLE.md owns this)
- Telegram API integration
- Rendering algorithms
- SVG generation algorithms
- PNG generation algorithms
- Layout coordinates
- Color implementation
- Font selection
- Implementation details
- Infrastructure

---

# 13. Traceability

This specification:

- Uses terminology from TELEGRAM_GLOSSARY.md (TJS-000A)
- Follows the semantic model from TELEGRAM_SEMANTIC_MODEL.md (TJS-000)
- Conforms to TELEGRAM_ARCHITECTURE_DECISION.md
- References TELEGRAM_PUBLISHING_MODEL.md for publishing architecture
- References TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md for editorial decisions
- References TELEGRAM_PUBLICATION_LIFECYCLE.md for lifecycle mechanics
- References Repository Authority Principle (TELEGRAM_PUBLICATION_LIFECYCLE.md §3.1)
- References Editorial Accessibility (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md §4.9)
- References Deterministic Rendering (TELEGRAM_PUBLISHING_PRINCIPLES.md P-016)
- References Visual Stability (TELEGRAM_PUBLISHING_PRINCIPLES.md P-015)
- References Source Fidelity (TELEGRAM_PUBLISHING_PRINCIPLES.md P-017)
- References Consistency (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md §4.8)
- References Timeliness (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md §4.10)

---

# 14. Change History

| Date | Version | Description |
|------|---------|-------------|
| 2026-07-13 | 1.0.0 | Initial compilation from approved Semantic Foundation |

---

# References

## Depends on

- TELEGRAM_SEMANTIC_MODEL.md (TJS-000)
- TELEGRAM_GLOSSARY.md (TJS-000A)
- TELEGRAM_ARCHITECTURE_DECISION.md
- TELEGRAM_PUBLISHING_MODEL.md (TJS-010)
- TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md (TJS-020)
- TELEGRAM_PUBLICATION_LIFECYCLE.md (TJS-021)
- PROJECT_PRINCIPLES.md
- CHARTER.md

## Referenced by

- Future Telegram graphic specifications
- TELEGRAM_PUBLISHING_MODEL.md (TJS-010)
- TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md (TJS-020)
- TELEGRAM_PUBLICATION_LIFECYCLE.md (TJS-021)

---

**End of Specification**
