# Telegram Architecture Proposal

**Date:** 2026-07-09
**Scope:** Proposed future Telegram Journal Specification (TJS) architecture

---

## 1. Design Principles

The proposed architecture follows the repository's established principles:

- **One Document — One Responsibility** (PROJECT_PRINCIPLES P-10)
- **Single Source of Truth** (GLOSSARY.md)
- **Separation of Concerns** (EDITORIAL_STANDARDS §3)
- **Stable Terminology** (GLOSSARY.md)

---

## 2. Proposed Document Set

| # | Proposed Filename | Purpose | Responsibility | Origin |
|---|------------------|---------|---------------|--------|
| 1 | TJS-001-Journal-Concept.md | Journal identity, mission, principles | Concept | RENAMED from existing (update §12) |
| 2 | TJS-002-Editorial-Policy.md | Editorial standards, formatting, territory rules | Editorial | RENAMED from TJS-004 (clearer name) |
| 3 | TJS-003-Message-Templates.md | Canonical publication templates, hierarchy, validation | Templates | RENAMED from TJS-005 (clearer name) |
| 4 | TJS-004-Rendering-Rules.md | Rendering pipeline, HTML generation, ordering | Rendering | RENAMED from TJS-006 (clearer name) |
| 5 | TJS-005-Publication-Lifecycle.md | Complete publication lifecycle (creation, updates, ownership, removal) | Lifecycle | MERGED from TJS-002 + TJS-007 + TJS-008 |
| 6 | TJS-006-Channel-Management.md | Telegram Bot API integration, rate limits, admin interaction | Integration | NEW |
| 7 | TJS-007-Graphic-Rendering.md | Graphic generation rules for Telegram publications | Graphics | NEW |

**Total: 7 documents** (down from 8, with deduplication)

---

## 3. Document Details

### TJS-001 — Journal Concept (RETAIN)

**Action:** RETAIN with updates

**Changes required:**
- Update §12 to reflect new document names
- Add Document Class: Normative
- Add References section
- Fix lowercase RFC 2119 keywords

**Rationale:** The journal concept is foundational and well-written. Only metadata and cross-references need updating.

---

### TJS-002 — Editorial Policy (RENAMED from TJS-004)

**Action:** RENAME TJS-004 → TJS-002

**Rationale:** "Editorial Policy" is a clearer name than the document ID suggests. The new numbering reflects the reading order: Concept → Editorial Policy → Templates → Rendering → Lifecycle.

**Changes required:**
- Update Specification ID to TJS-002
- Add Document Class: Normative
- Add References section
- Remove Component field (non-standard for TJS)

**Deduplication:** Absorb formatting rules from TJS-003 §9. TJS-002 becomes the single owner of editorial and formatting standards.

---

### TJS-003 — Message Templates (RENAMED from TJS-005)

**Action:** RENAME TJS-005 → TJS-003

**Rationale:** "Message Templates" is the clearest name for this document's responsibility.

**Changes required:**
- Update Specification ID to TJS-003
- Fix metadata (replace "Project" and "Class" with standard fields)
- Add Document Class: Normative
- Absorb publication structure from TJS-003 (current) — TJS-003 becomes the single owner of publication structure AND templates

**Deduplication:** Absorb TJS-003 (current Post Structure) into this document. The current TJS-003 is less detailed and can be fully subsumed.

---

### TJS-004 — Rendering Rules (RENAMED from TJS-006)

**Action:** RENAME TJS-006 → TJS-004

**Rationale:** "Rendering Rules" is the clearest name for this document's responsibility.

**Changes required:**
- Update Specification ID to TJS-004
- Fix metadata
- Fix incorrect reference "TJS-003 — Editorial Policy" → "TJS-002 — Editorial Policy"
- Add Document Class: Normative

---

### TJS-005 — Publication Lifecycle (MERGED from TJS-002 + TJS-007 + TJS-008)

**Action:** MERGE TJS-002 + TJS-007 + TJS-008 into one document

**Rationale:** Three documents covering the same topic (Publication Lifecycle) is a critical SSOT violation. The merged document will contain:

**From TJS-002 (conceptual lifecycle):**
- Publication types (§4)
- Archive policy (§9)
- Deletion policy (§10)
- Traceability (§11)
- Reliability (§12)

**From TJS-007 (operational lifecycle):**
- Publication creation rules (§4)
- Canonical equality (§6)
- Publication ownership (§10)
- Non-destructive channel principle (§11)
- Error handling (§13)

