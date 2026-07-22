# CASE001_PUBLICATION_VIEWPOINTS

**Document ID:** CASE001-PUB-VIEWPOINTS

**Title:** Publication — Architectural Viewpoint Audit

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Viewpoint Audit №001

---

# Purpose

This document determines whether the eleven competing Publication models are actually competing models or different architectural viewpoints of the same concept.

---

# Part 1: Viewpoint Identification

## Classification of Each Model

| Model | Name | Classification | Justification |
|-------|------|----------------|---------------|
| A | Publication as Message | **Integration Viewpoint** | Describes how Publication appears at the Telegram integration boundary. Focuses on transmission, delivery, and platform identity. |
| B | Publication as Document | **Persistence Viewpoint** | Describes how Publication appears in storage and archival. Focuses on structure, persistence, and editorial standards. |
| C | Publication as Event | **Lifecycle Viewpoint** | Describes when Publication is triggered. Focuses on the moment of creation and the trigger mechanism. |
| D | Publication as Information Object | **Domain Viewpoint** | Describes what Publication IS in the domain. Focuses on identity, behavior, and invariants. |
| E | Publication as Business Object | **Business Viewpoint** | Describes what Publication MEANS to the business. Focuses on value, stakeholders, and business rules. |
| F | Publication as Editorial Artifact | **Editorial Viewpoint** | Describes how Publication follows editorial standards. Focuses on policy, templates, and formatting. |
| G | Publication as Communication Unit | **Distribution Viewpoint** | Describes how Publication reaches residents. Focuses on mass distribution, accessibility, and timeliness. |
| H | Publication as Aggregate Root | **DDD Viewpoint** | Describes Publication's role in Domain-Driven Design. Focuses on ownership, boundaries, and aggregate semantics. |
| I | Publication as Value Object | **Analytical Viewpoint** | Describes Publication's identity mechanism. Focuses on attributes, immutability, and equality. |
| J | Publication as Entity | **Analytical Viewpoint** | Describes Publication's persistence and mutability. Focuses on identity, state changes, and continuity. |
| K | Publication as Domain Event | **Temporal Viewpoint** | Describes Publication as a point in time. Focuses on triggers, timestamps, and event-driven architecture. |

---

## Key Observation

**Models H, I, J, K are DDD analytical classifications, not semantic models.**

They answer "what DDD role does Publication play?" not "what IS Publication?"

Models A, B, C, D, E, F, G are semantic descriptions from different perspectives.

They answer "what IS Publication?" from different angles.

---

# Part 2: Layer Mapping

## Publication Across Architectural Layers

| Layer | Publication Appears As | Identity | Owner | Lifecycle |
|-------|----------------------|----------|-------|-----------|
| **Reality Layer** | Information about power outages | Content-based | DSO | Static (historical) |
| **Business Layer** | Business artifact serving residents | Territory + Date | SvitloSk Project | Created → Distributed → Archived |
| **Domain Layer** | Domain entity with invariants | Internal ID | Publication Engine | Generated → Published → Updated → Archived → Removed |
| **DDD Layer** | Aggregate Root | Internal ID | Publication Engine | Owns lifecycle, referenced by all |
| **Editorial Layer** | Editorial product following standards | Territory + Date + Template | Editorial System | Created per editorial rules |
| **Publication Layer** | Deterministic information unit | Territory + Date + Template | Publication Engine | Generated → Rendered → Delivered |
| **Integration Layer** | Telegram message | Telegram Message ID | Telegram Publisher | Created → Published → Updated → Deleted |
| **Telegram Layer** | Channel message | Telegram Message ID | Telegram Channel | Visible → Edited → Removed |
| **Persistence Layer** | Database record | Internal ID | Data Storage | Inserted → Updated → Archived |
| **Repository Layer** | Specification artifact | Document ID | Repository Governance | Draft → Approved → Stable |
| **Documentation Layer** | Normative definition | Term name | Glossary | Defined → Used → Referenced |

---

## Layer Analysis

**The same Publication appears differently on different layers.**

| Layer | What Publication IS |
|-------|-------------------|
| Business | Business artifact |
| Domain | Domain entity |
| DDD | Aggregate Root |
| Editorial | Editorial product |
| Publication | Information unit |
| Integration | Telegram message |
| Telegram | Channel message |
| Persistence | Database record |
| Repository | Specification artifact |
| Documentation | Normative definition |

