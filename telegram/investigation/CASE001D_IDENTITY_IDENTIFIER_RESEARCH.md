# CASE001D_IDENTITY_IDENTIFIER_RESEARCH

**Document ID:** CASE001D-RESEARCH

**Title:** Identity vs Identifier — Foundational Research

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity vs Identifier Investigation

---

# Purpose

This document investigates the fundamental difference between Identity and Identifier within the SvitloSk domain.

---

# Part 1: Identity vs Identifier — Core Distinction

## Definition

**Identity** is WHAT an object IS — its essential nature that makes it "the same object" throughout its lifecycle.

**Identifier** is HOW an object is REFERRED TO — a label, key, or reference used to point to the object.

## Fundamental Difference

| Aspect | Identity | Identifier |
|--------|----------|------------|
| Nature | WHAT the object is | HOW the object is referred to |
| Existence | Exists independently of any reference | Exists only as a reference |
| Persistence | Persists across all representations | May change between representations |
| Uniqueness | One object = one identity | One object may have multiple identifiers |
| Dependence | Does not depend on external systems | May depend on external systems |
| Lifecycle | Survives edits, updates, migrations | May be created, changed, released |

---

# Part 2: Evidence from Repository

## Evidence E-001: Telegram Message ID Is Explicitly Called an "Identifier"

**Document:** TJS-000A §10

**Quote:** "Telegram Message ID — The platform identifier assigned to a published message in Telegram. This is a technical identifier, not a semantic concept."

**Analysis:** The repository explicitly distinguishes between "identifier" (Telegram Message ID) and "semantic concept" (Publication). This confirms that Identifier ≠ Identity.

---

## Evidence E-002: Publication Exists Before Identifier Is Assigned

**Document:** TJS-021 §4.1

**Quote:** "The state in which a Publication has been created from normalized data but has not yet been published to Telegram. A Generated Publication exists in the Repository but is not yet visible to readers."

**Analysis:** Publication (Identity) exists in Generated state before Telegram Message ID (Identifier) is assigned. This proves Identity exists independently of Identifier.

---

## Evidence E-003: Ownership Is Determined by Identifier, Not Identity

**Document:** Legacy TJS-007 §10

**Quote:** "Ownership SHALL be determined by the stored Telegram Message ID."

**Analysis:** The system uses Telegram Message ID (Identifier) to determine ownership, but this does not mean Telegram Message ID IS the identity. It is a mechanism for referencing the object.

---

## Evidence E-004: Publication Ownership Is Defined by Creation Method

**Document:** TELEGRAM_GLOSSARY.md §11

**Quote:** "Publication Ownership — The model determining which component owns which Publications. Ownership is determined by the stored Telegram Message ID."

**Analysis:** Ownership is determined by Identifier (Telegram Message ID), but Identity (what the Publication IS) is determined by Territory + Date + Template.

---

## Evidence E-005: Multiple Representations Share One Identity

**Document:** CASE001_PUBLICATION_STATE_MODEL.md

**Analysis:** Publication exists simultaneously as:
- Publication Package
- Telegram Message
- Repository Object
- Editorial Object
- Lifecycle Object
- Historical Record

All are DIFFERENT PROJECTIONS of ONE Identity. Each projection may have its own Identifier, but the Identity remains the same.

---

# Part 3: Identity Reconstruction

## For Every Object

### Publication

**Has Identity?** YES

**What creates it?** Publication Engine (Territory + Date + Template)

**When does it appear?** At creation (Generated state)

**Can it exist before Identifier?** YES — Publication exists before Telegram Message ID is assigned

**Can it survive Identifier changes?** YES — Identity persists when Telegram Message ID changes

**Can Identity disappear?** NO — Identity concept persists even after removal

**Can Identity split?** NO — one Publication = one Identity

**Can Identity merge?** NO — one Publication = one Identity

**Can Identity migrate?** YES — Identity can move between platforms

**Can Identity exist simultaneously in multiple representations?** YES — see Projection Analysis

