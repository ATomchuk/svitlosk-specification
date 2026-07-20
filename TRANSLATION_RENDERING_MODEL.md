# TRANSLATION_RENDERING_MODEL

**Document ID:** TRM-001

**Title:** Translation Rendering Model

**Document Class:** Translation Governance Model

**Status:** Stable

**Author:** SvitloSk Project

---

# 1. Purpose

Define the four-layer translation rendering model for SvitloSk.

---

# 2. The Four-Layer Model

`
Semantic Layer
    |
    v
Identifier Layer
    |
    v
Rendering Layer
    |
    v
Presentation Layer
`

---

# 3. Layer Definitions

## Semantic Layer

The MEANING of the term within SvitloSk.

This layer is language-independent.

Example: "The absence of an outage" (concept)

## Identifier Layer

The CANONICAL ENGLISH term used in specifications.

This layer is English, permanent, and never translated.

Example: "Powered"

## Rendering Layer

The UKRAINIAN translation of the term for documentation.

This layer is Ukrainian and follows the approved translation.

Example: "Без знеструмлення"

## Presentation Layer

The DISPLAYED form of the term in specific contexts.

This layer MAY vary by context (graphic label vs documentation text).

Example: Graphic label = "Без знеструмлення" (max 25 chars)

---

# 4. Model Application

## Publication Engine

| Layer | Value |
|-------|-------|
| Semantic | Architectural Component implementing the Publisher Role |
| Identifier | Publication Engine |
| Rendering | Движок публікацій |
| Presentation | Движок публікацій (same across all contexts) |

## Canonical Equality

| Layer | Value |
|-------|-------|
| Semantic | Byte-for-byte identical output from identical input |
| Identifier | Canonical Equality |
| Rendering | Канонічна рівність |
| Presentation | Канонічна рівність (same across all contexts) |

## Powered

| Layer | Value |
|-------|-------|
| Semantic | NOT currently experiencing an outage |
| Identifier | Powered |
| Rendering | Без знеструмлення |
| Presentation | Без знеструмлення (universal — same in all contexts) |

---

# 5. Model vs One-to-One Mapping

| Dimension | One-to-One | Four-Layer |
|-----------|-----------|-----------|
| Semantic precision | LOW | HIGH |
| Context flexibility | NONE | YES |
| Long-term maintainability | FRAGILE | ROBUST |
| Architecture alignment | POOR | GOOD |

The four-layer model is superior for long-term repository maintenance because it separates meaning from display.

---

# 6. TTDR Integration

TTDR-001 SHALL use the four-layer model for every approved term.

Every term entry SHALL specify all four layers.

---

**End of Rendering Model**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
