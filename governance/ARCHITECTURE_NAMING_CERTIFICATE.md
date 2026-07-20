# ARCHITECTURE_NAMING_CERTIFICATE

**Document ID:** NPA-006

**Title:** Architecture Naming Certificate

**Document Class:** Certificate

**Status:** CERTIFIED

**Author:** SvitloSk Project

---

# 1. Final Questions

| # | Question | Answer |
|---|----------|--------|
| 1 | Has Publication Engine become a Proper Architectural Name? | **YES** — satisfies all 5 canonicalization criteria |
| 2 | When did this transition occur? | When TJS-010 formalized the 8-component architecture and Glossary provided normative definition |
| 3 | Should canonical identifiers ever be translated literally? | **NO** — they SHALL be translated as a single unit per PR-NAM-001 |
| 4 | Should Glossary definitions become richer? | **YES** — improved definition proposed for Publication Engine |
| 5 | Improved normative definition? | See GLOSSARY_DEFINITION_IMPROVEMENT.md |

---

# 2. Improved Definition of Publication Engine

> The architectural Component implementing the Publisher Role. The Publication Engine is responsible for generating and distributing Publications.
>
> **Architectural Responsibilities:** Publication generation, distribution, ownership model, daily cycle, publication windows.
>
> **Boundaries:** Does NOT own editorial content, Telegram Bot API, or graphic generation.
>
> **Interactions:** Receives from Parser, Schedule Generator, Graphic Generator. Produces for Telegram Publisher. Stores in Data Storage. Delivers through Telegram Channel.
>
> **Naming:** Named "Engine" because it processes data into publication packages. It functions partly as a Coordinator (assembling outputs from producers) and partly as an Engine (processing data into deterministic output).

---

# 3. Certification Statement

**All 8 canonical components are Proper Architectural Names. PR-NAM-001 is proposed. Glossary definition improvement is proposed. No canonical identifier changes recommended.**

---

**End of Certificate**

**Certifier:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** CERTIFIED
