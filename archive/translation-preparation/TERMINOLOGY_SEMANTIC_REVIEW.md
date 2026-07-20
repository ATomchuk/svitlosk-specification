# TERMINOLOGY_SEMANTIC_REVIEW

**Document ID:** TSR-001

**Title:** Terminology Semantic Review

**Document Class:** Semantic Review

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Semantic analysis of three pending translation terms.

---

# 1. Publication Engine

## 1.1 Occurrence Analysis

| Metric | Value |
|--------|-------|
| Total occurrences | 145 |
| Canonical spec occurrences | ~40 (TJS-010, TJS-020, TJS-022) |
| Working doc occurrences | ~80 |
| Archive occurrences | ~25 |

## 1.2 Architectural Identity

"Publication Engine" is defined in TELEGRAM_GLOSSARY.md (§14):

> "The architectural Component implementing the Publisher Role. The Publication Engine is responsible for generating and distributing Publications."

It is NOT a service. It is NOT a pipeline. It is NOT a mechanism.

It IS an **architectural Component** — one of 8 primary components in the Telegram subsystem.

## 1.3 Contexts

| Context | Usage |
|---------|-------|
| TJS-010 §4.1 | Core component definition |
| Interaction Matrix | Receives from Parser, produces for Telegram Publisher |
| Component Matrix | Implements Publisher Role |
| Constraints | SHALL NOT modify manual/image publications |
| Glossary | "architectural Component implementing the Publisher Role" |

## 1.4 Candidate Translations

| # | Candidate | Advantages | Disadvantages |
|---|-----------|-----------|---------------|
| 1 | Движок публікацій | Natural Ukrainian IT term for "engine" | Slightly informal |
| 2 | Механізм публікацій | Formal, precise | Less common in IT |
| 3 | Система публікацій | Broad, familiar | Too broad — implies entire system |
| 4 | Компонент публікацій | Architecturally accurate | Loses "engine" semantics |
| 5 | Генератор публікацій | Captures "generates publications" | Incomplete — also distributes |

## 1.5 Semantic Recommendation

The Ukrainian translation should reflect that this is an **architectural Component**, not a generic engine. However, "Движок публікацій" is the most natural Ukrainian IT term and is widely understood. The architectural precision comes from context (it is always referred to as a Component), not from the name itself.

---

# 2. Canonical Equality

## 2.1 Occurrence Analysis

| Metric | Value |
|--------|-------|
| Total occurrences | 35 |
| Canonical spec occurrences | 2 (TJS-010 §11, TJS-022 C-003) |
| Glossary definition | 1 (TELEGRAM_GLOSSARY.md §14) |
| Working doc occurrences | ~20 |
| Archive occurrences | ~12 |

## 2.2 Origin and Intent

"Canonical Equality" was intentionally introduced as a quality guarantee in TJS-010 (Publishing Model) §11:

> "Two publications generated from identical datasets SHALL be byte-for-byte identical. Equivalent publications SHALL NOT generate Telegram edits."

It is defined in TELEGRAM_GLOSSARY.md:

> "The comparison of two Publications generated from identical datasets to determine whether they are byte-for-byte identical."

## 2.3 Semantic Analysis

| Concept | Match? | Reasoning |
|---------|--------|-----------|
| Canonical Equality | YES | Original term — comparison of identical output |
| Canonical Conformance | NO | Would mean "conforms to a standard" — different concept |
| Canonical Consistency | NO | Would mean "remains consistent over time" — different concept |
| Canonical Equivalence | PARTIAL | Close — but "equality" is stronger (byte-for-byte) |
| Translation Equivalence | NO | Would relate to translation, not rendering |

## 2.4 Candidate Translations

