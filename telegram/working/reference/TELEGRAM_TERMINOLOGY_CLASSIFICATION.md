# Telegram Terminology Classification

**Date:** 2026-07-13
**Purpose:** Classification of every discovered concept
**Source:** TELEGRAM_TERMINOLOGY_MATRIX.md

---

# Classification Categories

| Category | Description |
|----------|-------------|
| Core | Foundational semantic concepts owned by TJS-000 |
| Supporting | Concepts used by TJS specifications |
| Platform | Telegram-specific technical concepts |
| Derived | Concepts derived from core concepts |
| Administrative | Territorial and geographic concepts |
| Architectural | Governance and methodology concepts |
| Audit | Analysis and review concepts |
| Migration | Migration-specific concepts |
| Process | Workflow and procedure concepts |

---

# Core Concepts (8)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 1 | Journal | TJS-000 | Core |
| 2 | Issue | TJS-000 | Candidate |
| 3 | Publication | TJS-000 | Core |
| 4 | Telegram | TJS-000 | Core |
| 5 | Publication Engine | TJS-000 | Core |
| 6 | Publisher | TJS-000 | Core |
| 7 | Parser | GLOSSARY | Core |
| 8 | SvitloSk | TJS-001 | Core |

---

# Supporting Concepts — Lifecycle (22)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 9 | Publication Lifecycle | TJS-005 | Core |
| 10 | Lifecycle State Model | TJS-005 | Core |
| 11 | Generated | TJS-005 | Supporting |
| 12 | Published | TJS-005 | Supporting |
| 13 | Updated | TJS-005 | Supporting |
| 14 | Archived | TJS-005 | Supporting |
| 15 | Removed | TJS-005 | Supporting |
| 16 | Temporary Publication | TJS-005 | Supporting |
| 17 | Permanent Publication | TJS-005 | Supporting |
| 18 | Update Rules | TJS-005 | Supporting |
| 19 | Archive Policy | TJS-005 | Supporting |
| 20 | Deletion Policy | TJS-005 | Supporting |
| 21 | Publication Ownership | TJS-005 | Supporting |
| 22 | Non-destructive Channel Principle | TJS-005 | Supporting |
| 23 | Non-destructive Update Principle | TJS-005 | Supporting |
| 24 | Publication Session | TJS-005 | Supporting |
| 25 | Daily Publication Cycle | TJS-005 | Supporting |
| 26 | Publication Windows | TJS-005 | Supporting |
| 27 | Traceability | TJS-005 | Supporting |
| 28 | Reliability | TJS-005 | Supporting |
| 29 | Canonical Equality | TJS-005 | Supporting |
| 30 | Error Handling | TJS-005 | Supporting |

---

# Supporting Concepts — Templates & Structure (15)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 31 | Publication Structure | TJS-003 | Supporting |
| 32 | Publication Grammar | TJS-003 | Supporting |
| 33 | Canonical Templates | TJS-003 | Supporting |
| 34-37 | Template A/B/C/D | TJS-003 | Derived |
| 38 | Territory Header | TJS-003 | Supporting |
| 39 | Publication Sections | TJS-003 | Supporting |
| 40 | Header | TJS-003 | Supporting |
| 41 | Main Information | TJS-003 | Supporting |
| 42 | Graphic Block | TJS-003 | Supporting |
| 43 | Additional Information | TJS-003 | Supporting |
| 44 | Footer | TJS-003 | Supporting |
| 45 | Validation Rules | TJS-003 | Supporting |

---

# Supporting Concepts — Formatting (10)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 46 | Formatting Rules | TJS-004 + TJS-005 | Supporting |
| 47 | Editorial Policy | TJS-004 | Core |
| 48 | Editorial Principles | TJS-004 | Supporting |
| 49 | Territory Presentation | TJS-004 | Supporting |
| 50 | Message Categories | TJS-004 | Supporting |
| 51 | Time Format | TJS-004 | Supporting |
| 52 | Settlement Formatting | TJS-004 | Supporting |
| 53 | Address Formatting | TJS-004 | Supporting |
| 54 | Branding | TJS-004 | Supporting |
| 55 | Editing Rules | TJS-003 | Supporting |