---

### Issue

**Has Identity?** YES

**What creates it?** Editorial System (Calendar day)

**When does it appear?** When first Publication for a day is generated

**Can it exist before Identifier?** YES — Issue exists before any ID is assigned

**Can it survive Identifier changes?** YES — Identity persists

**Can Identity disappear?** NO — concept persists

**Can Identity split?** NO

**Can Identity merge?** NO

**Can Identity migrate?** YES

**Can Identity exist simultaneously in multiple representations?** YES

---

### Journal

**Has Identity?** YES

**What creates it?** Editorial System (Continuous publication)

**When does it appear?** At project start

**Can it exist before Identifier?** YES

**Can it survive Identifier changes?** YES

**Can Identity disappear?** NO

**Can Identity split?** NO

**Can Identity merge?** NO

**Can Identity migrate?** YES

**Can Identity exist simultaneously in multiple representations?** YES

---

### Territory

**Has Identity?** YES

**What creates it?** Real-world existence (Administrative boundaries)

**When does it appear?** Before SvitloSk

**Can it exist before Identifier?** YES — Territory exists before SvitloSk

**Can it survive Identifier changes?** YES

**Can Identity disappear?** NO — unless real-world boundaries change

**Can Identity split?** YES — territories can be reorganized

**Can Identity merge?** YES — territories can be combined

**Can Identity migrate?** NO — territory is location-specific

**Can Identity exist simultaneously in multiple representations?** YES

---

### Address

**Has Identity?** YES

**What creates it?** Official designation

**When does it appear?** Before SvitloSk

**Can it exist before Identifier?** YES

**Can it survive Identifier changes?** YES

**Can Identity disappear?** NO — unless address is officially changed

**Can Identity split?** NO

**Can Identity merge?** NO

**Can Identity migrate?** NO

**Can Identity exist simultaneously in multiple representations?** YES

---

### Telegram Message

**Has Identity?** NO — borrows Identity from Publication

**What creates it?** Telegram platform

**When does it appear?** At delivery

**Can it exist before Identifier?** NO — Telegram Message ID IS the Identifier

**Can it survive Identifier changes?** NO — Telegram Message ID is the Identifier

**Can Identity disappear?** YES — Telegram Message can be deleted

**Can Identity split?** NO

**Can Identity merge?** NO

**Can Identity migrate?** NO

**Can Identity exist simultaneously in multiple representations?** NO — Telegram Message is one representation

---

### Publication Package

**Has Identity?** NO — borrows Identity from Reporting Period

**What creates it?** Publication Engine

**When does it appear?** At generation

**Can it exist before Identifier?** YES — Package exists before any ID

**Can it survive Identifier changes?** YES

**Can Identity disappear?** NO

**Can Identity split?** NO

**Can Identity merge?** NO

**Can Identity migrate?** YES

**Can Identity exist simultaneously in multiple representations?** YES

---

### Normalized Dataset

**Has Identity?** YES — unique per retrieval

**What creates it?** Parser

**When does it appear?** At parsing

**Can it exist before Identifier?** YES

**Can it survive Identifier changes?** YES

**Can Identity disappear?** YES — consumed by Publication Engine

**Can Identity split?** NO

**Can Identity merge?** NO

**Can Identity migrate?** YES

**Can Identity exist simultaneously in multiple representations?** YES

---

# Part 4: Identifier Reconstruction

## For Every Identifier

### Telegram Message ID

**Who creates it?** Telegram platform

**Who owns it?** Telegram platform

**Can it change?** NO — immutable once assigned

**Can it be regenerated?** NO — unique per message

**Can multiple Identifiers represent one Identity?** YES — same Publication can have different Telegram Message IDs if re-published

**Can one Identifier represent different Identities?** NO — one Telegram Message ID = one Telegram Message

**Can Identifier disappear while Identity survives?** YES — Publication can exist without Telegram Message ID (Generated state)

