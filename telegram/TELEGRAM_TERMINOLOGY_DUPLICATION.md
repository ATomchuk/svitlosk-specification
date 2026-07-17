# Telegram Terminology Duplication

**Date:** 2026-07-13
**Purpose:** All duplicated concepts, hidden synonyms, conflicts
**Source:** TELEGRAM_TERMINOLOGY_MATRIX.md

---

# Duplicated Concepts

## Duplication #1: Publication vs Message vs Post

| Variant | Document | Context |
|---------|----------|---------|
| Publication | TJS-000, TJS-002, TJS-003, TJS-005, TJS-007, TJS-008 | "one independent publication belonging to an Issue" |
| Telegram Publication | TJS-005, TJS-006 | "every Telegram Publication generated" |
| Message | TJS-007 §10 | "stored Telegram Message ID" |
| Post | TJS-003 (file name), TJS-007 §11 | "Post Structure", "Publisher-owned Posts" |
| Telegram Message | TJS-007 §10, §12 | "editing the existing Telegram Message" |

**Analysis:** "Publication" is the canonical term defined in TJS-000. "Message" and "Post" are platform-level synonyms used in TJS-007. "Telegram Publication" is a qualified form.

**Recommendation:** "Publication" is canonical. "Message" and "Post" should be deprecated in favor of "Publication". "Telegram Message" should remain as a platform-specific reference (the message object in Telegram's API).

**Severity:** MEDIUM — hidden synonym

---

## Duplication #2: Publisher vs Telegram Publisher

| Variant | Document | Context |
|---------|----------|---------|
| Publisher | TJS-005 §4, TJS-006, TJS-007 | "The Publisher SHALL create Publications" |
| Telegram Publisher | TJS-006 §1, TJS-007 §12, TJS-008 | "used by the Telegram Publisher" |
| Publication Engine | TJS-001 §10, TJS-005, TJS-007, TJS-008 | "receives processed information from the Publication Engine" |

**Analysis:** "Publisher" is the logical Role. "Telegram Publisher" is the Telegram-specific realization. "Publication Engine" is the architectural Component. Three different abstraction levels for related concepts.

**Recommendation:** Keep all three with clear distinctions: Publisher (Role), Publication Engine (Component), Telegram Publisher (platform-specific implementation).

**Severity:** LOW — intentional abstraction levels

---

## Duplication #3: Publication Lifecycle (Triple)

| Variant | Document | Context |
|---------|----------|---------|
| Publication Lifecycle | TJS-002 §1, TJS-007 §1, TJS-008 §1 | All three define "complete lifecycle" |
| Lifecycle | TJS-002 §3, TJS-007 §3, TJS-008 §3 | Shortened form |
| Publication Lifecycle States | Audit docs | Referenced in audits |

**Analysis:** Three documents with the same title defining overlapping but different lifecycle models. This is the CRITICAL SSOT violation identified in the architecture audit.

**Recommendation:** MERGE into TJS-005. "Publication Lifecycle" is the single canonical term.

**Severity:** CRITICAL — SSOT violation

---

## Duplication #4: Lifecycle State Model (Triple)

| Variant | Document | States |
|---------|----------|--------|
| Lifecycle Overview | TJS-002 §3 | 6 states: Generated, Scheduled, Published, Updated, Archived, Removed |
| Publication Lifecycle | TJS-007 §3 | 5 states: Dataset → Render → Publish → Update → Retain/Remove |
| Publication Cycle | TJS-008 §3 | 6 steps: generation, publication, monitoring, updating, generation, removal |

**Analysis:** Three different state models with different state counts and names.

**Recommendation:** Unify into one canonical state model in TJS-005.

**Severity:** CRITICAL — conflicting definitions

---

## Duplication #5: Temporary Publication

| Variant | Document | Scope |
|---------|----------|-------|
| Temporary Publications | TJS-002 §7 | 3 types: Tomorrow, Upcoming notice, Technical maintenance |
| Tomorrow Publications | TJS-007 §8, TJS-008 §12 | 1 type: Tomorrow only |
| Removable Publication | Implicit | Publication that may be removed |

**Analysis:** TJS-002 defines 3 types of temporary publications. TJS-007 and TJS-008 restrict to Tomorrow only. Conflicting scope.

**Recommendation:** Unify in TJS-005 with clear classification.

**Severity:** MAJOR — conflicting scope

---

## Duplication #6: Permanent Publication

| Variant | Document | Context |
|---------|----------|---------|
| Permanent Publications | TJS-007 §9 | Current-day Publications remain |
| Historical Publications | TJS-002 §9, TJS-007 §9 | Publications forming the archive |
| Current-day Publications | TJS-007 §9 | Publications for the current reporting day |

**Analysis:** "Permanent", "Historical", and "Current-day" are used somewhat interchangeably but with different temporal scopes.

**Recommendation:** Clarify: "Permanent" = never deleted; "Historical" = archived; "Current-day" = today's publications.

**Severity:** LOW — overlapping but distinguishable

---

## Duplication #7: Update Rules

| Variant | Document | Conditions |
|---------|----------|-----------|
| Update Rules | TJS-002 §8 | 3 conditions: source change, formatting, graphics |
| Publication Updates | TJS-007 §5 | 2 conditions: dataset change, rendering change |
| Update Policy | TJS-008 §11 | 2 conditions: dataset change, rendering change |

**Analysis:** Three different sets of update conditions.

**Recommendation:** Unify in TJS-005 with authoritative conditions.

**Severity:** CRITICAL — conflicting definitions

---

## Duplication #8: Archive Policy

| Variant | Document | Context |
|---------|----------|---------|
| Archive Policy | TJS-002 §9 | "Historical publications form the permanent public archive" |
| Permanent Publications | TJS-007 §9 | "Current-day Publications SHALL remain" |

**Analysis:** Related but at different lifecycle stages (historical vs current-day).

**Recommendation:** Keep both but clarify scope: Archive Policy = historical; Permanent = current-day.

**Severity:** LOW — distinguishable

---

## Duplication #9: Non-destructive Principles

| Variant | Document | Scope |
|---------|----------|-------|
| Non-destructive Channel Principle | TJS-007 §11 | Don't modify others' content |
| Non-destructive Update Principle | TJS-008 §10 | Update in place, don't recreate |

**Analysis:** Related but DISTINCT principles. Channel = ownership; Update = strategy.

**Recommendation:** Keep both as separate principles in TJS-005.

**Severity:** LOW — intentional distinction

---

## Duplication #10: Publication Structure

| Variant | Document | Detail Level |
|---------|----------|-------------|
| Standard Publication Structure | TJS-003 §3 | 5 sections: Header, Main, Graphic, Additional, Footer |
| Publication Grammar | TJS-005 §4 | Grammar tree: Territory Header → Sections → Settlement → Time → Street → Addresses |

**Analysis:** TJS-003 is conceptual; TJS-005 is normative. Different terminology for overlapping concepts.

**Recommendation:** ABSORB TJS-003 into TJS-005. "Publication Structure" and "Publication Grammar" should be unified.

**Severity:** MAJOR — overlapping definitions

---

## Duplication #11: Header

| Variant | Document | Context |
|---------|----------|---------|
| Header | TJS-003 §4 | "The header identifies the publication" |
| Territory Header | TJS-005 §5 | "The Publication SHALL begin with the Territory title" |

**Analysis:** TJS-003's "Header" is broader (type, date, schedule). TJS-005's "Territory Header" is specific (territory name).

**Recommendation:** "Territory Header" is the canonical term. TJS-003's "Header" concept is absorbed.

**Severity:** LOW — different scope

---

## Duplication #12: Formatting Rules (Triple)

| Variant | Document | Level |
|---------|----------|-------|
| Formatting Rules | TJS-003 §9 | General principles (spacing, typography) |
| Formatting | TJS-004 §11 | Policy (permitted types: bold + plain text) |
| Formatting Rules | TJS-005 §15 | Implementation (bold with `<b>` tag) |

**Analysis:** Three documents at different abstraction levels.

**Recommendation:** TJS-004 owns policy; TJS-005 owns implementation. TJS-003's rules absorbed into TJS-004.

**Severity:** MAJOR — triple ownership

---

# Hidden Synonyms

| Canonical Term | Hidden Synonym | Document | Evidence |
|---------------|---------------|----------|----------|
| Publication | Message | TJS-007 §10 | "stored Telegram Message ID" |
| Publication | Post | TJS-003 filename, TJS-007 §11 | "Post Structure", "Publisher-owned Posts" |
| Publication | Telegram Message | TJS-007 §12 | "editing the existing Telegram Message" |
| Publisher | Telegram Publisher | TJS-006 §1 | "used by the Telegram Publisher" |
| Settlement | Village | Implicit | Ukrainian "село" |
| Starosta District | Starosta Okruh | TJS-004 §3 | "SAMCHYKY SO" |

---

# Conflicting Definitions

| Concept | Definition A | Definition B | Conflict |
|---------|-------------|-------------|----------|
| Settlement Ordering | TJS-005 §7: "canonical TERRITORIAL_MODEL.md order; alphabetical sorting PROHIBITED" | TJS-006 §7: "SHALL be ordered alphabetically using Ukrainian alphabet" | MUTUALLY EXCLUSIVE |
| Lifecycle States | TJS-002 §3: 6 states | TJS-007 §3: 5 states | DIFFERENT COUNT |
| Update Conditions | TJS-002 §8: 3 conditions | TJS-007 §5: 2 conditions | DIFFERENT SET |
| Temporary Scope | TJS-002 §7: 3 types | TJS-007 §8: 1 type | DIFFERENT SCOPE |

---

# Undefined Terms

| Term | Used In | Definition Status |
|------|---------|------------------|
| Issue | TJS-000 §4 | Defined in TJS-000 but NOT used by any TJS specification |
| Publication Package | TJS-004 §4, TJS-005, TJS-008 | Used but definition varies |
| Reporting Period | TJS-002 §7, TJS-008 §6 | Used but not formally defined |
| Deployment Configuration | TJS-008 §6 | Used but not defined |
| Normalized Dataset | TJS-006 §4, TJS-007, TJS-008 | Used but defined in GLOSSARY, not TJS |

---

# Terms Used Before Being Defined

| Term | Used In | Defined In |
|------|---------|-----------|
| Publication | TJS-001 §10 (implicitly) | TJS-000 §4 |
| Journal | TJS-001 §3 | TJS-000 §4 |
| Issue | Not used by TJS | TJS-000 §4 |

---

# Platform Terms (Telegram-Specific)

| Term | Context |
|------|---------|
| Telegram Message ID | Platform identifier |
| Telegram Bot API | Platform interface |
| Rate Limiting | Platform constraint |
| Channel | Platform concept |
| subscribers | Platform audience |

---

# SvitloSk-Specific Terms

| Term | Context |
|------|---------|
| SvitloSk | Project name |
| Telegram Journal | Project's publication channel |
| Publication Engine | Project's component |
| Parser | Project's component |
| Starokostiantyniv | Primary community |

---

**End of Duplication Analysis**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
