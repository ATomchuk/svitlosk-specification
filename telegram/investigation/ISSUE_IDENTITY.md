# ISSUE_IDENTITY

**Document ID:** CASE002A-IDENTITY

**Title:** Issue — Identity Analysis

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Investigation

---

# Purpose

This document analyzes Issue identity, separating Object, Identity, Identifier, Representation, and Lifecycle.

---

# Issue Identity Analysis

## Object

**Issue is a Domain Object** — created by SvitloSk business logic.

**Evidence:** TJS-000 §4, TJS-021 §8

**Characteristics:**

- Created by Publication Engine
- Has business meaning
- Has lifecycle
- Has relationships

---

## Identity

**Identity: Calendar day**

**Evidence:** TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"

**Characteristics:**

- Created when first Publication is generated
- Persistent (survives as historical record)
- Unique (one Issue per calendar day)
- Immutable (calendar day cannot change)

**Identity Criteria:**

| Criterion | Value | Evidence |
|-----------|-------|----------|
| Calendar day | Fixed | TJS-000 §4 |
| Temporal scope | One day | TJS-000 §4 |
| Journal membership | Belongs to Journal | TJS-000 §4 |

---

## Identifier

**No explicit Identifier defined.**

**Evidence:** No specification assigns an ID to Issue.

**Possible Identifiers:**

| Candidate | Evidence | Status |
|-----------|----------|--------|
| Calendar date | TJS-000 §4 | IMPLICIT |
| Issue number | No evidence | NOT DEFINED |
| Database ID | No evidence | NOT DEFINED |

**Conclusion:** Issue has no explicit Identifier. Identity is Calendar day (implicit).

---

## Representation

**Representation: Journal concept**

**Evidence:** TJS-000 §4: "Journal → Issue → Publication" hierarchy

**Characteristics:**

- Part of Journal hierarchy
- Conceptual, not physical
- Referenced by Publications
- Preserved as historical record

---

## Lifecycle

**Lifecycle: Opens → Maintained → Closes → Historical**

**Evidence:** TJS-021 §8

**Characteristics:**

- Created by Publication Engine
- Maintained through Publication changes
- Closed when all Publications archived
- Becomes historical after closing

---

# Identity Timeline

| Phase | Identity | Identifier | Representation | Lifecycle |
|-------|----------|------------|----------------|-----------|
| Non-Existence | None | None | None | None |
| Open | Calendar day | None | Journal concept | Opens |
| Maintained | Calendar day | None | Journal concept | Maintained |
| Closed | Calendar day | None | Journal concept | Closes |
| Historical | Calendar day | None | Journal concept | Historical |

---

# Key Insight

**Issue Identity is Calendar day — stable, unique, immutable.**

**Issue has no explicit Identifier.**

**Issue Representation is Journal concept — part of Journal hierarchy.**

**Issue Lifecycle is derived from Publication lifecycle.**

---

# End of Issue Identity