**Can Identifier survive while Identity disappears?** NO — if Publication is removed, Telegram Message ID is released

---

### Document ID (DOC-XXX)

**Who creates it?** Repository governance

**Who owns it?** Repository governance

**Can it change?** NO — immutable

**Can it be regenerated?** NO — unique

**Can multiple Identifiers represent one Identity?** YES — document can have multiple IDs (DOC, TJS, SSP)

**Can one Identifier represent different Identities?** NO — one Document ID = one document

**Can Identifier disappear while Identity survives?** NO — document cannot exist without ID

**Can Identifier survive while Identity disappears?** NO — if document is deleted, ID is released

---

### ADR ID (ADR-XXX)

**Who creates it?** Repository governance

**Who owns it?** Repository governance

**Can it change?** NO — immutable

**Can it be regenerated?** NO — unique

**Can multiple Identifiers represent one Identity?** NO — one ADR = one ID

**Can one Identifier represent different Identities?** NO — one ADR ID = one ADR

**Can Identifier disappear while Identity survives?** NO

**Can Identifier survive while Identity disappears?** NO

---

### Document ID (TJS-XXX)

**Who creates it?** Repository governance

**Who owns it?** Repository governance

**Can it change?** NO — immutable

**Can it be regenerated?** NO — unique

**Can multiple Identifiers represent one Identity?** YES — TJS document can also have a filename

**Can one Identifier represent different Identities?** NO

**Can Identifier disappear while Identity survives?** NO

**Can Identifier survive while Identity disappears?** NO

---

### Session ID

**Who creates it?** Publication Engine

**Who owns it?** Publication Engine

**Can it change?** NO — immutable per session

**Can it be regenerated?** YES — new session = new ID

**Can multiple Identifiers represent one Identity?** YES — session can have multiple IDs

**Can one Identifier represent different Identities?** NO

**Can Identifier disappear while Identity survives?** YES — session ends, ID released

**Can Identifier survive while Identity disappears?** NO

---

# Part 5: Identity / Identifier Relationship Models

## Model A: Identity Creates Identifier

**Description:** Identity exists first, then Identifier is created to reference it.

**Evidence:** Publication (Identity) exists in Generated state before Telegram Message ID (Identifier) is assigned.

**Fit:** PARTIAL — fits Publication but not all objects.

---

## Model B: Identifier Creates Identity

**Description:** Identifier exists first, then Identity is created around it.

**Evidence:** Telegram Message — Identity is defined by the Identifier.

**Fit:** PARTIAL — fits Telegram Message but not Publication.

---

## Model C: Identity Independent from Identifier

**Description:** Identity exists independently of any Identifier.

**Evidence:** Publication exists before Telegram Message ID. Territory exists before SvitloSk.

**Fit:** GOOD — fits most objects.

---

## Model D: Identifier Is Only a Projection

**Description:** Identifier is one projection of Identity, not Identity itself.

**Evidence:** Publication has multiple projections (Telegram Message, Repository Object, etc.) each with own Identifier.

**Fit:** GOOD — fits most objects.

---

## Model E: Identity Equals Identifier

**Description:** Identity and Identifier are the same thing.

**Evidence:** Telegram Message — Identity IS the Telegram Message ID.

**Fit:** POOR — does not fit Publication, Territory, Address.

---

# Part 6: Projection Analysis

## Publication as Multiple Projections

**Projection 1: Publication Package**

- Same Identity? YES
- Different Identifier? YES (Package has no explicit ID)
- Same Object? YES — projection

**Projection 2: Telegram Message**

- Same Identity? YES
- Different Identifier? YES (Telegram Message ID)
- Same Object? YES — projection

**Projection 3: Repository Object**

- Same Identity? YES
- Different Identifier? YES (Database ID, implied)
- Same Object? YES — projection

**Projection 4: Editorial Object**

- Same Identity? YES
- Different Identifier? NO (no explicit ID)
- Same Object? YES — projection

**Projection 5: Historical Record**

