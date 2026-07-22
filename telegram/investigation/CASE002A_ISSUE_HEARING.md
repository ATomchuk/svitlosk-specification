# CASE002A_ISSUE_HEARING

**Document ID:** CASE002A-HEARING

**Title:** Issue — Architectural Hearing

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Investigation

---

# Purpose

This document conducts the architectural hearing for the concept of Issue within the SvitloSk domain.

---

# Part 1: Repository Evidence

## Every Occurrence of Issue

| # | Document | Section | Definition/Usage |
|---|----------|---------|------------------|
| 1 | TJS-000 §4 | Primary Concepts | "Issue (Випуск журналу) — Issue represents one editorial edition of the Journal for a single calendar day" |
| 2 | TJS-000 §5 | Semantic Boundaries | "Issue — Owns: Daily edition, date scope; Does NOT own: Formatting, rendering" |
| 3 | TJS-000A §8 | Core Concepts | "Issue — One editorial edition of the Journal for a single calendar day" |
| 4 | TJS-021 §8.1 | Issue Opening | "An Issue opens when the first Publication for a calendar day is generated" |
| 5 | TJS-021 §8.2 | Issue Maintenance | "An Issue is maintained through: Publication creation, updates, replacement, removal" |
| 6 | TJS-021 §8.3 | Issue Closing | "An Issue closes when: All Publications archived, no further updates expected, next day's Issue opens" |
| 7 | TJS-010 §6.5 | Complete Issue | "The daily publication package consists of: one post for Starokostiantyniv; one post for every starosta district" |
| 8 | TJS-020 §4.5 | Issue Integrity | "The integrity of each daily edition SHALL be preserved for public accountability" |
| 9 | GLOSSARY.md §3 | Publication Model | "Publication represents one independent publication belonging to an Issue" |
| 10 | CASE001 investigations | Multiple | "Issue is the TEMPORAL CONTAINER for Publications" |

---

# Part 2: Semantic Reconstruction

## Semantic Meaning 1: Editorial Edition

**Source:** TJS-000 §4, TJS-000A §8

**Definition:** One editorial edition of the Journal for a single calendar day.

**Evidence:** "Issue represents one editorial edition of the Journal for a single calendar day"

---

## Semantic Meaning 2: Temporal Container

**Source:** TJS-021 §8, CASE001 investigations

**Definition:** A container that holds Publications for one calendar day.

**Evidence:** "An Issue opens when the first Publication for a calendar day is generated"

---

## Semantic Meaning 3: Daily Edition

**Source:** TJS-000 §5, TJS-010 §6.5

**Definition:** The daily edition of the Journal containing all Publications for that day.

**Evidence:** "Issue — Owns: Daily edition, date scope"

---

## Semantic Meaning 4: Journal Unit

**Source:** TJS-000 §4 (hierarchy)

**Definition:** A unit in the hierarchy: Journal → Issue → Publication.

**Evidence:** "Journal (Журнал) ↓ Issue (Випуск журналу) ↓ Publication (Публікація)"

---

## Semantic Meaning 5: Historical Record Container

**Source:** TJS-021 §8.3, TJS-020 §4.5

**Definition:** A container that preserves daily publications as historical record.

**Evidence:** "The Issue remains available as part of the historical record after closing"

---

# Part 3: Competing Models

## Model A: Issue as Container

**Definition:** Issue is a temporal container that holds Publications for one calendar day.

**Evidence:**

- TJS-021 §8.2: "An Issue is maintained through: Publication creation, updates, replacement, removal"
- CASE001: "Issue is the TEMPORAL CONTAINER for Publications"

**Characteristics:**

- Contains Publications
- Has no content of its own
- Exists only to group Publications
- Temporal scope: one calendar day

---

## Model B: Issue as Editorial Unit

**Definition:** Issue is one editorial edition of the Journal for a single calendar day.

**Evidence:**

- TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"
- TJS-000A §8: "One editorial edition of the Journal for a single calendar day"

