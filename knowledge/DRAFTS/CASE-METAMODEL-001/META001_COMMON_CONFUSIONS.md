# Common Confusions

**Document Class:** Meta-Model Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document identifies common confusions between categories.

---

# Common Confusions

## Confusion 1: CONCEPT vs OBJECT

### Problem

Same word used for abstract idea and concrete entity.

### Example

- Publisher (CONCEPT) — abstract idea
- Publisher (SERVICE) — concrete activity

### Resolution

Use different terms:
- Publisher Role (CONCEPT)
- Publisher Service (SERVICE)

---

## Confusion 2: SERVICE vs ROLE

### Problem

Same word used for continuous activity and abstract responsibility.

### Example

- Publisher (SERVICE) — continuous activity
- Publisher (ROLE) — abstract responsibility

### Resolution

Use different terms:
- Publisher Service (SERVICE)
- Publisher Role (ROLE)

---

## Confusion 3: ARTIFACT vs DOCUMENT

### Problem

Physical/digital objects confused with written information.

### Example

- Publication (ARTIFACT) — produced by system
- Specification (DOCUMENT) — authored by humans

### Resolution

Distinguish by origin:
- System-produced → ARTIFACT
- Human-authored → DOCUMENT

---

## Confusion 4: PROCESS vs EVENT

### Problem

Transformation activities confused with instantaneous occurrences.

### Example

- Parsing (PROCESS) — transformation
- Data Changed (EVENT) — occurrence

### Resolution

Distinguish by temporal characteristic:
- Transient activity → PROCESS
- Instantaneous occurrence → EVENT

---

## Confusion 5: SERVICE vs PROCESS

### Problem

Continuous activities confused with transient activities.

### Example

- Parser (SERVICE) — continuous
- Parsing (PROCESS) — transient

### Resolution

Distinguish by persistence:
- Continuous → SERVICE
- Transient → PROCESS

---

## Confusion 6: STATE vs EVENT

### Problem

Persistent conditions confused with instantaneous occurrences.

### Example

- Publication State (STATE) — persistent
- Publication Expired (EVENT) — instantaneous

### Resolution

Distinguish by temporal characteristic:
- Persistent condition → STATE
- Instantaneous occurrence → EVENT

---

## Confusion 7: COLLECTION vs OBJECT

### Problem

Groups of entities confused with single entities.

### Example

- Publication Package (COLLECTION) — multiple Publications
- Publication (OBJECT) — single entity

### Resolution

Distinguish by containment:
- Contains multiple → COLLECTION
- Single entity → OBJECT

---

## Confusion 8: CONCEPT vs ARTIFACT

### Problem

Abstract ideas confused with physical/digital objects.

### Example

- Publication (CONCEPT) — abstract idea
- Publication (ARTIFACT) — concrete object

### Resolution

Distinguish by concreteness:
- Abstract → CONCEPT
- Concrete → ARTIFACT

---

# Confusion Summary

| Confusion | Categories | Resolution |
|-----------|------------|------------|
| CONCEPT vs OBJECT | Abstract vs Concrete | Distinguish by creation ability |
| SERVICE vs ROLE | Activity vs Responsibility | Distinguish by description vs performance |
| ARTIFACT vs DOCUMENT | Physical vs Written | Distinguish by origin |
| PROCESS vs EVENT | Transformation vs Occurrence | Distinguish by temporal characteristic |
| SERVICE vs PROCESS | Continuous vs Transient | Distinguish by persistence |
| STATE vs EVENT | Condition vs Occurrence | Distinguish by temporal characteristic |
| COLLECTION vs OBJECT | Containment vs Entity | Distinguish by multiplicity |
| CONCEPT vs ARTIFACT | Idea vs Produced Object | Distinguish by concreteness |

---

# Traceability

| Confusion | Source |
|-----------|--------|
| All confusions | Analysis of category definitions and properties |

---

**End of Common Confusions**
