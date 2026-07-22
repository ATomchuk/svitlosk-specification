# CASE001C_IDENTITY_RESEARCH

**Document ID:** CASE001C-RESEARCH

**Title:** Identity — Foundational Research

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity Investigation

---

# Purpose

This document provides foundational research on the concept of Identity within the SvitloSk domain. It studies what makes any domain object remain "the same object" throughout its lifecycle.

---

# Part 1: Identity Inventory

## Every Place Where Identity Is Defined or Implied

| # | Concept | Identity Mechanism | Source | Explicit? |
|---|---------|-------------------|--------|-----------|
| 1 | Publication | Territory + Date + Template | Reconstructed from TJS-005, TJS-006, Legacy TJS-007 §4 | IMPLICIT |
| 2 | Telegram Message ID | Platform identifier | TJS-000A §10 | EXPLICIT |
| 3 | Issue | Calendar day | TJS-000 §4, TJS-021 §8 | IMPLICIT |
| 4 | Journal | Continuous publication | TJS-000 §4 | IMPLICIT |
| 5 | Territory | Administrative name | TERRITORIAL_MODEL.md | EXPLICIT |
| 6 | Address | Official geographical location | GLOSSARY.md §4, DATA_MODEL.md | EXPLICIT |
| 7 | Publication Package | Reporting Period | GLOSSARY.md §3 | IMPLICIT |
| 8 | Lifecycle | State sequence | TJS-021 §4 | EXPLICIT |
| 9 | Session | One execution | Legacy TJS-008 §15 | EXPLICIT |
| 10 | Time Interval | Start + End time | GLOSSARY.md §5 | IMPLICIT |
| 11 | Parser output | Normalized Dataset | GLOSSARY.md §2 | IMPLICIT |
| 12 | Repository identifiers | Document ID | DOCUMENT_INDEX.md | EXPLICIT |
| 13 | ADR references | ADR ID | ADR-001 | EXPLICIT |
| 14 | Document identifiers | DOC-XXX | DOCUMENT_INDEX.md | EXPLICIT |
| 15 | Queue | Official queue identifier | GLOSSARY.md §5 | EXPLICIT |
| 16 | Subqueue | Official subqueue identifier | GLOSSARY.md §5 | EXPLICIT |
| 17 | Settlement | Official settlement name | TERRITORIAL_MODEL.md | EXPLICIT |
| 18 | Street | Official street name | TERRITORIAL_MODEL.md | EXPLICIT |
| 19 | Daily Snapshot | Reporting day | DATA_MODEL.md | IMPLICIT |
| 20 | Analytics Record | Historical dataset | DATA_MODEL.md | IMPLICIT |

---

# Part 2: Candidate Identity Models

## Model A — Technical Identity

**Definition:** Identity is assigned by the technical system (database ID, platform identifier).

**Examples:**

- Telegram Message ID
- Database primary key (implied)
- Session ID

**Evidence:**

- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message"
- Legacy TJS-007 §10: "Ownership SHALL be determined by the stored Telegram Message ID"

---

## Model B — Business Identity

**Definition:** Identity is determined by business meaning (what the object represents in the real world).

**Examples:**

- Territory (Administrative Centre or Starosta District)
- Address (official geographical location)
- Queue (official electricity distribution queue)

**Evidence:**

- GLOSSARY.md §4: "Territory — A publication unit representing either the Administrative Centre or one Starosta District"
- GLOSSARY.md §5: "Queue identifiers SHALL preserve their official representation"

---

## Model C — Editorial Identity

**Definition:** Identity is determined by editorial purpose (what role the object plays in the Journal).

**Examples:**

- Issue (one editorial edition for a calendar day)
- Publication (one independent publication belonging to an Issue)
- Publication Package (complete collection for one Reporting Period)

**Evidence:**

- TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"
- TJS-000 §4: "Publication represents one independent publication belonging to an Issue"

---

## Model D — Repository Identity

**Definition:** Identity is determined by repository governance (document IDs, ADR references).

**Examples:**

- DOC-000 (Charter)
- DOC-004 (Glossary)
- ADR-001 (Component vs Role)
- TJS-021 (Publication Lifecycle)

**Evidence:**

- DOCUMENT_INDEX.md: "Every normative document SHALL be registered in this index"
- DOCUMENT_INDEX.md: "Document identifiers SHALL be unique"

