# Telegram Architectural Evidence Matrix

**Date:** 2026-07-13
**Source:** TELEGRAM_ARCHITECTURAL_EVIDENCE_AUDIT.md
**Scope:** Complete verification matrix for all previous audit findings

---

## Matrix Structure

Every finding from the Semantic Responsibility Audit is verified against documentary evidence.

Columns:
- **Finding** — Original finding ID and description
- **Evidence** — Exact documentary citations
- **Verification** — CONFIRMED / PARTIALLY CONFIRMED / REJECTED
- **Confidence** — HIGH / MEDIUM / LOW
- **Original Classification** — From the Semantic Responsibility Audit
- **Revised Classification** — After evidence verification

---

## Lifecycle Overlaps (TJS-002, TJS-007, TJS-008)

### M-001: Lifecycle State Model

| | Evidence |
|---|---------|
| TJS-002 §3 | "Each publication shall pass through one or more of the following states: 1. Generated 2. Scheduled 3. Published 4. Updated 5. Archived 6. Removed" |
| TJS-007 §3 | "Dataset → Render → Publish → Update (if required) → Retain or Remove" |
| TJS-008 §3 | "1. generation of the Today's Package; 2. publication of Today's Posts; 3. monitoring Dataset updates; 4. updating changed Publications; 5. generation of Tomorrow Publications; 6. removal of obsolete Tomorrow Publications" |
| TJS-002 Purpose | "defines the complete lifecycle of publications" |
| TJS-007 Purpose | "defines the complete lifecycle of Publications" |
| TJS-008 Purpose | "defines the lifecycle of Telegram Journal Publications" |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** Three documents, three different state models (6 states, 5 states, 6 steps), three different naming conventions (state-based, flow-based, cycle-based). All claim to define "the lifecycle." This is duplicated AUTHORITY, not duplicated wording.

---

### M-002: Update Rules

| | Evidence |
|---|---------|
| TJS-002 §8 | "Published messages may be edited only when: - official source data changes; - formatting corrections are required; - generated graphics are regenerated" |
| TJS-007 §5 | "A Publication MAY be updated only when: - the normalized dataset changes; or - the rendering rules change" |
| TJS-008 §11 | "A Publication SHALL be updated only when: - the normalized Dataset changes; or - the Rendering Rules change. No other event SHALL trigger Publication updates." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** TJS-002 has 3 conditions. TJS-007 and TJS-008 have 2 conditions. TJS-002 includes "formatting corrections" and "generated graphics" which the others exclude. TJS-008 adds "No other event SHALL trigger" which TJS-002 does not. The conditions are explicitly DIFFERENT.

---

### M-003: Temporary Publications

| | Evidence |
|---|---------|
| TJS-002 §7 | "Examples include: - Tomorrow schedule announcement - Upcoming publication notice - Technical maintenance reminder" |
| TJS-007 §8 | "Tomorrow Publications are temporary... Only Tomorrow Publications MAY be removed automatically." |
| TJS-008 §12 | "Tomorrow Publications SHALL... be deleted automatically after becoming obsolete." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** TJS-002 lists 3 types of temporary publications. TJS-007 explicitly restricts to "Tomorrow Publications only." TJS-008 restricts to Tomorrow Publications. The scope is explicitly DIFFERENT.

---

### M-004: Archive/Permanent Rules

| | Evidence |
|---|---------|
| TJS-002 §9 | "Historical publications form the permanent public archive of the Telegram Journal. Archive entries shall not be modified except to correct verified technical errors." |
| TJS-007 §9 | "Current-day Publications SHALL remain in the Telegram Journal. The Publisher SHALL NOT remove historical Publications generated for the current reporting day." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **PARTIALLY CONFIRMED** | **MEDIUM** | (A) SSOT VIOLATION | **(D) REQUIRED EVIDENCE** |

**Evidence analysis:** TJS-002 defines ARCHIVE policy (historical records). TJS-007 defines PERMANENT classification (current-day records). These are related but at different lifecycle stages. Both claim authority over "preservation" but with different temporal scopes. Downgraded from SSOT VIOLATION to REQUIRED EVIDENCE because the responsibilities are distinguishable.

---

### M-005: Temporary vs Permanent Classification

| | Evidence |
|---|---------|
| TJS-002 §5 | "The daily schedule shall never be deleted." |
| TJS-002 §7 | "These publications may be removed automatically after they become irrelevant." |
| TJS-007 §8 | "Only Tomorrow Publications MAY be removed automatically." |
| TJS-007 §9 | "The Publisher SHALL NOT remove historical Publications generated for the current reporting day." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** Both documents define what is permanent and what is temporary. TJS-002 says daily schedules "shall never be deleted." TJS-007 says "Current-day Publications SHALL remain." Both use different phrasing for the same preservation concept.

