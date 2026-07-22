# META001_ONTOLOGY_HEARING

**Document ID:** META001-HEARING

**Title:** Fundamental Ontological Types Hearing

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Ontological Types Investigation

---

# Purpose

This document determines the complete set of fundamental ontological types from which every repository concept is built.

---

# Part I: Fundamental Ontological Types

## Reconstructed Ontological Types

| # | Type | Definition | Why It Exists |
|---|------|------------|---------------|
| 1 | Reality | Physical existence independent of observers | Foundation of everything |
| 2 | Object | Thing with identity that persists over time | Models entities in world |
| 3 | Event | Something that happens at a point in time | Models occurrences |
| 4 | Process | Sequence of actions that transforms inputs | Models activities |
| 5 | State | Condition of an Object at a point in time | Models status |
| 6 | Role | Responsibility performed by an Actor | Models functions |
| 7 | Identity | What makes an Object the same over time | Models uniqueness |
| 8 | Information | Relation between Reality and a Knower | Models knowledge content |
| 9 | Knowledge | Belief held by a Knower about Reality | Models understanding |
| 10 | Representation | Portrayal of Information in a format | Models expression |
| 11 | Carrier | Medium that holds Representation | Models storage/delivery |
| 12 | Communication | Process of transferring meaning | Models information flow |
| 13 | Relationship | Connection between concepts | Models associations |
| 14 | Collection | Group of Objects treated as unit | Models aggregation |
| 15 | Boundary | Demarcation separating inside from outside | Models scope |
| 16 | Context | Setting in which something exists | Models environment |
| 17 | Lifecycle | Sequence of states an Object passes through | Models evolution |
| 18 | Meaning | Interpretation of content by a Knower | Models semantics |
| 19 | Signal | Physical indication of something | Models transmission |
| 20 | Evidence | Proof or indication of Reality | Models verification |

---

# Part II: Type Properties

| Type | Exists Independently? | Has Identity? | Has Lifecycle? | Can Own? | Can Change? | Can Disappear? | Can Contain? | Can Be Contained? |
|------|----------------------|---------------|----------------|----------|-------------|----------------|--------------|-------------------|
| Reality | YES | NO | YES | NO | YES | NO | YES | NO |
| Object | YES | YES | YES | YES | YES | YES | YES | YES |
| Event | NO | NO | NO | NO | NO | YES | NO | YES |
| Process | NO | NO | YES | NO | YES | YES | YES | YES |
| State | NO | NO | NO | NO | YES | YES | NO | YES |
| Role | NO | YES | NO | NO | NO | YES | NO | YES |
| Identity | NO | YES | NO | NO | NO | YES | NO | YES |
| Information | NO | NO | NO | NO | YES | YES | NO | YES |
| Knowledge | NO | NO | NO | NO | YES | YES | NO | YES |
| Representation | NO | PARTIALLY | YES | YES | YES | YES | YES | YES |
| Carrier | NO | YES | YES | YES | YES | YES | YES | YES |
| Communication | NO | NO | YES | NO | YES | YES | YES | NO |
| Relationship | NO | NO | NO | NO | YES | YES | NO | NO |
| Collection | NO | PARTIALLY | YES | YES | YES | YES | YES | YES |
| Boundary | NO | NO | NO | NO | YES | YES | NO | NO |
| Context | NO | NO | NO | NO | YES | YES | NO | NO |
| Lifecycle | NO | NO | YES | NO | YES | YES | YES | YES |
| Meaning | NO | NO | NO | NO | YES | YES | NO | YES |
| Signal | NO | NO | NO | NO | YES | YES | NO | YES |
| Evidence | NO | NO | NO | NO | YES | YES | NO | YES |

---

# Part III: Repository Concept Classification

## Classification Matrix

