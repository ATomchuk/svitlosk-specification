# Telegram Architecture Decision

**Date:** 2026-07-13
**Status:** Approved
**Document Class:** Architecture Decision Record
**Author:** SvitloSk Project

---

# Purpose

This document defines the approved architecture of the Telegram documentation subsystem. It is the canonical architectural definition for all Telegram Journal Specification (TJS) documents.

This document supersedes every previous proposal, audit, review, and recommendation regarding Telegram documentation architecture.

---

# Architectural Status

This document becomes the authoritative architectural definition for the Telegram documentation subsystem.

All previous audits (Semantic Responsibility Audit, Architectural Evidence Audit, Architecture Review) remain historical evidence only. They informed the decisions recorded here but do not govern future architecture.

This document governs.

---

# Approved Document Set

The Telegram documentation subsystem consists of exactly 7 documents.

---

## TJS-001 — Journal Concept

**Document ID:** TJS-001

**Document Name:** Journal Concept

**Primary Responsibility:** Defines the identity, mission, principles, audience and role of the official SvitloSk Telegram Journal.

**Owns:**
- Journal identity (what it is, what it is NOT)
- Journal mission and vision
- Core principles (Respect for data, Accuracy, Clarity, Automation, Transparency, Consistency, Availability, Chronological integrity, Community-first)
- Audience definition
- Role within SvitloSk ecosystem
- Editorial philosophy
- Historical archive concept

**Does NOT own:**
- Editorial rules (TJS-002)
- Publication templates (TJS-003)
- Rendering rules (TJS-004)
- Publication lifecycle (TJS-005)
- Channel management (TJS-006)
- Graphic rendering (TJS-007)
- Any implementation details

**Document Class:** Normative

**Status:** RETAINED (update §12, add Document Class, add References, fix lowercase RFC 2119)

**Dependencies:** None (foundational document)

**Referenced by:** TJS-002, TJS-003, TJS-004, TJS-005, TJS-006, TJS-007 (all implicitly)

---

## TJS-002 — Editorial Policy

**Document ID:** TJS-002

**Document Name:** Editorial Policy

**Primary Responsibility:** Defines the editorial standards, formatting policy, territory presentation rules and permitted formatting types for all text publications in the Telegram Journal.

**Owns:**
- Editorial principles (Territory-first, One post — one territory, Maximum readability, Minimal formatting, Consistent structure, No decorative elements, Automatic generation)
- Territory presentation rules (uppercase, first element)
- Publication package composition
- Message categories and ordering (Planned, Emergency)
- Category title formatting (emoji indicators, bold)
- Time format rules (emoji + HH:MM–HH:MM)
- Settlement formatting policy (bold, no prefix)
- Address formatting policy (preserve abbreviations, line by line)
- Permitted formatting types (bold + plain text only; italic, underline, spoiler, blockquote, code blocks prohibited)
- Update timestamp convention
- Branding rules (no signatures, no separators, no location icons)
- Terminology governance (Outage term)
- Formatting POLICY (what is permitted)

**Does NOT own:**
- Journal identity (TJS-001)
- Publication templates (TJS-003)
- Rendering pipeline (TJS-004)
- Publication lifecycle (TJS-005)
- Channel management (TJS-006)
- Graphic rendering (TJS-007)
- Formatting IMPLEMENTATION (TJS-003)
- Detailed template structure (TJS-003)

**Document Class:** Normative

**Status:** RETAINED (current ID; add Document Class, add References, remove Component field)

**Dependencies:** TJS-001 (implicit), TERRITORIAL_MODEL.md

**Referenced by:** TJS-003 (declared), TJS-004 (implicit)

---

## TJS-003 — Message Templates

**Document ID:** TJS-003

**Document Name:** Message Templates

**Primary Responsibility:** Defines the canonical publication templates, structural grammar, hierarchy, formatting implementation and validation rules for every Telegram Publication.

