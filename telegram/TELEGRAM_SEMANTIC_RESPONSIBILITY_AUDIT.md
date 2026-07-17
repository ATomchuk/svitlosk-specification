# Telegram Semantic Responsibility Audit

**Date:** 2026-07-13
**Scope:** All 14 documents in telegram/ (8 TJS specifications + 6 analysis documents)
**Methodology:** Semantic responsibility analysis (identical to Pipeline Semantic Duplication Audit)
**Constraint:** Repository remains unchanged. Analysis only.

---

## Audit Principle

This audit evaluates **Semantic Responsibility** — not wording, not section names, not terminology.

For every document:
1. Primary Responsibility (one sentence)
2. Secondary Responsibilities (if any)
3. Architectural Boundary (what belongs, what does NOT belong)
4. Can another document legitimately contain similar information? (YES / PARTIALLY / NO)

---

# Part 1: Individual Document Responsibility Analysis

---

## TJS-001 — Journal Concept

**Primary Responsibility:** Defines the identity, mission, principles, audience and role of the official SvitloSk Telegram Journal.

**Secondary Responsibilities:** Establishes the foundational editorial philosophy (§6) and the historical archive concept (§11).

**Architectural Boundary:**

BELONGS:
- Journal identity (what it is, what it is NOT)
- Journal mission and vision
- Core principles (Respect for data, Accuracy, Clarity, Automation, Transparency, etc.)
- Audience definition
- Role within SvitloSk ecosystem
- Future specifications list (§12)

DOES NOT BELONG:
- Detailed editorial rules (TJS-004)
- Publication lifecycle mechanics (TJS-002/007/008)
- Post structure (TJS-003)
- Templates (TJS-005)
- Rendering rules (TJS-006)
- Any implementation details

**Can another TJS document legitimately contain similar information?**
**NO.** Journal identity is a unique, foundational responsibility. No other document can own this.

**Overlap Assessment:** No other TJS document defines journal identity, mission or principles. TJS-004 references "Editorial Principles" but these are editorial rules, not journal-level principles.

---

## TJS-002 — Publication Lifecycle

**Primary Responsibility:** Defines the complete lifecycle of publications within the Telegram Journal, including lifecycle states, publication types, update rules, archive policy and deletion policy.

**Secondary Responsibilities:**
- Publication type taxonomy (§4) — 7 categories
- Archive policy (§9) — historical record preservation
- Deletion policy (§10) — what may and may not be deleted
- Traceability (§11) — source, timestamp, generator version
- Reliability guarantees (§12) — no duplicates, correct targeting

**Architectural Boundary:**

BELONGS:
- Publication lifecycle states (Generated → Scheduled → Published → Updated → Archived → Removed)
- Publication type taxonomy
- Daily schedule lifecycle
- Emergency publication lifecycle
- Temporary publication rules
- Update rules
- Archive policy
- Deletion policy
- Traceability requirements
- Reliability guarantees

DOES NOT BELONG:
- Journal identity (TJS-001)
- Post structure (TJS-003)
- Templates (TJS-005)
- Rendering (TJS-006)
- Daily publication cycle scheduling (TJS-008)
- Publication windows (TJS-008)
- Publication ownership (TJS-007)
- Non-destructive channel principle (TJS-007)

**Can another TJS document legitimately contain similar information?**
**PARTIALLY.** The lifecycle CONCEPT is foundational and shared. However, the specific operational details (publication types, archive policy, deletion policy) are unique to this document. TJS-007 and TJS-008 contain overlapping but NOT identical content.

---

## TJS-003 — Post Structure

**Primary Responsibility:** Defines the official structural format of publications (Header, Main Info, Graphic, Additional Info, Footer).

**Secondary Responsibilities:**
- Formatting rules (§9)
- Editing rules (§10)

**Architectural Boundary:**

BELONGS:
- Standard publication structure (5 sections)
- Header definition
- Main information definition
- Graphic block definition
- Additional information definition
- Footer definition
- Editing rules (post-publication corrections)

DOES NOT BELONG:
- Detailed canonical templates (TJS-005)
- Editorial policy (TJS-004)
- Rendering pipeline (TJS-006)
- Lifecycle mechanics (TJS-002/007/008)
- Detailed formatting rules (TJS-004 §9, TJS-005 §15)

**Can another TJS document legitimately contain similar information?**
**PARTIALLY.** TJS-005 (Message Templates) contains a more detailed and normative version of the same structural concept (§4 Publication Grammar). TJS-005's structure is more authoritative and implementation-ready. TJS-003 provides a conceptual overview while TJS-005 provides the normative specification.