**Critical Finding:** Publication is NOT different objects on different layers. It is the SAME concept viewed from different perspectives.

---

# Part 3: Identity Continuity

## Identity Across Layers

| Layer | Identity Mechanism | Same Identity? |
|-------|-------------------|----------------|
| Business | Territory + Date + Purpose | YES — this IS the Publication |
| Domain | Internal ID | YES — this IDENTIFIES the same Publication |
| DDD | Internal ID (Aggregate Root) | YES — same as Domain |
| Editorial | Territory + Date + Template | YES — this DESCRIBES the same Publication |
| Publication | Territory + Date + Template | YES — same as Editorial |
| Integration | Telegram Message ID | YES — this REFERENCES the same Publication |
| Telegram | Telegram Message ID | YES — same as Integration |
| Persistence | Internal ID + Database Key | YES — this STORES the same Publication |
| Repository | Document ID | DIFFERENT — this is the SPECIFICATION, not the Publication |
| Documentation | Term Name | DIFFERENT — this is the DEFINITION, not the Publication |

---

## Identity Continuity Verdict

**Publication maintains identity continuity across Business, Domain, DDD, Editorial, Publication, Integration, Telegram, and Persistence layers.**

**Publication does NOT maintain identity continuity across Repository and Documentation layers** — those layers describe the SPECIFICATION of Publication, not Publication itself.

---

## One Object or Multiple Objects?

**ONE OBJECT.**

Arguments:

1. **Same content** — the information about power outages is the same across all layers
2. **Same lifecycle** — the state changes propagate across layers
3. **Same ownership** — the Publication Engine creates and manages it across layers
4. **Same relationships** — it belongs to Issue, contains Territory, etc.
5. **Transformation, not replacement** — each layer transforms the REPRESENTATION, not the CONCEPT

**What changes across layers:**

- Format (HTML, database record, specification text)
- Identity mechanism (Internal ID, Telegram Message ID)
- Available operations (read, update, archive)
- Visibility (residents, developers, auditors)

**What does NOT change:**

- The information content
- The territorial scope
- The temporal scope
- The business purpose
- The editorial standards

---

# Part 4: Canonical Publication

## Investigation: Should the Repository Introduce "Canonical Publication"?

### Evidence For

| Evidence | Source |
|----------|--------|
| Publication has 7 different definitions | GLOSSARY, TELEGRAM_GLOSSARY, DATA_MODEL, TJS-000, TJS-010, TJS-021, TJS-022 |
| Publication appears differently on 11 layers | Layer Mapping Matrix |
| Competing models create confusion | CASE001_PUBLICATION_HEARING |
| Identity is undefined | UQ-001 in Hearing |
| Platform independence is claimed but not enforced | TJS-000 §3 vs lifecycle mechanics |

### Evidence Against

| Evidence | Source |
|----------|--------|
| Publication is already well-defined in GLOSSARY.md | GLOSSARY.md §3 |
| Publication is the semantic center of the ontology | SEMANTIC_CENTER_ANALYSIS |
| Publication has clear ownership (Publication Engine) | ONTOLOGY_OWNERSHIP_MATRIX |
| Publication has clear lifecycle (TJS-021) | TJS-021 |
| Adding "Canonical Publication" adds complexity | PROJECT_PRINCIPLES P-08: Organic Growth |

### Analysis

**"Canonical Publication" would:**

1. Provide a single, authoritative definition from which all layer-specific representations derive
2. Resolve the 7-definition inconsistency
3. Clarify identity criteria
4. Enable platform independence
5. Provide a reference point for all architectural decisions

**"Canonical Publication" would NOT:**

1. Change how Publication behaves on any layer
2. Change the existing definitions (they become layer-specific projections)
3. Require migration (existing definitions remain valid)
4. Add new behavior (just clarifies existing behavior)

### Conclusion

**The investigation finds that "Canonical Publication" is a CONCEPTUALLY VALID addition that would resolve many inconsistencies WITHOUT requiring implementation changes.**

**However, this investigation does NOT recommend adoption.** The Architect will decide.

---

# Part 5: Projection Model

## Projection Model Construction

