# SRC001_SOURCE_INVENTORY

**Document ID:** CASE-SRC-001-SI

**Title:** Source Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every source that may contain Publisher knowledge.

---

# 2. Source Inventory

## 2.1 Current Specifications

### SPEC-001: GLOSSARY.md

**Location:** Root directory

**Publisher Knowledge:**

- Publisher definition (§3)
- Publication Engine definition (§3)
- Publisher Role definition (§3)
- Publication definition (§3)
- Publication Pipeline definition (§3)
- Rendering definition (§3)
- Distribution definition (§3)
- Publication Lifecycle definition (§3)

---

### SPEC-002: ARCHITECTURE.md

**Location:** Root directory

**Publisher Knowledge:**

- Publication Model Layer (§Layer 6)
- Component Model (§Component Model)
- Logical Processing Flow (§Logical Processing Flow)

---

### SPEC-003: DATA_MODEL.md

**Location:** Root directory

**Publisher Knowledge:**

- Publication entity (§Publication)
- Publication Package entity (§Publication Package)
- Data Lifecycle (§Data Lifecycle)

---

### SPEC-004: TELEGRAM_PUBLISHING_CANONICAL_MODEL.md

**Location:** telegram/specs/

**Publisher Knowledge:**

- Publishing Architecture (§3)
- Component Responsibilities (§4)
- Component Interactions (§5)
- Publishing Principles (§6)
- Publishing Constraints (§7)
- Publishing Boundaries (§8)
- Publishing Lifecycle Overview (§9)
- Publishing Data Flow (§10)

---

### SPEC-005: TELEGRAM_PUBLICATION_LIFECYCLE.md

**Location:** telegram/specs/

**Publisher Knowledge:**

- Lifecycle States (§4)
- Lifecycle Transitions (§5)
- Publication Evolution (§6)
- Publication Maintenance (§7)
- Issue Lifecycle (§8)

---

### SPEC-006: TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md

**Location:** telegram/specs/

**Publisher Knowledge:**

- Editorial Mission (§3)
- Editorial Principles (§4)
- Editorial Behaviour (§5)
- Editorial Constraints (§6)

---

### SPEC-007: TELEGRAM_SEMANTIC_MODEL.md

**Location:** telegram/foundation/

**Publisher Knowledge:**

- Semantic definitions
- Terminology

---

### SPEC-008: TELEGRAM_ARCHITECTURE_DECISION.md

**Location:** telegram/foundation/

**Publisher Knowledge:**

- Architecture decisions
- Component boundaries

---

## 2.2 ADRs

### ADR-001: Component vs Role

**Location:** adr/

**Publisher Knowledge:**

- Publication Engine = Component
- Publisher = Role
- Relationship between Component and Role

---

## 2.3 Research Documents

### RESEARCH-001: CASE-PUB-001

**Location:** knowledge/DRAFTS/CASE-PUB-001/

**Publisher Knowledge:**

- Journal Release concept
- Publishing Kernel concept
- Competing models
- Contradictions

---

### RESEARCH-002: CASE-PUB-002

**Location:** knowledge/DRAFTS/CASE-PUB-002/

**Publisher Knowledge:**

- Telegram operations inventory
- Responsibility extraction
- Publisher skeleton v0
- Telegram remainder
- Candidate interfaces

---

### RESEARCH-003: CASE-JRN-001

**Location:** knowledge/DRAFTS/CASE-JRN-001/

**Publisher Knowledge:**

- Journal ontology
- Journal Edition concept
- Publication as atomic unit

---

### RESEARCH-004: CASE-INF-001

**Location:** knowledge/DRAFTS/CASE-INF-001/

**Publisher Knowledge:**

- Information ontology
- Information/Knowledge/Data/Representation separation
- Information lifecycle

---

### RESEARCH-005: CASE-LC-001

**Location:** knowledge/DRAFTS/CASE-LC-001/

**Publisher Knowledge:**

- Lifecycle as pattern
- Lifecycle operations
- Update behavior
- Temporal behavior
- Publisher thickness

---

### RESEARCH-006: CASE-SYS-001

**Location:** knowledge/DRAFTS/CASE-SYS-001/

**Publisher Knowledge:**

- System objects
- System boundaries
- System flows
- Component placement
- Competing models

---

## 2.4 Archived Materials

### ARCHIVE-001: PROJECT_PUBLISHING_CORE_MODEL.md

**Location:** archive/knowledge/

**Publisher Knowledge:**

- Historical publishing model
- Core publishing concepts

---

### ARCHIVE-002: PROJECT_PUBLISHING_KNOWLEDGE_REGISTER.md

**Location:** archive/knowledge/

**Publisher Knowledge:**

- Historical knowledge register
- Publishing knowledge inventory

---

### ARCHIVE-003: PROJECT_BASELINE_v1.0.md

**Location:** archive/baselines/

**Publisher Knowledge:**

- Historical baseline
- Early architectural decisions

---

### ARCHIVE-004: PROJECT_BASELINE_v2.0.md

**Location:** archive/baselines/

**Publisher Knowledge:**

- Historical baseline v2
- Evolved architectural decisions

---

### ARCHIVE-005: PROJECT_BASELINE_v3.0.md

**Location:** archive/baselines/

**Publisher Knowledge:**

- Historical baseline v3
- Latest archived baseline

---

## 2.5 Operational Artifacts

### OPS-001: today.txt (External)

**Location:** OutagesSk repository

**Publisher Knowledge:**

- Publisher input format
- Parser output format

**Note:** This file describes Publisher INPUTS, not Publisher itself.

---

## 2.6 Telegram Implementation

### IMPL-001: Telegram Bot Code

**Location:** External (OutagesSk repository)

**Publisher Knowledge:**

- Practical publishing operations
- Channel-specific logic
- Message formatting
- Lifecycle mechanics

**Note:** Contains largest amount of practical Publisher knowledge.

---

# 3. Source Inventory Summary

| Category | Count | Examples |
|----------|-------|----------|
| Current Specifications | 8 | GLOSSARY, ARCHITECTURE, TELEGRAM specs |
| ADRs | 1 | ADR-001 Component vs Role |
| Research Documents | 6 | CASE-PUB-001 through CASE-SYS-001 |
| Archived Materials | 5 | Historical baselines, knowledge registers |
| Operational Artifacts | 1 | today.txt |
| Telegram Implementation | 1 | Telegram Bot Code |
| **Total** | **22** | |

---

# 4. Findings

## 4.1 Finding SI-001

**There are 22 potential sources of Publisher knowledge.**

Across 6 categories.

**Evidence:** Analysis of repository structure.

**Confidence:** HIGH.

## 4.2 Finding SI-002

**Current specifications contain the most formal Publisher knowledge.**

8 specifications with Publisher-related content.

**Evidence:** Analysis of specification content.

**Confidence:** HIGH.

## 4.3 Finding SI-003

**Telegram implementation contains the most practical Publisher knowledge.**

But it is EXTERNAL to the current repository.

**Evidence:** Architect confirmation.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| SI-001 | Analysis of repository structure |
| SI-002 | Analysis of specification content |
| SI-003 | Architect confirmation |

---

**End of Source Inventory**
