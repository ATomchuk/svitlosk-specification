# RESEARCH_ARCHITECTURE

**Document ID:** META005-ARCHITECTURE

**Title:** Research Architecture

**Document Class:** Research Architecture

**Status:** Stable

**Author:** SvitloSk Project — Chief Research Architect

---

# Purpose

This document constructs the complete architecture of the research process itself.

---

# Research Architecture

## Research Objects

| Object | Category | Role |
|--------|----------|------|
| Question | Process | Triggers investigation |
| Investigation | Process | Systematic inquiry |
| Evidence | Knowledge | Supports conclusions |
| Models | Representation | Conceptual representations |
| Findings | Knowledge | Validated conclusions |
| Knowledge Units | Knowledge | Atomic knowledge |
| Contradictions | Relationship | Conflicts between statements |
| Principles | Knowledge | Architectural truths |
| Verification | Process | Confirmation of claims |
| Audit | Process | Independent examination |
| Canonical Knowledge | Knowledge | Permanent repository knowledge |
| Lock | State | Permanent closure |

---

## Research Processes

| Process | Input | Output | Participants |
|---------|-------|--------|--------------|
| Evidence Collection | Repository | Evidence Register | Researcher |
| Model Construction | Evidence | Model Inventory | Researcher |
| Cross-Examination | Models | Attack Analysis | Researcher |
| Contradiction Search | Models, Evidence | Contradiction Register | Researcher |
| Knowledge Extraction | Findings | Knowledge Units | Researcher |
| Verification | Knowledge Units | Verification Report | Verifier |
| Audit | Knowledge Units | Audit Report | Auditor |
| Canonical Promotion | Verified Knowledge | Canonical Knowledge | Curator |
| Lock | Canonical Knowledge | LOCK Status | Governance |

---

## Research States

| State | Description | Duration |
|-------|-------------|----------|
| UNKNOWN | No inquiry exists | Indefinite |
| QUESTIONED | Inquiry posed | Until investigation |
| INVESTIGATED | Investigation complete | After investigation |
| EVIDENCED | Evidence collected | After collection |
| MODELED | Models constructed | After modeling |
| EXAMINED | Cross-examination complete | After examination |
| FOUND | Findings validated | After validation |
| KNOWLEDGED | Knowledge extracted | After extraction |
| VERIFIED | Verification complete | After verification |
| AUDITED | Audit complete | After audit |
| CANONICAL | Promoted to Canonical | After promotion |
| LOCKED | Permanent closure | After locking |

---

## Research Dependencies

```text
Question
    │
    ▼
Investigation
    │
    ▼
Evidence
    │
    ▼
Models
    │
    ▼
Examination
    │
    ▼
Findings
    │
    ▼
Knowledge Units
    │
    ▼
Verification
    │
    ▼
Audit
    │
    ▼
Canonical Knowledge
    │
    ▼
Lock
```

---

# Key Insight

**Research is a SYSTEM with objects, processes, states, and dependencies.**

**The research architecture is as real as the software architecture it investigates.**

**Understanding the research architecture enables better research.**

---

# End of Research Architecture
