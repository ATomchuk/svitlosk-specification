# REPOSITORY_ROOT_PHILOSOPHY

**Document ID:** TJS-R4.2-P1

**Title:** Repository Root Philosophy

**Document Class:** Architectural Philosophy

**Status:** DEFINED

**Author:** SvitloSk Project

---

# Purpose

Define the official purpose of the repository root.

---

# 1. Repository Root Purpose

The repository root SHALL serve as the **navigation and governance entry point**.

It SHALL NOT serve as:

* An engineering dashboard
* A working workspace
* An archive of completed work

---

# 2. Root Functions

| Function | Belongs in Root? | Justification |
|----------|-----------------|---------------|
| Repository entry point (README.md) | YES | GitHub convention — every visitor starts here |
| Foundation navigation | YES | Foundation documents define the project |
| Contributor onboarding | YES | CHARTER + PRINCIPLES orient new contributors |
| Engineering governance | NO — belongs in governance/ | Not entry-point material |
| Subsystem specifications | NO — belongs in telegram/, specification/ | Too granular for root |
| Completed audits | NO — belongs in archive/ | Historical, not navigational |
| Working documents | NO — belongs in working/ | Active work not for visitors |

---

# 3. Root Philosophy Statement

**The repository root SHALL contain exactly those documents that a new contributor or external visitor needs to understand the project identity, navigate to subsystems, and find governance documents.**

Nothing else belongs in root.

---

# 4. Design Principles

| # | Principle | Application |
|---|-----------|------------|
| 1 | Minimal root | Only essential navigation and identity documents |
| 2 | Foundation at root | Foundation documents define the project — visible at first glance |
| 3 | Subsystems in directories | Each subsystem owns its own directory |
| 4 | Governance centralized | Engineering governance separated from Foundation |
| 5 | Archive hidden | Historical records not visible at root level |

---

**End of Root Philosophy**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** DEFINED