---

## Model E — Historical Identity

**Definition:** Identity is determined by temporal position (when the object existed).

**Examples:**

- Daily Snapshot (one reporting day)
- Historical Archive (persistent storage of historical records)
- Reporting Period (time interval for Publications)

**Evidence:**

- DATA_MODEL.md: "Daily Snapshot — Immutable representation of normalized operational information for one reporting day"
- GLOSSARY.md §2: "Historical Archive — The persistent storage of historical Interpretation Results and Publications"

---

## Model F — Platform Identity

**Definition:** Identity is determined by the platform (Telegram) where the object exists.

**Examples:**

- Telegram Message ID
- Telegram Channel
- Subscribers

**Evidence:**

- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message"
- TJS-000A §10: "Channel — The communication medium through which Publications are delivered"

---

## Model G — Lifecycle Identity

**Definition:** Identity is determined by the lifecycle state (what state the object is in).

**Examples:**

- Generated Publication
- Published Publication
- Updated Publication
- Archived Publication
- Removed Publication

**Evidence:**

- TJS-021 §4: "Every Publication SHALL pass through one or more of the following states"
- TJS-021 §5: Lifecycle transitions define state changes

---

# Part 3: Identity Criteria

## For Every Candidate Model

### Model A — Technical Identity

| Question | Answer |
|----------|--------|
| What creates identity? | System assignment (database ID, platform identifier) |
| What preserves identity? | Persistence in storage |
| What destroys identity? | Deletion from storage |
| Can identity change? | NO — technical IDs are immutable |
| Can identity split? | NO — one ID = one object |
| Can identity merge? | NO — one ID = one object |
| Can identity migrate? | YES — ID can move between systems |
| Can identity be regenerated? | NO — IDs are unique |
| Can identity survive edits? | YES — ID persists through edits |
| Can identity survive publication? | YES — ID persists through publication |
| Can identity survive deletion? | NO — ID is released on deletion |

### Model B — Business Identity

| Question | Answer |
|----------|--------|
| What creates identity? | Real-world existence (territory, address, queue) |
| What preserves identity? | Continued existence in the real world |
| What destroys identity? | Real-world ceases to exist |
| Can identity change? | NO — business identity is stable |
| Can identity split? | NO — one business object = one identity |
| Can identity merge? | NO — one business object = one identity |
| Can identity migrate? | NO — business identity is location-specific |
| Can identity be regenerated? | NO — business identity is unique |
| Can identity survive edits? | YES — edits don't change business meaning |
| Can identity survive publication? | YES — publication doesn't change business meaning |
| Can identity survive deletion? | NO — deletion removes business object |

### Model C — Editorial Identity

| Question | Answer |
|----------|--------|
| What creates identity? | Editorial decision (issue, publication, package) |
| What preserves identity? | Editorial consistency |
| What destroys identity? | Editorial removal |
| Can identity change? | NO — editorial identity is stable |
| Can identity split? | NO — one editorial object = one identity |
| Can identity merge? | NO — one editorial object = one identity |
| Can identity migrate? | NO — editorial identity is context-specific |
| Can identity be regenerated? | NO — editorial identity is unique |
| Can identity survive edits? | YES — edits don't change editorial meaning |
| Can identity survive publication? | YES — publication doesn't change editorial meaning |
| Can identity survive deletion? | NO — deletion removes editorial object |

### Model D — Repository Identity

| Question | Answer |
|----------|--------|
| What creates identity? | Repository governance (document registration) |
| What preserves identity? | Repository persistence |
| What destroys identity? | Repository removal |
| Can identity change? | NO — document IDs are immutable |
| Can identity split? | NO — one document = one ID |
| Can identity merge? | NO — one document = one ID |
| Can identity migrate? | YES — documents can move between repositories |
| Can identity be regenerated? | NO — IDs are unique |
| Can identity survive edits? | YES — ID persists through edits |
| Can identity survive publication? | YES — publication doesn't change ID |
| Can identity survive deletion? | NO — deletion removes document |

### Model E — Historical Identity

