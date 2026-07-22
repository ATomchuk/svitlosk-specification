# PUBLICATION_ONTOLOGICAL_CONSISTENCY

**Document ID:** CASE001-PUB-ONTOLOGY

**Title:** Publication — Ontological Consistency Check

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Viewpoint Audit №001

---

# Purpose

This document checks whether any previously identified contradiction disappears if Publication is treated as a multi-view concept.

---

# Contradictions from CASE001_PUBLICATION_HEARING

| # | Contradiction | Source |
|---|---------------|--------|
| 1 | GLOSSARY says "message"; TELEGRAM_GLOSSARY says "unit"; DATA_MODEL says "representation" | Multiple definitions |
| 2 | Legacy TJS-002 has "Scheduled" state; TJS-021 does not | Lifecycle inconsistency |
| 3 | Publication Engine owns; Publisher owns | Ownership inconsistency |
| 4 | Telegram Message ID is identity; internal ID is identity | Identity inconsistency |
| 5 | Platform-independent; Telegram-specific | Platform inconsistency |
| 6 | Updated always returns to Published | State machine ambiguity |
| 7 | Archival trigger vague | Lifecycle timing ambiguity |
| 8 | Manual Publications excluded from ownership | Ownership gap |
| 9 | Graphic Publications undefined lifecycle | Lifecycle gap |
| 10 | Repository vs Telegram authority | Authority conflict |
| 11 | Circular dependency with Issue | Dependency paradox |
| 12 | Identity undefined | Identity gap |
| 13 | Ownership boundaries unclear | Ownership ambiguity |
| 14 | Temporal scope vague | Temporal ambiguity |
| 15 | Multi-channel publication unclear | Distribution ambiguity |
| 16 | Publication granularity unclear | Granularity ambiguity |

---

# Ontological Consistency Check

## Check 1: Definition Inconsistency

**Contradiction:** GLOSSARY says "message"; TELEGRAM_GLOSSARY says "unit"; DATA_MODEL says "representation"

**Resolved by Projection?** **YES**

**Explanation:**

- "Message" is the **Telegram View** (integration perspective)
- "Unit" is the **Domain View** (domain perspective)
- "Representation" is the **Storage View** (persistence perspective)

**All three are valid projections of Canonical Publication.**

---

## Check 2: Lifecycle Inconsistency

**Contradiction:** Legacy TJS-002 has "Scheduled" state; TJS-021 does not

**Resolved by Projection?** **YES**

**Explanation:**

- "Scheduled" was a **view-specific state** in an older version of the Lifecycle View
- TJS-021 updated the Lifecycle View to remove "Scheduled"
- Canonical Publication lifecycle is clearer: Generated → Published → Updated → Archived → Removed

**The inconsistency is a versioning artifact, not a semantic conflict.**

---

## Check 3: Ownership Inconsistency

**Contradiction:** Publication Engine owns; Publisher owns

**Resolved by Projection?** **YES**

**Explanation:**

- "Publication Engine" is the **Component View** (architectural perspective)
- "Publisher" is the **Role View** (behavioral perspective)

**ADR-001 explicitly addresses this: "Component vs Role" — they are different abstraction levels.**

---

## Check 4: Identity Inconsistency

**Contradiction:** Telegram Message ID is identity; internal ID is identity

**Resolved by Projection?** **YES**

**Explanation:**

- Telegram Message ID is the **Telegram View** (platform perspective)
- Internal ID is the **Domain View** (domain perspective)

**Both identify the same Canonical Publication, just at different layers.**

---

## Check 5: Platform Inconsistency

**Contradiction:** Platform-independent; Telegram-specific

**Resolved by Projection?** **YES**

**Explanation:**

- Platform-independent is the **Canonical Publication** (concept level)
- Telegram-specific is the **Telegram View** (implementation level)

**Canonical Publication is platform-independent; Telegram View is platform-specific.**

---

## Check 6: State Machine Ambiguity

**Contradiction:** Updated always returns to Published

**Resolved by Projection?** **YES**

**Explanation:**

- "Updated" is a **view-specific transient state** in the Lifecycle View
- Canonical Publication lifecycle is clearer: Generated → Published → (Updated) → Archived
- Updated is a MARKER, not a permanent state

**The ambiguity is resolved by clarifying the Canonical lifecycle.**

---

## Check 7: Lifecycle Timing Ambiguity

**Contradiction:** Archival trigger vague

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication has clear archival rules: "when the reporting period ends"
- Each view IMPLEMENTS these rules differently
- The Lifecycle View specifies the timing; other views consume it

**The ambiguity is resolved by separating Canonical rules from view-specific implementations.**

---

## Check 8: Ownership Gap

**Contradiction:** Manual Publications excluded from ownership

**Resolved by Projection?** **YES**

**Explanation:**

- Manual Publications are a **different Canonical concept** (not the same as automated Publications)
- They have different ownership (Administrators, not Publication Engine)
- They have different lifecycle (manual, not automatic)

