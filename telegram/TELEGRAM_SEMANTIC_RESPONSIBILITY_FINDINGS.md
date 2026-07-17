# Telegram Semantic Responsibility Findings

**Date:** 2026-07-13
**Source:** TELEGRAM_SEMANTIC_RESPONSIBILITY_AUDIT.md
**Scope:** All findings from the semantic responsibility audit

---

## Finding Classification

Each finding answers:
1. Do both documents own the same responsibility? YES / NO
2. Would merging improve the architecture? YES / NO
3. Would merging violate Separation of Concerns? YES / NO
4. Would merging reduce clarity? YES / NO
5. Recommended decision: KEEP SEPARATE / MERGE / SPLIT / RENAME / RESTRUCTURE

---

## FINDING F-001: Triple Lifecycle State Model Duplication

**Documents:** TJS-002 §3, TJS-007 §3, TJS-008 §3

**Description:** All three documents define the publication lifecycle state model. TJS-002 defines 6 states (Generated, Scheduled, Published, Updated, Archived, Removed). TJS-007 defines 5 states (Dataset → Render → Publish → Update → Retain/Remove). TJS-008 defines 6 steps (generation, publication, monitoring, updating, Tomorrow generation, Tomorrow removal). The state models are DIFFERENT — they are not identical text, they are conflicting architectural definitions.

**Analysis:**
- TJS-002's model is conceptual (state-based)
- TJS-007's model is operational (flow-based)
- TJS-008's model is temporal (cycle-based)

These represent the SAME lifecycle from three different perspectives, but they define DIFFERENT state counts and DIFFERENT state names. This creates architectural ambiguity: which state model is authoritative?

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** — all three own "lifecycle state model" |
| Would merging improve the architecture? | **YES** — eliminates conflicting state models |
| Would merging violate Separation of Concerns? | **NO** — lifecycle states are ONE concept |
| Would merging reduce clarity? | **NO** — eliminates ambiguity about which model is authoritative |
| Recommended decision | **MERGE** |

**Justification:** Three documents defining three different state models for the same lifecycle is a critical architectural violation. One document must own the authoritative state model. The merged document would present a single, unified lifecycle state model.

---

## FINDING F-002: Triple Update Rules Duplication

**Documents:** TJS-002 §8, TJS-007 §5, TJS-008 §11

**Description:** All three documents define when publications may be updated. TJS-002 lists 3 conditions (source change, formatting correction, graphic regeneration). TJS-007 lists 2 conditions (dataset change, rendering change). TJS-008 lists 2 conditions (dataset change, rendering change). TJS-002 includes "formatting corrections" and "graphic regeneration" which the other two do not.

**Analysis:**
- TJS-002's conditions are broader (includes formatting)
- TJS-007 and TJS-008 are narrower (dataset or rendering only)
- The discrepancy creates ambiguity: can formatting corrections trigger updates?

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** — all three own "update rules" |
| Would merging improve the architecture? | **YES** — eliminates conflicting update conditions |
| Would merging violate Separation of Concerns? | **NO** — update rules are ONE concept |
| Would merging reduce clarity? | **NO** — resolves ambiguity about permitted update triggers |
| Recommended decision | **MERGE** |

**Justification:** Three documents with three slightly different sets of update conditions creates architectural ambiguity. One document must own the authoritative update rules.

---

## FINDING F-003: Triple Temporary Publications Duplication

**Documents:** TJS-002 §7, TJS-007 §8, TJS-008 §12

**Description:** All three documents define temporary publication rules. TJS-002 lists 3 types (Tomorrow schedule, Upcoming notice, Technical maintenance). TJS-007 and TJS-008 restrict to Tomorrow Publications only.

