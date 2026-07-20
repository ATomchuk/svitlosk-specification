# PUBLICATION_ENGINE_GLOSSARY_v3

**Document ID:** ARM-004

**Title:** Publication Engine Glossary v3

**Document Class:** Glossary Definition

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. Previous Versions

| Version | Opening | Issue |
|---------|---------|-------|
| v1 (current) | "The architectural Component implementing the Publisher Role." | Starts with implementation, not responsibility |
| v2 (proposed A-4.1) | "Publication Engine is the canonical architectural Component responsible for..." | Better but verbose |

---

# 2. Final Definition (v3)

> **Publication Engine**
>
> **Ukrainian:** Движок публікацій
>
> **Definition:** Publication Engine is the canonical architectural Component responsible for generating deterministic Publication Packages from normalized outage data and governing their complete publication lifecycle.
>
> **Responsibilities:**
> - Transforms normalized dataset into deterministic Publication Packages
> - Manages the publication lifecycle from creation through archival
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
> - Stores: Publications (Data Storage)
> - Delivers: Publications (Telegram Channel)
>
> **Naming:** "Engine" denotes a self-contained, deterministic processing Component with autonomous lifecycle management. Publication Engine additionally performs coordination by assembling outputs from multiple producers, but its primary responsibility is deterministic transformation.

---

# 3. Why v3 Is Stronger

| Dimension | v1 | v2 | v3 |
|-----------|----|----|-----|
| Opens with | Implementation | Responsibility | Responsibility |
| Responsibility clarity | Vague | Good | Precise |
| Ownership | Not listed | Listed | Listed |
| Boundaries | Not listed | Listed | Listed |
| Interactions | Not listed | Listed | Listed |
| Lifecycle | Not mentioned | Mentioned | Explicit |
| Naming rationale | Not explained | Explained | Explained |
| Conciseness | HIGH | MEDIUM | HIGH |

---

**End of Glossary v3**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
