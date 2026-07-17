# Telegram Documentation Migration Plan

**Date:** 2026-07-13
**Status:** Prepared
**Source:** TELEGRAM_ARCHITECTURE_DECISION.md (Approved)
**Scope:** Migration from 8-document architecture to 7-document architecture

---

## Migration Objectives

1. Eliminate all SSOT violations (8 unique violations)
2. Eliminate the triple lifecycle duplication (TJS-002 + TJS-007 + TJS-008)
3. Eliminate the publication structure duplication (TJS-003 Post Structure + TJS-005 Message Templates)
4. Eliminate the formatting rules triplication (TJS-003 + TJS-004 + TJS-005)
5. Resolve the TJS-002 orphan status
6. Fix all incorrect cross-references
7. Standardize metadata across all documents
8. Create new documents for missing areas (Channel Management, Graphic Rendering)
9. Preserve ALL existing content — zero information loss

---

## Migration Principles

1. **No information loss.** Every section of every existing document is accounted for in the Migration Matrix.
2. **Deterministic execution.** Every operation is precisely defined. No ambiguity.
3. **Reversible where possible.** Before final deletion, source files are preserved as backup.
4. **Validation at every checkpoint.** After each phase, validation criteria are checked.
5. **Architecture Decision compliance.** Every operation traces to an approved AD.

---

## Migration Phases

### Phase 1: Pre-Migration Preparation

**Objective:** Create backup copies and validate source documents.

**Operations:**
1. Create backup directory: `telegram/_backup/`
2. Copy all 8 current TJS files to backup
3. Validate backup integrity (file count, byte comparison)

**Duration:** ~5 minutes
**Risk:** LOW
**Rollback:** Delete backup directory

**Checkpoint:** All 8 source files backed up successfully.

---

### Phase 2: Lifecycle Merge (AD-001, AD-004)

**Objective:** Create merged TJS-005 (Publication Lifecycle) from TJS-002 + TJS-007 + TJS-008.

**Operations:**
1. Create new file: `TJS-005-Publication-Lifecycle.md`
2. Absorb from TJS-002:
   - §3 Lifecycle Overview → unified lifecycle state model
   - §4 Publication Types
   - §5 Daily Schedule Lifecycle
   - §6 Emergency Publications
   - §7 Temporary Publications
   - §8 Update Rules (unified with TJS-007 §5, TJS-008 §11)
   - §9 Archive Policy
   - §10 Deletion Policy
   - §11 Traceability
   - §12 Reliability
3. Absorb from TJS-007:
   - §3 Publication Lifecycle (flow diagram)
   - §4 Publication Creation
   - §5 Publication Updates (merged into update rules)
   - §6 Canonical Equality
   - §7 Publication Ordering
   - §8 Temporary Publications (merged)
   - §9 Permanent Publications
   - §10 Publication Ownership
   - §11 Non-destructive Channel Principle
   - §12 Publication Lifecycle Diagram
   - §13 Error Handling
4. Absorb from TJS-008:
   - §3 Publication Cycle
   - §4 Daily Publication Package
   - §5 Tomorrow Publication Package
   - §6 Publication Windows
   - §7 Event-driven Publication Principle
   - §8 Stable Journal Principle
   - §9 Deterministic Daily Journal Principle
   - §10 Non-destructive Update Principle
   - §11 Update Policy (merged)
   - §12 Tomorrow Publication Lifecycle
   - §13 Manual Publications
   - §14 Image Publications
   - §15 Publication Session
   - §16 Daily Lifecycle Diagram
   - §17 Telegram Journal Architecture Diagram
5. Remove files:
   - `TJS-002-Publication-Lifecycle.md`
   - `TJS-007-Publication-Lifecycle.md`
   - `TJS-008-Publication-Lifecycle.md`

**Duration:** ~30 minutes
**Risk:** MEDIUM (merging 3 documents requires careful content reconciliation)
**Rollback:** Restore from backup

**Checkpoint:** New TJS-005 contains all content from all 3 source files. No content lost.

---

### Phase 3: Post Structure Absorption (AD-002, AD-003)

**Objective:** Absorb TJS-003 (Post Structure) into TJS-003 (Message Templates) and move formatting rules to TJS-002 (Editorial Policy).

**Operations:**
1. Update `TJS-005-Message-Templates.md` (will become TJS-003):
   - Absorb §3 Standard Publication Structure
   - Absorb §4 Header
   - Absorb §5 Main Information
   - Absorb §6 Graphic Block
   - Absorb §7 Additional Information
   - Absorb §8 Footer
   - Absorb §10 Editing Rules
2. Move to TJS-002 (Editorial Policy):
   - §9 Formatting Rules → absorbed into TJS-002 Formatting section
3. Remove file: `TJS-003-Post-Structure.md`

**Duration:** ~15 minutes
**Risk:** LOW (content is being absorbed, not lost)
**Rollback:** Restore from backup

**Checkpoint:** TJS-003 (Message Templates) contains all structural content. TJS-002 contains formatting policy. TJS-003 Post Structure removed.

---

### Phase 4: Metadata and Reference Updates (AD-005, AD-006, AD-009)

**Objective:** Fix metadata, cross-references, and outdated content.

