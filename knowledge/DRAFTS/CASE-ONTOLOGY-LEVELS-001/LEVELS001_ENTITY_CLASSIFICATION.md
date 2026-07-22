# Entity Classification

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document classifies every entity by architectural level.

---

# Entity Classification

## Level 1: CONCEPT

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Journal | Abstract service idea | CHARTER §10 | YES | — | — | YES | NO | YES | NO |
| Publisher | Abstract role idea | GLOSSARY §7 | YES | — | — | YES | NO | YES | NO |
| Publication | Abstract unit idea | GLOSSARY §3 | YES | — | — | YES | NO | YES | NO |
| Lifecycle | Abstract pattern idea | CASE-LC-001 | YES | — | — | YES | NO | YES | NO |
| Territory | Abstract geographic idea | GLOSSARY §4 | YES | — | — | YES | NO | NO | NO |
| Information | Abstract content idea | CASE-INF-001 | YES | — | — | YES | NO | NO | NO |
| Knowledge | Abstract interpretation idea | CASE-INF-001 | YES | — | — | YES | NO | NO | NO |
| Open Data | Abstract official data idea | GLOSSARY §2 | YES | — | — | YES | NO | NO | NO |

---

## Level 2: OBJECT

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Journal Edition | Daily instance | CASE-JRN-001 | YES | Publisher | Residents | TEMPORARY | YES | YES | Publisher |
| Publication Package | Collection of Publications | GLOSSARY §3 | YES | Publisher | Channels | TEMPORARY | YES | YES | Publisher |
| Emergency Outage Publication | Product type | CASE-INFPROD-001 | YES | Publisher | Channels | PERSISTENT | YES | YES | Publisher |
| Planned Outage Publication | Product type | CASE-INFPROD-001 | YES | Publisher | Channels | TEMPORARY | YES | YES | Publisher |
| Queue Graph Publication | Product type | CASE-INFPROD-001 | YES | Publisher | Channels | TEMPORARY | YES | YES | Publisher |
| Technical Publication | Product type | CASE-INFPROD-001 | YES | Publisher | Channels | PERSISTENT | YES | YES | Publisher |
| Service Publication | Product type | CASE-INFPROD-001 | YES | Publisher | Channels | PERSISTENT | YES | YES | Publisher |

---

## Level 3: PROCESS

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Parsing | Data transformation | GLOSSARY §2 | YES | Parser | Parser | NO | NO | YES | Parser |
| Interpretation | Information transformation | GLOSSARY §2 | YES | Interpreter | Publisher | NO | NO | YES | Interpreter |
| Rendering | Publication transformation | GLOSSARY §3 | YES | Adapter | Channel | NO | NO | YES | Adapter |
| Distribution | Publication delivery | GLOSSARY §3 | YES | Publisher | Channel | NO | NO | YES | Publisher |

---

## Level 4: SERVICE

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Journal | Ongoing publication service | CHARTER §10 | YES | System | Residents | YES | NO | YES | System |
| Publisher | Publication preparation service | GLOSSARY §7 | YES | System | Channels | YES | NO | YES | System |
| Parser | Data retrieval service | GLOSSARY §2 | YES | System | Publisher | YES | NO | YES | System |
| Archive | Historical storage service | GLOSSARY §2 | YES | System | System | YES | NO | YES | System |

---

## Level 5: ROLE

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Publisher | Logical publishing responsibility | GLOSSARY §7 | YES | — | — | YES | NO | YES | — |
| Interpreter | Logical interpretation responsibility | GLOSSARY §2 | YES | — | — | YES | NO | YES | — |
| Adapter | Logical channel responsibility | CASE-SVT-ONTOLOGY-001 | YES | — | — | YES | NO | YES | — |

---

## Level 6: ARTIFACT

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Publication | Information artifact | GLOSSARY §3 | YES | Publisher | Channels | YES | YES | YES | Publisher |
| Publication Package | Collection artifact | GLOSSARY §3 | YES | Publisher | Channels | TEMPORARY | YES | YES | Publisher |
| Representation | Channel-specific artifact | CASE-INF-001 | YES | Adapter | Residents | TEMPORARY | YES | YES | Adapter |

