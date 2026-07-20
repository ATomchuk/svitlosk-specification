# GLOSSARY_DEFINITION_IMPROVEMENT

**Document ID:** NPA-005

**Title:** Glossary Definition Improvement

**Document Class:** Glossary Improvement

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. Current Definition (TJS-000A §8)

> **Publication Engine**
> **Ukrainian:** Движок публікацій
> **Definition:** The architectural Component implementing the Publisher Role. The Publication Engine is responsible for generating and distributing Publications.

---

# 2. Analysis

The current definition is **accurate but insufficient**. It describes WHAT the component is and WHAT it does, but does not explain:

- WHY it is called "Engine" (not "Coordinator")
- HOW it relates to neighbouring components
- WHAT it owns vs. what it does not own
- Its BOUNDARIES and INTERACTIONS

---

# 3. Improved Definition

> **Publication Engine**
>
> **Ukrainian:** Движок публікацій
>
> **Definition:** The architectural Component implementing the Publisher Role. The Publication Engine is responsible for generating and distributing Publications.
>
> **Architectural Responsibilities:**
> - Publication generation and distribution
> - Ownership model (which Publications it owns)
> - Daily publication cycle
> - Publication windows (when it operates)
>
> **Boundaries:**
> - DOES NOT own editorial content
> - DOES NOT own Telegram Bot API
> - DOES NOT own graphic generation
>
> **Interactions:**
> - Receives Normalized Dataset from Parser
> - Receives Schedules from Schedule Generator
> - Receives Graphics from Graphic Generator
> - Produces Publication Package for Telegram Publisher
> - Stores Publications in Data Storage
> - Delivers Publications through Telegram Channel
>
> **Naming:** Named "Engine" because it processes data into publication packages through a deterministic pipeline. It functions partly as a Coordinator (assembling outputs from multiple producers) and partly as an Engine (processing data into deterministic output).

---

# 4. Recommendation

The improved definition should replace the current one-line definition in TELEGRAM_GLOSSARY.md §8.

This is a **definition improvement**, not a name change. The canonical identifier "Publication Engine" remains unchanged.

---

**End of Glossary Improvement**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
