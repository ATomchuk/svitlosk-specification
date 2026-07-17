# TELEGRAM_GRAPHIC_METADATA_REVIEW

**Document ID:** TJS-G1.05-R3

**Title:** Graphic Metadata Review

**Document Class:** Metadata Analysis

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Determine whether Graphic Publication Metadata SHALL exist as a reusable canonical component.

---

# 1. Shared Metadata Analysis

| Metadata | Source | Shared by All Types? | Current Location |
|----------|--------|---------------------|------------------|
| Generation timestamp | SSP-007 §4 (branding) | YES | §6.2 Branding Elements |
| Publication timestamp | Lifecycle §5.1 | YES | Not in Graphic spec |
| Territory | Glossary §Territory | YES | §5 Taxonomy |
| Source dataset | Repository Authority §3.1 | YES | Not in Graphic spec |
| Version | Identity Model | YES | Not in Graphic spec |
| Publication identity | Lifecycle §4 | YES | Not in Graphic spec |

---

# 2. Decision: YES — Introduce §6.4 Graphic Publication Metadata

**Justification:**

1. All 6 metadata elements are shared across ALL 5 publication types
2. They are currently scattered across multiple sections and subsystems
3. A single canonical location avoids repetition and ensures consistency
4. Every graphic publication SHALL carry these metadata elements
5. Metadata supports traceability (every graphic can be traced to its source)

---

# 3. §6.4 Graphic Publication Metadata Definition

```
§6.4 Graphic Publication Metadata
├── 6.4.1 Generation Timestamp (час генерації)
│   The timestamp when the graphic was generated
├── 6.4.2 Publication Timestamp (час публікації)
│   The timestamp when the graphic was published to Telegram
├── 6.4.3 Territory (територія)
│   The territory this graphic represents
├── 6.4.4 Source Dataset (джерело даних)
│   The normalized dataset used to generate this graphic
├── 6.4.5 Version (версія)
│   The version identifier of this graphic
└── 6.4.6 Publication Identity (ідентифікатор публікації)
    The unique identifier for this graphic publication
```

---

# 4. Metadata Properties

| Property | Statement |
|----------|-----------|
| Every graphic SHALL carry all 6 metadata elements | MANDATORY |
| Metadata SHALL be traceable to source data | MANDATORY |
| Metadata SHALL be unique per graphic | MANDATORY |
| Metadata SHALL be preserved in archive | MANDATORY |

---

# 5. Verification

| Check | Result |
|-------|--------|
| Metadata shared by all types | YES — 5/5 types |
| Metadata not duplicated elsewhere | YES |
| Metadata traceable to sources | YES — 6/6 |
| Metadata supports traceability | YES |

**Result:** PASS

---

**End of Metadata Review**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE — §6.4 approved