---

### M-006: Lifecycle Diagrams

| | Evidence |
|---|---------|
| TJS-007 §12 | Titled "Publication Lifecycle Diagram" — Parser → Dataset → Engine → Publisher → Create/Update/Delete → Journal |
| TJS-008 §16 | Titled "Daily Lifecycle" — 00:00 → 05:00 → Generate → Publish → Monitor → Update → Tomorrow → Next day |
| TJS-008 §17 | Titled "Telegram Journal Architecture" — Sources → Parser → Dataset → Engine → Rendering → Journal |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **MEDIUM** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** Two documents contain lifecycle diagrams. TJS-007's diagram and TJS-008 §17's diagram show similar component flows. TJS-008 §16 shows a temporal cycle. All represent the same lifecycle. Downgraded confidence because the diagrams serve different purposes (operational vs temporal vs architectural).

---

## Structure Overlaps (TJS-003, TJS-005)

### M-007: Publication Structure

| | Evidence |
|---|---------|
| TJS-003 §1 | "defines the official structure of publications" |
| TJS-003 §3 | "The standard publication consists of: 1. Header 2. Main information 3. Graphic (optional) 4. Additional information 5. Footer" |
| TJS-005 §1 | "establishes the normative structure, hierarchy" |
| TJS-005 §4 | "Publication → Territory Header → Planned Outages Section → Emergency Outages Section → Update Time" |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** Both claim authority over "structure." TJS-003 uses "Header, Main information, Graphic, Additional information, Footer." TJS-005 uses "Territory Header, Planned Outages Section, Emergency Outages Section, Update Time." The structures use DIFFERENT terminology. This is duplicated authority.

---

### M-008: Header Definition

| | Evidence |
|---|---------|
| TJS-003 §4 | "The header identifies the publication. It shall contain: - publication type; - date; - if applicable, affected schedule." |
| TJS-005 §5 | "The Publication SHALL begin with the Territory title. Telegram Publications SHALL render Territory titles in uppercase." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** TJS-003 says the header contains "publication type, date, affected schedule." TJS-005 says the header is "Territory title in uppercase." These are DIFFERENT definitions of what the header contains. TJS-003's header is conceptual (type, date). TJS-005's header is territorial (Territory name).

---

## Formatting Overlaps (TJS-003, TJS-004, TJS-005)

### M-009: Formatting Rules

| | Evidence |
|---|---------|
| TJS-003 §9 | "Publications shall use: - short paragraphs; - consistent spacing; - limited emoji usage; - uniform typography; - consistent ordering of sections." |
| TJS-004 §11 (Formatting) | "Only the following formatting is permitted: - bold; - plain text. Italic, underline, spoiler, blockquote, code blocks and other formatting are prohibited." |
| TJS-005 §15 | "Telegram formatting SHALL use only: - **bold** (`<b>`). Telegram block quotes MAY be used by future specifications where appropriate. No other formatting SHALL be used." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | (A) SSOT VIOLATION | **(A) SSOT VIOLATION** |

**Evidence analysis:** Three documents define "formatting rules." TJS-003 defines general principles (spacing, typography). TJS-004 defines permitted types (bold + plain text). TJS-005 defines implementation (bold with HTML tag). TJS-003's criteria are DIFFERENT from TJS-004/TJS-005. TJS-004 and TJS-005 are consistent.

---

## Editorial vs Template Overlaps (TJS-004, TJS-005)

### M-010 through M-014: Policy vs Implementation

| | Evidence |
|---|---------|
| TJS-004 §3 | "Territory name is always the first element... written using uppercase letters" |
| TJS-005 §5 | "The Publication SHALL begin with the Territory title... SHALL render Territory titles in uppercase" |
| TJS-004 §9 | "Settlement names are displayed in bold" |
| TJS-005 §10 | "Settlement names SHALL be rendered in bold" |
| TJS-005 §16 References | "Depends on: TJS-004 — Editorial Policy" |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **NOT A VIOLATION** | **HIGH** | (D) Required Evidence | **(D) REQUIRED EVIDENCE** |

**Evidence analysis:** The content is CONSISTENT. TJS-004 uses policy language ("is displayed"). TJS-005 uses normative language ("SHALL be rendered") with HTML implementation. TJS-005 explicitly depends on TJS-004 (declared in References). This is normal cross-document cooperation.

---

## Rendering Overlaps (TJS-005, TJS-006)