| Repository Concept | Primary Type | Secondary Type | Evidence |
|--------------------|--------------|----------------|----------|
| Publication | Object | Information | Has identity, lifecycle, contains Information |
| Issue | Object | Collection | Has identity, contains Publications |
| Journal | Collection | Object | Contains Issues, has identity |
| Publication Package | Collection | Object | Contains Publications |
| Parser | Object | Process | Has identity, performs data retrieval |
| Publication Engine | Object | Process | Has identity, performs generation |
| Publisher | Role | — | Describes responsibility |
| Schedule Generator | Object | Process | Has identity, performs generation |
| Graphic Generator | Object | Process | Has identity, performs generation |
| Telegram Publisher | Object | Process | Has identity, performs delivery |
| Telegram Message | Carrier | Representation | Medium holding Publication |
| Telegram Channel | Boundary | Carrier | Demarcation for delivery |
| Territory | Object | Boundary | Has identity, defines scope |
| Community | Object | Boundary | Has identity, defines scope |
| Settlement | Object | — | Has identity |
| Street | Object | — | Has identity |
| Address | Object | — | Has identity |
| Schedule | Object | Information | Has identity, contains information |
| Time Interval | Object | — | Has identity |
| Normalized Dataset | Information | Representation | Structured information |
| Interpretation Result | Information | Representation | Information for residents |
| Processing Cycle | Process | Event | Sequence of actions |
| Historical Archive | Collection | Carrier | Preserves records |
| Issue Lifecycle | Lifecycle | Process | Sequence of states |
| Publication Lifecycle | Lifecycle | Process | Sequence of states |
| Open Data | Information | Evidence | Officially published information |
| Data Source | Object | Role | Origin of information |
| DSO | Object | Role | Organization |
| Resident | Object | Role | Person using system |
| Information Consumer | Role | — | Receives Publications |
| Stakeholder | Role | — | Has interest in project |
| Component | Object | Role | Architectural building block |
| Role | Role | — | Logical responsibility |

---

# Part IV: Ontological Taxonomy

## Level 1: Fundamental Ontological Types

1. Reality
2. Object
3. Event
4. Process
5. State
6. Role
7. Identity
8. Information
9. Knowledge
10. Representation
11. Carrier
12. Communication
13. Relationship
14. Collection
15. Boundary
16. Context
17. Lifecycle
18. Meaning
19. Signal
20. Evidence

---

## Level 2: Derived Types

| Derived Type | Derived From | Examples |
|--------------|--------------|----------|
| Entity | Object + Identity | Publication, Territory, Address |
| Aggregate | Collection + Object | Journal, Publication Package |
| Domain Object | Object + Business | Publication, Issue, Schedule |
| Architectural Object | Object + Implementation | Parser, Publication Engine |
| Information Object | Object + Information | Publication, Open Data |
| Representation Object | Object + Representation | Telegram Message, Repository Object |
| Carrier Object | Object + Carrier | Telegram Message, Database Record |
| Process Object | Object + Process | Parser, Publication Engine |
| Event Object | Object + Event | Processing Cycle |
| Lifecycle Object | Object + Lifecycle | Publication Lifecycle, Issue Lifecycle |
| Role Object | Object + Role | Publisher, Interpreter |
| Boundary Object | Object + Boundary | Territory, Telegram Channel |
| Collection Object | Object + Collection | Journal, Publication Package |
| Context Object | Object + Context | Reporting Period |

---

## Level 3: Repository Concepts

