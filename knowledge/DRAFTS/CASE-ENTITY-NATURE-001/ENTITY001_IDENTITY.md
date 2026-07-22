# Identity

**Document Class:** Entity Nature Investigation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity identity.

---

# Identity

## Entities WITH Identity

| Entity | Nature | Identity Type | Evidence |
|--------|--------|---------------|----------|
| Journal Edition | INSTANCE | Reporting Period | CASE-JRN-001 |
| Publication Package | COLLECTION | Reporting Period | GLOSSARY §3 |
| Publication | ARTIFACT | Territory + Time | GLOSSARY §3 |
| Territory | REFERENCE | Geographic | GLOSSARY §4 |
| Representation | ARTIFACT | Channel + Time | CASE-INF-001 |
| Channel | SERVICE | Channel identity | GLOSSARY §3 |
| Adapter | SERVICE + ROLE | Channel identity | CASE-SVT-ONTOLOGY-001 |

---

## Entities WITHOUT Identity

| Entity | Nature | Why No Identity |
|--------|--------|-----------------|
| Journal | SERVICE | Abstract concept |
| Publisher | SERVICE + ROLE | Abstract concept |
| Lifecycle | PATTERN | Abstract pattern |
| Information | CONCEPT | Abstract concept |
| Knowledge | CONCEPT | Abstract concept |
| Open Data | CONCEPT | Abstract concept |
| Parser | SERVICE | Abstract concept |
| Archive | SERVICE | Abstract concept |

---

# Identity Summary

| Identity Type | Entities | Count |
|---------------|----------|-------|
| Reporting Period | Journal Edition, Publication Package | 2 |
| Territory | Publication | 1 |
| Geographic | Territory | 1 |
| Channel + Time | Representation | 1 |
| Channel identity | Channel, Adapter | 2 |
| **Total with Identity** | | **7** |

---

# Traceability

| Identity | Source |
|----------|--------|
| All identity | Analysis of entity nature and domain knowledge |

---

**End of Identity**
