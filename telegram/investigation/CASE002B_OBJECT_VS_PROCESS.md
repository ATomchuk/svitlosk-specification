# CASE002B_OBJECT_VS_PROCESS

**Document ID:** CASE002B-MAIN

**Title:** Object vs Process Hearing — Issue Ontology

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Ontology Investigation

---

# Purpose

This document investigates whether Issue is actually an Object or something fundamentally different.

---

# Part 1: The Hidden Assumption

## Hypothesis H1: Issue IS an Object

**Assumption:** Issue is a thing that exists, has identity, has properties, and has lifecycle.

**Evidence Supporting H1:**

- TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"
- TJS-000A §8: "One editorial edition of the Journal for a single calendar day"
- TJS-021 §8: Issue has lifecycle (opens → maintained → closes → historical)
- TJS-000 §5: Issue "Owns: Daily edition, date scope"
- CASE001 investigations: Issue is classified as "Domain Object"

**Evidence Contradicting H1:**

- Issue has no explicit identifier
- Issue ownership is unclear
- Issue lifecycle is derived from Publication lifecycle
- Issue appears to be defined by its relationship to Publications

---

## Hypothesis H2: Issue is NOT an Object

**Assumption:** Issue is not a thing, but something else — perhaps a process, a boundary, or a window.

**Evidence Supporting H2:**

- TJS-021 §8.1: "An Issue opens when the first Publication... is generated" — Issue is TRIGGERED, not CREATED
- TJS-021 §8.2: "An Issue is maintained through: Publication creation, updates..." — Issue is MAINTAINED, not OWNED
- TJS-021 §8.3: "An Issue closes when: All Publications... archived" — Issue is CLOSED by external events
- TJS-021 §8.3: "The Issue remains available as part of the historical record" — Issue PERSISTS as record, not as object
- No Issue ID, no Issue ownership model, no Issue identity model

**Evidence Contradicting H2:**

- TJS-000 §4 explicitly defines Issue as a concept in the semantic hierarchy
- TJS-000 §5 explicitly states what Issue "owns"
- Issue is treated as a thing throughout the repository

---

# Part 2: Candidate Ontological Categories

## Category 1: Object

**Definition:** A thing that exists, has identity, has properties, and has lifecycle.

**Fit:** PARTIAL

**Evidence:**

- Issue has existence (TJS-000 §4)
- Issue has identity (Calendar day)
- Issue has properties (Daily edition, date scope)
- Issue has lifecycle (Opens → Maintained → Closes)

**But:** Issue has no explicit identifier, ownership is unclear, lifecycle is derived.

---

## Category 2: Entity

**Definition:** A thing with distinct identity that persists over time.

**Fit:** PARTIAL

**Evidence:**

- Issue has identity (Calendar day)
- Issue persists (becomes historical)

**But:** Issue has no explicit identifier, identity is implicit.

---

## Category 3: Aggregate Root

**Definition:** The root entity of an aggregate, owning its lifecycle and invariants.

**Fit:** POOR

**Evidence:**

- Issue does not own Publications
- Issue does not have clear invariants
- Issue lifecycle is derived from Publication lifecycle

---

## Category 4: Process

**Definition:** A sequence of actions that transforms inputs into outputs.

**Fit:** GOOD

**Evidence:**

- TJS-021 §8.1: "An Issue opens when..." — Process START
- TJS-021 §8.2: "An Issue is maintained through..." — Process EXECUTION
- TJS-021 §8.3: "An Issue closes when..." — Process END
- Issue is defined by actions (opening, maintaining, closing), not by properties

**But:** Issue persists as historical record after process ends.

---

## Category 5: Temporal Window

**Definition:** A bounded time period during which certain activities occur.

**Fit:** GOOD

**Evidence:**

- TJS-000 §4: "Issue represents one editorial edition... for a single calendar day"
- Issue is scoped to one calendar day
- Issue opens and closes based on temporal triggers

