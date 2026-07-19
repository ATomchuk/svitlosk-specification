# INTERNATIONAL_REPOSITORY_COMPARISON

**Document ID:** TJS-R4.2-P5

**Title:** International Repository Comparison

**Document Class:** Comparison

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Compare SvitloSk against international repository practice.

---

# 1. Repository Type Comparison

| Practice | SvitloSk | GitHub Standard | Compliant? |
|----------|----------|----------------|-----------|
| README.md at root | YES | YES | YES |
| Governance at root | YES — 12 Foundation docs | Common for standards repos | YES |
| Subsystems in directories | YES — telegram/ | Standard practice | YES |
| Working artifacts in subdirectories | YES — working/ | Standard practice | YES |
| Archive in subdirectories | YES — archive/ | Standard practice | YES |
| Documentation separate from code | YES — specification/ | Standard practice | YES |

---

# 2. Standards Repository Comparison

| Repository | Root Strategy | SvitloSk Alignment |
|-----------|---------------|-------------------|
| CNCF specifications | README + governance at root | ALIGNED |
| Kubernetes specifications | README + governance at root | ALIGNED |
| IETF RFCs | README + process at root | ALIGNED |
| W3C standards | README + standards at root | ALIGNED |

---

# 3. Intentional Deviations

| # | Deviation | Justification |
|---|-----------|--------------|
| 1 | No CHANGELOG.md | Changelog maintained through git history and PROJECT_BASELINE documents |
| 2 | No CONTRIBUTING.md | Contributor guidance is in CHARTER.md and PROJECT_PRINCIPLES.md |
| 3 | No LICENSE file | License is declared in CHARTER.md |

---

# 4. Comparison Verdict

**SvitloSk follows international standards repository practice.** 3 intentional deviations — all justified by existing governance documents.

---

**End of International Repository Comparison**

**Comparator:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
