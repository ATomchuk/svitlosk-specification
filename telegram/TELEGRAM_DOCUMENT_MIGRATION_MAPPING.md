# Telegram Document Migration Mapping

**Date:** 2026-07-13
**Scope:** Current State → Target State mapping
**Status:** MAPPING COMPLETE

---

# Purpose

This document provides a complete mapping from the current document state to the target document state, without modifying any files.

---

# Current State → Target State Mapping

## TJS Specifications

| Current ID | Current Title | Current File | Target ID | Target Title | Target File | Action |
|-----------|--------------|-------------|-----------|-------------|-------------|--------|
| TJS-001 | Journal Concept | TJS-001-Journal-Concept.md | TJS-001 | Journal Concept | TJS-001-Journal-Concept.md | RETAIN |
| TJS-002 | Publication Lifecycle | TJS-002-Publication-Lifecycle.md | TJS-005 | Publication Lifecycle | TJS-005-Publication-Lifecycle.md | MERGE (into TJS-005) |
| TJS-003 | Post Structure | TJS-003-Post-Structure.md | TJS-005 | Message Templates | — | ABSORB (into TJS-005) |
| TJS-004 | Editorial Policy | TJS-004-Editorial-Policy.md | TJS-004 | Editorial Policy | TJS-004-Editorial-Policy.md | RETAIN |
| TJS-005 | Message Templates | TJS-005-Message-Templates.md | TJS-005 | Message Templates | TJS-005-Message-Templates.md | RETAIN |
| TJS-006 | Rendering Rules | TJS-006-Rendering-Rules.md | TJS-006 | Rendering Rules | TJS-006-Rendering-Rules.md | RETAIN |
| TJS-007 | Publication Lifecycle | TJS-007-Publication-Lifecycle.md | TJS-005 | Publication Lifecycle | TJS-005-Publication-Lifecycle.md | MERGE (into TJS-005) |
| TJS-008 | Publication Lifecycle | TJS-008-Publication-Lifecycle.md | TJS-005 | Publication Lifecycle | TJS-005-Publication-Lifecycle.md | MERGE (into TJS-005) |

**Note:** The Architecture Decision uses target-state IDs that don't match current-state IDs. The mapping above uses CURRENT-STATE IDs.

---

## Foundational Documents

| Current ID | Current Title | Current File | Target ID | Target Title | Target File | Action |
|-----------|--------------|-------------|-----------|-------------|-------------|--------|
| TJS-000 | Semantic Model | TELEGRAM_SEMANTIC_MODEL.md | TJS-000 | Semantic Model | TELEGRAM_SEMANTIC_MODEL.md | RETAIN |
| TJS-000A | Glossary | TELEGRAM_GLOSSARY.md | TJS-000A | Glossary | TELEGRAM_GLOSSARY.md | RETAIN |
| TJS-000B | Alignment Process | TELEGRAM_SPECIFICATION_ALIGNMENT_PROCESS.md | TJS-000B | Alignment Process | TELEGRAM_SPECIFICATION_ALIGNMENT_PROCESS.md | RETAIN |
| TJS-000C | Alignment Pipeline | TELEGRAM_ALIGNMENT_PIPELINE.md | TJS-000C | Alignment Pipeline | TELEGRAM_ALIGNMENT_PIPELINE.md | RETAIN |
| TJS-000D | Alignment Governance | TELEGRAM_ALIGNMENT_GOVERNANCE.md | TJS-000D | Alignment Governance | TELEGRAM_ALIGNMENT_GOVERNANCE.md | RETAIN |
| TJS-TEMPLATE | Alignment Template | TJS_ALIGNMENT_TEMPLATE.md | TJS-TEMPLATE | Alignment Template | TJS_ALIGNMENT_TEMPLATE.md | RETAIN |

---

## Architecture Decision

| Current ID | Current Title | Current File | Target ID | Target Title | Target File | Action |
|-----------|--------------|-------------|-----------|-------------|-------------|--------|
| — | Architecture Decision | TELEGRAM_ARCHITECTURE_DECISION.md | — | Architecture Decision | TELEGRAM_ARCHITECTURE_DECISION.md | RETAIN (update content) |

---

## New Documents (Target State Only)

| Target ID | Target Title | Target File | Action |
|-----------|-------------|-------------|--------|
| TJS-010 | Channel Management | TJS-010-Channel-Management.md | CREATE |
| TJS-011 | Graphic Rendering | TJS-011-Graphic-Rendering.md | CREATE |

---

# Mapping Summary

| Action | Count | Details |
|--------|-------|---------|
| RETAIN | 10 | TJS-001, TJS-004, TJS-005, TJS-006, TJS-000, TJS-000A-D, TJS-TEMPLATE, Architecture Decision |
| MERGE | 3 | TJS-002 + TJS-007 + TJS-008 → TJS-005 |
| ABSORB | 1 | TJS-003 → TJS-005 |
| CREATE | 2 | TJS-010 (Channel Management), TJS-011 (Graphic Rendering) |
| **Total** | **16** | |

---

# Identity Mapping Summary

| Current ID | Target ID | Current Title | Target Title | Action |
|-----------|-----------|--------------|-------------|--------|
| TJS-001 | TJS-001 | Journal Concept | Journal Concept | RETAIN |
| TJS-002 | TJS-005 | Publication Lifecycle | Publication Lifecycle | MERGE |
| TJS-003 | TJS-005 | Post Structure | Message Templates | ABSORB |
| TJS-004 | TJS-004 | Editorial Policy | Editorial Policy | RETAIN |
| TJS-005 | TJS-005 | Message Templates | Message Templates | RETAIN |
| TJS-006 | TJS-006 | Rendering Rules | Rendering Rules | RETAIN |
| TJS-007 | TJS-005 | Publication Lifecycle | Publication Lifecycle | MERGE |
| TJS-008 | TJS-005 | Publication Lifecycle | Publication Lifecycle | MERGE |
| — | TJS-010 | — | Channel Management | CREATE |
| — | TJS-011 | — | Graphic Rendering | CREATE |

---

**End of Migration Mapping**

**Mapper:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
