# PUBLICATION_ENGINE_GLOSSARY_v4

**Document ID:** GSR-002

**Title:** Publication Engine Glossary v4

**Document Class:** Glossary Definition

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. Version History

| Version | Definition | Issue |
|---------|-----------|-------|
| v1 (original) | "The architectural Component implementing the Publisher Role..." | Starts with implementation, not responsibility |
| v2 (A-4.1) | "Publication Engine is the canonical architectural Component responsible for..." | Better, but verbose |
| v3 (A-4.2) | "Publication Engine is the canonical architectural Component responsible for generating deterministic Publication Packages from normalized outage data and governing their complete publication lifecycle." | "their" pronoun ambiguous |
| v4 (A-4.3) | "Publication Engine is the canonical architectural Component responsible for generating deterministic Publication Packages from normalized outage data and governing the complete lifecycle of those Publications." | Precise, unambiguous |

---

# 2. Final Definition (v4)

> **Publication Engine**
>
> **Ukrainian:** Движок публікацій
>
> **Definition:** Publication Engine is the canonical architectural Component responsible for generating deterministic Publication Packages from normalized outage data and governing the complete lifecycle of those Publications.
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
> - Stores: Publications (Data Storage)
> - Delivers: Publications (Telegram Channel)
>
> **Naming:** "Engine" denotes a self-contained, deterministic processing Component with autonomous lifecycle management. Additionally performs coordination by assembling outputs from multiple producers.

---

# 3. v3 vs v4

| Dimension | v3 | v4 |
|-----------|----|----|
| Opening | "governing their complete publication lifecycle" | "governing the complete lifecycle of those Publications" |
| Ambiguity | "their" = ambiguous | "those Publications" = explicit |
| Repository pattern | "publication lifecycle" | "lifecycle of those Publications" — matches Glossary §11 |
| Object ownership | Vague | Explicit entity ownership |
| Semantic precision | GOOD | BETTER |

---

# 4. What Changed (and What Did Not)

| Element | Changed? | Reason |
|---------|---------|--------|
| Canonical identifier | NO | Publication Engine unchanged |
| Ukrainian rendering | NO | Движок публікацій unchanged |
| Architectural responsibilities | NO | Same 5 responsibilities |
| Ownership list | NO | Same 5 ownership items |
| Boundaries | NO | Same 4 boundaries |
| Interactions | NO | Same 4 interactions |
| Naming rationale | NO | Same explanation |
| **Wording precision** | **YES** | "their complete publication lifecycle" → "the complete lifecycle of those Publications" |

---

**End of Glossary v4**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