| Question | Answer |
|----------|--------|
| What creates identity? | Temporal position (day, period) |
| What preserves identity? | Historical persistence |
| What destroys identity? | Historical erasure |
| Can identity change? | NO — historical identity is fixed |
| Can identity split? | NO — one historical object = one identity |
| Can identity merge? | NO — one historical object = one identity |
| Can identity migrate? | NO — historical identity is time-specific |
| Can identity be regenerated? | NO — historical identity is unique |
| Can identity survive edits? | YES — edits don't change historical meaning |
| Can identity survive publication? | YES — publication doesn't change historical meaning |
| Can identity survive deletion? | NO — deletion removes historical object |

### Model F — Platform Identity

| Question | Answer |
|----------|--------|
| What creates identity? | Platform assignment (Telegram) |
| What preserves identity? | Platform persistence |
| What destroys identity? | Platform deletion |
| Can identity change? | NO — platform IDs are immutable |
| Can identity split? | NO — one platform object = one ID |
| Can identity merge? | NO — one platform object = one ID |
| Can identity migrate? | NO — platform identity is platform-specific |
| Can identity be regenerated? | NO — IDs are unique |
| Can identity survive edits? | YES — ID persists through edits |
| Can identity survive publication? | YES — publication doesn't change ID |
| Can identity survive deletion? | NO — deletion removes platform object |

### Model G — Lifecycle Identity

| Question | Answer |
|----------|--------|
| What creates identity? | Lifecycle state assignment |
| What preserves identity? | Lifecycle continuity |
| What destroys identity? | Lifecycle termination |
| Can identity change? | YES — lifecycle state changes |
| Can identity split? | NO — one object = one lifecycle |
| Can identity merge? | NO — one object = one lifecycle |
| Can identity migrate? | NO — lifecycle is object-specific |
| Can identity be regenerated? | NO — lifecycle is unique |
| Can identity survive edits? | YES — edits don't change lifecycle |
| Can identity survive publication? | YES — publication doesn't change lifecycle |
| Can identity survive deletion? | NO — deletion terminates lifecycle |

---

# Part 4: Identity Timeline

## Following One Publication From Birth to Archive

| Phase | Identity Before | Identity After | Changed? | External Added? | Internal Added? | Historical Added? |
|-------|-----------------|----------------|----------|-----------------|-----------------|-------------------|
| Creation | None | Territory + Date + Template | YES | NO | YES | NO |
| Delivery | Territory + Date + Template | Territory + Date + Template + Telegram Message ID | YES | YES | NO | NO |
| Active Life | Territory + Date + Template + Telegram Message ID | Territory + Date + Template + Telegram Message ID | NO | NO | NO | NO |
| Archival | Territory + Date + Template + Telegram Message ID | Territory + Date + Template + Telegram Message ID | NO | NO | NO | YES |

---

# Part 5: Identity Layers

| Layer | Object | Owns Identity? | Borrows Identity? |
|-------|--------|----------------|-------------------|
| Business | Business Object | YES — business meaning | NO |
| Information | Information Object | YES — informational content | NO |
| Document | Document | YES — document ID | NO |
| Publication | Publication | YES — Territory + Date + Template | NO |
| Telegram Message | Telegram Message | NO — borrows from Publication | YES |
| Publication Package | Publication Package | NO — borrows from Reporting Period | YES |
| Historical Record | Historical Record | NO — borrows from Publication | YES |
| Database Record | Database Record | NO — borrows from Publication | YES |
| Repository Artifact | Repository Artifact | YES — document ID | NO |

---

# Part 6: Identity Ownership

| Component | Owns Identity? | Evidence |
|-----------|---------------|----------|
| Parser | NO | Parser produces data, not identity |
| Publication Engine | **YES** | Publication Engine creates Publication with identity |
| Publisher Role | NO | Logical role, not identity owner |
| Telegram Publisher | NO | Delivery mechanism, not identity owner |
| Data Storage | NO | Persistence mechanism, not identity owner |
| Issue | NO | Container, not identity owner |
| Journal | NO | Ultimate container, not identity owner |

---

# Part 7: Identity Dependencies

| Identity | Depends On | Stable? |
|----------|------------|---------|
| Publication | Territory, Date, Template | YES — all are stable |
| Telegram Message ID | Telegram platform | NO — platform-specific |
| Issue | Calendar day | YES — calendar is stable |
| Journal | Continuous publication | YES — journal is permanent |
| Territory | Administrative boundaries | YES — boundaries are stable |
| Address | Official designation | YES — addresses are stable |
| Publication Package | Reporting Period | YES — periods are stable |
| Lifecycle | Object existence | YES — lifecycle tracks existence |
| Content | Normalized Dataset | NO — content can change |
| Metadata | Generation process | YES — metadata is stable |
| Time | Current time | NO — time is always changing |

