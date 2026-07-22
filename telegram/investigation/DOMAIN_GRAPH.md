# DOMAIN_GRAPH

**Document ID:** A66-DOMAIN-GRAPH

**Title:** Domain Kernel Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Dual Kernel Investigation

---

# Purpose

This document draws the complete Domain Kernel graph.

---

# Domain Kernel Graph

```text
                        REALITY
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
      Community          DSO          Open Data
           │               │               │
     ┌─────┴─────┐    ┌────┴────┐          │
     ▼           ▼    ▼         ▼          ▼
Admin Centre  Starosta  Queue  Outage   Data Source
     │         District  │    Schedule
     │           │       │       │
     ▼           ▼       ▼       ├──→ Availability Window
 Settlement  Settlement Subqueue └──→ Outage Window
     │           │
     ▼           ▼
  Street      Street
     │           │
     ▼           ▼
  Address    Address

Planned Power Outage ←── DSO
Emergency Power Outage ←── DSO
Electricity Availability ←── DSO

Time Interval
     │
     └──→ (used by all temporal concepts)

Resident
     │
     └──→ Information Consumer
```

---

# Domain Kernel Dependencies

| Concept | Depends On | Depended By |
|---------|------------|-------------|
| Community | None | Administrative Centre, Starosta District |
| Administrative Centre | Community | Settlement |
| Starosta District | Community | Settlement |
| Settlement | Administrative Centre, Starosta District | Street |
| Street | Settlement | Address |
| Address | Street | (used by Publications) |
| DSO | None | Queue, Subqueue, Outage Schedule, Planned Power Outage, Emergency Power Outage |
| Queue | DSO | Subqueue |
| Subqueue | Queue | (used by Schedules) |
| Outage Schedule | DSO | Availability Window, Outage Window |
| Availability Window | Outage Schedule | (used by Schedules) |
| Outage Window | Outage Schedule | (used by Schedules) |
| Planned Power Outage | DSO | (used by Publications) |
| Emergency Power Outage | DSO | (used by Publications) |
| Electricity Availability | DSO | (derived from Schedules) |
| Open Data | None | Data Source |
| Data Source | Open Data | (provides data to Parser) |
| Time Interval | None | (used by all temporal concepts) |
| Resident | None | Information Consumer |
| Information Consumer | Resident | (receives Publications) |

---

# Domain Kernel Properties

| Property | Value |
|----------|-------|
| Root concepts | 4 (Community, DSO, Open Data, Time Interval) |
| Leaf concepts | 7 (Address, Subqueue, Planned Power Outage, Emergency Power Outage, Availability Window, Outage Window, Resident) |
| Central concepts | 3 (DSO, Settlement, Outage Schedule) |
| Total paths | 22 |

---

# Key Insight

**The Domain Kernel has 4 root concepts that exist independently of everything else.**

**All other Domain concepts are derived from or related to these 4 roots.**

**The Domain Kernel is a clean, hierarchical structure with no cycles.**

---

# End of Domain Kernel Graph