**Owns:**
- Canonical publication templates (Template A: City Today, Template B: District Today, Template C: City Tomorrow, Template D: District Tomorrow)
- Structural grammar (Publication → Territory Header → Sections → Settlement → Time → Street → Addresses)
- Publication structure (absorbed from TJS-003 Post Structure: Header, Main Information, Graphic Block, Additional Information, Footer)
- Territory header rules (uppercase, abbreviated or full name)
- Section ordering rules (Planned before Emergency, empty sections not rendered)
- Settlement ordering (canonical TERRITORIAL_MODEL.md order; alphabetical sorting prohibited)
- Time interval ordering (sorted by start time)
- Time interval formatting (single-day: 🕘 HH:MM–HH:MM; multi-day: dates)
- Settlement formatting implementation (bold with `<b>` tag, no administrative prefixes)
- Street formatting (new line, preserve Ukrainian abbreviations)
- Address rules (one line per street, no duplicates, repeat across time intervals)
- Validation rules (prohibitions list)
- Formatting IMPLEMENTATION (bold with `<b>` tag; block quotes MAY be used by future specs)
- Graphic Block concept (absorbed from TJS-003 Post Structure §6)
- Additional Information concept (absorbed from TJS-003 Post Structure §7)
- Footer concept (absorbed from TJS-003 Post Structure §8)
- Editing rules (absorbed from TJS-003 Post Structure §10: factual/layout corrections permitted)

**Does NOT own:**
- Journal identity (TJS-001)
- Editorial policy (TJS-002) — TJS-003 IMPLEMENTS TJS-002's rules
- Rendering pipeline (TJS-004)
- Publication lifecycle (TJS-005)
- Channel management (TJS-006)
- Graphic rendering (TJS-007)
- Formatting POLICY (TJS-002)

**Document Class:** Normative

**Status:** RETAINED (current ID; absorb TJS-003 Post Structure; fix metadata)

**Dependencies:** TJS-001 (implicit), TJS-002 (declared), TERRITORIAL_MODEL.md

**Referenced by:** TJS-004, TJS-005, TJS-007

---

## TJS-004 — Rendering Rules

**Document ID:** TJS-004

**Document Name:** Rendering Rules

**Primary Responsibility:** Defines the canonical rendering pipeline that transforms normalized data into deterministic Telegram HTML output.

**Owns:**
- Rendering pipeline (Validation → Sorting → Grouping → Duplicate Removal → Formatting → HTML Escaping → Length Validation → Telegram HTML)
- Rendering principles (Deterministic, Canonical Equality, Human Readability, Minimal Formatting, Stable Ordering, Source Fidelity)
- Territory ordering (Administrative Centre first, Starosta Districts alphabetical)
- Time ordering (sorted by start time)
- Settlement ordering (alphabetically using Ukrainian alphabet — DEFERRED: subject to ADR)
- Street ordering (Natural Sort)
- Building number ordering (Natural Sort)
- Duplicate removal (no duplicate addresses)
- Long publication split (split between complete Settlement blocks)
- HTML rendering rules (allowed tags: `<b>`, `<br>`; escape reserved characters; UTF-8; no trailing whitespace)
- Stable output rule (no cosmetic changes; formatting changes only when dataset or spec changes)
- Empty block rule (no empty sections)
- Validation rules (valid HTML, closed tags, valid UTF-8, deterministic ordering, no duplicates, no empty sections, length within limits)
- Error handling (logged, prevent publication, preserve previously published)

**Does NOT own:**
- Journal identity (TJS-001)
- Editorial policy (TJS-002)
- Publication templates (TJS-003)
- Publication lifecycle (TJS-005)
- Channel management (TJS-006)
- Graphic rendering (TJS-007)
- Formatting POLICY (TJS-002)

**Document Class:** Normative

**Status:** RETAINED (current ID; fix metadata, fix incorrect reference "TJS-003 — Editorial Policy" → "TJS-002 — Editorial Policy")

**Dependencies:** TJS-001 (implicit), TJS-002 (implicit), TJS-003 (declared), SSP-003 (Publication Engine), TERRITORIAL_MODEL.md

**Referenced by:** TJS-005

---

## TJS-005 — Publication Lifecycle

**Document ID:** TJS-005

**Document Name:** Publication Lifecycle

**Primary Responsibility:** Defines the complete lifecycle of Publications within the SvitloSk Telegram Journal — from creation through rendering, publication, update, retention, and removal.

