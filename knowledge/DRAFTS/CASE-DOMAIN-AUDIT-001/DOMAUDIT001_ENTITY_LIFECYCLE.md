# Entity Lifecycle

**Document Class:** Domain Completeness Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity lifecycle.

---

# Entity Lifecycle

## Permanent Entities

| Entity | Lifecycle | Notes |
|--------|-----------|-------|
| Journal | Continuous | Always exists |
| Publisher | Continuous | Always exists |
| Publication Engine | Continuous | Always exists |
| Publication | Persistent | Created, archived permanently |
| Information Product | Persistent | Created, archived permanently |
| Lifecycle | Continuous | Always exists |
| Information | Persistent | From DSO |
| Knowledge | Persistent | Derived from Information |
| Open Data | Persistent | From DSO |
| Territory | Persistent | Reference data |
| Administrative Centre | Persistent | Reference data |
| Starosta District | Persistent | Reference data |
| Settlement | Persistent | Reference data |
| Street | Persistent | Reference data |
| Address | Persistent | Reference data |
| Archive | Continuous | Always exists |
| Historical Record | Persistent | Archived permanently |

---

## Temporary Entities

| Entity | Lifecycle | Notes |
|--------|-----------|-------|
| Journal Edition | Daily | One per day |
| Publication Package | Daily | One per reporting period |
| Emergency Outage Publication | Persistent | Archived permanently |
| Planned Outage Publication | Daily | Expires end of day |
| Planned Outage Publication (Tomorrow) | Daily | Disappears end of day |
| Queue Graph Publication | Daily | Disappears end of day |
| Technical Publication | Persistent | Archived permanently |
| Service Publication | Persistent | Archived permanently |

---

## State-Dependent Entities

| Entity | Lifecycle | Notes |
|--------|-----------|-------|
| Publication State | State-dependent | Changes with lifecycle |
| Lifecycle State | State-dependent | Changes with lifecycle |
| Lifecycle Transition | State-dependent | Changes with lifecycle |

---

## Identity-Dependent Entities

| Entity | Lifecycle | Notes |
|--------|-----------|-------|
| Publication Identity | Identity-dependent | Created with Publication |
| Publication Version | Identity-dependent | Created with updates |
| Publication History | Identity-dependent | Created with changes |
| Publication Context | Identity-dependent | Created with Publication |

---

## Channel-Dependent Entities

| Entity | Lifecycle | Notes |
|--------|-----------|-------|
| Representation | Channel-dependent | Created for channel |
| Rendering | Channel-dependent | Process for channel |
| Channel | Continuous | Always exists |
| Adapter | Continuous | Always exists |
| Telegram Adapter | Continuous | Always exists |
| Facebook Adapter | Continuous | Always exists |

---

## Data-Dependent Entities

| Entity | Lifecycle | Notes |
|--------|-----------|-------|
| Parser | Continuous | Always exists |
| Parsed Data | Data-dependent | Created from data |
| Normalized Dataset | Data-dependent | Created from data |
| Schedule | Data-dependent | Created from data |
| Queue | Data-dependent | From DSO |
| Subqueue | Data-dependent | From DSO |

---

# Lifecycle Summary

| Lifecycle Type | Entities | Count |
|----------------|----------|-------|
| Permanent | Journal, Publisher, Publication Engine, Publication, Information Product, Lifecycle, Information, Knowledge, Open Data, Territory, Administrative Centre, Starosta District, Settlement, Street, Address, Archive, Historical Record | 17 |
| Temporary | Journal Edition, Publication Package, Emergency Outage Publication, Planned Outage Publication, Queue Graph Publication, Technical Publication, Service Publication | 7 |
| State-dependent | Publication State, Lifecycle State, Lifecycle Transition | 3 |
| Identity-dependent | Publication Identity, Publication Version, Publication History, Publication Context | 4 |
| Channel-dependent | Representation, Rendering, Channel, Adapter, Telegram Adapter, Facebook Adapter | 6 |
| Data-dependent | Parser, Parsed Data, Normalized Dataset, Schedule, Queue, Subqueue | 6 |
| **Total** | | **40** |

---

# Traceability

| Lifecycle | Source |
|-----------|--------|
| All lifecycles | Analysis of entity inventory and domain knowledge |

---

**End of Entity Lifecycle**
