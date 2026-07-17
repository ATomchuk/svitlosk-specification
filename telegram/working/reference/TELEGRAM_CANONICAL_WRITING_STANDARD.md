# Telegram Canonical Writing Standard

**Date:** 2026-07-13
**Scope:** Normative writing rules for Telegram specifications
**Status:** STANDARD DEFINED

---

# Purpose

This document defines the normative writing rules for all Telegram specifications.

---

# RFC 2119 Rules

| Term | Meaning | Use When | Example |
|------|---------|----------|---------|
| SHALL | Mandatory requirement | Defining mandatory behaviour | "Publications SHALL use only Glossary-approved terminology" |
| SHALL NOT | Prohibition | Defining what is forbidden | "Publications SHALL NOT redefine semantic concepts" |
| SHOULD | Recommended action | Recommending but not requiring | "Specifications SHOULD use active voice" |
| MAY | Optional action | Allowing but not requiring | "The Publisher MAY use either form" |

---

# Writing Rules

## WR-001: One Concept Per Paragraph

**Rule:** Each paragraph SHALL address exactly one concept.

**Rationale:** Ensures clarity and prevents concept mixing.

---

## WR-002: One Responsibility Per Section

**Rule:** Each section SHALL own exactly one responsibility.

**Rationale:** Ensures single responsibility and prevents duplication.

---

## WR-003: Prohibition of Implementation

**Rule:** Specifications SHALL NOT describe implementation details, algorithms, workflows, Telegram API specifics, rendering algorithms, or infrastructure.

**Rationale:** Specifications define WHAT, not HOW.

---

## WR-004: Glossary Compliance

**Rule:** All terms SHALL come from TELEGRAM_GLOSSARY.md. No term SHALL be introduced without Glossary approval.

**Rationale:** Ensures semantic consistency across all specifications.

---

## WR-005: RFC 2119 Usage

**Rule:** RFC 2119 terminology SHALL be used correctly. All keywords SHALL be uppercase.

**Rationale:** Ensures normative clarity.

---

## WR-006: Terminology Discipline

**Rule:** The same concept SHALL always use the same term. No synonyms permitted.

**Rationale:** Ensures semantic consistency.

---

## WR-007: Professional Language

**Rule:** Specifications SHALL use professional architectural language. No colloquialisms, no jargon, no ambiguous terms.

**Rationale:** Ensures readability and professionalism.

---

## WR-008: Active Voice

**Rule:** Specifications SHALL use active voice where possible.

**Rationale:** Ensures clarity and directness.

---

## WR-009: Present Tense

**Rule:** Definitions SHALL use present tense.

**Rationale:** Ensures timeless definitions.

---

## WR-010: Short Sentences

**Rule:** Sentences SHALL NOT exceed 25 words.

**Rationale:** Ensures readability.

---

# Writing Style Summary

| Rule | Statement |
|------|-----------|
| WR-001 | One concept per paragraph |
| WR-002 | One responsibility per section |
| WR-003 | No implementation in specifications |
| WR-004 | All terms from Glossary |
| WR-005 | RFC 2119 correct usage |
| WR-006 | Same concept, same term |
| WR-007 | Professional language |
| WR-008 | Active voice |
| WR-009 | Present tense for definitions |
| WR-010 | Maximum 25 words per sentence |

---

**End of Writing Standard**

**Definer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