**Owns:**
- Lifecycle state model (unified from TJS-002 §3, TJS-007 §3, TJS-008 §3)
- Publication type taxonomy (from TJS-002 §4: Daily schedule, Schedule update, Emergency outage notification, Emergency restoration notification, Informational notice, Technical notice, System status message)
- Daily schedule lifecycle flow (from TJS-002 §5)
- Emergency publication lifecycle flow (from TJS-002 §6)
- Temporary publication rules (from TJS-002 §7, TJS-007 §8, TJS-008 §12)
- Update rules (unified from TJS-002 §8, TJS-007 §5, TJS-008 §11)
- Archive policy (from TJS-002 §9)
- Deletion policy (from TJS-002 §10)
- Traceability (from TJS-002 §11)
- Reliability guarantees (from TJS-002 §12)
- Publication creation rules (from TJS-007 §4)
- Canonical equality check (from TJS-007 §6)
- Publication ordering (from TJS-007 §7)
- Temporary vs permanent classification (from TJS-007 §8-9)
- Publication ownership model (from TJS-007 §10)
- Non-destructive channel principle (from TJS-007 §11)
- Error handling (from TJS-007 §13)
- Daily publication cycle (from TJS-008 §3)
- Daily and Tomorrow publication packages (from TJS-008 §4-5)
- Publication windows (from TJS-008 §6)
- Event-driven publication principle (from TJS-008 §7)
- Stable journal principle (from TJS-008 §8)
- Deterministic daily journal principle (from TJS-008 §9)
- Non-destructive update principle (from TJS-008 §10)
- Manual publications exclusion (from TJS-008 §13)
- Image publications exclusion (from TJS-008 §14)
- Publication session concept (from TJS-008 §15)
- Lifecycle diagrams (consolidated from TJS-007 §12, TJS-008 §16-17)

**Does NOT own:**
- Journal identity (TJS-001)
- Editorial policy (TJS-002)
- Publication templates (TJS-003)
- Rendering pipeline (TJS-004)
- Channel management (TJS-006)
- Graphic rendering (TJS-007)
- Settlement ordering conflict (DEFERRED to ADR)

**Document Class:** Normative

**Status:** CREATED (merged from TJS-002 + TJS-007 + TJS-008)

**Dependencies:** TJS-001 (implicit), TJS-002 (implicit), TJS-003 (declared), TJS-004 (declared), TERRITORIAL_MODEL.md, DATA_MODEL.md, SSP-002 (Parser), SSP-003 (Publication Engine)

**Referenced by:** TJS-006, TJS-007, future Scheduler, future Telegram Publisher

---

## TJS-006 — Channel Management

**Document ID:** TJS-006

**Document Name:** Channel Management

**Primary Responsibility:** Defines the Telegram Bot API integration rules, rate limiting, message editing constraints and channel administration interaction.

**Owns:**
- Telegram Bot API integration rules
- Rate limiting and API constraints
- Message editing rules (Telegram-specific)
- Channel administration interaction
- Error recovery at API level

**Does NOT own:**
- Journal identity (TJS-001)
- Editorial policy (TJS-002)
- Publication templates (TJS-003)
- Rendering pipeline (TJS-004)
- Publication lifecycle (TJS-005)
- Graphic rendering (TJS-007)

**Document Class:** Normative

**Status:** CREATED (new document — addresses gap identified in TELEGRAM_GAP_ANALYSIS.md)

**Dependencies:** TJS-001 (implicit), TJS-005 (declared), SSP-003 (Publication Engine)

**Referenced by:** future Telegram Publisher implementation

---

## TJS-007 — Graphic Rendering

**Document ID:** TJS-007

**Document Name:** Graphic Rendering

**Primary Responsibility:** Defines the graphic generation rules for Telegram publications, including image formats, size constraints, graphic-to-text pairing and validation.

**Owns:**
- Graphic generation rules for Telegram posts
- Image format requirements (PNG/SVG)
- Telegram image size constraints
- Graphic-to-text pairing rules
- Graphic validation rules

