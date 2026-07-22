# CASE001_PUBLICATION_CONTRADICTIONS

**Document ID:** CASE001B-CONTRADICTIONS

**Title:** Publication — Contradiction Search

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document searches for every contradiction concerning Publication — not only wording, but also identity, ownership, lifecycle, state, behaviour, relationships, projection, and representation.

---

# Contradictions Found

## Contradiction 1: Publication ID

**Documents:**

- DATA_MODEL.md §5: "Every logical entity SHALL be uniquely identifiable"
- No specification defines a Publication ID field

**Lines:**

- DATA_MODEL.md: logical integrity rules
- All TJS documents: no Publication ID mentioned

**Severity:** MEDIUM

**Possible Explanation:** DATA_MODEL.md states a general principle (unique identifiability) but no specification implements it for Publication. The principle may be satisfied by Territory + Date + Template composite key, but this is never explicitly stated.

---

## Contradiction 2: Temporary vs Permanent Classification

**Documents:**

- TJS-021 §4.4: "Archived Publications remain available in the Telegram Journal permanently"
- TJS-021 §5.5: "Only temporary Publications MAY be removed"
- GLOSSARY.md §3: "Tomorrow Publications SHALL expire after the reporting period ends"

**Lines:**

- TJS-021 §4.4, §5.5, §5.6
- GLOSSARY.md §3 (Tomorrow Publication definition)

**Severity:** LOW

**Possible Explanation:** The classification "temporary vs permanent" is clear for Tomorrow Publications (temporary) vs all others (permanent). But the boundary is implicit — no specification explicitly lists which Publication types are temporary. Tomorrow Publications are the only explicitly temporary type.

---

## Contradiction 3: Manual Publications Lifecycle

**Documents:**

- TJS-010 §5.2: "Publication Engine → Manual Publications: ILLEGAL"
- TJS-008 §14: "Publication Engine SHALL NOT modify or remove Image Publications"
- TJS-021 §4: Lifecycle states defined for Publications

**Lines:**

- TJS-010 §5.2 (Illegal Interactions)
- TJS-008 §14 (Image Publications)
- TJS-021 §4 (Lifecycle States)

**Severity:** HIGH

**Possible Explanation:** Manual Publications are called "Publications" but are excluded from the automatic lifecycle. They are created by different actors (Administrators), have different ownership, and cannot be modified by Publication Engine. This suggests Manual Publications may be a different concept sharing the name "Publication."

---

## Contradiction 4: Graphic Publications Lifecycle

**Documents:**

- TJS-022 §6: Graphic Publications have their own lifecycle (Generation → Validation → Delivery → Archive)
- TJS-021 §4: Publication lifecycle states (Generated → Published → Updated → Archived → Removed)

**Lines:**

- TJS-022 §6.1-6.4 (Graphic Publication Requirements)
- TJS-021 §4 (Lifecycle States)

**Severity:** MEDIUM

**Possible Explanation:** Graphic Publications have a different lifecycle than text Publications. TJS-022 defines 4 states (Generation → Validation → Delivery → Archive) while TJS-021 defines 5 states. Graphic Publications cannot be Updated (they are regenerated, not edited). This is evidence that Graphic Publications and text Publications are different concepts.

---

## Contradiction 5: Ownership Authority

**Documents:**

- TJS-021 §3.1: "Repository SHALL be the single authoritative source of truth"
- Legacy TJS-007 §10: "Ownership SHALL be determined by the stored Telegram Message ID"

**Lines:**

- TJS-021 §3.1 (Repository Authority Principle)
- Legacy TJS-007 §10 (Ownership Model)

**Severity:** LOW

**Possible Explanation:** The Repository Authority Principle (current) and Telegram Message ID ownership (legacy) represent different authority models. The current model supersedes the legacy model, but the legacy text remains in the repository. This is a documentation evolution issue, not a live contradiction.

---

## Contradiction 6: Lifecycle States Count

**Documents:**

