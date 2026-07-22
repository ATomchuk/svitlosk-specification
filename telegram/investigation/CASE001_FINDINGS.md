# CASE001_FINDINGS

**Document ID:** CASE001-004

**Title:** Case Investigation №001 — Findings

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Investigation №001

---

# Purpose

This document records factual observations from the semantic core investigation of the Telegram Publishing Domain. Facts only. No interpretation. No recommendations. No conclusions.

---

# Finding F-001: Domain Split

The Telegram Publishing Domain contains concepts that exist independently of SvitloSk and concepts that exist only because SvitloSk exists.

**Source:** All normative documentation

---

# Finding F-002: Physical Reality Layer

The following concepts exist in physical/administrative reality regardless of any software:

- Starokostiantyniv Community
- Administrative Centre
- Starosta District
- Settlement
- Street
- Address
- Distribution System Operator
- Planned Power Outage
- Emergency Power Outage
- Outage Schedule
- Queue
- Subqueue
- Electricity Availability
- Availability Window
- Outage Window
- Open Data
- Data Source
- Residents
- Information Consumers

**Source:** CHARTER.md, GLOSSARY.md, TERRITORIAL_MODEL.md

---

# Finding F-003: Business Process Layer

The following concepts exist because SvitloSk chose to perform a specific editorial process:

- Journal
- Issue
- Publication
- Publication Channel
- Publication Package
- Editorial Policy
- Reporting Period
- Archive
- Territory (publication unit)
- Publisher Role
- Canonical Templates
- Source Fidelity
- Traceability
- Reliability
- Editorial Principles
- Territory Presentation
- Time Format
- Settlement Formatting
- Address Formatting
- Branding
- Publication Grammar
- Territory Header
- Publication Sections
- Graphic Clarity
- Graphic Branding
- Graphic Accessibility
- Graphic Color
- Daily Publication Cycle
- Formatting Rules

**Source:** TJS-000, TJS-000A, TJS-010, TJS-020, TJS-021, TJS-022

---

# Finding F-004: Software Implementation Layer

The following concepts exist only because software components exist:

- Publication Engine
- Parser
- Data Storage
- Schedule Generator
- Graphic Generator
- Telegram Publisher
- Publication Lifecycle States
- Telegram Message ID
- Rate Limiting
- Rendering Pipeline
- Deterministic Rendering
- Non-destructive Channel
- Non-destructive Update
- Publication Ownership
- Publication Session
- Publication Windows
- Canonical Equality
- Error Handling
- Validation Rules
- Long Publication Split
- HTML Rendering Rules
- Stable Output Rule
- Empty Block Rule
- Editing Rules
- Graphic Automation
- Graphic Format
- Graphic Validation
- Graphic Timeline
- Repository Authority
- Repository State
- Publication Lifecycle
- Graphic Publication
- Tomorrow Schedule Graphic
- Emergency Information Card
- Statistics Card
- Service Graphic

**Source:** TJS-010, TJS-021, TJS-022, SSP specifications

---

# Finding F-005: Semantic Hierarchy

The Telegram semantic hierarchy is:

Journal → Issue → Publication → Telegram

**Source:** TJS-000 §4

---

# Finding F-006: Platform Independence

Telegram is explicitly defined as the publication platform, NOT the Journal itself. The Journal exists independently from any publication platform.

**Source:** TJS-000 §3

---

# Finding F-007: Publication Types

Publications have the following type taxonomy:

- Text Publication
- Graphic Publication
- City Today (Template A)
- District Today (Template B)
- City Tomorrow (Template C)
- District Tomorrow (Template D)

**Source:** TJS-000A §9

---

# Finding F-008: Package Types

Publication Packages have the following types:

- Today's Package
- Tomorrow Package

**Source:** TJS-000A §9

---

# Finding F-009: Lifecycle States

Publications pass through the following states:

- Generated
- Published
- Updated
- Archived
- Removed

**Source:** TJS-000A §11, TJS-021 §4

---

# Finding F-010: Graphic Types

Graphic publications have the following types:

- T-001: Tomorrow Schedule Graphic
- T-003: Emergency Information Card
- T-004: Information Card
- T-005: Statistics Card
- T-006: Service Graphic

**Source:** TJS-022 §5

---

# Finding F-011: Ownership Boundaries

The Publishing System owns:

- Publication Engine: publication generation, distribution, ownership model, daily cycle, publication windows
- Parser: data retrieval, data validation, data normalization
- Publisher Role: publication preparation, generation, distribution
- Telegram Publisher: Telegram Bot API interaction, message delivery
- Schedule Generator: schedule generation, outage period calculation, daily schedules, change detection
- Graphic Generator: graphic generation, image format, size constraints
- Data Storage: persistent storage, historical preservation, metadata
- Telegram Channel: channel delivery, subscriber management, admin interaction

**Source:** TJS-010 §4, §8

---

# Finding F-012: What Publishing System Does NOT Own

The Publishing System does NOT own:

