# Persistence Requirement

**Document Class:** Entity Nature Investigation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines persistence requirement for each entity.

---

# Persistence Requirement

## Permanent Entities

| Entity | Nature | Persistence | Evidence |
|--------|--------|-------------|----------|
| Journal | SERVICE | Permanent | CHARTER §10 |
| Publisher | SERVICE + ROLE | Permanent | GLOSSARY §7 |
| Publication | ARTIFACT | Permanent | GLOSSARY §3 |
| Lifecycle | PATTERN | Permanent | CASE-LC-001 |
| Territory | REFERENCE | Permanent | GLOSSARY §4 |
| Information | CONCEPT | Permanent | CASE-INF-001 |
| Knowledge | CONCEPT | Permanent | CASE-INF-001 |
| Open Data | CONCEPT | Permanent | GLOSSARY §2 |
| Parser | SERVICE | Permanent | GLOSSARY §2 |
| Archive | SERVICE | Permanent | GLOSSARY §2 |
| Channel | SERVICE | Permanent | GLOSSARY §3 |
| Adapter | SERVICE + ROLE | Permanent | CASE-SVT-ONTOLOGY-001 |

---

## Temporary Entities

| Entity | Nature | Persistence | Evidence |
|--------|--------|-------------|----------|
| Journal Edition | INSTANCE | Daily | CASE-JRN-001 |
| Publication Package | COLLECTION | Daily | GLOSSARY §3 |
| Representation | ARTIFACT | Temporary | CASE-INF-001 |

---

## Persistent Entities

| Entity | Nature | Persistence | Evidence |
|--------|--------|-------------|----------|
| Publication | ARTIFACT | Persistent | GLOSSARY §3 |

---

# Persistence Summary

| Persistence | Entities | Count |
|-------------|----------|-------|
| Permanent | Journal, Publisher, Publication, Lifecycle, Territory, Information, Knowledge, Open Data, Parser, Archive, Channel, Adapter | 12 |
| Daily | Journal Edition, Publication Package | 2 |
| Persistent | Publication | 1 |
| Temporary | Representation | 1 |
| **Total** | | **16** |

---

# Traceability

| Persistence Requirement | Source |
|-------------------------|--------|
| All persistence requirements | Analysis of entity nature and domain knowledge |

---

**End of Persistence Requirement**
