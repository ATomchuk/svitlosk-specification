# ONTOLOGY_RELATIONSHIP_USAGE

**Document_ID:** OBA-005

**Title:** Ontology Relationship Usage

**Document Class:** Relationship Audit

**Status:** COMPLETE

**Author:** Independent Ontology Auditor

---

# 1. Relationship Usage

| # | Relationship | Used In | Unused? |
|---|-------------|---------|---------|
| 1 | Journal CONTAINS Issue | TJS-000 | NO |
| 2 | Issue CONTAINS Publication | TJS-000 | NO |
| 3 | Publication BELONGS TO Publication Package | TJS-010 | NO |
| 4 | Publication Engine IMPLEMENTS Publisher | TJS-010 | NO |
| 5 | Parser PRODUCES Normalized Dataset | TJS-010 | NO |
| 6 | Schedule Generator PRODUCES Schedules | TJS-010 | NO |
| 7 | Graphic Generator PRODUCES Graphics | TJS-010 | NO |
| 8 | Publication Engine CONSUMES Dataset | TJS-010 | NO |
| 9 | Publication Engine CONSUMES Schedules | TJS-010 | NO |
| 10 | Publication Engine CONSUMES Graphics | TJS-010 | NO |
| 11 | Publication Engine PRODUCES Package | TJS-010 | NO |
| 12 | Telegram Publisher DELIVERS Messages | TJS-010 | NO |
| 13 | Telegram Channel DELIVERS to Subscribers | TJS-010 | NO |
| 14 | Data Storage STORES Publications | TJS-010 | NO |
| 15 | Territory CONTAINS Community | TJS-022 | NO |
| 16 | Community CONTAINS Settlement | TJS-022 | NO |
| 17 | Settlement CONTAINS Street | TJS-022 | NO |
| 18 | Street CONTAINS Address | TJS-022 | NO |

---

# 2. Unused Relationships

| Count | Details |
|-------|---------|
| Unused | 0 |
| Partially used | 0 |
| Over-specified | 0 |

---

# 3. Relationship Verdict

**All 18 relationships are actively used in the specifications.** Zero unused relationships.

---

**End of Relationship Usage**

**Auditor:** Independent Ontology Auditor
**Date:** 2026-07-13
**Status:** COMPLETE — 18/18 used
