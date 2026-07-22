# Pairwise Falsification

**Document Class:** Ontology Falsification

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document performs pairwise falsification.

---

# Pairwise Falsification

## CONCEPT vs OBJECT

### Attempt to Falsify

Could an OBJECT actually be a CONCEPT?

### Counterexample

Database Table is an OBJECT but could be considered a CONCEPT.

### Why It Fails

Database Table is concrete, not abstract. CONCEPT must be abstract.

### Distinction Accepted

**Necessary Conditions:**
- CONCEPT: Abstract, not observable, cannot be created
- OBJECT: Concrete, identifiable, can be created

**Sufficient Conditions:**
- CONCEPT: Abstract AND not observable
- OBJECT: Concrete AND identifiable

**Impossible Conditions:**
- CONCEPT: Concrete
- OBJECT: Abstract

**Minimal Example:**
- CONCEPT: Inheritance (abstract idea)
- OBJECT: Journal Edition (concrete entity)

**Counterexample Rejection:** Database Table is concrete, not abstract.

### Confidence: HIGH

---

## OBJECT vs INSTANCE

### Attempt to Falsify

Could an OBJECT actually be an INSTANCE?

### Counterexample

Journal Edition is an OBJECT but could be considered an INSTANCE.

### Why It Fails

Journal Edition is a generic type, not a specific realization.

### Distinction Accepted

**Necessary Conditions:**
- OBJECT: Generic entity
- INSTANCE: Specific realization of type

**Sufficient Conditions:**
- OBJECT: Concrete AND identifiable
- INSTANCE: Concrete AND realization of type

**Impossible Conditions:**
- OBJECT: Abstract
- INSTANCE: Not realization of type

**Minimal Example:**
- OBJECT: Publication (generic type)
- INSTANCE: Publication for Territory X (specific realization)

**Counterexample Rejection:** Publication is generic, not specific.

### Confidence: HIGH

---

## SERVICE vs ROLE

### Attempt to Falsify

Could a ROLE actually be a SERVICE?

### Counterexample

Publisher is a ROLE but could be considered a SERVICE.

### Why It Fails

Publisher as ROLE is abstract responsibility, not continuous activity.

### Distinction Accepted

**Necessary Conditions:**
- SERVICE: Continuous activity, provides capabilities
- ROLE: Logical responsibility, describes behavior

**Sufficient Conditions:**
- SERVICE: Continuous AND provides capabilities
- ROLE: Logical AND describes behavior

**Impossible Conditions:**
- SERVICE: Abstract
- ROLE: Continuous activity

**Minimal Example:**
- SERVICE: Parser (continuous activity)
- ROLE: Publisher (abstract responsibility)

**Counterexample Rejection:** Publisher as ROLE is abstract, not continuous.

### Confidence: HIGH

---

## ARTIFACT vs DOCUMENT

### Attempt to Falsify

Could an ARTIFACT actually be a DOCUMENT?

### Counterexample

Publication is an ARTIFACT but could be considered a DOCUMENT.

### Why It Fails

Publication is produced by system, not written by humans.

### Distinction Accepted

**Necessary Conditions:**
- ARTIFACT: Physical/digital, produced by system
- DOCUMENT: Written, has content

**Sufficient Conditions:**
- ARTIFACT: Physical/digital AND produced by system
- DOCUMENT: Written AND has content

**Impossible Conditions:**
- ARTIFACT: Abstract
- DOCUMENT: Physical/digital produced by system

**Minimal Example:**
- ARTIFACT: Publication (produced by system)
- DOCUMENT: Specification (written by humans)

**Counterexample Rejection:** Publication is produced, not written.

### Confidence: HIGH

---

## PROCESS vs EVENT

### Attempt to Falsify

Could an EVENT actually be a PROCESS?

### Counterexample

Data Changed is an EVENT but could be considered a PROCESS.

### Why It Fails

Data Changed is instantaneous, not a transformation.

### Distinction Accepted