**Characteristics:**

- Has editorial purpose
- Represents one day's editorial output
- Part of Journal hierarchy
- Has editorial integrity requirements

---

## Model C: Issue as Business Object

**Definition:** Issue is a business concept representing daily editorial output.

**Evidence:**

- TJS-000 §5: "Issue — Owns: Daily edition, date scope"
- TJS-020 §4.5: "The integrity of each daily edition SHALL be preserved"

**Characteristics:**

- Has business meaning
- Has ownership (Editorial System)
- Has lifecycle (Opens → Maintained → Closes)
- Has integrity requirements

---

## Model D: Issue as Time Slice

**Definition:** Issue is a temporal slice of the Journal's continuous publication.

**Evidence:**

- TJS-000 §4: "Journal represents the continuous informational publication"
- TJS-000 §4: "Issue represents one editorial edition... for a single calendar day"

**Characteristics:**

- Temporal boundary: one calendar day
- Part of continuous Journal
- Slice of ongoing publication
- Time-bounded

---

## Model E: Issue as Publication Collection

**Definition:** Issue is a collection of Publications for one reporting period.

**Evidence:**

- TJS-010 §6.5: "The daily publication package consists of: one post for Starokostiantyniv; one post for every starosta district"
- TJS-021 §8.2: "An Issue is maintained through: Publication creation, updates, replacement, removal"

**Characteristics:**

- Contains multiple Publications
- Grouped by calendar day
- Has composition rules
- Has completeness requirements

---

## Model F: Issue as Historical Record

**Definition:** Issue is a preserved daily edition for historical reference.

**Evidence:**

- TJS-021 §8.3: "The Issue remains available as part of the historical record after closing"
- TJS-020 §4.5: "The integrity of each daily edition SHALL be preserved for public accountability"

**Characteristics:**

- Permanent after closing
- Preserved for accountability
- Historical reference
- Immutable after archival

---

## Model G: Issue as Process

**Definition:** Issue is a daily editorial process that opens, fills, and closes.

**Evidence:**

- TJS-021 §8.1: "An Issue opens when..."
- TJS-021 §8.2: "An Issue is maintained through..."
- TJS-021 §8.3: "An Issue closes when..."

**Characteristics:**

- Has opening trigger
- Has maintenance activities
- Has closing conditions
- Temporal process

---

# Part 4: Deep Cross Examination

## For Every Model

### Model A: Issue as Container

| Question | Answer | Evidence |
|----------|--------|----------|
| What creates Issue? | Publication Engine (when first Publication is generated) | TJS-021 §8.1 |
| Can Issue exist before Publication? | NO — Issue opens when first Publication is generated | TJS-021 §8.1 |
| Can Publication exist before Issue? | UNCLEAR — circular dependency | TJS-000 §4, TJS-021 §8.1 |
| Does Issue own Publication? | NO — Publication Engine owns Publications | TJS-010 §4.1 |
| Does Publication own Issue? | NO — Issue is a container | TJS-000 §4 |
| Can Issue exist without Publications? | NO — Issue opens when first Publication is generated | TJS-021 §8.1 |
| Can Issue contain zero Publications? | NO — Issue requires at least one Publication | TJS-021 §8.1 |
| Can one Publication belong to multiple Issues? | NO — one Publication belongs to one Issue | TJS-000 §4 |
| Can Issue survive Publication deletion? | UNCLEAR — no evidence | — |
| Can Issue survive forever? | YES — remains as historical record | TJS-021 §8.3 |
| Can Issue be recreated? | NO — one Issue per calendar day | TJS-000 §4 |
| Is Issue temporal? | YES — bounded by calendar day | TJS-000 §4 |
| Is Issue historical? | YES — preserved after closing | TJS-021 §8.3 |
| Is Issue immutable? | NO — maintained through Publication changes | TJS-021 §8.2 |

### Model B: Issue as Editorial Unit

