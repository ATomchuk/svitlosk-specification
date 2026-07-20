# CANONICAL_TRANSLATION_ORDER

**Document ID:** TRA-003

**Title:** Canonical Translation Order

**Document Class:** Translation Order

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Translation Order Recommendation

The optimal translation order for the first wave considers:

- Terminology dependencies (GLOSSARY must exist before specs that reference it)
- Cross-references (TJS-000 defines terms used by TJS-010, TJS-020, TJS-021, TJS-022)
- Future consistency (foundation terms must be established first)
- Translation efficiency (glossary terms translated once, reused everywhere)

---

# 2. Recommended Order

| Priority | Document | Reason |
|----------|----------|--------|
| 1 | TJS-000A — TELEGRAM_GLOSSARY.uk.md | Terminology foundation — all other specs reference glossary terms |
| 2 | TJS-000 — TELEGRAM_SEMANTIC_MODEL.uk.md | Semantic foundation — defines core concepts |
| 3 | TJS-010 — TELEGRAM_PUBLISHING_CANONICAL_MODEL.uk.md | Publishing architecture — references glossary and semantic model |
| 4 | TJS-020 — TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.uk.md | Editorial system — references glossary |
| 5 | TJS-021 — TELEGRAM_PUBLICATION_LIFECYCLE.uk.md | Lifecycle — references publishing and editorial |
| 6 | TJS-022 — TELEGRAM_GRAPHIC_PUBLICATION_MODEL.uk.md | Graphic model — references all above |

---

# 3. Order Justification

| Priority | Justification |
|----------|--------------|
| TJS-000A first | Glossary defines ALL terminology. Every other spec uses these terms. Translating the glossary first ensures consistent terminology across all translations. |
| TJS-000 second | Semantic model defines the conceptual framework. All specs build on these concepts. |
| TJS-010 third | Publishing model is the most complex spec. It references glossary, semantic model, and defines 8 components. |
| TJS-020 fourth | Editorial system references publishing model. |
| TJS-021 fifth | Lifecycle references both publishing and editorial. |
| TJS-022 sixth | Graphic model references all above. |

---

# 4. First Translation Target

**TJS-000A.uk.md** — Telegram Glossary in Ukrainian.

This is the optimal first target because:

1. It defines ALL terminology used in every other spec
2. Once glossary terms are translated, they propagate to all subsequent translations
3. It is the shortest document — quick win, establishes the pattern
4. It validates the entire workflow on a small document before tackling larger specs

---

**End of Canonical Translation Order**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
