# RESEARCH_LIFECYCLE

**Document ID:** META005-LIFECYCLE

**Title:** Research Lifecycle

**Document Class:** Research Architecture

**Status:** Stable

**Author:** SvitloSk Project — Chief Research Architect

---

# Purpose

This document reconstructs the complete lifecycle of architectural research.

---

# Research Lifecycle

## Lifecycle States

| # | State | Description | Duration |
|---|-------|-------------|----------|
| 0 | UNKNOWN | No inquiry exists | Indefinite |
| 1 | QUESTIONED | An inquiry has been posed | Until investigation begins |
| 2 | INVESTIGATED | Systematic inquiry has occurred | During investigation |
| 3 | EVIDENCED | Evidence has been collected | During investigation |
| 4 | MODELED | Multiple models have been constructed | During investigation |
| 5 | EXAMINED | Models have been cross-examined | During investigation |
| 6 | FOUND | Validated findings have been produced | After investigation |
| 7 | KNOWLEDGED | Findings have been extracted to Knowledge Base | After extraction |
| 8 | VERIFIED | Findings have been independently verified | After verification |
| 9 | AUDITED | Findings have been independently audited | After audit |
| 10 | CANONICAL | Findings have been promoted to Canonical | After promotion |
| 11 | LOCKED | Findings are permanently closed | After locking |

---

## Lifecycle Transitions

| From | To | Trigger | Required Evidence |
|------|----|---------|-------------------|
| UNKNOWN → QUESTIONED | Inquiry posed | Research question defined |
| QUESTIONED → INVESTIGATED | Investigation begins | Investigation started |
| INVESTIGATED → EVIDENCED | Evidence collected | Evidence register complete |
| EVIDENCED → MODELED | Models constructed | Model inventory complete |
| MODELED → EXAMINED | Cross-examination complete | Attack analysis complete |
| EXAMINED → FOUND | Findings validated | Multiple confirmations |
| FOUND → KNOWLEDGED | Knowledge extracted | Knowledge Base updated |
| KNOWLEDGED → VERIFIED | Independent verification | Verification audit passed |
| VERIFIED → AUDITED | Independent audit | Audit report complete |
| AUDITED → CANONICAL | Promotion to Canonical | Canonical Knowledge promoted |
| CANONICAL → LOCKED | Permanent closure | LOCK status granted |

---

## Lifecycle Diagram

```text
UNKNOWN
    │
    ▼
QUESTIONED
    │
    ▼
INVESTIGATED
    │
    ▼
EVIDENCED
    │
    ▼
MODELED
    │
    ▼
EXAMINED
    │
    ▼
FOUND
    │
    ▼
KNOWLEDGED
    │
    ▼
VERIFIED
    │
    ▼
AUDITED
    │
    ▼
CANONICAL
    │
    ▼
LOCKED
```

---

# Key Insight

**The research lifecycle has 12 states from UNKNOWN to LOCKED.**

**Each state has clear requirements for progression.**

**The lifecycle is LINEAR — each state depends on the previous.**

---

# End of Research Lifecycle
