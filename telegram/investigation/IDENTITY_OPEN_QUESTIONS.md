# IDENTITY_OPEN_QUESTIONS

**Document ID:** CASE001C-QUESTIONS

**Title:** Identity — Open Questions

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity Investigation

---

# Purpose

This document lists every unresolved question, every assumption, and every place where repository documentation is insufficient.

---

# Unresolved Questions

## Question IQ-001: Precise Identity Criteria

**Question:** What is the exact identity criteria for Publication?

**Current State:** Reconstructed as Territory + Date + Template, but not explicitly defined in any specification.

**Impact:** HIGH — affects identity model, equality checks, and lifecycle management.

**Evidence:**

- DATA_MODEL.md: "Every logical entity SHALL be uniquely identifiable"
- No explicit Publication ID defined
- Legacy TJS-007 §10 mentions Telegram Message ID

---

## Question IQ-002: Internal Publication ID

**Question:** Is there an internal Publication ID?

**Current State:** No internal Publication ID exists in any specification.

**Impact:** HIGH — affects identity persistence and cross-system migration.

**Evidence:**

- No specification defines internal Publication ID
- DATA_MODEL.md implies need for unique identification

---

## Question IQ-003: Platform Migration

**Question:** How does identity survive platform migration?

**Current State:** No specification addresses platform migration.

**Impact:** MEDIUM — affects portability and multi-channel support.

**Evidence:**

- TJS-000 §3: "The Journal exists independently from any publication platform"
- But all lifecycle mechanics reference Telegram

---

## Question IQ-004: Identity After Replacement

**Question:** What happens to identity when Publication is replaced?

**Current State:** No specification addresses identity after replacement.

**Impact:** MEDIUM — affects lifecycle management.

**Evidence:**

- TJS-021 §7.2: "Publication replacement SHALL occur only when..."
- No specification addresses identity after replacement

---

## Question IQ-005: Identity Uniqueness

**Question:** Can two Publications have the same identity?

**Current State:** No specification addresses identity uniqueness.

**Impact:** MEDIUM — affects equality checks and deduplication.

**Evidence:**

- Legacy TJS-007 §6: "Two publications generated from identical datasets SHALL be byte-for-byte identical"
- This implies same identity = same Publication

---

## Question IQ-006: Identity Verification

**Question:** How is identity verified across components?

**Current State:** No specification addresses identity verification.

**Impact:** MEDIUM — affects cross-component consistency.

**Evidence:**

- TJS-010 §5.1: Approved interactions involve Publications
- No specification addresses how identity is verified

---

## Question IQ-007: Identity vs Traceability

**Question:** What is the relationship between identity and traceability?

**Current State:** No specification addresses this relationship.

**Impact:** LOW — affects documentation clarity.

**Evidence:**

- GLOSSARY.md §2: "Traceability — The ability to identify the origin of every piece of information"
- Traceability and identity are related but distinct concepts

---

## Question IQ-008: Identity vs Repository Authority

**Question:** How does identity interact with the Repository Authority Principle?

**Current State:** No specification addresses this interaction.

**Impact:** LOW — affects governance clarity.

**Evidence:**

- TJS-021 §3.1: "Repository SHALL be the single authoritative source of truth"
- Repository is authoritative for state, but identity is a different concern

---

# Assumptions

## Assumption A-001: Territory + Date + Template = Identity

**Assumption:** Publication identity is Territory + Date + Template.

**Basis:** Reconstructed from evidence across multiple specifications.

**Risk:** Not explicitly defined. May be incorrect.

---

## Assumption A-002: Telegram Message ID = External Reference

**Assumption:** Telegram Message ID is an external reference, not intrinsic identity.

**Basis:** Publication exists before Telegram Message ID is assigned (Generated state).

**Risk:** Legacy TJS-007 §10 treats Telegram Message ID as ownership determinant.

---

## Assumption A-003: Identity Persists Across Lifecycle

**Assumption:** Identity persists across all lifecycle states.

**Basis:** Territory, Date, and Template never change.

**Risk:** Not explicitly stated in any specification.

---

## Assumption A-004: Manual Publications Have Different Identity

**Assumption:** Manual Publications have different identity than automated Publications.

**Basis:** Different creation actor, different lifecycle.

**Risk:** Not explicitly stated in any specification.

---

# Insufficient Documentation

## Insufficient Document ID-001: GLOSSARY.md

**What Is Insufficient:**

- No identity criteria defined for Publication
- No attribute list defined
- No lifecycle overview

**What Is Needed:**

- Explicit identity criteria
- Complete attribute list
- Lifecycle overview

**Impact:** HIGH — GLOSSARY is the semantic authority.

---

## Insufficient Document ID-002: DATA_MODEL.md

**What Is Insufficient:**

- No identity criteria defined for Publication
- No attribute list defined
- No relationships defined

**What Is Needed:**

- Explicit identity criteria
- Complete attribute list
- Relationship definitions

**Impact:** HIGH — DATA_MODEL is the logical data authority.

---

## Insufficient Document ID-003: TJS-021 (Publication Lifecycle)

**What Is Insufficient:**

- No identity criteria defined
- No attribute list defined
- Archival trigger is vague

**What Is Needed:**

- Explicit identity criteria
- Complete attribute list
- Precise archival trigger

**Impact:** MEDIUM — TJS-021 is the lifecycle authority.

---

## Insufficient Document ID-004: TJS-010 (Publishing Model)

**What Is Insufficient:**

- No identity criteria defined
- No attribute list defined
- Ownership model is incomplete

**What Is Needed:**

- Explicit identity criteria
- Complete attribute list
- Complete ownership model

**Impact:** MEDIUM — TJS-010 is the publishing authority.

---

## Insufficient Document ID-005: TJS-000A (Telegram Glossary)

**What Is Insufficient:**

- No identity criteria defined for Publication
- No attribute list defined

**What Is Needed:**

- Explicit identity criteria
- Complete attribute list

**Impact:** MEDIUM — TJS-000A is the Telegram terminology authority.

---

# Open Questions Summary

| Category | Count |
|----------|-------|
| Unresolved Questions | 8 |
| Assumptions | 4 |
| Insufficient Documents | 5 |
| **Total** | **17** |

---

# End of Open Questions
