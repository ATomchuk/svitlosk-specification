# CASE001_PUBLICATION_OPEN_QUESTIONS

**Document ID:** CASE001B-OPEN-QUESTIONS

**Title:** Publication — Research Questions

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document identifies what is still unknown, what cannot yet be proven, which repository documents are insufficient, and which future investigation should answer remaining questions.

---

# What Is Still Unknown

## Question 1: What is an Interpretation Result?

**Status:** UNKNOWN

**Evidence:** GLOSSARY.md §3 states "Publication SHALL be derived exclusively from an Interpretation Result." No normative document defines "Interpretation Result."

**Impact:** Publication's source data lineage is incomplete. We know Publication comes from normalized data, but the intermediate "Interpretation Result" concept is undefined.

**Future Investigation Required:** YES — Define Interpretation Result in glossary or semantic model.

---

## Question 2: What is the internal Publication ID?

**Status:** UNKNOWN

**Evidence:** DATA_MODEL.md states "Every logical entity SHALL be uniquely identifiable" but no Publication ID field is defined in any specification.

**Impact:** Publication identity relies on composite key (Territory + Date + Template) rather than a single identifier. This may be sufficient, but is never explicitly stated.

**Future Investigation Required:** Partially — composite key may be sufficient. Explicit confirmation needed.

---

## Question 3: What happens to Publications when Territory structure changes?

**Status:** UNKNOWN

**Evidence:** No specification addresses Territory restructuring (merges, splits, renaming).

**Impact:** If a Starosta District is merged or renamed, existing Publications reference the old Territory. Identity continuity may break.

**Future Investigation Required:** YES — Territory change lifecycle needs specification.

---

## Question 4: What happens to Publications when data source changes?

**Status:** UNKNOWN

**Evidence:** No specification addresses what happens when Khmelnytskyioblenergo changes its data format or API.

**Impact:** Parser may fail to normalize data, causing Publication generation to halt. No graceful degradation is specified.

**Future Investigation Required:** YES — Data source change lifecycle needs specification.

---

## Question 5: What is the maximum Publication count per day?

**Status:** UNKNOWN

**Evidence:** No specification limits the number of Publications per Issue or per day.

**Impact:** If many territories have outages, the Journal may have many Publications. No upper bound is defined.

**Future Investigation Required:** Partially — practical limits may emerge from Telegram constraints.

---

## Question 6: What happens to Publications during system downtime?

**Status:** UNKNOWN

**Evidence:** No specification addresses system availability, downtime, or recovery.

**Impact:** If the system goes down during a reporting period, Publications may be missed or delayed. No recovery mechanism is specified.

**Future Investigation Required:** YES — System resilience needs specification.

---

## Question 7: What happens to Publications during Telegram downtime?

**Status:** UNKNOWN

**Evidence:** No specification addresses Telegram API availability or retry mechanisms.

**Impact:** If Telegram is unavailable, Publications cannot be delivered. No retry or queue mechanism is specified.

**Future Investigation Required:** YES — Telegram delivery resilience needs specification.

---

## Question 8: What is the relationship between Graphic Publications and text Publications?

**Status:** UNKNOWN

**Evidence:** TJS-022 defines Graphic Publications. TJS-021 defines text Publication lifecycle. No specification explicitly links them.

**Impact:** Graphic Publications (T-001 through T-005) have different triggers, different lifecycles, and different update mechanics. Their relationship to text Publications is unclear.

**Future Investigation Required:** YES — Unified publication model may be needed.

---

## Question 9: Can Manual Publications be archived?

**Status:** UNKNOWN

**Evidence:** TJS-021 §5.5: "Only temporary Publications MAY be removed." No specification addresses Manual Publication archival.

**Impact:** Manual Publications may persist indefinitely on Telegram without archival mechanism.

**Future Investigation Required:** YES — Manual Publication lifecycle needs specification.

---

## Question 10: What is the retention policy for archived Publications?

**Status:** UNKNOWN

**Evidence:** TJS-021 §4.4: "Archived Publications remain available in the Telegram Journal permanently." No retention policy is defined.

**Impact:** "Permanently" is undefined. No data retention, cleanup, or archival-to-deep-storage mechanism is specified.

**Future Investigation Required:** Partially — "permanent" may be intentional.

---

# What Cannot Yet Be Proven

## Proof 1: Publication Engine is Aggregate Root

**Status:** CANNOT PROVE