```text
                    ┌─────────────────────────────────┐
                    │      CANONICAL PUBLICATION       │
                    │  (Platform-independent concept)  │
                    └───────────────┬─────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
            ▼                       ▼                       ▼
    ┌───────────────┐      ┌───────────────┐      ┌───────────────┐
    │ Business View │      │ Domain View   │      │ Editorial View│
    │               │      │               │      │               │
    │ - Stakeholders│      │ - Identity    │      │ - Standards   │
    │ - Value       │      │ - Invariants  │      │ - Templates   │
    │ - Purpose     │      │ - Lifecycle   │      │ - Formatting  │
    └───────┬───────┘      └───────┬───────┘      └───────┬───────┘
            │                       │                       │
            └───────────────────────┼───────────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
            ▼                       ▼                       ▼
    ┌───────────────┐      ┌───────────────┐      ┌───────────────┐
    │ Telegram View │      │ Storage View  │      │ Documentation │
    │               │      │               │      │               │
    │ - Message ID  │      │ - Database ID │      │ - Glossary    │
    │ - Bot API     │      │ - Persistence │      │ - Specifications│
    │ - Channel     │      │ - Archive     │      │ - Definitions │
    └───────────────┘      └───────────────┘      └───────────────┘
```

---

## Projection Model Explanation

### Canonical Publication

**Definition:** The platform-independent, layer-independent concept of "one unit of public information generated by SvitloSk for distribution to residents."

**Properties:**

- Has identity (internal, not platform-specific)
- Has content (territorial information about outages)
- Has lifecycle (Created → Distributed → Archived)
- Has owner (Publication Engine)
- Has relationships (belongs to Issue, contains Territory)
- Is deterministic (same input = same output)
- Is traceable (to official source data)

### Business View

**Projects:** What Publication MEANS to the business

**Shows:** Stakeholders, value, purpose, business rules

**Hides:** Technical implementation, platform details, storage mechanisms

### Domain View

**Projects:** What Publication IS in the domain

**Shows:** Identity, invariants, lifecycle, relationships

**Hides:** Platform-specific details, storage details, editorial details

### Editorial View

**Projects:** How Publication follows editorial standards

**Shows:** Templates, formatting rules, editorial policy

**Hides:** Technical implementation, platform details, storage details

### Telegram View

**Projects:** How Publication appears on Telegram

**Shows:** Telegram Message ID, Bot API interaction, channel delivery

**Hides:** Domain internals, storage details, business rules

### Storage View

**Projects:** How Publication is persisted

**Shows:** Database ID, persistence mechanism, archive strategy

**Hides:** Domain internals, platform details, business rules

### Documentation View

**Projects:** How Publication is documented

**Shows:** Glossary definitions, specifications, terminology

**Hides:** Implementation details, runtime behavior

---

## Contradiction Resolution

| Contradiction | Resolved by Projection? | Explanation |
|---------------|------------------------|-------------|
| 7 different definitions | YES | Each definition is a view-specific projection of Canonical Publication |
| Platform independence vs Telegram mechanics | YES | Canonical Publication is platform-independent; Telegram View is platform-specific |
| Identity undefined | YES | Canonical Publication has internal identity; each view projects it differently |
| Manual Publications excluded | YES | Manual Publications are a different Canonical concept projected through same views |
| Updated state ambiguity | YES | Canonical Publication has clear lifecycle; Updated is a view-specific state |
| Archival trigger vague | YES | Canonical Publication has clear archival rules; each view implements them differently |
| Circular dependency with Issue | YES | Canonical Publication belongs to Canonical Issue; views project this relationship differently |
| Ownership model gaps | YES | Canonical Publication has clear ownership; Manual Publications have different ownership |
| Graphic Publication lifecycle | YES | Graphic Publication is a different Canonical concept projected through same views |
| Repository vs Telegram authority | YES | Canonical Publication is the authority; Repository and Telegram are views |
| Publication content undefined | YES | Canonical Publication has clear content; each view shows different aspects |
| Relationship with Interpretation | YES | Canonical Publication is derived from Canonical Interpretation Result |
| Ownership boundaries | YES | Canonical Publication has clear owner; each view projects ownership differently |
| Temporal scope | YES | Canonical Publication has clear temporal rules; each view implements them |
| Multi-channel publication | YES | Canonical Publication can be projected through multiple channel views |
| Publication granularity | YES | Canonical Publication has clear granularity; Long Publication Split is a view transformation |

---

# Part 6: Ontological Consistency

## Contradiction Resolution Check