| Question | Answer | Evidence |
|----------|--------|----------|
| What creates Issue? | Editorial System (conceptually) | TJS-000 §4 |
| Can Issue exist before Publication? | NO — Issue opens when first Publication is generated | TJS-021 §8.1 |
| Can Publication exist before Issue? | UNCLEAR — circular dependency | TJS-000 §4, TJS-021 §8.1 |
| Does Issue own Publication? | NO — Issue contains, does not own | TJS-000 §5 |
| Does Publication own Issue? | NO | — |
| Can Issue exist without Publications? | NO | TJS-021 §8.1 |
| Can Issue contain zero Publications? | NO | TJS-021 §8.1 |
| Can one Publication belong to multiple Issues? | NO | TJS-000 §4 |
| Can Issue survive Publication deletion? | UNCLEAR | — |
| Can Issue survive forever? | YES — historical record | TJS-021 §8.3 |
| Can Issue be recreated? | NO | TJS-000 §4 |
| Is Issue temporal? | YES | TJS-000 §4 |
| Is Issue historical? | YES | TJS-021 §8.3 |
| Is Issue immutable? | NO | TJS-021 §8.2 |

### Model C: Issue as Business Object

| Question | Answer | Evidence |
|----------|--------|----------|
| What creates Issue? | Publication Engine / Editorial System | TJS-021 §8.1 |
| Can Issue exist before Publication? | NO | TJS-021 §8.1 |
| Can Publication exist before Issue? | UNCLEAR | — |
| Does Issue own Publication? | NO | TJS-010 §4.1 |
| Does Publication own Issue? | NO | — |
| Can Issue exist without Publications? | NO | TJS-021 §8.1 |
| Can Issue contain zero Publications? | NO | TJS-021 §8.1 |
| Can one Publication belong to multiple Issues? | NO | TJS-000 §4 |
| Can Issue survive Publication deletion? | UNCLEAR | — |
| Can Issue survive forever? | YES | TJS-021 §8.3 |
| Can Issue be recreated? | NO | TJS-000 §4 |
| Is Issue temporal? | YES | TJS-000 §4 |
| Is Issue historical? | YES | TJS-021 §8.3 |
| Is Issue immutable? | NO | TJS-021 §8.2 |

### Model D: Issue as Time Slice

| Question | Answer | Evidence |
|----------|--------|----------|
| What creates Issue? | Calendar (temporal boundary) | TJS-000 §4 |
| Can Issue exist before Publication? | NO | TJS-021 §8.1 |
| Can Publication exist before Issue? | UNCLEAR | — |
| Does Issue own Publication? | NO | — |
| Does Publication own Issue? | NO | — |
| Can Issue exist without Publications? | NO | TJS-021 §8.1 |
| Can Issue contain zero Publications? | NO | TJS-021 §8.1 |
| Can one Publication belong to multiple Issues? | NO | TJS-000 §4 |
| Can Issue survive Publication deletion? | UNCLEAR | — |
| Can Issue survive forever? | YES | TJS-021 §8.3 |
| Can Issue be recreated? | NO | TJS-000 §4 |
| Is Issue temporal? | YES | TJS-000 §4 |
| Is Issue historical? | YES | TJS-021 §8.3 |
| Is Issue immutable? | NO | — |

### Model E: Issue as Publication Collection

| Question | Answer | Evidence |
|----------|--------|----------|
| What creates Issue? | Publication Engine (when first Publication is generated) | TJS-021 §8.1 |
| Can Issue exist before Publication? | NO | TJS-021 §8.1 |
| Can Publication exist before Issue? | UNCLEAR | — |
| Does Issue own Publication? | NO — collection contains, does not own | — |
| Does Publication own Issue? | NO | — |
| Can Issue exist without Publications? | NO | TJS-021 §8.1 |
| Can Issue contain zero Publications? | NO | TJS-021 §8.1 |
| Can one Publication belong to multiple Issues? | NO | TJS-000 §4 |
| Can Issue survive Publication deletion? | UNCLEAR | — |
| Can Issue survive forever? | YES | TJS-021 §8.3 |
| Can Issue be recreated? | NO | TJS-000 §4 |
| Is Issue temporal? | YES | TJS-000 §4 |
| Is Issue historical? | YES | TJS-021 §8.3 |
| Is Issue immutable? | NO | TJS-021 §8.2 |

