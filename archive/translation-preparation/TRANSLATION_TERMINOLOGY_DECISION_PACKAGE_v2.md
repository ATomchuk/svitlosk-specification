# TRANSLATION_TERMINOLOGY_DECISION_PACKAGE_v2

**Document ID:** TOD-002

**Title:** Translation Terminology Decision Package v2

**Document Class:** Decision Package

**Status:** READY FOR OWNER APPROVAL

**Author:** SvitloSk Project

---

# 1. Publication Engine

| Field | Value |
|-------|-------|
| English term | Publication Engine |
| Category | A — Architecture Terms |
| Meaning inside SvitloSk | The architectural Component implementing the Publisher Role. Responsible for generating and distributing Publications. One of 8 primary components in the Telegram subsystem. Defined in TELEGRAM_GLOSSARY.md: "The architectural Component implementing the Publisher Role." |

## Re-evaluation

The previous analysis concluded that "Publication Engine" is an **architectural Component**. This creates a tension with the word "Engine":

- "Engine" implies a processing mechanism
- "Component" is the architectural classification

The question is whether the Ukrainian translation should reflect the **architectural classification** (Component) or the **functional name** (Engine).

### Candidates Re-evaluated

| # | Candidate | Architectural Justification |
|---|-----------|--------------------------|
| 1 | Движок публікацій | Reflects the functional name "Engine." Natural Ukrainian IT term. Widely understood. Does NOT reflect the architectural classification as Component. |
| 2 | Компонент публікацій | Reflects the architectural classification. Precise. But loses the "Engine" identity — the term would become generic. |
| 3 | Компонент Publication Engine | Hybrid. Preserves the proper name while adding the classification. But mixes languages. |

### Architectural Justification

In the Telegram subsystem, there are 8 Components: Parser, Publication Engine, Publisher (Role), Telegram Publisher, Schedule Generator, Graphic Generator, Data Storage, Telegram Channel.

The English name "Publication Engine" is a **proper name** for this Component — it is NOT a generic description. The Glossary defines it as "The architectural Component implementing the Publisher Role."

Therefore: the Ukrainian translation should preserve the proper name's identity while being natural in Ukrainian.

### Final Recommendation

| Field | Value |
|-------|-------|
| Approved Ukrainian equivalent | Движок публікацій |
| Rejected alternatives | Компонент публікацій (too generic — loses proper name identity), Механізм публікацій (less natural in IT), Система публікацій (too broad) |
| Reason for rejection | Компонент публікацій would make the term generic — every component would be a "Component of X." "Publication Engine" is a proper name. |
| Rationale | "Движок публікацій" is the natural Ukrainian IT term for "engine." It preserves the proper name identity while being immediately understandable. The architectural classification (Component) is established by context, not by the name. |
| Date approved | PENDING OWNER APPROVAL |
| Approved by | PENDING |
| Status | **PENDING OWNER APPROVAL** |

---

# 2. Canonical Equality

| Field | Value |
|-------|-------|
| English term | Canonical Equality |
| Category | B — Deterministic Terms |
| Meaning inside SvitloSk | The guarantee that two publications generated from identical datasets SHALL be byte-for-byte identical. Defined in TELEGRAM_GLOSSARY.md: "The comparison of two Publications generated from identical datasets to determine whether they are byte-for-byte identical." |

## Re-evaluation

### Alternative Investigation

| Alternative | Found in repository? | Found in historical documents? |
|------------|---------------------|-------------------------------|
| Canonical Equality | YES — 35 occurrences, defined in Glossary | YES — originated in TJS-006, TJS-007 |
| Canonical Identity | NO — zero occurrences | NO |
| Canonical Equivalence | NO — zero occurrences (only in semantic review as rejected alternative) | NO |

"Canonical Equality" is the ONLY form used in the repository. No variant exists.

### Candidates Re-evaluated

| # | Candidate | Semantic Precision |
|---|-----------|-------------------|
| 1 | Канонічна рівність | "рівність" = equality. Direct translation. Already in Glossary. Matches the English term exactly. |
| 2 | Канонічна тотожність | "тотожність" = identity/identicalness. Stronger — implies strict logical identity. The definition says "byte-for-byte identical" which IS strict identity. |

### Semantic Analysis

The definition says "byte-for-byte identical." This is NOT mathematical equality (which allows different representations of the same value). This IS strict identity (the bytes must match exactly).

"тотожність" (identity) is semantically MORE precise than "рівність" (equality) for byte-for-byte comparison. However, "рівність" is already established in the Glossary and is widely understood.

### Final Recommendation

