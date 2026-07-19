# TELEGRAM_TRANSLATION_METADATA_STANDARD

**Document ID:** TJS-L1-A5

**Title:** Telegram Translation Metadata Standard

**Document Class:** Metadata Standard

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Define the standard translation header for bilingual documents.

---

# 1. Translation Metadata Header

Every translated document SHALL include the following metadata:

`yaml
---
translation_status: [Draft | Review | Approved | Stable]
canonical_source: [English filename]
language: [uk | en]
source_version: [version of English source]
translation_version: [version of Ukrainian translation]
last_synchronization: [YYYY-MM-DD]
translator: [translator name or identifier]
review_status: [Pending | Approved | Published]
---
`

---

# 2. Translation Metadata Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| translation_status | Enum | YES | Draft, Review, Approved, Stable |
| canonical_source | String | YES | Filename of the English source document |
| language | Enum | YES | uk (Ukrainian) or en (English) |
| source_version | String | YES | Version of the English source |
| translation_version | String | YES | Version of the Ukrainian translation |
| last_synchronization | Date | YES | Last date translation was synchronized with source |
| translator | String | YES | Name or identifier of the translator |
| review_status | Enum | YES | Pending, Approved, Published |

---

# 3. Translation File Naming Convention

| Pattern | Example | Description |
|---------|---------|-------------|
| Document.uk.md | TELEGRAM_GLOSSARY.uk.md | Ukrainian translation |
| Document.en.md | TELEGRAM_GLOSSARY.en.md | English original (if needed) |

**Convention:** [Original Filename].uk.md

This follows international GitHub/Open Source best practices:
- Simple suffix-based naming
- Language code after the dot
- Original filename preserved
- Easy to discover all translations

---

# 4. Translation Directory Structure

`
telegram/
├── foundation/
│   ├── TELEGRAM_SEMANTIC_MODEL.md        (English)
│   ├── TELEGRAM_SEMANTIC_MODEL.uk.md     (Ukrainian)
│   ├── TELEGRAM_GLOSSARY.md              (English)
│   └── TELEGRAM_GLOSSARY.uk.md           (Ukrainian)
├── specs/
│   ├── TELEGRAM_PUBLISHING_CANONICAL_MODEL.md        (English)
│   ├── TELEGRAM_PUBLISHING_CANONICAL_MODEL.uk.md     (Ukrainian)
│   └── ...
`

---

# 5. Translation Metadata Location

Every translated document SHALL include the metadata header at the top of the file, after the document title and before the first content section.

---

# 6. Translation Standard Summary

| Element | Convention |
|---------|-----------|
| File naming | [Original].uk.md |
| Metadata location | Top of file, after title |
| Metadata format | YAML front matter |
| Language code | uk (Ukrainian) |
| Canonical source | English filename |
| Synchronization | Date-based |

---

**End of Translation Metadata Standard**

**Standardizer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
