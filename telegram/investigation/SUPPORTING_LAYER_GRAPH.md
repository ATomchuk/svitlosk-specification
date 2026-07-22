# SUPPORTING_LAYER_GRAPH

**Document ID:** CASE001G-SUPPORTING-GRAPH

**Title:** Supporting Layer Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Minimal Kernel Investigation

---

# Purpose

This document draws the dependency graph for the supporting layer.

---

# Supporting Layer

## Derived Concepts

```text
Publication
    │
    ├──→ Publication Package (collection)
    ├──→ Interpretation Result (input)
    ├──→ Parsed Data (input)
    ├──→ Normalized Dataset (input)
    ├──→ Graphic (visual)
    ├──→ Daily Snapshot (archive)
    └──→ Analytics Record (analysis)
```

## Projection Concepts

```text
Publication
    │
    ├──→ Telegram Message (platform)
    ├──→ Repository Object (storage)
    └──→ Historical Record (archive)
```

## Implementation Concepts

```text
Publication Engine
    │
    ├──→ Parser
    ├──→ Telegram Publisher
    ├──→ Schedule Generator
    ├──→ Graphic Generator
    ├──→ Data Storage
    └──→ Telegram Channel
```

## Convenience Abstractions

```text
Territory
    │
    ├──→ Community (top-level)
    ├──→ Administrative Centre
    ├──→ Starosta District
    ├──→ Settlement
    └──→ Street

Journal
    │
    └──→ Issue (daily)
```

---

# Supporting Layer Dependencies

| Concept | Type | Depends On |
|---------|------|------------|
| Publication Package | Derived | Publication |
| Interpretation Result | Derived | Parser |
| Parsed Data | Derived | Parser |
| Normalized Dataset | Derived | Parser |
| Graphic | Derived | Schedule |
| Daily Snapshot | Derived | Publication |
| Analytics Record | Derived | Historical Record |
| Telegram Message | Projection | Publication |
| Repository Object | Projection | Publication |
| Historical Record | Projection | Publication |
| Publication Engine | Implementation | Publisher Role |
| Parser | Implementation | Data Retrieval Role |
| Telegram Publisher | Implementation | Publisher Role |
| Schedule Generator | Implementation | Schedule generation |
| Graphic Generator | Implementation | Graphic generation |
| Data Storage | Implementation | Persistent storage |
| Telegram Channel | Implementation | Publication channel |
| Territory | Abstraction | Geographic grouping |
| Community | Abstraction | Top-level scope |
| Administrative Centre | Abstraction | Geographic grouping |
| Starosta District | Abstraction | Geographic grouping |
| Settlement | Abstraction | Geographic grouping |
| Street | Abstraction | Geographic grouping |
| Journal | Abstraction | Continuous publication |
| Issue | Abstraction | Daily grouping |

---

# Key Insight

**All supporting layer concepts are DERIVED from or PROJECTED from kernel concepts.**

**No supporting layer concept is essential for the system to exist.**

**The kernel is self-sufficient; the supporting layer adds value but is not required.**

---

# End of Supporting Layer Graph
