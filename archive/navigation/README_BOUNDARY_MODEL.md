# README_BOUNDARY_MODEL

**Document ID:** TJS-N1.2-C6

**Title:** README Boundary Model

**Document Class:** Boundary Model

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Define EXACTLY which classes belong in README.

---

# 1. Document Class Boundary

| Document Class | README? | DOCUMENT_INDEX? | Both? | Neither? | Reason |
|---------------|---------|----------------|-------|----------|--------|
| Project Identity | YES | NO | NO | NO | Entry point material |
| Mission / Vision | YES | NO | NO | NO | Entry point material |
| Design Philosophy | YES | NO | NO | NO | Entry point material |
| Project Values | YES | NO | NO | NO | Entry point material |
| System Architecture (high-level) | YES | NO | NO | NO | Entry point material |
| Current Status | YES | NO | NO | NO | Entry point material |
| Roadmap | YES | NO | NO | NO | Entry point material |
| Contributing | YES | NO | NO | NO | Entry point material |
| License | YES | NO | NO | NO | Entry point material |
| Foundation Documents | NO | YES | NO | NO | Governance navigation |
| Engineering Process | NO | YES | NO | NO | Governance navigation |
| Translation Standard | NO | YES | NO | NO | Governance navigation |
| Component Specs (SSP) | NO | YES | NO | NO | Detailed navigation |
| Telegram Specs (TJS) | NO | YES | NO | NO | Detailed navigation |
| ADR | NO | YES | NO | NO | Detailed navigation |
| Release Artifacts | NO | NO | NO | YES | Historical, not navigable |
| Audit Artifacts | NO | NO | NO | YES | Historical, not navigable |

---

# 2. Boundary Rules

| Rule | Statement |
|------|-----------|
| BR-001 | README SHALL contain project identity, mission, values, philosophy, status, roadmap |
| BR-002 | README SHALL NOT contain detailed document listings |
| BR-003 | README SHALL link to DOCUMENT_INDEX for detailed navigation |
| BR-004 | Release artifacts SHALL NOT appear in README or INDEX |
| BR-005 | Audit artifacts SHALL NOT appear in README or INDEX |

---

# 3. Boundary Verdict

**The boundary is definitive.** README = entry point. DOCUMENT_INDEX = navigation. Release/Audit = neither.

---

**End of README Boundary Model**

**Modeler:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
