# Telegram Publishing Component Matrix

**Date:** 2026-07-13
**Scope:** One row for every component in the Telegram Publishing System
**Status:** HARVEST COMPLETE

---

| Component | Purpose | Owns | Does NOT own | Depends on | Used by | Lifecycle | Notes |
|-----------|---------|------|-------------|------------|---------|-----------|-------|
| Publication Engine | Transforms normalized dataset into deterministic Publication Package | Publication generation, distribution, ownership model, daily cycle, publication windows | Editorial content, Telegram Bot API, graphic generation | Parser (normalized dataset), TJS-004 (Rendering Rules), TJS-005 (Lifecycle) | TJS-006 (Channel Management) | Created → Publishes → Updates → Retains/Removes | Implements Publisher Role |
| Parser | Retrieves Open Data from approved Data Sources | Data retrieval, validation, normalization | Interpretation, publication, rendering | Data Sources (external) | Publication Engine | Retrieve → Validate → Normalize | Only component authorized to transform external data |
| Publisher (Role) | Logical role for preparing, generating and distributing Publications | Publication preparation, generation, distribution | Data retrieval, parsing, reinterpretation | — | Implemented by Publication Engine | Role-based | Implementation-independent concept |
| Telegram Publisher | Telegram-specific implementation of Publisher Role | Telegram Bot API interaction, message delivery | Data retrieval, parsing, editorial content | Publication Engine, Telegram Bot API | Subscribers, Administrators | Platform-specific | Platform-specific component |
| Schedule Generator | Transforms normalized outage data into deterministic schedules | Schedule generation, outage period calculation, daily schedules, change detection | Publication rendering, Telegram delivery | Parser (normalized data), Data Storage | Publication Engine | Data → Schedule → Publication | SSP-006 |
| Graphic Generator | Produces visual materials based on normalized outage schedules | Graphic generation, image format, size constraints | Text publication, lifecycle management | Parser (normalized data), SSP-003 | TJS-007 (Graphic Rendering) | Data → Graphic → Publication | SSP-007 |
| Data Storage | Preserving normalized data, publications, schedules, historical records | Persistent storage, historical preservation, metadata | Publication rendering, Telegram delivery | Parser (data), Publication Engine (publications) | All components | Store → Retrieve → Archive | SSP-005 |
| Telegram Channel | Primary public information journal delivering Publications | Channel delivery, subscriber management, admin interaction | Editorial content, lifecycle rules, publication generation | Publication Engine (publications) | Subscribers, Administrators | Channel lifecycle | SSP-004 |

---

# Component Summary

| Component | Type | Abstraction Level |
|-----------|------|-------------------|
| Publication Engine | Architectural Component | Implementation |
| Parser | Architectural Component | Implementation |
| Publisher | Logical Role | Conceptual |
| Telegram Publisher | Architectural Component | Implementation (platform-specific) |
| Schedule Generator | Architectural Component | Implementation |
| Graphic Generator | Architectural Component | Implementation |
| Data Storage | Architectural Component | Implementation |
| Telegram Channel | Architectural Component | Implementation (platform-specific) |

---

# Component Relationships

| Relationship | Source | Target | Type |
|-------------|--------|--------|------|
| Publication Engine implements | Publisher (Role) | — | Implements |
| Parser produces data for | — | Publication Engine | Data flow |
| Telegram Publisher implements | Publisher (Role) for Telegram | — | Implements |
| Schedule Generator produces schedules for | — | Publication Engine | Data flow |
| Graphic Generator produces graphics for | — | Publication Engine | Data flow |
| Data Storage stores data from | Parser, Publication Engine | — | Persistence |
| Telegram Channel delivers | Publication Engine | Subscribers | Distribution |

---

**End of Component Matrix**

**Harvester:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