**But:** Issue persists as historical record after window closes.

---

## Category 6: Boundary

**Definition:** A demarcation that separates inside from outside.

**Fit:** PARTIAL

**Evidence:**

- Issue defines what Publications belong to one day
- Issue separates daily editions

**But:** Boundary is a property, not the primary nature.

---

## Category 7: Context

**Definition:** A setting or environment in which something exists.

**Fit:** PARTIAL

**Evidence:**

- Issue provides context for Publications (which day they belong to)

**But:** Issue is more than context — it has lifecycle and integrity requirements.

---

## Category 8: Collection

**Definition:** A group of items treated as a unit.

**Fit:** PARTIAL

**Evidence:**

- Issue contains Publications
- Issue is a collection of daily Publications

**But:** Collection is a relationship, not the primary nature.

---

## Category 9: Editorial Session

**Definition:** A bounded editorial activity period.

**Fit:** GOOD

**Evidence:**

- Issue is defined as "editorial edition" (TJS-000 §4)
- Issue has opening, maintenance, closing (TJS-021 §8)
- Issue is bounded by editorial activity

**But:** Issue persists as historical record after session ends.

---

# Part 3: For EACH Candidate

## Object

| Question | Answer | Evidence |
|----------|--------|----------|
| Can it exist independently? | NO — depends on Journal and Publications | TJS-000 §4 |
| Does it have identity? | YES — Calendar day | TJS-000 §4 |
| Does it require identifier? | NO — no explicit identifier defined | — |
| Can it own Publications? | NO — Publication Engine owns Publications | TJS-010 §4.1 |
| Can Publications exist without it? | UNCLEAR — circular dependency | TJS-000 §4, TJS-021 §8.1 |
| Can it exist empty? | NO — requires at least one Publication | TJS-021 §8.1 |
| Can it be archived? | YES — becomes historical record | TJS-021 §8.3 |
| Can it be recreated? | NO — one Issue per calendar day | TJS-000 §4 |
| Can it mutate? | YES — maintained through Publication changes | TJS-021 §8.2 |
| Does it have lifecycle? | YES — Opens → Maintained → Closes | TJS-021 §8 |
| Does it have boundaries? | YES — one calendar day | TJS-000 §4 |
| Does it have owner? | UNCLEAR — no explicit owner | — |
| Can it participate in relationships? | YES — contains Publications, belongs to Journal | TJS-000 §4 |

## Process

| Question | Answer | Evidence |
|----------|--------|----------|
| Can it exist independently? | NO — depends on trigger | TJS-021 §8.1 |
| Does it have identity? | YES — Calendar day | TJS-000 §4 |
| Does it require identifier? | NO | — |
| Can it own Publications? | NO | TJS-010 §4.1 |
| Can Publications exist without it? | UNCLEAR | — |
| Can it exist empty? | NO — requires action | TJS-021 §8.1 |
| Can it be archived? | YES — becomes historical | TJS-021 §8.3 |
| Can it be recreated? | NO | TJS-000 §4 |
| Can it mutate? | YES — process evolves | TJS-021 §8.2 |
| Does it have lifecycle? | YES — IS lifecycle | TJS-021 §8 |
| Does it have boundaries? | YES — start and end | TJS-021 §8.1, §8.3 |
| Does it have owner? | UNCLEAR | — |
| Can it participate in relationships? | YES | TJS-000 §4 |

## Temporal Window

| Question | Answer | Evidence |
|----------|--------|----------|
| Can it exist independently? | NO — depends on calendar | TJS-000 §4 |
| Does it have identity? | YES — Calendar day | TJS-000 §4 |
| Does it require identifier? | NO | — |
| Can it own Publications? | NO | — |
| Can Publications exist without it? | UNCLEAR | — |
| Can it exist empty? | NO — window implies activity | — |
| Can it be archived? | YES | TJS-021 §8.3 |
| Can it be recreated? | NO | — |
| Can it mutate? | NO — window is fixed | — |
| Does it have lifecycle? | PARTIALLY — window opens and closes | — |
| Does it have boundaries? | YES — IS boundaries | — |
| Does it have owner? | NO | — |
| Can it participate in relationships? | YES | — |