**Does NOT own:**
- Journal identity (TJS-001)
- Editorial policy (TJS-002)
- Publication templates (TJS-003)
- Rendering pipeline (TJS-004)
- Publication lifecycle (TJS-005)
- Channel management (TJS-006)

**Document Class:** Normative

**Status:** CREATED (new document — addresses gap identified in TELEGRAM_GAP_ANALYSIS.md)

**Dependencies:** TJS-001 (implicit), TJS-003 (declared), SSP-007 (Graphic Generator), SSP-003 (Publication Engine)

**Referenced by:** future Telegram Publisher implementation

---

# Approved Responsibility Matrix

One responsibility. One owner. No shared ownership.

| Responsibility | Owner | Evidence |
|---------------|-------|----------|
| Journal identity | TJS-001 | TJS-001 §1, §3, §9 |
| Journal mission | TJS-001 | TJS-001 §4 |
| Journal principles | TJS-001 | TJS-001 §7 |
| Editorial policy | TJS-002 | TJS-002 §1 |
| Formatting policy | TJS-002 | TJS-002 §11 (Formatting) |
| Territory rules | TJS-002 | TJS-002 §3 (Territory) |
| Publication templates | TJS-003 | TJS-003 §1, §13 |
| Publication structure | TJS-003 | TJS-003 §4 (Grammar), absorbed TJS-003 Post Structure §3-8 |
| Formatting implementation | TJS-003 | TJS-003 §15 |
| Validation rules | TJS-003 | TJS-003 §14 |
| Rendering pipeline | TJS-004 | TJS-004 §1, §4 |
| Sorting algorithms | TJS-004 | TJS-004 §5-8 |
| HTML generation | TJS-004 | TJS-004 §11 |
| Lifecycle states | TJS-005 | TJS-005 (merged from TJS-002 §3, TJS-007 §3, TJS-008 §3) |
| Update rules | TJS-005 | TJS-005 (merged from TJS-002 §8, TJS-007 §5, TJS-008 §11) |
| Publication types | TJS-005 | TJS-005 (from TJS-002 §4) |
| Ownership model | TJS-005 | TJS-005 (from TJS-007 §10) |
| Non-destructive principles | TJS-005 | TJS-005 (from TJS-007 §11, TJS-008 §10) |
| Daily cycle | TJS-005 | TJS-005 (from TJS-008 §3) |
| Publication windows | TJS-005 | TJS-005 (from TJS-008 §6) |
| Archive policy | TJS-005 | TJS-005 (from TJS-002 §9) |
| Deletion policy | TJS-005 | TJS-005 (from TJS-002 §10) |
| Traceability | TJS-005 | TJS-005 (from TJS-002 §11) |
| Error handling | TJS-005 | TJS-005 (from TJS-007 §13) |
| Channel management | TJS-006 | TJS-006 §1 |
| Graphic rendering | TJS-007 | TJS-007 §1 |

---

# Approved Dependency Graph

Dependencies flow in one direction. No cycles are permitted.

```text
TJS-001 (Journal Concept)
    │
    └──→ TJS-002 (Editorial Policy)
              │
              └──→ TJS-003 (Message Templates)
                        │
                        ├──→ TJS-004 (Rendering Rules)
                        │        │
                        │        └──→ TJS-005 (Publication Lifecycle)
                        │                 │
                        │                 ├──→ TJS-006 (Channel Management)
                        │                 │
                        │                 └──→ TJS-007 (Graphic Rendering)
                        │
                        └──→ TJS-007 (Graphic Rendering)
```

**Dependency Rules:**
- TJS-001 has no dependencies (foundational)
- TJS-002 depends on TJS-001 (implicit)
- TJS-003 depends on TJS-002 (declared), TJS-001 (implicit)
- TJS-004 depends on TJS-003 (declared), TJS-002 (implicit), TJS-001 (implicit)
- TJS-005 depends on TJS-004 (declared), TJS-003 (declared), TJS-002 (implicit), TJS-001 (implicit)
- TJS-006 depends on TJS-005 (declared), TJS-001 (implicit)
- TJS-007 depends on TJS-003 (declared), TJS-001 (implicit)

