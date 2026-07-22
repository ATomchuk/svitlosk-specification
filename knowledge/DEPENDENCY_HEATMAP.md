# DEPENDENCY_HEATMAP

**Document ID:** META003-HEATMAP

**Title:** Dependency Heat Map

**Document Class:** Research Audit

**Status:** Stable

**Author:** SvitloSk Project — Repository Research Architect

---

# Purpose

This document constructs a dependency heat map highlighting research coverage.

---

# Dependency Heat Map

## Concept Dependencies

```text
                    Publication (LOCKED)
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
    Information      Identity        Issue
    (DEEPLY)         (LOCKED)        (DEEPLY)
         │               │               │
         ▼               ▼               ▼
    Reality          Identifier      Journal
    (DEEPLY)         (LOCKED)        (DEEPLY)
         │               │               │
         ▼               ▼               ▼
    Knowledge         Publication    Calendar Day
    (DEEPLY)          Identity       (DEEPLY)
                      (LOCKED)
```

---

## Architecture Dependencies

```text
              Publication Engine (PARTIAL)
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
  Parser          Schedule       Graphic
 (NOT)           Generator      Generator
                  (NOT)          (NOT)
    │               │               │
    ▼               ▼               ▼
  Data           Telegram       Data
  Storage        Publisher      Storage
  (NOT)          (PARTIAL)      (NOT)
```

---

## Territory Dependencies

```text
        Community (PARTIAL)
              │
    ┌─────────┴─────────┐
    ▼                   ▼
Administrative      Starosta
Centre (PARTIAL)    District (PARTIAL)
    │                   │
    ▼                   ▼
Settlement         Settlement
(PARTIAL)          (PARTIAL)
    │                   │
    ▼                   ▼
Street             Street
(PARTIAL)          (PARTIAL)
    │                   │
    ▼                   ▼
Address            Address
(PARTIAL)          (PARTIAL)
```

---

## Heat Map Legend

| Color | Meaning |
|-------|---------|
| GREEN | LOCKED / DEEPLY INVESTIGATED |
| YELLOW | PARTIALLY INVESTIGATED |
| RED | NOT INVESTIGATED |

---

## Heat Map Summary

| Region | Green | Yellow | Red |
|--------|-------|--------|-----|
| Publication Concepts | 5 | 2 | 0 |
| Issue Concepts | 5 | 0 | 0 |
| Identity Concepts | 4 | 0 | 0 |
| Information Concepts | 5 | 0 | 0 |
| Ontology Concepts | 5 | 0 | 0 |
| Architecture Concepts | 1 | 2 | 5 |
| Territory Concepts | 0 | 7 | 0 |
| Electricity Concepts | 0 | 0 | 6 |
| **Total** | **20** | **9** | **11** |

---

# Key Insight

**The Repository has strong coverage in Domain concepts (Publication, Issue, Identity, Information).**

**The Repository has WEAK coverage in Architecture concepts (Parser, Schedule Generator, etc.).**

**The Repository has NO coverage in Electricity concepts (Queue, Subqueue, etc.).**

---

# End of Dependency Heat Map