| Field | Value |
|-------|-------|
| Approved Ukrainian equivalent | Канонічна рівність |
| Rejected alternatives | Канонічна тотожність (semantically stronger but not established), Канонічна ідентичність (less common), Стандартна рівність (loses "canonical") |
| Reason for rejection | Канонічна тотожність is semantically more precise but Канонічна рівність is already in the Glossary and widely used. Consistency with existing documentation outweighs marginal semantic improvement. |
| Rationale | "Канонічна рівність" is already established in the Glossary, has 35 occurrences in the repository, and is immediately understood. The semantic precision of "тотожність" does not justify breaking consistency with existing documentation. |
| Date approved | PENDING OWNER APPROVAL |
| Approved by | PENDING |
| Status | **PENDING OWNER APPROVAL** |

---

# 3. Powered

| Field | Value |
|-------|-------|
| English term | Powered |
| Category | C — Public Communication Terms |
| Meaning inside SvitloSk | A graphic rendering shorthand meaning "NOT currently experiencing an outage." Used as a color label (Orange) and timeline state (opposite of "Outage"). NOT about electrical supply in general. |

## Re-evaluation — Context-Dependent Analysis

"Powered" appears in 15 occurrences, all within TJS-022 (Graphic Publication Model). The contexts are:

### Context 1: Documentation (specification text)

| Dimension | Assessment |
|-----------|-----------|
| Where | TJS-022 descriptions, definitions |
| Audience | Engineers, specification readers |
| Appropriate translation | Descriptive — full Ukrainian phrase |
| Candidate | Без знеструмлення |

### Context 2: User Interface (graphic labels)

| Dimension | Assessment |
|-----------|-----------|
| Where | Color labels on graphics, timeline labels |
| Audience | End users (residents) |
| Appropriate translation | Short — must fit in small graphic space |
| Candidate | Норма or Без знеструмлення |

### Context 3: Algorithm descriptions

| Dimension | Assessment |
|-----------|-----------|
| Where | Code-level descriptions, generation logic |
| Audience | Engineers |
| Appropriate translation | Technical — use established project term |
| Candidate | Без знеструмлення |

### Context 4: Graphic Publication Model (color semantics)

| Dimension | Assessment |
|-----------|-----------|
| Where | C-003: "Powered = Orange" |
| Audience | Graphic designers, engineers |
| Appropriate translation | Label — short, clear |
| Candidate | Без знеструмлення |

### Context-Dependent Translation Rules

| Context | Approved Translation | Length Constraint |
|---------|---------------------|-------------------|
| Documentation text | Без знеструмлення | No constraint |
| Graphic labels | Без знеструмлення | Max 25 characters |
| Algorithm descriptions | Без знеструмлення | No constraint |
| Color semantics (C-003) | Без знеструмлення | Max 25 characters |

### Final Recommendation

| Field | Value |
|-------|-------|
| Approved Ukrainian equivalent | Без знеструмлення (universal across all contexts) |
| Rejected alternatives | Норма (too generic — could mean many things), Електропостачання (misleading — implies active supply), Забезпечення (incomplete), Відсутність відключення (awkward) |
| Reason for rejection | "Норма" is too generic and could conflict with other uses. "Електропостачання" misrepresents the meaning — Powered means absence of outage, not presence of supply. "Без знеструмлення" is the only candidate that directly matches the project's linguistic model centered on "знеструмлення." |
| Rationale | "Без знеструмлення" directly expresses "no outage" which is the precise meaning of "Powered" in SvitloSk. It matches the project's core linguistic model, is immediately understood by Ukrainian readers, and works across all contexts (documentation, graphics, algorithms). The length constraint for graphics (25 chars) is satisfied. |
| Date approved | PENDING OWNER APPROVAL |
| Approved by | PENDING |
| Status | **PENDING OWNER APPROVAL** |

---

# 4. Pre-Approved Terms (from existing Matrix)

The following 42 terms from the Translation Terminology Matrix are pre-approved at LOW ambiguity risk and do NOT require owner approval.

| Category A (Architecture) | Category B (Deterministic) | Category C (Public Communication) |
|--------------------------|--------------------------|----------------------------------|
| Parser | Traceability | Outage |
| Publisher | Reliability | Emergency outage |
| Channel | | Planned outage |
| Subscribers | | Restoration |
| Administrators | | Queue |
| Publication Identity | | Subqueue |
| Publication Engine (PENDING) | Canonical Equality (PENDING) | Powered (PENDING) |
| Archive | | |
| Repository | | |

---

# 5. Summary

| Term | Category | Recommendation | Status |
|------|----------|---------------|--------|
| Publication Engine | A — Architecture | Движок публікацій | PENDING OWNER APPROVAL |
| Canonical Equality | B — Deterministic | Канонічна рівність | PENDING OWNER APPROVAL |
| Powered | C — Public Communication | Без знеструмлення (universal) | PENDING OWNER APPROVAL |

---

**End of Decision Package**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** READY FOR OWNER APPROVAL