**Operations:**
1. Update TJS-001:
   - Add Document Class: Normative
   - Add References section
   - Fix lowercase RFC 2119 keywords (line 83: "shall" → "SHALL")
   - Update §12 Future Specifications with correct document names
2. Update TJS-002 (Editorial Policy):
   - Add Document Class: Normative
   - Add References section
   - Remove Component field (line 7)
   - Absorb formatting rules from TJS-003 §9
3. Update TJS-003 (Message Templates):
   - Fix metadata (replace "Project: SvitloSk" and "Class: Normative" with standard fields)
   - Add Document Class: Normative
   - Absorb TJS-003 Post Structure content
4. Update TJS-004 (Rendering Rules):
   - Fix metadata (replace "Project: SvitloSk" and "Class: Normative" with standard fields)
   - Add Document Class: Normative
   - Fix incorrect reference §17: "TJS-003 — Editorial Policy" → "TJS-002 — Editorial Policy"

**Duration:** ~20 minutes
**Risk:** LOW
**Rollback:** Restore from backup

**Checkpoint:** All metadata standardized. All cross-references correct.

---

### Phase 5: New Document Creation (AD-008)

**Objective:** Create TJS-006 (Channel Management) and TJS-007 (Graphic Rendering).

**Operations:**
1. Create `TJS-006-Channel-Management.md`:
   - Document ID: TJS-006
   - Document Name: Channel Management
   - Document Class: Normative
   - Status: Draft
   - Responsibility: Telegram Bot API integration, rate limiting, message editing, channel administration, error recovery
   - Dependencies: TJS-001 (implicit), TJS-005 (declared), SSP-003 (Publication Engine)
2. Create `TJS-007-Graphic-Rendering.md`:
   - Document ID: TJS-007
   - Document Name: Graphic Rendering
   - Document Class: Normative
   - Status: Draft
   - Responsibility: Graphic generation rules, image formats, size constraints, graphic-to-text pairing, validation
   - Dependencies: TJS-001 (implicit), TJS-003 (declared), SSP-007 (Graphic Generator), SSP-003 (Publication Engine)

**Duration:** ~15 minutes
**Risk:** LOW (new documents, no content conflict)
**Rollback:** Delete new files

**Checkpoint:** Both new documents created with correct metadata and dependencies.

---

### Phase 6: Final Validation

**Objective:** Verify migration completeness and correctness.

**Operations:**
1. Run TELEGRAM_MIGRATION_VALIDATION.md checklist
2. Verify no duplicated responsibilities
3. Verify no orphan documents
4. Verify all references valid
5. Verify SSOT preserved
6. Verify SRP preserved
7. Verify Separation of Concerns preserved
8. Verify metadata complete
9. Verify dependencies valid
10. Verify document IDs preserved
11. Verify no information loss

**Duration:** ~15 minutes
**Risk:** LOW
**Rollback:** N/A (validation only)

**Checkpoint:** All validation criteria pass.

---

## Execution Order

```
Phase 1: Pre-Migration Preparation
    ↓
Phase 2: Lifecycle Merge (AD-001, AD-004)
    ↓
Phase 3: Post Structure Absorption (AD-002, AD-003)
    ↓
Phase 4: Metadata and Reference Updates (AD-005, AD-006, AD-009)
    ↓
Phase 5: New Document Creation (AD-008)
    ↓
Phase 6: Final Validation
```

**Total phases:** 6
**Estimated total duration:** ~100 minutes

---

## Rollback Strategy

| Phase | Rollback Action |
|-------|----------------|
| Phase 1 | Delete backup directory |
| Phase 2 | Restore all files from backup; delete new TJS-005 |
| Phase 3 | Restore TJS-003 Post Structure from backup; revert TJS-003 and TJS-002 |
| Phase 4 | Restore all files from backup |
| Phase 5 | Delete new TJS-006 and TJS-007 |
| Phase 6 | N/A (validation only) |

**Full rollback:** Restore all 8 original files from backup. Delete any new files.

---

## Validation Checkpoints

| Phase | Checkpoint | Criteria |
|-------|-----------|----------|
| Phase 1 | Backup complete | 8 files in backup directory, byte-identical to originals |
| Phase 2 | Lifecycle merged | New TJS-005 contains all content from TJS-002 + TJS-007 + TJS-008 |
| Phase 3 | Structure absorbed | TJS-003 (Message Templates) contains all structural content; TJS-003 Post Structure removed |
| Phase 4 | Metadata updated | All 7 documents have Document Class, References, uppercase RFC 2119 |
| Phase 5 | New documents created | TJS-006 and TJS-007 exist with correct metadata |
| Phase 6 | Validation passed | All criteria in TELEGRAM_MIGRATION_VALIDATION.md pass |

---

## Completion Criteria

Migration is COMPLETE when:

1. Exactly 7 TJS documents exist in `telegram/`
2. No TJS document has duplicated responsibility
3. No TJS document is orphaned
4. All cross-references are correct
5. All metadata is standardized
6. All content from all 8 original documents is preserved
7. The Approved Architecture (TELEGRAM_ARCHITECTURE_DECISION.md) is fully implemented
8. TELEGRAM_MIGRATION_VALIDATION.md checklist passes 100%

---

**End of Migration Plan**

**Planner:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