## Editorial Session

| Question | Answer | Evidence |
|----------|--------|----------|
| Can it exist independently? | NO — depends on editorial activity | TJS-000 §4 |
| Does it have identity? | YES — Calendar day | TJS-000 §4 |
| Does it require identifier? | NO | — |
| Can it own Publications? | NO | — |
| Can Publications exist without it? | UNCLEAR | — |
| Can it exist empty? | NO — requires editorial activity | — |
| Can it be archived? | YES | TJS-021 §8.3 |
| Can it be recreated? | NO | — |
| Can it mutate? | YES — session evolves | TJS-021 §8.2 |
| Does it have lifecycle? | YES — session lifecycle | TJS-021 §8 |
| Does it have boundaries? | YES — session start/end | TJS-021 §8.1, §8.3 |
| Does it have owner? | UNCLEAR | — |
| Can it participate in relationships? | YES | — |

---

# Part 4: Necessary Conditions

## Conditions for "Object"

| Condition | Issue Satisfies? | Evidence |
|-----------|------------------|----------|
| Has existence | YES | TJS-000 §4 |
| Has identity | YES | Calendar day |
| Has properties | YES | Daily edition, date scope |
| Has lifecycle | YES | Opens → Maintained → Closes |
| Has boundaries | YES | One calendar day |
| Can be pointed to | PARTIALLY | No explicit identifier |

**Verdict:** Issue PARTIALLY satisfies Object conditions.

---

## Conditions for "Process"

| Condition | Issue Satisfies? | Evidence |
|-----------|------------------|----------|
| Has start | YES | Opens when first Publication generated |
| Has end | YES | Closes when all Publications archived |
| Has activities | YES | Publication creation, updates, removal |
| Has triggers | YES | First Publication, last Publication archived |
| Transforms inputs to outputs | PARTIALLY | Maintains Publications |

**Verdict:** Issue PARTIALLY satisfies Process conditions.

---

## Conditions for "Temporal Window"

| Condition | Issue Satisfies? | Evidence |
|-----------|------------------|----------|
| Has start time | YES | Opens when first Publication generated |
| Has end time | YES | Closes when all Publications archived |
| Has duration | YES | One calendar day |
| Bounded | YES | Calendar day boundary |

**Verdict:** Issue PARTIALLY satisfies Temporal Window conditions.

---

# Part 5: Cross Examination

## Attack on Object Model

**Supporting Evidence:**

- Issue has identity (Calendar day)
- Issue has lifecycle (Opens → Maintained → Closes)
- Issue has properties (Daily edition, date scope)
- Issue is defined in semantic hierarchy (TJS-000 §4)

**Contradicting Evidence:**

- Issue has no explicit identifier
- Issue ownership is unclear
- Issue lifecycle is derived from Publication lifecycle
- Issue appears to be defined by its relationship to Publications
- Issue cannot exist without Publications

**Remaining Uncertainty:** Is Issue a true Object or a derived concept?

---

## Attack on Process Model

**Supporting Evidence:**

- Issue is triggered by first Publication (TJS-021 §8.1)
- Issue is maintained through actions (TJS-021 §8.2)
- Issue is closed by external events (TJS-021 §8.3)
- Issue is defined by actions, not properties

**Contradicting Evidence:**

- Issue persists as historical record after process ends (TJS-021 §8.3)
- Issue has identity (Calendar day)
- Issue is treated as a thing in semantic hierarchy

**Remaining Uncertainty:** Does Issue persist as object after process ends?

---

## Attack on Temporal Window Model

**Supporting Evidence:**

- Issue is scoped to one calendar day (TJS-000 §4)
- Issue opens and closes based on temporal triggers

