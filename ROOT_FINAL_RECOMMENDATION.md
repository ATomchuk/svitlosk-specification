# ROOT_FINAL_RECOMMENDATION

**Document ID:** RA-006

**Title:** Root Final Recommendation

**Document Class:** Architecture Decision

**Status:** DECIDED

**Author:** SvitloSk Project

---

# 1. Current Architecture

`
Root (20 files)
    +-- 13 Foundation
    +-- 1 Baseline (PROJECT_BASELINE_v3.0.md)
    +-- 6 Translation governance
`

---

# 2. Recommended Architecture

`
Root (13 files — Foundation only)
    +-- README.md
    +-- 12 Foundation documents

governance/
    +-- baselines/       (PROJECT_BASELINE_v3.0.md)
    +-- translation/     (6 translation governance docs)

archive/
    +-- navigation/      (42 files)
    +-- review/          (8 files)
    +-- translation-preparation/ (8 files)
    +-- baselines/       (8 files — historical baselines + status snapshots)
    +-- engineering/     (3 files)
`

---

# 3. Migration Required?

**YES — 7 files need additional relocation beyond H-1:**

| # | File | From | To |
|---|------|------|----|
| 1 | PROJECT_BASELINE_v3.0.md | root/ | governance/baselines/ |
| 2 | TRANSLATION_KICKOFF.md | root/ | governance/translation/ |
| 3 | TRANSLATION_STYLE_GUIDE.md | root/ | governance/translation/ |
| 4 | TRANSLATION_QA_CHECKLIST.md | root/ | governance/translation/ |
| 5 | TRANSLATION_TERMINOLOGY_DECISION_REGISTER.md | root/ | governance/translation/ |
| 6 | TERMINOLOGY_FREEZE.md | root/ | governance/translation/ |
| 7 | TRANSLATION_RENDERING_MODEL.md | root/ | governance/translation/ |

Plus H-1's 65 files.

**Total: 72 files relocated. Root: 13 files.**

---

# 4. Architectural Impact

| Dimension | Impact |
|-----------|--------|
| Foundation | NONE — unchanged |
| Telegram | NONE — unchanged |
| SSP | NONE — unchanged |
| ADR | NONE — unchanged |
| Translation governance | IMPROVED — organized under governance/ |
| Baseline governance | IMPROVED — organized under governance/ |
| Root | IMPROVED — 13 files, pure Foundation |

---

# 5. Risk

| Risk | Level | Mitigation |
|------|-------|-----------|
| Broken references | LOW | DOCUMENT_INDEX uses Document IDs, not paths |
| Translation workflow disruption | LOW | Files are in same repo, just different directory |
| Git history | NONE | Moves tracked by Git |

---

# 6. Alternative Architecture

If designing from zero:

`
Root: README.md + 12 Foundation = 13 files
governance/baselines/
governance/translation/
archive/ (organized by type)
`

This IS the recommended architecture. The only change from current is moving 7 files.

---

# 7. Final Recommendation

**Implement both H-1 (65 files) and H-1A (7 additional files) in a single migration.**

**Root: 85 files -> 13 files (85% reduction).**

**PR-ROOT-001 compliance: 100%.**

---

**End of Final Recommendation**

**Recommender:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** DECIDED
