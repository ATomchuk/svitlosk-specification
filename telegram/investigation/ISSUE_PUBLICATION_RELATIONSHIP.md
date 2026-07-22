# ISSUE_PUBLICATION_RELATIONSHIP

**Document ID:** CASE002A-RELATIONSHIP

**Title:** Issue — Publication Relationship

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Investigation

---

# Purpose

This document analyzes the relationship between Issue and Publication.

---

# Relationship Analysis

## Evidence

| Source | Statement |
|--------|-----------|
| TJS-000 §4 | "Issue represents one editorial edition of the Journal for a single calendar day" |
| TJS-000 §4 | "Publication represents one independent publication belonging to an Issue" |
| TJS-021 §8.1 | "An Issue opens when the first Publication for a calendar day is generated" |
| TJS-021 §8.2 | "An Issue is maintained through: Publication creation, updates, replacement, removal" |
| TJS-021 §8.3 | "An Issue closes when: All Publications for the day have been archived" |
| TJS-010 §6.5 | "The daily publication package consists of: one post for Starokostiantyniv; one post for every starosta district" |

---

## Relationship Model

```text
Issue (Container)
    │
    ├──→ Contains
    │       │
    │       ├──→ Publication (Territory A)
    │       ├──→ Publication (Territory B)
    │       ├──→ Publication (Territory C)
    │       └──→ ... (more Publications)
    │
    └──→ Temporal Scope: One calendar day
```

---

## Relationship Characteristics

| Characteristic | Value | Evidence |
|----------------|-------|----------|
| Direction | Issue → contains → Publication | TJS-000 §4 |
| Cardinality | One Issue contains many Publications | TJS-010 §6.5 |
| Ownership | Publication Engine owns Publications, not Issue | TJS-010 §4.1 |
| Temporal | Issue scoped to one calendar day | TJS-000 §4 |
| Lifecycle | Issue lifecycle derived from Publication lifecycle | TJS-021 §8 |

---

## Circular Dependency

**Evidence:**

- TJS-000 §4: "Publication represents one independent publication belonging to an Issue"
- TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated"

**Analysis:**

1. Publication belongs to Issue (structural relationship)
2. Issue opens when first Publication is generated (temporal trigger)
3. This creates a circular dependency

**Possible Explanations:**

- Structural relationship (Publication belongs to Issue) vs temporal trigger (Issue opens when Publication generated)
- These are complementary, not contradictory
- Issue is defined by calendar day, not by Publication existence

---

## Compatibility with CASE-001

| Aspect | Compatible? | Evidence |
|--------|-------------|----------|
| Publication Identity | YES | Issue does not affect Publication Identity |
| Publication Lifecycle | YES | Issue lifecycle derived from Publication lifecycle |
| Publication Ownership | YES | Publication Engine owns Publications, not Issue |
| Publication Content | YES | Issue does not affect Publication content |
| Publication Platform | YES | Issue is platform-independent |

---

# Key Insight

**Issue contains Publications for one calendar day.**

**Issue lifecycle is derived from Publication lifecycle.**

**Publication belongs to Issue, but Issue does not own Publications.**

**Circular dependency exists but is resolvable (structural vs temporal).**

---

# End of Issue / Publication Relationship
