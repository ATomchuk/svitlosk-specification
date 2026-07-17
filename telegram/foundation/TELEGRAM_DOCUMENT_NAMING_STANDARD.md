# TELEGRAM_DOCUMENT_NAMING_STANDARD

**Document ID:** TJS-F1-A2

**Title:** Telegram Document Naming Standard

**Document Class:** Naming Convention

**Status:** APPROVED

**Author:** SvitloSk Project

---

# Purpose

Define the canonical naming convention for all Telegram documentation.

---

# 1. Naming Rules

## 1.1 Canonical Specifications

| Rule | Convention | Example |
|------|-----------|---------|
| Pattern | TELEGRAM_[SUBSYSTEM]_[TYPE].md | TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md |
| Subsystem | PUBLISHING, EDITORIAL, LIFECYCLE, GRAPHIC, SEMANTIC | — |
| Type | MODEL, SPECIFICATION, SYSTEM | — |
| Case | UPPER_CASE with underscores | — |

## 1.2 Foundation Documents

| Rule | Convention | Example |
|------|-----------|---------|
| Pattern | TELEGRAM_[CONCEPT].md | TELEGRAM_SEMANTIC_MODEL.md |
| Pattern | TELEGRAM_GLOSSARY.md | TELEGRAM_GLOSSARY.md |
| Pattern | TJS_[FRAMEWORK].md | TJS_ALIGNMENT_TEMPLATE.md |

## 1.3 Working Materials

| Rule | Convention | Example |
|------|-----------|---------|
| Pattern | TELEGRAM_[SUBSYSTEM]_[ARTIFACT].md | TELEGRAM_GRAPHIC_HARVEST.md |
| Pattern | TELEGRAM_[SUBSYSTEM]_[REVIEW].md | TELEGRAM_GRAPHIC_PRINCIPLE_REVIEW.md |
| Pattern | TELEGRAM_[SUBSYSTEM]_[VALIDATION].md | TELEGRAM_GRAPHIC_BLUEPRINT_VALIDATION.md |

## 1.4 Legacy Documents

| Rule | Convention | Example |
|------|-----------|---------|
| Pattern | TJS-[NNN]-[Name].md | TJS-001-Journal-Concept.md |
| Number | Three digits, zero-padded | TJS-001, TJS-008 |
| Name | Title-Case with hyphens | Journal-Concept |

---

# 2. Naming Prohibitions

| Prohibition | Reason |
|-------------|--------|
| NO mixed case (Telegram_Glossary.md) | Inconsistent |
| NO spaces in filenames | Path issues |
| NO special characters | Path issues |
| NO duplicate prefixes | Confusing |
| NO abbreviations without definition | Unclear |

---

# 3. Naming Consistency Verification

| Pattern | Status |
|---------|--------|
| TELEGRAM_*.md | CONSISTENT |
| TJS-*.md | CONSISTENT |
| TJS_ALIGNMENT_*.md | CONSISTENT |
| TJS_ALIGNMENT_TEMPLATE_REPORT.md | INCONSISTENT — should be TELEGRAM_* or TJS_* |

---

# 4. Recommended Fixes

| File | Current Name | Recommended Name |
|------|-------------|-----------------|
| TJS_ALIGNMENT_TEMPLATE_REPORT.md | TJS_ALIGNMENT_TEMPLATE_REPORT.md | TELEGRAM_ALIGNMENT_TEMPLATE_REPORT.md |
| TJS_ALIGNMENT_TEMPLATE_VALIDATION.md | TJS_ALIGNMENT_TEMPLATE_VALIDATION.md | TELEGRAM_ALIGNMENT_TEMPLATE_VALIDATION.md |

---

**End of Naming Standard**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** APPROVED