### Model F: Issue as Historical Record

| Question | Answer | Evidence |
|----------|--------|----------|
| What creates Issue? | Archival process | TJS-021 §8.3 |
| Can Issue exist before Publication? | NO | TJS-021 §8.1 |
| Can Publication exist before Issue? | UNCLEAR | — |
| Does Issue own Publication? | NO — preserves, does not own | — |
| Does Publication own Issue? | NO | — |
| Can Issue exist without Publications? | NO | TJS-021 §8.1 |
| Can Issue contain zero Publications? | NO | TJS-021 §8.1 |
| Can one Publication belong to multiple Issues? | NO | TJS-000 §4 |
| Can Issue survive Publication deletion? | UNCLEAR | — |
| Can Issue survive forever? | YES — historical record | TJS-021 §8.3 |
| Can Issue be recreated? | NO | — |
| Is Issue temporal? | YES | TJS-000 §4 |
| Is Issue historical? | YES — IS historical record | TJS-021 §8.3 |
| Is Issue immutable? | YES — after archival | TJS-021 §8.3 |

### Model G: Issue as Process

| Question | Answer | Evidence |
|----------|--------|----------|
| What creates Issue? | Trigger (first Publication generated) | TJS-021 §8.1 |
| Can Issue exist before Publication? | NO | TJS-021 §8.1 |
| Can Publication exist before Issue? | UNCLEAR | — |
| Does Issue own Publication? | NO | — |
| Does Publication own Issue? | NO | — |
| Can Issue exist without Publications? | NO | TJS-021 §8.1 |
| Can Issue contain zero Publications? | NO | TJS-021 §8.1 |
| Can one Publication belong to multiple Issues? | NO | TJS-000 §4 |
| Can Issue survive Publication deletion? | UNCLEAR | — |
| Can Issue survive forever? | YES — becomes historical | TJS-021 §8.3 |
| Can Issue be recreated? | NO — one process per day | TJS-000 §4 |
| Is Issue temporal? | YES — IS temporal process | TJS-021 §8 |
| Is Issue historical? | YES — becomes historical | TJS-021 §8.3 |
| Is Issue immutable? | NO — process changes | TJS-021 §8.2 |

---

# Part 5: Identity

## Object

**Issue is a Domain Object** — created by SvitloSk business logic.

**Evidence:** TJS-000 §4, TJS-021 §8

---

## Identity

**Identity: Calendar day**

**Evidence:** TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"

**Characteristics:**

- Created when first Publication is generated
- Persistent (survives as historical record)
- Unique (one Issue per calendar day)

---

## Identifier

**No explicit Identifier defined.**

**Evidence:** No specification assigns an ID to Issue.

---

## Representation

**Representation: Journal concept**

**Evidence:** TJS-000 §4: "Journal → Issue → Publication" hierarchy

---

## Lifecycle

**Lifecycle: Opens → Maintained → Closes → Historical**

**Evidence:** TJS-021 §8

---

# Part 6: Lifecycle

## Complete Lifecycle

```text
Non-Existence
    │
    │ Trigger: First Publication for calendar day generated
    │ Actor: Publication Engine
    ▼
Open
    │
    │ Activity: Publication creation, updates, replacement, removal
    │ Actor: Publication Engine
    ▼
Maintained
    │
    │ Trigger: All Publications archived, no further updates expected
    │ Actor: Publication Engine (automated)
    ▼
Closed
    │
    │ State: Historical record
    │ Duration: Permanent
    ▼
Historical
```