**External dependencies:**
- TJS-003 depends on TERRITORIAL_MODEL.md
- TJS-004 depends on SSP-003 (Publication Engine), TERRITORIAL_MODEL.md
- TJS-005 depends on DATA_MODEL.md, TERRITORIAL_MODEL.md, SSP-002 (Parser), SSP-003 (Publication Engine)
- TJS-006 depends on SSP-003 (Publication Engine)
- TJS-007 depends on SSP-007 (Graphic Generator), SSP-003 (Publication Engine)

**Circular dependency check:** NONE. Dependency graph is acyclic.

---

# Approved Architectural Decisions

---

## AD-001: Publication Lifecycle Merge

**Decision ID:** AD-001

**Decision:** TJS-002 (Publication Lifecycle), TJS-007 (Publication Lifecycle) and TJS-008 (Publication Lifecycle) SHALL be merged into a single document: TJS-005 (Publication Lifecycle).

**Reason:** Three documents defined the same responsibility ("Publication Lifecycle") with conflicting state models (6 states, 5 states, 6 steps), conflicting update rules (3 conditions, 2 conditions, 2 conditions), and conflicting temporary publication definitions (3 types, 1 type, 1 type). This violated SSOT, SRP, and Separation of Concerns.

**Evidence Source:** CF-001 (Architecture Review), EB-001, EB-002, EB-003 (Evidence Audit), F-001, F-002, F-003 (Semantic Audit)

**Affected Documents:** TJS-002 (removed), TJS-007 (removed), TJS-008 (removed), TJS-005 (created)

**Implementation Required:** YES

**Expected Repository Impact:** 3 files removed, 1 file created. All cross-references to TJS-002, TJS-007, TJS-008 must be updated.

---

## AD-002: Post Structure Absorption

**Decision ID:** AD-002

**Decision:** TJS-003 (Post Structure) SHALL be absorbed into TJS-003 (Message Templates). The current TJS-003 (Post Structure) file SHALL be removed.

**Reason:** TJS-003 (Post Structure) and TJS-005 (Message Templates) both defined "publication structure" with different terminology (5 sections vs grammar tree). TJS-005 is more detailed (405 lines vs 140 lines), more normative, and already covers all structural concepts. TJS-003's unique content (Graphic block, Additional information, Footer, Editing rules) is absorbed as additional sections.

**Evidence Source:** CF-002 (Architecture Review), EB-005 (Evidence Audit), F-005 (Semantic Audit)

**Affected Documents:** TJS-003 Post Structure (removed), TJS-003 Message Templates (updated to absorb content)

**Implementation Required:** YES

**Expected Repository Impact:** 1 file removed. TJS-003 (Message Templates) gains 4 additional sections.

---

## AD-003: Formatting Hierarchy

**Decision ID:** AD-003

**Decision:** TJS-002 (Editorial Policy) SHALL own formatting POLICY. TJS-003 (Message Templates) SHALL own formatting IMPLEMENTATION. TJS-003 (Post Structure) §9 formatting rules SHALL be absorbed into TJS-002.

**Reason:** Three documents defined "formatting rules" with different criteria: TJS-003 §9 (general principles), TJS-004 §11 (permitted types), TJS-005 §15 (HTML implementation). TJS-004 is the only Approved document and already owns the formatting policy. TJS-005 explicitly depends on TJS-004. The policy/implementation split is architecturally sound.

**Evidence Source:** CF-003 (Architecture Review), EB-006 (Evidence Audit), F-006 (Semantic Audit)

**Affected Documents:** TJS-002 (absorbs TJS-003 §9), TJS-003 (retains §15 implementation)

**Implementation Required:** YES

**Expected Repository Impact:** TJS-002 gains formatting rules from TJS-003 §9. No file changes beyond absorption.

---

## AD-004: TJS-002 Unique Content Absorption

**Decision ID:** AD-004

**Decision:** TJS-002 (Publication Lifecycle) unique content SHALL be absorbed into TJS-005 (Publication Lifecycle). The current TJS-002 (Publication Lifecycle) file SHALL be removed.

**Reason:** TJS-002 is an orphan document (not referenced by any other TJS). Its unique content (publication types, archive policy, deletion policy, traceability, reliability) has no owner if TJS-002 is removed. This content belongs in the lifecycle document.

