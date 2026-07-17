# TELEGRAM_GRAPHIC_CLASSIFICATION_OWNER

**Document ID:** TJS-G1.056-R3

**Title:** Graphic Classification Owner

**Document Class:** Owner Analysis

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Determine the canonical owner of the Publication Families classification wording.

---

# 1. Candidate Analysis

| Candidate | Argument For | Argument Against |
|-----------|-------------|------------------|
| TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md (TJS-022) | Defines the taxonomy, so it should define how families are classified | — |
| Canonical Specification Standard (TJS-STD) | Defines writing standards for all specifications | Too broad — doesn't define domain-specific classification |
| Architecture Decision (TAD) | Architectural decisions live here | This is a taxonomy detail, not an architectural decision |

---

# 2. Decision: TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md (TJS-022)

**Justification:**

1. The Graphic Publication Model owns the taxonomy (§5)
2. Publication Families are part of the taxonomy
3. The classification wording describes HOW families are used within the taxonomy
4. The Graphic Publication Model is the natural location for this definition
5. Placing it in the Architecture Decision would be too granular
6. Placing it in the Canonical Specification Standard would be too broad

---

# 3. Architecture Position

```
TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md (TJS-022)
├── §5 Graphic Publication Taxonomy
│   ├── §5.1 Publication Families
│   │   ├── Canonical Wording (EN + UK)
│   │   ├── Classification: organizational categories
│   │   ├── NOT architectural entities
│   │   ├── NOT semantic concepts
│   │   └── Used ONLY for document readability
│   ├── §5.2 Tomorrow Schedule Graphic (T-001)
│   ├── §5.3 Emergency Information Card (T-003)
│   ├── §5.4 Information Card (T-004)
│   ├── §5.5 Statistics Card (T-005)
│   └── §5.6 Service Graphic (T-006)
```

---

# 4. Verification

| Check | Result |
|-------|--------|
| Owner is unique | YES — TJS-022 |
| Owner is appropriate | YES — owns taxonomy |
| No ownership conflict | YES |
| No duplication | YES |

**Result:** PASS

---

**End of Owner Analysis**

**Analyst:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE — Owner: TJS-022 §5.1
