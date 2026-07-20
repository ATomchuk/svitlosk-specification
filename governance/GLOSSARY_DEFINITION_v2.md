# GLOSSARY_DEFINITION_v2

**Document ID:** SEM-004

**Title:** Glossary Definition v2

**Document Class:** Glossary Improvement

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. Current Definition

> **Publication Engine**
>
> **Ukrainian:** Движок публікацій
>
> **Definition:** The architectural Component implementing the Publisher Role. The Publication Engine is responsible for generating and distributing Publications.

---

# 2. Improved Definition

> **Publication Engine**
>
> **Ukrainian:** Движок публікацій
>
> **Definition:** Publication Engine is the canonical architectural Component responsible for transforming normalized outage data into deterministic Publication Packages and managing their complete lifecycle.
>
> **Architectural Responsibilities:**
> - Transforms normalized dataset into deterministic Publication Packages
> - Manages publication lifecycle (creation, distribution, ownership, daily cycle)
> - Controls publication windows (when publications are generated and updated)
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
> - Editorial content (owned by Editorial System)
> - Telegram Bot API interaction (owned by Telegram Publisher)
> - Graphic generation (owned by Graphic Generator)
> - Data retrieval (owned by Parser)
>
> **Inputs:**
> - Normalized Dataset (from Parser)
> - Schedules (from Schedule Generator)
> - Graphics (from Graphic Generator)
>
> **Outputs:**
> - Publication Package (to Telegram Publisher)
>
> **Interactions:**
> - Receives Normalized Dataset from Parser
> - Receives Schedules from Schedule Generator
> - Receives Graphics from Graphic Generator
> - Produces Publication Package for Telegram Publisher
> - Stores Publications in Data Storage
> - Delivers Publications through Telegram Channel
>
> **Lifecycle Responsibility:**
> - Publication Engine manages the complete publication lifecycle
> - From generation through distribution to archival
> - Owns the daily publication cycle and publication windows
>
> **Naming:**
> - Named "Engine" because it is a self-contained, deterministic processing Component
> - It autonomously transforms input into output through a deterministic pipeline
> - It additionally performs coordination by assembling outputs from multiple producers
> - The term "Engine" captures its primary responsibility: deterministic transformation with autonomous lifecycle management

---

# 3. Why This Is Stronger

| Dimension | Current Definition | Improved Definition |
|-----------|-------------------|-------------------|
| Starts with | "The architectural Component implementing..." | "Publication Engine is the canonical architectural Component responsible for..." |
| Architectural responsibility | Vague | Specific: transform + manage lifecycle |
| Ownership | Not defined | Explicit list |
| Boundaries | Not defined | Explicit list |
| Inputs/Outputs | Not defined | Explicit |
| Interactions | Not defined | Explicit |
| Lifecycle | Not defined | Explicit |
| Naming rationale | Not explained | Explained |

---

**End of Glossary Definition v2**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
