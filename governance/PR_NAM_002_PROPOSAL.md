# PR_NAM_002_PROPOSAL

**Document ID:** SEM-006

**Title:** PR-NAM-002 Proposal

**Document Class:** Principle Proposal

**Status:** PROPOSED

**Author:** SvitloSk Project

---

# 1. Proposed Principle

## PR-NAM-002 — Canonical Identifier Immutability

Canonical architectural identifiers become immutable after architectural stabilization.

### Definition

A canonical identifier is "architecturally stabilized" when:

1. It has been used consistently for at least one major specification release
2. It has a normative Glossary definition
3. It has been referenced across multiple documents
4. No architectural alternative has been proposed and accepted

### Implications

Once architecturally stabilized:

- The identifier SHALL NOT be renamed without Architecture Decision Record
- The identifier SHALL be translated as a single unit
- The identifier SHALL maintain its Glossary definition
- The identifier SHALL be treated as permanent repository identity

### Relationship to PR-NAM-001

PR-NAM-001 defines WHEN an identifier becomes a Proper Architectural Name.

PR-NAM-002 defines WHAT HAPPENS after it becomes one — it becomes immutable.

Together they form a complete naming governance:

PR-NAM-001: Canonicalization → PR-NAM-002: Immutability

---

# 2. Should PR-NAM-002 Be Required?

| Question | Assessment |
|----------|-----------|
| Does the repository need permanent identifier governance? | YES — 8 components, potential future growth |
| Is PR-NAM-001 sufficient? | PARTIAL — defines canonicalization but not immutability |
| Does PR-NAM-002 add value? | YES — explicitly defines post-stabilization rules |

---

# 3. Recommendation

**PR-NAM-002 should be adopted** to complete the naming governance framework. Together with PR-NAM-001, it provides permanent, deterministic naming rules for all future repository components.

---

**End of PR-NAM-002 Proposal**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** PROPOSED
