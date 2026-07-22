# Mixed Levels

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document detects mixed abstraction levels.

---

# Mixed Levels

## MIXED-001: Publisher (Concept) vs Publisher (Service) vs Publisher (Role)

### Current State

Publisher exists at THREE levels:
- Level 1: CONCEPT (abstract idea)
- Level 4: SERVICE (continuous activity)
- Level 5: ROLE (logical responsibility)

### Problem

These are DIFFERENT architectural levels mixed under the same name.

### Evidence

- GLOSSARY §7: "Publisher: The logical Role..."
- CASE-PUB-004: "Publisher is an EXECUTOR..."
- CASE-SVT-ONTOLOGY-001: "Publisher as service"

### Classification

MIXED LEVELS — same name at different levels.

---

## MIXED-002: Publication (Concept) vs Publication (Artifact)

### Current State

Publication exists at TWO levels:
- Level 1: CONCEPT (abstract idea)
- Level 6: ARTIFACT (physical/digital object)

### Problem

These are DIFFERENT architectural levels mixed under the same name.

### Evidence

- GLOSSARY §3: "Publication: A public information message..."
- CASE-PUB-001: "Publication is atomic unit"

### Classification

MIXED LEVELS — same name at different levels.

---

## MIXED-003: Representation (Artifact) vs Rendering (Process)

### Current State

Representation is Level 6 (ARTIFACT).

Rendering is Level 3 (PROCESS).

### Problem

These are DIFFERENT architectural levels.

### Evidence

- CASE-INF-001: "Representation is channel-specific output"
- CASE-TG-CORE-001: "Rendering is conversion process"

### Classification

DIFFERENT LEVELS — correctly separated.

---

## MIXED-004: Schedule (Concept) vs Graph Publication (Artifact)

### Current State

Schedule is Level 1 (CONCEPT).

Graph Publication is Level 6 (ARTIFACT).

### Problem

These are DIFFERENT architectural levels.

### Evidence

- GLOSSARY §5: "Schedule: Logical representation of electricity availability"
- CASE-INFPROD-001: "Graph Publication is product type"

### Classification

DIFFERENT LEVELS — correctly separated.

---

## MIXED-005: Journal (Concept) vs Journal (Service) vs Journal Edition (Object)

### Current State

Journal exists at TWO levels:
- Level 1: CONCEPT (abstract idea)
- Level 4: SERVICE (continuous activity)

Journal Edition is Level 2 (OBJECT).

### Problem

Journal and Journal Edition are DIFFERENT architectural levels.

### Evidence

- CHARTER §10: "Journal is primary communication channel"
- CASE-JRN-001: "Journal Edition is daily instance"

### Classification

DIFFERENT LEVELS — correctly separated.

---

## MIXED-006: Lifecycle (Concept) vs Lifecycle State (State)

### Current State

Lifecycle is Level 1 (CONCEPT).

Lifecycle State is Level 8 (STATE).

### Problem

These are DIFFERENT architectural levels.

### Evidence

- CASE-LC-001: "Lifecycle is a pattern"
- TELEGRAM_LIFECYCLE: "Lifecycle State is condition"

### Classification

DIFFERENT LEVELS — correctly separated.

---

## MIXED-007: Publication Package (Object) vs Publication Package (Artifact)

### Current State

Publication Package exists at TWO levels:
- Level 2: OBJECT (discrete entity)
- Level 6: ARTIFACT (physical/digital object)

### Problem

These are DIFFERENT architectural levels mixed under the same name.

### Evidence

- GLOSSARY §3: "Publication Package: The complete collection..."
- CASE-PUB-001: "Publication Package is composite"

### Classification

MIXED LEVELS — same name at different levels.

---

## MIXED-008: Journal Edition (Object) vs Journal Edition (Artifact)

### Current State

Journal Edition exists at TWO levels:
- Level 2: OBJECT (discrete entity)
- Level 6: ARTIFACT (physical/digital object)

### Problem

These are DIFFERENT architectural levels mixed under the same name.

### Evidence

- CASE-JRN-001: "Journal Edition is daily instance"
- CASE-INFPROD-001: "Journal Edition contains Publications"

### Classification

MIXED LEVELS — same name at different levels.

---

# Mixed Levels Summary

| Mixed ID | Entity | Levels | Problem |
|----------|--------|--------|---------|
| MIXED-001 | Publisher | CONCEPT, SERVICE, ROLE | Same name at different levels |
| MIXED-002 | Publication | CONCEPT, ARTIFACT | Same name at different levels |
| MIXED-003 | Representation, Rendering | ARTIFACT, PROCESS | Different levels (correct) |
| MIXED-004 | Schedule, Graph Publication | CONCEPT, ARTIFACT | Different levels (correct) |
| MIXED-005 | Journal, Journal Edition | CONCEPT/SERVICE, OBJECT | Different levels (correct) |
| MIXED-006 | Lifecycle, Lifecycle State | CONCEPT, STATE | Different levels (correct) |
| MIXED-007 | Publication Package | OBJECT, ARTIFACT | Same name at different levels |
| MIXED-008 | Journal Edition | OBJECT, ARTIFACT | Same name at different levels |

---

# Traceability

| Mixed Level | Source |
|-------------|--------|
| All mixed levels | Analysis of entity classification and architectural levels |

---

**End of Mixed Levels**
