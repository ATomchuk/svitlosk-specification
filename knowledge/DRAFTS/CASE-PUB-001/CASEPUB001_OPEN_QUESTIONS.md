# CASEPUB001_OPEN_QUESTIONS

**Document ID:** CASE-PUB-001-OQ

**Title:** Open Questions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document lists all unresolved questions from the CASE-PUB-001 investigation.

Following Research Method V1.0, these questions guide future research.

---

# 2. Open Questions

## 2.1 OQ-001: Journal Release Identity Granularity

**Question:** What is the precise identity of a Journal Release?

**Evidence:**
- Journal Release has composite identity: Reporting Period + Territory Set
- But what happens when a Journal Release is updated?
- Does the version change? Does the identity change?

**Importance:** HIGH — affects lifecycle state management.

**Dependencies:** Requires lifecycle definition.

---

## 2.2 OQ-002: Temporary Publication Lifecycle

**Question:** How do temporary Publications (tomorrow information) interact with the Journal Release lifecycle?

**Evidence:**
- User context: "Planned outage publication (tomorrow) — temporary information which disappears before the end of current day"
- This implies temporary Publications have a different lifecycle than permanent Publications

**Importance:** HIGH — affects lifecycle transitions.

**Dependencies:** Requires lifecycle definition.

---

## 2.3 OQ-003: Graph Publication Identity

**Question:** Is the Graph of planned power schedule for tomorrow a separate entity or part of the Journal Release?

**Evidence:**
- User context: "Graph of planned power schedule for tomorrow (12 subqueues, only when such graph exists)"
- The graph is a visual representation, not a text Publication
- It may be a separate entity or a special type of Publication

**Importance:** MEDIUM — affects Journal Release structure.

**Dependencies:** Requires domain analysis.

---

## 2.4 OQ-004: Channel Adapter Interface

**Question:** What is the interface between the Publishing Kernel and Channel Adapters?

**Evidence:**
- KERNEL-004 Finding: "The Publishing Kernel would distribute Journal Releases to channel adapters"
- But the interface is not defined

**Importance:** MEDIUM — affects architecture definition.

**Dependencies:** Requires Publishing Kernel definition.

---

## 2.5 OQ-005: Facebook Channel Requirements

**Question:** What are the specific requirements for the Facebook channel?

**Evidence:**
- User context: "Facebook will become another communication channel"
- But no Facebook-specific requirements are documented

**Importance:** MEDIUM — affects multi-channel architecture.

**Dependencies:** Requires Facebook channel analysis.

---

## 2.6 OQ-006: PWA Channel Relationship

**Question:** How does the PWA (Progressive Web Application) relate to the Journal Release?

**Evidence:**
- ARCHITECTURE.md mentions PWA as a publication channel
- But PWA operates independently around 12 electrical subqueues
- The relationship between PWA and Journal Release is unclear

**Importance:** MEDIUM — affects architecture understanding.

**Dependencies:** Requires PWA architecture analysis.

---

## 2.7 OQ-007: Publication Rendering vs Distribution

**Question:** Is rendering part of the Publishing Kernel or part of the Channel Adapter?

**Evidence:**
- TELEGRAM_PUBLISHING_CANONICAL_MODEL.md: "Publication Engine — Transforms normalized dataset into deterministic Publication Package"
- This implies rendering is part of the Publication Engine
- But rendering may be channel-specific

**Importance:** MEDIUM — affects responsibility allocation.

**Dependencies:** Requires architecture decision.

---

## 2.8 OQ-008: Journal Release Update Semantics

**Question:** When a Journal Release is updated, what happens to existing Representations in channels?

**Evidence:**
- TELEGRAM_PUBLICATION_LIFECYCLE.md: "Updates SHOULD modify existing Publications instead of replacing them"
- But this is Telegram-specific
- How do other channels handle updates?

**Importance:** MEDIUM — affects lifecycle design.

**Dependencies:** Requires multi-channel analysis.

---

## 2.9 OQ-009: Archive Scope

**Question:** Does the Archive store Journal Releases or Publications?

**Evidence:**
- GLOSSARY.md: "Historical Archive: The persistent storage of historical Interpretation Results and Publications"
- But Journal Releases are collections of Publications
- Which level is archived?

**Importance:** LOW — affects storage design.

**Dependencies:** Requires archive design.

---

## 2.10 OQ-010: Sequence Numbering

**Question:** Are Journal Releases sequentially numbered?

**Evidence:**
- Identity analysis suggests Journal Release has ordinal identity (sequence)
- But no evidence of sequence numbering in current specs

**Importance:** LOW — affects identity design.

**Dependencies:** Requires identity definition.

---

# 3. Question Priority

## 3.1 High Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-001 | Journal Release Identity Granularity | Affects lifecycle state management |
| OQ-002 | Temporary Publication Lifecycle | Affects lifecycle transitions |

## 3.2 Medium Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-003 | Graph Publication Identity | Affects Journal Release structure |
| OQ-004 | Channel Adapter Interface | Affects architecture definition |
| OQ-005 | Facebook Channel Requirements | Affects multi-channel architecture |
| OQ-006 | PWA Channel Relationship | Affects architecture understanding |
| OQ-007 | Publication Rendering vs Distribution | Affects responsibility allocation |
| OQ-008 | Journal Release Update Semantics | Affects lifecycle design |

## 3.3 Low Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-009 | Archive Scope | Affects storage design |
| OQ-010 | Sequence Numbering | Affects identity design |

---

# 4. Question Dependencies

```
OQ-001 (Identity) ← OQ-002 (Temporary Lifecycle)
                  ← OQ-008 (Update Semantics)

OQ-004 (Adapter Interface) ← OQ-005 (Facebook Requirements)
                           ← OQ-006 (PWA Relationship)

OQ-007 (Rendering vs Distribution) ← OQ-004 (Adapter Interface)
```

---

# 5. Findings

## 5.1 Finding OQ-001

**Ten open questions were identified during the investigation.**

Two are high priority, six are medium priority, two are low priority.

**Evidence:** Analysis of all investigation documents.

**Confidence:** HIGH.

## 5.2 Finding OQ-002

**The highest priority questions relate to Journal Release identity and temporary Publication lifecycle.**

These questions affect the core lifecycle design.

**Evidence:** OQ-001, OQ-002.

**Confidence:** HIGH.

## 5.3 Finding OQ-003

**Several questions relate to multi-channel architecture.**

These questions will need resolution when Facebook channel is implemented.

**Evidence:** OQ-004, OQ-005, OQ-006, OQ-007, OQ-008.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OQ-001 | Analysis of all investigation documents |
| OQ-002 | OQ-001, OQ-002 |
| OQ-003 | OQ-004, OQ-005, OQ-006, OQ-007, OQ-008 |

---

**End of Open Questions**
