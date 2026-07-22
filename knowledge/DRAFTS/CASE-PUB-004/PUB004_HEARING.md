# PUB004_HEARING

**Document ID:** CASE-PUB-004

**Title:** Publisher Decision Model Investigation Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-PUB-004: Publisher Decision Model Investigation.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The DECISION MODEL of the Publisher.

NOT implementation.

NOT architecture.

ONLY decision making.

## 2.2 What This Case Does NOT Investigate

- Implementation details
- Architecture design
- Specification modification
- ADR creation

## 2.3 Investigation Constraint

The goal is to discover: Who decides WHAT should happen.

NOT who executes it.

---

# 3. Context

## 3.1 Previous Investigations

- CASE-PUB-001: Publication architecture
- CASE-PUB-002: Telegram Publisher reverse engineering
- CASE-PUB-003: Semantic normalization
- CASE-JRN-001: Journal ontology
- CASE-INF-001: Information ontology
- CASE-LC-001: Information lifecycle ontology
- CASE-SYS-001: System composition
- CASE-SRC-001: Source audit
- CASE-INFPROD-001: Information product ontology
- CASE-TG-CORE-001: Telegram core reverse engineering

## 3.2 Established Knowledge

Previous investigations established:

- Publisher responsibilities
- Information Products
- Lifecycle Pattern
- Telegram Core
- Semantic Vocabulary

## 3.3 Current Focus

Now investigate ONLY decision making.

---

# 4. Research Questions

## Research 1 — Events

Which events can occur inside Publisher?

## Research 2 — Decision Makers

For every event, who decides?

## Research 3 — Actions

For every decision, what action follows?

## Research 4 — Business Decisions

Are there decisions that are PURELY BUSINESS decisions?

## Research 5 — Decision Dependencies

Which decisions depend on TIME, INFORMATION, or CHANNEL?

## Research 6 — Decision Graph

Construct decision graph.

## Research 7 — Competing Models

Construct competing models.

## Research 8 — Hidden Assumptions

Identify hidden assumptions.

## Research 9 — Missing Concepts

Identify missing concepts.

## Research 10 — Audit

Produce audit.

---

# 5. Deliverables

| Document | Purpose |
|----------|---------|
| PUB004_HEARING.md | Case scope and research questions |
| PUB004_EVENTS.md | Event inventory |
| PUB004_DECISION_MAKERS.md | Decision makers |
| PUB004_ACTIONS.md | Action inventory |
| PUB004_BUSINESS_DECISIONS.md | Business decisions |
| PUB004_DECISION_DEPENDENCIES.md | Decision dependencies |
| PUB004_DECISION_GRAPH.md | Decision graph |
| PUB004_MODELS.md | Competing models |
| PUB004_ASSUMPTIONS.md | Hidden assumptions |
| PUB004_MISSING.md | Missing concepts |
| PUB004_AUDIT.md | Audit certificate |

---

# 6. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