| # | Contradiction | Resolved by Projection? | Explanation |
|---|---------------|------------------------|-------------|
| 1 | GLOSSARY says "message"; TELEGRAM_GLOSSARY says "unit" | YES | "Message" is the Integration View; "unit" is the Domain View |
| 2 | Legacy TJS-002 has "Scheduled" state; TJS-021 does not | YES | "Scheduled" was a view-specific state that was removed |
| 3 | Publication Engine owns; Publisher owns | YES | "Publication Engine" is the Component View; "Publisher" is the Role View |
| 4 | Telegram Message ID is identity; internal ID is identity | YES | Telegram Message ID is the Integration View; internal ID is the Domain View |
| 5 | Platform-independent; Telegram-specific | YES | Canonical Publication is platform-independent; Telegram View is platform-specific |
| 6 | Updated always returns to Published | YES | Updated is a transient view-specific state; Canonical lifecycle is clearer |
| 7 | Archival trigger vague | YES | Canonical Publication has clear archival rules; views implement them |
| 8 | Manual Publications excluded | YES | Manual Publications are a different Canonical concept |
| 9 | Graphic Publications undefined lifecycle | YES | Graphic Publications are a different Canonical concept |
| 10 | Repository vs Telegram authority | YES | Canonical Publication is the authority; Repository and Telegram are views |
| 11 | Circular dependency with Issue | YES | Canonical Publication belongs to Canonical Issue; views project differently |
| 12 | Identity undefined | YES | Canonical Publication has internal identity; views project it |

---

## Ontological Consistency Verdict

**ALL 12 previously identified contradictions are RESOLVED by the projection model.**

**The projection model provides a consistent ontological framework for Publication.**

---

# Part 7: DDD Validation

## DDD Classifications as Analytical Lenses

| DDD Classification | Is It Alternative Identity? | Is It Analytical Lens? | Justification |
|--------------------|-----------------------------|------------------------|---------------|
| Aggregate Root | NO | **Analytical Lens** | Describes Publication's role in the aggregate hierarchy. Not an alternative identity, but a way of analyzing ownership and boundaries. |
| Aggregate Member | NO | **Analytical Lens** | Describes Publication's relationship to its containing aggregate. Not an alternative identity, but a way of analyzing containment. |
| Entity | NO | **Analytical Lens** | Describes Publication's identity mechanism. Not an alternative identity, but a way of analyzing identity semantics. |
| Value Object | NO | **Analytical Lens** | Describes Publication's equality mechanism. Not an alternative identity, but a way of analyzing equality semantics. |
| Domain Event | NO | **Analytical Lens** | Describes Publication's trigger mechanism. Not an alternative identity, but a way of analyzing temporal semantics. |

---

## DDD Classification Analysis

### Publication as Aggregate Root

**When analyzing from the DDD perspective:**

- Publication owns its lifecycle
- Publication is referenced by all other concepts
- Publication has invariants that must be preserved
- Publication is the central entity in the domain

**This is a VALID analytical lens.** It describes Publication's role in the aggregate hierarchy.

### Publication as Entity

**When analyzing from the DDD perspective:**

- Publication has identity
- Publication has mutable state
- Publication persists over time
- Publication participates in domain events

**This is a VALID analytical lens.** It describes Publication's identity mechanism.

### Publication as Value Object

**When analyzing from the DDD perspective:**

- Publication is identified by attributes (Territory + Date + Template)
- Publication is deterministic (same attributes = same Publication)
- Publication can be compared by value (Canonical Equality)

**This is a PARTIALLY VALID analytical lens.** It describes Publication's equality mechanism, but Publication also has identity (Telegram Message ID or internal ID).

### Publication as Domain Event

**When analyzing from the DDD perspective:**

- Publication is triggered by Dataset changes
- Publication has timestamp
- Publication has payload (the information)
- Publication has consumers (residents)

**This is a PARTIALLY VALID analytical lens.** It describes Publication's trigger mechanism, but Publication persists beyond the triggering moment.

---

## DDD Validation Verdict

**DDD classifications (Aggregate Root, Entity, Value Object, Domain Event) are ANALYTICAL LENSES, not alternative identities.**

**They describe different ASPECTS of the same Canonical Publication:**

- Aggregate Root: ownership and boundaries
- Entity: identity and mutability
- Value Object: equality and attributes
- Domain Event: triggering and temporal semantics