**Evidence Source:** CF-005 (Architecture Review), EB-011 (Evidence Audit), F-011 (Semantic Audit), DEPENDENCY_MAP

**Affected Documents:** TJS-002 Publication Lifecycle (removed), TJS-005 (absorbs unique content)

**Implementation Required:** YES

**Expected Repository Impact:** 1 file removed. TJS-005 gains publication types, archive policy, deletion policy, traceability, and reliability sections.

---

## AD-005: Cross-Reference Correction

**Decision ID:** AD-005

**Decision:** Incorrect cross-references SHALL be corrected during restructuring.

**Reason:** Two documents contain incorrect cross-references that create confusion:
- TJS-006 §17 references "TJS-003 — Editorial Policy" but TJS-003 is "Post Structure"
- TJS-008 §18 references "TJS-007 — Channel Management" but TJS-007 is "Publication Lifecycle"

**Evidence Source:** CF-008 (Architecture Review), DEPENDENCY_MAP, INVENTORY

**Affected Documents:** TJS-006 (fix §17 reference), TJS-008 (fix §18 reference — or remove if TJS-008 is merged)

**Implementation Required:** YES

**Expected Repository Impact:** 2 reference corrections. After AD-001 merge, TJS-008 is removed, so only TJS-006 §17 requires correction.

---

## AD-006: Metadata Standardization

**Decision ID:** AD-006

**Decision:** All TJS documents SHALL have standard repository metadata: Document Class, References section, uppercase RFC 2119 keywords.

**Reason:** All 8 current TJS documents lack standard metadata. TJS-005 and TJS-006 use non-standard fields ("Project", "Class"). TJS-001, TJS-002, TJS-003, TJS-004 lack References sections. TJS-001, TJS-002, TJS-003 use lowercase RFC 2119 keywords.

**Evidence Source:** CF-009 (Architecture Review), INVENTORY, GAP_ANALYSIS

**Affected Documents:** All 7 approved documents

**Implementation Required:** YES

**Expected Repository Impact:** Metadata updates across all documents.

---

## AD-007: No Renumbering

**Decision ID:** AD-007

**Decision:** Existing TJS document IDs SHALL be retained. No renumbering SHALL occur.

**Reason:** The original proposal renumbered TJS-004 → TJS-002, TJS-005 → TJS-003, TJS-006 → TJS-004. This changes the identity of the only Approved document (TJS-004) and the most detailed document (TJS-005). Both audits recommend no renumbering.

**Evidence Source:** C-004 (Architecture Review), D-006 (Decision Report), SEMANTIC_FINAL_REPORT, EVIDENCE_DECISION_REPORT

**Affected Documents:** All documents (IDs retained)

**Implementation Required:** NO (decision is to NOT renumber)

**Expected Repository Impact:** None. IDs stay the same.

---

## AD-008: 8 → 7 Architecture Approval

**Decision ID:** AD-008

**Decision:** The Telegram documentation subsystem SHALL consist of exactly 7 documents, down from 8.

**Reason:** The 8 → 7 reduction resolves all identified SSOT violations, eliminates the triple lifecycle duplication, absorbs the orphaned Post Structure, and creates new documents for missing areas (Channel Management, Graphic Rendering).

**Evidence Source:** D-006 (Decision Report), CF-001 through CF-010 (Architecture Review)

**Affected Documents:** All documents (architecture changes)

**Implementation Required:** YES

**Expected Repository Impact:** 3 files removed (TJS-002 Lifecycle, TJS-003 Post Structure, TJS-007 Lifecycle, TJS-008 Lifecycle), 3 files created (TJS-005 Lifecycle merged, TJS-006 Channel Management new, TJS-007 Graphic Rendering new), 4 files updated (TJS-001, TJS-002 Editorial, TJS-003 Templates, TJS-004 Rendering)

---

## AD-009: TJS-001 §12 Update

**Decision ID:** AD-009

**Decision:** TJS-001 §12 (Future Specifications) SHALL be updated to reflect actual and proposed document names.

**Reason:** TJS-001 §12 lists: TJS-005 as "Visual Identity", TJS-006 as "Automation", TJS-007 as "Moderation", TJS-008 as "Analytics". These do not match actual filenames or the approved architecture.

