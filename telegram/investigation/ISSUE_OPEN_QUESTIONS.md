# ISSUE_OPEN_QUESTIONS

**Document ID:** CASE002A-QUESTIONS

**Title:** Issue — Open Questions

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Investigation

---

# Purpose

This document lists every unresolved question about Issue.

---

# Repository Gaps

## Gap RG-001: No Issue Definition in GLOSSARY.md

**Gap:** GLOSSARY.md does not define "Issue".

**Impact:** HIGH — affects terminology consistency.

**What Is Needed:** Explicit definition of "Issue" in GLOSSARY.md.

**Evidence:** GLOSSARY.md §3 defines Publication, Publication Package, but not Issue.

---

## Gap RG-002: No Issue Identity Model

**Gap:** No specification defines Issue identity model.

**Impact:** MEDIUM — affects identity clarity.

**What Is Needed:** Explicit identity criteria for Issue.

**Evidence:** TJS-000 §4 implies Identity is Calendar day, but not explicitly stated.

---

## Gap RG-003: No Issue Ownership Model

**Gap:** No specification defines who owns Issue.

**Impact:** MEDIUM — affects ownership clarity.

**What Is Needed:** Explicit ownership for Issue.

**Evidence:** TJS-000 §5 implies Issue owns "Daily edition, date scope" but doesn't say who owns Issue.

---

## Gap RG-004: No Issue Identifier Model

**Gap:** No specification defines Issue identifier.

**Impact:** MEDIUM — affects identification clarity.

**What Is Needed:** Explicit identifier for Issue.

**Evidence:** DATA_MODEL.md requires unique identification, but no Issue ID is defined.

---

# Conceptual Gaps

## Gap CG-001: Circular Dependency Not Resolved

**Gap:** Publication belongs to Issue, but Issue opens when first Publication is generated.

**Impact:** HIGH — affects conceptual clarity.

**What Is Needed:** Resolution of circular dependency.

**Evidence:** TJS-000 §4, TJS-021 §8.1

---

## Gap CG-002: Issue Lifecycle Not Fully Defined

**Gap:** Issue lifecycle is defined briefly in TJS-021 §8, but not in detail.

**Impact:** MEDIUM — affects lifecycle clarity.

**What Is Needed:** Detailed Issue lifecycle model.

**Evidence:** TJS-021 §8 has 3 phases; Publication lifecycle has 5 states.

---

## Gap CG-003: Issue Relationship with Reporting Period Unclear

**Gap:** No specification defines relationship between Issue and Reporting Period.

**Impact:** LOW — affects temporal model clarity.

**What Is Needed:** Clarification of Issue vs Reporting Period.

**Evidence:** GLOSSARY.md §2 defines Reporting Period; TJS-000 §4 defines Issue.

---

# Missing Evidence

## Gap ME-001: No Evidence of Issue Deletion

**Gap:** No specification addresses what happens when Issue is deleted.

**Impact:** MEDIUM — affects lifecycle completeness.

**What Is Needed:** Evidence of Issue deletion rules.

**Evidence:** TJS-021 §8.3 says Issue becomes historical, but doesn't address deletion.

---

## Gap ME-002: No Evidence of Issue Recreation

**Gap:** No specification addresses whether Issue can be recreated.

**Impact:** LOW — affects lifecycle completeness.

**What Is Needed:** Evidence of Issue recreation rules.

**Evidence:** No specification addresses this.

---

## Gap ME-003: No Evidence of Issue Migration

**Gap:** No specification addresses whether Issue can be migrated.

**Impact:** LOW — affects portability.

**What Is Needed:** Evidence of Issue migration rules.

**Evidence:** No specification addresses this.

---

# Architectural Uncertainties

## Gap AU-001: Issue as Domain Object vs Editorial Concept

**Gap:** Unclear whether Issue is a domain object or an editorial concept.

**Impact:** MEDIUM — affects ontological position.

**What Is Needed:** Clarification of Issue nature.

**Evidence:** TJS-000 §4 defines Issue as "editorial edition"; investigations treat it as "domain object".

---

## Gap AU-002: Issue Lifecycle vs Publication Lifecycle Relationship

**Gap:** Unclear whether Issue lifecycle is independent or derived from Publication lifecycle.

**Impact:** MEDIUM — affects lifecycle architecture.

**What Is Needed:** Clarification of lifecycle relationship.

**Evidence:** TJS-021 §8 defines both; relationship unclear.

---

## Gap AU-003: Issue Container vs Collection Nature

**Gap:** Unclear whether Issue is a container (holds Publications) or a collection (is composed of Publications).

**Impact:** LOW — affects structural model.

**What Is Needed:** Clarification of structural nature.

**Evidence:** Both terms used in investigations.

---

# Open Questions Summary

| Category | Count |
|----------|-------|
| Repository Gaps | 4 |
| Conceptual Gaps | 3 |
| Missing Evidence | 3 |
| Architectural Uncertainties | 3 |
| **Total** | **13** |

---

# End of Open Questions
