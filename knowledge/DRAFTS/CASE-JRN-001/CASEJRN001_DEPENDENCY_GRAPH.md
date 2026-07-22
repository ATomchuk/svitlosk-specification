# CASEJRN001_DEPENDENCY_GRAPH

**Document ID:** CASE-JRN-001-DEP

**Title:** Dependency Graph

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs the dependency graph of Journal concepts, showing which concepts depend on which other concepts.

---

# 2. Concept Dependencies

## 2.1 Journal Dependencies

### Journal depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| Publication | CONTAINS | CHARTER.md §10 ("daily publications") |
| Reporting Period | TEMPORAL | CHARTER.md §10 ("daily") |
| Territory | SPATIAL | User context (organized by territory) |
| Channel | DELIVERS | CHARTER.md §10 ("communication channel") |

### Journal is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| Issue | INSTANTIATES | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| Release | REALIZES | User context |

---

## 2.2 Publication Dependencies

### Publication depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| Interpretation Result | DERIVED_FROM | GLOSSARY.md §3 |
| Reporting Period | TEMPORAL | GLOSSARY.md §3 |
| Territory | SPATIAL | GLOSSARY.md §4 |
| Channel | DELIVERED_VIA | GLOSSARY.md §3 |

### Publication is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| Publication Package | COLLECTS | GLOSSARY.md §3 |
| Issue | CONTAINS | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| Release | CONTAINS | User context |

---

## 2.3 Publication Package Dependencies

### Publication Package depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| Publication | COLLECTS | GLOSSARY.md §3 |
| Reporting Period | TEMPORAL | GLOSSARY.md §3 |

### Publication Package is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| Issue | REALIZES | TELEGRAM_PUBLICATION_LIFECYCLE.md |

---

## 2.4 Reporting Period Dependencies

### Reporting Period depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| (none) | — | GLOSSARY.md §2 |

### Reporting Period is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| Journal | TEMPORAL_BOUNDARY | CHARTER.md §10 |
| Publication | TEMPORAL_IDENTITY | GLOSSARY.md §3 |
| Publication Package | TEMPORAL_BOUNDARY | GLOSSARY.md §3 |
| Issue | TEMPORAL_BOUNDARY | TELEGRAM_PUBLICATION_LIFECYCLE.md |

---

## 2.5 Territory Dependencies

### Territory depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| Community | PARENT | GLOSSARY.md §4 |
| Administrative Centre | SUBTYPE | GLOSSARY.md §4 |
| Starosta District | SUBTYPE | GLOSSARY.md §4 |

### Territory is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| Journal | SPATIAL_BOUNDARY | User context |
| Publication | SPATIAL_IDENTITY | GLOSSARY.md §4 |

---

## 2.6 Issue Dependencies

### Issue depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| Journal | INSTANTIATES | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| Publication | CONTAINS | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| Reporting Period | TEMPORAL_BOUNDARY | TELEGRAM_PUBLICATION_LIFECYCLE.md |

### Issue is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| (none) | — | — |

---

## 2.7 Release Dependencies

### Release depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| Journal | REALIZES | User context |
| Publication | CONTAINS | User context |
| Territory | ORGANIZES_BY | User context |
| Reporting Period | TEMPORAL_BOUNDARY | User context |

### Release is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| (none) | — | — |

---

## 2.8 Channel Dependencies

### Channel depends on:

| Dependency | Type | Evidence |
|------------|------|----------|
| Publication | DELIVERS | GLOSSARY.md §3 |

### Channel is depended upon by:

| Dependent | Type | Evidence |
|-----------|------|----------|
| Journal | DELIVERS_VIA | CHARTER.md §10 |

---

# 3. Dependency Graph

## 3.1 Visual Representation

