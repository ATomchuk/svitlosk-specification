# Telegram Document Dependency Graph

**Date:** 2026-07-13
**Scope:** Architectural dependency graph
**Status:** GRAPH DESIGNED

---

# Purpose

This document defines the dependency direction for every architectural group.

---

# Dependency Diagram

```text
                    ┌─────────────────┐
                    │   Foundation    │
                    │ (TJS-000, etc.) │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Architecture  │
                    │ (ADR, Blueprints)│
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
   ┌────────▼────────┐ ┌────▼─────┐ ┌────────▼────────┐
   │    Publishing   │ │ Editorial│ │    Lifecycle    │
   │   (Blueprint)   │ │(Blueprint)│ │   (Semantics)   │
   └────────┬────────┘ └────┬─────┘ └────────┬────────┘
            │                │                │
            └────────────────┼────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Specifications│
                    │   (Template)    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │     Legacy      │
                    │  (Historical)   │
                    └─────────────────┘
```

---

# Dependency Rules

| Group | Depends On | Referenced By | May Reference | Must NOT Reference |
|-------|-----------|---------------|---------------|-------------------|
| Foundation | CHARTER, PROJECT_PRINCIPLES, GLOSSARY | All groups | — | — |
| Architecture | Foundation | All groups | Foundation | — |
| Publishing | Foundation, Architecture | Specifications, Processes | Foundation, Architecture | Legacy |
| Editorial | Foundation, Architecture | Specifications, Processes | Foundation, Architecture | Legacy |
| Lifecycle | Foundation, Architecture | Specifications, Processes | Foundation, Architecture | Legacy |
| Graphics | Foundation, Architecture | Specifications, Processes | Foundation, Architecture | Legacy |
| Specifications | Foundation, Architecture | Processes | Foundation, Architecture, Publishing, Editorial, Lifecycle, Graphics | Legacy |
| Legacy | — | Reference | — | — |
| Processes | Foundation, Architecture | Reference | Foundation, Architecture, Publishing, Editorial, Lifecycle, Graphics | Legacy |
| Reference | Foundation | All groups | Foundation | — |

---

**End of Dependency Graph**

**Designer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