**Overlap Assessment:** TJS-003 §3-8 (structure) overlaps with TJS-005 §4-12 (grammar, sections, hierarchy). TJS-005 is more detailed and normative.

---

## TJS-004 — Editorial Policy

**Primary Responsibility:** Defines the editorial standards governing all text publications in the Telegram Journal.

**Secondary Responsibilities:**
- Territory presentation rules (§3)
- Publication package composition (§4)
- Message categories and ordering (§5)
- Category title formatting (§6)
- Time format rules (§8)
- Settlement formatting (§9)
- Address formatting (§10)
- Permitted formatting (§11)
- Update timestamp convention (§12)
- Branding rules (§13)
- Terminology governance (§14)

**Architectural Boundary:**

BELONGS:
- Editorial principles (Territory-first, One post — one territory, Maximum readability, etc.)
- Territory presentation rules
- Publication package composition
- Message categories and ordering
- Category title formatting
- Time format rules
- Settlement formatting rules
- Address formatting rules
- Permitted formatting types
- Update timestamp convention
- Branding rules
- Terminology governance (Outage term)

DOES NOT BELONG:
- Journal identity (TJS-001)
- Detailed canonical templates (TJS-005)
- Rendering pipeline (TJS-006)
- Lifecycle mechanics (TJS-002/007/008)
- Publication structure (TJS-003) — editorial POLICY, not structure

**Can another TJS document legitimately contain similar information?**
**PARTIALLY.** TJS-005 contains implementation-level formatting rules (§9 Time Interval Formatting, §10 Settlement Formatting, §11-12 Street/Address Rules, §15 Formatting Rules). These implement TJS-004's editorial rules. The question is whether TJS-004 and TJS-005 duplicate the SAME responsibility or whether TJS-004 owns the POLICY and TJS-005 owns the IMPLEMENTATION.

---

## TJS-005 — Message Templates

**Primary Responsibility:** Defines the canonical publication templates, structural grammar, hierarchy, formatting and validation rules for every Telegram Publication.

**Secondary Responsibilities:**
- Publication grammar tree (§4)
- Territory header rules (§5)
- Section ordering rules (§6)
- Settlement ordering (§7)
- Time interval ordering and formatting (§8-9)
- Settlement formatting (§10)
- Street and address formatting (§11-12)
- 4 canonical templates: City Today, District Today, City Tomorrow, District Tomorrow (§13)
- Validation rules (§14)
- Formatting rules (§15)

**Architectural Boundary:**

BELONGS:
- Canonical publication templates (A, B, C, D)
- Structural grammar (Publication → Territory Header → Sections → Settlement → Time → Street → Addresses)
- Settlement ordering (canonical from TERRITORIAL_MODEL.md)
- Time interval ordering and formatting
- Street and address formatting with examples
- Template-specific rules (Tomorrow = no Update Time)
- Validation rules (prohibitions list)

DOES NOT BELONG:
- Journal identity (TJS-001)
- Editorial policy principles (TJS-004) — TJS-005 IMPLEMENTS them
- Rendering pipeline (TJS-006) — TJS-005 defines WHAT, TJS-006 defines HOW
- Lifecycle mechanics (TJS-002/007/008)
- Post structure overview (TJS-003) — subsumed by TJS-005

**Can another TJS document legitimately contain similar information?**
**NO.** The canonical templates are a unique, normative responsibility. TJS-003's structural overview is less detailed and can be subsumed.

---

## TJS-006 — Telegram Rendering Rules

**Primary Responsibility:** Defines the canonical rendering pipeline that transforms normalized data into deterministic Telegram HTML output.

**Secondary Responsibilities:**
- Rendering principles (Deterministic, Canonical Equality, Human Readability, Minimal Formatting, Stable Ordering, Source Fidelity)
- Territory ordering (§5)
- Time ordering (§6)
- Settlement ordering (§7) — alphabetical
- Street ordering (§8) — Natural Sort
- Duplicate removal (§9)
- Long publication split (§10)
- HTML rendering rules (§11)
- Stable output rule (§12)
- Empty block rule (§13)
- Validation rules (§14)
- Error handling (§15)

**Architectural Boundary:**