---

# Part 8: Identity Invariants

## What NEVER Changes

| Invariant | Evidence |
|-----------|----------|
| Territory of a Publication | TJS-021 §6.1: "Every Publication SHALL represent exactly one Territory" |
| Date of a Publication | TJS-005: Templates define "Today" and "Tomorrow" variants |
| Template of a Publication | Legacy TJS-007 §4: "Every Publication SHALL use one Canonical Template" |
| Document ID of a specification | DOCUMENT_INDEX.md: "Document identifiers SHALL be unique" |
| ADR ID of an architecture decision | ADR-001: Document ID is stable |
| Territory name | TERRITORIAL_MODEL.md: "All project components SHALL derive territorial information exclusively from this model" |
| Address (official) | GLOSSARY.md §4: "Addresses SHALL be treated exactly as officially published" |
| Queue identifier | GLOSSARY.md §5: "Queue identifiers SHALL preserve their official representation" |
| Subqueue identifier | GLOSSARY.md §5: "Subqueue identifiers SHALL preserve their official representation" |

## What MAY Change

| Mutable | Evidence |
|---------|----------|
| Publication content | TJS-021 §5.2: "A Published Publication becomes Updated when the normalized dataset changes" |
| Publication lifecycle state | TJS-021 §5: Lifecycle transitions define state changes |
| Publication ownership | TJS-010 §4.1 vs Legacy TJS-007 §10: Ownership can change |
| Publication archive status | TJS-021 §5.4: "A Published Publication becomes Archived when the reporting period ends" |
| Telegram Message ID | Assigned at delivery, released at removal |
| Content | Changes when data changes |
| Lifecycle State | Changes through transitions |
| Archive Status | Changes at archival |

---

# Part 9: Identity Contradictions

## Contradiction IC-001: Publication ID Not Defined

**Evidence:**

- DATA_MODEL.md: "Every logical entity SHALL be uniquely identifiable"
- No explicit Publication ID defined in any specification
- Legacy TJS-007 §10 mentions Telegram Message ID

**Severity:** HIGH

**Possible Explanation:** Publication identity is Territory + Date + Template (reconstructed), not explicitly defined.

---

## Contradiction IC-002: Telegram Message ID as Identity

**Evidence:**

- Legacy TJS-007 §10: "Ownership SHALL be determined by the stored Telegram Message ID"
- TJS-000A §10: "Telegram Message ID — The platform identifier assigned to a published message"
- But Publication exists before Telegram Message ID is assigned (Generated state)

**Severity:** MEDIUM

**Possible Explanation:** Telegram Message ID is an external reference, not intrinsic identity.

---

## Contradiction IC-003: Identity vs Relationship

**Evidence:**

- TJS-000 §4: "Publication represents one independent publication belonging to an Issue"
- TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated"
- Circular dependency between Publication and Issue

**Severity:** MEDIUM

**Possible Explanation:** Issue membership is a relationship, not identity. Circular dependency is temporal, not identity-based.

---

## Contradiction IC-004: Platform Independence vs Platform Identity

**Evidence:**

- TJS-000 §3: "Telegram itself SHALL NOT be considered the Journal"
- TJS-000 §3: "The Journal exists independently from any publication platform"
- But Telegram Message ID is part of identity model

**Severity:** MEDIUM

**Possible Explanation:** Canonical Publication is platform-independent; Telegram View is platform-specific.

---

# Part 10: Open Questions

## Unresolved Questions

| # | Question | Impact |
|---|----------|--------|
| 1 | What is the precise identity criteria for Publication? | HIGH |
| 2 | Is there an internal Publication ID? | HIGH |
| 3 | How does identity survive platform migration? | MEDIUM |
| 4 | What happens to identity when Publication is replaced? | MEDIUM |
| 5 | Can two Publications have the same identity? | MEDIUM |
| 6 | How is identity verified across components? | MEDIUM |
| 7 | What is the relationship between identity and traceability? | LOW |
| 8 | How does identity interact with the Repository Authority Principle? | LOW |

---

# End of Identity Research
