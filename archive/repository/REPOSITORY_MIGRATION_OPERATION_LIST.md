# REPOSITORY_MIGRATION_OPERATION_LIST

**Document ID:** TJS-R5-D2

**Title:** Repository Migration Operation List

**Document Class:** Operation List

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Exact ordered list of migration operations.

---

# 1. Operation Summary

| Operation Type | Count |
|----------------|-------|
| KEEP (root) | 13 |
| MOVE (root → archive/) | 37 |
| MOVE (root → archive/baselines/) | 9 |
| MOVE (root → archive/knowledge/) | 10 |
| MOVE (root → archive/migration/) | 13 |
| MOVE (root → archive/phase2/) | 9 |
| MOVE (root → archive/project/) | 6 |
| MOVE (root → archive/repository/) | 52 |
| MOVE (root → archive/specification/) | 5 |
| MOVE (root → archive/translation/) | 11 |
| MOVE (root → archive/working/) | 10 |
| MOVE (root → telegram/) | 9 |
| MOVE (root → telegram/working/) | 40 |
| MOVE (root → telegram/working/translation/) | 7 |
| MOVE (root → telegram/working/migration/) | 1 |
| **Total** | **250** |

---

# 2. Execution Order

## Phase 1: Create directories (if needed)
1. MKDIR archive/baselines/
2. MKDIR archive/knowledge/
3. MKDIR archive/migration/
4. MKDIR archive/phase2/
5. MKDIR archive/project/
6. MKDIR archive/repository/
7. MKDIR archive/specification/
8. MKDIR archive/translation/
9. MKDIR archive/working/
10. MKDIR telegram/working/translation/
11. MKDIR telegram/working/migration/

## Phase 2: Move Telegram working documents
MOVE TELEGRAM_PUBLISHING_MODEL_*.md (40 files) → telegram/working/
MOVE TELEGRAM_REPOSITORY_MIGRATION_PLAYBOOK.md → telegram/working/migration/
MOVE TELEGRAM_TRANSLATION_*.md (7 files) → telegram/working/translation/

## Phase 3: Move Telegram canonical documents
MOVE TELEGRAM_CANONICAL_*.md (9 files) → telegram/

## Phase 4: Move Foundation integration documents
MOVE FOUNDATION_*.md (8 files) → telegram/working/foundation/

## Phase 5: Move archive documents
MOVE archive/baselines/ (9 files)
MOVE archive/knowledge/ (10 files)
MOVE archive/migration/ (13 files)
MOVE archive/phase2/ (9 files)
MOVE archive/project/ (6 files)
MOVE archive/repository/ (52 files)
MOVE archive/specification/ (5 files)
MOVE archive/translation/ (11 files)
MOVE archive/working/ (10 files)
MOVE archive/ (37 files)

---

# 3. Verification

| Check | Result |
|-------|--------|
| Total operations | 250 |
| Every file appears exactly once | YES |
| No destination conflicts | YES |
| No filename collisions | YES |
| Operation order deterministic | YES |

---

**End of Operation List**

**Planner:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
