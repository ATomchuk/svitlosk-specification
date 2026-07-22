# CASEJRN001_OPEN_QUESTIONS

**Document ID:** CASE-JRN-001-OQ

**Title:** Open Questions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document lists all unresolved questions from the CASE-JRN-001 investigation.

Following Research Method V1.0, these questions guide future research.

---

# 2. Open Questions

## 2.1 OQ-001: Journal Ontological Category

**Question:** What is the ontological category of Journal?

**Evidence:**
- CHARTER.md §1: "SvitloSk is an information service..."
- CHARTER.md §10: "Journal is the primary public communication channel..."
- CHARTER.md §10: "It serves as a public archive..."

**Analysis:**
Journal is described as Service, Channel, and Archive — which are different categories.

**Importance:** HIGH — affects the entire ontology.

**Dependencies:** None.

---

## 2.2 OQ-002: Journal Continuity

**Question:** Does Journal exist continuously, or only during publication?

**Evidence:**
- CHARTER.md §10: "Journal is the primary public communication channel..."
- Channels typically exist continuously.

**Analysis:**
If Journal is a channel, it may exist continuously.

If Journal is a service, it may only exist when active.

**Importance:** HIGH — affects the identity of Journal.

**Dependencies:** OQ-001.

---

## 2.3 OQ-003: Journal Without Publications

**Question:** Can Journal exist without Publications?

**Evidence:**
- CHARTER.md §10: "It serves as a public archive of processed information, daily publications..."

**Analysis:**
If Journal is an archive, it can exist without current Publications (only historical ones).

If Journal is a service, it may not exist without active Publications.

**Importance:** HIGH — affects the identity of Journal.

**Dependencies:** OQ-001.

---

## 2.4 OQ-004: Smallest Indivisible Object

**Question:** What is the smallest indivisible object inside Journal?

**Evidence:**
- GLOSSARY.md §3: "Publication: A public information message..."

**Analysis:**
Publication is defined as a "message," which is typically atomic.

But could Publications be decomposed into smaller units?

**Importance:** MEDIUM — affects the atomicity of the ontology.

**Dependencies:** None.

---

## 2.5 OQ-005: Issue Identity

**Question:** What is the identity of Issue — temporal or editorial?

**Evidence:**
- TELEGRAM_PUBLICATION_LIFECYCLE.md: "An Issue opens when the first Publication for a calendar day is generated."
- TELEGRAM_PUBLICATION_LIFECYCLE.md: "The Issue represents one editorial edition..."

**Analysis:**
Issue is defined both temporally (daily) and editorially (one edition).

Which is the primary identity?

**Importance:** MEDIUM — affects the identity of Issue.

**Dependencies:** None.

---

## 2.6 OQ-006: Release Existence

**Question:** Does Release exist as a canonical concept?

**Evidence:**
- User context: "One Journal Release may contain..."
- GLOSSARY.md: No definition of "Release."

**Analysis:**
Release is used in user context but not defined in canonical documents.

Is Release a valid concept, or should it be replaced by Issue?

**Importance:** MEDIUM — affects the terminology.

**Dependencies:** OQ-005.

---

## 2.7 OQ-007: Issue vs Release

**Question:** Are Issue and Release synonyms, or do they represent different concepts?

**Evidence:**
- TELEGRAM_PUBLICATION_LIFECYCLE.md: "Issue"
- User context: "Release"

**Analysis:**
Both refer to "one edition of the Journal for one day."

But Release may have additional characteristics (territory organization).

**Importance:** MEDIUM — affects the terminology.

**Dependencies:** OQ-006.

---

## 2.8 OQ-008: Publication Atomicity

**Question:** Is Publication truly atomic, or is it a composite of smaller units?

**Evidence:**
- GLOSSARY.md §3: "Publication: A public information message..."

**Analysis:**
A message is typically atomic.

But Publications may contain multiple data points (outages, addresses, times).

**Importance:** LOW — affects the granularity of the ontology.

**Dependencies:** OQ-004.

---

## 2.9 OQ-009: Reporting Period Flexibility

**Question:** Is Reporting Period always temporal, or can it also be content-based?

**Evidence:**
- GLOSSARY.md §2: "Reporting Period: The time interval for which Publications are generated."

**Analysis:**
Reporting Period is defined as a "time interval."

But could Reporting Period also be defined by content (e.g., "all emergency publications")?

**Importance:** LOW — affects the flexibility of the ontology.

**Dependencies:** None.

---

## 2.10 OQ-010: Territory Flexibility

**Question:** Is Territory always spatial, or can it also be content-based?

**Evidence:**
- GLOSSARY.md §4: "Territory: A publication unit representing either: the Administrative Centre; one Starosta District."

**Analysis:**
Territory is defined as a "publication unit" representing geographic areas.

But could Territory also be defined by content (e.g., "all planned outage publications")?

**Importance:** LOW — affects the flexibility of the ontology.

**Dependencies:** None.

---

# 3. Question Priority

## 3.1 High Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-001 | Journal Ontological Category | Affects the entire ontology |
| OQ-002 | Journal Continuity | Affects the identity of Journal |
| OQ-003 | Journal Without Publications | Affects the identity of Journal |

## 3.2 Medium Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-004 | Smallest Indivisible Object | Affects the atomicity of the ontology |
| OQ-005 | Issue Identity | Affects the identity of Issue |
| OQ-006 | Release Existence | Affects the terminology |
| OQ-007 | Issue vs Release | Affects the terminology |

## 3.3 Low Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-008 | Publication Atomicity | Affects the granularity of the ontology |
| OQ-009 | Reporting Period Flexibility | Affects the flexibility of the ontology |
| OQ-010 | Territory Flexibility | Affects the flexibility of the ontology |

---

# 4. Question Dependencies

```
OQ-001 (Journal Category) ← OQ-002 (Continuity)
                         ← OQ-003 (Without Publications)

OQ-006 (Release Existence) ← OQ-007 (Issue vs Release)

OQ-004 (Smallest Object) ← OQ-008 (Publication Atomicity)
```

---

# 5. Findings

## 5.1 Finding OQ-001

**Ten open questions were identified during the investigation.**

Three are high priority, four are medium priority, three are low priority.

**Evidence:** Analysis of all investigation documents.

**Confidence:** HIGH.

## 5.2 Finding OQ-002

**The highest priority questions relate to the ontological category of Journal.**

Journal is described as Service, Channel, and Archive — which are different categories.

**Evidence:** CHARTER.md §1, §10.

**Confidence:** HIGH.

## 5.3 Finding OQ-003

**Several questions relate to the identity and existence of concepts.**

Issue, Release, and Publication have unclear identity and existence.

**Evidence:** TELEGRAM_PUBLICATION_LIFECYCLE.md, GLOSSARY.md §3, User context.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OQ-001 | CHARTER.md §1, §10 |
| OQ-002 | TELEGRAM_PUBLICATION_LIFECYCLE.md, GLOSSARY.md §3, User context |
| OQ-003 | All investigation documents |

---

**End of Open Questions**
