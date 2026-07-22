# SYS001_HEARING

**Document ID:** CASE-SYS-001

**Title:** System Composition Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-SYS-001: reconstruction of the complete architecture of SvitloSk as a living system.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The COMPLETE COMPOSITION of the system — all objects, boundaries, actors, flows, and relationships.

NOT another object. THE WHOLE.

## 2.2 What This Case Does NOT Investigate

- Software implementation
- Infrastructure
- Existing specification validity
- Individual component design

## 2.3 Investigation Constraint

This investigation reconstructs what the system ACTUALLY appears to be after all previous investigations.

It must NOT propose architecture.

It must NOT redesign.

Only reconstruct.

---

# 3. Context

## 3.1 Previous Investigations

- CASE-PUB-001: Publication architecture
- CASE-JRN-001: Journal ontology
- CASE-INF-001: Information ontology
- CASE-LC-001: Information lifecycle ontology
- CASE-SVT-ONTOLOGY-001: SvitloSk ontology reconstruction

## 3.2 Architect Context

### Mission

SvitloSk is a local public information service for the Starokostiantyniv community.

### Three Independent Information Domains

#### Domain A — Queue Schedule

- Official emergency electricity limitation
- 6 queues, 12 subqueues
- Hourly schedule
- Primary information for the PWA

#### Domain B — Planned Outages

- Address-based
- Maintenance
- Settlements, streets, buildings
- Independent from Queue Schedule

#### Domain C — Emergency Outages

- Address-based
- Unexpected
- Independent from both Queue Schedule and Planned Outages

### Current Parsers

#### Parser A

- Produces Queue Schedule
- Data refreshed approximately every two hours

#### Parser B

- Produces Planned + Emergency Outages
- Data refreshed approximately every two hours

### Publisher

- Intended to become a common subsystem
- Telegram and Facebook are peers
- Publisher coordinates publication
- Adapters publish

### Telegram

- Produces multiple independent posts
- Posts grouped by territorial districts
- Tomorrow information disappears automatically
- Posts may be edited after publication

### Facebook

- Should become another publication adapter
- Same publication model
- Different representation

### PWA

- Centered around Queue Schedule
- Push notifications belong ONLY to Queue Schedule
- Does NOT belong to planned or emergency outages

---

# 4. Research Tasks

## Research 1 — System Objects

Identify ALL system-level objects.

## Research 2 — Boundaries

Identify ALL boundaries.

## Research 3 — Actors

Identify ALL actors.

## Research 4 — Flows

Reconstruct ALL flows.

## Research 5 — Lifecycle Placement

Determine where Lifecycle belongs.

## Research 6 — Component Boundaries

Determine where Journal, Publisher, PWA begin and end.

## Research 7 — Competing Models

Build at least five competing whole-system models.

## Research 8 — Hidden Couplings

Identify hidden couplings.

## Research 9 — Unnecessary Abstractions

Search for unnecessary abstractions.

## Research 10 — Missing Concepts

Search for missing concepts.

## Research 11 — System Dependency Graph

Produce System Dependency Graph.

## Research 12 — Open Questions

Produce Open Questions.

---

# 5. Deliverables

| Document | Purpose |
|----------|---------|
| SYS001_HEARING.md | Case scope and research questions |
| SYS001_OBJECTS.md | System objects |
| SYS001_BOUNDARIES.md | Boundaries |
| SYS001_ACTORS.md | Actors |
| SYS001_FLOWS.md | Flows |
| SYS001_LIFECYCLE.md | Lifecycle placement |
| SYS001_PLACEMENT.md | Journal/Publisher/PWA placement |
| SYS001_MODELS.md | Competing models |
| SYS001_COUPLINGS.md | Hidden couplings |
| SYS001_ABSTRACTIONS.md | Unnecessary abstractions |
| SYS001_MISSING.md | Missing concepts |
| SYS001_DEPENDENCY.md | System dependency graph |
| SYS001_QUESTIONS.md | Open questions |
| SYS001_CERTIFICATE.md | Investigation certificate |

---

# 6. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