**From TJS-008 (implementation lifecycle):**
- Daily publication cycle (§3)
- Publication windows (§6)
- Event-driven principle (§7)
- Stable journal principle (§8)
- Deterministic principle (§9)
- Tomorrow lifecycle (§12)
- Manual/Image publications (§13-14)
- Publication session (§15)
- Daily lifecycle diagram (§16)
- Architecture diagram (§17)

**Deduplication:** Eliminates triple SSOT violation. One document owns all lifecycle concepts.

---

### TJS-006 — Channel Management (NEW)

**Action:** CREATE new document

**Rationale:** TJS-001 §12 originally listed "TJS-007 — Moderation" as a future specification. Channel management (Telegram Bot API integration, rate limits, admin interaction) is a missing area identified in the gap analysis.

**Responsibility:**
- Telegram Bot API integration rules
- Rate limiting and API constraints
- Message editing rules (Telegram-specific)
- Channel administration interaction
- Error recovery at API level

**Dependencies:** TJS-005 (Publication Lifecycle), SSP-003 (Publication Engine)

---

### TJS-007 — Graphic Rendering (NEW)

**Action:** CREATE new document

**Rationale:** Graphics are referenced in TJS-003 (Post Structure §6) and TJS-005 (Message Templates) but no document specifies how graphics are rendered for Telegram publications.

**Responsibility:**
- Graphic generation rules for Telegram posts
- Image format requirements (PNG/SVG)
- Telegram image size constraints
- Graphic-to-text pairing rules
- Graphic validation rules

**Dependencies:** TJS-003 (Message Templates), SSP-007 (Graphic Generator), SSP-003 (Publication Engine)

---

## 4. Documents Removed

| Document | Reason |
|----------|--------|
| TJS-003 (current Post Structure) | MERGED into TJS-003 (Message Templates) — less detailed version |
| TJS-002 (current Publication Lifecycle) | MERGED into TJS-005 (Publication Lifecycle) — superseded |
| TJS-007 (current Publication Lifecycle) | MERGED into TJS-005 (Publication Lifecycle) — superseded |
| TJS-008 (current Publication Lifecycle) | MERGED into TJS-005 (Publication Lifecycle) — superseded |

---

## 5. Document ID Mapping

| Current ID | Current Name | Proposed ID | Proposed Name | Action |
|-----------|-------------|-------------|---------------|--------|
| TJS-001 | Journal Concept | TJS-001 | Journal Concept | RETAIN (update metadata) |
| TJS-002 | Publication Lifecycle | — | — | MERGED into TJS-005 |
| TJS-003 | Post Structure | — | — | MERGED into TJS-003 |
| TJS-004 | Editorial Policy | TJS-002 | Editorial Policy | RENUMBER |
| TJS-005 | Message Templates | TJS-003 | Message Templates | RENUMBER |
| TJS-006 | Rendering Rules | TJS-004 | Rendering Rules | RENUMBER |
| TJS-007 | Publication Lifecycle | — | — | MERGED into TJS-005 |
| TJS-008 | Publication Lifecycle | — | — | MERGED into TJS-005 |
| — | — | TJS-005 | Publication Lifecycle | MERGED from TJS-002+007+008 |
| — | — | TJS-006 | Channel Management | NEW |
| — | — | TJS-007 | Graphic Rendering | NEW |

---

## 6. Proposed Dependency Graph

```text
TJS-001 (Journal Concept)
    │
    └──→ TJS-002 (Editorial Policy)
              │
              └──→ TJS-003 (Message Templates)
                        │
                        ├──→ TJS-004 (Rendering Rules)
                        │        │
                        │        └──→ TJS-005 (Publication Lifecycle)
                        │                 │
                        │                 └──→ TJS-006 (Channel Management)
                        │
                        └──→ TJS-007 (Graphic Rendering)
```

---

## 7. Expected Benefits

| Benefit | Description |
|---------|-------------|
| SSOT restored | Publication lifecycle has exactly one owner |
| Deduplication | 8 documents → 7 documents (with 4 merged into 1) |
| Clear naming | Each document name reflects its responsibility |
| Complete coverage | Missing areas (Channel Management, Graphic Rendering) addressed |
| Metadata compliance | All documents follow repository metadata standards |
| Correct cross-references | All inter-document references validated |

---

## 8. Migration Impact

| Impact | Description |
|--------|-------------|
| DOCUMENT_INDEX.md | Must be updated with new document names and IDs |
| SSP cross-references | SSP-003 and SSP-007 reference TJS documents — must be updated |
| TERRITORIAL_MODEL.md | Referenced by multiple TJS — no change needed |
| DATA_MODEL.md | Referenced by TJS-005 — no change needed |
| Existing TJS files | Must be renamed, renumbered, and deduplicated |

---

**Architect:** SvitloSk Certification Pipeline