BELONGS:
- Rendering pipeline (Validation → Sorting → Grouping → Duplicate Removal → Formatting → HTML Escaping → Length Validation → Telegram HTML)
- Deterministic rendering principle
- Canonical equality principle
- Sorting algorithms (territory, time, settlement, street)
- HTML tag restrictions (<b>, <br> only)
- Publication splitting rules
- Error handling during rendering

DOES NOT BELONG:
- Journal identity (TJS-001)
- Editorial policy (TJS-004)
- Templates (TJS-005) — TJS-006 defines HOW to render, TJS-005 defines WHAT to render
- Lifecycle mechanics (TJS-002/007/008)
- Post structure (TJS-003)

**Can another TJS document legitimately contain similar information?**
**NO.** The rendering pipeline is a unique technical responsibility. No other document defines the deterministic rendering process.

**Note on TJS-006 §7 (Settlement Ordering) vs TJS-005 §7 (Settlement Ordering):**
TJS-005 §7 says settlements follow canonical TERRITORIAL_MODEL.md order. TJS-006 §7 says settlements are ordered alphabetically using Ukrainian alphabet. These appear to CONTRADICT each other. This is a semantic conflict, not just duplication.

---

## TJS-007 — Publication Lifecycle

**Primary Responsibility:** Defines the operational lifecycle of Telegram Journal Publications — creation rules, update mechanics, ownership model, ordering, temporary vs permanent classification, and the non-destructive channel principle.

**Secondary Responsibilities:**
- Publication creation rules (§4) — one territory, one template, one rendering
- Canonical equality check (§6) — compare before updating
- Publication ordering (§7) — deterministic, alphabetical
- Temporary publications (§8) — Tomorrow Publications
- Permanent publications (§9) — current-day publications
- Publication ownership (§10) — Telegram Message ID based
- Non-destructive channel principle (§11) — Publisher only touches its own
- Lifecycle diagram (§12)
- Error handling (§13)

**Architectural Boundary:**

BELONGS:
- Publication creation rules
- Canonical equality check
- Publication ordering (deterministic)
- Temporary vs permanent classification
- Publication ownership model
- Non-destructive channel principle
- Lifecycle state diagram
- Error handling for lifecycle failures

DOES NOT BELONG:
- Journal identity (TJS-001)
- Publication type taxonomy (TJS-002 §4)
- Archive policy (TJS-002 §9)
- Deletion policy specifics (TJS-002 §10)
- Traceability (TJS-002 §11)
- Daily publication cycle scheduling (TJS-008)
- Publication windows (TJS-008)
- Event-driven principle (TJS-008)
- Stable journal principle (TJS-008)
- Deterministic daily journal principle (TJS-008)
- Publication session (TJS-008)

**Can another TJS document legitimately contain similar information?**
**PARTIALLY.** TJS-002 and TJS-008 overlap on lifecycle states and update rules. However, TJS-007 owns unique concepts: ownership model, non-destructive channel principle, canonical equality check.

---

## TJS-008 — Publication Lifecycle

**Primary Responsibility:** Defines the daily publication cycle — when publications are created, updated and removed throughout the reporting day, including scheduling, event-driven updates and Tomorrow Publication lifecycle.

**Secondary Responsibilities:**
- Daily publication cycle (§3) — 6-step cycle
- Daily publication package (§4) — Today's Package
- Tomorrow publication package (§5)
- Publication windows (§6) — 05:00, 12:00, throughout day, next day 05:00
- Event-driven publication principle (§7) — data triggers, not time
- Stable journal principle (§8) — visual stability
- Deterministic daily journal principle (§9) — identical input → identical output
- Non-destructive update principle (§10) — update in place
- Update policy (§11) — dataset or rendering change only
- Tomorrow publication lifecycle (§12)
- Manual publications (§13) — outside lifecycle
- Image publications (§14) — outside lifecycle
- Publication session (§15) — one execution = one state
- Daily lifecycle diagram (§16)
- Architecture diagram (§17)

**Architectural Boundary:**

BELONGS:
- Daily publication cycle (6-step)
- Today's Package and Tomorrow Package
- Publication windows (temporal scheduling)
- Event-driven principle
- Stable journal principle
- Deterministic daily journal principle
- Non-destructive update principle
- Update policy
- Tomorrow lifecycle
- Manual/Image publication exclusion
- Publication session concept
- Daily lifecycle diagram
- Architecture diagram