- Editorial decisions (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md)
- Publication lifecycle mechanics (TELEGRAM_PUBLICATION_LIFECYCLE.md)
- Graphic publication rules (TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md)
- Semantic terminology (TELEGRAM_SEMANTIC_MODEL.md)
- Glossary definitions (TELEGRAM_GLOSSARY.md)
- Telegram API integration (implementation)
- Rendering algorithms (implementation)
- Infrastructure (implementation)

**Source:** TJS-010 §8.2

---

# Finding F-013: Editorial Principles Count

The Editorial System is governed by 10 canonical principles:

1. Reader First
2. Editorial Truth
3. Editorial Silence
4. Minimal Editorial Intervention
5. Issue Integrity
6. Deterministic Editorial Behaviour
7. Territorial Organization
8. Consistency
9. Accessibility
10. Timeliness

**Source:** TJS-020 §4

---

# Finding F-014: Publishing Principles Count

The Publishing System is governed by 20 canonical principles.

**Source:** TJS-010 §6

---

# Finding F-015: Graphic Principles Count

The Graphic Publication Model is governed by 2 canonical principles:

1. Graphic Automation
2. Graphic Clarity

**Source:** TJS-022 §4

---

# Finding F-016: Color Semantics

Graphic publications use the following color semantics:

- Powered = Orange
- Outage = Dark Gray

No additional semantic colors are introduced.

**Source:** TJS-022 §8.3

---

# Finding F-017: Forbidden Terms

The Telegram Glossary defines forbidden terms with canonical replacements:

- Message → Publication / Telegram Message ID
- Post → Publication
- Telegram Message → Publication / Telegram Message ID
- Daily Page → Issue / Today's Package
- Publication Set → Publication Package
- Feed → Journal
- Page → Publication / Issue
- Coordinator → (not used)
- Workflow → Daily Publication Cycle / Processing Flow
- Working Repository → (not used)
- Historical Storage → Archive
- Journal Finality → (not used)
- Repository → (not used)
- History → Archive
- System Publication → Publication
- Starostyn District → Starosta District

**Source:** TJS-000A §17

---

# Finding F-018: Territorial Hierarchy

The canonical territorial hierarchy is:

```
Community
├── Administrative Centre
│     └── Urban Area
│           └── Street
│                 └── Address
└── Starosta District
      └── Settlement
            └── Street
                  └── Address
```

**Source:** TERRITORIAL_MODEL.md

---

# Finding F-019: Data Flow

The canonical data flow is:

External Data Sources → Parser → Normalized Dataset → Publication Engine → Publication Package → Telegram Publisher → Telegram Channel → Subscribers

**Source:** TJS-010 §3.3

---

# Finding F-020: Component Interactions

The following component interactions are approved:

- Parser → Publication Engine: Normalized Dataset
- Parser → Data Storage: Normalized Dataset
- Publication Engine → Telegram Publisher: Publication Package
- Publication Engine → Data Storage: Publication
- Publication Engine → Schedule Generator: Schedule Request
- Publication Engine → Graphic Generator: Graphic Request
- Telegram Publisher → Telegram Channel: Publication
- Telegram Channel → Subscribers: Publication
- Administrators → Telegram Channel: Manual Publication
- Administrators → Telegram Channel: Image Publication
- Publication Engine → Telegram Channel: Publication (owned)

**Source:** TJS-010 §5.1

---

# Finding F-021: Illegal Interactions

The following component interactions are illegal:

- Publication Engine → Manual Publications
- Publication Engine → Image Publications
- Publication Engine → Other publisher's Publications
- Parser → Publication Engine (reinterpretation)
- Publication Engine → Parser
- Subscribers → Telegram Channel (write)
- Any component → Glossary (modify)

**Source:** TJS-010 §5.2

---

# Finding F-022: Repository Authority Principle

Repository SHALL be the single authoritative source of truth for the publication state of the Telegram Journal. Telegram SHALL only represent the current Repository state. In the event of any conflict, Repository state SHALL prevail.

**Source:** TJS-021 §3.1

---

# Finding F-023: Non-Destructive Principles

Two non-destructive principles are defined:

1. Non-destructive Channel: Publisher SHALL modify only Publications it owns
2. Non-destructive Update: Updates SHOULD modify existing Publications instead of replacing

**Source:** TJS-000A, TJS-021 §7

---

# Finding F-024: Graphic Invariants

Graphic publication invariants include:

- Identity: unique publication identity, exactly one type, exactly one territory
- Content: faithful representation, no factual change, required metadata
- Visual: approved layout, official branding, approved colors, readable on all displays
- Temporal: deterministic for identical input, traceable to source, identity preserved across updates

**Source:** TJS-022 §9

---

# Finding F-025: Graphic Constraints Count

The Graphic Publication Model defines 7 mandatory constraints:

- C-001: Graphic Branding
- C-002: Graphic Accessibility
- C-003: Graphic Color
- C-004: Graphic Automation Trigger
- C-005: Graphic Format
- C-006: Graphic Validation
- C-007: Graphic Timeline

**Source:** TJS-022 §11

---

# End of Document
