# Publisher Relationships

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the relationships between Publisher concepts.

---

# Core Relationships

## REL-001: Publisher executes Publication

**From:** Publisher

**To:** Publication

**Type:** Execution

**Evidence:** CASE-PUB-002, CASE-PUB-004, CASE-PUB-005

---

## REL-002: Lifecycle governs Publication lifecycle

**From:** Lifecycle

**To:** Publication

**Type:** Governance

**Evidence:** CASE-LC-001, CASE-PUB-004, CASE-PUB-005

---

## REL-003: Publication belongs to Journal Edition

**From:** Publication

**To:** Journal Edition

**Type:** Membership

**Evidence:** CASE-JRN-001, CASE-INFPROD-001

---

## REL-004: Parser produces Information

**From:** Parser

**To:** Information

**Type:** Production

**Evidence:** CASE-SVT-ONTOLOGY-001, CASE-TG-CORE-001

---

## REL-005: Information becomes Knowledge through Interpretation

**From:** Information

**To:** Knowledge

**Type:** Transformation

**Evidence:** CASE-INF-001

---

## REL-006: Knowledge becomes Publication through Publisher

**From:** Knowledge

**To:** Publication

**Type:** Transformation

**Evidence:** CASE-PUB-002, CASE-PUB-004

---

## REL-007: Publication becomes Representation through Adapter

**From:** Publication

**To:** Representation

**Type:** Transformation

**Evidence:** CASE-TG-CORE-001, CASE-INFPROD-001

---

# Domain Relationships

## REL-008: Queue Schedule is Domain A

**From:** Queue Schedule

**To:** Domain A

**Type:** Classification

**Evidence:** CASE-SVT-ONTOLOGY-001, Architect Intent

---

## REL-009: Planned Outage is Domain B

**From:** Planned Outage

**To:** Domain B

**Type:** Classification

**Evidence:** CASE-SVT-ONTOLOGY-001, Architect Intent

---

## REL-010: Emergency Outage is Domain C

**From:** Emergency Outage

**To:** Domain C

**Type:** Classification

**Evidence:** CASE-SVT-ONTOLOGY-001, Architect Intent

---

## REL-011: Domains are Independent

**From:** Domain A

**To:** Domain B, Domain C

**Type:** Independence

**Evidence:** CASE-SVT-ONTOLOGY-001, Architect Intent

---

# Territorial Relationships

## REL-012: Publication is organized by Territory

**From:** Publication

**To:** Territory

**Type:** Organization

**Evidence:** CASE-INFPROD-001, CASE-TG-CORE-001

---

## REL-013: Journal Edition contains Publications by Territory

**From:** Journal Edition

**To:** Publication, Territory

**Type:** Composition

**Evidence:** CASE-JRN-001, CASE-INFPROD-001

---

# Lifecycle Relationships

## REL-014: Publication has lifecycle states

**From:** Publication

**To:** State

**Type:** Attribute

**Evidence:** CASE-LC-001, CASE-PUB-005

---

## REL-015: Temporary Publications expire

**From:** Temporary Publication

**To:** Expiry

**Type:** Behavior

**Evidence:** CASE-INFPROD-001, CASE-PUB-005

---

## REL-016: Permanent Publications are archived

**From:** Permanent Publication

**To:** Archive

**Type:** Behavior

**Evidence:** CASE-INFPROD-001, CASE-PUB-005

---

# Channel Relationships

## REL-017: Adapter delivers Representation to Channel

**From:** Adapter

**To:** Channel, Representation

**Type:** Delivery

**Evidence:** CASE-TG-CORE-001

---

## REL-018: Publisher distributes through Adapters

**From:** Publisher

**To:** Adapter

**Type:** Distribution

**Evidence:** CASE-PUB-002, CASE-SVT-ONTOLOGY-001

---

# Relationship Count

| Category | Count |
|----------|-------|
| Core | 7 |
| Domain | 4 |
| Territorial | 2 |
| Lifecycle | 3 |
| Channel | 2 |
| **Total** | **18** |

---

# Evidence

| Relationship | Source |
|--------------|--------|
| REL-001 to REL-007 | CASE-PUB-002, CASE-PUB-004, CASE-PUB-005, CASE-INF-001, CASE-INFPROD-001, CASE-JRN-001, CASE-LC-001, CASE-SVT-ONTOLOGY-001, CASE-TG-CORE-001 |
| REL-008 to REL-011 | CASE-SVT-ONTOLOGY-001, Architect Intent |
| REL-012 to REL-013 | CASE-INFPROD-001, CASE-JRN-001, CASE-TG-CORE-001 |
| REL-014 to REL-016 | CASE-INFPROD-001, CASE-LC-001, CASE-PUB-005 |
| REL-017 to REL-018 | CASE-PUB-002, CASE-SVT-ONTOLOGY-001, CASE-TG-CORE-001 |

---

**End of Relationships**