DOES NOT BELONG:
- Journal identity (TJS-001)
- Publication type taxonomy (TJS-002 §4)
- Archive policy (TJS-002 §9)
- Deletion policy (TJS-002 §10)
- Traceability (TJS-002 §11)
- Publication ownership (TJS-007 §10)
- Non-destructive channel principle (TJS-007 §11)
- Post structure (TJS-003)
- Templates (TJS-005)
- Rendering (TJS-006)

**Can another TJS document legitimately contain similar information?**
**PARTIALLY.** TJS-002 and TJS-007 overlap on lifecycle states and update rules. However, TJS-008 owns unique concepts: daily cycle, publication windows, event-driven principle, publication session.

---

## Analysis Documents (TELEGRAM_*)

These documents are analytical/meta documents, not specifications. They are excluded from the pairwise responsibility analysis but are referenced for context.

| Document | Responsibility |
|----------|---------------|
| TELEGRAM_DOCUMENT_INVENTORY | Complete inventory of all TJS documents |
| TELEGRAM_DOCUMENT_CLASSIFICATION | Classification and responsibility mapping |
| TELEGRAM_DOCUMENT_DEPENDENCY_MAP | Dependency relationships between documents |
| TELEGRAM_GAP_ANALYSIS | Identification of documentation gaps |
| TELEGRAM_ARCHITECTURE_PROPOSAL | Proposed 8→7 restructuring |
| TELEGRAM_EXECUTIVE_SUMMARY | Summary of all findings |

---

# Part 2: Pairwise Responsibility Analysis

---

## Analysis Method

For every pair of documents, identify overlapping content and classify as:
- (A) REAL SSOT VIOLATION — Two documents define the same authoritative responsibility
- (B) CONTEXTUAL REUSE — One document references another for explanation
- (C) HISTORICAL REFERENCE — Historical information intentionally repeated
- (D) REQUIRED EVIDENCE — Shared facts used as supporting evidence
- (E) NORMAL CROSS-DOCUMENT COOPERATION — Documents cooperate but responsibilities differ

---

## TJS-001 vs All Others

| Pair | Overlap | Classification |
|------|---------|---------------|
| TJS-001 ↔ TJS-002 | TJS-001 §6 (Editorial Philosophy) sets principles; TJS-002 implements lifecycle under those principles | (E) Normal cooperation — different responsibilities |
| TJS-001 ↔ TJS-003 | TJS-001 defines what journal IS; TJS-003 defines post structure | (E) Normal cooperation |
| TJS-001 ↔ TJS-004 | TJS-001 §7 (Core Principles); TJS-004 defines Editorial Principles | (B) CONTEXTUAL REUSE — TJS-004 derives from TJS-001's principles but defines editorial-specific rules |
| TJS-001 ↔ TJS-005 | TJS-001 establishes identity; TJS-005 implements templates | (E) Normal cooperation |
| TJS-001 ↔ TJS-006 | TJS-001 establishes identity; TJS-006 implements rendering | (E) Normal cooperation |
| TJS-001 ↔ TJS-007 | TJS-001 §11 (Historical Archive); TJS-007 §9 (Permanent Publications) | (B) CONTEXTUAL REUSE — TJS-007 implements the archive concept from TJS-001 |
| TJS-001 ↔ TJS-008 | TJS-001 establishes identity; TJS-008 implements daily cycle | (E) Normal cooperation |

**Verdict: TJS-001 has NO SSOT violations with any document.**

---

## TJS-002 vs TJS-007

| Overlapping Concept | TJS-002 | TJS-007 | Classification |
|--------------------|---------|---------|---------------|
| Lifecycle states | §3 (6 states: Generated, Scheduled, Published, Updated, Archived, Removed) | §3 (5 states: Dataset → Render → Publish → Update → Retain/Remove) | **(A) REAL SSOT VIOLATION** — both define the authoritative lifecycle state model |
| Update rules | §8 (3 conditions: source change, formatting, graphics) | §5 (2 conditions: dataset change, rendering change) | **(A) REAL SSOT VIOLATION** — both define when updates are permitted |
| Temporary publications | §7 (Tomorrow schedule, upcoming notice, maintenance reminder) | §8 (Tomorrow Publications only) | **(A) REAL SSOT VIOLATION** — both define what is temporary |
| Archive/Permanent | §9 (Archive Policy) | §9 (Permanent Publications) | **(A) REAL SSOT VIOLATION** — both define preservation rules |
| Deletion policy | §10 (Deletion prohibited for daily/emergency/official) | §8 (Only Tomorrow may be removed) | **(D) REQUIRED EVIDENCE** — same fact, used as supporting evidence |

