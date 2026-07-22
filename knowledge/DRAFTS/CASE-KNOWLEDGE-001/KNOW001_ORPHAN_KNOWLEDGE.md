# KNOW001_ORPHAN_KNOWLEDGE

**Document ID:** CASE-KNOWLEDGE-001-OK

**Title:** Orphan Knowledge

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document finds knowledge that exists only inside CASE folders.

---

# 2. Orphan Knowledge

## 2.1 Orphan: Three Independent Domains

### Location

CASE-SVT-ONTO001, CASE-INFPROD-001, CASE-TG-CORE-001

### Risk

HIGH — This is a FUNDAMENTAL architectural concept.

If lost, future work may re-derive it.

### Candidate for Canonicalization

YES — Should be in ARCHITECTURE.md or DATA_MODEL.md.

---

## 2.2 Orphan: Publisher as Executor

### Location

CASE-PUB-004, CASE-PUB-005

### Risk

HIGH — This is a FUNDAMENTAL architectural insight.

If lost, future work may assume Publisher is decision maker.

### Candidate for Canonicalization

YES — Should be in GLOSSARY.md or ARCHITECTURE.md.

---

## 2.3 Orphan: Lifecycle as Pattern

### Location

CASE-LC-001, CASE-PUB-004

### Risk

HIGH — This affects lifecycle placement.

If lost, future work may assume lifecycle is owned by a component.

### Candidate for Canonicalization

YES — Should be in GLOSSARY.md or ARCHITECTURE.md.

---

## 2.4 Orphan: Information/Knowledge/Data Separation

### Location

CASE-INF-001

### Risk

HIGH — This is a FUNDAMENTAL concept separation.

If lost, future work may conflate these concepts.

### Candidate for Canonicalization

YES — Should be in GLOSSARY.md.

---

## 2.5 Orphan: 27 Business Rules

### Location

CASE-PUB-005

### Risk

MEDIUM — These rules define Publisher behavior.

If lost, future work may reinvent them.

### Candidate for Canonicalization

YES — Should be in specification.

---

## 2.6 Orphan: 6 Information Products

### Location

CASE-INFPROD-001

### Risk

MEDIUM — These define what Publisher produces.

If lost, future work may redefine products.

### Candidate for Canonicalization

YES — Should be in DATA_MODEL.md.

---

## 2.7 Orphan: 10 Candidate Canonical Rules

### Location

CASE-PUB-005

### Risk

MEDIUM — These are stable rules for specification.

If lost, future work may miss them.

### Candidate for Canonicalization

YES — Should be in specification.

---

## 2.8 Orphan: Semantic Vocabulary (45 terms)

### Location

CASE-PUB-003

### Risk

MEDIUM — This defines terminology.

If lost, future work may create inconsistent terminology.

### Candidate for Canonicalization

YES — Should be in GLOSSARY.md.

---

# 3. Orphan Knowledge Summary

| Knowledge | Risk | Candidate for Canonicalization |
|-----------|------|-------------------------------|
| Three Independent Domains | HIGH | YES |
| Publisher as Executor | HIGH | YES |
| Lifecycle as Pattern | HIGH | YES |
| Information/Knowledge/Data Separation | HIGH | YES |
| 27 Business Rules | MEDIUM | YES |
| 6 Information Products | MEDIUM | YES |
| 10 Candidate Canonical Rules | MEDIUM | YES |
| Semantic Vocabulary | MEDIUM | YES |

---

# 4. Findings

## 4.1 Finding OK-001

**8 orphan knowledge items identified.**

4 are HIGH risk, 4 are MEDIUM risk.

**Evidence:** Analysis of orphan knowledge.

**Confidence:** HIGH.

## 4.2 Finding OK-002

**ALL orphan knowledge is a CANDIDATE for canonicalization.**

None should be lost.

**Evidence:** Analysis of orphan knowledge.

**Confidence:** HIGH.

## 4.3 Finding OK-003

**HIGH risk orphans relate to FUNDAMENTAL concepts.**

Three domains, Publisher role, lifecycle pattern, concept separation.

**Evidence:** Analysis of orphan knowledge.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OK-001 | Analysis of orphan knowledge |
| OK-002 | Analysis of orphan knowledge |
| OK-003 | Analysis of orphan knowledge |

---

**End of Orphan Knowledge**
