# IDENTITY_TIMELINE_v2

**Document ID:** CASE001D-TIMELINE

**Title:** Identity Timeline v2 — Tracking Identity and Identifier Through Lifecycle

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity vs Identifier Investigation

---

# Purpose

This document follows ONE Publication through its entire lifecycle, tracking Identity, Identifier, Representation, Ownership, and Lifecycle at every stage.

---

# Publication Lifecycle Timeline

## Stage 1: Birth (Non-Existence → Created)

**State:** Publication does not exist → Generated

**Identity:** None → Territory + Date + Template

**Identifier:** None

**Representation:** None → Repository Object

**Ownership:** None → Publication Engine

**Lifecycle:** None → Generated

**Changes:**

- Identity CREATED (Territory + Date + Template)
- Identifier: NONE
- Representation CREATED (Repository Object)
- Ownership CREATED (Publication Engine)
- Lifecycle CREATED (Generated)

**Evidence:** TJS-021 §6.1, TJS-010 §4.1

---

## Stage 2: Parser (Data Retrieval)

**State:** Generated

**Identity:** Territory + Date + Template

**Identifier:** None

**Representation:** Repository Object

**Ownership:** Publication Engine

**Lifecycle:** Generated

**Changes:**

- Identity: UNCHANGED
- Identifier: NONE
- Representation: UNCHANGED
- Ownership: UNCHANGED
- Lifecycle: UNCHANGED

**Evidence:** TJS-010 §4.2

---

## Stage 3: Publication Engine (Generation)

**State:** Generated

**Identity:** Territory + Date + Template

**Identifier:** None

**Representation:** Repository Object

**Ownership:** Publication Engine

**Lifecycle:** Generated

**Changes:**

- Identity: UNCHANGED
- Identifier: NONE
- Representation: UNCHANGED
- Ownership: UNCHANGED
- Lifecycle: UNCHANGED

**Evidence:** TJS-010 §4.1

---

## Stage 4: Storage (Persistence)

**State:** Generated

**Identity:** Territory + Date + Template

**Identifier:** Database ID (implied)

**Representation:** Repository Object (persisted)

**Ownership:** Publication Engine

**Lifecycle:** Generated

**Changes:**

- Identity: UNCHANGED
- Identifier: ADDED (Database ID)
- Representation: ENRICHED (persisted)
- Ownership: UNCHANGED
- Lifecycle: UNCHANGED

**Evidence:** TJS-010 §4.7

---

## Stage 5: Telegram (Delivery)

**State:** Generated → Published

**Identity:** Territory + Date + Template

**Identifier:** Telegram Message ID

**Representation:** Repository Object + Telegram Message

**Ownership:** Publication Engine

**Lifecycle:** Generated → Published

**Changes:**

- Identity: UNCHANGED
- Identifier: ADDED (Telegram Message ID)
- Representation: EXPANDED (Telegram Message added)
- Ownership: UNCHANGED
- Lifecycle: CHANGED (Generated → Published)

**Evidence:** TJS-021 §5.1, TJS-010 §3.3

---

## Stage 6: Update (Data Change)

**State:** Published → Updated → Published

**Identity:** Territory + Date + Template

**Identifier:** Telegram Message ID

**Representation:** Repository Object + Telegram Message

**Ownership:** Publication Engine

**Lifecycle:** Published → Updated → Published

**Changes:**

- Identity: UNCHANGED
- Identifier: UNCHANGED
- Representation: UPDATED (content changed)
- Ownership: UNCHANGED
- Lifecycle: CHANGED (Published → Updated → Published)

**Evidence:** TJS-021 §5.2, §5.3

---

## Stage 7: Archive (Reporting Period Ends)

**State:** Published → Archived

**Identity:** Territory + Date + Template

**Identifier:** Telegram Message ID + Archive Reference

**Representation:** Repository Object + Telegram Message + Historical Record

**Ownership:** Publication Engine

**Lifecycle:** Published → Archived

**Changes:**

- Identity: UNCHANGED
- Identifier: ADDED (Archive Reference)
- Representation: EXPANDED (Historical Record added)
- Ownership: UNCHANGED
- Lifecycle: CHANGED (Published → Archived)

**Evidence:** TJS-021 §5.4

---

## Stage 8: Deletion (Temporary Publications Only)

**State:** Published → Removed

**Identity:** Territory + Date + Template

**Identifier:** None (Telegram Message ID released)

**Representation:** None (Telegram Message deleted)

**Ownership:** None (ownership released)

**Lifecycle:** Published → Removed

**Changes:**

- Identity: UNCHANGED (concept persists)
- Identifier: RELEASED (Telegram Message ID removed)
- Representation: DESTROYED (Telegram Message deleted)
- Ownership: RELEASED
- Lifecycle: CHANGED (Published → Removed)

**Evidence:** TJS-021 §5.5, §5.6

---

# Timeline Summary

| Stage | Identity | Identifier | Representation | Ownership | Lifecycle |
|-------|----------|------------|----------------|-----------|-----------|
| Birth | CREATED | NONE | CREATED | CREATED | CREATED |
| Parser | UNCHANGED | NONE | UNCHANGED | UNCHANGED | UNCHANGED |
| Engine | UNCHANGED | NONE | UNCHANGED | UNCHANGED | UNCHANGED |
| Storage | UNCHANGED | ADDED | ENRICHED | UNCHANGED | UNCHANGED |
| Telegram | UNCHANGED | ADDED | EXPANDED | UNCHANGED | CHANGED |
| Update | UNCHANGED | UNCHANGED | UPDATED | UNCHANGED | CHANGED |
| Archive | UNCHANGED | ADDED | EXPANDED | UNCHANGED | CHANGED |
| Deletion | UNCHANGED | RELEASED | DESTROYED | RELEASED | CHANGED |

---

# Key Insight

**Identity is created at birth and NEVER changes.**

**Identifiers are added and released throughout lifecycle.**

**Representations are created, expanded, updated, and destroyed.**

**Ownership is created and released.**

**Lifecycle changes through transitions.**

**But Identity persists across ALL changes.**

---

# End of Identity Timeline v2