**Unique to TJS-002:** Publication types (§4), Traceability (§11), Reliability (§12)
**Unique to TJS-007:** Creation rules (§4), Canonical equality (§6), Ordering (§7), Ownership (§10), Non-destructive channel principle (§11), Lifecycle diagram (§12), Error handling (§13)

**Verdict: 4 REAL SSOT VIOLATIONS. The lifecycle state model, update rules, temporary publications, and archive/permanent rules are each defined authoritatively in BOTH documents.**

---

## TJS-002 vs TJS-008

| Overlapping Concept | TJS-002 | TJS-008 | Classification |
|--------------------|---------|---------|---------------|
| Lifecycle states | §3 (6 states) | §3 (6-step daily cycle) | **(A) REAL SSOT VIOLATION** — both define lifecycle state models |
| Update rules | §8 (3 conditions) | §11 (2 conditions: dataset or rendering change) | **(A) REAL SSOT VIOLATION** — both define when updates are permitted |
| Temporary publications | §7 (Tomorrow + others) | §12 (Tomorrow only) | **(A) REAL SSOT VIOLATION** — both define temporary publication rules |
| Deletion policy | §10 (Prohibited for daily/emergency/official) | §12 (Delete obsolete Tomorrow) | **(D) REQUIRED EVIDENCE** — same fact in different context |

**Unique to TJS-002:** Publication types (§4), Archive policy (§9), Deletion policy (§10), Traceability (§11), Reliability (§12)
**Unique to TJS-008:** Daily package (§4-5), Publication windows (§6), Event-driven principle (§7), Stable journal principle (§8), Deterministic principle (§9), Non-destructive update (§10), Manual/Image publications (§13-14), Publication session (§15), Diagrams (§16-17)

**Verdict: 3 REAL SSOT VIOLATIONS.**

---

## TJS-007 vs TJS-008

| Overlapping Concept | TJS-007 | TJS-008 | Classification |
|--------------------|---------|---------|---------------|
| Lifecycle states | §3 (5 states) | §3 (6-step cycle) | **(A) REAL SSOT VIOLATION** — both define lifecycle state models |
| Update rules | §5 (2 conditions) | §11 (2 conditions) | **(A) REAL SSOT VIOLATION** — both define when updates are permitted |
| Temporary/Remove | §8 (Tomorrow only) | §12 (Tomorrow only) | **(A) REAL SSOT VIOLATION** — both define removal rules |
| Non-destructive principle | §11 (Non-destructive CHANNEL) | §10 (Non-destructive UPDATE) | **(B) CONTEXTUAL REUSE** — related but distinct principles |
| Ordering | §7 (Deterministic: Centre → Districts) | — (implicit in daily cycle) | (E) Normal cooperation |

**Unique to TJS-007:** Creation rules (§4), Canonical equality (§6), Ownership (§10), Non-destructive channel principle (§11), Lifecycle diagram (§12), Error handling (§13)
**Unique to TJS-008:** Daily cycle (§3), Daily/Tomorrow packages (§4-5), Publication windows (§6), Event-driven principle (§7), Stable journal principle (§8), Deterministic principle (§9), Manual/Image publications (§13-14), Publication session (§15), Diagrams (§16-17)

**Verdict: 3 REAL SSOT VIOLATIONS.**

---

## TJS-003 vs TJS-005

| Overlapping Concept | TJS-003 | TJS-005 | Classification |
|--------------------|---------|---------|---------------|
| Publication structure | §3 (5 sections: Header, Main, Graphic, Additional, Footer) | §4 (Grammar: Territory Header → Sections → Settlement → Time → Street → Addresses) | **(A) REAL SSOT VIOLATION** — both define the authoritative publication structure |
| Header definition | §4 (type, date, schedule) | §5 (Territory Header, uppercase) | **(A) REAL SSOT VIOLATION** — both define what the header contains |
| Main information | §5 (verified info from official data) | §6 (Sections: Planned, Emergency) | **(B) CONTEXTUAL REUSE** — TJS-003 is conceptual, TJS-005 is normative |
| Graphic block | §6 (optional, auto-generated) | — (not defined in templates) | (E) Normal — TJS-003 defines concept, future TJS-007 will define rendering |
| Formatting rules | §9 (short paragraphs, spacing, emoji, typography) | §15 (bold only, no other formatting) | **(A) REAL SSOT VIOLATION** — both define formatting rules |
| Editing rules | §10 (factual/layout corrections permitted) | — (not in scope) | (E) Normal — different scope |

