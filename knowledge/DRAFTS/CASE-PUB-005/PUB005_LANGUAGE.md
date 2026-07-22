# PUB005_LANGUAGE

**Document ID:** CASE-PUB-005-LG

**Title:** Rule Language

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document extracts every verb used for publisher behavior.

---

# 2. Rule Language

## 2.1 Verb Inventory

| Verb | Usage | Frequency | Duplicate? |
|------|-------|-----------|------------|
| Create | RULE-001, RULE-014 | 2 | — |
| Update | RULE-002, RULE-016 | 2 | — |
| Replace | RULE-003, RULE-013 | 2 | — |
| Remove | RULE-004, RULE-008, RULE-010, RULE-027 | 4 | Yes (3 synonyms) |
| Archive | RULE-005 | 1 | — |
| Preserve | RULE-006 | 1 | — |
| Expire | RULE-007, RULE-009, RULE-011, RULE-012 | 4 | Yes (2 opposites) |
| Disappear | RULE-008, RULE-010 | 2 | Duplicate of Remove |
| Generate | RULE-014 | 1 | — |
| Edit | RULE-023 | 1 | — |
| Delete | RULE-024 | 1 | Duplicate of Remove |
| Send | RULE-021, RULE-022 | 2 | — |
| Group | RULE-018 | 1 | — |
| Order | RULE-019, RULE-020 | 2 | — |
| Follow | RULE-025 | 1 | — |
| Protect | RULE-026 | 1 | — |
| Show | RULE-017 | 1 | — |

---

## 2.2 Verb Analysis

### Create vs Generate

| Verb | Usage | Meaning |
|------|-------|---------|
| Create | Publication creation | New object |
| Generate | Graph generation | New object |

**Analysis:** Both mean "new object creation." Potentially synonymous.

---

### Update vs Edit

| Verb | Usage | Meaning |
|------|-------|---------|
| Update | Publication update | Modify existing |
| Edit | Channel message edit | Modify existing |

**Analysis:** Both mean "modify existing." Potentially synonymous.

---

### Replace vs Substitute

| Verb | Usage | Meaning |
|------|-------|---------|
| Replace | Graph replacement | Entire replacement |

**Analysis:** "Replace" is the only term used.

---

### Remove vs Delete vs Disappear

| Verb | Usage | Meaning |
|------|-------|---------|
| Remove | Publication removal | Remove from view |
| Delete | Channel message deletion | Remove from channel |
| Disappear | Publication disappearance | Remove from view |

**Analysis:** All three mean "remove from view." Potentially synonymous.

---

### Expire vs End vs Terminate

| Verb | Usage | Meaning |
|------|-------|---------|
| Expire | Publication expiry | End of lifetime |

**Analysis:** "Expire" is the only term used.

---

### Archive vs Preserve vs Store

| Verb | Usage | Meaning |
|------|-------|---------|
| Archive | Publication archival | Permanent storage |
| Preserve | Publication preservation | Permanent storage |

**Analysis:** Both mean "permanent storage." Potentially synonymous.

---

## 2.3 Verb Deduplication

| Canonical Verb | Synonyms | Usage |
|----------------|----------|-------|
| Create | Generate | New object creation |
| Update | Edit | Modify existing |
| Remove | Delete, Disappear | Remove from view |
| Archive | Preserve | Permanent storage |
| Expire | — | End of lifetime |
| Replace | — | Entire replacement |
| Send | — | Channel delivery |
| Group | — | Organization |
| Order | — | Sorting |
| Follow | — | Conformance |
| Protect | — | Safety |
| Show | — | Display |

---

# 3. Findings

## 3.1 Finding LG-001

**17 verbs identified.**

**Evidence:** Analysis of rule language.

**Confidence:** HIGH.

## 3.2 Finding LG-002

**4 verb groups have SYNONYMS.**

Create/Generate, Update/Edit, Remove/Delete/Disappear, Archive/Preserve.

**Evidence:** Analysis of verb analysis.

**Confidence:** HIGH.

## 3.3 Finding LG-003

**After deduplication, 12 canonical verbs remain.**

Create, Update, Remove, Archive, Expire, Replace, Send, Group, Order, Follow, Protect, Show.

**Evidence:** Analysis of verb deduplication.

**Confidence:** HIGH.

---

# 4. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| LG-001 | Analysis of rule language |
| LG-002 | Analysis of verb analysis |
| LG-003 | Analysis of verb deduplication |

---

**End of Rule Language**