- TJS-021 §4: 5 states (Generated, Published, Updated, Archived, Removed)
- Legacy TJS-002 §4: 6 states (Scheduled, Generated, Published, Updated, Archived, Removed)
- Legacy TJS-007 §4: 4 steps (Generate, Publish, Update, Archive)
- DATA_MODEL.md §4: 6 steps (Collected, Validated, Normalized, Interpreted, Published, Archived)

**Lines:**

- TJS-021 §4 (Current lifecycle)
- Legacy TJS-002 §4 (Legacy lifecycle)
- Legacy TJS-007 §4 (Legacy steps)
- DATA_MODEL.md §4 (Data lifecycle)

**Severity:** LOW

**Possible Explanation:** Different specifications define different lifecycle models. TJS-021 is the authoritative lifecycle specification. Legacy documents represent historical evolution. DATA_MODEL.md lifecycle describes the DATA lifecycle, not the Publication lifecycle. These are different projections.

---

## Contradiction 7: Platform Independence vs Telegram Mechanics

**Documents:**

- TJS-000 §3: "Telegram itself SHALL NOT be considered the Journal"
- GLOSSARY.md §3: "Publication MAY be distributed through multiple Publication Channels"
- TJS-021 §5.1: "Generated → Published: delivered to the Telegram channel"

**Lines:**

- TJS-000 §3 (Platform independence)
- GLOSSARY.md §3 (Publication Channel)
- TJS-021 §5.1 (Transition references Telegram explicitly)

**Severity:** MEDIUM

**Possible Explanation:** Publication is designed to be platform-independent, but lifecycle mechanics reference Telegram explicitly. The transition "Generated → Published" is defined as "delivered to the Telegram channel." If Publication were truly platform-independent, this transition would reference "a Publication Channel" not "the Telegram channel."

---

## Contradiction 8: Interpretation Result

**Documents:**

- GLOSSARY.md §3: "Publication SHALL be derived exclusively from an Interpretation Result"
- No normative document defines "Interpretation Result"

**Lines:**

- GLOSSARY.md §3 (Publication definition)
- All TJS documents: no Interpretation Result definition

**Severity:** HIGH

**Possible Explanation:** GLOSSARY.md references "Interpretation Result" as the source of Publications, but no specification defines what an Interpretation Result is. This is a knowledge gap — the concept is referenced but never defined.

---

## Contradiction 9: Issue Opening Trigger

**Documents:**

- TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated"
- TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"

**Lines:**

- TJS-021 §8.1 (Issue opening)
- TJS-000 §4 (Issue definition)

**Severity:** LOW

**Possible Explanation:** TJS-021 defines Issue opening as triggered by Publication generation. TJS-000 defines Issue as a calendar-day container. These are complementary definitions, not contradictions. Issue opening is the first Publication for that day.

---

## Contradiction 10: Archival Permanence vs Deletion

**Documents:**

- TJS-021 §4.4: "Archived Publications remain available in the Telegram Journal permanently"
- TJS-021 §5.6: "An Archived Publication SHALL NOT become Removed"
- TJS-021 §7.3: "Deletion SHALL occur only for temporary Publications"

**Lines:**

- TJS-021 §4.4, §5.6, §7.3

**Severity:** LOW

**Possible Explanation:** These are consistent statements, not contradictions. Archived Publications are permanent. Only temporary Publications can be removed. The apparent tension between "permanently" and "deletion" is resolved by the temporary/permanent classification.

---

## Contradiction 11: Canonical Equality vs Content Changes

**Documents:**

- TJS-010 §6.16: "Two publications generated from identical datasets SHALL be byte-for-byte identical"
- TJS-021 §6.2: "Publications MAY be updated when the normalized dataset changes"

**Lines:**

- TJS-010 §6.16 (Canonical Equality)
- TJS-021 §6.2 (Update philosophy)

**Severity:** LOW

**Possible Explanation:** These are not contradictory. Canonical Equality applies to publications generated from the SAME dataset. When the dataset changes, a different dataset produces a different publication. The equality is about determinism (same input → same output), not about immutability.

