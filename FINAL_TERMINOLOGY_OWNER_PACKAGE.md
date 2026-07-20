# FINAL_TERMINOLOGY_OWNER_PACKAGE

**Document ID:** TOD-003

**Title:** Final Terminology Owner Package

**Document Class:** Decision Package

**Status:** READY FOR OWNER APPROVAL

**Author:** SvitloSk Project

---

# 1. Publication Engine

## Evidence

| Source | Occurrences | Classification |
|--------|-------------|---------------|
| TJS-010 (Publishing Model) | 20 | Architectural Component — section 4.1, interaction matrix, constraints |
| TJS-020 (Editorial Model) | 2 | Referenced as component outside editorial scope |
| TELEGRAM_GLOSSARY.md | 5 | Defined as "architectural Component implementing the Publisher Role" |
| Working documents | ~120 | Used throughout publishing and graphic working docs |

## Architectural Reasoning

The Glossary definition (§14) is unambiguous:

> "The architectural Component implementing the Publisher Role. The Publication Engine is responsible for generating and distributing Publications."

TJS-010 §4.1 gives it its own section alongside 7 other Components:

Parser (§4.2), Publisher Role (§4.3), Telegram Publisher (§4.4), Schedule Generator (§4.5), Graphic Generator (§4.6), Data Storage (§4.7), Telegram Channel (§4.8).

It is a **proper architectural name** for a specific Component. It is NOT a generic description.

## Semantic Reasoning

"Publication Engine" = the Component that generates and distributes Publications.

"Engine" in Ukrainian IT ("Движок") universally means "processing core" — the central processing unit.

"Компонент" would make the name generic — every Component would become "Компонент X."

"Движок" preserves the distinctive identity.

## Alternatives

| Candidate | Architectural Fit | Semantic Fit | Recommendation |
|-----------|------------------|-------------|---------------|
| Движок публікацій | GOOD — preserves proper name | GOOD — natural IT term | RECOMMENDED |
| Компонент публікацій | POOR — too generic | POOR — loses identity | REJECTED |
| Механізм публікацій | MEDIUM — formal | MEDIUM — less natural | REJECTED |
| Publication Engine (not translated) | N/A — violates DTS-001 | N/A | REJECTED |

## Final Recommendation

| Field | Value |
|-------|-------|
| English Term | Publication Engine |
| Semantic Layer | Architectural Component implementing the Publisher Role |
| Identifier Layer | Publication Engine |
| Rendering Layer | Движок публікацій |
| Presentation Layer | Движок публікацій (universal) |
| Confidence Level | HIGH |
| Repository Impact | 145 occurrences in working docs. Glossary entry updated on approval. |
| **Decision** | **PENDING OWNER APPROVAL** |

---

# 2. Canonical Equality

## Evidence

| Source | Occurrences | Classification |
|--------|-------------|---------------|
| TJS-010 §11 | 1 | Quality guarantee: "byte-for-byte identical" |
| TELEGRAM_GLOSSARY.md | 1 | Defined: "comparison of two Publications... byte-for-byte identical" |
| Working documents | ~33 | Used in traceability, duplication, section matrices |
| Legacy (TJS-006, TJS-007) | 2 | Original source of the term |

## Semantic Reasoning

The definition says: "byte-for-byte identical."

This is strict identity — not mathematical equality (which allows different representations).

"Canonical Identity" — does NOT exist in the repository (0 occurrences).

"Canonical Equivalence" — does NOT exist in the repository (0 occurrences).

"Canonical Equality" is the ONLY established form (35 occurrences, Glossary-defined).

## Alternatives

| Candidate | Established? | Semantic Precision | Recommendation |
|-----------|-------------|-------------------|---------------|
| Канонічна рівність | YES — in Glossary, 35 occurrences | GOOD — "рівність" = equality | RECOMMENDED |
| Канонічна тотожність | NO — not established | BETTER — "тотожність" = identity | NOT recommended — breaks consistency |
| Канонічна ідентичність | NO — not established | GOOD | NOT recommended — breaks consistency |

## Final Recommendation

| Field | Value |
|-------|-------|
| English Term | Canonical Equality |
| Semantic Layer | Byte-for-byte identical output from identical input |
| Identifier Layer | Canonical Equality |
| Rendering Layer | Канонічна рівність |
| Presentation Layer | Канонічна рівність (universal) |
| Confidence Level | HIGH |
| Repository Impact | 35 occurrences. Already in Glossary as approved. No changes needed. |
| **Decision** | **PENDING OWNER APPROVAL** |

