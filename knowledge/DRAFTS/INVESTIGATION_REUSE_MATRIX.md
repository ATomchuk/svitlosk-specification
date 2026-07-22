# Investigation Reuse Matrix

**Document Class:** Knowledge Freeze

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document maps knowledge reuse across investigations.

---

# Reuse Matrix

| Investigation | Knowledge Extracted | Used Later In | Can Become Canonical | Needs Revalidation | Historical Only |
|---------------|---------------------|---------------|----------------------|--------------------|--------------------|
| CASE-PUB-001 | Publication architecture, Journal Release, Publishing Kernel | CASE-PUB-002, CASE-PUB-003, CASE-PUB-004 | YES | NO | NO |
| CASE-PUB-002 | Telegram operations, Publisher responsibilities | CASE-PUB-003, CASE-PUB-004, CASE-TG-CORE-001 | YES | NO | NO |
| CASE-PUB-003 | Terminology normalization | — | YES | NO | NO |
| CASE-PUB-004 | Decision model, Events, Decision makers | CASE-PUB-005 | YES | PARTIALLY | NO |
| CASE-PUB-005 | Business rules, 17 rules | — | YES | NO | NO |
| CASE-JRN-001 | Journal ontology, Journal Edition | CASE-INFPROD-001 | YES | NO | NO |
| CASE-SVT-ONTOLOGY-001 | SvitloSk ontology, Three domains | CASE-INFPROD-001, CASE-TG-CORE-001 | YES | NO | NO |
| CASE-INF-001 | Information ontology, 20 objects | CASE-JRN-001, CASE-LC-001, CASE-SYS-001 | YES | NO | NO |
| CASE-LC-001 | Lifecycle ontology, Pattern concept | CASE-SYS-001 | YES | NO | NO |
| CASE-SYS-001 | System composition, 35 objects | — | YES | NO | NO |
| CASE-SRC-001 | Source audit, 22 sources | — | YES | NO | NO |
| CASE-INFPROD-001 | Information products, 6 products | CASE-TG-CORE-001 | YES | NO | NO |
| CASE-TG-CORE-001 | Telegram core, 21 operations | — | YES | NO | NO |
| CASE-KNOWLEDGE-001 | Knowledge persistence, 71% draft | CASE-KNOWLEDGE-002 | YES | NO | NO |
| CASE-KNOWLEDGE-002 | Canonical knowledge, 15 items | — | YES | NO | NO |
| CASE-GAP-001 | Gap discovery, 84 gaps | CASE-GAP-OWNERSHIP-001 | YES | NO | NO |
| CASE-GAP-OWNERSHIP-001 | Gap ownership, 84 ownerships | — | YES | NO | NO |
| CASE-HISTORY-001 | Historical evolution, 5 versions | — | YES | NO | NO |
| CASE-DOCARCH-001 | Documentation architecture, 26 documents | — | YES | NO | NO |
| CASE-KNOWLEDGE-REUSE-001 | Knowledge reuse, 8 items | — | YES | NO | NO |
| CASE-DOMAIN-AUDIT-001 | Domain completeness, 40 entities | CASE-ONTOLOGY-LEVELS-001, CASE-ENTITY-NATURE-001 | YES | NO | NO |
| CASE-ONTOLOGY-LEVELS-001 | Architectural levels, 12 levels | CASE-METAMODEL-001 | YES | NO | NO |
| CASE-ENTITY-NATURE-001 | Entity nature, 16 entities | CASE-METAMODEL-001 | YES | NO | NO |
| CASE-METAMODEL-001 | Meta-model, 14 categories | CASE-FALSIFICATION-001 | YES | NO | NO |
| CASE-FALSIFICATION-001 | Falsified ontology, 14 categories | — | YES | NO | NO |

---

# Reuse Summary

| Category | Count |
|----------|-------|
| Total Investigations | 25 |
| Knowledge Can Become Canonical | 25 |
| Knowledge Needs Revalidation | 1 |
| Knowledge Historical Only | 0 |

---

# Traceability

| Reuse | Source |
|-------|--------|
| All reuse | Analysis of all CASE investigations |

---

**End of Investigation Reuse Matrix**