---

## Contradiction 12: Manual Publication Creation

**Documents:**

- TJS-010 §5.1: "Administrators → Telegram Channel: Manual Publication"
- TJS-010 §5.2: "Publication Engine → Manual Publications: ILLEGAL"

**Lines:**

- TJS-010 §5.1 (Approved Interactions)
- TJS-010 §5.2 (Illegal Interactions)

**Severity:** MEDIUM

**Possible Explanation:** Administrators can create Manual Publications directly to Telegram Channel, bypassing Publication Engine. This creates two creation paths for "Publications" — automatic (via Publication Engine) and manual (via Administrators). This is evidence of two different concepts sharing one name.

---

## Contradiction 13: Graphic Publication Types vs Publication Types

**Documents:**

- TJS-022 §5: 5 graphic publication types (T-001 through T-005)
- TJS-005: Canonical Templates (A, B, C, D) for text Publications

**Lines:**

- TJS-022 §5 (Graphic publication types)
- TJS-005 (Canonical Templates)

**Severity:** LOW

**Possible Explanation:** Graphic Publications and text Publications have different type systems. T-001 through T-005 are graphic types. A, B, C, D are text templates. These are different classification systems for different publication formats.

---

## Contradiction 14: Telegram Message ID as Ownership

**Documents:**

- Legacy TJS-007 §10: "Ownership SHALL be determined by the stored Telegram Message ID"
- TJS-010 §4.1: "Publication Engine owns Publications"
- TJS-021 §3.1: "Repository SHALL be the single authoritative source of truth"

**Lines:**

- Legacy TJS-007 §10 (Ownership model)
- TJS-010 §4.1 (Component ownership)
- TJS-021 §3.1 (Repository Authority)

**Severity:** LOW

**Possible Explanation:** Three different ownership models exist: Telegram Message ID (legacy), Publication Engine (current architectural), Repository Authority (current authoritative). The current model supersedes legacy. These represent evolution, not live contradiction.

---

# Contradiction Summary

| # | Topic | Severity | Resolved? |
|---|-------|----------|-----------|
| 1 | Publication ID | MEDIUM | Partially — composite key possible |
| 2 | Temporary/Permanent | LOW | Yes — implicit classification |
| 3 | Manual Publications Lifecycle | HIGH | No — different concept? |
| 4 | Graphic Publications Lifecycle | MEDIUM | Partially — different lifecycle |
| 5 | Ownership Authority | LOW | Yes — legacy superseded |
| 6 | Lifecycle States Count | LOW | Yes — different projections |
| 7 | Platform Independence | MEDIUM | No — Telegram explicit in mechanics |
| 8 | Interpretation Result | HIGH | No — undefined concept |
| 9 | Issue Opening Trigger | LOW | Yes — complementary |
| 10 | Archival Permanence | LOW | Yes — consistent |
| 11 | Canonical Equality | LOW | Yes — different conditions |
| 12 | Manual Publication Creation | MEDIUM | No — two creation paths |
| 13 | Graphic vs Text Types | LOW | Yes — different systems |
| 14 | Ownership Models | LOW | Yes — evolution |

---

# Severity Distribution

| Severity | Count |
|----------|-------|
| HIGH | 2 |
| MEDIUM | 4 |
| LOW | 8 |
| **Total** | **14** |

---

# Unresolved Contradictions

**4 contradictions remain unresolved:**

1. **Manual Publications Lifecycle** (HIGH) — Manual Publications are called "Publications" but excluded from automatic lifecycle. May be a different concept.
2. **Interpretation Result** (HIGH) — Referenced in GLOSSARY but never defined in any normative document.
3. **Platform Independence vs Telegram Mechanics** (MEDIUM) — Lifecycle transitions reference Telegram explicitly despite platform-independent design.
4. **Manual Publication Creation** (MEDIUM) — Two creation paths (automatic + manual) for "Publications."

---

# End of Contradiction Search
