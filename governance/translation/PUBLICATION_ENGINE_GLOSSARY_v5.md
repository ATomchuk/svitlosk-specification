# PUBLICATION_ENGINE_GLOSSARY_v5

**Document ID:** GSR-007

**Title:** Publication Engine Glossary v5

**Document Class:** Glossary Definition

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. Version History

| Version | Key Wording | Issue |
|---------|-----------|-------|
| v1 | "The architectural Component implementing the Publisher Role." | Implementation-first |
| v2 | "Publication Engine is the canonical architectural Component responsible for..." | Better but verbose |
| v3 | "...governing their complete publication lifecycle." | "their" ambiguous |
| v4 | "...governing the complete lifecycle of those Publications." | "those" = pronoun reference |
| v5 | "...governing the complete lifecycle of the generated Publications." | "generated" = descriptor, matches TJS-010 §5.1 |

---

# 2. Final Definition (v5)

> **Publication Engine**
>
> **Ukrainian:** Движок публікацій
>
> **Definition:** Publication Engine is the canonical architectural Component responsible for generating deterministic Publication Packages from normalized outage data and governing the complete lifecycle of the generated Publications.
>
> **Responsibilities:**
> - Transforms normalized dataset into deterministic Publication Packages
> - Manages the complete lifecycle of generated Publications
> - Controls publication windows and daily publication cycle
> - Implements the Publisher Role with deterministic, repeatable behaviour
>
> **Ownership:**
> - Publication generation
> - Publication distribution
> - Publication ownership model
> - Daily publication cycle
> - Publication windows
>
> **Boundaries — Does NOT Own:**
> - Editorial content
> - Telegram Bot API interaction
> - Graphic generation
> - Data retrieval
>
> **Interactions:**
> - Consumes: Normalized Dataset (Parser), Schedules (Schedule Generator), Graphics (Graphic Generator)
> - Produces: Publication Package (to Telegram Publisher)
> - Stores: generated Publications (Data Storage)
> - Delivers: generated Publications (Telegram Channel)
>
> **Naming:** "Engine" denotes a self-contained, deterministic processing Component with autonomous lifecycle management. Additionally performs coordination by assembling outputs from multiple producers.

---

# 3. What Changed (v4 → v5)

| Element | v4 | v5 |
|---------|----|----|
| Core phrase | "lifecycle of those Publications" | "lifecycle of the generated Publications" |
| Pronoun/Descriptor | "those" (pronoun) | "generated" (descriptor) |
| Repository pattern match | "lifecycle of those Publications" | "lifecycle of the generated Publications" — matches TJS-010 line 206 |

---

# 4. What Did NOT Change

| Element | Status |
|---------|--------|
| Canonical identifier | UNCHANGED |
| Ukrainian rendering | UNCHANGED |
| Architectural responsibilities | UNCHANGED |
| Ownership list | UNCHANGED |
| Boundaries | UNCHANGED |
| Interactions | UNCHANGED |
| Naming rationale | UNCHANGED |

---

**End of Glossary v5**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
