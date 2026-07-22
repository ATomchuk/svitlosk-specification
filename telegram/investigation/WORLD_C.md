# WORLD_C

**Document ID:** CASE001F-WORLD-C

**Title:** World C — Publication Becomes Only Representation

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Publication Existence Investigation

---

# Purpose

This document describes World C where Publication disappears and only representations remain.

---

# World C: Publication Becomes Only Representation

## Proposed Architecture

```text
External Data Sources
        │
        ▼
      Parser
        │
        ▼
  Normalized Dataset
        │
        ▼
  Publication Engine
        │
        ├──→ Telegram Message (for Telegram)
        ├──→ Repository Entry (for storage)
        └──→ Archive Entry (for history)
```

---

## Proposed Domain Concepts

```text
Journal
    │
    └──→ Issue
              │
              ├──→ Telegram Message
              ├──→ Repository Entry
              └──→ Archive Entry
```

---

## Changes Required

| # | Change | Impact |
|---|--------|--------|
| 1 | Remove "Publication" as domain concept | HIGH — architectural change |
| 2 | Telegram Message becomes primary | HIGH — platform-dependent |
| 3 | Repository Entry becomes primary | HIGH — storage-dependent |
| 4 | Archive Entry becomes primary | HIGH — history-dependent |
| 5 | Each has its own lifecycle | HIGH — lifecycle fragmentation |
| 6 | Each has its own identity | HIGH — identity fragmentation |
| 7 | Each has its own ownership | HIGH — ownership fragmentation |

---

## Consequences

| Aspect | Change | Severity |
|--------|--------|----------|
| Domain concepts | No Publication — only platform artifacts | HIGH |
| Lifecycle | Multiple conflicting lifecycles | HIGH |
| Identity | Multiple identities (Telegram Message ID, Database ID, Archive Reference) | HIGH |
| Ownership | Multiple owners (Telegram Publisher, Data Storage, Archive) | HIGH |
| Consistency | No single concept across representations | HIGH |
| Traceability | Broken — no single concept to trace | HIGH |
| Determinism | Broken — each representation may differ | HIGH |

---

## Problems

### Problem 1: No Single Domain Concept

**Current:** Publication is the single domain concept across all representations

**World C:** Telegram Message, Repository Entry, Archive Entry are separate concepts

**Consequence:** No unified domain model

---

### Problem 2: Platform Dependency

**Current:** Publication is platform-independent

**World C:** Telegram Message is platform-dependent

**Consequence:** System becomes tied to Telegram

---

### Problem 3: Lifecycle Fragmentation

**Current:** Publication has single lifecycle (Generated → Published → Updated → Archived → Removed)

**World C:** Each representation has its own lifecycle

**Consequence:** No unified lifecycle management

---

### Problem 4: Identity Fragmentation

**Current:** Publication has single identity (Territory + Date + Template)

**World C:** Each representation has its own identity

**Consequence:** No unified identity model

---

### Problem 5: Ownership Fragmentation

**Current:** Publication has single owner (Publication Engine)

**World C:** Each representation has its own owner

**Consequence:** No unified ownership model

---

## System Status

**Architecture:** FRAGMENTED

**Lifecycle:** BROKEN — multiple conflicting lifecycles

**Identity:** BROKEN — multiple identities

**Ownership:** BROKEN — multiple owners

---

# End of World C
