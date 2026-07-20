# ROOT_GOVERNANCE_BOUNDARY_FINAL

**Document ID:** GA-003

**Title:** Root vs Governance Boundary Final

**Document Class:** Boundary Model

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Root Documents — Why Root?

| # | Document | Why MUST it remain in Root? | Why MUST it NOT move to governance/? |
|---|----------|---------------------------|-------------------------------------|
| 1 | README.md | Navigation entry point — GitHub convention | README is navigation, not governance |
| 2 | CHARTER.md | Project identity — "what is this?" | Identity is NOT governance |
| 3 | PROJECT_PRINCIPLES.md | Foundation — defines how project works | Permanent Foundation, not active governance |
| 4 | DOCUMENT_INDEX.md | Navigation — "where do I find things?" | Navigation is NOT governance |
| 5 | EDITORIAL_STANDARDS.md | Foundation — defines editorial rules | Permanent Foundation, not active governance |
| 6 | GLOSSARY.md | Navigation + Foundation — "what do words mean?" | Permanent Foundation |
| 7 | RFC_PROCESS.md | Foundation — defines change process | Permanent Foundation |
| 8 | ARCHITECTURE.md | Foundation — defines system structure | Permanent Foundation |
| 9 | DATA_MODEL.md | Foundation — defines data model | Permanent Foundation |
| 10 | SYSTEM_OVERVIEW.md | Foundation — defines system overview | Permanent Foundation |
| 11 | TERRITORIAL_MODEL.md | Foundation — defines territory | Permanent Foundation |
| 12 | DOCUMENTATION_TRANSLATION_STANDARD.md | Foundation — defines translation rules | Permanent Foundation |
| 13 | SPECIFICATION_ENGINEERING_PROCESS.md | Foundation — defines engineering process | Permanent Foundation |

---

# 2. Governance Documents — Why governance/?

| # | Document | Why MUST it NOT remain in Root? | Why governance/ is correct? |
|---|----------|-------------------------------|---------------------------|
| 1 | PROJECT_BASELINE_v3.0.md | Snapshot, not identity/navigation | Baselines are versioned governance artifacts |
| 2 | TRANSLATION_KICKOFF.md | Specialized, not repo-wide | Translation is a governance domain |
| 3 | TRANSLATION_STYLE_GUIDE.md | Specialized, not repo-wide | Translation is a governance domain |
| 4 | TRANSLATION_QA_CHECKLIST.md | Specialized, not repo-wide | Translation is a governance domain |
| 5 | TRANSLATION_TERMINOLOGY_DECISION_REGISTER.md | Specialized, not repo-wide | Translation is a governance domain |
| 6 | TERMINOLOGY_FREEZE.md | Specialized, not repo-wide | Translation is a governance domain |
| 7 | TRANSLATION_RENDERING_MODEL.md | Specialized, not repo-wide | Translation is a governance domain |

---

# 3. Boundary Principle

**Root = permanent, normative, repository-wide foundation + navigation.**

**governance/ = active, versioned, domain-specific governance.**

The distinction is PERMANENCE and SCOPE. Foundation documents define the project forever. Governance documents serve a specific phase or domain.

---

**End of Root Governance Boundary**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
