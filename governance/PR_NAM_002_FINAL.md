# PR_NAM_002_FINAL

**Document ID:** ARM-006

**Title:** PR-NAM-002 Final

**Document Class:** Principle

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. PR-NAM-002 — Canonical Identifier Immutability Principle

## Statement

Once a canonical architectural identifier becomes part of the normative architecture, it SHALL NOT be renamed unless an Architecture Decision Record explicitly supersedes the architecture.

## Definition of "Part of Normative Architecture"

A canonical identifier is part of the normative architecture when:

1. It has a normative definition in the Glossary
2. It has been used consistently across multiple specification versions
3. It has been referenced in at least one Stable canonical specification

## Implications

Once architecturally immutable:

- The identifier SHALL NOT be renamed without ADR
- The identifier SHALL be translated as a single unit (per PR-NAM-001)
- The identifier SHALL maintain its Glossary definition
- The identifier SHALL be treated as permanent repository identity

## Relationship to PR-NAM-001

| Principle | Governance Scope |
|-----------|-----------------|
| PR-NAM-001 | WHEN an identifier becomes a Proper Architectural Name (canonicalization criteria) |
| PR-NAM-002 | WHAT happens after — the identifier becomes immutable |

Together: PR-NAM-001 (Canonicalization) → PR-NAM-002 (Immutability)

---

# 2. Adoption Readiness

| Check | Result |
|-------|--------|
| Clear criteria for immutability | YES |
| Relationship to PR-NAM-001 defined | YES |
| Repository need demonstrated | YES — 8 components, potential future growth |
| No conflicts with existing principles | YES |

---

**End of PR-NAM-002**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
