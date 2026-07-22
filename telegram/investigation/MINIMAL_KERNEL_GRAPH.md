# MINIMAL_KERNEL_GRAPH

**Document ID:** CASE001G-KERNEL-GRAPH

**Title:** Minimal Kernel Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Minimal Kernel Investigation

---

# Purpose

This document draws the dependency graph for the minimal kernel.

---

# Minimal Kernel

```
Open Data
    │
    ▼
Data Source
    │
    ▼
    Parser
    │
    ▼
Normalized Dataset
    │
    ▼
Publication Engine
    │
    ├──→ Schedule
    │         │
    │         ▼
    │    Time Interval
    │
    ├──→ Address
    │
    └──→ Publication
              │
              ▼
         Telegram Channel
              │
              ▼
           Residents
```

---

# Kernel Dependencies

| Concept | Depends On | Depended By |
|---------|------------|-------------|
| Open Data | None | Data Source |
| Data Source | Open Data | Parser |
| Parser | Data Source | Publication Engine |
| Normalized Dataset | Parser | Publication Engine |
| Publication Engine | Normalized Dataset | Publication |
| Schedule | Publication Engine | Publication |
| Time Interval | Schedule | Publication |
| Address | None | Publication |
| Publication | Publication Engine, Schedule, Time Interval, Address | Telegram Channel |
| Telegram Channel | Publication | Residents |
| Residents | Telegram Channel | None |

---

# Kernel Properties

| Property | Value |
|----------|-------|
| Total concepts | 11 |
| Dependencies | 10 |
| Cycles | 0 |
| Root concepts | 2 (Open Data, Address) |
| Leaf concepts | 1 (Residents) |
| Central concept | Publication (6 dependencies) |

---

# Key Insight

**Publication is the CENTRAL concept of the minimal kernel.**

**All other concepts either feed into Publication or are fed by Publication.**

**Publication cannot be removed without breaking the entire kernel.**

---

# End of Minimal Kernel Graph