---

# Part 7: Behaviour

## Actions Issue Performs

| Action | Evidence |
|--------|----------|
| Contains Publications | TJS-000 §4, TJS-021 §8.2 |
| Preserves daily edition | TJS-021 §8.3 |
| Maintains editorial integrity | TJS-020 §4.5 |

---

## Actions Performed ON Issue

| Action | Actor | Evidence |
|--------|-------|----------|
| Opening | Publication Engine | TJS-021 §8.1 |
| Maintenance | Publication Engine | TJS-021 §8.2 |
| Closing | Publication Engine | TJS-021 §8.3 |
| Archival | Publication Engine | TJS-021 §8.3 |

---

# Part 8: Ontological Position

## Where Issue Belongs

| Layer | Belongs? | Evidence |
|-------|----------|----------|
| Reality | NO | Issue does not exist in reality |
| Business | YES | Issue is a business concept |
| Information | NO | Issue is not information |
| Representation | NO | Issue is not a representation |
| Architecture | NO | Issue is not an architectural component |
| Governance | NO | Issue is not a governance concept |

**Conclusion:** Issue belongs to the **Business Domain**.

---

# Part 9: Contradictions

## Contradiction 1: Publication Belongs to Issue vs Issue Appears After First Publication

**Evidence:**

- TJS-000 §4: "Publication represents one independent publication belonging to an Issue"
- TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated"

**Severity:** HIGH

**Possible Explanation:** Circular dependency. Publication belongs to Issue, but Issue is created by Publication. This is a temporal paradox.

---

## Contradiction 2: Issue Has No Explicit Identifier

**Evidence:**

- DATA_MODEL.md: "Every logical entity SHALL be uniquely identifiable"
- No Issue ID defined in any specification

**Severity:** MEDIUM

**Possible Explanation:** Issue identity is Calendar day (implicit), not explicit identifier.

---

## Contradiction 3: Issue Ownership Unclear

**Evidence:**

- TJS-010 §4.1: Publication Engine owns Publications
- No specification states who owns Issue

**Severity:** MEDIUM

**Possible Explanation:** Issue is a container, not an owned object. Or Editorial System owns Issue (implied by TJS-000 §5).

---

## Contradiction 4: Issue Lifecycle vs Publication Lifecycle

**Evidence:**

- TJS-021 defines Publication lifecycle in detail
- TJS-021 §8 defines Issue lifecycle briefly
- Issue lifecycle is less detailed than Publication lifecycle

**Severity:** LOW

**Possible Explanation:** Issue lifecycle is derived from Publication lifecycle.

---

# Part 10: Cross-reference with CASE-001

## Issue Models vs Publication

| Issue Model | Compatible with Publication? | Evidence |
|-------------|------------------------------|----------|
| Container | YES | Publication is contained in Issue |
| Editorial Unit | YES | Publication is part of editorial edition |
| Business Object | YES | Both are business objects |
| Time Slice | YES | Publication belongs to time slice |
| Publication Collection | YES | Publication is element of collection |
| Historical Record | YES | Publication is preserved in Issue |
| Process | YES | Publication is output of Issue process |

---

# Part 11: Unanswered Questions

| # | Question | Type | Impact |
|---|----------|------|--------|
| 1 | What creates Issue — Publication Engine or Editorial System? | Repository gap | HIGH |
| 2 | Can Issue exist without Publications? | Conceptual gap | HIGH |
| 3 | Can Issue survive Publication deletion? | Missing evidence | MEDIUM |
| 4 | Who owns Issue? | Repository gap | MEDIUM |
| 5 | Does Issue have an Identifier? | Repository gap | MEDIUM |
| 6 | Is Issue immutable after closing? | Conceptual gap | LOW |
| 7 | Can Issue be recreated? | Conceptual gap | LOW |
| 8 | What is the relationship between Issue and Reporting Period? | Missing evidence | LOW |

---

# End of Issue Hearing
