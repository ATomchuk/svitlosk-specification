# Telegram Editorial Principle Review

**Date:** 2026-07-13
**Scope:** Complete review of all Editorial Principles
**Status:** REVIEW COMPLETE

---

# Purpose

This document reviews every Editorial Principle harvested during Stage E-0. The goal is to verify that each principle belongs to the Editorial Model, is uniquely defined, supports the mission of SvitloSk, and has the best possible canonical name.

---

# Review Results

## EP-001: Reader First Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Unique — no duplicate found |
| Mission Compatibility | 5/5 — Directly supports community-first approach |
| Canonical Naming | "Reader First" — clear, concise, appropriate |
| Necessity | KEEP |

**Rationale:** Core editorial principle that prioritizes the community. Essential for SvitloSk's mission.

---

## EP-002: Editorial Truth Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Partially duplicated with EP-003 (Editorial Silence) and EP-006 (Source Fidelity) |
| Mission Compatibility | 5/5 — Core integrity principle |
| Canonical Naming | "Editorial Truth" — clear, professional |
| Necessity | KEEP — but consider MERGE with EP-003 |

**Rationale:** Essential integrity principle. Overlaps with EP-003 and EP-006 but from different angles (truth vs silence vs fidelity).

---

## EP-003: Editorial Silence Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Partially duplicated with EP-002 (Editorial Truth) and EP-006 (Source Fidelity) |
| Mission Compatibility | 5/5 — Core integrity principle |
| Canonical Naming | "Editorial Silence" — evocative, memorable |
| Necessity | KEEP — unique perspective on integrity |

