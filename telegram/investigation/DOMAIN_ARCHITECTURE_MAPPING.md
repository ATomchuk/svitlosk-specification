# DOMAIN_ARCHITECTURE_MAPPING

**Document ID:** A66-MAPPING

**Title:** Domain-Architecture Mapping

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Dual Kernel Investigation

---

# Purpose

This document maps Architecture concepts to Domain concepts.

---

# Mapping Table

## One-to-One Mappings

| Architecture Concept | Domain Concept | Mapping Type |
|---------------------|----------------|--------------|
| Parser | Data Source | One-to-one |
| Data Storage | (none — storage is architectural) | No mapping |
| Telegram Channel | (none — channel is architectural) | No mapping |
| Telegram Publisher | (none — publisher is architectural) | No mapping |

---

## One-to-Many Mappings

| Architecture Concept | Domain Concepts | Mapping Type |
|---------------------|-----------------|--------------|
| Publication Engine | Publication, Schedule, Graphic | One-to-many |
| Schedule Generator | Outage Schedule, Queue, Subqueue | One-to-many |
| Graphic Generator | Outage Timeline, Availability Window, Outage Window | One-to-many |

---

## Many-to-One Mappings

| Architecture Concepts | Domain Concept | Mapping Type |
|----------------------|----------------|--------------|
| Parser, Publication Engine, Data Storage | Open Data | Many-to-one |
| Schedule Generator, Graphic Generator, Publication Engine | DSO | Many-to-one |
| Parser, Publication Engine | Community | Many-to-one |

---

## No Mapping

| Architecture Concept | Reason |
|---------------------|--------|
| Normalized Dataset | Implementation-specific format |
| Parsed Data | Implementation-specific format |
| Interpretation Result | Implementation-specific format |
| Publication Package | Collection concept (architectural) |
| Processing Cycle | Process concept (architectural) |
| Specification | Governance concept |
| Canonical Documentation | Governance concept |
| ADR | Governance concept |
| Normative Document | Governance concept |
| Telegram Bot API | Platform-specific interface |
| Rate Limiting | Platform-specific constraint |
| Repository | Storage-specific concept |
| Historical Archive | Storage-specific concept |

---

# Mapping Summary

| Mapping Type | Count |
|--------------|-------|
| One-to-one | 1 |
| One-to-many | 3 |
| Many-to-one | 3 |
| No mapping | 14 |
| **Total** | **21** |

---

# Key Insight

**Only 7 Architecture concepts have Domain mappings.**

**14 Architecture concepts have NO Domain mapping — they are purely implementation-specific.**

**This confirms the separation between Domain and Architecture kernels.**

---

# End of Domain-Architecture Mapping
