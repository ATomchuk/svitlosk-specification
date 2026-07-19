# FOUNDATION_BOUNDARY_MODEL

**Document ID:** TJS-R4.2-P2

**Title:** Foundation Boundary Model

**Document Class:** Boundary Model

**Status:** DEFINED

**Author:** SvitloSk Project

---

# Purpose

Define what is Foundation and what is not.

---

# 1. Foundation Definition

Foundation documents are **permanent, normative, repository-wide governance documents** that define:

* project identity and principles
* documentation standards
* engineering processes
* translation standards
* terminology and data models
* architecture and system overview

---

# 2. Foundation Ownership Criteria

A document SHALL belong to Foundation if and only if:

| Criterion | Required |
|-----------|----------|
| Permanent | YES — not superseded by future work |
| Normative | YES — defines rules for the entire repository |
| Repository-wide | YES — applies to all subsystems, not just Telegram |
| Governance | YES — defines how the repository operates |
| Stable | YES — approved through governance process |

A document SHALL NOT belong to Foundation if:

| Criterion | Disqualifies |
|-----------|-------------|
| Temporary | YES — completed audits, reports, certificates |
| Subsystem-specific | YES — Telegram-only documents |
| Working | YES — in-progress work |
| Historical | YES — superseded by newer versions |

---

# 3. Foundation vs Governance

| Dimension | Foundation | Governance |
|-----------|-----------|------------|
| Purpose | Permanent platform knowledge | Engineering process tracking |
| Stability | Frozen until ADR | Updated each release |
| Scope | Repository-wide | Repository-wide |
| Location | Root (visible) | governance/ (separate) |
| Example | CHARTER.md | PROJECT_BASELINE_v2.1.md |

---

# 4. Foundation Boundary Statement

**Foundation documents are the permanent, normative, repository-wide governance layer. They define WHAT the project is and HOW it operates. They live at the repository root for maximum visibility.**

---

**End of Foundation Boundary Model**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** DEFINED