**Contradicting Evidence:**

- Issue persists as historical record after window closes
- Issue has integrity requirements (TJS-020 §4.5)
- Issue is more than a window — it has editorial meaning

**Remaining Uncertainty:** Is Issue just a window or something more?

---

# Part 6: DDD Investigation

## Entity

**Does Issue satisfy Entity?**

| Condition | Satisfies? | Evidence |
|-----------|------------|----------|
| Has distinct identity | YES | Calendar day |
| Has lifecycle | YES | Opens → Maintained → Closes |
| Has mutability | YES | Maintained through changes |
| Has persistence | YES | Becomes historical |

**Verdict:** Issue PARTIALLY satisfies Entity.

---

## Value Object

**Does Issue satisfy Value Object?**

| Condition | Satisfies? | Evidence |
|-----------|------------|----------|
| Identified by attributes | PARTIALLY | Calendar day |
| Immutable | NO | Maintained through changes |
| Replaceable | NO | One Issue per day |

**Verdict:** Issue does NOT satisfy Value Object.

---

## Aggregate Root

**Does Issue satisfy Aggregate Root?**

| Condition | Satisfies? | Evidence |
|-----------|------------|----------|
| Owns child entities | NO | Does not own Publications |
| Has invariants | PARTIALLY | Integrity requirements |
| Has lifecycle | YES | Opens → Maintained → Closes |

**Verdict:** Issue does NOT satisfy Aggregate Root.

---

## Aggregate Member

**Does Issue satisfy Aggregate Member?**

| Condition | Satisfies? | Evidence |
|-----------|------------|----------|
| Belongs to aggregate | YES | Belongs to Journal |
| Has identity | YES | Calendar day |
| Has lifecycle | YES | Derived from Publication |

**Verdict:** Issue PARTIALLY satisfies Aggregate Member.

---

## Domain Event

**Does Issue satisfy Domain Event?**

| Condition | Satisfies? | Evidence |
|-----------|------------|----------|
| Records something that happened | PARTIALLY | Records daily edition |
| Has timestamp | YES | Calendar day |
| Is transient | NO | Persists as historical |

**Verdict:** Issue does NOT satisfy Domain Event.

---

## Domain Service

**Does Issue satisfy Domain Service?**

| Condition | Satisfies? | Evidence |
|-----------|------------|----------|
| Performs behavior | PARTIALLY | Maintains Publications |
| Stateless | NO | Has state (Open, Maintained, Closed) |
| No identity | NO | Has identity (Calendar day) |

**Verdict:** Issue does NOT satisfy Domain Service.

---

# Part 7: Object vs Process Investigation

## Behavior Analysis

**Does Issue behave more like an Object or a Process?**

### Object Behaviors

| Behavior | Evidence |
|----------|----------|
| Has state | TJS-021 §8: Open, Maintained, Closed |
| Has properties | TJS-000 §5: Daily edition, date scope |
| Has identity | TJS-000 §4: Calendar day |
| Persists | TJS-021 §8.3: Becomes historical |

### Process Behaviors

| Behavior | Evidence |
|----------|----------|
| Has start trigger | TJS-021 §8.1: Opens when first Publication generated |
| Has end trigger | TJS-021 §8.3: Closes when all Publications archived |
| Has activities | TJS-021 §8.2: Publication creation, updates, removal |
| Is defined by actions | TJS-021 §8: Maintained through actions |

**Verdict:** Issue exhibits BOTH Object and Process behaviors.

---

# Part 8: Timeline Test

## Temporal Sequence

```text
Calendar Day Begins
    │
    │ (no Issue yet)
    ▼
First Publication Generated
    │
    │ (Issue OPENS)
    ▼
Issue Exists
    │
    │ (Publications created, updated, removed)
    ▼
All Publications Archived
    │
    │ (Issue CLOSES)
    ▼
Issue Becomes Historical
    │
    │ (Issue persists permanently)
    ▼
Calendar Day Ends
```