**Necessary Conditions:**
- PROCESS: Discrete activity, transforms data
- EVENT: Instantaneous, has causes and effects

**Sufficient Conditions:**
- PROCESS: Discrete AND transforms data
- EVENT: Instantaneous AND has causes

**Impossible Conditions:**
- PROCESS: Instantaneous
- EVENT: Transforms data

**Minimal Example:**
- PROCESS: Parsing (discrete activity)
- EVENT: Data Changed (instantaneous occurrence)

**Counterexample Rejection:** Data Changed is instantaneous, not a process.

### Confidence: HIGH

---

## SERVICE vs PROCESS

### Attempt to Falsify

Could a PROCESS actually be a SERVICE?

### Counterexample

Parsing is a PROCESS but could be considered a SERVICE.

### Why It Fails

Parsing is transient, not continuous.

### Distinction Accepted

**Necessary Conditions:**
- SERVICE: Continuous, provides capabilities
- PROCESS: Discrete, transforms data

**Sufficient Conditions:**
- SERVICE: Continuous AND provides capabilities
- PROCESS: Discrete AND transforms data

**Impossible Conditions:**
- SERVICE: Discrete
- PROCESS: Continuous

**Minimal Example:**
- SERVICE: Parser (continuous activity)
- PROCESS: Parsing (discrete activity)

**Counterexample Rejection:** Parsing is discrete, not continuous.

### Confidence: HIGH

---

## STATE vs EVENT

### Attempt to Falsify

Could an EVENT actually be a STATE?

### Counterexample

Publication Expired is an EVENT but could be considered a STATE.

### Why It Fails

Publication Expired is instantaneous, not a condition.

### Distinction Accepted

**Necessary Conditions:**
- STATE: Condition, can change, is observed
- EVENT: Instantaneous, has causes, triggers transitions

**Sufficient Conditions:**
- STATE: Condition AND can change
- EVENT: Instantaneous AND has causes

**Impossible Conditions:**
- STATE: Instantaneous
- EVENT: Condition

**Minimal Example:**
- STATE: Publication State (condition)
- EVENT: Publication Expired (instantaneous occurrence)

**Counterexample Rejection:** Publication Expired is instantaneous, not a condition.

### Confidence: HIGH

---

## COLLECTION vs OBJECT

### Attempt to Falsify

Could an OBJECT actually be a COLLECTION?

### Counterexample

Journal Edition is an OBJECT but could be considered a COLLECTION.

### Why It Fails

Journal Edition is a single entity, not a group.

### Distinction Accepted

**Necessary Conditions:**
- OBJECT: Single entity
- COLLECTION: Group of related entities

**Sufficient Conditions:**
- OBJECT: Concrete AND identifiable
- COLLECTION: Group AND has boundaries

**Impossible Conditions:**
- OBJECT: Group
- COLLECTION: Single entity

**Minimal Example:**
- OBJECT: Publication (single entity)
- COLLECTION: Publication Package (group of Publications)

**Counterexample Rejection:** Publication is single, not a group.

### Confidence: HIGH

---

# Pairwise Falsification Summary

| Pair | Falsification Attempted | Distinction Accepted | Confidence |
|------|------------------------|---------------------|------------|
| CONCEPT vs OBJECT | YES | YES | HIGH |
| OBJECT vs INSTANCE | YES | YES | HIGH |
| SERVICE vs ROLE | YES | YES | HIGH |
| ARTIFACT vs DOCUMENT | YES | YES | HIGH |
| PROCESS vs EVENT | YES | YES | HIGH |
| SERVICE vs PROCESS | YES | YES | HIGH |
| STATE vs EVENT | YES | YES | HIGH |
| COLLECTION vs OBJECT | YES | YES | HIGH |

---

# Traceability

| Pairwise Falsification | Source |
|------------------------|--------|
| All pairwise falsifications | Analysis of category definitions and counterexamples |

---

**End of Pairwise Falsification**
