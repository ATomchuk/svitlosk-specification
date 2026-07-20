# ARCHITECTURE_RESPONSIBILITY_MATRIX

**Document ID:** ARM-001

**Title:** Architecture Responsibility Matrix

**Document Class:** Responsibility Matrix

**Status:** COMPLETE

**Author:** Independent Architect

---

# 1. Unified Responsibility Matrix

| Component | Purpose | Owns | Consumes | Produces | Controls | Lifecycle | Persistent State | External Deps | Internal Deps |
|-----------|---------|------|----------|----------|----------|-----------|-----------------|--------------|--------------|
| Parser | Retrieve Open Data | Data retrieval, validation, normalization | External Data Sources | Normalized Dataset | NONE | NONE | NONE | Data Sources | NONE |
| Publication Engine | Generate deterministic Publications | Publication generation, distribution, ownership, daily cycle, windows | Normalized Dataset, Schedules, Graphics | Publication Package | Publication lifecycle | Full lifecycle (Generated→Published→Updated→Archived) | Publication state | NONE | Parser, Schedule Generator, Graphic Generator |
| Publisher (Role) | Logical preparation/generation/distribution | Preparation, generation, distribution | NONE | Publication | NONE | NONE | NONE | NONE | NONE (implementation-independent) |
| Telegram Publisher | Telegram-specific delivery | Telegram Bot API, message delivery | Publication Package | Published messages | Message lifecycle | Message lifecycle | Telegram Message IDs | Telegram Bot API | Publication Engine |
| Schedule Generator | Generate deterministic schedules | Schedule generation, outage calculation, daily schedules, change detection | Normalized Dataset | Schedules | NONE | NONE | NONE | NONE | NONE |
| Graphic Generator | Produce visual materials | Graphic generation, image format, size constraints | Normalized Dataset, Schedules | Graphics | NONE | NONE | NONE | NONE | NONE |
| Data Storage | Preserve data and records | Persistent storage, historical preservation, metadata | Data, Publications, Schedules | Stored records | NONE | NONE | Persistent records | NONE | ALL components |
| Telegram Channel | Deliver Publications to subscribers | Channel delivery, subscriber management, admin interaction | Published messages | Channel feed | Channel state | Channel lifecycle | Subscriber list | Telegram platform | NONE |

---

# 2. Matrix Summary

| Component | Primary Responsibility | Unique? |
|-----------|----------------------|---------|
| Parser | Data retrieval and normalization | YES |
| Publication Engine | Deterministic publication generation and lifecycle management | YES |
| Publisher (Role) | Logical role (implementation-independent) | YES — abstract |
| Telegram Publisher | Telegram-specific message delivery | YES |
| Schedule Generator | Deterministic schedule generation | YES |
| Graphic Generator | Visual material production | YES |
| Data Storage | Persistent data preservation | YES |
| Telegram Channel | Public channel delivery | YES |

---

# 3. Matrix Verdict

**Every Component has exactly one primary responsibility. No duplicates found.**

---

**End of Responsibility Matrix**

**Author:** Independent Architect
**Date:** 2026-07-13
**Status:** COMPLETE