**Key Observation:** Issue appears AFTER first Publication, not before.

**Implication:** Issue is triggered by Publication, not the other way around.

---

# Part 9: Dependency Test

## Experiment 1: Remove Issue

**Question:** Can Publication still exist without Issue?

**Evidence:**

- TJS-000 §4: "Publication represents one independent publication belonging to an Issue"
- But TJS-021 §8.1: "An Issue opens when the first Publication... is generated"

**Analysis:** If Issue is removed, Publication could still exist, but would have no daily grouping. The relationship "belongs to Issue" would be lost.

**Verdict:** Publication CAN exist without Issue, but loses daily grouping.

---

## Experiment 2: Remove Publication

**Question:** Can Issue still exist without Publication?

**Evidence:**

- TJS-021 §8.1: "An Issue opens when the first Publication... is generated"
- Issue requires at least one Publication to exist

**Analysis:** If Publication is removed, Issue cannot exist. Issue is triggered by Publication.

**Verdict:** Issue CANNOT exist without Publication.

---

## Comparison

| Experiment | Result |
|------------|--------|
| Remove Issue | Publication can exist (loses grouping) |
| Remove Publication | Issue cannot exist |

**Conclusion:** Issue depends on Publication more than Publication depends on Issue.

---

# Part 10: Minimal Sufficiency

## If Issue Is Removed — What Must Replace It?

### Option 1: Nothing

**Justification:** Publication can exist without Issue.

**Consequence:** Loss of daily grouping, loss of editorial integrity, loss of historical record.

---

### Option 2: Temporal Window

**Justification:** Issue is essentially a temporal window (one calendar day).

**Consequence:** Replaces Issue with a simpler concept, but loses editorial meaning.

---

### Option 3: Boundary

**Justification:** Issue defines what Publications belong to one day.

**Consequence:** Replaces Issue with a structural concept, but loses lifecycle.

---

### Option 4: Session

**Justification:** Issue is an editorial session (opens, maintains, closes).

**Consequence:** Replaces Issue with a process concept, but loses persistence.

---

### Option 5: Collection

**Justification:** Issue is a collection of daily Publications.

**Consequence:** Replaces Issue with a grouping concept, but loses temporal meaning.

---

### Option 6: Process

**Justification:** Issue is a daily editorial process.

**Consequence:** Replaces Issue with a behavioral concept, but loses object nature.

---

# Part 11: Contradiction Analysis

## Contradiction Matrix

| Statement A | Statement B | Compatible? | Explanation |
|-------------|-------------|-------------|-------------|
| Publication belongs to Issue | Issue opens after first Publication | NO | Circular dependency |
| Issue contains Publications | Issue exists without Publications | NO | Contradictory |
| Issue closes after last Publication | Issue persists as historical | PARTIALLY | Temporal vs permanent |
| Issue is an Object | Issue is triggered by Publication | PARTIALLY | Object vs Process |

---

# Part 12: Key Findings

## Finding 1: Issue Is NOT a Pure Object

**Evidence:**

- Issue has no explicit identifier
- Issue ownership is unclear
- Issue lifecycle is derived from Publication lifecycle
- Issue is triggered by Publication, not the other way around

---

## Finding 2: Issue Is NOT a Pure Process

**Evidence:**

- Issue persists as historical record after process ends
- Issue has identity (Calendar day)
- Issue is treated as a thing in semantic hierarchy

---

## Finding 3: Issue Is a Hybrid Concept

**Evidence:**

- Issue exhibits BOTH Object and Process behaviors
- Issue has properties (Object) AND actions (Process)
- Issue persists (Object) AND is triggered (Process)

---

## Finding 4: Issue Is Derivative

**Evidence:**

- Issue depends on Publication (cannot exist without it)
- Issue lifecycle is derived from Publication lifecycle
- Issue is defined by its relationship to Publications

---

# End of Object vs Process Hearing
