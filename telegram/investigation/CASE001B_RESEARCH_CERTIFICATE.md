# CASE001B_RESEARCH_CERTIFICATE

**Document ID:** CASE001B-CERTIFICATE

**Title:** CASE-001B — Publication as a Living Domain Object — Research Certificate

**Document Class:** Investigation Artifact

**Status:** Complete

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Research Summary

**Investigation:** CASE-001B — Publication as a Living Domain Object

**Scope:** Reconstruct the real behaviour of Publication inside the Telegram Publishing System

**Constraint:** NOT a naming audit. NOT a DDD audit. NOT an architectural recommendation.

**Method:** Investigate repository evidence only. Ignore previous conclusions. Start from zero.

---

# Lifecycle Reconstructed

**5 Phases identified:**

1. **Non-Existence** — Publication does not exist. Data is retrieved, normalized, stored.
2. **Creation** — Publication Engine generates Publication from Normalized Dataset. Territory, Date, Template fixed. Content rendered. Lifecycle state = Generated.
3. **Delivery** — Telegram Publisher delivers to Telegram Channel. Telegram Message ID assigned. Lifecycle state = Published.
4. **Active Life** — Conditional updates when data changes. In-place editing. Lifecycle state = Published → Updated → Published.
5. **Archival/Removal** — Reporting period ends. Permanent Publications archived. Temporary Publications removed.

**Lifecycle Diagram:**

```
Non-Existence → Generated → Published ↔ Updated → Archived
                                          ↓
                                        Removed (temporary only)
```

**Evidence:** TJS-021 (TELEGRAM_PUBLICATION_LIFECYCLE.md), TJS-010 (TELEGRAM_PUBLISHING_CANONICAL_MODEL.md)

---

# Identity Model

**Primary Identity:** Territory + Date + Template

- No internal Publication ID exists in repository
- Telegram Message ID is an external reference assigned after delivery
- Identity persists across all lifecycle states
- Composite key uniquely identifies each Publication

**External Reference:** Telegram Message ID

- Assigned by Telegram platform after delivery
- Released when Publication is removed
- NOT identity — reference only

**Evidence:** TJS-005 (Canonical Templates), TJS-006 (Territory Ordering), Legacy TJS-007 §10

---

# Behaviour Summary

**Publication Engine is Aggregate Root:**

- ONLY component performing ALL actions: Create, Modify, Read, Own, Reference, Destroy, Archive
- No other component can create, modify, own, or destroy Publications
- All other components either produce input, deliver, display, store, or contain Publications

**Component Interaction Matrix:**

| Component | Creates | Modifies | Reads | Owns | References | Destroys | Archives |
|-----------|---------|----------|-------|------|------------|----------|----------|
| Parser | - | - | - | - | - | - | - |
| Schedule Generator | - | - | - | - | - | - | - |
| Graphic Generator | - | - | - | - | - | - | - |
| Publication Engine | YES | YES | YES | YES | YES | YES | YES |
| Telegram Publisher | - | YES | YES | - | YES | YES | - |
| Telegram Channel | - | - | YES | - | YES | - | - |
| Data Storage | - | YES | YES | - | YES | - | YES |
| Issue | - | - | - | - | YES | - | - |
| Journal | - | - | - | - | YES | - | - |

**6 Representations are Projections:**

Publication Package, Telegram Message, Repository Object, Editorial Object, Lifecycle Object, Historical Object — all projections of one Canonical Publication.

**Attribute Classification:**

- 7 IMMUTABLE (Territory, Date, Template, Generation Timestamp, Publication Timestamp, Source Dataset, Publication Identity)
- 4 MUTABLE (Content, Lifecycle State, Ownership, Archive Status)
- 3 DERIVED (Version, Ordering Position, Temporal Relevance)
- 1 EXTERNAL (Telegram Message ID)

---

# Contradictions Found

**Total: 14 contradictions**

| Severity | Count |
|----------|-------|
| HIGH | 2 |
| MEDIUM | 4 |
| LOW | 8 |

**Unresolved: 4 contradictions**

1. Manual Publications Lifecycle (HIGH) — different concept?
2. Interpretation Result (HIGH) — undefined concept
3. Platform Independence vs Telegram Mechanics (MEDIUM) — Telegram explicit in lifecycle
4. Manual Publication Creation (MEDIUM) — two creation paths

---

# Unresolved Questions

**Total: 26 open questions**

| Category | Count |
|----------|-------|
| Unknown | 10 |
| Cannot Prove | 3 |
| Insufficient Documents | 5 |
| Future Investigations | 8 |

**Critical Unknowns:**

1. What is an Interpretation Result? (undefined)
2. What happens when Territory structure changes? (unspecified)
3. What happens during system/Telegram downtime? (unspecified)
4. What is Manual Publication lifecycle? (unspecified)
5. How do Graphic Publications relate to text Publications? (unspecified)

---

# Deliverables Produced

| # | Document | Content |
|---|----------|---------|
| 1 | CASE001_PUBLICATION_LIFECYCLE_RECONSTRUCTION.md | Complete life of one Publication (5 phases) |
| 2 | CASE001_PUBLICATION_BEHAVIOUR_MATRIX.md | Component × Action matrix (9 × 8) |
| 3 | CASE001_PUBLICATION_IDENTITY_ANALYSIS.md | Identity investigation (9 candidates) |
| 4 | CASE001_PUBLICATION_STATE_MODEL.md | 6 representations as projections |
| 5 | CASE001_PUBLICATION_MUTATION_MODEL.md | 15 attributes classified |
| 6 | CASE001_PUBLICATION_COMPONENT_INTERACTION.md | Detailed component analysis |
| 7 | CASE001_PUBLICATION_CONTRADICTIONS.md | 14 contradictions found |
| 8 | CASE001_PUBLICATION_OPEN_QUESTIONS.md | 26 open questions |
| 9 | CASE001B_RESEARCH_CERTIFICATE.md | This document |

---

# Evidence Sources

| Document | Sections Used |
|----------|--------------|
| TJS-021 (TELEGRAM_PUBLICATION_LIFECYCLE.md) | §3.1, §4, §5, §6, §7, §8, §9 |
| TJS-010 (TELEGRAM_PUBLISHING_CANONICAL_MODEL.md) | §3, §4, §5, §6 |
| TJS-020 (TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md) | §4 |
| TJS-022 (TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md) | §5, §6 |
| GLOSSARY.md | §3 (Publication Model) |
| DATA_MODEL.md | §4, §5 |
| Legacy TJS-007 | §4, §5, §6, §8, §9, §10, §11 |
| Legacy TJS-008 | §12, §14 |
| Legacy TJS-002 | §4 |
| TJS-005 (Publication Grammar) | Templates A, B, C, D |
| TJS-006 (Territory Ordering) | Territory structure |

---

# Research Certificate

**This document certifies that CASE-001B — Publication as a Living Domain Object investigation is COMPLETE.**

**All 9 deliverables have been produced.**

**The investigation reconstructed:**

- Complete lifecycle (5 phases)
- Identity model (Territory + Date + Template)
- Behaviour summary (Publication Engine as Aggregate Root)
- 14 contradictions (4 unresolved)
- 26 open questions (10 unknown, 3 unprovable, 5 insufficient, 8 future investigations)

**This is research only. No recommendations. No preferred model. The Architect will decide.**

---

**End of Research Certificate**