**Unique to TJS-003:** Graphic block concept (§6), Additional information (§7), Footer concept (§8), Editing rules (§10)
**Unique to TJS-005:** Canonical templates A-D (§13), Validation rules (§14), Detailed grammar tree (§4), Settlement ordering (§7), Time interval rules (§8-9), Street/address rules (§11-12)

**Verdict: 3 REAL SSOT VIOLATIONS. TJS-005 is more detailed and normative. TJS-003's content can be subsumed.**

---

## TJS-004 vs TJS-005

| Overlapping Concept | TJS-004 | TJS-005 | Classification |
|--------------------|---------|---------|---------------|
| Territory presentation | §3 (uppercase, first element) | §5 (uppercase Territory Header) | **(D) REQUIRED EVIDENCE** — TJS-005 implements TJS-004's rule |
| Time format | §8 (emoji + HH:MM–HH:MM) | §9 (single-day: 🕘 HH:MM–HH:MM; multi-day: dates) | **(D) REQUIRED EVIDENCE** — TJS-005 extends TJS-004's rule |
| Settlement formatting | §9 (bold, no prefix) | §10 (bold, no prefix, <b> tag) | **(D) REQUIRED EVIDENCE** — TJS-005 implements TJS-004's rule |
| Address formatting | §10 (preserve abbreviations, line by line) | §11-12 (preserve abbreviations, one line per street) | **(D) REQUIRED EVIDENCE** — TJS-005 implements TJS-004's rule |
| Formatting rules | §11 (bold + plain text only) | §15 (bold only, <b> tag) | **(D) REQUIRED EVIDENCE** — TJS-005 implements TJS-004's rule |
| Category titles | §6 (emoji indicators, bold) | §6 (emoji + Ukrainian labels) | **(D) REQUIRED EVIDENCE** — TJS-005 implements TJS-004's rule |
| Message categories | §5 (Planned, Emergency) | §6 (Planned, Emergency) | **(D) REQUIRED EVIDENCE** — same fact |
| Branding | §13 (no signatures, no separators) | — (not in scope) | (E) Normal — different scope |

**Verdict: NO REAL SSOT VIOLATIONS.** TJS-004 owns the POLICY; TJS-005 owns the IMPLEMENTATION. The overlaps are contextual reuse — TJS-005 references and implements TJS-004's rules with concrete examples and HTML tags.

**Critical Distinction:** TJS-004 says "bold; plain text" (policy level). TJS-005 says "bold (<b>); no other formatting" (implementation level). This is NORMAL cross-document cooperation, not duplication.

---

## TJS-004 vs TJS-003

| Overlapping Concept | TJS-004 | TJS-003 | Classification |
|--------------------|---------|---------|---------------|
| Formatting rules | §11 (bold + plain text) | §9 (short paragraphs, spacing, emoji, typography) | **(A) REAL SSOT VIOLATION** — both define formatting rules, with DIFFERENT content |

**Verdict: 1 REAL SSOT VIOLATION.** TJS-004 and TJS-003 both define formatting rules but with different specificity and content. This must be resolved.

---

## TJS-005 vs TJS-006

| Overlapping Concept | TJS-005 | TJS-006 | Classification |
|--------------------|---------|---------|---------------|
| Settlement ordering | §7 (canonical TERRITORIAL_MODEL.md order) | §7 (alphabetical, Ukrainian alphabet) | **CONFLICT** — these appear to CONTRADICT each other |
| Time ordering | §8 (sorted by start time) | §6 (sorted by start time) | (D) REQUIRED EVIDENCE — same fact |
| Duplicate removal | §12 (no duplicates) | §9 (no duplicates) | (D) REQUIRED EVIDENCE — same fact |
| Validation | §14 (prohibitions list) | §14 (pre-publication checks) | (E) Normal cooperation — different scope |

**Critical Finding:** TJS-005 §7 says settlements follow canonical TERRITORIAL_MODEL.md order. TJS-006 §7 says settlements are ordered alphabetically. These are CONTRADICTORY ordering rules. This is a semantic conflict that must be resolved.

**Verdict: 1 SEMANTIC CONFLICT (Settlement ordering). No additional SSOT violations.**

---

## TJS-006 vs TJS-007

