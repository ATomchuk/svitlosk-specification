# TRANSLATION_QA_CHECKLIST

**Document ID:** TQ-001

**Title:** Translation QA Checklist

**Document Class:** Quality Assurance Checklist

**Status:** STABLE

**Author:** SvitloSk Project

---

# Purpose

Mandatory quality checklist for every translated document.

---

# 1. Structure Verification

| # | Check | Status |
|---|-------|--------|
| 1 | Document structure identical to canonical English source | [ ] |
| 2 | Section numbering identical | [ ] |
| 3 | Section count identical | [ ] |
| 4 | Table count identical | [ ] |
| 5 | List count identical | [ ] |

---

# 2. Heading Verification

| # | Check | Status |
|---|-------|--------|
| 6 | All headings translated | [ ] |
| 7 | Heading hierarchy identical | [ ] |
| 8 | Heading capitalization correct | [ ] |

---

# 3. Terminology Verification

| # | Check | Status |
|---|-------|--------|
| 9 | All terms match Translation Terminology Matrix | [ ] |
| 10 | No unauthorized synonyms used | [ ] |
| 11 | Document IDs remain in English | [ ] |
| 12 | File paths remain in English | [ ] |

---

# 4. RFC 2119 Verification

| # | Check | Status |
|---|-------|--------|
| 13 | SHALL not translated | [ ] |
| 14 | SHOULD not translated | [ ] |
| 15 | MAY not translated | [ ] |
| 16 | MUST not translated | [ ] |
| 17 | REQUIRED not translated | [ ] |
| 18 | PROHIBITED not translated | [ ] |

---

# 5. Semantic Verification

| # | Check | Status |
|---|-------|--------|
| 19 | No semantic drift from English source | [ ] |
| 20 | No added requirements | [ ] |
| 21 | No removed requirements | [ ] |
| 22 | No modified requirements | [ ] |

---

# 6. Reference Verification

| # | Check | Status |
|---|-------|--------|
| 23 | All internal links valid | [ ] |
| 24 | All Document ID references preserved | [ ] |
| 25 | All section references correct | [ ] |

---

# 7. Translation Status Verification

| # | Check | Status |
|---|-------|--------|
| 26 | Translation Status block present | [ ] |
| 27 | Document ID matches English source | [ ] |
| 28 | Original Document field correct | [ ] |
| 29 | Canonical Version matches | [ ] |
| 30 | Translation Version set | [ ] |
| 31 | Last Synchronization date set | [ ] |

---

# 8. Formatting Verification

| # | Check | Status |
|---|-------|--------|
| 32 | Markdown formatting identical | [ ] |
| 33 | Code blocks not translated | [ ] |
| 34 | Table alignment preserved | [ ] |
| 35 | Line breaks preserved | [ ] |

---

# 9. Checklist Summary

| # | Check Category | Total Checks |
|---|---------------|-------------|
| 1 | Structure | 5 |
| 2 | Headings | 3 |
| 3 | Terminology | 4 |
| 4 | RFC 2119 | 6 |
| 5 | Semantic | 4 |
| 6 | References | 3 |
| 7 | Translation Status | 6 |
| 8 | Formatting | 4 |
| **Total** | | **35** |

---

# 10. Pass Criteria

| Criterion | Required |
|-----------|----------|
| All 35 checks PASS | YES |
| Zero semantic drift | YES |
| Zero broken references | YES |
| Translation Status block valid | YES |

**A translated document SHALL NOT become Official Translation unless all 35 checks pass.**

---

**End of QA Checklist**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** STABLE