```
                    ┌─────────────┐
                    │  Reporting  │
                    │   Period    │
                    └──────┬──────┘
                           │
                           ▼
┌──────────┐        ┌──────────────┐        ┌──────────┐
│ Territory├───────►│   Journal    │◄───────┤ Channel  │
└──────────┘        └──────┬───────┘        └──────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │  Issue   │ │ Release  │ │Pub. Pkg. │
        └────┬─────┘ └────┬─────┘ └────┬─────┘
             │            │            │
             └────────────┼────────────┘
                          ▼
                   ┌─────────────┐
                   │ Publication │
                   └──────┬──────┘
                          │
                          ▼
                   ┌─────────────┐
                   │Interpretation│
                   │   Result    │
                   └─────────────┘
```

## 3.2 Dependency Directions

### Upward Dependencies (what depends on what)

```
Publication → Interpretation Result
Publication → Reporting Period
Publication → Territory
Publication → Channel

Publication Package → Publication
Publication Package → Reporting Period

Issue → Journal
Issue → Publication
Issue → Reporting Period

Release → Journal
Release → Publication
Release → Territory
Release → Reporting Period

Journal → Publication
Journal → Reporting Period
Journal → Territory
Journal → Channel
```

### Downward Dependencies (what is depended upon by what)

```
Interpretation Result → Publication
Reporting Period → Publication, Publication Package, Issue, Release, Journal
Territory → Publication, Release, Journal
Channel → Publication, Journal
Publication → Publication Package, Issue, Release, Journal
```

---

# 4. Dependency Analysis

## 4.1 Root Concepts

Concepts that have NO upstream dependencies:

| Concept | Evidence |
|---------|----------|
| Interpretation Result | GLOSSARY.md §2 |
| Reporting Period | GLOSSARY.md §2 |
| Territory | GLOSSARY.md §4 |
| Channel | GLOSSARY.md §3 |

These are FOUNDATIONAL concepts that other concepts depend upon.

## 4.2 Leaf Concepts

Concepts that have NO downstream dependencies:

| Concept | Evidence |
|---------|----------|
| Issue | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| Release | User context |

These are TERMINAL concepts that nothing else depends upon.

## 4.3 Core Concepts

Concepts that are both depended upon and depend upon others:

| Concept | Evidence |
|---------|----------|
| Publication | GLOSSARY.md §3 |
| Journal | CHARTER.md §10 |

These are CENTRAL concepts that connect the ontology.

---

# 5. Dependency Violations

## 5.1 Potential Violations

| Violation | Description | Severity |
|-----------|-------------|----------|
| Circular: Journal ↔ Issue | Journal instantiates Issue, Issue realizes Journal | LOW |
| Circular: Journal ↔ Release | Journal realizes Release, Release realizes Journal | LOW |

## 5.2 Analysis

These are NOT true circular dependencies.

They represent DIFFERENT ASPECTS of the same relationship:
- Journal is the ABSTRACT concept
- Issue/Release is the CONCRETE instantiation

The dependency is UNIDIRECTIONAL in each direction:
- Journal → Issue: Journal is instantiated as Issue
- Issue → Journal: Issue realizes Journal

---

# 6. Findings

## 6.1 Finding DEP-001

**The dependency graph has four root concepts: Interpretation Result, Reporting Period, Territory, Channel.**

These are foundational concepts with no upstream dependencies.

**Evidence:** Analysis of GLOSSARY.md §2, §3, §4.

**Confidence:** HIGH.

## 6.2 Finding DEP-002

**Publication is the central concept connecting the ontology.**

It depends on root concepts and is depended upon by container concepts.

**Evidence:** GLOSSARY.md §3.

**Confidence:** HIGH.

## 6.3 Finding DEP-003

**Journal is the highest-level concept in the ontology.**

It depends on Publication, Reporting Period, Territory, and Channel.

**Evidence:** CHARTER.md §10.

**Confidence:** HIGH.

## 6.4 Finding DEP-004

**Issue and Release are leaf concepts with no downstream dependencies.**

They are terminal concepts that represent concrete instantiations.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md, User context.

**Confidence:** HIGH.

---

# 7. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| DEP-001 | GLOSSARY.md §2, §3, §4 |
| DEP-002 | GLOSSARY.md §3 |
| DEP-003 | CHARTER.md §10 |
| DEP-004 | TELEGRAM_PUBLICATION_LIFECYCLE.md, User context |

---

**End of Dependency Graph**
