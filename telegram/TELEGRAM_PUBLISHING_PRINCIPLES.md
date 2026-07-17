# Telegram Publishing Principles

**Date:** 2026-07-13
**Scope:** Every approved architectural principle for the Publishing System
**Status:** HARVEST COMPLETE

---

# Purpose

This document harvests every approved architectural principle governing the Telegram Publishing System. Each principle is traceable to its original source.

---

# P-001: Repository Authority Principle

**Statement:** TELEGRAM_GLOSSARY.md is the authoritative semantic source for every Telegram specification. When terminology conflicts arise, the Glossary SHALL prevail.

**Source:** TELEGRAM_GLOSSARY.md §2, §5

**Type:** Semantic governance

---

# P-002: Publishing Synchronization Principle

**Statement:** Publication updates SHALL occur only after a new normalized Dataset becomes available. Time alone SHALL NOT trigger Publication updates.

**Source:** TJS-008-Publication-Lifecycle.md §7

**Type:** Operational principle

---

# P-003: Deterministic Publishing Principle

**Statement:** Two identical normalized Datasets SHALL always generate identical Telegram Journals. Publication order, formatting and content SHALL remain deterministic.

**Source:** TJS-008-Publication-Lifecycle.md §9

**Type:** Operational principle

---

# P-004: Editorial Neutrality Principle

**Statement:** Every publication must increase clarity without changing the meaning of the official source. The journal does not interpret, predict or alter official information. It reorganizes and presents it in a form that is easier to understand.

**Source:** TJS-001-Journal-Concept.md §6

**Type:** Editorial principle

---

# P-005: Complete Issue Principle

**Statement:** The daily publication package consists of: one post for Starokostiantyniv; one post for every starosta district with available information; separate posts containing information for the following day. Posts without information are not created.

**Source:** TJS-004-Editorial-Policy.md §Publication Package

**Type:** Publication completeness principle

---

# P-006: Appropriate Complexity Principle

**Statement:** Every new component SHALL solve an existing problem. Complexity SHALL grow only when justified by real project needs. Features SHALL never be added solely because they may become useful.

**Source:** PROJECT_PRINCIPLES.md P-08

**Type:** Architectural principle

---

# P-007: Local First Architecture

**Statement:** The Journal exists independently from any publication platform. Telegram itself SHALL NOT be considered the Journal. Telegram SHALL only be considered the publication platform.

**Source:** TELEGRAM_SEMANTIC_MODEL.md §3

**Type:** Architectural principle

---

# P-008: Working Repository Principle

**Statement:** The canonical repository SHALL contain approved knowledge only. Temporary audit artifacts SHALL remain isolated from the canonical documentation.

**Source:** PROJECT_PRINCIPLES.md P-11

**Type:** Repository governance principle

---

# P-009: Journal Finality Principle

**Statement:** The Telegram Journal SHALL be treated as a long-lived public information journal. The Publisher SHALL modify only Publications that it owns. The Publisher SHALL NOT modify, delete or reorder Publications created by other publishers or administrators.

**Source:** TJS-007-Publication-Lifecycle.md §11, TELEGRAM_GLOSSARY.md §11

**Type:** Lifecycle principle

---

# P-010: Semantic Ownership Principle

**Statement:** TELEGRAM_SEMANTIC_MODEL.md is the single semantic authority for all Telegram terminology. No Telegram specification SHALL redefine concepts owned by the Semantic Model.

**Source:** TELEGRAM_SEMANTIC_MODEL.md §6, TELEGRAM_GLOSSARY.md §16

**Type:** Semantic governance principle

---

# P-011: Single Responsibility Principle

**Statement:** One responsibility. One owner. No shared ownership. Every TJS document SHALL define one complete subject area.

**Source:** TELEGRAM_ARCHITECTURE_DECISION.md §Responsibility Matrix, §Constraints #1, #10

**Type:** Architectural principle

---

# P-012: Separation of Concerns Principle

**Statement:** The principle that Policy and Implementation are separated across documents. Formatting POLICY is owned by TJS-002; Formatting IMPLEMENTATION is owned by TJS-003.

**Source:** TELEGRAM_GLOSSARY.md §16, TELEGRAM_ARCHITECTURE_DECISION.md §Constraints #3

**Type:** Architectural principle

---

# P-013: Non-Destructive Channel Principle

