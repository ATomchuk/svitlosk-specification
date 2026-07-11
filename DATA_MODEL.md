# DATA_MODEL

Status: Stable (Стабільний)

Document ID: DOC-008

Document Class: Normative

Author: SvitloSk Project

---

# Purpose

This document defines the canonical logical data model of the SvitloSk Project.

It establishes the logical entities processed by the system, their relationships, lifecycle and integrity requirements.

This document defines logical data only.

Implementation details are intentionally excluded.

---

# Why this document matters

A stable logical data model provides consistency across the entire project.

It enables independent evolution of software components while preserving compatibility, reproducibility and architectural integrity.

All SSP specifications SHALL build upon the logical entities defined by this document.

---

# Relationship with Core Documents

This document defines the logical representation of information processed by SvitloSk.

| Document | Responsibility |
|----------|----------------|
| CHARTER.md | Defines the mission of the project |
| PROJECT_PRINCIPLES.md | Defines engineering principles |
| GLOSSARY.md | Defines canonical terminology |
| TERRITORIAL_MODEL.md | Defines territorial entities |
| ARCHITECTURE.md | Defines system organization |
| DATA_MODEL.md | Defines logical data representation |

---

# Scope

This specification defines:

- logical entities;
- logical relationships;
- data lifecycle;
- integrity requirements;
- logical categories;
- data governance principles.

Administrative geography is intentionally excluded.

Territorial relationships are defined exclusively in TERRITORIAL_MODEL.md.

---

# Data Governance

The logical data model is the canonical representation of information used throughout the SvitloSk Project.

All SSP specifications SHALL reference the entities defined by this document.

No specification SHALL redefine logical entities independently.

Changes to the logical data model SHALL be introduced through the repository governance process.

---

# Source of Truth

Official Open Data SHALL remain the only operational source of truth.

SvitloSk SHALL NOT:

- modify official information;
- create operational facts;
- predict future events.

The system MAY enrich operational information with technical metadata required for processing, traceability and archival purposes.

---

# Logical Entity Groups

The logical model consists of the following categories:

## Reference Entities

Stable entities describing the operational environment.

Examples include:

- Address
- Queue
- Subqueue

---

## Operational Entities

Entities representing official operational information.

Examples include:

- Planned Power Outage
- Emergency Power Outage
- Schedule

---

## Publication Entities

Entities created from interpreted operational information.

Examples include:

- Publication
- Publication Package

---

## Archive Entities

Entities supporting historical preservation and analytical processing.

Examples include:

- Daily Snapshot
- Analytics Record

---

# Core Logical Entities

## Address

Logical reference to a physical location served by the project.

Territorial hierarchy SHALL be defined exclusively by TERRITORIAL_MODEL.md.

---

## Queue

Logical representation of an official electricity distribution queue.

Operational values are determined by the official Data Source.

---

## Subqueue

Logical subdivision of a Queue.

Supported operational values are defined by the current operational configuration.

---

## Planned Power Outage

Logical representation of an officially announced scheduled interruption of electricity supply.

A Planned Power Outage SHALL reference:

- operational time interval;
- affected addresses;
- official source.

---

## Emergency Power Outage

Logical representation of an officially announced unscheduled interruption of electricity supply.

An Emergency Power Outage SHALL reference:

- publication timestamp;
- affected addresses;
- official source.

---

## Schedule

Logical representation of electricity availability for one operational period.

Schedules SHALL reference one Subqueue.

---

## Publication

Logical representation of interpreted information prepared for public distribution.

Each Publication SHALL be traceable to normalized operational data.

---

## Publication Package

Logical collection of Publications generated during one reporting period.

---

## Daily Snapshot

Immutable representation of normalized operational information for one reporting day.

Archived Daily Snapshots SHALL become read-only.

---

## Analytics Record

Logical representation of statistical information derived from historical datasets.

Analytics SHALL NEVER modify operational information.

---

# Data Categories

## Operational Data

Current information obtained from official sources.

---

## Historical Data

Archived operational information preserved by SvitloSk.

---

## Analytical Data

Information derived exclusively from Historical Data.

Analytical Data SHALL NOT replace Operational Data.

---

## Configuration Data

Technical information governing system behaviour.

Configuration Data SHALL NOT contain operational information.

---

## Reference Data

Stable information describing entities used by the logical model.

Reference Data changes infrequently.

---

# Data Lifecycle

Every operational dataset SHALL follow the canonical lifecycle.

```
Collected

    │

    ▼

Validated

    │

    ▼

Normalized

    │

    ▼

Interpreted

    │

    ▼

Published

    │

    ▼

Archived
```

Archived datasets SHALL remain immutable.

---

# Logical Relationships

| Entity | Logical Relationship |
|---------|----------------------|
| Address | Referenced by Operational Entities |
| Queue | Groups Subqueues |
| Subqueue | Used by Schedule |
| Schedule | References Operational Data |
| Publication | Generated from normalized operational data |
| Publication Package | Collection of Publications |
| Daily Snapshot | Archive representation of operational data |
| Analytics Record | Derived from Historical Data |

---

# Data Integrity

Every logical entity SHALL be:

- uniquely identifiable;
- traceable;
- reproducible;
- timestamped where applicable;
- linked to its official source.

Logical integrity SHALL be preserved throughout the entire processing lifecycle.

---

# Consistency Rules

Every Publication SHALL originate from normalized operational data.

Historical datasets SHALL preserve the original operational state existing at publication time.

Archived information SHALL remain reproducible.

Logical entities SHALL remain internally consistent across all system components.

---

# Model Evolution

The logical data model is designed for long-term stability.

New logical entities MAY be introduced through the RFC process.

Existing entities SHOULD remain backward compatible whenever practical.

Breaking changes SHALL require explicit architectural approval.

---

# Repository Rule

Normative documents SHALL reference logical entities defined by this specification.

Territorial hierarchy SHALL always be referenced from TERRITORIAL_MODEL.md.

Logical entities SHALL NOT be redefined elsewhere in the repository.

---

# References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- GLOSSARY.md
- TERRITORIAL_MODEL.md
- ARCHITECTURE.md

## Referenced by

- All SSP specifications

---

**End of Document**