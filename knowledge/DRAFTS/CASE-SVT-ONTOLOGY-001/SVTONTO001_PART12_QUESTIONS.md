# SVTONTO001_PART12_QUESTIONS

**Document ID:** CASE-SVT-ONTOLOGY-001-P12

**Title:** Open Questions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document lists all unresolved questions from the CASE-SVT-ONTOLOGY-001 investigation.

---

# 2. Open Questions

## 2.1 OQ-001: Parser Architecture

**Question:** Does SvitloSk have ONE Parser or TWO independent Parsers?

**Evidence:**
- GLOSSARY: Single Parser component
- Architect Intent: Two independent parsers (Parser A, Parser B)

**Importance:** HIGH — affects architectural decomposition.

**Dependencies:** None.

---

## 2.2 OQ-002: Journal Primacy

**Question:** Is Journal the PRIMARY channel, or are all channels equal?

**Evidence:**
- CHARTER.md §10: "primary public communication channel"
- Architect Intent: "Telegram and Facebook are PEER adapters. Neither is primary."

**Importance:** HIGH — affects the role of Journal.

**Dependencies:** None.

---

## 2.3 OQ-003: Telegram Centrality

**Question:** Is the specification Telegram-centric or channel-independent?

**Evidence:**
- GLOSSARY: "Telegram Journal", "Telegram Journal Specifications"
- Architect Intent: "Publishing Subsystem. NOT Telegram."

**Importance:** HIGH — affects the entire specification structure.

**Dependencies:** OQ-002.

---

## 2.4 OQ-004: PWA Role

**Question:** Is PWA a publication channel or a Queue Schedule-specific application?

**Evidence:**
- ARCHITECTURE.md: "Supported publication channels include: PWA"
- Architect Intent: "PWA application is primarily built around this domain [Queue Schedule]"

**Importance:** MEDIUM — affects the role of PWA.

**Dependencies:** None.

---

## 2.5 OQ-005: Publication Scope

**Question:** Is Publication universal across all domains, or specific to Journal?

**Evidence:**
- GLOSSARY.md §3: "for distribution through one or more supported communication channels"
- Architect Intent: "Push notifications belong ONLY to Queue Schedule"

**Importance:** MEDIUM — affects the scope of Publication.

**Dependencies:** None.

---

## 2.6 OQ-006: Journal Edition vs Issue

**Question:** Are Journal Edition and Issue synonyms?

**Evidence:**
- Architect Intent: "journal edition"
- TELEGRAM_PUBLICATION_LIFECYCLE.md: "Issue"

**Importance:** MEDIUM — affects terminology.

**Dependencies:** None.

---

## 2.7 OQ-007: Journal Edition vs Publication Package

**Question:** Are Journal Edition and Publication Package synonyms?

**Evidence:**
- Architect Intent: "journal edition"
- GLOSSARY.md §3: "Publication Package"

**Importance:** MEDIUM — affects terminology.

**Dependencies:** OQ-006.

---

## 2.8 OQ-008: Release Validity

**Question:** Is Release a valid concept, or an artifact of previous investigations?

**Evidence:**
- CASE-PUB-001: "Release is a COMPOSITE ENTITY"
- GLOSSARY, CHARTER, Architect Intent: No mention of "Release"

**Importance:** LOW — affects terminology.

**Dependencies:** None.

---

## 2.9 OQ-009: Push Notification Scope

**Question:** Can Push Notifications be extended to other domains in the future?

**Evidence:**
- Architect Intent: "Push notifications belong ONLY to Queue Schedule"

**Importance:** LOW — affects future extensibility.

**Dependencies:** None.

---

## 2.10 OQ-010: Journal Contains Queue Graph

**Question:** Does Journal contain only the "tomorrow queue graph" or the full Queue Schedule?

**Evidence:**
- Architect Intent: "tomorrow queue graph" is one item in Journal
- Architect Intent: PWA displays full Queue Schedule

**Importance:** LOW — affects Journal scope.

**Dependencies:** OQ-004.

---

# 3. Question Priority

## 3.1 High Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-001 | Parser Architecture | Affects architectural decomposition |
| OQ-002 | Journal Primacy | Affects the role of Journal |
| OQ-003 | Telegram Centrality | Affects the entire specification |

## 3.2 Medium Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-004 | PWA Role | Affects the role of PWA |
| OQ-005 | Publication Scope | Affects the scope of Publication |
| OQ-006 | Journal Edition vs Issue | Affects terminology |
| OQ-007 | Journal Edition vs Publication Package | Affects terminology |

## 3.3 Low Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-008 | Release Validity | Affects terminology |
| OQ-009 | Push Notification Scope | Affects future extensibility |
| OQ-010 | Journal Contains Queue Graph | Affects Journal scope |

---

# 4. Question Dependencies

```
OQ-002 (Journal Primacy) ← OQ-003 (Telegram Centrality)

OQ-006 (Journal Edition vs Issue) ← OQ-007 (Journal Edition vs Publication Package)
```

---

# 5. Findings

## 5.1 Finding OQ-001

**Ten open questions were identified during the investigation.**

Three are high priority, four are medium priority, three are low priority.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 5.2 Finding OQ-002

**The highest priority questions relate to Parser architecture, Journal primacy, and Telegram centrality.**

These questions affect the fundamental architecture.

**Evidence:** GLOSSARY, CHARTER, Architect Intent.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OQ-001 | Analysis of all evidence sources |
| OQ-002 | GLOSSARY, CHARTER, Architect Intent |

---

**End of Open Questions**