**Statement:** The Publisher SHALL modify only Publications that it owns. The Publisher SHALL NOT modify, delete or reorder Publications created by other publishers or administrators.

**Source:** TJS-007-Publication-Lifecycle.md §11, TELEGRAM_GLOSSARY.md §11

**Type:** Lifecycle principle

---

# P-014: Non-Destructive Update Principle

**Statement:** Updates SHOULD modify existing Publications instead of replacing them. Replacing an existing Publication SHALL be considered a last resort.

**Source:** TJS-008-Publication-Lifecycle.md §10, TELEGRAM_GLOSSARY.md §11

**Type:** Lifecycle principle

---

# P-015: Stable Journal Principle

**Statement:** The Telegram Journal SHALL remain visually stable throughout the reporting day. Existing Publications SHALL be updated in place whenever possible. Publications SHALL NOT be deleted and recreated solely because their content has changed.

**Source:** TJS-008-Publication-Lifecycle.md §8

**Type:** Lifecycle principle

---

# P-016: Deterministic Rendering Principle

**Statement:** The same normalized dataset SHALL always produce identical output. Two publications generated from identical datasets SHALL be byte-for-byte identical.

**Source:** TELEGRAM_GLOSSARY.md §14, TJS-006-Rendering-Rules.md §3

**Type:** Rendering principle

---

# P-017: Source Fidelity Principle

**Statement:** Rendering SHALL NOT modify or reinterpret official information. The principle that rendering SHALL NOT modify or reinterpret official information.

**Source:** TELEGRAM_GLOSSARY.md §14, TJS-006-Rendering-Rules.md §3

**Type:** Rendering principle

---

# P-018: Dependency Direction Principle

**Statement:** Dependencies flow from TJS-001 downward. No circular dependencies are permitted.

**Source:** TELEGRAM_GLOSSARY.md §16, TELEGRAM_ARCHITECTURE_DECISION.md §Dependency Graph

**Type:** Architectural governance principle

---

# P-019: One Document — One Subject Principle

**Statement:** Every normative document defines one complete subject area. Documents SHOULD complement one another instead of overlapping.

**Source:** PROJECT_PRINCIPLES.md P-10, TELEGRAM_GLOSSARY.md §16

**Type:** Documentation governance principle

---

# P-020: Accuracy Before Speed Principle

**Statement:** Publishing information quickly is important. Publishing accurate information is mandatory. Whenever these goals conflict, accuracy SHALL take priority.

**Source:** PROJECT_PRINCIPLES.md P-04

**Type:** Operational principle

---

# Principles Summary

| # | Principle | Source | Type |
|---|-----------|--------|------|
| P-001 | Repository Authority | TG §2, §5 | Semantic governance |
| P-002 | Publishing Synchronization | TJS-008 §7 | Operational |
| P-003 | Deterministic Publishing | TJS-008 §9 | Operational |
| P-004 | Editorial Neutrality | TJS-001 §6 | Editorial |
| P-005 | Complete Issue | TJS-004 §Package | Publication completeness |
| P-006 | Appropriate Complexity | PP P-08 | Architectural |
| P-007 | Local First Architecture | TSM §3 | Architectural |
| P-008 | Working Repository | PP P-11 | Repository governance |
| P-009 | Journal Finality | TJS-007 §11, TG §11 | Lifecycle |
| P-010 | Semantic Ownership | TSM §6, TG §16 | Semantic governance |
| P-011 | Single Responsibility | TAD §Responsibility, §Constraints | Architectural |
| P-012 | Separation of Concerns | TG §16, TAD §Constraints | Architectural |
| P-013 | Non-Destructive Channel | TJS-007 §11, TG §11 | Lifecycle |
| P-014 | Non-Destructive Update | TJS-008 §10, TG §11 | Lifecycle |
| P-015 | Stable Journal | TJS-008 §8 | Lifecycle |
| P-016 | Deterministic Rendering | TG §14, TJS-006 §3 | Rendering |
| P-017 | Source Fidelity | TG §14, TJS-006 §3 | Rendering |
| P-018 | Dependency Direction | TG §16, TAD §Dependency | Architectural governance |
| P-019 | One Document — One Subject | PP P-10, TG §16 | Documentation governance |
| P-020 | Accuracy Before Speed | PP P-04 | Operational |

---

**Total Principles Harvested:** 20

---

**End of Publishing Principles**

**Harvester:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
