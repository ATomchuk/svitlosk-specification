# Knowledge Base

**Document Class:** Knowledge Foundation

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document establishes the Knowledge Base — a permanent repository for architectural knowledge discovered through investigations.

---

# Knowledge Base Architecture

## Knowledge Flow

```
Research
    ↓
Finding
    ↓
Validated Finding
    ↓
Canonical Knowledge
    ↓
Specification / ADR
```

## Repository Structure

```
knowledge/
    INDEX.md
    PUBLISHER/
    FINDINGS/
    PRINCIPLES/
    MODELS/
    QUESTIONS/
    HISTORY/
```

---

# Directory Purposes

| Directory | Purpose | Contents |
|-----------|---------|----------|
| PUBLISHER/ | Canonical Publisher Knowledge Base | Publisher_XXX files |
| FINDINGS/ | Validated architectural findings | KF-XXX files |
| PRINCIPLES/ | Architectural principles derived from findings | KP-XXX files |
| MODELS/ | Stable architectural models | KM-XXX files |
| QUESTIONS/ | Unresolved architectural questions | KQ-XXX files |
| HISTORY/ | Historical knowledge artifacts | Investigation artifacts |

---

## PUBLISHER/

**Why:** Canonical Publisher Knowledge Base — the permanent knowledge foundation for future Publisher specifications.

**Content:** README, Concepts, Products, Responsibilities, Operations, Rules, Lifecycle, Relationships, States, Interfaces, Channel Boundary, Glossary.

---

# Knowledge Object Types

## Finding (KF-XXX)

**Definition:** A validated architectural conclusion confirmed by multiple investigations.

**Properties:** ID, Statement, Meaning, Evidence, Confidence, Status

---

## Principle (KP-XXX)

**Definition:** An architectural truth that applies across contexts.

**Properties:** ID, Statement, Evidence, Source, Applications

---

## Model (KM-XXX)

**Definition:** A stable architectural model discovered through investigation.

**Properties:** ID, Description, Components, Relationships, Evidence

---

## Question (KQ-XXX)

**Definition:** An unresolved architectural question requiring future investigation.

**Properties:** ID, Question, Importance, Dependencies, Hypotheses

---

# Knowledge Statuses

| Status | Meaning |
|--------|---------|
| Draft | Newly created, not yet validated |
| Validated | Confirmed by multiple investigations |
| Canonical | Accepted as repository knowledge |
| Retired | No longer relevant |

---

# End of Knowledge Base Index
