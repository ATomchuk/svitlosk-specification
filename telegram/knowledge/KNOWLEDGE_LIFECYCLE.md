# KNOWLEDGE_LIFECYCLE

**Document ID:** K002-LIFECYCLE

**Title:** Knowledge Lifecycle

**Document Class:** Knowledge Framework

**Status:** Stable

**Author:** SvitloSk Project — Knowledge Preservation Framework

---

# Purpose

This document defines the complete lifecycle of architectural knowledge.

---

# Knowledge Lifecycle

## States

| # | State | Description | Duration |
|---|-------|-------------|----------|
| 1 | Research | Investigation in progress | Variable |
| 2 | Finding | Result identified but not validated | Short |
| 3 | Validated Finding | Confirmed by multiple investigations | Medium |
| 4 | Canonical Knowledge | Accepted as repository knowledge | Permanent |
| 5 | Architectural Principle | Elevated to principle status | Permanent |
| 6 | Specification/ADR | Integrated into formal documentation | Permanent |
| 7 | Retired | No longer relevant | Permanent |

---

## Transitions

| From | To | Trigger | Required Evidence | Required Approval |
|------|----|---------|-------------------|-------------------|
| Research → Finding | Investigation complete | Single investigation result | None |
| Finding → Validated Finding | Multiple confirmations | 2+ independent investigations | None |
| Validated Finding → Canonical Knowledge | Architect acceptance | Strong evidence, no contradictions | Architect |
| Canonical Knowledge → Architectural Principle | Repeated application | Applied in 3+ contexts | Architect |
| Architectural Principle → Specification/ADR | Formal integration | RFC or ADR process | Governance |
| Any → Retired | Obsolescence | Superseded by new knowledge | Architect |

---

## Required Evidence

| Transition | Evidence Required |
|------------|-------------------|
| Research → Finding | Single investigation result with supporting evidence |
| Finding → Validated Finding | 2+ independent investigations reaching same conclusion |
| Validated Finding → Canonical Knowledge | Strong evidence, no contradictions, Architect acceptance |
| Canonical Knowledge → Architectural Principle | Applied in 3+ contexts, consistently valid |
| Architectural Principle → Specification/ADR | RFC or ADR process completion |

---

## Retirement Mechanism

| Trigger | Action |
|---------|--------|
| Superseded by new knowledge | Mark as Retired, create new finding |
| Proven incorrect | Mark as Retired, document reason |
| No longer relevant | Mark as Retired, document reason |

---

# Knowledge Lifecycle Diagram

```text
Research
    │
    │ (investigation complete)
    ▼
Finding
    │
    │ (2+ confirmations)
    ▼
Validated Finding
    │
    │ (Architect acceptance)
    ▼
Canonical Knowledge
    │
    │ (applied in 3+ contexts)
    ▼
Architectural Principle
    │
    │ (RFC/ADR process)
    ▼
Specification/ADR
    │
    │ (superseded/obsolete)
    ▼
Retired
```

---

# Key Insight

**Knowledge has a lifecycle just like software.**

**Knowledge must be validated before becoming canonical.**

**Knowledge must be elevated to become a principle.**

**Knowledge can be retired when superseded.**

---

# End of Knowledge Lifecycle