| # | Candidate | Advantages | Disadvantages |
|---|-----------|-----------|---------------|
| 1 | Канонічна рівність | Direct translation, already in Glossary | "рівність" may imply mathematical equality |
| 2 | Канонічна тотожність | Stronger identity semantics | "тотожність" implies strict logical identity |
| 3 | Канонічна ідентичність | Captures "identical output" | Less common in Ukrainian IT |
| 4 | Стандартна рівність | Implies standard-based | Loses "canonical" semantics |
| 5 | Канонічна однаковість | Natural Ukrainian for "sameness" | Less formal |

## 2.5 Semantic Recommendation

"Canonical Equality" is a well-defined, intentional project term. It means specifically "byte-for-byte identical output from identical input." The Ukrainian translation should capture this precision. "Канонічна рівність" is already in the Glossary and is the most established translation. "Канонічна тотожність" is a valid alternative if stronger identity semantics are desired.

---

# 3. Powered

## 3.1 Occurrence Analysis

| Metric | Value |
|--------|-------|
| Total occurrences | 15 |
| Canonical spec occurrences | 6 (TJS-022) |
| Working doc occurrences | 9 |

## 3.2 Context Analysis

"Powered" appears exclusively in the **Graphic Publication Model** (TJS-022) in these contexts:

| Context | Line | Meaning |
|---------|------|---------|
| Color semantics | §11 C-003 | "Powered = Orange" — visual state color |
| Timeline state | §5.1 | "Powered/Outage" — two states on timeline |
| Statistics | §5.5 | "Powered percentage" — percentage of time without outage |
| Color mapping | §11 | "Powered" paired with "Outage" as opposing states |

## 3.3 Semantic Interpretation

"Powered" in SvitloSk does NOT mean:

- "has electrical supply" (generic)
- "is connected to grid" (technical)
- "is operational" (system)

"Powered" in SvitloSk means:

- "NOT currently experiencing an outage"
- "the absence of a scheduled or emergency outage"
- "normal state — no interruption"

The project context is "знеструмлення" (outages). The opposite of "знеструмлення" is NOT "Powered" in the electrical engineering sense — it is "no outage" or "normal supply."

## 3.4 Linguistic Model

SvitloSk's linguistic model centers on:

| Concept | Ukrainian | English Equivalent |
|---------|-----------|-------------------|
| Outage event | Знеструмлення | Outage |
| No outage | Відсутність знеструмлення | No outage |
| Restoration | Відновлення електропостачання | Power restoration |
| Grid state | Стан мережі | Grid state |
| Schedule | Розклад | Schedule |

"Powered" is NOT part of this linguistic model. It is a graphic rendering shorthand for "no outage."

## 3.5 Candidate Translations

| # | Candidate | Advantages | Disadvantages |
|---|-----------|-----------|---------------|
| 1 | Без знеструмлення | Directly says "no outage" — matches project language | Long for a color label |
| 2 | Норма | Short, means "normal state" | Too generic |
| 3 | Електропостачання | Standard Ukrainian for "power supply" | Misleading — implies active supply |
| 4 | Забезпечення | Means "provision/supply" | Incomplete without context |
| 5 | Відсутність відключення | "Absence of disconnection" | Long, awkward |

## 3.6 Translation Recommendation

For the **color label** context (C-003: "Powered = Orange"), the translation should be SHORT and CLEAR. For the **statistics** context ("Powered percentage"), the translation should be DESCRIPTIVE.

| Context | Recommended | Alternative |
|---------|------------|-------------|
| Color label | Без знеструмлення | Норма |
| Statistics | Відсоток без знеструмлення | Відсоток норми |
| Timeline | Без знеструмлення / Знеструмлення | Норма / Відключення |

---

# 4. Summary

| Term | Occurrences | Semantic Clarity | Recommended Direction |
|------|-------------|-----------------|----------------------|
| Publication Engine | 145 | HIGH — architectural Component | Движок публікацій (natural IT term) |
| Canonical Equality | 35 | HIGH — well-defined quality guarantee | Канонічна рівність (already in Glossary) |
| Powered | 15 | MEDIUM — graphic shorthand for "no outage" | Без знеструмлення (matches project language) |

---

**End of Semantic Review**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