### M-015: Settlement Ordering (CONFLICT)

| | Evidence |
|---|---------|
| TJS-005 §7 | "Inside a Starosta District Publication, Settlements SHALL appear in the canonical order defined by TERRITORIAL_MODEL.md. Alphabetical sorting is prohibited." |
| TJS-006 §7 | "Settlements SHALL be ordered alphabetically using the Ukrainian alphabet." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **CONFIRMED** | **HIGH** | CONFLICT | **CONFLICT** |

**Evidence analysis:** "Alphabetical sorting is prohibited" vs "SHALL be ordered alphabetically." These are MUTUALLY EXCLUSIVE rules. Both use normative language. This is a semantic CONFLICT, not just duplication.

---

### M-016: Time Ordering

| | Evidence |
|---|---------|
| TJS-005 §8 | "Inside each Settlement, Time Intervals SHALL be sorted by their starting time." |
| TJS-006 §6 | "Time intervals SHALL always be sorted by their start time." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **NOT A VIOLATION** | **HIGH** | (D) Required Evidence | **(D) REQUIRED EVIDENCE** |

**Evidence analysis:** Same fact, same rule, different documents. This is required evidence — the same ordering rule cited in both the template spec and the rendering spec.

---

### M-017: Duplicate Removal

| | Evidence |
|---|---------|
| TJS-005 §12 | "Duplicate addresses are prohibited." |
| TJS-006 §9 | "Duplicate addresses SHALL NOT appear in publications." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **NOT A VIOLATION** | **HIGH** | (D) Required Evidence | **(D) REQUIRED EVIDENCE** |

**Evidence analysis:** Same fact, same rule. Required evidence.

---

## Non-Destructive Principles (TJS-007, TJS-008)

### M-018: Non-Destructive Channel vs Non-Destructive Update

| | Evidence |
|---|---------|
| TJS-007 §11 | "Non-destructive Channel Principle... The Publisher SHALL modify only Publications that it owns." |
| TJS-008 §10 | "Non-destructive Update Principle... Updates SHOULD modify existing Publications instead of replacing them." |

| Verification | Confidence | Original | Revised |
|-------------|------------|----------|---------|
| **NOT A VIOLATION** | **HIGH** | (B) Contextual Reuse | **(B) CONTEXTUAL REUSE** |

**Evidence analysis:** Different principle names ("Channel" vs "Update"). Different content (ownership rules vs update strategy). Different concerns (WHAT you may touch vs HOW you may change). These are related but DISTINCT principles.

---

## Summary Matrix

| Finding | Verification | Confidence | Classification Change? |
|---------|-------------|------------|----------------------|
| M-001: Lifecycle state model | CONFIRMED | HIGH | No change |
| M-002: Update rules | CONFIRMED | HIGH | No change |
| M-003: Temporary publications | CONFIRMED | HIGH | No change |
| M-004: Archive/Permanent rules | PARTIALLY CONFIRMED | MEDIUM | **CHANGED**: (A) → (D) |
| M-005: Temp vs Permanent | CONFIRMED | HIGH | No change |
| M-006: Lifecycle diagrams | CONFIRMED | MEDIUM | No change |
| M-007: Publication structure | CONFIRMED | HIGH | No change |
| M-008: Header definition | CONFIRMED | HIGH | No change |
| M-009: Formatting rules | CONFIRMED | HIGH | No change |
| M-010: Territory presentation | NOT A VIOLATION | HIGH | No change (was already D) |
| M-011: Time format | NOT A VIOLATION | HIGH | No change (was already D) |
| M-012: Settlement formatting | NOT A VIOLATION | HIGH | No change (was already D) |
| M-013: Address formatting | NOT A VIOLATION | HIGH | No change (was already D) |
| M-014: Category titles | NOT A VIOLATION | HIGH | No change (was already D) |
| M-015: Settlement ordering | CONFIRMED | HIGH | No change (CONFLICT) |
| M-016: Time ordering | NOT A VIOLATION | HIGH | No change (was already D) |
| M-017: Duplicate removal | NOT A VIOLATION | HIGH | No change (was already D) |
| M-018: Non-destructive principles | NOT A VIOLATION | HIGH | No change (was already B) |

---

## Classification Changes

| Finding | Original Classification | Revised Classification | Reason |
|---------|------------------------|----------------------|--------|
| M-004: Archive/Permanent | (A) SSOT VIOLATION | (D) REQUIRED EVIDENCE | Responsibilities are distinguishable by temporal scope |

**Total classification changes: 1**

---

**End of Evidence Matrix**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