| Repository Concept | Derived Type | Primary Type |
|--------------------|--------------|--------------|
| Publication | Domain Object | Object |
| Issue | Domain Object | Object |
| Journal | Aggregate | Collection |
| Publication Package | Aggregate | Collection |
| Parser | Architectural Object | Object |
| Publication Engine | Architectural Object | Object |
| Publisher | Role Object | Role |
| Schedule Generator | Architectural Object | Object |
| Graphic Generator | Architectural Object | Object |
| Telegram Publisher | Architectural Object | Object |
| Telegram Message | Carrier Object | Carrier |
| Telegram Channel | Boundary Object | Boundary |
| Territory | Boundary Object | Boundary |
| Community | Boundary Object | Boundary |
| Settlement | Domain Object | Object |
| Street | Domain Object | Object |
| Address | Domain Object | Object |
| Schedule | Information Object | Object |
| Time Interval | Domain Object | Object |
| Normalized Dataset | Information Object | Information |
| Interpretation Result | Information Object | Information |
| Processing Cycle | Process Object | Process |
| Historical Archive | Collection Object | Collection |
| Issue Lifecycle | Lifecycle Object | Lifecycle |
| Publication Lifecycle | Lifecycle Object | Lifecycle |
| Open Data | Information Object | Information |
| Data Source | Domain Object | Object |
| DSO | Domain Object | Object |
| Resident | Domain Object | Object |
| Information Consumer | Role Object | Role |
| Stakeholder | Role Object | Role |
| Component | Architectural Object | Object |
| Role | Role Object | Role |

---

# Part V: Impossible Combinations

## Can Process Have Identity?

**Answer:** PARTIALLY

**Evidence:**

- Processing Cycle has identity (one complete execution)
- But Process itself is abstract

**Conclusion:** Process INSTANCES can have identity; Process TYPE cannot.

---

## Can Event Own Something?

**Answer:** NO

**Evidence:**

- Events happen, they don't own
- Events have no persistence

**Conclusion:** Events CANNOT own.

---

## Can Information Exist Without Representation?

**Answer:** YES

**Evidence:**

- Information exists in Knowledge
- Representation is optional
- Information can be unexpressed

**Conclusion:** Information CAN exist without Representation.

---

## Can Representation Exist Without Information?

**Answer:** NO

**Evidence:**

- Representation portrays Information
- Without Information, Representation has no content

**Conclusion:** Representation CANNOT exist without Information.

---

## Can Role Own Lifecycle?

**Answer:** NO

**Evidence:**

- Role is abstract responsibility
- Lifecycle belongs to Objects

**Conclusion:** Roles CANNOT own Lifecycle.

---

## Can Carrier Have Meaning?

**Answer:** NO

**Evidence:**

- Carrier is medium, not content
- Meaning belongs to Information/Knowledge

**Conclusion:** Carriers CANNOT have Meaning.

---

## Can Publication Be Event?

**Answer:** NO

**Evidence:**

- Publication persists over time
- Events are instantaneous
- Publication has lifecycle

**Conclusion:** Publication CANNOT be Event.

---

## Can Publication Be Object?

**Answer:** YES

**Evidence:**

- Publication has identity (Territory + Date + Template)
- Publication has lifecycle
- Publication persists over time

**Conclusion:** Publication CAN be Object.

---

## Can Publication Be Process?

**Answer:** NO

**Evidence:**

- Publication is result, not process
- Publication persists; Process transforms

**Conclusion:** Publication CANNOT be Process.

---

## Can Issue Be Session?

**Answer:** PARTIALLY

**Evidence:**

- Issue has temporal scope (one day)
- Issue has opening and closing
- But Issue persists as historical record

**Conclusion:** Issue has Session characteristics but is Object.

---

## Can Issue Be Object?

**Answer:** YES

**Evidence:**

- Issue has identity (Calendar day)
- Issue has lifecycle
- Issue persists over time

**Conclusion:** Issue CAN be Object.

---

## Can Journal Be Aggregate?

**Answer:** YES

**Evidence:**

- Journal contains Issues
- Journal has identity
- Journal is collection of Issues

**Conclusion:** Journal CAN be Aggregate.

---

# Part VI: Ontological Reduction

## Remove Publication

**Does Object still exist?** YES

**Evidence:** Object is fundamental type; Publication is instance

---

## Remove Object

**Does Publication still exist?** NO

**Evidence:** Publication is instance of Object; without Object type, no Publication

---

## Remove Information

