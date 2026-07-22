# ARCHITECTURE_GRAPH

**Document ID:** A66-ARCHITECTURE-GRAPH

**Title:** Architecture Kernel Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Dual Kernel Investigation

---

# Purpose

This document draws the complete Architecture Kernel graph.

---

# Architecture Kernel Graph

```text
                    DATA FLOW
                        │
                        ▼
              External Data Sources
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
           ┌────────────┼────────────┐
           │            │            │
           ▼            ▼            ▼
    Schedule Generator  │    Graphic Generator
           │            │            │
           ▼            │            ▼
       Schedule         │        Graphic
                        │
                        ▼
                 Publication Package
                        │
                        ▼
                 Telegram Publisher
                        │
                        ▼
                 Telegram Channel
                        │
                        ▼
                    Subscribers

                    STORAGE
                        │
                        ▼
                   Data Storage
                        │
           ┌────────────┼────────────┐
           │            │            │
           ▼            ▼            ▼
    Normalized Data  Publication  Historical
       Storage        Storage     Archive

                    GOVERNANCE
                        │
                        ▼
                   Specification
                        │
                        ▼
              Canonical Documentation
                        │
                        ▼
                       ADR
                        │
                        ▼
               Normative Document
```

---

# Architecture Kernel Dependencies

| Concept | Depends On | Depended By |
|---------|------------|-------------|
| Parser | External Data Sources | Normalized Dataset |
| Normalized Dataset | Parser | Publication Engine, Data Storage |
| Publication Engine | Normalized Dataset | Publication Package, Schedule, Graphic |
| Schedule Generator | Normalized Dataset | Schedule |
| Schedule | Schedule Generator | Publication Engine |
| Graphic Generator | Normalized Dataset | Graphic |
| Graphic | Graphic Generator | Publication Engine |
| Publication Package | Publication Engine | Telegram Publisher |
| Telegram Publisher | Publication Package | Telegram Channel |
| Telegram Channel | Telegram Publisher | Subscribers |
| Data Storage | Parser, Publication Engine | (stores data) |
| Historical Archive | Data Storage | (preserves records) |
| Specification | None | Canonical Documentation |
| Canonical Documentation | Specification | ADR |
| ADR | Canonical Documentation | Normative Document |
| Normative Document | ADR | (governs implementation) |

---

# Architecture Kernel Properties

| Property | Value |
|----------|-------|
| Root concepts | 2 (External Data Sources, Specification) |
| Leaf concepts | 3 (Subscribers, Historical Archive, Normative Document) |
| Central concepts | 2 (Publication Engine, Data Storage) |
| Total paths | 16 |

---

# Key Insight

**The Architecture Kernel has 2 root concepts: External Data Sources and Specification.**

**External Data Sources is the physical entry point; Specification is the governance entry point.**

**The Architecture Kernel is a flow-based structure with clear data direction.**

---

# End of Architecture Kernel Graph
