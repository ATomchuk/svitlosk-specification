# CASE001_PUBLICATION_STATE_MODEL

**Document ID:** CASE001B-STATE

**Title:** Publication — State Model

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document determines whether Publication ever exists simultaneously in multiple representations.

---

# Multiple Representations

## Representation 1: Publication Package

**What it is:** The collection of Publications for one Reporting Period.

**Evidence:**

- GLOSSARY.md §3: "The complete collection of Publications generated during one Reporting Period"
- TJS-010 §4.1: Publication Engine produces Publication Package

**Simultaneous with Publication?** YES

**Explanation:** Publication exists within Publication Package. They coexist.

---

## Representation 2: Telegram Message

**What it is:** The platform-specific artifact on Telegram.

**Evidence:**

- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message"
- TJS-010 §3.3: "Telegram Channel → Subscribers: Publication"

**Simultaneous with Publication?** YES

**Explanation:** Publication is displayed as Telegram Message. They coexist during Published state.

---

## Representation 3: Repository Object

**What it is:** The persisted data in Data Storage.

**Evidence:**

- TJS-021 §3.1: "Repository SHALL be the single authoritative source of truth"
- TJS-010 §4.7: Data Storage owns persistent storage

**Simultaneous with Publication?** YES

**Explanation:** Publication is stored in Repository. They coexist.

---

## Representation 4: Editorial Object

**What it is:** The editorial product following standards.

**Evidence:**

- TJS-020: Editorial System governs Publications
- TJS-005: Canonical Templates define structure

**Simultaneous with Publication?** YES

**Explanation:** Publication follows editorial standards. Editorial aspect coexists with other aspects.

---

## Representation 5: Lifecycle Object

**What it is:** The state machine governing Publication.

**Evidence:**

- TJS-021: Publication Lifecycle defines states and transitions
- TJS-021 §4: "Every Publication SHALL pass through one or more of the following states"

**Simultaneous with Publication?** YES

**Explanation:** Publication has lifecycle. Lifecycle aspect coexists with other aspects.

---

## Representation 6: Historical Object

**What it is:** The archived Publication in historical record.

**Evidence:**

- TJS-021 §4.4: "Archived Publications remain available in the Telegram Journal permanently"
- GLOSSARY.md §3: "Historical Archive — The persistent storage of historical Interpretation Results and Publications"

**Simultaneous with Publication?** YES

**Explanation:** Publication becomes historical record. Historical aspect coexists with other aspects.

---

# Are These Different Objects or Different Projections?

## Analysis

| Representation | Same Object? | Evidence |
|----------------|--------------|----------|
| Publication Package | YES | Publication exists within Package |
| Telegram Message | YES | Publication is displayed as Message |
| Repository Object | YES | Publication is stored in Repository |
| Editorial Object | YES | Publication follows editorial standards |
| Lifecycle Object | YES | Publication has lifecycle |
| Historical Object | YES | Publication becomes historical record |

---

## Conclusion

**These are DIFFERENT PROJECTIONS of one object, NOT different objects.**

**Evidence:**

1. **Same identity** — Territory + Date + Template persists across all representations
2. **Same content** — The information about power outages is the same
3. **Same lifecycle** — State changes propagate across all representations
4. **Same ownership** — Publication Engine owns Publication across all representations
5. **Transformation, not replacement** — Each representation transforms the PRESENTATION, not the CONCEPT

---

# Projection Model

```text
                    ┌─────────────────────────────────┐
                    │      CANONICAL PUBLICATION       │
                    │  (Territory + Date + Template)   │
                    └───────────────┬─────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
            ▼                       ▼                       ▼
    ┌───────────────┐      ┌───────────────┐      ┌───────────────┐
    │ Package View  │      │ Telegram View │      │ Repository    │
    │               │      │               │      │ View          │
    │ - Collection  │      │ - Message ID  │      │ - Database ID │
    │ - Ordering    │      │ - Bot API     │      │ - Persistence │
    └───────────────┘      └───────────────┘      └───────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
            ▼                       ▼                       ▼
    ┌───────────────┐      ┌───────────────┐      ┌───────────────┐
    │ Editorial     │      │ Lifecycle     │      │ Historical    │
    │ View          │      │ View          │      │ View          │
    │               │      │               │      │               │
    │ - Standards   │      │ - States      │      │ - Archive     │
    │ - Templates   │      │ - Transitions │      │ - Permanence  │
    └───────────────┘      └───────────────┘      └───────────────┘
```

---

# State Model Summary

| Representation | Coexists With Publication? | Same Object? |
|----------------|---------------------------|--------------|
| Publication Package | YES | YES — Projection |
| Telegram Message | YES | YES — Projection |
| Repository Object | YES | YES — Projection |
| Editorial Object | YES | YES — Projection |
| Lifecycle Object | YES | YES — Projection |
| Historical Object | YES | YES — Projection |

**All representations are projections of one Canonical Publication.**

---

# End of State Model
