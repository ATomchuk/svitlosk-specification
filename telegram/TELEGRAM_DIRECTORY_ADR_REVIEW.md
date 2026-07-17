# TELEGRAM_DIRECTORY_ADR_REVIEW

**Document ID:** TJS-F1.2-R5

**Title:** Telegram Directory ADR Review

**Document Class:** ADR Placement Review

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Determine the permanent location of TELEGRAM_ARCHITECTURE_DECISION.md.

---

# 1. What ADR Represents

TELEGRAM_ARCHITECTURE_DECISION.md is an Architecture Decision Record. It:
- Documents approved architectural decisions
- Is referenced by ALL canonical specifications
- Governs architectural evolution
- Is permanent and normative
- Records which decisions were made and why

---

# 2. Is ADR a Specification?

**NO.**

ADR does NOT define system behaviour. It does NOT describe what the system DOES. It records which architectural decisions were approved and why.

---

# 3. Is ADR Architecture Governance?

**YES.**

ADR is architecture governance. It records decisions, rationale, and constraints. It is the authoritative source for architectural decisions.

---

# 4. Does ADR Belong to Foundation?

**YES.**

| Criterion | Assessment |
|-----------|-----------|
| Referenced by all specifications | YES — dependency direction: Foundation → Specs |
| Permanent and normative | YES — like Foundation |
| Not a specification | YES — does not define behaviour |
| Not a working material | YES — not temporary |

---

# 5. Alternatives

## Option A: foundation/

| Pros | Cons |
|------|------|
| Correct dependency direction | None |
| ADR is governance, not specification | |
| Permanent and normative | |
| Referenced by all specs | |

## Option B: specs/

| Pros | Cons |
|------|------|
| Near specifications | WRONG — ADR is not a specification |
| | Violates dependency direction |
| | Confuses governance with specification |

---

# 6. Recommendation: foundation/

**ADR belongs in foundation/.**

It is architecture governance, not a specification. It is referenced by all specifications. It is permanent and normative. Foundation/ is the correct architectural location.

---

**End of ADR Review**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE — ADR → foundation/