**Can Representation exist?** NO

**Evidence:** Representation portrays Information; without Information, no Representation

---

## Remove Representation

**Can Carrier exist?** YES

**Evidence:** Carrier can be empty; Carrier exists without content

---

## Remove Process

**Can Lifecycle exist?** NO

**Evidence:** Lifecycle is sequence of states (process-like); without Process, no Lifecycle

---

# Part VII: Ontological Dependency Graph

```text
Reality
    │
    ▼
Object ←── Identity
    │
    ├──→ Event
    ├──→ Process ←── Lifecycle
    ├──→ State
    ├──→ Role
    ├──→ Relationship
    ├──→ Collection
    ├──→ Boundary
    └──→ Context
           │
           ▼
    Information ←── Knowledge
           │
           ▼
    Representation ←── Meaning
           │
           ▼
      Carrier ←── Signal
           │
           ▼
    Communication ←── Evidence
```

---

# Part VIII: World Practice Comparison

| Source | Ontology | Our Types | Comparison |
|--------|----------|-----------|------------|
| Philosophy | Substance, Property, Relation | Object, State, Relationship | GOOD match |
| Information Science | Data, Information, Knowledge | Information, Knowledge | GOOD match |
| DDD | Entity, Value Object, Aggregate, Event | Object, Collection, Event | GOOD match |
| Communication Theory | Sender, Message, Receiver, Channel | Object, Information, Carrier, Communication | GOOD match |
| Semiotics | Sign, Object, Interpretant | Signal, Object, Meaning | GOOD match |
| Archival Science | Record, Archive, Collection | Carrier, Collection, Object | GOOD match |

---

# Part IX: Minimal Fundamental Ontology

## How Many Ontological Types Are Absolutely Necessary?

**Answer: 10**

| # | Type | Why Necessary |
|---|------|---------------|
| 1 | Reality | Foundation of everything |
| 2 | Object | Models entities |
| 3 | Process | Models activities |
| 4 | Information | Models knowledge content |
| 5 | Representation | Models expression |
| 6 | Carrier | Models storage/delivery |
| 7 | Communication | Models information flow |
| 8 | Relationship | Models associations |
| 9 | Collection | Models aggregation |
| 10 | Identity | Models uniqueness |

---

# Part X: Ontological Level Mixing

## Does Repository Mix Ontological Levels?

**Answer:** YES

**Evidence:**

| Mixing | Example | Severity |
|--------|---------|----------|
| Object mixed with Process | Parser is Object AND Process | MEDIUM |
| Role mixed with Entity | Publisher is Role AND has lifecycle | LOW |
| Representation mixed with Carrier | Telegram Message is both | MEDIUM |
| Information mixed with Publication | Publication contains Information | LOW |
| Collection mixed with Object | Journal is Collection AND has identity | LOW |

---

# Part XI: Key Findings

## Finding 1: 20 Fundamental Ontological Types Exist

**Evidence:**

- Reality, Object, Event, Process, State, Role, Identity, Information, Knowledge, Representation, Carrier, Communication, Relationship, Collection, Boundary, Context, Lifecycle, Meaning, Signal, Evidence

---

## Finding 2: 10 Types Are Absolutely Necessary

**Evidence:**

- Reality, Object, Process, Information, Representation, Carrier, Communication, Relationship, Collection, Identity

---

## Finding 3: Every Repository Concept Can Be Classified

**Evidence:**

- All concepts classified into primary and secondary types
- No concept is unclassifiable

---

## Finding 4: Repository Mixes Ontological Levels

**Evidence:**

- Object mixed with Process (Parser, Publication Engine)
- Representation mixed with Carrier (Telegram Message)
- Information mixed with Publication
- Collection mixed with Object (Journal)

---

## Finding 5: Minimal Ontology Is 10 Types

**Evidence:**

- 10 types are absolutely necessary
- All other types are derived or optional

---

# End of Ontological Types Hearing