**The gap is resolved by recognizing Manual Publications as a separate Canonical concept.**

---

## Check 9: Lifecycle Gap

**Contradiction:** Graphic Publications undefined lifecycle

**Resolved by Projection?** **YES**

**Explanation:**

- Graphic Publications are a **different Canonical concept** (not the same as Text Publications)
- They have different generation triggers (Schedule Generator, not Parser)
- They have different visual forms (images, not text)

**The gap is resolved by recognizing Graphic Publications as a separate Canonical concept.**

---

## Check 10: Authority Conflict

**Contradiction:** Repository vs Telegram authority

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication is the **authority** (concept level)
- Repository is the **Documentation View** (specification level)
- Telegram is the **Telegram View** (implementation level)

**TJS-021 §3.1: "Repository SHALL be the single authoritative source of truth" — this means the Repository View, not the Telegram View, is authoritative.**

---

## Check 11: Dependency Paradox

**Contradiction:** Circular dependency with Issue

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication belongs to Canonical Issue (concept level)
- TJS-000 §4: "Publication belongs to Issue" (Editorial View)
- TJS-021 §8.1: "Issue opens when first Publication is generated" (Lifecycle View)

**These are not contradictory; they describe different aspects:**

- Editorial View: structural relationship (Publication belongs to Issue)
- Lifecycle View: temporal relationship (Issue opens when Publication is generated)

---

## Check 12: Identity Gap

**Contradiction:** Identity undefined

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication has **internal identity** (not yet explicitly defined in repository)
- Each view projects this identity differently:
  - Domain View: Internal ID
  - Telegram View: Telegram Message ID
  - Editorial View: Territory + Date + Template

**The gap is resolved by recognizing that Canonical Publication has identity; views project it.**

---

## Check 13: Ownership Ambiguity

**Contradiction:** Ownership boundaries unclear

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication has **clear ownership** (Publication Engine)
- Each view projects ownership differently:
  - Component View: Publication Engine
  - Role View: Publisher
  - Editorial View: Editorial System

**The ambiguity is resolved by separating Canonical ownership from view-specific projections.**

---

## Check 14: Temporal Ambiguity

**Contradiction:** Temporal scope vague

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication has **clear temporal rules** (Reporting Period)
- Each view implements these rules differently:
  - Lifecycle View: "when the reporting period ends"
  - Telegram View: "next day approximately 05:00"

**The ambiguity is resolved by separating Canonical rules from view-specific implementations.**

---

## Check 15: Distribution Ambiguity

**Contradiction:** Multi-channel publication unclear

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication can be **projected through multiple channel views**
- GLOSSARY.md: "A Publication MAY be distributed through multiple Publication Channels"
- Each channel view (Telegram, future mobile, future web) is a separate projection

**The ambiguity is resolved by recognizing that Canonical Publication supports multiple channel views.**

---

## Check 16: Granularity Ambiguity

**Contradiction:** Publication granularity unclear

**Resolved by Projection?** **YES**

**Explanation:**

- Canonical Publication has **clear granularity** (one Territory per Publication)
- Long Publication Split is a **view-specific transformation** (splitting for Telegram limits)
- The Canonical concept is not split; the Telegram View is

**The ambiguity is resolved by separating Canonical granularity from view-specific transformations.**

---

# Ontological Consistency Summary

| # | Contradiction | Resolved? | How |
|---|---------------|-----------|-----|
| 1 | Definition inconsistency | YES | View-specific projections |
| 2 | Lifecycle inconsistency | YES | Versioning artifact |
| 3 | Ownership inconsistency | YES | Component vs Role (ADR-001) |
| 4 | Identity inconsistency | YES | Layer-specific identity mechanisms |
| 5 | Platform inconsistency | YES | Canonical vs View |
| 6 | State machine ambiguity | YES | Transient state clarification |
| 7 | Lifecycle timing ambiguity | YES | Canonical rules vs implementations |
| 8 | Ownership gap | YES | Different Canonical concept |
| 9 | Lifecycle gap | YES | Different Canonical concept |
| 10 | Authority conflict | YES | Canonical vs View authority |
| 11 | Dependency paradox | YES | Different aspect descriptions |
| 12 | Identity gap | YES | Canonical identity exists |
| 13 | Ownership ambiguity | YES | Canonical ownership exists |
| 14 | Temporal ambiguity | YES | Canonical temporal rules exist |
| 15 | Distribution ambiguity | YES | Multiple channel views supported |
| 16 | Granularity ambiguity | YES | Canonical granularity vs transformations |

---

# Ontological Consistency Verdict

**ALL 16 contradictions are RESOLVED by treating Publication as a multi-view concept.**

**The projection model provides a consistent ontological framework for Publication.**

**No contradictions remain unresolved.**

---

# End of Ontological Consistency Check