**Analysis:**
- TJS-002 is broader (3 types of temporary publications)
- TJS-007 and TJS-008 are narrower (Tomorrow only)
- The discrepancy creates ambiguity: are "Upcoming notices" and "Technical maintenance reminders" temporary?

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** — all three own "temporary publication rules" |
| Would merging improve the architecture? | **YES** — eliminates conflicting definitions of "temporary" |
| Would merging violate Separation of Concerns? | **NO** — temporary classification is ONE concept |
| Would merging reduce clarity? | **NO** — resolves ambiguity about what qualifies as temporary |
| Recommended decision | **MERGE** |

---

## FINDING F-004: Archive/Permanent Rules Duplication

**Documents:** TJS-002 §9, TJS-007 §9

**Description:** Both documents define archive/preservation rules. TJS-002 §9 (Archive Policy) says archive entries shall not be modified except to correct verified technical errors. TJS-007 §9 (Permanent Publications) says current-day publications shall remain and the Publisher shall not remove them.

**Analysis:**
- TJS-002 defines ARCHIVE policy (historical preservation)
- TJS-007 defines PERMANENT classification (current-day preservation)
- These are related but slightly different: archive = historical; permanent = current-day

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **PARTIALLY** — TJS-002 owns archive policy; TJS-007 owns permanent classification |
| Would merging improve the architecture? | **YES** — one document owns all preservation rules |
| Would merging violate Separation of Concerns? | **NO** — preservation rules are ONE concept at different lifecycle stages |
| Would merging reduce clarity? | **NO** — consolidates preservation rules in one place |
| Recommended decision | **MERGE** |

---

## FINDING F-005: Post Structure vs Message Templates Duplication

**Documents:** TJS-003, TJS-005

**Description:** TJS-003 defines publication structure (5 sections: Header, Main Info, Graphic, Additional Info, Footer). TJS-005 defines publication grammar (Territory Header → Sections → Settlement → Time → Street → Addresses) with 4 canonical templates.

**Analysis:**
- TJS-003 is conceptual (high-level section overview)
- TJS-005 is normative and detailed (canonical templates, grammar tree, validation)
- TJS-005's structure is MORE DETAILED and MORE AUTHORITATIVE than TJS-003
- TJS-003 does not add information that TJS-005 does not already cover (except Graphic block concept and Editing rules)

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** — both own "publication structure" |
| Would merging improve the architecture? | **YES** — eliminates dual ownership of structure |
| Would merging violate Separation of Concerns? | **NO** — publication structure is ONE concept |
| Would merging reduce clarity? | **NO** — TJS-005 is already the more authoritative source |
| Recommended decision | **MERGE** (absorb TJS-003 into TJS-005) |

**Justification:** TJS-003's 140 lines provide a conceptual overview that TJS-005's 405 lines already cover in greater detail. The unique content from TJS-003 (Graphic block §6, Additional information §7, Footer §8, Editing rules §10) can be absorbed as additional sections in TJS-005.

---

## FINDING F-006: Formatting Rules Triplication

**Documents:** TJS-003 §9, TJS-004 §11, TJS-005 §15

**Description:** Three documents define formatting rules:
- TJS-003 §9: "short paragraphs, consistent spacing, limited emoji usage, uniform typography, consistent ordering"
- TJS-004 §11: "bold; plain text. Italic, underline, spoiler, blockquote, code blocks prohibited"
- TJS-005 §15: "bold (<b>). No other formatting. Block quotes MAY be used by future specs"

**Analysis:**
- TJS-003 defines GENERAL formatting principles (spacing, typography)
- TJS-004 defines PERMITTED formatting types (bold + plain text)
- TJS-005 defines IMPLEMENTATION formatting (bold with <b> tag)
- These are at DIFFERENT abstraction levels but all claim authority over "formatting rules"

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** — all three own "formatting rules" at different levels |
| Would merging improve the architecture? | **YES** — one document owns all formatting rules |
| Would merging violate Separation of Concerns? | **NO** — formatting rules are ONE concept |
| Would merging reduce clarity? | **NO** — eliminates ambiguity about which formatting rules are authoritative |
| Recommended decision | **MERGE** (TJS-004 owns formatting policy; TJS-005 implements it) |

