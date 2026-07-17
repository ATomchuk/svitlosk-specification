# Telegram Derived Terms

**Date:** 2026-07-13
**Purpose:** All Derived concepts with parent-child relationships
**Status:** APPROVED — semantic language frozen

---

# Derived Terms

Derived terms are concepts that inherit meaning from an APPROVED parent concept. They may be used only in the context of their parent concept.

---

## D-001: Text Publication

| Field | Value |
|-------|-------|
| English | Text Publication |
| Ukrainian | Текстова публікація |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication |
| Reason | A Publication containing text only (as opposed to Image Publications). Implicit concept — not explicitly defined in any TJS document but used implicitly. |

---

## D-002: Graphic Publication

| Field | Value |
|-------|-------|
| English | Graphic Publication |
| Ukrainian | Графічна публікація |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication |
| Reason | A Publication containing graphics. Overlaps with "Image Publications" (TJS-008 §14). Should be unified with Image Publications. |

---

## D-003: City Today

| Field | Value |
|-------|-------|
| English | City Today |
| Ukrainian | Місто сьогодні |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication |
| Reason | Template A type — publishes today's information for the Administrative Centre. |

---

## D-004: District Today

| Field | Value |
|-------|-------|
| English | District Today |
| Ukrainian | Округ сьогодні |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication |
| Reason | Template B type — publishes today's information for one Starosta District. |

---

## D-005: City Tomorrow

| Field | Value |
|-------|-------|
| English | City Tomorrow |
| Ukrainian | Місто завтра |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication |
| Reason | Template C type — publishes tomorrow's planned outages for the Administrative Centre. |

---

## D-006: District Tomorrow

| Field | Value |
|-------|-------|
| English | District Tomorrow |
| Ukrainian | Округ завтра |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication |
| Reason | Template D type — publishes tomorrow's planned outages for one Starosta District. |

---

## D-007: Today's Package

| Field | Value |
|-------|-------|
| English | Today's Package |
| Ukrainian | Пакет сьогодні |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication Package |
| Reason | All today's publications for the current reporting day. |

---

## D-008: Tomorrow Package

| Field | Value |
|-------|-------|
| English | Tomorrow Package |
| Ukrainian | Пакет завтра |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | Publication Package |
| Reason | All tomorrow's publications for the next reporting day. |

---

## D-009: Publication Package

| Field | Value |
|-------|-------|
| English | Publication Package |
| Ukrainian | Пакет публікацій |
| Status | DERIVED |
| Category | Derived |
| Parent Concept | — |
| Reason | Collection of publications for a territory. Derived from the concept of grouping publications. |

---

## Parent-Child Relationship Map

```text
Publication (APPROVED)
├── Text Publication (DERIVED)
├── Graphic Publication (DERIVED)
├── City Today (DERIVED)
├── District Today (DERIVED)
├── City Tomorrow (DERIVED)
├── District Tomorrow (DERIVED)
└── Temporary Publication (APPROVED — lifecycle term)

Publication Package (DERIVED)
├── Today's Package (DERIVED)
└── Tomorrow Package (DERIVED)
```

---

## Summary

| # | Derived Term | Parent | Status |
|---|-------------|--------|--------|
| D-001 | Text Publication | Publication | DERIVED |
| D-002 | Graphic Publication | Publication | DERIVED |
| D-003 | City Today | Publication | DERIVED |
| D-004 | District Today | Publication | DERIVED |
| D-005 | City Tomorrow | Publication | DERIVED |
| D-006 | District Tomorrow | Publication | DERIVED |
| D-007 | Today's Package | Publication Package | DERIVED |
| D-008 | Tomorrow Package | Publication Package | DERIVED |
| D-009 | Publication Package | — | DERIVED |

**Total Derived Terms:** 9

---

**End of Derived Terms**

**Approver:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
