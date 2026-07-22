# Entity Ownership

**Document Class:** Domain Completeness Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity ownership.

---

# Entity Ownership

## Publisher-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Publisher | Publisher | Core Publisher concept |
| Publication Engine | Publisher | Implements Publisher Role |
| Publication Package | Publisher | Collection of Publications |
| Publication | Publisher | Atomic unit of information |
| Publication State | Publisher | Lifecycle state |
| Publication Version | Publisher | Version of Publication |
| Publication History | Publisher | Historical record |
| Publication Identity | Publisher | Unique identifier |
| Publication Context | Publisher | Context of Publication |
| Information Product | Publisher | Product type |
| Emergency Outage Publication | Publisher | Product type |
| Planned Outage Publication | Publisher | Product type |
| Queue Graph Publication | Publisher | Product type |
| Technical Publication | Publisher | Product type |
| Service Publication | Publisher | Product type |

---

## Lifecycle-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Lifecycle | Lifecycle | Pattern for information flow |
| Lifecycle State | Lifecycle | State in lifecycle |
| Lifecycle Transition | Lifecycle | Transition between states |

---

## Parser-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Parser | Parser | Retrieves Open Data |
| Parsed Data | Parser | Normalized data |
| Normalized Dataset | Parser | Structured data |

---

## Territory-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Territory | Territory | Geographic unit |
| Administrative Centre | Territory | Principal territorial unit |
| Starosta District | Territory | Territorial subdivision |
| Settlement | Territory | Populated place |
| Street | Territory | Official street |
| Address | Territory | Geographical location |

---

## Information-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Information | Information | Factual content |
| Knowledge | Information | Interpreted information |
| Open Data | Information | Official published data |

---

## Schedule-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Schedule | Schedule | Electricity availability |
| Queue | Schedule | Electricity distribution queue |
| Subqueue | Schedule | Queue subdivision |
| Graph Publication | Publisher | Visualization |
| Text Publication | Publisher | Text publication |
| Technical Publication | Publisher | System update publication |

---

## Channel-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Channel | Channel | Communication medium |
| Adapter | Adapter | Channel-specific implementation |
| Telegram Adapter | Telegram | Telegram-specific adapter |
| Facebook Adapter | Facebook | Facebook-specific adapter |

---

## Archive-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Archive | Archive | Historical storage |
| Historical Record | Archive | Archived information |

---

## Representation-Owned Entities

| Entity | Owner | Why |
|--------|-------|-----|
| Representation | Adapter | Channel-specific output |
| Rendering | Adapter | Conversion process |

---

# Ownership Summary

| Owner | Entities | Count |
|-------|----------|-------|
| Publisher | 15 | 15 |
| Lifecycle | 3 | 3 |
| Parser | 3 | 3 |
| Territory | 6 | 6 |
| Information | 3 | 3 |
| Schedule | 3 | 3 |
| Channel | 4 | 4 |
| Archive | 2 | 2 |
| Adapter | 2 | 2 |
| **Total** | | **40** |

---

# Traceability

| Ownership | Source |
|-----------|--------|
| All ownership | Analysis of entity inventory and domain knowledge |

---

**End of Entity Ownership**
