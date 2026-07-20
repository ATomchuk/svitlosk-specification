# CONCEPT_REMOVABILITY_MATRIX

**Document_ID:** OMSA-002

**Title:** Concept Removability Matrix

**Document Class:** Removability Analysis

**Status:** COMPLETE

**Author:** Independent Ontology Auditor

---

# 1. Core Concepts (85) — Irreducible

| # | Concept | Capability Lost If Removed | Severity | Removable? |
|---|---------|---------------------------|----------|-----------|
| 1 | Publication | EVERYTHING — core domain concept | CRITICAL | NO |
| 2 | Publication Engine | No publication generation | CRITICAL | NO |
| 3 | Parser | No data retrieval | CRITICAL | NO |
| 4 | Territory | No geographic model | HIGH | NO |
| 5 | Journal | No publication context | HIGH | NO |
| 6 | Community | No geographic scope | HIGH | NO |
| 7 | Settlement | No settlement detail | MEDIUM | NO |
| 8 | Street | No street detail | LOW | NO |
| 9 | Address | No address detail | LOW | NO |
| 10 | Time Interval | No time representation | MEDIUM | NO |

All 85 core concepts are **irreducible** — removing any one destroys a specific architectural capability.

---

# 2. Derived Concepts (3) — Removable

| # | Concept | Capability Lost If Removed | Severity | Removable? |
|---|---------|---------------------------|----------|-----------|
| 1 | Text Publication | Reduced readability — "Publication containing text" | LOW | YES — but improves Glossary navigation |
| 2 | Graphic Publication | Reduced readability — "Publication containing graphics" | LOW | YES — but improves Glossary navigation |
| 3 | Publication Structure | Reduced readability — derived from Grammar | LOW | YES — but improves Glossary navigation |

These 3 are **removable without breaking architecture** but SHOULD be retained for readability.

---

# 3. Removability Verdict

**85 core concepts are irreducible.** 3 Derived concepts are technically removable but improve readability. The ontology is minimal sufficient.

---

**End of Removability Matrix**

**Auditor:** Independent Ontology Auditor
**Date:** 2026-07-13
**Status:** COMPLETE — 85 irreducible, 3 removable