**Rationale:** "Silence" captures the concept of NOT speaking (not interpreting, not predicting). This is distinct from "Truth" (what IS said) and "Fidelity" (how it's said).

---

## EP-004: Minimal Editorial Intervention Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Unique — no duplicate found |
| Mission Compatibility | 5/5 — Supports automation and consistency |
| Canonical Naming | "Minimal Editorial Intervention" — clear, professional |
| Necessity | KEEP |

**Rationale:** Important workflow principle that defines the boundary between automatic and manual editing.

---

## EP-005: Issue Integrity Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Unique — no duplicate found |
| Mission Compatibility | 4/5 — Supports historical preservation |
| Canonical Naming | "Issue Integrity" — clear, appropriate |
| Necessity | KEEP |

**Rationale:** Important preservation principle that ensures daily publications remain available.

---

## EP-006: Source Fidelity Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Partially duplicated with EP-002 (Editorial Truth) and EP-003 (Editorial Silence) |
| Mission Compatibility | 5/5 — Core integrity principle |
| Canonical Naming | "Source Fidelity" — clear, professional |
| Necessity | KEEP — but consider MERGE with EP-002 |

**Rationale:** "Fidelity" captures the concept of faithfulness to the source. This is distinct from "Truth" (what IS said) and "Silence" (what is NOT said).

---

## EP-007: Deterministic Editorial Behaviour Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Unique — no duplicate found |
| Mission Compatibility | 5/5 — Supports consistency and reproducibility |
| Canonical Naming | "Deterministic Editorial Behaviour" — precise, technical |
| Necessity | KEEP |

**Rationale:** Important quality principle that ensures identical inputs produce identical outputs.

---

## EP-008: Accuracy Before Speed Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Project Principle (PP P-04) |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: NO — belongs to PROJECT_PRINCIPLES |
| Semantic Uniqueness | Unique — but is a Project Principle, not an Editorial Principle |
| Mission Compatibility | 5/5 — Core quality principle |
| Canonical Naming | "Accuracy Before Speed" — clear, memorable |
| Necessity | MOVE — should remain in PROJECT_PRINCIPLES |

**Rationale:** This is a Project Principle (PP P-04), not an Editorial Principle. It is correctly defined in PROJECT_PRINCIPLES.md. It should not be duplicated in the Editorial Model.

---

## EP-009: Territory-First Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Unique — no duplicate found |
| Mission Compatibility | 5/5 — Core structure principle |
| Canonical Naming | "Territory-First" — clear, concise |
| Necessity | KEEP |

**Rationale:** Important structure principle that defines how publications are organized.

---

## EP-010: Consistency Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Partially duplicated with EP-007 (Deterministic Editorial Behaviour) |
| Mission Compatibility | 4/5 — Supports quality and predictability |
| Canonical Naming | "Consistency" — simple, clear |
| Necessity | KEEP — but consider MERGE with EP-007 |

**Rationale:** "Consistency" is broader than "Deterministic" — it covers visual consistency, structural consistency, and content consistency.

---

## EP-011: Transparency Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Project Principle (PP P-06) |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: NO — belongs to PROJECT_PRINCIPLES |
| Semantic Uniqueness | Unique — but is a Project Principle, not an Editorial Principle |
| Mission Compatibility | 4/5 — Supports governance and trust |
| Canonical Naming | "Transparency" — clear, appropriate |
| Necessity | MOVE — should remain in PROJECT_PRINCIPLES |

**Rationale:** This is a Project Principle (PP P-06), not an Editorial Principle. It is correctly defined in PROJECT_PRINCIPLES.md. It should not be duplicated in the Editorial Model.

---

## EP-012: Community-First Principle

| Criterion | Assessment |
|-----------|------------|
| Classification | Editorial Principle |
| Ownership | Should remain inside TELEGRAM_EDITORIAL_MODEL: YES |
| Semantic Uniqueness | Fully duplicated with EP-001 (Reader First) |
| Mission Compatibility | 5/5 — Core audience principle |
| Canonical Naming | "Community-First" — clear, appropriate |
| Necessity | MERGE — merge with EP-001 |

**Rationale:** "Community-First" and "Reader First" express the same concept. EP-001 ("Reader First") is more precise for a publication system. EP-012 should be merged into EP-001.

---

# Missing Principles Search

Comparing against professional editorial systems for SvitloSk:

## MP-001: Accessibility Principle

**Statement:** Publications SHALL be accessible to all residents regardless of technical experience or device.

**Source:** CHARTER §4 (Social Mission)

**Why beneficial:** SvitloSk serves a community with varying technical literacy. An accessibility principle ensures publications are usable by everyone.

**Recommendation:** ADD as EP-013

---

## MP-002: Timeliness Principle

**Statement:** Publications SHALL be delivered promptly when official data becomes available.

**Source:** CHARTER §2 (Mission: "delivers it promptly")

**Why beneficial:** Timeliness is a core part of the mission. An explicit timeliness principle reinforces this.

**Recommendation:** ADD as EP-014

---

## MP-003: Completeness Principle

**Statement:** Publications SHALL include all relevant information from the official source for the reporting period.

**Source:** Implicit in TJS-004 §Categories (all categories without records are omitted)

**Why beneficial:** Ensures no information is silently dropped.

**Recommendation:** CONSIDER — may be covered by EP-010 (Consistency)

---

# Final Review Summary

| # | Principle | Classification | Owner | Uniqueness | Mission Score | Recommendation |
|---|-----------|---------------|-------|------------|---------------|----------------|
| EP-001 | Reader First | Editorial | Editorial Model | Unique | 5/5 | KEEP |
| EP-002 | Editorial Truth | Editorial | Editorial Model | Partially duplicated | 5/5 | KEEP |
| EP-003 | Editorial Silence | Editorial | Editorial Model | Partially duplicated | 5/5 | KEEP |
| EP-004 | Minimal Editorial Intervention | Editorial | Editorial Model | Unique | 5/5 | KEEP |
| EP-005 | Issue Integrity | Editorial | Editorial Model | Unique | 4/5 | KEEP |
| EP-006 | Source Fidelity | Editorial | Editorial Model | Partially duplicated | 5/5 | KEEP |
| EP-007 | Deterministic Editorial Behaviour | Editorial | Editorial Model | Unique | 5/5 | KEEP |
| EP-008 | Accuracy Before Speed | Project | PROJECT_PRINCIPLES | Unique (as editorial) | 5/5 | MOVE |
| EP-009 | Territory-First | Editorial | Editorial Model | Unique | 5/5 | KEEP |
| EP-010 | Consistency | Editorial | Editorial Model | Partially duplicated | 4/5 | KEEP |
| EP-011 | Transparency | Project | PROJECT_PRINCIPLES | Unique (as editorial) | 4/5 | MOVE |
| EP-012 | Community-First | Editorial | Editorial Model | Fully duplicated with EP-001 | 5/5 | MERGE |
| MP-001 | Accessibility | Editorial | Editorial Model | Unique | 5/5 | ADD |
| MP-002 | Timeliness | Editorial | Editorial Model | Unique | 5/5 | ADD |
| MP-003 | Completeness | Editorial | Editorial Model | Partially duplicated | 4/5 | CONSIDER |

---

# Canonical Naming Recommendations

| Current Name | Alternative Names | Recommendation |
|-------------|-------------------|----------------|
| Reader First | Community Priority, Audience First | KEEP "Reader First" — more precise for publication |
| Editorial Truth | Source Accuracy, Factual Integrity | KEEP "Editorial Truth" — clear and memorable |
| Editorial Silence | Editorial Restraint, Non-Interference | KEEP "Editorial Silence" — evocative and unique |
| Minimal Editorial Intervention | Automatic Generation, Minimal Touch | KEEP "Minimal Editorial Intervention" — precise |
| Issue Integrity | Daily Integrity, Archive Integrity | KEEP "Issue Integrity" — clear |
| Source Fidelity | Source Faithfulness, Official Fidelity | KEEP "Source Fidelity" — professional |
| Deterministic Editorial Behaviour | Deterministic Publishing, Consistent Output | KEEP "Deterministic Editorial Behaviour" — precise |
| Territory-First | Territory Priority, Geographic First | KEEP "Territory-First" — clear and concise |
| Consistency | Predictability, Uniformity | KEEP "Consistency" — simple and clear |
| Community-First | Community Priority | MERGE into "Reader First" |

---

**End of Editorial Principle Review**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
