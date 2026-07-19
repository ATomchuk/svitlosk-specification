# TRANSLATION_REPOSITORY_STRATEGY

**Document ID:** TJS-L2-S6

**Title:** Translation Repository Strategy

**Document Class:** Repository Strategy

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Determine where Ukrainian documents SHALL live.

---

# 1. Repository Placement Strategy

## 1.1 Recommended Strategy: Parallel Files with Language Suffix

| Pattern | Example | Description |
|---------|---------|-------------|
| Document.md | TELEGRAM_GLOSSARY.md | English original |
| Document.uk.md | TELEGRAM_GLOSSARY.uk.md | Ukrainian translation |

## 1.2 Strategy Justification

| Criterion | Assessment |
|-----------|-----------|
| GitHub usability | YES — .uk.md files are naturally displayed |
| Parallel files | YES — English and Ukrainian coexist |
| Cross links | YES — translations reference English originals |
| Repository navigation | YES — same directory, language suffix distinguishes |
| International best practice | YES — follows GitHub/Open Source conventions |

## 1.3 Strategy Comparison

| Strategy | Pros | Cons | Verdict |
|----------|------|------|---------|
| Document.uk.md | Simple, GitHub-friendly, standard | None | RECOMMENDED |
| Separate uk/ directory | Clean separation | Path complexity, broken references | REJECTED |
| Separate repository | Maximum isolation | Maintenance nightmare | REJECTED |
| Inline bilingual | Single file | Mixing languages, hard to maintain | REJECTED |

---

# 2. Translation Placement

| Document | English Location | Ukrainian Location |
|----------|-----------------|-------------------|
| TJS-000 | telegram/foundation/TELEGRAM_SEMANTIC_MODEL.md | telegram/foundation/TELEGRAM_SEMANTIC_MODEL.uk.md |
| TJS-000A | telegram/foundation/TELEGRAM_GLOSSARY.md | telegram/foundation/TELEGRAM_GLOSSARY.uk.md |
| TJS-010 | telegram/specs/TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | telegram/specs/TELEGRAM_PUBLISHING_CANONICAL_MODEL.uk.md |
| TJS-020 | telegram/specs/TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md | telegram/specs/TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.uk.md |
| TJS-021 | telegram/specs/TELEGRAM_PUBLICATION_LIFECYCLE.md | telegram/specs/TELEGRAM_PUBLICATION_LIFECYCLE.uk.md |
| TJS-022 | telegram/specs/TELEGRAM_GRAPHIC_PUBLICATION_MODEL.md | telegram/specs/TELEGRAM_GRAPHIC_PUBLICATION_MODEL.uk.md |

---

# 3. Repository Navigation

| Scenario | Navigation Path |
|----------|----------------|
| Find English spec | telegram/specs/TELEGRAM_*_MODEL.md |
| Find Ukrainian spec | telegram/specs/TELEGRAM_*_MODEL.uk.md |
| Find all versions | telegram/specs/TELEGRAM_*_MODEL*.md |
| Compare versions | Side-by-side in same directory |

---

# 4. Strategy Verdict

**filename.uk.md is the optimal strategy.**

It follows international GitHub/Open Source best practices, preserves parallel files, enables easy cross-linking, and maintains repository navigation simplicity.

---

**End of Repository Strategy**

**Strategist:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
