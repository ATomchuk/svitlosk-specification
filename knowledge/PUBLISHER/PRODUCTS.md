# Publisher Products

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the information products produced by Publisher.

---

# Information Products

## Emergency Outage Publication

**Domain:** C — Emergency Outages

**Atomic:** YES

**Temporary:** NO (permanent)

**Channel-Independent:** YES

**Territory-Organized:** YES

**Evidence:** CASE-INFPROD-001, CASE-SVT-ONTOLOGY-001

---

## Planned Outage Publication (Today)

**Domain:** B — Planned Outages

**Atomic:** YES

**Temporary:** YES (expires end of day)

**Channel-Independent:** YES

**Territory-Organized:** YES

**Evidence:** CASE-INFPROD-001, CASE-SVT-ONTOLOGY-001

---

## Planned Outage Publication (Tomorrow)

**Domain:** B — Planned Outages

**Atomic:** YES

**Temporary:** YES (disappears end of day)

**Channel-Independent:** YES

**Territory-Organized:** YES

**Evidence:** CASE-INFPROD-001, CASE-SVT-ONTOLOGY-001

---

## Queue Graph Publication (Tomorrow)

**Domain:** A — Queue Schedule

**Atomic:** NO (composite)

**Temporary:** YES (disappears end of day)

**Channel-Independent:** PARTIALLY (format differs)

**Territory-Organized:** NO (single product)

**Evidence:** CASE-INFPROD-001, CASE-TG-CORE-001

---

## Technical Publication

**Domain:** System

**Atomic:** YES

**Temporary:** NO (permanent)

**Channel-Independent:** YES

**Territory-Organized:** NO

**Evidence:** CASE-INFPROD-001, CASE-TG-CORE-001

---

## Service Publication (Future)

**Domain:** System

**Atomic:** YES

**Temporary:** NO (permanent)

**Channel-Independent:** YES

**Territory-Organized:** NO

**Evidence:** CASE-INFPROD-001

---

# Product Taxonomy

| Dimension | Categories |
|-----------|------------|
| Domain | Queue (A), Planned (B), Emergency (C), System (D) |
| Atomicity | Atomic (5), Composite (1) |
| Persistence | Permanent (3), Temporary (3) |
| Channel Independence | Fully (5), Partially (1) |
| Territory Organization | Territory-based (3), Non-territory (3) |

---

# Product Inventory

| Product | Domain | Atomic | Temporary | Channel-Independent | Territory-Organized |
|---------|--------|--------|-----------|---------------------|---------------------|
| Emergency Outage | C | YES | NO | YES | YES |
| Planned Outage (Today) | B | YES | YES | YES | YES |
| Planned Outage (Tomorrow) | B | YES | YES | YES | YES |
| Queue Graph (Tomorrow) | A | NO | YES | PARTIALLY | NO |
| Technical | System | YES | NO | YES | NO |
| Service (Future) | System | YES | NO | YES | NO |

---

# Evidence

| Product | Source |
|---------|--------|
| Emergency Outage | CASE-INFPROD-001, CASE-SVT-ONTOLOGY-001 |
| Planned Outage (Today) | CASE-INFPROD-001, CASE-SVT-ONTOLOGY-001 |
| Planned Outage (Tomorrow) | CASE-INFPROD-001, CASE-SVT-ONTOLOGY-001 |
| Queue Graph (Tomorrow) | CASE-INFPROD-001, CASE-TG-CORE-001 |
| Technical | CASE-INFPROD-001, CASE-TG-CORE-001 |
| Service (Future) | CASE-INFPROD-001 |

---

**End of Products**
