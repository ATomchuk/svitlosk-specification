# KNOWLEDGE_REPOSITORY_STRUCTURE

**Document ID:** K002-STRUCTURE

**Title:** Knowledge Repository Structure

**Document Class:** Knowledge Framework

**Status:** Stable

**Author:** SvitloSk Project — Knowledge Preservation Framework

---

# Purpose

This document designs the minimal repository structure for preserving architectural knowledge.

---

# Proposed Structure

```
knowledge/
    INDEX.md
    findings/
        KF-001_Publication_Creates_Identity.md
        KF-002_Identity_Not_Equal_Identifier.md
        KF-003_Publication_Bridges_Information_Representation.md
        KF-004_Reality_Is_Ontology_Foundation.md
        KF-005_Publication_Is_Irreducible.md
        KF-006_Issue_Is_Derivative.md
        KF-007_Information_Requires_Knower.md
        KF-008_Eight_Meta_Levels_Exist.md
        KNOWLEDGE_FINDINGS_INDEX.md
    principles/
        ARCHITECTURAL_KNOWLEDGE_PRINCIPLES.md
    models/
        (future: competing models, if needed)
    open_questions/
        (future: unresolved questions, if needed)
    superseded/
        (future: findings that are no longer valid)
```

---

# Structure Justification

## Why Minimal?

**Evidence:**

- Only 8 knowledge findings need to be preserved
- Only 10 principles need to be documented
- No models need to be preserved yet
- No open questions need to be preserved yet

**Rationale:**

- Structure should grow with knowledge, not pre-empt it
- Each finding is self-contained with its own file
- Principles are separate because they are meta-level knowledge
- Models and open questions are optional additions

---

## Why This Structure?

| Directory | Purpose | Justification |
|-----------|---------|---------------|
| knowledge/ | Root for all knowledge | Separates knowledge from specifications |
| findings/ | Validated findings | Each finding is self-contained |
| principles/ | Architectural principles | Meta-level knowledge |
| models/ | Competing models | Investigation artifacts |
| open_questions/ | Unresolved questions | Future research targets |
| superseded/ | Retired knowledge | Historical record |

---

# How Knowledge Differs from Specification

| Aspect | Knowledge | Specification |
|--------|-----------|---------------|
| Purpose | Preserves investigation findings | Defines system requirements |
| Status | Draft / Validated / Stable | Stable / Draft |
| Change frequency | High during investigation | Low after approval |
| Audience | Architects, researchers | Implementers, reviewers |
| Formality | Informal evidence | Normative requirements |
| Governance | No formal process | RFC / ADR process |

---

# How Knowledge Differs from ADR

| Aspect | Knowledge | ADR |
|--------|-----------|-----|
| Purpose | Records what was found | Records what was decided |
| Status | Draft / Validated | Accepted / Superseded |
| Change frequency | High during investigation | Low after approval |
| Audience | Architects, researchers | Implementers, reviewers |
| Formality | Informal evidence | Formal decision record |
| Governance | No formal process | Formal ADR process |

---

# How Knowledge Differs from Research

| Aspect | Knowledge | Research |
|--------|-----------|----------|
| Purpose | Preserves stable findings | Documents investigation process |
| Status | Validated / Stable | Complete / In Progress |
| Change frequency | Low after validation | High during investigation |
| Audience | Architects, researchers | Investigators |
| Formality | Semi-formal | Informal |
| Governance | Minimal | None |

---

# Key Insight

**Knowledge is a NEW category — distinct from Specification, ADR, and Research.**

**Knowledge preserves FINDINGS, not requirements, decisions, or processes.**

**The minimal structure is 2 directories: findings/ and principles/.**

---

# End of Knowledge Repository Structure
