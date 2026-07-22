# Category Comparison

**Document Class:** Meta-Model Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document analyzes every pair of categories.

---

# Category Comparison

## CONCEPT vs OBJECT

### Border

CONCEPT is abstract, OBJECT is concrete.

### Key Difference

Concepts cannot be created or destroyed. Objects can.

### Evidence

- Journal (CONCEPT) vs Journal Edition (OBJECT)
- Publisher (CONCEPT) vs Publication (ARTIFACT)

### Confusion Risk

MEDIUM — both describe domain entities.

---

## OBJECT vs INSTANCE

### Border

OBJECT is a discrete entity. INSTANCE is a concrete realization of a type.

### Key Difference

Objects are generic, instances are specific.

### Evidence

- Publication (OBJECT) vs Publication for Territory X (INSTANCE)

### Confusion Risk

LOW — instances are a subset of objects.

---

## CONCEPT vs SERVICE

### Border

CONCEPT is abstract. SERVICE is continuous activity.

### Key Difference

Concepts describe ideas. Services perform activities.

### Evidence

- Publisher (CONCEPT) vs Publisher (SERVICE)

### Confusion Risk

MEDIUM — same word used for different levels.

---

## SERVICE vs ROLE

### Border

SERVICE is continuous activity. ROLE is logical responsibility.

### Key Difference

Services are concrete, roles are abstract.

### Evidence

- Publisher (SERVICE) vs Publisher (ROLE)

### Confusion Risk

HIGH — same word used for different concepts.

---

## ARTIFACT vs DOCUMENT

### Border

ARTIFACT is physical/digital object. DOCUMENT is written information.

### Key Difference

Artifacts are produced by system. Documents are authored.

### Evidence

- Publication (ARTIFACT) vs Specification (DOCUMENT)

### Confusion Risk

LOW — different origins.

---

## PROCESS vs EVENT

### Border

PROCESS is transformation. EVENT is occurrence.

### Key Difference

Processes are activities, events are instantaneous.

### Evidence

- Parsing (PROCESS) vs Data Changed (EVENT)

### Confusion Risk

LOW — different temporal characteristics.

---

## COLLECTION vs OBJECT

### Border

COLLECTION contains multiple entities. OBJECT is a single entity.

### Key Difference

Collections contain, objects are contained.

### Evidence

- Publication Package (COLLECTION) vs Publication (OBJECT)

### Confusion Risk

LOW — clear containment relationship.

---

## CONCEPT vs ARTIFACT

### Border

CONCEPT is abstract. ARTIFACT is physical/digital.

### Key Difference

Concepts are ideas, artifacts are produced objects.

### Evidence

- Publication (CONCEPT) vs Publication (ARTIFACT)

### Confusion Risk

MEDIUM — same word used for different levels.

---

## SERVICE vs PROCESS

### Border

SERVICE is continuous. PROCESS is transient.

### Key Difference

Services persist, processes complete.

### Evidence

- Parser (SERVICE) vs Parsing (PROCESS)

### Confusion Risk

MEDIUM — related but different.

---

## ROLE vs SERVICE

### Border

ROLE is abstract responsibility. SERVICE is concrete activity.

### Key Difference

Roles describe, services perform.

### Evidence

- Publisher (ROLE) vs Publisher (SERVICE)

### Confusion Risk

HIGH — same word used for different concepts.

---

## STATE vs EVENT

### Border

STATE is condition. EVENT is occurrence.

### Key Difference

States persist, events are instantaneous.

### Evidence

- Publication State (STATE) vs Publication Expired (EVENT)

### Confusion Risk

LOW — different temporal characteristics.

---

# Comparison Summary

| Pair | Border | Confusion Risk |
|------|--------|----------------|
| CONCEPT vs OBJECT | Abstract vs Concrete | MEDIUM |
| OBJECT vs INSTANCE | Generic vs Specific | LOW |
| CONCEPT vs SERVICE | Abstract vs Activity | MEDIUM |
| SERVICE vs ROLE | Activity vs Responsibility | HIGH |
| ARTIFACT vs DOCUMENT | Physical vs Written | LOW |
| PROCESS vs EVENT | Transformation vs Occurrence | LOW |
| COLLECTION vs OBJECT | Containment vs Entity | LOW |
| CONCEPT vs ARTIFACT | Idea vs Produced Object | MEDIUM |
| SERVICE vs PROCESS | Continuous vs Transient | MEDIUM |
| ROLE vs SERVICE | Abstract vs Concrete | HIGH |
| STATE vs EVENT | Condition vs Occurrence | LOW |

---

# Traceability

| Comparison | Source |
|------------|--------|
| All comparisons | Analysis of category definitions and properties |

---

**End of Category Comparison**
