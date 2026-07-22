# CASE001_PUBLICATION_BOUNDARIES

**Document ID:** CASE001-PUB-005

**Title:** Publication — Boundary Analysis

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Semantic Investigation №001

---

# Purpose

This document determines what is NOT Publication and explains why.

---

# Concepts That Are NOT Publication

## B-001: Publication Package

**What it is:** The complete collection of Publications generated during one Reporting Period.

**Why it is NOT Publication:**

- GLOSSARY.md: "The complete collection of Publications generated during one Reporting Period"
- It CONTAINS Publications but IS NOT a Publication
- It is an aggregation, not a unit
- It has no individual content — only collective content

**Evidence:** GLOSSARY.md §3, TJS-000A §9

---

## B-002: Issue

**What it is:** One editorial edition of the Journal for a single calendar day.

**Why it is NOT Publication:**

- TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"
- Issue CONTAINS Publications but IS NOT a Publication
- It is a temporal container, not a content unit
- It has no individual content — only collective content

**Evidence:** TJS-000 §4, TJS-000A §8

---

## B-003: Journal

**What it is:** The continuous informational publication of the SvitloSk project.

**Why it is NOT Publication:**

- TJS-000 §4: "Journal represents the continuous informational publication"
- Journal CONTAINS Issues which CONTAIN Publications
- It is the ultimate container, not a unit
- It has no individual content — only collective content

**Evidence:** TJS-000 §4, TJS-000A §8

---

## B-004: Telegram Message

**What it is:** The platform-specific artifact created when a Publication is delivered to Telegram.

**Why it is NOT Publication:**

- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message in Telegram. This is a technical identifier, not a semantic concept."
- Telegram Message is the PLATFORM representation, not the SEMANTIC concept
- It is an implementation detail, not a domain concept
- It is tied to Telegram, while Publication is platform-independent

**Evidence:** TJS-000A §10, TJS-000 §3

---

## B-005: Graphic

**What it is:** A visual element that may accompany a Publication.

**Why it is NOT Publication:**

- TJS-022 defines Graphic Publications as a TYPE of Publication
- However, a standalone Graphic (not part of a Publication) is NOT a Publication
- Graphics are visual elements, not information units
- They are produced by Graphic Generator, not Publication Engine

**Evidence:** TJS-022, TJS-010 §4.6

---

## B-006: Schedule

**What it is:** Logical representation of electricity availability for one operational period.

**Why it is NOT Publication:**

- DATA_MODEL.md: "Schedules SHALL reference one Subqueue"
- Schedule is INPUT to Publication, not Publication itself
- It is raw data, not interpreted information
- It is produced by Schedule Generator, not Publication Engine

**Evidence:** DATA_MODEL.md, TJS-010 §4.5

---

## B-007: Channel

**What it is:** The communication medium through which Publications are delivered.

**Why it is NOT Publication:**

- TJS-000A §10: "Channel — The communication medium through which Publications are delivered"
- Channel is the DELIVERY MECHANISM, not the CONTENT
- It is infrastructure, not domain concept
- It can exist without Publications (empty channel)

**Evidence:** TJS-000A §10, GLOSSARY.md §3

---

## B-008: Editorial Decision

**What it is:** A normative rule governing publication behavior.

**Why it is NOT Publication:**

- TJS-020 defines Editorial System as governing Publications
- Editorial decisions are RULES, not CONTENT
- They are meta-level, not object-level
- They shape Publications but are not Publications

**Evidence:** TJS-020, GLOSSARY.md §3

---

## B-009: Publication Window

**What it is:** The time windows during which the Publication Engine operates.

**Why it is NOT Publication:**

- TJS-000A: "Publication Windows — The time windows during which the Publication Engine operates"
- Windows are TEMPORAL CONSTRAINTS, not content
- They are operational parameters, not domain objects
- They exist without any Publication being created

**Evidence:** TJS-000A, Legacy TJS-008 §6

---

## B-010: Normalized Dataset

**What it is:** The direct machine-readable representation of information produced by the Parser.

**Why it is NOT Publication:**

- GLOSSARY.md: "Parsed Data SHALL correspond exactly to the retrieved Open Data"
- Normalized Dataset is INPUT, not OUTPUT
- It is raw data, not interpreted information
- It exists before Publication is created

**Evidence:** GLOSSARY.md §2, TJS-010 §3.3

---

## B-011: Interpretation Result

**What it is:** The normalized information produced by the Interpretation process.

**Why it is NOT Publication:**

- GLOSSARY.md: "Interpretation Results become input for Publication generation"
- Interpretation Result is INPUT, not OUTPUT
- It is intermediate, not final
- It exists before Publication is created

**Evidence:** GLOSSARY.md §2, TJS-010 §3.3

---

## B-012: Manual Publication

**What it is:** A Publication created manually by administrators, outside the automated lifecycle.

**Why it is NOT Publication (in the canonical sense):**

- TJS-000A: "Manual Publications — Publications created manually by administrators, outside the automated lifecycle"
- It is explicitly EXCLUDED from automatic lifecycle management
- It is created by different actor (administrators vs Publication Engine)
- It has different lifecycle rules

**However:** It IS still called a "Publication" — it is a different KIND of Publication.

**Evidence:** TJS-000A, TJS-010 §5.1, Legacy TJS-008 §13

---

## B-013: Image Publication

**What it is:** Visual publications published manually, outside the automatic lifecycle.

**Why it is NOT Publication (in the canonical sense):**

- TJS-000A: "Image Publications — Visual publications published manually, outside the automatic lifecycle"
- It is explicitly EXCLUDED from automatic lifecycle management
- It is created by different actor
- It has different lifecycle rules

**However:** It IS still called a "Publication" — it is a different KIND of Publication.

**Evidence:** TJS-000A, TJS-010 §5.1, Legacy TJS-008 §14

---

# Boundary Summary

| Concept | Is Publication? | Reason |
|---------|----------------|--------|
| Publication Package | NO | Aggregation of Publications |
| Issue | NO | Temporal container of Publications |
| Journal | NO | Ultimate container of all Issues |
| Telegram Message | NO | Platform implementation detail |
| Graphic | NO | Visual element (unless part of Graphic Publication) |
| Schedule | NO | Input data, not output |
| Channel | NO | Delivery mechanism, not content |
| Editorial Decision | NO | Rule, not content |
| Publication Window | NO | Temporal constraint, not content |
| Normalized Dataset | NO | Input data, not output |
| Interpretation Result | NO | Intermediate data, not final |
| Manual Publication | DIFFERENT KIND | Excluded from automatic lifecycle |
| Image Publication | DIFFERENT KIND | Excluded from automatic lifecycle |

---

# End of Document
