# Reusable Knowledge

**Document Class:** Ontology Falsification

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document identifies reusable knowledge after falsification.

---

# Reusable Knowledge

## FOUNDATIONAL

### F-001: CONCEPT Definition

**Definition:** An abstract idea that describes the domain, cannot be created or destroyed, and is not directly observable.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-002: OBJECT Definition

**Definition:** A discrete, identifiable entity that exists in the system, can be created and destroyed, and has state.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-003: INSTANCE Definition

**Definition:** A concrete realization of a type that has identity and can be created and destroyed.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-004: COLLECTION Definition

**Definition:** A group of related entities that has boundaries and can contain multiple entities.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-005: PROCESS Definition

**Definition:** A discrete activity that transforms data, has input and output, and is repeatable.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-006: SERVICE Definition

**Definition:** A continuous activity performed by the system that provides capabilities and has defined interfaces.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-007: ROLE Definition

**Definition:** A logical responsibility performed within the system that describes behavior and is independent of implementation.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-008: ARTIFACT Definition

**Definition:** A physical or digital object produced by the system that can be stored and distributed.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-009: DOCUMENT Definition

**Definition:** Written or recorded information that has content, can be read, and has format.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-010: STATE Definition

**Definition:** A condition or mode of existence that can change over time and is observed.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

### F-011: EVENT Definition

**Definition:** An occurrence that happens at a specific time, has causes and effects, and triggers transitions.

**Confidence:** HIGH

**Evidence:** Survived falsification with 3 counterexamples.

---

## ARCHITECTURAL

### A-001: CONCEPT vs OBJECT Distinction

**Distinction:** CONCEPT is abstract, OBJECT is concrete.

**Necessary Conditions:**
- CONCEPT: Abstract, not observable, cannot be created
- OBJECT: Concrete, identifiable, can be created

**Confidence:** HIGH

**Evidence:** Survived pairwise falsification.

---

### A-002: SERVICE vs ROLE Distinction

**Distinction:** SERVICE is continuous activity, ROLE is logical responsibility.

**Necessary Conditions:**
- SERVICE: Continuous, provides capabilities
- ROLE: Logical, describes behavior

**Confidence:** HIGH

**Evidence:** Survived pairwise falsification.

---

### A-003: ARTIFACT vs DOCUMENT Distinction

**Distinction:** ARTIFACT is produced by system, DOCUMENT is written by humans.

**Necessary Conditions:**
- ARTIFACT: Physical/digital, produced by system
- DOCUMENT: Written, has content

**Confidence:** HIGH

**Evidence:** Survived pairwise falsification.

---

### A-004: PROCESS vs EVENT Distinction

**Distinction:** PROCESS is transformation, EVENT is occurrence.

**Necessary Conditions:**
- PROCESS: Discrete, transforms data
- EVENT: Instantaneous, has causes

**Confidence:** HIGH

**Evidence:** Survived pairwise falsification.

---

### A-005: STATE vs EVENT Distinction

**Distinction:** STATE is condition, EVENT is occurrence.

**Necessary Conditions:**
- STATE: Condition, can change
- EVENT: Instantaneous, triggers transitions

**Confidence:** HIGH

**Evidence:** Survived pairwise falsification.

---

## EDITORIAL

### E-001: Use Different Terms for Different Levels

**Rule:** Use different terms for CONCEPT vs OBJECT, SERVICE vs ROLE, ARTIFACT vs DOCUMENT.

**Confidence:** HIGH

**Evidence:** Falsification showed confusion when same terms used.

---

### E-002: Distinguish by Origin for ARTIFACT vs DOCUMENT

**Rule:** ARTIFACT is produced by system, DOCUMENT is written by humans.

**Confidence:** HIGH

**Evidence:** Pairwise falsification showed clear distinction.

---

### E-003: Distinguish by Temporal for PROCESS vs EVENT

**Rule:** PROCESS is discrete activity, EVENT is instantaneous occurrence.

**Confidence:** HIGH

**Evidence:** Pairwise falsification showed clear distinction.

---

### E-004: Distinguish by Persistence for SERVICE vs PROCESS

**Rule:** SERVICE is continuous, PROCESS is transient.

**Confidence:** HIGH

**Evidence:** Pairwise falsification showed clear distinction.

---

# Reusable Knowledge Summary

| Category | Count | Status |
|----------|-------|--------|
| FOUNDATIONAL | 11 | HIGH confidence |
| ARCHITECTURAL | 5 | HIGH confidence |
| EDITORIAL | 4 | HIGH confidence |
| **Total** | **20** | **ALL HIGH** |

---

# Traceability

| Knowledge | Source |
|-----------|--------|
| All knowledge | Analysis of falsification and pairwise falsification |

---

**End of Reusable Knowledge**
