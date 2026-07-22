# REPOSITORY_CONCEPT_CLASSIFICATION

**Document ID:** META001-CLASSIFICATION

**Title:** Repository Concept Classification

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Ontological Types Investigation

---

# Purpose

This document classifies every repository concept into ontological types.

---

# Repository Concept Classification

## Publication

**Primary Type:** Object (Domain Object)

**Secondary Type:** Information Object

**Evidence:**

- Has identity (Territory + Date + Template)
- Has lifecycle (Generated → Published → Archived)
- Contains Information (content)
- Created for Communication purpose

---

## Issue

**Primary Type:** Object (Domain Object)

**Secondary Type:** Collection

**Evidence:**

- Has identity (Calendar day)
- Has lifecycle (Opens → Maintained → Closes)
- Contains Publications (collection)

---

## Journal

**Primary Type:** Collection (Aggregate)

**Secondary Type:** Object

**Evidence:**

- Contains Issues (collection)
- Has identity (continuous publication)
- Has lifecycle (permanent)

---

## Publication Package

**Primary Type:** Collection (Aggregate)

**Secondary Type:** Object

**Evidence:**

- Contains Publications (collection)
- Has identity (Reporting Period)
- Has lifecycle (Generated → Delivered)

---

## Parser

**Primary Type:** Object (Architectural Object)

**Secondary Type:** Process

**Evidence:**

- Has identity (component name)
- Performs data retrieval (process)

---

## Publication Engine

**Primary Type:** Object (Architectural Object)

**Secondary Type:** Process

**Evidence:**

- Has identity (component name)
- Performs publication generation (process)

---

## Publisher

**Primary Type:** Role

**Secondary Type:** —

**Evidence:**

- Describes responsibility (role)
- No identity, no lifecycle

---

## Schedule Generator

**Primary Type:** Object (Architectural Object)

**Secondary Type:** Process

**Evidence:**

- Has identity (component name)
- Performs schedule generation (process)

---

## Graphic Generator

**Primary Type:** Object (Architectural Object)

**Secondary Type:** Process

**Evidence:**

- Has identity (component name)
- Performs graphic generation (process)

---

## Telegram Publisher

**Primary Type:** Object (Architectural Object)

**Secondary Type:** Process

**Evidence:**

- Has identity (component name)
- Performs delivery (process)

---

## Telegram Message

**Primary Type:** Carrier

**Secondary Type:** Representation

**Evidence:**

- Medium holding Publication (carrier)
- Portrays Publication content (representation)

---

## Telegram Channel

**Primary Type:** Boundary

**Secondary Type:** Carrier

**Evidence:**

- Demarcation for delivery (boundary)
- Medium for communication (carrier)

---

## Territory

**Primary Type:** Boundary

**Secondary Type:** Object

**Evidence:**

- Defines scope (boundary)
- Has identity (administrative name)

---

## Community

**Primary Type:** Boundary

**Secondary Type:** Object

**Evidence:**

- Defines scope (boundary)
- Has identity (administrative name)

---

## Settlement

**Primary Type:** Object (Domain Object)

**Secondary Type:** —

**Evidence:**

- Has identity (official name)
- Physical location

---

## Street

**Primary Type:** Object (Domain Object)

**Secondary Type:** —

**Evidence:**

- Has identity (official name)
- Physical road

---

## Address

**Primary Type:** Object (Domain Object)

**Secondary Type:** —

**Evidence:**

- Has identity (official designation)
- Physical location

---

## Schedule

**Primary Type:** Object (Information Object)

**Secondary Type:** Information

**Evidence:**

- Has identity (unique per generation)
- Contains Information (outage schedule)

---

## Time Interval

**Primary Type:** Object (Domain Object)

**Secondary Type:** —

**Evidence:**

- Has identity (start + end time)
- Temporal concept

---

## Normalized Dataset

**Primary Type:** Information

**Secondary Type:** Representation

**Evidence:**

- Structured Information
- Machine-readable representation

---

## Interpretation Result

**Primary Type:** Information

**Secondary Type:** Representation

**Evidence:**

- Information for residents
- Normalized representation

---

## Processing Cycle

**Primary Type:** Process

**Secondary Type:** Event

**Evidence:**

- Sequence of actions (process)
- One complete execution (event)

---

## Historical Archive

**Primary Type:** Collection

**Secondary Type:** Carrier

**Evidence:**

- Preserves records (collection)
- Stores Information (carrier)

---

## Issue Lifecycle

**Primary Type:** Lifecycle

**Secondary Type:** Process

**Evidence:**

- Sequence of states (lifecycle)
- Manages Issue evolution (process)

---

## Publication Lifecycle

**Primary Type:** Lifecycle

**Secondary Type:** Process

**Evidence:**

- Sequence of states (lifecycle)
- Manages Publication evolution (process)

---

## Open Data

**Primary Type:** Information

**Secondary Type:** Evidence

**Evidence:**

- Officially published Information
- Provides evidence of Reality

---

## Data Source

**Primary Type:** Object (Domain Object)

**Secondary Type:** Role

**Evidence:**

- Has identity (organization name)
- Performs data provision (role)

---

## DSO

**Primary Type:** Object (Domain Object)

**Secondary Type:** Role

**Evidence:**

- Has identity (organization name)
- Performs electricity distribution (role)

---

## Resident

**Primary Type:** Object (Domain Object)

**Secondary Type:** Role

**Evidence:**

- Has identity (person)
- Uses SvitloSk (role)

---

## Information Consumer

**Primary Type:** Role

**Secondary Type:** —

**Evidence:**

- Describes receiving Publications (role)

---

## Stakeholder

**Primary Type:** Role

**Secondary Type:** —

**Evidence:**

- Describes having interest (role)

---

## Component

**Primary Type:** Object (Architectural Object)

**Secondary Type:** —

**Evidence:**

- Has identity (component name)
- Architectural building block

---

## Role

**Primary Type:** Role

**Secondary Type:** —

**Evidence:**

- Describes responsibility
- Implementation-independent

---

# Classification Summary

| Primary Type | Count |
|--------------|-------|
| Object | 24 |
| Collection | 3 |
| Carrier | 1 |
| Boundary | 3 |
| Information | 3 |
| Process | 1 |
| Lifecycle | 2 |
| Role | 5 |
| **Total** | **36** |

---

# Key Insight

**Object is the DOMINANT type — 24 of 36 concepts are Objects.**

**This confirms that SvitloSk is primarily an OBJECT-ORIENTED domain.**

---

# End of Repository Concept Classification
