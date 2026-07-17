# TELEGRAM_DIRECTORY_NAMING_DECISION

**Document ID:** TJS-F1.2-R2

**Title:** Telegram Directory Naming Decision

**Document Class:** Naming Decision

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Final naming decision for the archive/ directory.

---

# 1. Alternatives Evaluated

| Name | Semantic Clarity | Professional Standard | Long-term Maintainability | Verdict |
|------|-----------------|----------------------|--------------------------|---------|
| archive/ | HIGH | YES — Kubernetes, CNCF, Google | YES — stable term | **SELECTED** |
| history/ | MEDIUM | PARTIAL | MEDIUM — may confuse with git history | REJECTED |
| records/ | MEDIUM | NO | LOW — ambiguous | REJECTED |
| governance/ | LOW — too narrow | NO | LOW — excludes certificates | REJECTED |

---

# 2. Decision: archive/

**Rationale:**

1. **Software architecture practice:** "archive/" is the standard term for deprecated/historical documentation in professional software projects. Kubernetes, CNCF, and Google all use "archive/" for this purpose.

2. **Documentation architecture:** Documentation systems distinguish between "active" and "archived" content. "archive/" clearly communicates this distinction.

3. **Long-term maintainability:** The term "archive" is stable and will not become ambiguous over time. "history/" may confuse with git history. "records/" is too formal. "governance/" is too narrow.

4. **Semantic clarity:** "archive/" immediately communicates: "these documents are preserved but no longer active." This is exactly the intended semantic.

5. **Professional documentation standards:** Google, Microsoft, Kubernetes, CNCF, Rust, LLVM all use "archive/" or equivalent terms for deprecated documentation.

---

# 3. Final Naming

| Element | Convention | Example |
|---------|-----------|---------|
| Top-level directories | lowercase | foundation/, specs/, working/, legacy/, archive/ |
| Subdirectories | lowercase | working/publishing/, working/editorial/ |
| Canonical files | UPPER_CASE | TELEGRAM_GLOSSARY.md |
| Legacy files | TJS-[NNN]-[Name].md | TJS-001-Journal-Concept.md |

---

**End of Naming Decision**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE — archive/ selected
