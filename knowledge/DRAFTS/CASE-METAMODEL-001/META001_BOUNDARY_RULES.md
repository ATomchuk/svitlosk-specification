# Boundary Rules

**Document Class:** Meta-Model Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines boundaries between categories.

---

# Boundary Rules

## Rule 1: CONCEPT vs OBJECT

### Boundary

Concepts are abstract ideas. Objects are concrete entities.

### Test

Can you create or destroy it?

- YES → OBJECT
- NO → CONCEPT

### Application

- Journal (CONCEPT) — cannot be created/destroyed
- Journal Edition (OBJECT) — can be created/destroyed

---

## Rule 2: OBJECT vs INSTANCE

### Boundary

Objects are generic entities. Instances are specific realizations.

### Test

Is it a realization of a type?

- YES → INSTANCE
- NO → OBJECT

### Application

- Publication (OBJECT) — generic type
- Publication for Territory X (INSTANCE) — specific realization

---

## Rule 3: CONCEPT vs SERVICE

### Boundary

Concepts are abstract ideas. Services are continuous activities.

### Test

Does it perform continuous activity?

- YES → SERVICE
- NO → CONCEPT

### Application

- Publisher (CONCEPT) — abstract idea
- Publisher (SERVICE) — continuous activity

---

## Rule 4: SERVICE vs ROLE

### Boundary

Services are concrete activities. Roles are abstract responsibilities.

### Test

Does it describe behavior or perform activity?

- Describes behavior → ROLE
- Performs activity → SERVICE

### Application

- Publisher (ROLE) — describes responsibility
- Publisher (SERVICE) — performs activity

---

## Rule 5: ARTIFACT vs DOCUMENT

### Boundary

Artifacts are physical/digital objects. Documents are written information.

### Test

Is it produced by system or authored by humans?

- Produced by system → ARTIFACT
- Authored by humans → DOCUMENT

### Application

- Publication (ARTIFACT) — produced by system
- Specification (DOCUMENT) — authored by humans

---

## Rule 6: PROCESS vs EVENT

### Boundary

Processes are transformations. Events are occurrences.

### Test

Is it an activity or an occurrence?

- Activity → PROCESS
- Occurrence → EVENT

### Application

- Parsing (PROCESS) — transformation activity
- Data Changed (EVENT) — occurrence

---

## Rule 7: COLLECTION vs OBJECT

### Boundary

Collections contain multiple entities. Objects are single entities.

### Test

Does it contain multiple entities?

- YES → COLLECTION
- NO → OBJECT

### Application

- Publication Package (COLLECTION) — contains Publications
- Publication (OBJECT) — single entity

---

## Rule 8: CONCEPT vs ARTIFACT

### Boundary

Concepts are abstract ideas. Artifacts are physical/digital objects.

### Test

Is it abstract or concrete?

- Abstract → CONCEPT
- Concrete → ARTIFACT

### Application

- Publication (CONCEPT) — abstract idea
- Publication (ARTIFACT) — concrete object

---

## Rule 9: SERVICE vs PROCESS

### Boundary

Services are continuous. Processes are transient.

### Test

Does it persist or complete?

- Persists → SERVICE
- Completes → PROCESS

### Application

- Parser (SERVICE) — continuous activity
- Parsing (PROCESS) — transient activity

---

## Rule 10: ROLE vs SERVICE

### Boundary

Roles are abstract responsibilities. Services are concrete activities.

### Test

Does it describe behavior or perform activity?

- Describes behavior → ROLE
- Performs activity → SERVICE

### Application

- Publisher (ROLE) — abstract responsibility
- Publisher (SERVICE) — concrete activity

---

## Rule 11: STATE vs EVENT

### Boundary

States are conditions. Events are occurrences.

### Test

Does it persist or occur?

- Persists → STATE
- Occurs → EVENT

### Application

- Publication State (STATE) — persistent condition
- Publication Expired (EVENT) — instantaneous occurrence

---

# Boundary Summary

| Rule | Boundary | Test |
|------|----------|------|
| 1 | CONCEPT vs OBJECT | Can create/destroy? |
| 2 | OBJECT vs INSTANCE | Realization of type? |
| 3 | CONCEPT vs SERVICE | Performs activity? |
| 4 | SERVICE vs ROLE | Describes vs performs? |
| 5 | ARTIFACT vs DOCUMENT | Produced vs authored? |
| 6 | PROCESS vs EVENT | Activity vs occurrence? |
| 7 | COLLECTION vs OBJECT | Contains multiple? |
| 8 | CONCEPT vs ARTIFACT | Abstract vs concrete? |
| 9 | SERVICE vs PROCESS | Persists vs completes? |
| 10 | ROLE vs SERVICE | Describes vs performs? |
| 11 | STATE vs EVENT | Persists vs occurs? |

---

# Traceability

| Rule | Source |
|------|--------|
| All rules | Analysis of category definitions and properties |

---

**End of Boundary Rules**
