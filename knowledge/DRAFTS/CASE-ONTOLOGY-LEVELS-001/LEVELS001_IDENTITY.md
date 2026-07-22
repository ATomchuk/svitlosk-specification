# Identity

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity identity.

---

# Identity

## Entities WITH Identity

| Entity | Level | Identity Type | Evidence |
|--------|-------|---------------|----------|
| Journal Edition | OBJECT | Reporting Period | CASE-JRN-001 |
| Publication Package | OBJECT | Reporting Period | GLOSSARY §3 |
| Emergency Outage Publication | OBJECT | Territory + Time | CASE-INFPROD-001 |
| Planned Outage Publication | OBJECT | Territory + Time | CASE-INFPROD-001 |
| Queue Graph Publication | OBJECT | Time | CASE-INFPROD-001 |
| Technical Publication | OBJECT | Time | CASE-INFPROD-001 |
| Service Publication | OBJECT | Time | CASE-INFPROD-001 |
| Publication | ARTIFACT | Territory + Time | GLOSSARY §3 |
| Publication Package | ARTIFACT | Reporting Period | GLOSSARY §3 |
| Representation | ARTIFACT | Channel + Time | CASE-INF-001 |
| Specification | DOCUMENT | Document ID | GLOSSARY §1 |
| Glossary | DOCUMENT | Document ID | GLOSSARY §1 |

---

## Entities WITHOUT Identity

| Entity | Level | Why No Identity |
|--------|-------|-----------------|
| Journal | CONCEPT | Abstract concept |
| Publisher | CONCEPT | Abstract concept |
| Publication | CONCEPT | Abstract concept |
| Lifecycle | CONCEPT | Abstract concept |
| Territory | CONCEPT | Abstract concept |
| Information | CONCEPT | Abstract concept |
| Knowledge | CONCEPT | Abstract concept |
| Open Data | CONCEPT | Abstract concept |
| Parsing | PROCESS | Transformation |
| Interpretation | PROCESS | Transformation |
| Rendering | PROCESS | Transformation |
| Distribution | PROCESS | Transformation |
| Journal | SERVICE | Continuous activity |
| Publisher | SERVICE | Continuous activity |
| Parser | SERVICE | Continuous activity |
| Archive | SERVICE | Continuous activity |
| Publisher | ROLE | Logical responsibility |
| Interpreter | ROLE | Logical responsibility |
| Adapter | ROLE | Logical responsibility |
| Publication | ARTIFACT | Physical object |
| Publication Package | ARTIFACT | Physical object |
| Representation | ARTIFACT | Physical object |
| Publication State | STATE | Condition |
| Lifecycle State | STATE | Condition |
| Channel State | STATE | Condition |
| Data Changed | EVENT | Occurrence |
| Publication Expired | EVENT | Occurrence |
| Channel Connected | EVENT | Occurrence |
| Publisher Interface | INTERFACE | Interaction point |
| Adapter Interface | INTERFACE | Interaction point |
| Publisher Boundary | BOUNDARY | Limit |
| Channel Boundary | BOUNDARY | Limit |
| Domain Boundary | BOUNDARY | Limit |
| Publisher produces Publication | RELATION | Connection |
| Parser produces Information | RELATION | Connection |
| Channel delivers Representation | RELATION | Connection |

---

# Identity Summary

| Identity Type | Entities | Count |
|---------------|----------|-------|
| Reporting Period | Journal Edition, Publication Package | 2 |
| Territory + Time | Emergency Outage Publication, Planned Outage Publication | 2 |
| Time | Queue Graph Publication, Technical Publication, Service Publication | 3 |
| Territory + Time | Publication | 1 |
| Channel + Time | Representation | 1 |
| Document ID | Specification, Glossary | 2 |
| **Total with Identity** | | **11** |

---

# Traceability

| Identity | Source |
|----------|--------|
| All identity | Analysis of entity classification and architectural levels |

---

**End of Identity**