---

# Supporting Concepts — Rendering (13)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 56 | Rendering Pipeline | TJS-004 | Core |
| 57 | Deterministic Rendering | TJS-004 | Supporting |
| 58 | Stable Ordering | TJS-004 | Supporting |
| 59 | Source Fidelity | TJS-004 | Supporting |
| 60 | Territory Ordering | TJS-004 | Supporting |
| 61 | Time Ordering | TJS-004 | Supporting |
| 62 | Settlement Ordering | TJS-004 | Supporting |
| 63 | Street Ordering | TJS-004 | Supporting |
| 64 | Duplicate Removal | TJS-004 | Supporting |
| 65 | Long Publication Split | TJS-004 | Supporting |
| 66 | HTML Rendering Rules | TJS-004 | Supporting |
| 67 | Stable Output Rule | TJS-004 | Supporting |
| 68 | Empty Block Rule | TJS-004 | Supporting |

---

# Platform Concepts (10)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 69 | Channel | TJS-000 | Platform |
| 70 | Telegram Message ID | TJS-005 | Platform |
| 71 | Telegram Bot API | TJS-006 (new) | Platform |
| 72 | Rate Limiting | TJS-006 (new) | Platform |
| 73 | Message Editing | TJS-006 (new) | Platform |
| 74 | Channel Administration | TJS-006 (new) | Platform |
| 75 | subscribers | TJS-001 | Platform |
| 76 | administrators | TJS-005 | Platform |
| 77 | Manual Publications | TJS-005 | Platform |
| 78 | Image Publications | TJS-005 | Platform |

---

# Derived Concepts (10)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 79 | Graphic Rendering | TJS-007 (new) | Derived |
| 80 | Text Publication | Implicit | Derived |
| 81 | System Publication | Implicit | Derived |
| 82-85 | City/District Today/Tomorrow | TJS-003 | Derived |
| 86 | Today's Package | TJS-005 | Derived |
| 87 | Tomorrow Package | TJS-005 | Derived |
| 88 | Publication Package | TJS-004 | Derived |

---

# Administrative Concepts (8)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 89 | Settlement | GLOSSARY | Administrative |
| 90 | Starosta District | GLOSSARY | Administrative |
| 91 | Community | GLOSSARY | Administrative |
| 92 | Administrative Centre | GLOSSARY | Administrative |
| 93 | Territory | GLOSSARY | Administrative |
| 94 | Street | GLOSSARY | Administrative |
| 95 | Address | GLOSSARY | Administrative |
| 96 | Time Interval | TJS-003 | Administrative |

---

# Architectural Concepts (7)

| # | Term | Owner | Status |
|---|------|-------|--------|
| 97 | SSOT | GLOSSARY | Architectural |
| 98 | SRP | PROJECT_PRINCIPLES | Architectural |
| 99 | Separation of Concerns | ARCHITECTURE | Architectural |
| 100 | Semantic Ownership Principle | TJS-000 | Architectural |
| 101 | One Document — One Subject | PROJECT_PRINCIPLES | Architectural |
| 102 | Dependency Direction | ARCHITECTURE | Architectural |
| 103 | Metadata Compliance | ARCHITECTURE | Architectural |

---

# Summary

| Category | Count |
|----------|-------|
| Core | 8 |
| Supporting — Lifecycle | 22 |
| Supporting — Templates | 15 |
| Supporting — Formatting | 10 |
| Supporting — Rendering | 13 |
| Platform | 10 |
| Derived | 10 |
| Administrative | 8 |
| Architectural | 7 |
| **Total** | **103** |

---

**End of Classification**

**Classifier:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
