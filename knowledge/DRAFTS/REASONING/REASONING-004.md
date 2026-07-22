# REASONING-004_Issue_Became_Problematic

**Document ID:** REASONING-004

**Title:** Why Issue Became Problematic

**Status:** Draft

---

# Reasoning Chain

## Step 1: Issue Has Circular Dependency with Publication

- TJS-000 §4: "Publication represents one independent publication belonging to an Issue"
- TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated"
- Publication belongs to Issue, but Issue is created by Publication
- This is a circular dependency

---

## Step 2: Issue Has No Explicit Identifier

- No specification defines an Issue ID
- Issue identity is Calendar day (implicit)
- DATA_MODEL.md requires "uniquely identifiable" but no Issue ID exists

---

## Step 3: Issue Ownership Is Unclear

- TJS-000 §5: "Issue — Owns: Daily edition, date scope"
- But no specification states who owns Issue
- TJS-010 §4.1: Publication Engine owns Publications, not Issues

---

## Step 4: Issue Lifecycle Is Derived

- Issue lifecycle is defined in terms of Publication lifecycle
- Issue opens when first Publication is generated
- Issue closes when all Publications are archived
- Issue lifecycle depends on Publication lifecycle

---

## Step 5: Issue Is Derivative

- Issue exists only because Publications need to be grouped
- If Publications did not exist, Issue would have no purpose
- Issue is a convenience abstraction, not a foundational entity

---

# Conclusion

Issue is problematic because it has circular dependency with Publication, no explicit identifier, unclear ownership, derived lifecycle, and derivative nature. These issues suggest Issue is not a fundamental concept.

---

# Evidence

- CASE-002A: Issue Hearing
- CASE-002B: Issue Object vs Process
- CASE-001: Publication Investigation
- CASE-001D: Identity vs Identifier

---

# Origin Investigations

- CASE-002A
- CASE-002B
- CASE-001
- CASE-001D

---

# End of Reasoning
