# PR_NAM_001_PROPOSAL

**Document ID:** NPA-004

**Title:** PR-NAM-001 Proposal

**Document Class:** Principle Proposal

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. PR-NAM-001 — Proper Architectural Name Principle

## Statement

A canonical architectural identifier SHALL be treated as a Proper Architectural Name once it satisfies the repository canonicalization criteria.

## Canonicalization Criteria

| # | Criterion |
|---|-----------|
| 1 | The term has a normative definition in the Glossary |
| 2 | The term has exactly one architectural owner |
| 3 | The term has been stable across multiple specification versions |
| 4 | The term is used consistently across all relevant documents |
| 5 | The term is recognized by all repository stakeholders |

## Implications

Once an identifier becomes a Proper Architectural Name:

- It SHALL NOT be renamed without Architecture Decision Record
- It SHALL be translated as a single unit (not decomposed)
- It SHALL be treated as a permanent repository identity
- Its Glossary definition SHALL be maintained
- It SHALL NOT be decomposed into separate words for translation

## Application to Publication Engine

Publication Engine satisfies all 5 criteria:

| Criterion | Publication Engine |
|-----------|-------------------|
| Normative definition | YES — Glossary §14 |
| Unique owner | YES — Publishing Model |
| Stable identity | YES — multiple versions |
| Consistent usage | YES — 149 occurrences |
| Stakeholder recognition | YES — all references use this name |

---

# 2. Relationship to PR-ROOT-001

PR-NAM-001 supplements PR-ROOT-001 by defining the naming governance for architectural components.

---

**End of Principle Proposal**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