**Evidence Source:** CF-010 (Architecture Review), INVENTORY, GAP_ANALYSIS

**Affected Documents:** TJS-001

**Implementation Required:** YES

**Expected Repository Impact:** TJS-001 §12 updated with correct document names.

---

# Deferred Decisions

---

## DD-001: Settlement Ordering Resolution

**Finding:** CF-004 (Settlement Ordering Conflict)

**Reason:** TJS-005 §7 ("Alphabetical sorting is prohibited") and TJS-006 §7 ("Settlements SHALL be ordered alphabetically") define mutually exclusive rules. This conflict is confirmed with HIGH confidence but requires a design decision about which ordering is authoritative.

**Required Future Process:** Architecture Decision Record (ADR)

**Expected Resolution Mechanism:** An ADR must be created that determines:
- Whether TERRITORIAL_MODEL.md canonical order is the rendering order (Option A)
- Whether alphabetical order is the rendering order (Option B)
- Whether different scopes apply — content order vs rendering order (Option C)

**Note:** This ADR MUST be resolved before restructuring proceeds. The conflict affects both TJS-003 (Message Templates) and TJS-004 (Rendering Rules).

---

## DD-002: New Document Content Specification

**Finding:** TJS-006 (Channel Management) and TJS-007 (Graphic Rendering) — content not yet specified

**Reason:** The architectural decision to CREATE these documents is approved (AD-008), but their content is not yet specified. The responsibilities are proposed but not detailed.

**Required Future Process:** Document creation during restructuring

**Expected Resolution Mechanism:** TJS-006 and TJS-007 SHALL be authored during the restructuring phase, following the responsibility definitions in this document.

---

# Architecture Constraints

The following rules SHALL govern every future Telegram document:

1. **One responsibility — one owner.** No responsibility SHALL be defined authoritatively in more than one document.

2. **No duplicated lifecycle.** The Publication Lifecycle SHALL be owned exclusively by TJS-005. No other TJS document MAY define lifecycle states, update rules, or temporary/permanent classification.

3. **No duplicated formatting rules.** Formatting POLICY SHALL be owned exclusively by TJS-002. Formatting IMPLEMENTATION SHALL be owned exclusively by TJS-003. No other TJS document MAY define formatting rules.

4. **No duplicated message templates.** Publication templates SHALL be owned exclusively by TJS-003. No other TJS document MAY define canonical templates.

5. **SSOT preserved.** Every concept SHALL have exactly one authoritative definition.

6. **Dependency direction preserved.** Dependencies SHALL flow from TJS-001 downward. No circular dependencies are permitted.

7. **No architectural changes without Architecture Decision.** Any change to the document set, responsibilities, or dependency graph SHALL require an approved Architecture Decision.

8. **Metadata compliance.** Every TJS document SHALL have: Document Class, References section, uppercase RFC 2119 keywords.

9. **Glossary alignment.** Every TJS document SHALL use terminology defined by GLOSSARY.md. No TJS document MAY redefine repository terminology.

10. **One Document — One Subject.** Every TJS document SHALL define one complete subject area (PROJECT_PRINCIPLES P-10).

---

# Architecture Approval

This document supersedes every previous proposal regarding Telegram documentation architecture, including:

- TELEGRAM_ARCHITECTURE_PROPOSAL.md (superseded by AD-007: no renumbering)
- TELEGRAM_SEMANTIC_RESPONSIBILITY_FINAL_REPORT.md (superseded: findings consolidated into this document)
- TELEGRAM_ARCHITECTURAL_EVIDENCE_FINAL_REPORT.md (superseded: evidence consolidated into this document)
- TELEGRAM_ARCHITECTURAL_DECISION_REPORT.md (superseded: decisions approved in this document)

Previous audits remain historical evidence only. They informed the decisions recorded here but do not govern future architecture.

This document becomes the canonical architectural definition for the Telegram documentation subsystem.

---

**Architecture Status:** APPROVED

**Architect:** SvitloSk Certification Pipeline

**Date:** 2026-07-13

**End of Telegram Architecture Decision**
