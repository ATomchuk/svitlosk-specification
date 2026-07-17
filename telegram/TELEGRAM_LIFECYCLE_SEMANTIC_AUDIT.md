# Telegram Lifecycle Semantic Audit

**Date:** 2026-07-13
**Scope:** Semantic model of Lifecycle only
**Source:** Existing terminology harvest documents + TJS specifications

---

# Purpose

This audit reviews the semantic model of Publication Lifecycle. It determines how many lifecycle state models exist, whether they are actually different, and recommends ONE canonical model.

---

# Question 1: How many Lifecycle State Models currently exist?

**THREE** lifecycle state models currently exist.

---

# Question 2: List every version

| Version | Document | Section | Title |
|---------|----------|---------|-------|
| Version A | TJS-002-Publication-Lifecycle.md | §3 | "Lifecycle Overview" |
| Version B | TJS-007-Publication-Lifecycle.md | §3 | "Publication Lifecycle" |
| Version C | TJS-008-Publication-Lifecycle.md | §3 | "Publication Cycle" |

---

# Question 3: Where is every version defined?

| Version | File | Lines | Defining Text |
|---------|------|-------|---------------|
| A | TJS-002-Publication-Lifecycle.md | 27-37 | "Each publication shall pass through one or more of the following states: 1. Generated 2. Scheduled 3. Published 4. Updated 5. Archived 6. Removed" |
| B | TJS-007-Publication-Lifecycle.md | 35-57 | "Every Publication SHALL follow the same lifecycle. Dataset → Render → Publish → Update (if required) → Retain or Remove" |
| C | TJS-008-Publication-Lifecycle.md | 34-45 | "The Telegram Journal SHALL follow one daily publication cycle. The cycle consists of: 1. generation of the Today's Package; 2. publication of Today's Posts; 3. monitoring Dataset updates; 4. updating changed Publications; 5. generation of Tomorrow Publications; 6. removal of obsolete Tomorrow Publications" |

---

# Question 4: Are they actually different?

**YES — they are genuinely different.**

They do NOT describe the same concept using different wording. They describe DIFFERENT aspects of the lifecycle at DIFFERENT abstraction levels.

| Aspect | Version A (TJS-002) | Version B (TJS-007) | Version C (TJS-008) |
|--------|---------------------|---------------------|---------------------|
| Abstraction level | Conceptual | Operational | Temporal |
| Focus | Publication states | Component flow | Daily schedule |
| Input | Official data | Normalized dataset | Normalized dataset |
| Output | Publication states | Telegram message | Telegram posts |
| Time dimension | None | None | 24-hour cycle |
| Components mentioned | None | Parser, Engine, Publisher | Engine, Publisher |
| State count | 6 | 5 | 6 steps |

---

# Question 5: Comparison Table

## State-by-State Comparison

| Canonical State | Version A (TJS-002) | Version B (TJS-007) | Version C (TJS-008) | Compatible? |
|----------------|---------------------|---------------------|---------------------|-------------|
| **Generated** | Generated (state 1) | Render (stage 1) | generation of Today's Package (step 1) | PARTIALLY — different granularity |
| **Scheduled** | Scheduled (state 2) | — | — | UNIQUE to A |
| **Published** | Published (state 3) | Publish (stage 2) | publication of Today's Posts (step 2) | YES — consistent |
| **Updated** | Updated (state 4) | Update (stage 3) | updating changed Publications (step 4) | YES — consistent |
| **Archived** | Archived (state 5) | Retain (stage 4) | — | PARTIALLY — A has explicit state, B has flow |
| **Removed** | Removed (state 6) | Remove (stage 5) | removal of obsolete Tomorrow (step 6) | YES — consistent |
| **Monitoring** | — | — | monitoring Dataset updates (step 3) | UNIQUE to C |
| **Tomorrow generation** | — | — | generation of Tomorrow Publications (step 5) | UNIQUE to C |