| Overlapping Concept | TJS-006 | TJS-007 | Classification |
|--------------------|---------|---------|---------------|
| Error handling | §15 (rendering failures: logged, prevent publication) | §13 (lifecycle failures: never corrupt, never delete permanent) | (E) Normal cooperation — different error domains |
| Ordering | §5-8 (sorting algorithms) | §7 (publication order: Centre → Districts) | (E) Normal cooperation — different ordering concerns |

**Verdict: NO SSOT violations.**

---

## TJS-006 vs TJS-008

| Overlapping Concept | TJS-006 | TJS-008 | Classification |
|--------------------|---------|---------|---------------|
| Deterministic rendering | §3 (same input → same output) | §9 (same dataset → same journal) | (D) REQUIRED EVIDENCE — same principle at different levels |
| Error handling | §15 (rendering failures) | — (implicit) | (E) Normal cooperation |

**Verdict: NO SSOT violations.**

---

## TJS-007 vs TJS-008 (Detailed)

| Overlapping Concept | TJS-007 | TJS-008 | Classification |
|--------------------|---------|---------|---------------|
| Lifecycle diagram | §12 (Parser → Engine → Publisher → Create/Update/Delete) | §16 (00:00 → 05:00 → Generate → Publish → Monitor → Update → Tomorrow → Next day) | **(A) REAL SSOT VIOLATION** — both define lifecycle diagrams |
| Non-destructive principle | §11 (Non-destructive CHANNEL — don't touch others' posts) | §10 (Non-destructive UPDATE — update in place, don't recreate) | (B) CONTEXTUAL REUSE — related but DISTINCT principles |

**Unique to TJS-007:** Ownership model (§10), Error handling (§13)
**Unique to TJS-008:** Daily cycle (§3), Packages (§4-5), Windows (§6), Event-driven (§7), Stable journal (§8), Manual/Image (§13-14), Session (§15)

**Verdict: 1 REAL SSOT VIOLATION (lifecycle diagram).**

---

# Part 3: Special Analysis — Publication Lifecycle (TJS-002, TJS-007, TJS-008)

---

## The Question

Is "Publication Lifecycle" ONE responsibility or MULTIPLE responsibilities with similar names?

## Analysis

### What each document actually defines:

**TJS-002 — Conceptual Lifecycle**
- Publication type taxonomy (7 types)
- Lifecycle state model (6 states)
- Type-specific lifecycle flows (daily schedule, emergency, temporary)
- Archive policy
- Deletion policy
- Traceability
- Reliability guarantees

**TJS-007 — Operational Lifecycle**
- Lifecycle state model (5 states — different from TJS-002)
- Publication creation rules
- Canonical equality check
- Publication ordering
- Temporary vs permanent classification
- Publication ownership model
- Non-destructive channel principle
- Error handling

**TJS-008 — Temporal/Daily Lifecycle**
- Daily publication cycle (6-step)
- Daily and Tomorrow packages
- Publication windows (scheduling)
- Event-driven principle
- Stable journal principle
- Deterministic principle
- Non-destructive update principle
- Manual/Image publication exclusion
- Publication session

### The Architectural Verdict

**Publication Lifecycle is ONE responsibility that has been incorrectly split into THREE documents.**

The evidence:
1. All three documents use the SAME title: "Publication Lifecycle"
2. All three define lifecycle STATE MODELS (with different numbers of states — 5, 5, 6)
3. All three define UPDATE RULES (with slightly different conditions)
4. All three define TEMPORARY vs PERMANENT classification
5. The unique content in each document does NOT justify separate documents — it justifies SECTIONS within a single document

### What a single merged document would contain:

| Section | Source | Responsibility |
|---------|--------|---------------|
| Purpose & Scope | All three | Definition of lifecycle |
| Lifecycle State Model | TJS-002 §3, TJS-007 §3, TJS-008 §3 | Unified state model |
| Publication Types | TJS-002 §4 | Type taxonomy |
| Daily Cycle | TJS-008 §3, §16 | Temporal scheduling |
| Publication Windows | TJS-008 §6 | Scheduling |
| Creation Rules | TJS-007 §4 | How publications are created |
| Update Rules | TJS-002 §8, TJS-007 §5, TJS-008 §11 | When updates occur |
| Canonical Equality | TJS-007 §6 | Compare-before-update |
| Ordering | TJS-007 §7 | Deterministic order |
| Temporary Publications | TJS-002 §7, TJS-007 §8, TJS-008 §12 | Tomorrow lifecycle |
| Permanent Publications | TJS-002 §5, §9, TJS-007 §9 | Current-day preservation |
| Ownership | TJS-007 §10 | Message ID based |
| Non-destructive Channel | TJS-007 §11 | Don't touch others' posts |
| Non-destructive Update | TJS-008 §10 | Update in place |
| Manual/Image Exclusion | TJS-008 §13-14 | Outside lifecycle |
| Event-driven Principle | TJS-008 §7 | Data triggers |
| Stable Journal Principle | TJS-008 §8 | Visual stability |
| Deterministic Principle | TJS-008 §9 | Identical input → output |
| Publication Session | TJS-008 §15 | One execution = one state |
| Archive Policy | TJS-002 §9 | Historical preservation |
| Deletion Policy | TJS-002 §10 | What may be deleted |
| Traceability | TJS-002 §11 | Source tracking |
| Reliability | TJS-002 §12 | Guarantees |
| Error Handling | TJS-007 §13 | Failure recovery |
| Diagrams | TJS-007 §12, TJS-008 §16-17 | Visual representations |

**This is clearly ONE document's content, not THREE.**

---

# Part 4: Complete Overlap Summary

---

## All Detected Overlaps

| # | Document A | Document B | Overlapping Concept | Classification | Severity |
|---|-----------|-----------|-------------------|---------------|----------|
| 1 | TJS-002 | TJS-007 | Lifecycle state model | (A) SSOT VIOLATION | CRITICAL |
| 2 | TJS-002 | TJS-007 | Update rules | (A) SSOT VIOLATION | CRITICAL |
| 3 | TJS-002 | TJS-007 | Temporary publications | (A) SSOT VIOLATION | MAJOR |
| 4 | TJS-002 | TJS-007 | Archive/Permanent rules | (A) SSOT VIOLATION | MAJOR |
| 5 | TJS-002 | TJS-008 | Lifecycle state model | (A) SSOT VIOLATION | CRITICAL |
| 6 | TJS-002 | TJS-008 | Update rules | (A) SSOT VIOLATION | CRITICAL |
| 7 | TJS-002 | TJS-008 | Temporary publications | (A) SSOT VIOLATION | MAJOR |
| 8 | TJS-007 | TJS-008 | Lifecycle state model | (A) SSOT VIOLATION | CRITICAL |
| 9 | TJS-007 | TJS-008 | Update rules | (A) SSOT VIOLATION | CRITICAL |
| 10 | TJS-007 | TJS-008 | Temporary/Remove rules | (A) SSOT VIOLATION | MAJOR |
| 11 | TJS-007 | TJS-008 | Lifecycle diagram | (A) SSOT VIOLATION | MAJOR |
| 12 | TJS-003 | TJS-005 | Publication structure | (A) SSOT VIOLATION | MAJOR |
| 13 | TJS-003 | TJS-005 | Header definition | (A) SSOT VIOLATION | MAJOR |
| 14 | TJS-003 | TJS-005 | Formatting rules | (A) SSOT VIOLATION | MAJOR |
| 15 | TJS-004 | TJS-003 | Formatting rules | (A) SSOT VIOLATION | MAJOR |
| 16 | TJS-004 | TJS-005 | Territory presentation | (D) Required Evidence | MINOR |
| 17 | TJS-004 | TJS-005 | Time format | (D) Required Evidence | MINOR |
| 18 | TJS-004 | TJS-005 | Settlement formatting | (D) Required Evidence | MINOR |
| 19 | TJS-004 | TJS-005 | Address formatting | (D) Required Evidence | MINOR |
| 20 | TJS-004 | TJS-005 | Formatting rules | (D) Required Evidence | MINOR |
| 21 | TJS-004 | TJS-005 | Category titles | (D) Required Evidence | MINOR |
| 22 | TJS-005 | TJS-006 | Settlement ordering | CONFLICT | CRITICAL |
| 23 | TJS-007 | TJS-008 | Non-destructive principle | (B) Contextual Reuse | MINOR |

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total overlaps detected | 23 |
| (A) REAL SSOT VIOLATIONS | 15 |
| (B) CONTEXTUAL REUSE | 1 |
| (C) HISTORICAL REFERENCE | 0 |
| (D) REQUIRED EVIDENCE | 6 |
| (E) NORMAL COOPERATION | 0 (not counted above) |
| Semantic CONFLICTS | 1 |
| CRITICAL severity | 7 |
| MAJOR severity | 10 |
| MINOR severity | 6 |

---

**End of Audit**

**Auditor:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
