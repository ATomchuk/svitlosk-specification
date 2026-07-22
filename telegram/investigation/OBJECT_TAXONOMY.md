# OBJECT_TAXONOMY

**Document ID:** CASE001E-TAXONOMY

**Title:** Object Taxonomy

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Object Ontology Investigation

---

# Purpose

This document provides a complete taxonomy of all object categories found in the repository.

---

# Object Taxonomy

## Level 1: Primary Categories

### 1. Real-World Objects

**Definition:** Objects that exist independently of SvitloSk.

**Evidence:** GLOSSARY.md §4-5, TERRITORIAL_MODEL.md

**Subcategories:**

- Territorial Objects (Community, Territory, Settlement, Street, Address)
- Electricity Objects (Queue, Subqueue, Outage, Schedule)
- Physical Objects (Real-world locations, infrastructure)

**Characteristics:**

- Predate SvitloSk
- Exist in reality
- Official designation
- Stable

---

### 2. Domain Objects

**Definition:** Objects created by SvitloSk business logic.

**Evidence:** GLOSSARY.md §3, TJS-000 §4

**Subcategories:**

- Publication Objects (Publication, Issue, Journal)
- Collection Objects (Publication Package)
- Editorial Objects (Editorial Policy, Canonical Templates)

**Characteristics:**

- Created by system
- Business meaning
- Lifecycle management
- Identity management

---

### 3. Information Objects

**Definition:** Objects created by SvitloSk data processing.

**Evidence:** GLOSSARY.md §2, DATA_MODEL.md

**Subcategories:**

- Data Objects (Normalized Dataset, Parsed Data)
- Derived Objects (Schedule, Graphic)
- Analysis Objects (Analytics Record)

**Characteristics:**

- Derived from data
- Temporary or permanent
- Processing-dependent
- Traceable

---

### 4. Representation Objects

**Definition:** Projections of domain objects in specific contexts.

**Evidence:** Previous investigations, TJS-021 §3.1

**Subcategories:**

- Platform Representations (Telegram Message, Telegram Channel)
- Storage Representations (Repository Object, Database Record)
- Archive Representations (Historical Record, Daily Snapshot)
- Editorial Representations (Editorial Record)

**Characteristics:**

- Borrow Identity from domain objects
- Context-specific
- May have own Identifiers
- Projections, not independent objects

---

### 5. Architectural Objects

**Definition:** System building blocks.

**Evidence:** GLOSSARY.md §7, ARCHITECTURE.md

**Subcategories:**

- Components (Publication Engine, Parser, Telegram Publisher, Data Storage)
- Roles (Publisher, Interpreter)
- Interfaces (API, Telegram Bot API)

**Characteristics:**

- Implementation units
- Stable architectural identity
- NOT business concepts
- System design

---

## Level 2: Detailed Categories

### Reference Entities

**Definition:** Stable entities describing the operational environment.

**Evidence:** DATA_MODEL.md § "Reference Entities"

**Examples:** Address, Queue, Subqueue

---

### Operational Entities

**Definition:** Entities representing official operational information.

**Evidence:** DATA_MODEL.md § "Operational Entities"

**Examples:** Planned Power Outage, Emergency Power Outage, Schedule

---

### Publication Entities

**Definition:** Entities created from interpreted operational information.

**Evidence:** DATA_MODEL.md § "Publication Entities"

**Examples:** Publication, Publication Package

---

### Archive Entities

**Definition:** Entities supporting historical preservation.

**Evidence:** DATA_MODEL.md § "Archive Entities"

**Examples:** Daily Snapshot, Analytics Record

---

### Normative Documents

**Definition:** Documents defining mandatory project requirements.

**Evidence:** GLOSSARY.md §1

**Examples:** GLOSSARY.md, DATA_MODEL.md, TJS-021

---

# Taxonomy Summary

| Level 1 | Level 2 | Count | Examples |
|---------|---------|-------|----------|
| Real-World Objects | Territorial, Electricity, Physical | 10+ | Community, Territory, Address, Queue |
| Domain Objects | Publication, Collection, Editorial | 6 | Publication, Issue, Journal, Package |
| Information Objects | Data, Derived, Analysis | 5 | Dataset, Schedule, Graphic |
| Representation Objects | Platform, Storage, Archive, Editorial | 6 | Telegram Message, Repository Object |
| Architectural Objects | Components, Roles, Interfaces | 10+ | Publication Engine, Parser, Publisher |

---

# End of Object Taxonomy
