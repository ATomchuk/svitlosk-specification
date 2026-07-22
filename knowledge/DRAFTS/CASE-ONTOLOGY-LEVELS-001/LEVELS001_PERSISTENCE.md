# Persistence

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity persistence.

---

# Persistence

## Persistent Entities

| Entity | Level | Persistence Type | Evidence |
|--------|-------|------------------|----------|
| Journal | CONCEPT | Permanent | CHARTER §10 |
| Publisher | CONCEPT | Permanent | GLOSSARY §7 |
| Publication | CONCEPT | Permanent | GLOSSARY §3 |
| Lifecycle | CONCEPT | Permanent | CASE-LC-001 |
| Territory | CONCEPT | Permanent | GLOSSARY §4 |
| Information | CONCEPT | Permanent | CASE-INF-001 |
| Knowledge | CONCEPT | Permanent | CASE-INF-001 |
| Open Data | CONCEPT | Permanent | GLOSSARY §2 |
| Journal | SERVICE | Permanent | CHARTER §10 |
| Publisher | SERVICE | Permanent | GLOSSARY §7 |
| Parser | SERVICE | Permanent | GLOSSARY §2 |
| Archive | SERVICE | Permanent | GLOSSARY §2 |
| Publisher | ROLE | Permanent | GLOSSARY §7 |
| Interpreter | ROLE | Permanent | GLOSSARY §2 |
| Adapter | ROLE | Permanent | CASE-SVT-ONTOLOGY-001 |
| Publication | ARTIFACT | Permanent | GLOSSARY §3 |
| Specification | DOCUMENT | Permanent | GLOSSARY §1 |
| Glossary | DOCUMENT | Permanent | GLOSSARY §1 |
| Publisher Boundary | BOUNDARY | Permanent | CASE-PUB-001 |
| Channel Boundary | BOUNDARY | Permanent | CASE-TG-CORE-001 |
| Domain Boundary | BOUNDARY | Permanent | CASE-SVT-ONTOLOGY-001 |

---

## Temporary Entities

| Entity | Level | Persistence Type | Evidence |
|--------|-------|------------------|----------|
| Journal Edition | OBJECT | Daily | CASE-JRN-001 |
| Publication Package | OBJECT | Daily | GLOSSARY §3 |
| Emergency Outage Publication | OBJECT | Persistent | CASE-INFPROD-001 |
| Planned Outage Publication | OBJECT | Daily | CASE-INFPROD-001 |
| Queue Graph Publication | OBJECT | Daily | CASE-INFPROD-001 |
| Technical Publication | OBJECT | Persistent | CASE-INFPROD-001 |
| Service Publication | OBJECT | Persistent | CASE-INFPROD-001 |
| Publication Package | ARTIFACT | Daily | GLOSSARY §3 |
| Representation | ARTIFACT | Temporary | CASE-INF-001 |

---

## Transient Entities

| Entity | Level | Persistence Type | Evidence |
|--------|-------|------------------|----------|
| Parsing | PROCESS | Per request | GLOSSARY §2 |
| Interpretation | PROCESS | Per request | GLOSSARY §2 |
| Rendering | PROCESS | Per request | GLOSSARY §3 |
| Distribution | PROCESS | Per request | GLOSSARY §3 |
| Publication State | STATE | State-dependent | TELEGRAM_LIFECYCLE |
| Lifecycle State | STATE | State-dependent | CASE-LC-001 |
| Channel State | STATE | State-dependent | CASE-TG-CORE-001 |
| Data Changed | EVENT | Instantaneous | CASE-PUB-004 |
| Publication Expired | EVENT | Instantaneous | CASE-PUB-005 |
| Channel Connected | EVENT | Instantaneous | CASE-TG-CORE-001 |

---

# Persistence Summary

| Persistence Type | Entities | Count |
|------------------|----------|-------|
| Permanent | 21 | 21 |
| Daily | 4 | 4 |
| Persistent | 4 | 4 |
| Temporary | 1 | 1 |
| State-dependent | 3 | 3 |
| Instantaneous | 3 | 3 |
| **Total** | | **37** |

---

# Traceability

| Persistence | Source |
|-------------|--------|
| All persistence | Analysis of entity classification and architectural levels |

---

**End of Persistence**
