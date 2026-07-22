# PUBLICATION_MERGE_EXPERIMENT

**Document ID:** CASE001F-MERGE

**Title:** Publication Merge Experiment

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Publication Existence Investigation

---

# Purpose

This document attempts to merge Publication into Issue.

---

# Experiment: Merge Publication into Issue

## Proposed Merge

**Concept:** Publication disappears. Issue absorbs all Publication properties.

**Before:**

```text
Journal → Issue → Publication → Telegram
```

**After:**

```text
Journal → Issue → Telegram
```

---

## Properties to Merge

| Publication Property | Can Issue Absorb? | Evidence |
|----------------------|-------------------|----------|
| Territory identity | NO — Issue has Calendar day identity | TJS-000 §4 |
| Template identity | NO — Issue has no template concept | — |
| Lifecycle states | PARTIALLY — Issue lifecycle is simpler | TJS-021 §8 |
| Ownership model | NO — Issue ownership is undefined | — |
| Determinism | NO — Issue determinism is not defined | — |
| Traceability | NO — Issue traceability is not defined | — |
| Editorial integrity | PARTIALLY — Issue has integrity requirements | TJS-020 §4.5 |

---

## Problems with Merge

### Problem 1: Identity Conflict

**Publication Identity:** Territory + Date + Template

**Issue Identity:** Calendar day

**Conflict:** Two Publications for same day but different territories would have same Issue identity.

**Evidence:** TJS-000 §4 defines Issue as "one editorial edition for a single calendar day"

---

### Problem 2: Granularity Loss

**Publication:** Per Territory (Starokostiantyniv, Samchyky SO, etc.)

**Issue:** Per Calendar day (one Issue per day)

**Conflict:** Merging loses the ability to distinguish between different territories within one day.

**Evidence:** TJS-005 defines Canonical Templates for different territories

---

### Problem 3: Lifecycle Mismatch

**Publication Lifecycle:** Generated → Published → Updated → Archived → Removed (5 states)

**Issue Lifecycle:** Opens → Maintained → Closes (3 phases)

**Conflict:** Issue lifecycle is simpler and cannot absorb all Publication lifecycle states.

**Evidence:** TJS-021 §4 vs TJS-021 §8

---

### Problem 4: Ownership Gap

**Publication Owner:** Publication Engine (clearly defined)

**Issue Owner:** Unknown (no specification defines it)

**Conflict:** Merging would create ownership ambiguity.

**Evidence:** TJS-010 §4.1 defines Publication Engine ownership; no Issue ownership defined

---

### Problem 5: Circular Dependency Remains

**Current:** Publication belongs to Issue; Issue opens when first Publication generated

**Merged:** Issue belongs to Journal; Issue opens when... when?

**Conflict:** Issue still needs a trigger, but no Publication exists to trigger it.

**Evidence:** TJS-021 §8.1

---

### Problem 6: Telegram Delivery Breaks

**Current:** Publication Engine produces Publication Package → Telegram Publisher delivers

**Merged:** Publication Engine produces... what? Issue Package?

**Conflict:** Telegram Publisher expects Publication, not Issue.

**Evidence:** TJS-010 §3.3

---

## Consequences of Merge

| Aspect | Consequence | Severity |
|--------|-------------|----------|
| Identity | Territory granularity lost | HIGH |
| Lifecycle | Issue becomes more complex | HIGH |
| Ownership | Ownership becomes ambiguous | MEDIUM |
| Telegram delivery | Delivery mechanism breaks | HIGH |
| Repository consistency | All references must change | HIGH |
| Semantic hierarchy | Journal → Issue → Telegram (flatter) | MEDIUM |

---

# Conclusion

**Publication CANNOT be merged into Issue.**

**The merge fails because:**

1. Identity conflict (territory vs calendar day)
2. Granularity loss (territory-level vs day-level)
3. Lifecycle mismatch (5 states vs 3 phases)
4. Ownership gap (defined vs undefined)
5. Circular dependency remains
6. Telegram delivery breaks

---

# End of Merge Experiment