**Justification:** The resolution is to establish clear ownership: TJS-004 owns formatting POLICY (what is permitted). TJS-005 owns formatting IMPLEMENTATION (how to render in Telegram HTML). TJS-003's formatting rules are subsumed by TJS-004.

---

## FINDING F-007: Settlement Ordering Conflict

**Documents:** TJS-005 §7, TJS-006 §7

**Description:**
- TJS-005 §7: "Inside a Starosta District Publication, Settlements SHALL appear in the canonical order defined by TERRITORIAL_MODEL.md. Alphabetical sorting is prohibited. Parser ordering is prohibited."
- TJS-006 §7: "Settlements SHALL be ordered alphabetically using the Ukrainian alphabet."

These are DIRECTLY CONTRADICTORY. TJS-005 PROHIBITS alphabetical sorting. TJS-006 REQUIRES alphabetical sorting.

**Analysis:**
- This is not duplication — it is a semantic CONFLICT
- Two documents define mutually exclusive ordering rules
- One must be wrong, or the scope must be clarified

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **YES** — both own "settlement ordering" |
| Would merging improve the architecture? | N/A — this is a conflict, not just duplication |
| Would merging violate Separation of Concerns? | N/A |
| Would merging reduce clarity? | N/A |
| Recommended decision | **RESTRUCTURE** |

**Justification:** This conflict must be resolved architecturally. The question is: within a Starosta District Publication, are settlements ordered by TERRITORIAL_MODEL.md canonical order (TJS-005) or alphabetically (TJS-006)? This is an architectural decision that must be made and documented. The resolution should be: TJS-005 defines the canonical settlement order (for content); TJS-006 defines the rendering sort order (for display). If these are the same order, one document must reference the other. If they differ, the architectural intent must be clarified.

---

## FINDING F-008: Lifecycle Diagram Duplication

**Documents:** TJS-007 §12, TJS-008 §16-17

**Description:** Both documents contain lifecycle/architecture diagrams.
- TJS-007 §12: Parser → Engine → Publisher → Create/Update/Delete → Journal
- TJS-008 §16: Temporal daily lifecycle (00:00 → 05:00 → Generate → Publish → Monitor → Update → Tomorrow → Next day)
- TJS-008 §17: Architecture diagram (Sources → Parser → Dataset → Engine → Rendering → Journal)

**Analysis:**
- TJS-007's diagram shows OPERATIONAL flow (what components do)
- TJS-008's diagram shows TEMPORAL flow (when things happen)
- These are DIFFERENT diagrams for DIFFERENT purposes

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **PARTIALLY** — different diagram purposes |
| Would merging improve the architecture? | **YES** — all lifecycle diagrams in one place |
| Would merging violate Separation of Concerns? | **NO** — diagrams support the same lifecycle concept |
| Would merging reduce clarity? | **NO** — consolidates visual representations |
| Recommended decision | **MERGE** |

---

## FINDING F-009: TJS-004 Ownership Model Ambiguity

**Documents:** TJS-004 (Editorial Policy), TJS-005 (Message Templates)

**Description:** TJS-004 and TJS-005 both contain rules about territory presentation, time formatting, settlement formatting, address formatting, and formatting types. The question is whether this is duplication or normal cross-document cooperation.

**Analysis:**
- TJS-004 defines POLICY (what is allowed/required)
- TJS-005 defines IMPLEMENTATION (how to render in HTML)
- The overlap is CONSISTENT — TJS-005 implements TJS-004's rules
- This is CONTEXTUAL REUSE (Classification D), not SSOT violation

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** — TJS-004 owns policy, TJS-005 owns implementation |
| Would merging improve the architecture? | **NO** — they serve different abstraction levels |
| Would merging violate Separation of Concerns? | **YES** — mixing policy and implementation |
| Would merging reduce clarity? | **YES** — would conflate abstraction levels |
| Recommended decision | **KEEP SEPARATE** |

