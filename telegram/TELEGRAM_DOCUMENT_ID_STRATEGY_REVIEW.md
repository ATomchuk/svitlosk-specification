# Telegram Document ID Strategy Review

**Date:** 2026-07-13
**Scope:** Review of the current numbering strategy
**Status:** REVIEW COMPLETE

---

# Purpose

This document reviews the Telegram document numbering system to determine whether it follows a coherent strategy.

---

# Current Numbering System

## TJS Specifications

| ID Pattern | Current Usage | Target Usage (Architecture Decision) |
|-----------|---------------|-------------------------------------|
| TJS-001 | Journal Concept | Journal Concept |
| TJS-002 | Publication Lifecycle | Editorial Policy |
| TJS-003 | Post Structure | Message Templates |
| TJS-004 | Editorial Policy | Rendering Rules |
| TJS-005 | Message Templates | Publication Lifecycle |
| TJS-006 | Rendering Rules | Channel Management |
| TJS-007 | Publication Lifecycle | Graphic Rendering |
| TJS-008 | Publication Lifecycle | — (not assigned) |

## Foundational Documents

| ID Pattern | Current Usage |
|-----------|---------------|
| TJS-000 | Semantic Model |
| TJS-000A | Glossary |
| TJS-000B | Alignment Process |
| TJS-000C | Alignment Pipeline |
| TJS-000D | Alignment Governance |
| TJS-TEMPLATE | Alignment Template |

---

# Numbering Strategy Analysis

## Is there a coherent numbering strategy?

**NO**

The current numbering strategy has the following problems:

### Problem 1: No Sequential Order

The TJS-001 through TJS-008 IDs do not follow a logical reading order. The intended order (from the Architecture Decision) is:

```
TJS-001: Journal Concept (identity)
TJS-002: Editorial Policy (standards)
TJS-003: Message Templates (templates)
TJS-004: Rendering Rules (rendering)
TJS-005: Publication Lifecycle (lifecycle)
TJS-006: Channel Management (integration)
TJS-007: Graphic Rendering (graphics)
```

But the current IDs map to:

```
TJS-001: Journal Concept (identity) ✓
TJS-002: Publication Lifecycle (lifecycle) ✗ — should be Editorial Policy
TJS-003: Post Structure (structure) ✗ — should be Message Templates
TJS-004: Editorial Policy (standards) ✗ — should be Rendering Rules
TJS-005: Message Templates (templates) ✗ — should be Publication Lifecycle
TJS-006: Rendering Rules (rendering) ✗ — should be Channel Management
TJS-007: Publication Lifecycle (lifecycle) ✗ — should be Graphic Rendering
TJS-008: Publication Lifecycle (lifecycle) ✗ — not assigned in target
```

### Problem 2: Triple Lifecycle Duplication

Three documents (TJS-002, TJS-007, TJS-008) all use "Publication Lifecycle" as their name. This is a critical SSOT violation.

### Problem 3: Foundational ID Naming

The foundational documents use a different naming convention:
- TJS-000 (no suffix)
- TJS-000A (suffix A)
- TJS-000B (suffix B)
- TJS-000C (suffix C)
- TJS-000D (suffix D)
- TJS-TEMPLATE (full word suffix)

This is inconsistent with the TJS-001 through TJS-008 pattern.

---

# Numbering Strategy Recommendations

## Recommendation 1: Use Current-State IDs in Architecture Decision

The Architecture Decision SHOULD use current-state IDs to avoid confusion. The target-state mapping should be documented separately.

## Recommendation 2: Adopt Sequential Numbering

After migration, the TJS numbering SHOULD follow a logical reading order:

```
TJS-001: Journal Concept (identity)
TJS-002: Editorial Policy (standards)
TJS-003: Message Templates (templates)
TJS-004: Rendering Rules (rendering)
TJS-005: Publication Lifecycle (lifecycle)
TJS-006: Channel Management (integration)
TJS-007: Graphic Rendering (graphics)
```

## Recommendation 3: Use Consistent Foundational IDs

The foundational documents SHOULD use a consistent naming convention. Options:
- TJS-000 through TJS-000D (current)
- TJS-F01 through TJS-F06 (foundational prefix)

---

# Numbering Strategy Summary

| Criterion | Status |
|-----------|--------|
| Coherent numbering strategy? | NO |
| Sequential order? | NO |
| Consistent naming? | NO |
| No conflicts? | NO (6 conflicts) |
| No triple duplication? | NO (TJS-002, TJS-007, TJS-008) |

---

**End of Strategy Review**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
