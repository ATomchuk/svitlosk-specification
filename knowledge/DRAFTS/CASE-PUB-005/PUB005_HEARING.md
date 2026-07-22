# PUB005_HEARING

**Document ID:** CASE-PUB-005

**Title:** Publisher Rules Reconstruction Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-PUB-005: Publisher Rules Reconstruction.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The REAL BUSINESS RULES that already exist inside the current Telegram Publisher implementation.

NOT design.

NOT improvement.

ONLY reconstruction.

## 2.2 What This Case Does NOT Investigate

- Architecture design
- Implementation design
- Specification modification
- ADR creation

## 2.3 Investigation Constraint

Publisher remains the reference implementation.

We are extracting the canonical semantic model.

---

# 3. Context

## 3.1 Previous Investigations

- CASE-PUB-001: Publication architecture
- CASE-PUB-002: Telegram Publisher reverse engineering
- CASE-PUB-003: Semantic normalization
- CASE-PUB-004: Decision model investigation
- CASE-TG-CORE-001: Telegram core reverse engineering

## 3.2 Established Knowledge

Previous investigations established:

- Publisher is NOT the decision maker
- Publisher EXECUTES decisions
- Lifecycle is a pattern
- Telegram implementation contains largest amount of real project knowledge
- Telegram Publisher is the primary source of truth

---

# 4. Research Tasks

## Research 1 — Rule Inventory

List every business rule that currently exists.

## Research 2 — Rule Classification

Separate rules into categories.

## Research 3 — Rule Triggers

Identify trigger, condition, executor, affected object, result.

## Research 4 — Rule Ownership

Determine who owns each rule.

## Research 5 — Rule Dependencies

Build dependency graph.

## Research 6 — Rule Stability

Determine stable, derived, temporary, historical, implementation rules.

## Research 7 — Hidden Rules

Look for undocumented rules.

## Research 8 — Rule Language

Extract every verb used for publisher behavior.

## Research 9 — Candidate Canonical Rules

Identify stable rules for specification language.

## Research 10 — Missing Rules

Identify gaps.

---

# 5. Deliverables

| Document | Purpose |
|----------|---------|
| PUB005_HEARING.md | Case scope and research questions |
| PUB005_RULE_INVENTORY.md | Rule inventory |
| PUB005_CLASSIFICATION.md | Rule classification |
| PUB005_TRIGGERS.md | Rule triggers |
| PUB005_OWNERSHIP.md | Rule ownership |
| PUB005_DEPENDENCIES.md | Rule dependencies |
| PUB005_STABILITY.md | Rule stability |
| PUB005_HIDDEN_RULES.md | Hidden rules |
| PUB005_LANGUAGE.md | Rule language |
| PUB005_CANONICAL_RULES.md | Candidate canonical rules |
| PUB005_MISSING_RULES.md | Missing rules |
| PUB005_AUDIT.md | Audit certificate |

---

# 6. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
