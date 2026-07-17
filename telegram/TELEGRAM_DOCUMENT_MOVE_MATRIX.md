# Telegram Document Move Matrix

**Date:** 2026-07-13
**Scope:** Current Location → Target Location for every document
**Status:** MATRIX COMPLETE

---

# Purpose

This document maps every Telegram document from its current location to its target location, including migration phase, dependencies, and risk level.

---

# Move Matrix

## Foundation Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TELEGRAM_SEMANTIC_MODEL.md | telegram/ | telegram/Foundation/ | Phase 3 | None | LOW |
| TELEGRAM_GLOSSARY.md | telegram/ | telegram/Foundation/ | Phase 3 | None | LOW |
| TELEGRAM_SPECIFICATION_ALIGNMENT_PROCESS.md | telegram/ | telegram/Processes/ | Phase 8 | None | LOW |
| TELEGRAM_ALIGNMENT_PIPELINE.md | telegram/ | telegram/Processes/ | Phase 8 | None | LOW |
| TELEGRAM_ALIGNMENT_GOVERNANCE.md | telegram/ | telegram/Processes/ | Phase 8 | None | LOW |
| TJS_ALIGNMENT_TEMPLATE.md | telegram/ | telegram/Specifications/ | Phase 3 | None | LOW |

---

## Architecture Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TELEGRAM_ARCHITECTURE_DECISION.md | telegram/ | telegram/Architecture/ | Phase 4 | Foundation | LOW |
| TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | telegram/ | telegram/Architecture/ | Phase 4 | Foundation | LOW |
| TELEGRAM_EDITORIAL_SYSTEM_BLUEPRINT.md | telegram/ | telegram/Architecture/ | Phase 4 | Foundation | LOW |

---

## Publishing Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TELEGRAM_PUBLISHING_HARVEST.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_COMPONENT_MATRIX.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_INTERACTION_MATRIX.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_RESPONSIBILITY_MATRIX.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_DUPLICATION.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_PRINCIPLES.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_BOUNDARY_ANALYSIS.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_SECTION_MATRIX.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_TRACEABILITY_MATRIX.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |
| TELEGRAM_PUBLISHING_ARCHITECTURAL_GUARANTEES.md | telegram/ | telegram/Publishing/ | Phase 5 | Architecture | LOW |

---

## Editorial Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TELEGRAM_EDITORIAL_PRINCIPLES.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_DECISIONS.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_HARVEST.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_BOUNDARIES.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_RESPONSIBILITY_MATRIX.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_PRINCIPLE_DEFINITIONS.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_PRINCIPLE_CERTIFICATION.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_PRINCIPLE_BOUNDARIES.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_PRINCIPLE_RELATIONSHIPS.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |
| TELEGRAM_EDITORIAL_SYSTEM_BLUEPRINT.md | telegram/ | telegram/Editorial/ | Phase 6 | Architecture | LOW |

---

## Lifecycle Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TELEGRAM_LIFECYCLE_SEMANTIC_AUDIT.md | telegram/ | telegram/Lifecycle/ | Phase 7 | Architecture | LOW |

---

## Legacy Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TJS-001-Journal-Concept.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |
| TJS-002-Publication-Lifecycle.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |
| TJS-003-Post-Structure.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |
| TJS-004-Editorial-Policy.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |
| TJS-005-Message-Templates.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |
| TJS-006-Rendering-Rules.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |
| TJS-007-Publication-Lifecycle.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |
| TJS-008-Publication-Lifecycle.md | telegram/ | telegram/Legacy/ | Phase 7 | None | LOW |

---

## Process Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TELEGRAM_MIGRATION_*.md | telegram/ | telegram/Processes/ | Phase 8 | Architecture | LOW |
| TELEGRAM_ALIGNMENT_*.md | telegram/ | telegram/Processes/ | Phase 8 | Architecture | LOW |

---

## Reference Documents

| Document | Current Location | Target Location | Phase | Dependencies | Risk |
|----------|-----------------|-----------------|-------|-------------|------|
| TELEGRAM_CANONICAL_SEMANTIC_MODEL.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_CANONICAL_TERMINOLOGY.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_DERIVED_TERMS.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_FORBIDDEN_TERMS.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_FORBIDDEN_TERMINOLOGY.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_PLATFORM_TERMS.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_ARCHITECTURAL_TERMS.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_GLOSSARY_*.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_TERMINOLOGY_*.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |
| TELEGRAM_TRANSLATION_CONSISTENCY.md | telegram/ | telegram/Reference/ | Phase 8 | Foundation | LOW |

---

# Move Matrix Summary

| Phase | Documents Moved | Risk |
|-------|----------------|------|
| Phase 3 | 6 | LOW |
| Phase 4 | 3 | LOW |
| Phase 5 | 11 | LOW |
| Phase 6 | 10 | LOW |
| Phase 7 | 9 | LOW |
| Phase 8 | 16 | LOW |
| **Total** | **152** | |

---

**End of Move Matrix**

**Mapper:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