---

# 3. Powered

## Evidence — All Occurrences by Context

### A. Internal Identifiers (0 occurrences)

"Powered" is NOT used as an internal identifier or Document ID anywhere.

### B. Specification Language (6 occurrences in TJS-022)

| Line | Context | Wording |
|------|---------|---------|
| 116 | Color table | "Powered=Orange, Outage=Dark Gray" |
| 305 | Timeline description | "distinguish between powered and outage states" |
| 313 | Color composition table | "Powered | Orange" |
| 418 | Constraint C-003 | "Powered = Orange. Outage = Dark Gray." |

These use "Powered" as a **specification state name** — defining the graphic rendering system.

### C. Algorithm Descriptions (2 occurrences)

| Line | Context | Wording |
|------|---------|---------|
| 114 | T-001 properties | "Contains... powered intervals" |
| 176 | T-005 properties | "Contains... Powered percentage" |

These use "Powered" as a **data field name** — describing what data the graphic contains.

### D. UI Labels (0 occurrences in canonical specs)

"Powered" does NOT appear as a rendered UI label in any canonical specification. The specifications define WHAT the graphics contain, not HOW they are rendered to users.

### E. Graphic Publication Model (7 occurrences)

All within TJS-022. "Powered" is a **canonical state** in the graphic rendering system — one of two states alongside "Outage."

### F. Resident-Facing Text (0 occurrences)

"Powered" does NOT appear in any resident-facing text in the canonical specifications.

## Context Classification Summary

| Category | Occurrences | Wording Identical? |
|----------|-------------|-------------------|
| Internal identifier | 0 | N/A |
| Specification language | 6 | YES — use Rendering Layer |
| Algorithm description | 2 | YES — use Rendering Layer |
| UI label | 0 | N/A |
| Graphic publication | 7 | YES — use Rendering Layer |
| Resident-facing | 0 | N/A |

## TTDR Structure for Powered

The four-layer model resolves the context question:

| Layer | Value | Context Dependency |
|-------|-------|-------------------|
| Semantic | NOT currently experiencing an outage | NEVER changes |
| Identifier | Powered | NEVER changes (English source) |
| Rendering | Без знеструмлення | NEVER changes (approved translation) |
| Presentation | Без знеструмлення | NEVER changes (universal — all contexts) |

For "Powered," the Rendering Layer and Presentation Layer are IDENTICAL across all contexts.

TTDR does NOT need to distinguish contexts for this term because:

1. All 15 occurrences are within TJS-022 (one document)
2. "Powered" is used consistently as a state name
3. No resident-facing text uses "Powered"
4. The graphic label constraint (25 chars) is satisfied by "Без знеструмлення" (18 chars)

## Final Recommendation

| Field | Value |
|-------|-------|
| English Term | Powered |
| Semantic Layer | NOT currently experiencing an outage |
| Identifier Layer | Powered |
| Rendering Layer | Без знеструмлення |
| Presentation Layer | Без знеструмлення (universal) |
| Confidence Level | HIGH |
| Repository Impact | 15 occurrences in TJS-022. Graphic constraint C-003 updated on approval. |
| **Decision** | **PENDING OWNER APPROVAL** |

---

# 4. Summary

| Term | Category | Rendering | Confidence | Status |
|------|----------|-----------|-----------|--------|
| Publication Engine | A — Architecture | Движок публікацій | HIGH | PENDING OWNER APPROVAL |
| Canonical Equality | B — Deterministic | Канонічна рівність | HIGH | PENDING OWNER APPROVAL |
| Powered | C — Public Communication | Без знеструмлення | HIGH | PENDING OWNER APPROVAL |

---

# 5. Certification

| Question | Answer |
|----------|--------|
| Has every decision been justified by repository evidence? | YES — all 3 terms traced to canonical specs and Glossary |
| Can owner make final approval without further investigation? | YES — evidence complete |
| Will TTDR become stable after approvals? | YES — 45 terms + 3 new = 48 total approved |
| Is L-4 ready immediately after approval? | YES — first translation target: TJS-000.uk.md |

---

**End of Final Package**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** READY FOR OWNER APPROVAL