## Detailed Analysis

### Version A (TJS-002) — Conceptual State Model

```
Generated → Scheduled → Published → Updated → Archived → Removed
```

**Characteristics:**
- 6 explicit states
- State-based (publication exists in ONE state at a time)
- Includes "Scheduled" (no equivalent in B or C)
- Includes "Archived" as explicit state
- Does NOT include input/output
- Does NOT include time dimension

### Version B (TJS-007) — Operational Flow Model

```
Dataset → Render → Publish → Update → Retain/Remove
```

**Characteristics:**
- 5 stages (flow, not states)
- Flow-based (sequential processing)
- Includes input (Dataset) and output (Retain/Remove)
- "Render" is a PROCESS, not a state
- "Retain" is an OUTCOME, not a state
- Does NOT include time dimension
- Does NOT include "Scheduled" state

### Version C (TJS-008) — Temporal Cycle Model

```
1. Generation → 2. Publication → 3. Monitoring → 4. Updating → 5. Tomorrow generation → 6. Tomorrow removal
```

**Characteristics:**
- 6 steps (daily cycle)
- Time-based (24-hour operational cycle)
- Includes "Monitoring" (no equivalent in A or B)
- Includes "Tomorrow generation" (no equivalent in A or B)
- Does NOT include "Scheduled" state
- Does NOT include "Archived" state
- Focuses on WHAT happens WHEN, not WHAT state the publication is in

---

# Are They Describing the Same Concept?

**NO.** They describe THREE DIFFERENT aspects of the same system:

| Model | Describes | Analogy |
|-------|-----------|---------|
| Version A | What STATES a publication can be in | Traffic light colors |
| Version B | What PROCESS transforms data into publications | Assembly line stages |
| Version C | What HAPPENS during a 24-hour operational day | Daily schedule |

**These are NOT competing definitions of the same concept. They are three complementary views that SHOULD coexist in a single unified document.**

---

# Question 6: Recommended Canonical Lifecycle State Model

## Recommended Unified Model

The canonical Publication Lifecycle should contain THREE layers:

### Layer 1: Publication States (from TJS-002)

```
Generated → Published → Updated → Archived → Removed
```

**Note:** "Scheduled" is REMOVED from the canonical model because:
- It has no equivalent in TJS-007 or TJS-008
- It represents an implementation detail (scheduling), not a semantic state
- A publication is either Generated or Published — "Scheduled" is a transient state

### Layer 2: Processing Flow (from TJS-007)

```
Normalized Dataset → Render → Publish → Update (if required) → Retain or Remove
```

This is the OPERATIONAL view of how data becomes a publication.

### Layer 3: Daily Cycle (from TJS-008)

```
1. Generate Today's Package
2. Publish Today's Posts
3. Monitor Dataset updates
4. Update changed Publications
5. Generate Tomorrow Publications
6. Remove obsolete Tomorrow Publications
```

This is the TEMPORAL view of what happens during a 24-hour day.

## Recommendation

**DO NOT merge these into one model.** They serve different purposes:
- Layer 1 answers: "What state is this publication in?"
- Layer 2 answers: "How did this publication get created?"
- Layer 3 answers: "When does this happen during the day?"

A single unified document (TJS-005) should contain all three layers with clear labels:
- §X: Publication States (semantic)
- §Y: Processing Flow (operational)
- §Z: Daily Cycle (temporal)

---

# Lifecycle Semantic Verdict

| Question | Answer |
|----------|--------|
| How many lifecycle models exist? | 3 |
| Are they the same concept? | NO — 3 different aspects |
| Should they be merged into one model? | NO — they should coexist in one document |
| Is there ONE canonical lifecycle? | NOT YET — needs unification in TJS-005 |
| Recommended action | Create TJS-005 with all 3 layers clearly labeled |

---

**End of Lifecycle Semantic Audit**

**Auditor:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
