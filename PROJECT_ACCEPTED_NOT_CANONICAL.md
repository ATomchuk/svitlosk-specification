# PROJECT_ACCEPTED_NOT_CANONICAL

**Document ID:** X-2-H5

**Title:** Project Accepted But Not Canonical

**Document Class:** Decision Classification

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Classify every architectural decision by status.

---

# 1. Accepted But Not Yet Canonical

| Decision | Reason | Expected Owner | Target Specification |
|----------|--------|---------------|---------------------|
| Publication pipeline architecture | Designed but not compiled | Publishing Model | TJS-010 |
| Parser behavior rules | Defined in Component Matrix but not in canonical spec | Publishing Model | TJS-010 |
| Publisher Role definition | Defined in Component Matrix but not in canonical spec | Publishing Model | TJS-010 |
| Publication Engine responsibilities | Defined in Component Matrix but not in canonical spec | Publishing Model | TJS-010 |
| Schedule Generator behavior | Defined in Component Matrix but not in canonical spec | Publishing Model | TJS-010 |
| Graphic Generator behavior | Defined in Component Matrix but not in canonical spec | Graphic Model | TJS-022 |
| Data Storage behavior | Defined in Component Matrix but not in canonical spec | Publishing Model | TJS-010 |
| Telegram Channel behavior | Defined in Component Matrix but not in canonical spec | Publishing Model | TJS-010 |

---

# 2. Candidate for TJS-010

| Decision | Reason | Owner | Target |
|----------|--------|-------|--------|
| Publication pipeline architecture | Core publishing functionality | Publishing Model | TJS-010 |
| Parser behavior | Data ingestion rules | Publishing Model | TJS-010 |
| Publisher Role | Logical publishing role | Publishing Model | TJS-010 |
| Publication Engine | Core publishing engine | Publishing Model | TJS-010 |
| Schedule Generator | Schedule generation rules | Publishing Model | TJS-010 |
| Data Storage | Data persistence rules | Publishing Model | TJS-010 |
| Telegram Channel | Channel delivery rules | Publishing Model | TJS-010 |
| Publication sequencing | Deterministic ordering | Publishing Model | TJS-010 |
| Publication synchronization | Repository synchronization | Publishing Model | TJS-010 |
| Publication timing | Publication windows | Publishing Model | TJS-010 |

---

# 3. Already Canonical

| Decision | Owner | Specification |
|----------|-------|--------------|
| Semantic Foundation | Semantic Model | TJS-000 |
| Glossary | Glossary | TJS-000A |
| Editorial System | Editorial Model | TJS-020 |
| Publication Lifecycle | Lifecycle | TJS-021 |
| Graphic Publication Model | Graphic Model | TJS-022 |
| Repository Authority | Lifecycle §3.1 | TJS-021 |
| Canonical Specification Standard | Repository | TJS-STD |
| Document Identity Model | Repository | TJS-IDL |

---

# 4. Rejected

| Decision | Reason |
|----------|--------|
| (None identified) | — |

---

# 5. Still Open

| Decision | Reason | Expected Resolution |
|----------|--------|-------------------|
| TJS-010 compilation | Pending Stage P-3 | Next phase |

---

# 6. Classification Summary

| Category | Count |
|----------|-------|
| Accepted but not canonical | 8 |
| Candidate for TJS-010 | 10 |
| Already canonical | 8 |
| Rejected | 0 |
| Still open | 1 |

---

**End of Decision Classification**

**Classifier:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
