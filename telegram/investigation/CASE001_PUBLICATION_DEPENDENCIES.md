# CASE001_PUBLICATION_DEPENDENCIES

**Document ID:** CASE001-PUB-004

**Title:** Publication — Dependency Analysis

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Semantic Investigation №001

---

# Purpose

This document determines which concepts are impossible without Publication and which concepts Publication depends upon.

---

# Concepts That Publication Depends Upon

These concepts MUST exist for Publication to exist.

| # | Concept | Nature of Dependency | Evidence |
|---|---------|---------------------|----------|
| D-01 | Normalized Dataset | Publication is generated FROM normalized data | TJS-010 §3.3, TJS-021 §6.1 |
| D-02 | Interpretation Result | GLOSSARY says Publication is "derived exclusively from an Interpretation Result" | GLOSSARY.md §3 |
| D-03 | Open Data | Publication must be traceable to official source | GLOSSARY.md, CHARTER.md |
| D-04 | Data Source | Open Data comes from Data Source | GLOSSARY.md §2 |
| D-05 | Parser | Parser produces Normalized Dataset | TJS-010 §3.3 |
| D-06 | Publication Engine | Publication Engine generates Publication | TJS-010 §4.1 |
| D-07 | Territory | Every Publication represents exactly one Territory | Legacy TJS-007 §4, TJS-010 |
| D-08 | Canonical Template | Every Publication uses one Canonical Template | Legacy TJS-007 §4, TJS-005 |
| D-09 | Rendering Rules | Publication is rendered using Rendering Rules | Legacy TJS-007 §4, TJS-006 |
| D-10 | Issue | Publication belongs to an Issue | TJS-000 §4, TJS-000A |
| D-11 | Journal | Journal contains Issues which contain Publications | TJS-000 §4 |
| D-12 | Reporting Period | Publication is generated during one Reporting Period | GLOSSARY.md §3 |
| D-13 | Telegram Message ID | Publication receives Telegram Message ID after publication | Legacy TJS-007 §4 |
| D-14 | Repository | Repository is authoritative source of publication state | TJS-021 §3.1 |

---

# Concepts That Depend Upon Publication

These concepts CANNOT exist without Publication.

| # | Concept | Nature of Dependency | Evidence |
|---|---------|---------------------|----------|
| P-01 | Publication Package | Package is collection of Publications | GLOSSARY.md §3, TJS-000A |
| P-02 | Publication Lifecycle | Lifecycle governs Publication | TJS-021 |
| P-03 | Publication Engine | Engine generates Publications | TJS-010 §4.1 |
| P-04 | Publisher Role | Publisher creates Publications | GLOSSARY.md §3 |
| P-05 | Telegram Publisher | Delivers Publications to Telegram | TJS-010 §4.4 |
| P-06 | Text Publication | Derived type of Publication | TJS-000A §9 |
| P-07 | Graphic Publication | Derived type of Publication | TJS-000A §9, TJS-022 |
| P-08 | City Today | Derived type of Publication | TJS-000A §9, TJS-005 |
| P-09 | District Today | Derived type of Publication | TJS-000A §9, TJS-005 |
| P-10 | City Tomorrow | Derived type of Publication | TJS-000A §9, TJS-005 |
| P-11 | District Tomorrow | Derived type of Publication | TJS-000A §9, TJS-005 |
| P-12 | Today's Package | Derived type of Publication Package | TJS-000A §9 |
| P-13 | Tomorrow Package | Derived type of Publication Package | TJS-000A §9 |
| P-14 | Publication Ownership | Ownership model for Publications | TJS-010 §4.1, Legacy TJS-007 §10 |
| P-15 | Non-destructive Channel | Principle about modifying only owned Publications | TJS-000A, TJS-021 |
| P-16 | Non-destructive Update | Principle about modifying instead of replacing | TJS-000A, TJS-021 |
| P-17 | Canonical Equality | Comparison of identical Publications | TJS-000A, Legacy TJS-007 §6 |
| P-18 | Publication Session | One execution producing complete Journal state | TJS-000A, Legacy TJS-008 §15 |
| P-19 | Daily Publication Cycle | Daily operational cycle of Publications | TJS-000A, Legacy TJS-008 §3 |
| P-20 | Publication Windows | Time windows for engine operation | TJS-000A, Legacy TJS-008 §6 |
| P-21 | Traceability | Ability to identify origin of every Publication | TJS-000A, GLOSSARY.md |
| P-22 | Reliability | Guarantee of non-duplication | TJS-000A, Legacy TJS-002 §12 |
| P-23 | Archive | Preserved historical Publications | GLOSSARY.md, TJS-021 |
| P-24 | Long Publication Split | Division between Settlement blocks | TJS-000A, Legacy TJS-006 §10 |
| P-25 | Stable Output Rule | No cosmetic formatting changes | TJS-000A, Legacy TJS-006 §12 |
| P-26 | Empty Block Rule | No empty sections | TJS-000A, Legacy TJS-006 §13 |
| P-27 | Error Handling | Failure recovery rules | TJS-000A, Legacy TJS-007 §13 |

---

# Dependency Graph

```text
                    Open Data
                        │
                        ▼
                  Data Source
                        │
                        ▼
                    Parser
                        │
                        ▼
               Normalized Dataset
                        │
                        ▼
              Interpretation Result
                        │
                        ▼
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
    Territory                   Canonical Template
         │                             │
         └──────────────┬──────────────┘
                        │
                        ▼
                 Rendering Rules
                        │
                        ▼
               ┌────────────────┐
               │                │
               ▼                ▼
          Publication      Issue
               │                │
               │                ▼
               │            Journal
               │
               ▼
      ┌────────────────┐
      │                │
      ▼                ▼
 Publication     Telegram Message ID
    Package              │
      │                  │
      ▼                  ▼
  Archive        Telegram Channel
                       │
                       ▼
                  Subscribers
```

---

# Critical Path

The minimum concepts required for a single Publication to exist:

1. Open Data (source)
2. Data Source (origin)
3. Parser (retrieval)
4. Normalized Dataset (intermediate)
5. Territory (scope)
6. Canonical Template (format)
7. Rendering Rules (transformation)
8. Publication Engine (generation)
9. Publication (result)

---

# Circular Dependencies

**None found.**

All dependencies flow in one direction from Open Data to Publication to Consumers.

---

# End of Document
