# INF001_PART12_QUESTIONS

**Document ID:** CASE-INF-001-P12

**Title:** Open Questions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document lists all unresolved questions from the CASE-INF-001 investigation.

---

# 2. Open Questions

## 2.1 OQ-001: Parser Architecture

**Question:** Does SvitloSk have ONE Parser or TWO independent Parsers?

**Evidence:**
- GLOSSARY: Single Parser component
- Architect Intent: Two independent parsers

**Importance:** HIGH — affects information acquisition.

**Dependencies:** None.

---

## 2.2 OQ-002: Information Flow Count

**Question:** Does SvitloSk have ONE information flow or THREE independent flows?

**Evidence:**
- GLOSSARY: Single Processing Cycle
- Architect Intent: Three independent domains with different flows

**Importance:** HIGH — affects information architecture.

**Dependencies:** OQ-001.

---

## 2.3 OQ-003: Publication Scope

**Question:** Is Publication universal across all domains, or specific to Journal?

**Evidence:**
- GLOSSARY §3: "for distribution through one or more supported communication channels"
- Architect Intent: Queue Schedule uses PWA Timeline, not Publications

**Importance:** MEDIUM — affects the scope of Publication.

**Dependencies:** None.

---

## 2.4 OQ-004: Channel Ownership

**Question:** Do channels own information, or do they receive representations?

**Evidence:**
- GLOSSARY §3: "Telegram Journal: The official public communication channel..."
- Architect Intent: "Telegram and Facebook DO NOT own information."

**Importance:** MEDIUM — affects the information model.

**Dependencies:** None.

---

## 2.5 OQ-005: Journal Primacy

**Question:** Is Journal the PRIMARY product, or are PWA and Journal equal?

**Evidence:**
- CHARTER §10: "primary public communication channel"
- Architect Intent: "The PWA visualizes primarily Domain A."

**Importance:** MEDIUM — affects product hierarchy.

**Dependencies:** None.

---

## 2.6 OQ-006: Knowledge Layer

**Question:** Is Knowledge a separate layer from Information?

**Evidence:**
- CHARTER §1, §2: "analyses, interprets, transforms"
- GLOSSARY §2: "Interpretation: The process of transforming structured information into information understandable for residents"

**Importance:** MEDIUM — affects information model.

**Dependencies:** None.

---

## 2.7 OQ-007: Information vs Data

**Question:** Is Information distinct from Data?

**Evidence:**
- GLOSSARY §2: "Data Model: The structured internal representation of Parsed Data"
- CHARTER §7: "SvitloSk does not modify open data"

**Importance:** MEDIUM — affects information model.

**Dependencies:** None.

---

## 2.8 OQ-008: Address Lookup Scope

**Question:** Does Address Lookup bridge all three domains, or only Domains B/C to Domain A?

**Evidence:**
- Architect Intent: "Address Lookup: Allows resident to determine which subqueue serves their address"

**Importance:** LOW — affects cross-domain relationships.

**Dependencies:** None.

---

## 2.9 OQ-009: Tomorrow Information Expiry

**Question:** Does ALL tomorrow information expire, or only specific types?

**Evidence:**
- Architect Intent: "tomorrow queue graph" and "planned outages (tomorrow)" are temporary
- Architect Intent: "emergency outages (tomorrow)" — status unclear

**Importance:** LOW — affects persistence rules.

**Dependencies:** None.

---

## 2.10 OQ-010: Technical Messages Domain

**Question:** Do Technical Messages belong to a specific domain, or are they cross-domain?

**Evidence:**
- Architect Intent: "technical messages" are listed as Journal content

**Importance:** LOW — affects domain classification.

**Dependencies:** None.

---

# 3. Question Priority

## 3.1 High Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-001 | Parser Architecture | Affects information acquisition |
| OQ-002 | Information Flow Count | Affects information architecture |

## 3.2 Medium Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-003 | Publication Scope | Affects scope of Publication |
| OQ-004 | Channel Ownership | Affects information model |
| OQ-005 | Journal Primacy | Affects product hierarchy |
| OQ-006 | Knowledge Layer | Affects information model |
| OQ-007 | Information vs Data | Affects information model |

## 3.3 Low Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-008 | Address Lookup Scope | Affects cross-domain relationships |
| OQ-009 | Tomorrow Information Expiry | Affects persistence rules |
| OQ-010 | Technical Messages Domain | Affects domain classification |

---

# 4. Question Dependencies

```
OQ-001 (Parser Architecture) → OQ-002 (Information Flow Count)
```

---

# 5. Findings

## 5.1 Finding OQ-001

**Ten open questions were identified during the investigation.**

Two are high priority, five are medium priority, three are low priority.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

## 5.2 Finding OQ-002

**The highest priority questions relate to Parser architecture and information flow count.**

These questions affect the fundamental information model.

**Evidence:** GLOSSARY, Architect Intent.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OQ-001 | Analysis of all evidence sources |
| OQ-002 | GLOSSARY, Architect Intent |

---

**End of Open Questions**
