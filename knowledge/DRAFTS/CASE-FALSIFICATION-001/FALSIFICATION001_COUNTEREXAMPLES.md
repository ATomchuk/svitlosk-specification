# Counterexamples

**Document Class:** Ontology Falsification

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document creates counterexamples for every category.

---

# Counterexamples

## CONCEPT

### Current Definition

An abstract idea that describes the domain.

### Counterexample 1: Database Table

**Why it breaks:** Database table is concrete, not abstract.

**Resolution:** CONCEPT must be abstract.

### Counterexample 2: File

**Why it breaks:** File is concrete, not abstract.

**Resolution:** CONCEPT must be abstract.

### Counterexample 3: User

**Why it breaks:** User is concrete, not abstract.

**Resolution:** CONCEPT must be abstract.

### Confidence: HIGH

Definition survives falsification.

---

## OBJECT

### Current Definition

A discrete, identifiable entity that exists in the system.

### Counterexample 1: Database Schema

**Why it breaks:** Schema is abstract, not concrete.

**Resolution:** OBJECT must be concrete.

### Counterexample 2: Algorithm

**Why it breaks:** Algorithm is abstract, not concrete.

**Resolution:** OBJECT must be concrete.

### Counterexample 3: Protocol

**Why it breaks:** Protocol is abstract, not concrete.

**Resolution:** OBJECT must be concrete.

### Confidence: HIGH

Definition survives falsification.

---

## INSTANCE

### Current Definition

A concrete realization of a type.

### Counterexample 1: Singleton

**Why it breaks:** Singleton is a single instance, but type is not defined.

**Resolution:** INSTANCE requires a type.

### Counterexample 2: Prototype

**Why it breaks:** Prototype is a model, not a realization.

**Resolution:** INSTANCE requires realization of type.

### Counterexample 3: Template

**Why it breaks:** Template is a model, not a realization.

**Resolution:** INSTANCE requires realization of type.

### Confidence: HIGH

Definition survives falsification.

---

## COLLECTION

### Current Definition

A group of related entities.

### Counterexample 1: Set of unrelated items

**Why it breaks:** Set contains unrelated items, not related entities.

**Resolution:** COLLECTION requires related entities.

### Counterexample 2: Null set

**Why it breaks:** Null set is empty, but COLLECTION requires multiple entities.

**Resolution:** COLLECTION requires multiple entities.

### Counterexample 3: Single entity

**Why it breaks:** Single entity is not a group.

**Resolution:** COLLECTION requires multiple entities.

### Confidence: HIGH

Definition survives falsification.

---

## PROCESS

### Current Definition

A discrete activity that transforms data.

### Counterexample 1: Continuous process

**Why it breaks:** Continuous process is not discrete.

**Resolution:** PROCESS must be discrete.

### Counterexample 2: Non-transforming activity

**Why it breaks:** Activity does not transform data.

**Resolution:** PROCESS must transform data.

### Counterexample 3: Event

**Why it breaks:** Event is instantaneous, not a process.

**Resolution:** PROCESS must be an activity.

### Confidence: HIGH

Definition survives falsification.

---

## SERVICE

### Current Definition

A continuous activity performed by the system.

### Counterexample 1: One-time service

**Why it breaks:** One-time service is not continuous.

**Resolution:** SERVICE must be continuous.

### Counterexample 2: External service

**Why it breaks:** External service is not performed by the system.

**Resolution:** SERVICE must be performed by the system.

### Counterexample 3: Process

**Why it breaks:** Process is discrete, not continuous.

**Resolution:** SERVICE must be continuous.

### Confidence: HIGH

Definition survives falsification.

---

## ROLE

### Current Definition

A logical responsibility performed within the system.

### Counterexample 1: Concrete implementation

**Why it breaks:** Concrete implementation is not logical.

**Resolution:** ROLE must be logical.

### Counterexample 2: Physical component

**Why it breaks:** Physical component is not a responsibility.

**Resolution:** ROLE must be a responsibility.

### Counterexample 3: Service

**Why it breaks:** Service is continuous activity, not responsibility.

**Resolution:** ROLE must be a responsibility.

### Confidence: HIGH

Definition survives falsification.

---

## ARTIFACT

### Current Definition

A physical or digital object produced by the system.

### Counterexample 1: Abstract concept

**Why it breaks:** Abstract concept is not physical or digital.

**Resolution:** ARTIFACT must be physical or digital.

### Counterexample 2: External object

**Why it breaks:** External object is not produced by the system.

**Resolution:** ARTIFACT must be produced by the system.

### Counterexample 3: Document

**Why it breaks:** Document is written information, not produced object.

**Resolution:** ARTIFACT must be produced by the system.

### Confidence: HIGH

Definition survives falsification.

---

## DOCUMENT

### Current Definition

Written or recorded information.

### Counterexample 1: Physical object

**Why it breaks:** Physical object is not written information.

**Resolution:** DOCUMENT must be written information.

### Counterexample 2: Digital artifact

**Why it breaks:** Digital artifact is produced, not written.

**Resolution:** DOCUMENT must be written information.

### Counterexample 3: Abstract concept

**Why it breaks:** Abstract concept is not written information.

**Resolution:** DOCUMENT must be written information.

### Confidence: HIGH

Definition survives falsification.

---

## STATE

### Current Definition

A condition or mode of existence.

### Counterexample 1: Event

**Why it breaks:** Event is instantaneous, not a condition.

**Resolution:** STATE must be a condition.

### Counterexample 2: Process

**Why it breaks:** Process is an activity, not a condition.

**Resolution:** STATE must be a condition.

### Counterexample 3: Object

**Why it breaks:** Object is an entity, not a condition.

**Resolution:** STATE must be a condition.

### Confidence: HIGH

Definition survives falsification.

---

## EVENT

### Current Definition

An occurrence that happens at a specific time.

### Counterexample 1: State

**Why it breaks:** State is a condition, not an occurrence.

**Resolution:** EVENT must be an occurrence.

### Counterexample 2: Process

**Why it breaks:** Process is an activity, not an occurrence.

**Resolution:** EVENT must be an occurrence.

### Counterexample 3: Object

**Why it breaks:** Object is an entity, not an occurrence.

**Resolution:** EVENT must be an occurrence.

### Confidence: HIGH

Definition survives falsification.

---

# Counterexample Summary

| Category | Counterexamples | Survives? |
|----------|-----------------|-----------|
| CONCEPT | 3 | YES |
| OBJECT | 3 | YES |
| INSTANCE | 3 | YES |
| COLLECTION | 3 | YES |
| PROCESS | 3 | YES |
| SERVICE | 3 | YES |
| ROLE | 3 | YES |
| ARTIFACT | 3 | YES |
| DOCUMENT | 3 | YES |
| STATE | 3 | YES |
| EVENT | 3 | YES |

---

# Traceability

| Counterexample | Source |
|----------------|--------|
| All counterexamples | Analysis of category definitions |

---

**End of Counterexamples**