- Same Identity? YES
- Different Identifier? YES (Archive reference)
- Same Object? YES — projection

**Conclusion:** All are DIFFERENT PROJECTIONS of ONE Identity.

---

# Part 7: Identity Timeline

## Following ONE Publication

| Stage | Identity | Identifier | Representation | Ownership | Lifecycle |
|-------|----------|------------|----------------|-----------|-----------|
| Birth | Territory + Date + Template | None | Repository | Publication Engine | Generated |
| Parser | Territory + Date + Template | None | Repository | Publication Engine | Generated |
| Publication Engine | Territory + Date + Template | None | Repository | Publication Engine | Generated |
| Storage | Territory + Date + Template | Database ID (implied) | Repository | Publication Engine | Generated |
| Telegram | Territory + Date + Template | Telegram Message ID | Telegram | Publication Engine | Published |
| Update | Territory + Date + Template | Telegram Message ID | Telegram | Publication Engine | Updated |
| Archive | Territory + Date + Template | Telegram Message ID | Historical | Publication Engine | Archived |
| Deletion | Territory + Date + Template | None | None | None | Removed |

---

# Part 8: Identity / Identifier Contradictions

## Contradiction 1: Identity Without Identifier

**Evidence:** Publication in Generated state has Identity (Territory + Date + Template) but no Identifier (no Telegram Message ID, no Database ID).

**Severity:** MEDIUM

**Possible Explanation:** Identity exists before Identifier is assigned.

---

## Contradiction 2: Identifier Without Identity

**Evidence:** Telegram Message has Identifier (Telegram Message ID) but borrows Identity from Publication.

**Severity:** LOW

**Possible Explanation:** Telegram Message is a projection, not an independent object.

---

## Contradiction 3: Multiple Identifiers for One Identity

**Evidence:** Publication can have multiple Identifiers: Telegram Message ID, Database ID (implied), Archive reference.

**Severity:** LOW

**Possible Explanation:** Multiple projections of one Identity, each with own Identifier.

---

## Contradiction 4: Identity Duplication

**Evidence:** Manual Publications and automated Publications can have same Territory + Date + Template.

**Severity:** MEDIUM

**Possible Explanation:** Manual Publications are a different Canonical concept with different ownership.

---

## Contradiction 5: Platform-Dependent Identity

**Evidence:** Telegram Message ID depends on Telegram platform.

**Severity:** MEDIUM

**Possible Explanation:** Telegram Message ID is an Identifier, not Identity.

---

## Contradiction 6: Repository-Dependent Identity

**Evidence:** Document IDs depend on repository governance.

**Severity:** LOW

**Possible Explanation:** Document IDs are Identifiers, not Identity.

---

# Part 9: Philosophical Consistency

## Ontological Order

**Question:** What exists first — Object, Identity, Identifier, or Representation?

**Evidence:**

- Publication (Object) exists first
- Identity (Territory + Date + Template) is created at birth
- Identifier (Telegram Message ID) is assigned later
- Representation (Telegram Message) is created at delivery

**Conclusion:** Object → Identity → Identifier → Representation

**But:** For Telegram Message, Identifier creates Identity (Telegram Message ID defines what the message IS).

**Conclusion:** Different objects have different ontological orders.

---

# Part 10: Open Questions

| # | Question | Impact |
|---|----------|--------|
| 1 | What is the precise relationship between Identity and Identifier? | HIGH |
| 2 | Can Identity exist without any Identifier? | HIGH |
| 3 | Can Identifier exist without any Identity? | MEDIUM |
| 4 | How do multiple Identifiers relate to one Identity? | MEDIUM |
| 5 | What happens to Identity when Identifier changes? | MEDIUM |
| 6 | What happens to Identifier when Identity changes? | LOW |
| 7 | Is Identity a property of the object or a property of the system? | LOW |
| 8 | Is Identifier a property of the object or a property of the system? | LOW |

---

# End of Identity vs Identifier Research
