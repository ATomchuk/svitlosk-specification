# TELEGRAM_GRAPHIC_PRINCIPLE_REFINEMENT

**Document ID:** TJS-G0.55-R1

**Title:** Graphic Principle Refinement

**Document Class:** Architectural Decision

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Resolve two remaining architectural questions before Architecture Freeze.

---

# 1. Task A — GP-004: Graphic Branding Constraint

## Question

Can something named "Constraint" be legitimately classified as an Architectural Principle?

## Analysis

The project maintains a clear architectural distinction between Principles and Constraints:

| Document | Principles Section | Constraints Section |
|----------|-------------------|-------------------|
| Editorial System | §4 (10 principles) | §6 (3 categories) |
| Publication Lifecycle | §3.1 (Repository Authority) | §10 (7 constraints) |
| Publishing Model | P-001→P-020 (20 principles) | §Constraints |

Principles are aspirational — they express philosophical stances.
Constraints are mandatory — they restrict specific behavior.

GP-004 states: "Every generated graphic SHALL contain official SvitloSk branding."

This is mandatory. It mandates specific visual elements (logo, name, date, timestamp). It does not express a philosophical stance — it restricts specific behavior.

## Decision: Option A — Remove from Principles, Move to Constraints

**Justification:**

1. The project architecture separates Principles from Constraints — they are different architectural elements.
2. A "principle named Constraint" is architecturally inconsistent.
3. Branding is mandatory, not aspirational — it is a constraint.
4. The Graphic subsystem already has constraints identified in the harvest (No Additional Colors, Auto-triggered, Supported Formats).
5. Branding fits naturally into the Constraints section alongside these existing constraints.

## Affected Documents

| Document | Change |
|----------|--------|
| TELEGRAM_GRAPHIC_CANONICAL_RECOMMENDATIONS.md | GP-004 removed from Principles, added to Constraints |
| TELEGRAM_GRAPHIC_PRINCIPLE_MATRIX.md | GP-004 row updated |
| TELEGRAM_GRAPHIC_PRINCIPLE_READINESS.md | Final principle set updated |
| TELEGRAM_GRAPHIC_FINAL_PRINCIPLES.md | GP-004 not listed as principle |

---

# 2. Task B — GP-001: Graphic Accessibility

## Question

Is GP-001 a truly independent Graphic Principle OR merely a specialization of Editorial Accessibility?

## Analysis

### Editorial §4.9 (Accessibility)

> "Publications SHALL be accessible to all residents of the Starokostiantyniv Territorial Community regardless of their technical experience, device capabilities, or access limitations."

**Scope:** ALL publications — text, graphics, any format.
**Dimension:** Content accessibility — can residents UNDERSTAND the information?
**Key phrase:** "device capabilities" — already covers display types and screen sizes.

### GP-001 (Graphic Accessibility)

> "Graphics SHALL remain readable on all display types, including light displays, dark displays, and small mobile screens."

**Scope:** ONLY graphics.
**Dimension:** Visual readability — can residents SEE the graphic on their device?
**Key phrase:** "all display types" — specific to graphic visual rendering.

### Overlap Analysis

| Dimension | Editorial §4.9 | GP-001 |
|-----------|----------------|--------|
| Scope | All publications | Only graphics |
| "Device capabilities" | YES — covers display types | YES — specifies display types |
| "Access limitations" | YES — covers visual impairments | NO — not addressed |
| "Technical experience" | YES — covers reading ability | NO — not addressed |
| "Light/dark displays" | IMPLICITLY — via "device capabilities" | EXPLICITLY — specified |
| "Small mobile screens" | IMPLICITLY — via "device capabilities" | EXPLICITLY — specified |

### Conclusion

GP-001 IS a specialization of Editorial §4.9. It does not introduce a new philosophical stance — it applies the same stance to graphics specifically. Editorial §4.9 already covers "device capabilities" which includes display types and screen sizes.

## Decision: REFERENCE ONLY

**Justification:**

1. Editorial §4.9 already covers accessibility including "device capabilities."
2. GP-001 is a SPECIALIZATION, not an INDEPENDENT principle.
3. The Graphic subsystem SHALL reference Editorial §4.9 for accessibility governance.
4. The Graphic Constraints section SHALL specify visual readability requirements as constraints, referencing Editorial §4.9 as the governing principle.

## Implementation

The Graphic subsystem SHALL:
- Reference Editorial §4.9 as the accessibility principle
- Specify in Constraints: "Graphics SHALL remain readable on all display types"
- NOT own accessibility as a principle

---

# 3. Task C — Remaining Philosophy Verification

After Tasks A and B, the remaining Graphic Philosophy consists of:

| # | Element | Type | Unique? | Owned by Graphic? | Duplicated? |
|---|---------|------|---------|-------------------|-------------|
| 1 | Graphic Automation | Principle | YES | YES | NO |
| 2 | Graphic Clarity | Principle | YES | YES | NO |
| 3 | Graphic Branding | Constraint | YES | YES | NO |
| 4 | Graphic Accessibility | Constraint | YES | YES | NO (references Editorial §4.9) |

### Verification

| Check | Result |
|-------|--------|
| No duplicated principles | YES |
| One owner per principle | YES |
| No principle named "Constraint" | YES — GP-004 moved to Constraints |
| No duplicated Accessibility | YES — references Editorial §4.9 |
| No duplicated Branding | YES — unique to Graphic |
| Not owned by Publishing | YES |
| Not owned by Editorial | YES |
| Not owned by Lifecycle | YES |
| Not owned by Glossary | YES |
| Not owned by Semantic Foundation | YES |

**Result:** PASS — 10/10 checks passed

---

# 4. Summary

| Decision | Action | Justification |
|----------|--------|--------------|
| GP-004 (Branding) | Move to Constraints | Mandatory, not aspirational. Architecturally inconsistent as "principle named Constraint." |
| GP-001 (Accessibility) | Reference Editorial §4.9 | Specialization of existing principle. Not independent. |

**Final Graphic Philosophy: 2 Principles + 2 Constraints**

---

**End of Refinement**

**Decider:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
