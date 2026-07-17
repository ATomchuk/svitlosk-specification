# TELEGRAM_GRAPHIC_CANONICAL_RECOMMENDATIONS

**Document ID:** TJS-G0.5-R5

**Title:** Graphic Canonical Principle Recommendations

**Document Class:** Recommendations

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Produce the final recommended Graphic Principle Set. This SHALL become the future permanent Graphic philosophy.

---

# 1. Final Graphic Principle Set

## GP-001: Graphic Accessibility

**Principle:** Графічна доступність

Graphics SHALL remain readable on all display types, including light displays, dark displays, and small mobile screens. Graphic publications SHALL be accessible to all residents regardless of their device capabilities.

This principle governs graphic decisions about visual readability. It ensures that graphics serve all residents, not just those with high-end devices.

This principle SHALL NOT regulate: what data is used for graphics, how graphics are generated, what lifecycle states graphics pass through, or how the Telegram channel delivers graphics.

---

## GP-002: Graphic Automation

**Principle:** Графічна автоматизація

Graphics SHALL be generated automatically from normalized data without manual editing. The graphic generation process SHALL be triggered automatically after successful schedule generation. Manual intervention SHALL NOT be part of the standard graphic workflow.

This principle governs graphic decisions about automation and manual intervention. It defines the boundary between automatic generation and manual editing for graphic publications.

This principle SHALL NOT regulate: what data is used for graphics, how schedules are generated, what editorial decisions are made, or how the Telegram channel delivers graphics.

---

## GP-003: Graphic Clarity

**Principle:** Графічна ясність

Graphics SHALL be clear, minimalistic, and easy to understand at a glance. Graphic publications SHALL communicate outage information through visual simplicity, using proportional timelines, consistent color coding, and clean layout. Visual complexity SHALL NOT obscure the information.

This principle governs graphic decisions about visual design quality. It ensures that graphics communicate information effectively through visual simplicity.

This principle SHALL NOT regulate: what data is used for graphics, how graphics are generated, what branding elements are applied, or how the Telegram channel delivers graphics.

---

## GP-004: Graphic Branding Constraint

**Constraint:** Обмеження брендування графіки

Every generated graphic SHALL contain official SvitloSk branding: SvitloSk logo, project name, publication date, and generation timestamp. Branding elements SHALL be consistently applied across all graphic types.

This constraint governs graphic identity and brand consistency. It ensures that every graphic is identifiable as an official SvitloSk publication.

This constraint SHALL NOT regulate: what data is used for graphics, how graphics are generated, what colors represent outage states, or how the Telegram channel delivers graphics.

---

# 2. Referenced Principles (Not Owned)

The Graphic subsystem SHALL reference the following principles from other subsystems:

| # | Principle | Owner | Reference |
|---|-----------|-------|-----------|
| 1 | Deterministic Rendering (P-016) | Publishing | "Same input produces identical output" |
| 2 | Visual Stability (P-015) | Publishing | "Journal remains visually stable" |
| 3 | Source Fidelity (P-017) | Publishing | "Rendering SHALL NOT modify official information" |
| 4 | Consistency (§4.8) | Editorial | "Every publication consistent and predictable" |
| 5 | Accessibility (§4.9) | Editorial | "All residents can obtain and understand information" |
| 6 | Timeliness (§4.10) | Editorial | "Publications delivered promptly" |
| 7 | Repository Authority (§3.1) | Lifecycle | "Repository is SSOT for publication state" |

---

# 3. Referenced Constraints (Not Owned)

| # | Constraint | Owner | Reference |
|---|-----------|-------|-----------|
| 1 | No Additional Colors | Graphic Model | SSP-007 §8 — "No additional semantic colors" |
| 2 | Auto-triggered | Graphic Model | SSP-007 §10 — "Generation triggered automatically" |
| 3 | Supported Formats: PNG/SVG | Graphic Model | SSP-007 §5 — "Generator SHALL support PNG, SVG" |
| 4 | Invalid Graphics Never Published | Graphic Model | SSP-007 §11 — "Invalid graphics SHALL never be published" |
| 5 | Graphics Never Modify Source Data | Repository Authority | §3.1 — "Repository is SSOT" |
| 6 | Graphics Never Become Source of Truth | Repository Authority | §3.1 — "Repository is SSOT" |

---

# 4. Philosophy Summary

| Dimension | Value |
|-----------|-------|
| Total principles owned | 4 |
| Total constraints owned | 6 |
| Total principles referenced | 7 |
| Total constraints referenced | 6 |
| Philosophy style | Minimal, professional, internally consistent |
| Industry alignment | Google, Microsoft, Kubernetes documentation practices |

---

# 5. Naming Conventions

| Name | Ukrainian | Stable? | Professional? |
|------|-----------|---------|---------------|
| Graphic Accessibility | Графічна доступність | YES | YES |
| Graphic Automation | Графічна автоматизація | YES | YES |
| Graphic Clarity | Графічна ясність | YES | YES |
| Graphic Branding Constraint | Обмеження брендування графіки | YES | YES |

---

**End of Canonical Recommendations**

**Recommender:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
