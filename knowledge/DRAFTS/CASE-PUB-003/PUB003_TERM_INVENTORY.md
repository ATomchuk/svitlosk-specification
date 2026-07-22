# PUB003_TERM_INVENTORY

**Document ID:** CASE-PUB-003-TI

**Title:** Term Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document collects every term currently used around Publisher.

---

# 2. Term Inventory

## 2.1 Core Publisher Terms

| Term | Source | Context |
|------|--------|---------|
| Publisher | GLOSSARY | Logical Role |
| Publication Engine | GLOSSARY | Software Component |
| Publication | GLOSSARY | Information message |
| Publication Package | GLOSSARY | Collection of Publications |
| Publication Pipeline | GLOSSARY | Processing stages |
| Publication Channel | GLOSSARY | Communication medium |
| Publication Lifecycle | GLOSSARY | Lifecycle of Publication |
| Publisher Role | GLOSSARY | Logical responsibility |
| Publishing Subsystem | Architect Intent | Common subsystem |

---

## 2.2 Telegram-Specific Terms

| Term | Source | Context |
|------|--------|---------|
| Telegram Journal | GLOSSARY | Channel |
| Telegram Publisher | TELEGRAM_PUB | Implementation |
| Telegram Channel | TELEGRAM_PUB | Delivery |
| Telegram Message | TELEGRAM_PUB | Output |
| Telegram Post | Architect Intent | Output |
| Telegram Bot API | TELEGRAM_PUB | Interface |

---

## 2.3 Information Product Terms

| Term | Source | Context |
|------|--------|---------|
| Information Product | CASE-INFPROD-001 | Product concept |
| Emergency Outage Publication | CASE-INFPROD-001 | Product type |
| Planned Outage Publication | CASE-INFPROD-001 | Product type |
| Queue Graph Publication | CASE-INFPROD-001 | Product type |
| Technical Publication | CASE-INFPROD-001 | Product type |
| Service Publication | CASE-INFPROD-001 | Product type |

---

## 2.4 Lifecycle Terms

| Term | Source | Context |
|------|--------|---------|
| Generated | TELEGRAM_LIFECYCLE | State |
| Published | TELEGRAM_LIFECYCLE | State |
| Updated | TELEGRAM_LIFECYCLE | State |
| Archived | TELEGRAM_LIFECYCLE | State |
| Removed | TELEGRAM_LIFECYCLE | State |
| Expired | Architect Intent | Temporary state |

---

## 2.5 Representation Terms

| Term | Source | Context |
|------|--------|---------|
| Representation | CASE-INF-001 | Channel-specific output |
| Formatted Message | CASE-TG-CORE-001 | Intermediate output |
| Rendered Message | CASE-TG-CORE-001 | Intermediate output |
| Image File | CASE-TG-CORE-001 | Binary output |

---

## 2.6 Process Terms

| Term | Source | Context |
|------|--------|---------|
| Rendering | GLOSSARY | Conversion process |
| Distribution | GLOSSARY | Delivery process |
| Formatting | CASE-TG-CORE-001 | Text formatting |
| Generation | CASE-TG-CORE-001 | Creation process |
| Transformation | CASE-TG-CORE-001 | Data transformation |

---

## 2.7 Identity Terms

| Term | Source | Context |
|------|--------|---------|
| Journal Edition | Architect Intent | Daily container |
| Issue | TELEGRAM_LIFECYCLE | Daily edition |
| Release | CASE-PUB-001 | Composite entity |
| Edition | Architect Intent | Daily edition |

---

## 2.8 Domain Terms

| Term | Source | Context |
|------|--------|---------|
| Queue Schedule | Architect Intent | Domain A |
| Planned Outages | Architect Intent | Domain B |
| Emergency Outages | Architect Intent | Domain C |
| Territory | GLOSSARY | Geographic unit |
| Starosta District | GLOSSARY | Territorial subdivision |

---

# 3. Term Count

| Category | Count |
|----------|-------|
| Core Publisher | 9 |
| Telegram-Specific | 6 |
| Information Product | 6 |
| Lifecycle | 6 |
| Representation | 4 |
| Process | 5 |
| Identity | 4 |
| Domain | 5 |
| **Total** | **45** |

---

# 4. Findings

## 4.1 Finding TI-001

**There are 45 terms currently used.**

Across 8 categories.

**Evidence:** Analysis of all sources.

**Confidence:** HIGH.

## 4.2 Finding TI-002

**Some terms appear in multiple contexts.**

Publication, Message, Post may overlap.

**Evidence:** Analysis of term inventory.

**Confidence:** HIGH.

## 4.3 Finding TI-003

**Some terms are undefined.**

Release, Edition, Journal Release are not in GLOSSARY.

**Evidence:** Analysis of term inventory.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| TI-001 | Analysis of all sources |
| TI-002 | Analysis of term inventory |
| TI-003 | Analysis of term inventory |

---

**End of Term Inventory**
