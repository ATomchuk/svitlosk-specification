# TGCORE001_HEARING

**Document ID:** CASE-TG-CORE-001

**Title:** Reverse Engineering of Telegram Publisher Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-TG-CORE-001: Reverse Engineering of Telegram Publisher.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The Telegram subsystem — what enters, what happens, what exits.

NOT Publisher design.

NOT architecture.

ONLY reverse engineering.

## 2.2 What This Case Does NOT Investigate

- Publisher design
- Facebook integration
- PWA integration
- Architecture decisions

## 2.3 Investigation Constraint

> **Reference Subsystem Principle**
>
> Before designing the generic Publisher subsystem,
> the existing Telegram subsystem must be treated as the reference implementation.
>
> Publisher MUST be reconstructed FROM Telegram,
> not designed independently.

---

# 3. Context

## 3.1 Operational Pipeline

```
Parser(s)
    ↓
JSON / TXT operational artifacts
    ↓
Telegram subsystem
    ↓
Telegram posts
```

## 3.2 Important Example

```
Queue Schedule Parser
    ↓
Queue Schedule JSON
    ↓
Graph Generator
    ↓
SVG
    ↓
PNG
    ↓
Telegram publication
```

## 3.3 Key Insight

PNG is NOT the information product.

PNG is one possible representation.

Publisher works with DATA before representation.

---

# 4. Research Tasks

## Research 1 — Inputs

Identify every input consumed by Telegram subsystem.

## Research 2 — Outputs

Identify every output produced by Telegram subsystem.

## Research 3 — Internal Operations

List every operation performed.

## Research 4 — Transformations

Classify every operation.

## Research 5 — Representation Chain

Reconstruct the complete chain for every product.

## Research 6 — Hidden Components

Determine hidden components.

## Research 7 — Responsibility Separation

Determine where responsibilities currently exist.

## Research 8 — Telegram Core

Separate Telegram-specific from generic behavior.

## Research 9 — Missing Knowledge

Determine what cannot be explained.

## Research 10 — Audit

Verify completeness.

---

# 5. Deliverables

| Document | Purpose |
|----------|---------|
| TGCORE001_HEARING.md | Case scope and research questions |
| TGCORE001_INPUT_INVENTORY.md | Input inventory |
| TGCORE001_OUTPUT_INVENTORY.md | Output inventory |
| TGCORE001_OPERATION_GRAPH.md | Operation graph |
| TGCORE001_TRANSFORMATION_MATRIX.md | Transformation matrix |
| TGCORE001_REPRESENTATION_CHAINS.md | Representation chains |
| TGCORE001_HIDDEN_COMPONENTS.md | Hidden components |
| TGCORE001_RESPONSIBILITY_MAP.md | Responsibility map |
| TGCORE001_CORE_BOUNDARY.md | Core boundary |
| TGCORE001_UNKNOWNS.md | Unknowns |
| TGCORE001_AUDIT.md | Audit certificate |

---

# 6. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
