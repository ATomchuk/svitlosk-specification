# DOMAIN_KERNEL

**Document ID:** A66-DOMAIN-KERNEL

**Title:** Domain Kernel

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Dual Kernel Investigation

---

# Purpose

This document constructs the Domain Kernel — concepts that exist even if there is NO software.

---

# Domain Kernel

## Real-World Concepts (Exist Without SvitloSk)

| # | Concept | Exists Without SvitloSk? | Evidence |
|---|---------|--------------------------|----------|
| 1 | Community | YES | Administrative unit exists independently |
| 2 | Territory | YES | Geographic area exists independently |
| 3 | Administrative Centre | YES | Principal settlement exists independently |
| 4 | Starosta District | YES | Territorial subdivision exists independently |
| 5 | Settlement | YES | Populated place exists independently |
| 6 | Street | YES | Road exists independently |
| 7 | Address | YES | Geographical location exists independently |
| 8 | Queue | YES | Electricity distribution queue exists independently |
| 9 | Subqueue | YES | Subdivision of Queue exists independently |
| 10 | Planned Power Outage | YES | Scheduled interruption exists independently |
| 11 | Emergency Power Outage | YES | Unplanned interruption exists independently |
| 12 | Electricity Availability | YES | Current status exists independently |
| 13 | Outage Schedule | YES | Official schedule exists independently |
| 14 | Availability Window | YES | Time interval exists independently |
| 15 | Outage Window | YES | Time interval exists independently |
| 16 | Time Interval | YES | Time period exists independently |
| 17 | Open Data | YES | Officially published information exists independently |
| 18 | Data Source | YES | Official organization exists independently |
| 19 | DSO | YES | Distribution System Operator exists independently |
| 20 | Resident | YES | Person exists independently |

---

## Business Concepts (Exist Because of Business Process)

| # | Concept | Exists Without SvitloSk? | Evidence |
|---|---------|--------------------------|----------|
| 21 | Public Information | PARTIALLY | Concept exists, but SvitloSk defines specific form |
| 22 | Information Consumer | PARTIALLY | People exist, but "consumer" role is defined by SvitloSk |
| 23 | Stakeholder | PARTIALLY | People exist, but "stakeholder" role is defined by SvitloSk |

---

## SvitloSk-Dependent Concepts (Exist Only Because of SvitloSk)

| # | Concept | Exists Without SvitloSk? | Evidence |
|---|---------|--------------------------|----------|
| 24 | Journal | NO | Journal concept defined by SvitloSk |
| 25 | Issue | NO | Issue concept defined by SvitloSk |
| 26 | Publication | UNCLEAR | "Public information message" could exist, but SvitloSk defines specific form |
| 27 | Publication Package | NO | Collection concept defined by SvitloSk |
| 28 | Editorial Policy | NO | Normative rules defined by SvitloSk |
| 29 | Territory (publication unit) | NO | "Logical publication entity" defined by SvitloSk |

---

# Domain Kernel Graph

```text
Community
    │
    ├──→ Administrative Centre
    │         │
    │         └──→ Settlement
    │                   │
    │                   └──→ Street
    │                             │
    │                             └──→ Address
    │
    └──→ Starosta District
              │
              └──→ Settlement
                        │
                        └──→ Street
                                  │
                                  └──→ Address

DSO
    │
    ├──→ Queue
    │         │
    │         └──→ Subqueue
    │
    ├──→ Outage Schedule
    │         │
    │         ├──→ Availability Window
    │         └──→ Outage Window
    │
    ├──→ Planned Power Outage
    └──→ Emergency Power Outage

Open Data
    │
    └──→ Data Source

Time Interval
    │
    └──→ (used by all temporal concepts)

Resident
    │
    └──→ Information Consumer
```

---

# Domain Kernel Properties

| Property | Value |
|----------|-------|
| Total concepts | 23 |
| Real-world concepts | 20 |
| Business concepts | 3 |
| Dependencies | 22 |
| Cycles | 0 |
| Root concepts | 4 (Community, DSO, Open Data, Time Interval) |
| Leaf concepts | 7 (Address, Subqueue, Planned Power Outage, Emergency Power Outage, Availability Window, Outage Window, Resident) |

---

# Key Insight

**The Domain Kernel contains concepts that exist in reality, independent of any software.**

**These concepts would exist even if SvitloSk disappeared tomorrow.**

**The Domain Kernel is STABLE and IMMUTABLE.**

---

# End of Domain Kernel