**They do NOT contradict each other.** They complement each other.

**The repository's DDD_AGGREGATE_ANALYSIS correctly identifies Publication as Aggregate Root.** This is the primary DDD analytical lens.

**Other DDD lenses (Entity, Value Object, Domain Event) describe secondary aspects of Publication.**

---

# Part 8: Final Analysis

## Are the Eleven Models Truly Competing?

**NO.**

The eleven models are:

1. **Seven semantic descriptions** from different perspectives (Message, Document, Event, Info Object, Business, Editorial, Communication)
2. **Four DDD analytical classifications** (Aggregate Root, Entity, Value Object, Domain Event)

**The seven semantic descriptions are NOT competing.** They describe the same concept from different angles:

- Message: integration perspective
- Document: persistence perspective
- Event: temporal perspective
- Info Object: domain perspective
- Business: stakeholder perspective
- Editorial: standards perspective
- Communication: distribution perspective

**The four DDD classifications are NOT competing.** They analyze different aspects of the same concept:

- Aggregate Root: ownership
- Entity: identity
- Value Object: equality
- Domain Event: triggering

---

## Are They Different Architectural Viewpoints?

**YES.**

Each model is a VIEWPOINT — a way of looking at the same Canonical Publication from a specific angle.

**The projection model explains all viewpoints:**

```text
Canonical Publication
    ├── Business View (Model E)
    ├── Domain View (Model D)
    ├── Editorial View (Model F)
    ├── Integration View (Model A)
    ├── Persistence View (Model B)
    ├── Distribution View (Model G)
    ├── Temporal View (Models C, K)
    ├── DDD View (Models H, I, J)
    └── Documentation View (GLOSSARY definitions)
```

---

## Does One Canonical Publication Exist Beneath Them?

**YES — conceptually.**

The evidence supports the existence of a Canonical Publication:

1. **Semantic centrality** — Publication is the semantic center of the ontology
2. **Identity continuity** — Publication maintains identity across layers
3. **Contradiction resolution** — All 12 contradictions are resolved by projection
4. **DDD consistency** — DDD classifications are analytical lenses, not competing identities
5. **Layer consistency** — Publication appears differently on different layers but IS the same concept

**The Canonical Publication is:**

- Platform-independent (TJS-000 §3)
- Layer-independent (projection model)
- DDD-neutral (analytical lenses)
- Semantically consistent (one concept, many views)

---

## Would a Projection Model Remove Most Semantic Contradictions?

**YES.**

**Evidence:**

| Contradiction | Resolved? | How? |
|---------------|-----------|------|
| 7 different definitions | YES | Each is a view-specific projection |
| Platform independence vs Telegram | YES | Canonical is independent; Telegram is a view |
| Identity undefined | YES | Canonical has identity; views project it |
| Manual Publications excluded | YES | Different Canonical concept |
| Updated state ambiguity | YES | Canonical has clear lifecycle |
| Archival trigger vague | YES | Canonical has clear rules |
| Circular dependency with Issue | YES | Canonical relationships are clear |
| Ownership model gaps | YES | Canonical has clear ownership |
| Graphic Publication lifecycle | YES | Different Canonical concept |
| Repository vs Telegram authority | YES | Canonical is the authority |
| Publication content undefined | YES | Canonical has clear content |
| Relationship with Interpretation | YES | Clear derivation chain |
| Ownership boundaries | YES | Canonical has clear owner |
| Temporal scope | YES | Canonical has clear rules |
| Multi-channel publication | YES | Multiple channel views possible |
| Publication granularity | YES | Canonical has clear granularity |

**ALL 16 contradictions are resolved by the projection model.**

---

# Part 9: Hearing Certification

This document certifies that the Architectural Viewpoint Audit for Publication has been completed.

**Models analyzed:** 11

**Layers mapped:** 11

**Contradictions checked:** 16

**Contradictions resolved:** 16 (100%)

**Key findings:**

1. The eleven models are NOT competing — they are different viewpoints
2. One Canonical Publication conceptually exists beneath all viewpoints
3. A projection model explains all previous contradictions
4. DDD classifications are analytical lenses, not alternative identities
5. All 16 contradictions are resolved by the projection model

**Recommendation:** NONE

**Preferred model:** NONE

**Final verdict:** NONE

The Architect will decide.

---

# End of Viewpoint Audit
