# WORLD_B

**Document ID:** CASE001F-WORLD-B

**Title:** World B — Publication Does NOT Exist (Replaced by Issue)

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Publication Existence Investigation

---

# Purpose

This document describes World B where Publication does not exist and is replaced by Issue.

---

# World B: Publication Does NOT Exist

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
        ▼
    Issue Package
        │
        ▼
  Telegram Publisher
        │
        ▼
  Telegram Channel
        │
        ▼
    Subscribers
```

---

## Proposed Semantic Hierarchy

```text
Journal
    │
    └──→ Issue (contains all daily content)
              │
              └──→ Telegram
```

---

## Changes Required

| # | Change | Impact |
|---|--------|--------|
| 1 | Rename "Publication" to "Issue" throughout | HIGH — affects all documents |
| 2 | Merge Publication and Issue into single concept | HIGH — architectural change |
| 3 | Update lifecycle to apply to Issue | HIGH — lifecycle redesign |
| 4 | Update identity to Calendar day | MEDIUM — identity change |
| 5 | Update ownership model | MEDIUM — ownership change |
| 6 | Update all specifications | HIGH — documentation change |

---

## Consequences

| Aspect | Change | Severity |
|--------|--------|----------|
| Semantic hierarchy | Journal → Issue (no Publication level) | HIGH |
| Lifecycle | Issue has Generated, Published, Updated, Archived, Removed | HIGH |
| Identity | Issue identified by Calendar day | MEDIUM |
| Ownership | Issue owned by Publication Engine | MEDIUM |
| Territorial granularity | LOST — Issue is per day, not per territory | HIGH |
| Telegram delivery | Issue delivered directly to Telegram | MEDIUM |
| Repository consistency | BROKEN — all references to Publication must change | HIGH |

---

## Problems

### Problem 1: Loss of Territorial Granularity

**Current:** Publication is per Territory (Starokostiantyniv, Samchyky SO, etc.)

**World B:** Issue is per Calendar day (one Issue per day)

**Consequence:** Cannot distinguish between different territories within one day

---

### Problem 2: Identity Mismatch

**Current:** Publication identity = Territory + Date + Template

**World B:** Issue identity = Calendar day

**Consequence:** Two Publications for same day but different territories would have same identity

---

### Problem 3: Circular Dependency Remains

**Current:** Publication belongs to Issue; Issue opens when first Publication generated

**World B:** Issue belongs to Journal; Issue opens when... when?

**Consequence:** Issue still needs a trigger, but no Publication exists to trigger it

---

### Problem 4: Lifecycle Complexity

**Current:** Publication lifecycle is well-defined (5 states)

**World B:** Issue lifecycle would need to absorb all Publication lifecycle states

**Consequence:** Issue becomes more complex, not simpler

---

## System Status

**Architecture:** REQUIRES MAJOR RESTRUCTURING

**Lifecycle:** PARTIALLY WORKING — needs expansion

**Identity:** INCONSISTENT — territory granularity lost

**Ownership:** PARTIALLY VALID — needs revision

---

# End of World B