---

## Level 7: DOCUMENT

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Specification | Normative document | GLOSSARY §1 | YES | System | System | YES | YES | YES | System |
| Glossary | Terminology document | GLOSSARY §1 | YES | System | System | YES | YES | YES | System |

---

## Level 8: STATE

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Publication State | Publication condition | TELEGRAM_LIFECYCLE | NO | System | System | TEMPORAL | NO | YES | Lifecycle |
| Lifecycle State | Lifecycle condition | CASE-LC-001 | NO | System | System | TEMPORAL | NO | YES | Lifecycle |
| Channel State | Channel condition | CASE-TG-CORE-001 | NO | Adapter | Adapter | TEMPORAL | NO | YES | Adapter |

---

## Level 9: EVENT

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Data Changed | Information event | CASE-PUB-004 | YES | Parser | Lifecycle | NO | NO | NO | Parser |
| Publication Expired | Publication event | CASE-PUB-005 | YES | Lifecycle | Publisher | NO | NO | NO | Lifecycle |
| Channel Connected | Channel event | CASE-TG-CORE-001 | YES | Adapter | Adapter | NO | NO | NO | Adapter |

---

## Level 10: INTERFACE

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Publisher Interface | Publisher interaction point | CASE-PUB-002 | YES | Publisher | Adapter | YES | NO | NO | Publisher |
| Adapter Interface | Channel interaction point | CASE-TG-CORE-001 | YES | Adapter | Channel | YES | NO | NO | Adapter |

---

## Level 11: BOUNDARY

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Publisher Boundary | Publisher scope limit | CASE-PUB-001 | YES | System | System | YES | NO | NO | System |
| Channel Boundary | Channel scope limit | CASE-TG-CORE-001 | YES | System | System | YES | NO | NO | System |
| Domain Boundary | Domain separation | CASE-SVT-ONTOLOGY-001 | YES | System | System | YES | NO | NO | System |

---

## Level 12: RELATION

| Entity | Why? | Evidence | Independent? | Creator | Consumer | Persistent? | Identity? | Lifecycle? | Owned? |
|--------|------|----------|--------------|---------|----------|-------------|-----------|------------|--------|
| Publisher produces Publication | Connection | CASE-PUB-002 | YES | — | — | YES | NO | NO | — |
| Parser produces Information | Connection | GLOSSARY §2 | YES | — | — | YES | NO | NO | — |
| Channel delivers Representation | Connection | CASE-TG-CORE-001 | YES | — | — | YES | NO | NO | — |

---

# Classification Summary

| Level | Entities | Count |
|-------|----------|-------|
| CONCEPT | Journal, Publisher, Publication, Lifecycle, Territory, Information, Knowledge, Open Data | 8 |
| OBJECT | Journal Edition, Publication Package, Emergency Outage Publication, Planned Outage Publication, Queue Graph Publication, Technical Publication, Service Publication | 7 |
| PROCESS | Parsing, Interpretation, Rendering, Distribution | 4 |
| SERVICE | Journal, Publisher, Parser, Archive | 4 |
| ROLE | Publisher, Interpreter, Adapter | 3 |
| ARTIFACT | Publication, Publication Package, Representation | 3 |
| DOCUMENT | Specification, Glossary | 2 |
| STATE | Publication State, Lifecycle State, Channel State | 3 |
| EVENT | Data Changed, Publication Expired, Channel Connected | 3 |
| INTERFACE | Publisher Interface, Adapter Interface | 2 |
| BOUNDARY | Publisher Boundary, Channel Boundary, Domain Boundary | 3 |
| RELATION | Publisher produces Publication, Parser produces Information, Channel delivers Representation | 3 |
| **Total** | | **45** |

---

# Traceability

| Classification | Source |
|----------------|--------|
| All classifications | Analysis of entity inventory and architectural levels |

---

**End of Entity Classification**
