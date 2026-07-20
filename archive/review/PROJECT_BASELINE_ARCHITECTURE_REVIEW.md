# PROJECT_BASELINE_ARCHITECTURE_REVIEW

**Document ID:** RA-003

**Title:** Project Baseline Architecture Review

**Document Class:** Architecture Review

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Should a Project Baseline Remain in Root?

**NO.**

A Project Baseline is a point-in-time snapshot of the repository state. It will be superseded by future baselines. It does not define HOW the repository works — it records WHAT the repository WAS.

---

# 2. Alternative Locations

| Location | Advantages | Disadvantages |
|----------|-----------|---------------|
| governance/baselines/ | Clean separation, organized by type | One more directory level |
| governance/ | Simple, all governance together | Baselines mixed with permanent rules |
| archive/baselines/ | Already has v1.0, v2.0, v2.1 | But v3.0 is current, not historical |
| project/ | Dedicated area | Would need to be created |

---

# 3. Recommended Location

**governance/baselines/**

Rationale:
- Baselines are governance artifacts (they record governance decisions)
- They deserve their own subdirectory because they grow over time (v1.0, v2.0, v2.1, v3.0...)
- Current v3.0 is ACTIVE — it should not be in archive/
- Future baselines (v4.0, v5.0) will follow the same pattern

---

# 4. Verdict

PROJECT_BASELINE_v3.0.md SHALL be moved to governance/baselines/.

---

**End of Baseline Architecture Review**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
