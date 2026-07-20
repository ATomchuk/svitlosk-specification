# ENGINE_VS_COORDINATOR_COMPARISON

**Document ID:** SEM-002

**Title:** Engine vs Coordinator Comparison

**Document Class:** Comparison

**Status:** COMPLETE

**Author:** Independent Architect

---

# 1. Publication Engine Behaviour Analysis

## Inputs
- Normalized Dataset (from Parser)
- Schedules (from Schedule Generator)
- Graphics (from Graphic Generator)

## Outputs
- Publication Package (to Telegram Publisher)

## Owned Responsibilities
- Publication generation
- Distribution
- Ownership model
- Daily cycle
- Publication windows

## State Management
- Maintains publication state (Generated → Published → Updated → Archived)
- Manages daily publication cycle
- Controls publication windows

## Deterministic Behaviour
- Same normalized dataset ALWAYS produces identical Publication Package
- Deterministic output is a core design principle
- Canonical Equality guarantee applies

## Control Flow
- The Engine decides WHEN to generate
- The Engine decides HOW to assemble
- The Engine decides WHEN to publish
- The Engine decides WHEN to update
- The Engine decides WHEN to archive

---

# 2. Engine vs Coordinator Assessment

| Criterion | Publication Engine Behaviour | Engine? | Coordinator? |
|-----------|---------------------------|---------|-------------|
| Transforms input to output? | YES — data → package | YES | NO |
| Self-contained lifecycle? | YES — owns daily cycle | YES | NO |
| Deterministic output? | YES — Canonical Equality | YES | NO |
| Manages state? | YES — publication states | YES | PARTIAL |
| Assembles from producers? | YES — receives from 3 producers | PARTIAL | YES |
| Controls execution? | YES — decides timing | YES | YES |
| Independent operation? | YES — runs autonomously | YES | PARTIAL |

---

# 3. Comparison Verdict

Publication Engine is **primarily an Engine** that also performs coordination. It is NOT merely a Coordinator.

The key distinction: a Coordinator assembles but does NOT transform. Publication Engine both assembles AND transforms — it takes raw data, schedules, and graphics and produces a deterministic Publication Package. This transformation is the Engine's primary responsibility.

---

**End of Engine vs Coordinator Comparison**

**Auditor:** Independent Architect
**Date:** 2026-07-13
**Status:** COMPLETE
