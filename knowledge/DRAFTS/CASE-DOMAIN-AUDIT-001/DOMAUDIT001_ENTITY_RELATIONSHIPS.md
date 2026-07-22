# Entity Relationships

**Document Class:** Domain Completeness Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document maps relationships between entities.

---

# Entity Relationships

## Journal Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Journal produces | Journal | Journal Edition | Production |
| Journal Edition contains | Journal Edition | Publication | Composition |
| Journal Edition organized by | Journal Edition | Territory | Organization |

---

## Publisher Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Publisher generates | Publisher | Publication | Generation |
| Publisher distributes | Publisher | Channel | Distribution |
| Publication Engine implements | Publication Engine | Publisher | Implementation |
| Publication Package contains | Publication Package | Publication | Composition |

---

## Publication Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Publication has | Publication | Publication State | Attribute |
| Publication has | Publication | Publication Version | Attribute |
| Publication has | Publication | Publication History | Attribute |
| Publication has | Publication | Publication Identity | Attribute |
| Publication has | Publication | Publication Context | Attribute |
| Publication derived from | Publication | Interpretation Result | Derivation |

---

## Information Product Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Information Product is | Information Product | Publication | Specialization |
| Emergency Outage Publication is | Emergency Outage Publication | Information Product | Specialization |
| Planned Outage Publication is | Planned Outage Publication | Information Product | Specialization |
| Queue Graph Publication is | Queue Graph Publication | Information Product | Specialization |
| Technical Publication is | Technical Publication | Information Product | Specialization |
| Service Publication is | Service Publication | Information Product | Specialization |

---

## Lifecycle Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Lifecycle has | Lifecycle | Lifecycle State | Composition |
| Lifecycle has | Lifecycle | Lifecycle Transition | Composition |
| Lifecycle State transitions to | Lifecycle State | Lifecycle State | Transition |

---

## Parser Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Parser produces | Parser | Parsed Data | Production |
| Parser normalizes | Parser | Normalized Dataset | Normalization |
| Parsed Data becomes | Parsed Data | Normalized Dataset | Transformation |

---

## Territory Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Territory contains | Territory | Settlement | Composition |
| Administrative Centre is | Administrative Centre | Territory | Specialization |
| Starosta District is | Starosta District | Territory | Specialization |
| Settlement contains | Settlement | Street | Composition |
| Street contains | Street | Address | Composition |

---

## Information Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Information becomes | Information | Knowledge | Transformation |
| Information derived from | Information | Open Data | Derivation |
| Knowledge derived from | Knowledge | Information | Derivation |

---

## Schedule Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Queue contains | Queue | Subqueue | Composition |
| Subqueue has | Subqueue | Schedule | Association |
| Graph Publication visualizes | Graph Publication | Schedule | Visualization |
| Text Publication contains | Text Publication | Information | Composition |
| Technical Publication contains | Technical Publication | System Status | Composition |

---

## Representation Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Representation derived from | Representation | Publication | Derivation |
| Rendering produces | Rendering | Representation | Production |

---

## Channel Domain Relationships

| Relationship | From | To | Type |
|--------------|------|----|------|
| Channel uses | Channel | Adapter | Usage |
| Adapter implements | Adapter | Publisher | Implementation |
| Telegram Adapter implements | Telegram Adapter | Adapter | Implementation |
| Facebook Adapter implements | Facebook Adapter | Adapter | Implementation |
| Channel delivers | Channel | Representation | Delivery |

---

# 4. Relationship Count

| Domain | Relationships | Count |
|--------|---------------|-------|
| Journal | 3 | 3 |
| Publisher | 4 | 4 |
| Publication | 5 | 5 |
| Information Product | 6 | 6 |
| Lifecycle | 3 | 3 |
| Parser | 3 | 3 |
| Territory | 5 | 5 |
| Information | 3 | 3 |
| Schedule | 4 | 4 |
| Representation | 2 | 2 |
| Channel | 4 | 4 |
| **Total** | | **30** |

---

# Traceability

| Relationship | Source |
|--------------|--------|
| All relationships | Analysis of entity inventory and domain knowledge |

---

**End of Entity Relationships**
