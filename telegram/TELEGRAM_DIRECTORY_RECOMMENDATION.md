# TELEGRAM_DIRECTORY_RECOMMENDATION

**Document ID:** TJS-F1.1-R4

**Title:** Telegram Directory Recommendation

**Document Class:** Architecture Recommendation

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

One recommended directory architecture.

---

# 1. Recommendation: Option C (Layered Architecture)

```
telegram/
├── foundation/      (6 files — semantic model, glossary, alignment framework)
├── specs/           (5 files — canonical specifications + ADR)
├── working/         (130+ files — all working materials)
│   ├── publishing/  (10 files)
│   ├── editorial/   (11 files)
│   ├── graphic/     (50+ files)
│   ├── glossary/    (11 files)
│   ├── migration/   (9 files)
│   ├── alignment/   (5 files)
│   └── reference/   (35+ files)
├── legacy/          (8 files — historical TJS documents)
└── archive/         (30+ files — certificates, reviews, governance)
```

---

# 2. Justification

## 2.1 Why Option C?

| Criterion | Assessment |
|-----------|-----------|
| Foundation separated from specs | YES — TJS-000 is in foundation, TJS-020→022 are in specs |
| Working materials organized | YES — by subsystem inside working/ |
| Reference isolated | YES — inside working/reference/ |
| Archive isolated | YES — certificates and governance records |
| Clean responsibilities | YES — each directory has one clear purpose |
| Professional standard | YES — comparable to Kubernetes, CNCF |

## 2.2 Why NOT Option A (Proposed)?

| Issue | Impact |
|-------|--------|
| 11 directories | Excessive — professional systems use 5-6 |
| Foundation overlaps Canonical | TJS-000 is in Foundation but IS canonical |
| Publishing/, Editorial/, Graphic/ at top level | These are working materials, not canonical |
| Lifecycle has 1 file | Insufficient for top-level |
| Architecture has 2 files | Insufficient for top-level |

## 2.3 Why NOT Option B?

| Issue | Impact |
|-------|--------|
| Foundation overlaps specs | TJS-000 is both foundational and canonical |
| No reference directory | Reference materials need a home |

---

# 3. Directory Responsibilities

| Directory | Responsibility | Permanent? |
|-----------|---------------|-----------|
| foundation/ | Semantic model, glossary, alignment framework | YES |
| specs/ | Canonical specifications (TJS-020→022), ADR | YES |
| working/ | All working materials (harvests, reviews, validations) | TEMPORARY |
| legacy/ | Historical TJS specifications (TJS-001→008) | YES |
| archive/ | Certificates, governance records, audit reports | YES |

---

# 4. Working Subdirectories

| Subdirectory | Files | Purpose |
|-------------|-------|---------|
| working/publishing/ | 10 | Publishing model working materials |
| working/editorial/ | 11 | Editorial system working materials |
| working/graphic/ | 50+ | Graphic publication working materials |
| working/glossary/ | 11 | Glossary working materials |
| working/migration/ | 9 | Migration working materials |
| working/alignment/ | 5 | Alignment framework working materials |
| working/reference/ | 35+ | Reference working materials |

---

# 5. File Count Summary

| Directory | Files | Classification |
|-----------|-------|---------------|
| foundation/ | 6 | PERMANENT |
| specs/ | 5 | PERMANENT |
| working/ | 130+ | TEMPORARY |
| legacy/ | 8 | PERMANENT |
| archive/ | 30+ | PERMANENT |
| **Total** | **~180** | |

---

# 6. Naming Convention

| Element | Convention | Example |
|---------|-----------|---------|
| Top-level directories | lowercase | foundation/, specs/, working/ |
| Subdirectories | lowercase | working/publishing/, working/editorial/ |
| Canonical files | UPPER_CASE | TELEGRAM_GLOSSARY.md |
| Legacy files | TJS-[NNN]-[Name].md | TJS-001-Journal-Concept.md |

---

**End of Recommendation**

**Recommender:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE — Option C recommended
