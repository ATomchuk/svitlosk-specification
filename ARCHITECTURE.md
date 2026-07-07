# ARCHITECTURE

Project Specification

---

Document ID: DOC-006

Document: ARCHITECTURE.md

Project: SvitloSk

Status: Draft (Чернетка)

Class: Normative

Maintainer: SvitloSk Project

---

# Purpose

This document defines the official high-level architecture of the SvitloSk project.

It establishes the architectural boundaries of the system, defines the major system components, their responsibilities, interactions, and the principles governing future architectural evolution.

This document serves as the primary architectural reference for all future specifications.

---

# Why this document exists

Software implementation changes over time.

Architecture should remain stable.

Without a formally defined architecture:

- component boundaries become unclear;
- responsibilities overlap;
- implementation diverges from project goals;
- long-term maintenance becomes increasingly difficult.

ARCHITECTURE.md defines the stable architectural foundation of the SvitloSk project independently from any programming language or implementation technology.

---

# Scope

This document specifies:

- overall system architecture;
- architectural layers;
- major system components;
- component responsibilities;
- data flow;
- architectural constraints.

Implementation details are intentionally excluded.

---

# Architectural Principles

The architecture of SvitloSk SHALL comply with the following principles.

## Separation of Responsibilities

Each component SHALL have a single clearly defined responsibility.

---

## Open Data First

Every published result SHALL originate from official publicly available data.

---

## Interpretation without Modification

The system SHALL interpret official information.

The system SHALL NOT modify official facts.

The system SHALL NOT generate new facts.

The system SHALL NOT predict future events.

---

## Automation First

Every repetitive operation SHOULD be automated whenever technically feasible.

---

## Source of Truth

Official publicly available information SHALL always remain the single source of truth.

---

## Stateless Processing

Whenever possible, processing components SHOULD remain stateless.

Persistent storage SHALL be delegated to dedicated archive components.

---

## Reproducibility

Identical input data SHALL always produce identical results.

---

# High-Level Architecture

```
                    Official Open Data
                            │
                            ▼
                   Data Acquisition Layer
                            │
                            ▼
                      Parsing Engine
                            │
                            ▼
                 Interpretation Engine
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
   Archive Engine   Publication Engine   Notification Engine
          │                 │                 │
          ▼                 ▼                 ▼
 Historical Archive   Telegram / PWA     Push Notifications
```

---

# Architectural Layers

## Layer 1 — Data Sources

Provides official publicly available information.

Examples include:

- planned outage schedules;
- emergency outage announcements;
- official service messages.

---

## Layer 2 — Data Acquisition

Responsible for obtaining official data.

Responsibilities:

- downloading;
- integrity verification;
- scheduling.

---

## Layer 3 — Parsing

Transforms raw official data into normalized internal structures.

Responsibilities:

- parsing;
- validation;
- normalization.

---

## Layer 4 — Interpretation

Core component of the project.

Responsibilities:

- interpret official information;
- detect meaningful events;
- classify outages;
- prepare structured publication objects.

This layer SHALL NOT modify official facts.

---

## Layer 5 — Publication

Responsible for delivering information to residents.

Publication channels may include:

- Telegram;
- PWA application;
- Web interface;
- Tomorrow Schedule graphics;
- Public Information Journal.

---

## Layer 6 — Archive

Responsible for preserving historical information.

Responsibilities:

- long-term storage;
- historical lookup;
- statistics;
- auditability.

---

## Layer 7 — Notification

Responsible for delivering notifications.

Examples:

- Push notifications;
- Telegram alerts;
- critical outage notifications.

---

# Core Components

The SvitloSk architecture consists of the following logical components.

- Scheduler
- Data Acquisition
- Parser
- Interpreter
- Archive
- Publication Engine
- Graph Generator
- Notification Engine
- Configuration
- Monitoring

Each component SHALL be specified by its own specification document.

---

# Data Flow

The logical processing flow SHALL follow the sequence below.

```
Official Data

↓

Download

↓

Validation

↓

Parsing

↓

Normalization

↓

Interpretation

↓

Publication Object

↓

Archive

↓

Publication

↓

Notification
```

---

# Architectural Constraints

The architecture SHALL satisfy the following constraints.

- Components SHOULD remain loosely coupled.
- Components SHOULD communicate through clearly defined interfaces.
- Internal implementation SHALL NOT affect external specifications.
- No component SHALL directly modify official source data.
- All publications SHALL be reproducible from archived data.

---

# Non-goals

The architecture explicitly excludes the following responsibilities.

SvitloSk SHALL NOT:

- predict outages;
- replace official information sources;
- dispatch repair crews;
- issue operational commands;
- generate unofficial information.

---

# Future Extensions

The architecture is designed to allow future expansion without modifying the existing architectural principles.

Possible future extensions include:

- additional publication channels;
- analytical dashboards;
- open API;
- multi-community deployments;
- statistical reporting.

Future extensions SHALL comply with this specification.

---

# References

Depends on:

- CHARTER.md
- PROJECT_PRINCIPLES.md
- DOCUMENT_INDEX.md
- GLOSSARY.md

Referenced by:

- DATA_MODEL.md
- PARSER_SPECIFICATION.md
- GRAPH_SPECIFICATION.md
- TELEGRAM_PUBLICATION.md
- DESIGN_SYSTEM.md
- ENGINEERING.md

# Core System Principles

The SvitloSk architecture is based on a strict separation between data acquisition, interpretation, storage and publication.

Every subsystem has a single responsibility.

The system SHALL NOT contain components that perform unrelated functions.

---

## Principle 1 — Single Source of Truth

Every published message SHALL originate from officially published open data.

The system SHALL NOT generate information from assumptions or unofficial sources.

---

## Principle 2 — Interpretation

The system interprets official data.

Interpretation means transforming official technical information into a format understandable by residents of the Starokostiantyniv Community.

Interpretation MAY include:

- restructuring information;
- grouping events;
- calculating durations;
- generating timelines;
- generating visual schedules;
- preparing publication layouts.

Interpretation SHALL NEVER modify factual information.

---

## Principle 3 — Automation

All routine operations SHOULD be automated whenever possible.

Automation includes:

- downloading official data;
- validation;
- interpretation;
- publication generation;
- archive creation;
- notification preparation.

Human participation SHOULD be required only for exceptional situations.

---

## Principle 4 — Deterministic Processing

Identical input SHALL always produce identical output.

The system SHALL avoid non-deterministic behaviour.

---

## Principle 5 — Traceability

Every published artifact SHALL be traceable to:

- source data;
- processing time;
- software version;
- publication time.

Traceability SHALL be preserved for archived publications.

---

## Principle 6 — Independence of Components

Each architectural component SHALL have a clearly defined responsibility.

Components SHOULD communicate only through documented interfaces.

Internal implementation SHALL NOT affect external behaviour.

---

## Principle 7 — Extensibility

New publication channels, parsers or visualization modules SHALL be addable without redesigning the entire architecture.

Future expansion SHALL preserve backward compatibility whenever practical.
