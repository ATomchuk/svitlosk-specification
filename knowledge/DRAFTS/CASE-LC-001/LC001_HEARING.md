# LC001_HEARING

**Document ID:** CASE-LC-001

**Title:** Information Lifecycle Ontology Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-LC-001: reconstruction of the ontology of the Information Lifecycle.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The ONTOLOGY of the Information Lifecycle — what it is, what operations it contains, which subsystem owns each operation, and how it relates to other components.

## 2.2 What This Case Does NOT Investigate

- Software implementation
- Infrastructure
- Existing specification validity
- Channel-specific behavior (Telegram, Facebook)

## 2.3 Investigation Constraint

This investigation reconstructs the ONTOLOGY of the lifecycle itself.

It must NOT redesign the architecture.

---

# 3. Context

## 3.1 Previous Investigations

- CASE-SVT-ONTOLOGY-001: SvitloSk ontology reconstruction
- CASE-INF-001: Information ontology

## 3.2 Established Information Lifecycle

The Information Lifecycle has been identified as:

```
ORIGIN → ACQUISITION → NORMALIZATION → INTERPRETATION → PRESENTATION → DELIVERY → ARCHIVAL
```

This lifecycle is considered channel-independent.

## 3.3 Unresolved Question

One fundamental architectural question remains unresolved:

> What actually owns the Information Lifecycle?

> Does the Publishing Subsystem decide what happens to information?

> Or does the Information Lifecycle itself control publication?

---

# 4. Research Tasks

## Research 1 — Lifecycle Ontological Category

Determine whether Lifecycle is:
- object
- process
- state machine
- service
- engine
- protocol
- orchestration
- something else

## Research 2 — Lifecycle Operations

Identify every lifecycle operation:
- Create
- Update
- Replace
- Merge
- Republish
- Expire
- Archive
- Hide
- Reveal
- Delete
- Suspend
- Resume

Determine whether these operations are intrinsic to Lifecycle or belong elsewhere.

## Research 3 — Operation Ownership

Determine which subsystem SHOULD own each operation:
- Parser
- Information Lifecycle
- Publishing Kernel
- Telegram Adapter
- Facebook Adapter
- Journal
- Publication
- Issue
- None of the above

Construct competing models.

## Research 4 — Update Behavior

Investigate update behavior:
- Parser updates today.txt every two hours
- Who decides that an existing Telegram post must be edited?
- Parser? Lifecycle? Publisher? Telegram Adapter?
- Determine the complete causal chain

## Research 5 — Temporal Behavior

Investigate temporal behavior:
- Tomorrow planned outages disappear at end of current day
- Technical message always shows latest update timestamp
- Graph for tomorrow is replaced
- Temporary information expires
- Which architectural component owns temporal behavior?

## Research 6 — Publication Ownership

Differentiate:
- Information changes
- Publication changes
- Representation changes

Determine whether these are independent events.

## Research 7 — Competing Architectures

Construct competing architectures:
- A: Lifecycle inside Publisher
- B: Publisher inside Lifecycle
- C: Independent Lifecycle Engine
- D: Event-driven model
- E: Any additional architecture discovered

Do not recommend.

## Research 8 — Contradictions

Search for contradictions against:
- CASE-PUB-001
- CASE-JRN-001
- CASE-INF-001
- META-005
- META-006A

Document every contradiction.

## Research 9 — Hidden Assumptions

Search for hidden assumptions, especially those inherited from traditional publishing.

## Research 10 — Publisher Thickness

Determine whether Publisher should become thinner.
Investigate whether Publisher is only a transport layer.

No recommendation. Only evidence.

---

# 5. Deliverables

| Document | Purpose |
|----------|---------|
| LC001_HEARING.md | Case scope and research questions |
| LC001_RESEARCH1_ONTOLOGY.md | Lifecycle ontological category |
| LC001_RESEARCH2_OPERATIONS.md | Lifecycle operations |
| LC001_RESEARCH3_OWNERSHIP.md | Operation ownership |
| LC001_RESEARCH4_UPDATE.md | Update behavior |
| LC001_RESEARCH5_TEMPORAL.md | Temporal behavior |
| LC001_RESEARCH6_PUBLICATION.md | Publication ownership |
| LC001_RESEARCH7_ARCHITECTURES.md | Competing architectures |
| LC001_RESEARCH8_CONTRADICTIONS.md | Contradictions |
| LC001_RESEARCH9_ASSUMPTIONS.md | Hidden assumptions |
| LC001_RESEARCH10_PUBLISHER.md | Publisher thickness |
| LC001_GLOSSARY.md | Candidate glossary |
| LC001_QUESTIONS.md | Open questions |
| LC001_CERTIFICATE.md | Investigation certificate |

---

# 6. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
