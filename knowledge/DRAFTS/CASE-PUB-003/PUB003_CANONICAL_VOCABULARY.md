# PUB003_CANONICAL_VOCABULARY

**Document ID:** CASE-PUB-003-CV

**Title:** Candidate Canonical Vocabulary

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs candidate canonical vocabulary.

---

# 2. Candidate Canonical Vocabulary

## 2.1 Core Concepts

| Current Term | Alternative Term | Observed Meaning | Observed Conflicts |
|--------------|------------------|------------------|-------------------|
| Publisher | — | Logical Role | May confuse with human Publisher |
| Publication | Information Product | Information message | Overlaps with Information Product |
| Publication Package | Journal Edition | Collection for one day | Edition is undefined |
| Journal | — | Ongoing service | — |
| Journal Edition | Issue, Release | Daily instance | Three potential synonyms |

---

## 2.2 Telegram-Specific

| Current Term | Alternative Term | Observed Meaning | Observed Conflicts |
|--------------|------------------|------------------|-------------------|
| Telegram Journal | — | Telegram channel | — |
| Telegram Publisher | — | Telegram implementation | — |
| Telegram Message | — | Telegram output | — |
| Telegram Post | — | Social media output | — |

---

## 2.3 Information Products

| Current Term | Alternative Term | Observed Meaning | Observed Conflicts |
|--------------|------------------|------------------|-------------------|
| Information Product | — | Discrete unit of information | Overlaps with Publication |
| Emergency Outage Publication | — | Product type | — |
| Planned Outage Publication | — | Product type | — |
| Queue Graph Publication | — | Product type | — |
| Technical Publication | — | Product type | — |
| Service Publication | — | Product type | — |

---

## 2.4 Lifecycle

| Current Term | Alternative Term | Observed Meaning | Observed Conflicts |
|--------------|------------------|------------------|-------------------|
| Generated | Created | Publication created | — |
| Published | Delivered | Publication delivered | — |
| Updated | Modified | Publication modified | — |
| Archived | Preserved | Publication preserved | — |
| Removed | Deleted | Publication deleted | — |
| Expired | Ended | Temporary ended | — |

---

## 2.5 Representation

| Current Term | Alternative Term | Observed Meaning | Observed Conflicts |
|--------------|------------------|------------------|-------------------|
| Representation | Output | Channel-specific output | — |
| Formatted Message | — | Intermediate output | — |
| Rendered Message | — | Intermediate output | — |

---

## 2.6 Identity

| Current Term | Alternative Term | Observed Meaning | Observed Conflicts |
|--------------|------------------|------------------|-------------------|
| Publication Identity | — | Unique identifier | — |
| Territory | — | Geographic unit | — |
| Reporting Period | — | Temporal unit | — |
| Domain | — | Information domain | — |

---

# 3. Vocabulary Completeness

## 3.1 Well-Defined Terms

| Term | Status | Source |
|------|--------|--------|
| Publisher | DEFINED | GLOSSARY §3 |
| Publication | DEFINED | GLOSSARY §3 |
| Publication Package | DEFINED | GLOSSARY §3 |
| Journal | DEFINED | CHARTER §10 |
| Territory | DEFINED | GLOSSARY §4 |
| Reporting Period | DEFINED | GLOSSARY §2 |

## 3.2 Partially Defined Terms

| Term | Status | Source |
|------|--------|--------|
| Journal Edition | USED | Architect Intent |
| Issue | USED | TELEGRAM_LIFECYCLE |
| Release | USED | CASE-PUB-001 |
| Information Product | USED | CASE-INFPROD-001 |

## 3.3 Undefined Terms

| Term | Status | Source |
|------|--------|--------|
| Representation | USED | CASE-INF-001 |
| Formatted Message | USED | CASE-TG-CORE-001 |
| Rendered Message | USED | CASE-TG-CORE-001 |

---

# 4. Findings

## 4.1 Finding CV-001

**26 terms in candidate vocabulary.**

Across 6 categories.

**Evidence:** Analysis of canonical vocabulary.

**Confidence:** HIGH.

## 4.2 Finding CV-002

**6 terms are WELL-DEFINED.**

Publisher, Publication, Publication Package, Journal, Territory, Reporting Period.

**Evidence:** Analysis of vocabulary completeness.

**Confidence:** HIGH.

## 4.3 Finding CV-003

**4 terms are PARTIALLY DEFINED.**

Journal Edition, Issue, Release, Information Product.

**Evidence:** Analysis of vocabulary completeness.

**Confidence:** HIGH.

## 4.4 Finding CV-004

**3 terms are UNDEFINED.**

Representation, Formatted Message, Rendered Message.

**Evidence:** Analysis of vocabulary completeness.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| CV-001 | Analysis of canonical vocabulary |
| CV-002 | Analysis of vocabulary completeness |
| CV-003 | Analysis of vocabulary completeness |
| CV-004 | Analysis of vocabulary completeness |

---

**End of Candidate Canonical Vocabulary**