**Evidence:** Publication Engine performs ALL actions on Publication (Create, Modify, Read, Own, Reference, Destroy, Archive). But no specification explicitly states "Publication Engine is Aggregate Root."

**Limitation:** The Aggregate Root classification is an analytical conclusion from Phase 4, not a normative statement in any document.

---

## Proof 2: Territory + Date + Template is sufficient identity

**Status:** CANNOT PROVE

**Evidence:** No specification explicitly states "Publication identity = Territory + Date + Template." This is an analytical conclusion from Phase 4.

**Limitation:** The identity model is inferred from evidence, not stated in any document.

---

## Proof 3: Manual Publications are a different concept

**Status:** CANNOT PROVE

**Evidence:** Manual Publications are excluded from automatic lifecycle, created by different actors, and have different ownership. But they are still called "Publications."

**Limitation:** Whether Manual Publications are a different concept or a variant of the same concept is not resolved.

---

# Insufficient Repository Documents

## Document 1: TELEGRAM_SEMANTIC_MODEL.md (TJS-000)

**Insufficiency:** Defines Publication as "one independent publication belonging to an Issue" but does not define internal attributes, identity model, or mutation rules.

**Impact:** Publication's semantic definition is thin. More detail needed on what Publication IS at the semantic level.

---

## Document 2: TELEGRAM_GLOSSARY.md (TJS-000A)

**Insufficiency:** References "Interpretation Result" without defining it. References "Publication Channel" without specifying lifecycle implications.

**Impact:** Publication's source lineage and channel-specific behavior are undefined.

---

## Document 3: DATA_MODEL.md

**Insufficiency:** States "Every logical entity SHALL be uniquely identifiable" but does not define Publication ID. States "Publication" in logical relationships but does not specify attributes.

**Impact:** Publication's data model is incomplete.

---

## Document 4: TELEGRAM_PUBLICATION_LIFECYCLE.md (TJS-021)

**Insufficiency:** Defines lifecycle states and transitions but does not address: Territory changes, data source changes, system downtime, Telegram downtime, Manual Publications, Graphic Publications.

**Impact:** Publication lifecycle is incomplete for edge cases.

---

## Document 5: TELEGRAM_PUBLISHING_CANONICAL_MODEL.md (TJS-010)

**Insufficiency:** Defines component interactions but does not specify: retry mechanisms, error handling, queue management, delivery guarantees.

**Impact:** Publication delivery mechanics are incomplete.

---

# Future Investigation Requirements

## Investigation 1: Interpretation Result Definition

**Scope:** Define "Interpretation Result" in TELEGRAM_GLOSSARY.md or TELEGRAM_SEMANTIC_MODEL.md.

**Priority:** HIGH — Publication's source lineage depends on this.

---

## Investigation 2: Territory Change Lifecycle

**Scope:** Define what happens to Publications when Territory structure changes (merges, splits, renaming).

**Priority:** MEDIUM — Edge case but important for long-term integrity.

---

## Investigation 3: Data Source Change Lifecycle

**Scope:** Define what happens to Publications when data source format or API changes.

**Priority:** MEDIUM — Edge case but important for resilience.

---

## Investigation 4: Manual Publication Lifecycle

**Scope:** Define lifecycle for Manual Publications (creation, archival, removal).

**Priority:** HIGH — Manual Publications exist but have no specified lifecycle.

---

## Investigation 5: Graphic Publication Lifecycle Integration

**Scope:** Define how Graphic Publications relate to text Publications lifecycle.

**Priority:** MEDIUM — Different lifecycles need reconciliation.

---

## Investigation 6: System Resilience

**Scope:** Define behavior during system downtime, Telegram downtime, and recovery.

**Priority:** HIGH — No resilience mechanisms specified.

---

## Investigation 7: Publication ID Model

**Scope:** Confirm whether composite key (Territory + Date + Template) is sufficient or if explicit Publication ID is needed.

**Priority:** LOW — Composite key may be sufficient.

---

## Investigation 8: Retention Policy

**Scope:** Define retention policy for archived Publications (if any).

**Priority:** LOW — "Permanent" may be intentional.

---

# Open Questions Summary

| Category | Count |
|----------|-------|
| Unknown | 10 |
| Cannot Prove | 3 |
| Insufficient Documents | 5 |
| Future Investigations | 8 |
| **Total** | **26** |

---

# End of Research Questions
