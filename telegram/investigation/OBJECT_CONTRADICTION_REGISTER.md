# OBJECT_CONTRADICTION_REGISTER

**Document ID:** CASE001E-CONTRADICTIONS

**Title:** Object — Contradiction Register

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Object Ontology Investigation

---

# Purpose

This document searches specifically for Object-related contradictions in the repository.

---

# Contradictions Found

## Contradiction 1: Entity vs Object

**Evidence:**

- DATA_MODEL.md uses "Entity" (Reference Entities, Operational Entities, Publication Entities, Archive Entities)
- Previous investigations use "Object" (Publication, Territory, Address)
- GLOSSARY.md does not define "Object" explicitly

**Documents:**

- DATA_MODEL.md §Logical Entity Groups
- GLOSSARY.md (no "Object" definition)

**Severity:** MEDIUM

**Possible Explanation:** "Entity" is the data model term. "Object" is the ontological term. They overlap but are not identical.

---

## Contradiction 2: Representation Treated as Object

**Evidence:**

- Telegram Message is sometimes called an "object" but is actually a representation
- Historical Record is sometimes called an "object" but is actually a representation
- Repository Object is sometimes called an "object" but is actually a representation

**Documents:**

- Previous investigations (CASE001_PUBLICATION_STATE_MODEL.md)
- TJS-000A §10

**Severity:** MEDIUM

**Possible Explanation:** Representations are colloquially called "objects" but are ontologically distinct from domain objects.

---

## Contradiction 3: Component vs Object

**Evidence:**

- GLOSSARY.md §7: "A Component SHALL NOT be considered a business concept"
- But Components are often discussed alongside domain objects
- Components have identity, lifecycle, and relationships like objects

**Documents:**

- GLOSSARY.md §7
- ARCHITECTURE.md

**Severity:** LOW

**Possible Explanation:** Components are architectural objects, not business objects. They are a different category.

---

## Contradiction 4: Identity Confusion

**Evidence:**

- Some objects have intrinsic Identity (Publication, Territory)
- Some objects borrow Identity (Telegram Message, Historical Record)
- Some objects have no intrinsic Identity (Publication Package)
- No universal rule for when objects have Identity

**Documents:**

- CASE001C_IDENTITY_RESEARCH.md
- CASE001D_IDENTITY_IDENTIFIER_RESEARCH.md

**Severity:** MEDIUM

**Possible Explanation:** Identity is not a universal property. Different objects have different Identity characteristics.

---

## Contradiction 5: Lifecycle Confusion

**Evidence:**

- Some objects have complex lifecycles (Publication: Generated → Published → Updated → Archived → Removed)
- Some objects have simple lifecycles (Territory: static)
- Some objects have no lifecycle (Address: permanent)
- No universal lifecycle model

**Documents:**

- TJS-021 §4
- DATA_MODEL.md

**Severity:** LOW

**Possible Explanation:** Lifecycle complexity varies by object type. This is expected.

---

## Contradiction 6: Ownership Confusion

**Evidence:**

- Publication Engine owns Publications
- Parser owns Normalized Dataset
- But who owns Territory? Address? Queue?
- Real-world objects have no owner in the system

**Documents:**

- TJS-010 §4.1
- GLOSSARY.md §4-5

**Severity:** MEDIUM

**Possible Explanation:** Ownership is a system concept, not a universal property. Real-world objects are referenced, not owned.

---

## Contradiction 7: Object vs Data

**Evidence:**

- DATA_MODEL.md distinguishes between "entities" and "data"
- But some entities ARE data (Normalized Dataset, Schedule)
- The boundary between Object and Data is unclear

**Documents:**

- DATA_MODEL.md §Data Categories
- GLOSSARY.md §2

**Severity:** LOW

**Possible Explanation:** Data is a property of objects, not a separate category. Objects contain data.

---

## Contradiction 8: Object vs Concept

**Evidence:**

- GLOSSARY.md defines "concepts" (Publication, Territory, Address)
- But concepts are also objects in the ontology
- The boundary between Object and Concept is unclear

**Documents:**

- GLOSSARY.md §1-7
- TELEGRAM_GLOSSARY.md

**Severity:** LOW

**Possible Explanation:** Concepts are the semantic meaning of objects. Objects are the concrete instantiation of concepts.

---

# Contradiction Summary

| # | Contradiction | Severity | Resolved? |
|---|---------------|----------|-----------|
| 1 | Entity vs Object | MEDIUM | PARTIALLY — different terms for overlapping concepts |
| 2 | Representation treated as Object | MEDIUM | YES — representations are projections, not objects |
| 3 | Component vs Object | LOW | YES — components are architectural objects |
| 4 | Identity confusion | MEDIUM | YES — Identity is not universal |
| 5 | Lifecycle confusion | LOW | YES — lifecycle complexity varies |
| 6 | Ownership confusion | MEDIUM | YES — ownership is a system concept |
| 7 | Object vs Data | LOW | YES — data is a property of objects |
| 8 | Object vs Concept | LOW | YES — concepts are semantic meaning |

---

# Contradiction Counts

| Severity | Count |
|----------|-------|
| HIGH | 0 |
| MEDIUM | 4 |
| LOW | 4 |
| **Total** | **8** |

---

# End of Contradiction Register