**Justification:** TJS-004 (Approved status) is the editorial authority. TJS-005 (Draft status) implements those rules in concrete templates. This is NORMAL cross-document cooperation. The relationship should be explicitly documented: "TJS-005 implements the editorial rules defined by TJS-004."

---

## FINDING F-010: Non-Distinguishable Non-Destructive Principles

**Documents:** TJS-007 §11, TJS-008 §10

**Description:**
- TJS-007 §11: "Non-destructive Channel Principle" — Publisher only touches its own posts
- TJS-008 §10: "Non-destructive Update Principle" — update in place, don't recreate

**Analysis:**
- These are RELATED but DISTINCT principles
- TJS-007's principle is about CHANNEL OWNERSHIP (don't touch others' posts)
- TJS-008's principle is about UPDATE STRATEGY (edit in place, don't delete+recreate)
- They address different concerns: one is about WHAT you may touch; the other is about HOW you may change it

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | **NO** — different non-destructive principles |
| Would merging improve the architecture? | **YES** — both principles belong in the lifecycle document |
| Would merging violate Separation of Concerns? | **NO** — both are lifecycle principles |
| Would merging reduce clarity? | **NO** — consolidates non-destructive principles |
| Recommended decision | **MERGE** (into unified Publication Lifecycle) |

---

## FINDING F-011: TJS-002 Isolation

**Documents:** TJS-002

**Description:** TJS-002 is not referenced by any other TJS document. It is an orphan in the dependency graph. Despite defining publication types, archive policy, deletion policy, traceability and reliability — none of these are referenced by TJS-005, TJS-006, TJS-007 or TJS-008.

**Analysis:**
- TJS-002's unique content (publication types, traceability, reliability) is NOT referenced by any other TJS
- TJS-002's overlapping content (lifecycle states, update rules) IS duplicated in TJS-007 and TJS-008
- TJS-002 appears to be an EARLIER draft that was superseded but never removed

| Question | Answer |
|----------|--------|
| Do both documents own the same responsibility? | N/A — TJS-002 is isolated |
| Would merging improve the architecture? | **YES** — absorbs TJS-002's unique content |
| Would merging violate Separation of Concerns? | **NO** |
| Would merging reduce clarity? | **NO** |
| Recommended decision | **MERGE** (absorb unique content into unified TJS-005) |

---

## Findings Summary

| Finding | Severity | Documents | Decision |
|---------|----------|-----------|----------|
| F-001: Triple lifecycle state model | CRITICAL | TJS-002, TJS-007, TJS-008 | MERGE |
| F-002: Triple update rules | CRITICAL | TJS-002, TJS-007, TJS-008 | MERGE |
| F-003: Triple temporary publications | MAJOR | TJS-002, TJS-007, TJS-008 | MERGE |
| F-004: Archive/Permanent rules | MAJOR | TJS-002, TJS-007 | MERGE |
| F-005: Post Structure vs Templates | MAJOR | TJS-003, TJS-005 | MERGE |
| F-006: Formatting rules triplication | MAJOR | TJS-003, TJS-004, TJS-005 | MERGE |
| F-007: Settlement ordering conflict | CRITICAL | TJS-005, TJS-006 | RESTRUCTURE |
| F-008: Lifecycle diagram duplication | MAJOR | TJS-007, TJS-008 | MERGE |
| F-009: Editorial policy ownership | MINOR | TJS-004, TJS-005 | KEEP SEPARATE |
| F-010: Non-destructive principles | MINOR | TJS-007, TJS-008 | MERGE |
| F-011: TJS-002 isolation | MAJOR | TJS-002 | MERGE |

---

## Severity Distribution

| Severity | Count |
|----------|-------|
| CRITICAL | 3 |
| MAJOR | 6 |
| MINOR | 2 |
| **Total** | **11** |

---

**End of Findings**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
