# Entity Inventory

**Document Class:** Domain Completeness Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document identifies every domain entity.

---

# Entity Inventory

## Journal Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Journal | Ongoing publication service | Publisher | System | Residents | Publication | YES | YES |
| Journal Edition | One daily instance | Publisher | Publisher | Residents | Publication | YES | YES |

---

## Publisher Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Publisher | Prepare and distribute Publications | Publisher | System | Channels | Publication, Lifecycle | NO | NO |
| Publication Engine | Implement Publisher Role | Publisher | System | Channels | Parser, Publisher | NO | NO |
| Publication Package | Collection of Publications | Publisher | Publisher | Channels | Publication | YES | YES |

---

## Publication Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Publication | Atomic unit of information | Publisher | Publisher | Channels | Interpretation Result | YES | YES |
| Publication State | Lifecycle state | Lifecycle | System | System | Publication | YES | YES |
| Publication Version | Version of Publication | Publisher | Publisher | System | Publication | YES | YES |
| Publication History | Historical record | Publisher | Publisher | System | Publication | YES | YES |
| Publication Identity | Unique identifier | Publisher | Publisher | System | Publication | YES | YES |
| Publication Context | Context of Publication | Publisher | Publisher | System | Publication | YES | YES |

---

## Information Product Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Information Product | Discrete unit of information | Publisher | Publisher | Channels | Interpretation Result | YES | YES |
| Emergency Outage Publication | Emergency outage information | Publisher | Publisher | Channels | Emergency Outage | YES | YES |
| Planned Outage Publication | Planned outage information | Publisher | Publisher | Channels | Planned Outage | YES | YES |
| Queue Graph Publication | Queue schedule visualization | Publisher | Publisher | Channels | Queue Schedule | YES | YES |
| Technical Publication | System update information | Publisher | Publisher | Channels | System Status | YES | YES |
| Service Publication | Future project information | Publisher | Publisher | Channels | Service Announcement | YES | YES |

---

## Lifecycle Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Lifecycle | Pattern for information flow | Lifecycle | System | System | — | YES | YES |
| Lifecycle State | State in lifecycle | Lifecycle | System | System | Lifecycle | YES | YES |
| Lifecycle Transition | Transition between states | Lifecycle | System | System | Lifecycle State | YES | YES |

---

## Parser Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Parser | Retrieve Open Data | Parser | DSO | Publisher | DSO | YES | YES |
| Parsed Data | Normalized data | Parser | Parser | Publisher | Parser | YES | YES |
| Normalized Dataset | Structured data | Parser | Parser | Publisher | Parser | YES | YES |

---

## Territory Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Territory | Geographic unit | Territory | System | Publisher | Community | YES | YES |
| Administrative Centre | Principal territorial unit | Territory | System | Publisher | Community | YES | YES |
| Starosta District | Territorial subdivision | Territory | System | Publisher | Community | YES | YES |
| Settlement | Populated place | Territory | System | Publisher | Territory | YES | YES |
| Street | Official street | Territory | System | Publisher | Settlement | YES | YES |
| Address | Geographical location | Territory | System | Publisher | Street | YES | YES |

---

## Information Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Information | Factual content | Information | DSO | Publisher | DSO | YES | YES |
| Knowledge | Interpreted information | Information | Publisher | Channels | Information | YES | YES |
| Open Data | Official published data | Information | DSO | Parser | DSO | YES | YES |

---

## Schedule Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Schedule | Electricity availability | Schedule | Parser | Publisher | Parser | YES | YES |
| Queue | Electricity distribution queue | Schedule | DSO | Parser | DSO | YES | YES |
| Subqueue | Queue subdivision | Schedule | DSO | Parser | Queue | YES | YES |
| Graph Publication | Queue schedule visualization | Publisher | Publisher | Channels | Schedule | YES | YES |
| Text Publication | Text-based publication | Publisher | Publisher | Channels | Information | YES | YES |
| Technical Publication | System update publication | Publisher | Publisher | Channels | System Status | YES | YES |

---

## Representation Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Representation | Channel-specific output | Adapter | Adapter | Residents | Publication | YES | YES |
| Rendering | Conversion process | Adapter | Adapter | Channels | Publication | YES | YES |

---

## Channel Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Channel | Communication medium | Channel | System | Residents | Adapter | YES | YES |
| Adapter | Channel-specific implementation | Adapter | System | Channels | Publisher | YES | YES |
| Telegram Adapter | Telegram-specific adapter | Telegram | System | Telegram | Publisher | YES | YES |
| Facebook Adapter | Facebook-specific adapter | Facebook | System | Facebook | Publisher | YES | YES |

---

## Archive Domain

| Entity | Why It Exists | Owner | Creates | Consumes | Depends On | Without Publisher | Publisher Without It |
|--------|---------------|-------|---------|----------|------------|-------------------|---------------------|
| Archive | Historical storage | Archive | System | System | Publication | YES | YES |
| Historical Record | Archived information | Archive | System | System | Archive | YES | YES |

---

# 3. Entity Count

| Domain | Entities | Count |
|--------|----------|-------|
| Journal | Journal, Journal Edition | 2 |
| Publisher | Publisher, Publication Engine, Publication Package | 3 |
| Publication | Publication, Publication State, Publication Version, Publication History, Publication Identity, Publication Context | 6 |
| Information Product | Information Product, Emergency Outage Publication, Planned Outage Publication, Queue Graph Publication, Technical Publication, Service Publication | 6 |
| Lifecycle | Lifecycle, Lifecycle State, Lifecycle Transition | 3 |
| Parser | Parser, Parsed Data, Normalized Dataset | 3 |
| Territory | Territory, Administrative Centre, Starosta District, Settlement, Street, Address | 6 |
| Information | Information, Knowledge, Open Data | 3 |
| Schedule | Schedule, Queue, Subqueue, Graph Publication, Text Publication, Technical Publication | 6 |
| Representation | Representation, Rendering | 2 |
| Channel | Channel, Adapter, Telegram Adapter, Facebook Adapter | 4 |
| Archive | Archive, Historical Record | 2 |
| **Total** | | **40** |

---

# Traceability

| Entity | Source |
|--------|--------|
| All entities | CASE-PUB-001 through CASE-TG-CORE-001, GLOSSARY, CHARTER, TERRITORIAL_MODEL |

---

**End of Entity Inventory**
