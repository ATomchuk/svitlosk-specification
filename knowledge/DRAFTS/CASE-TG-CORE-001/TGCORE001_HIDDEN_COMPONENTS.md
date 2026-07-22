# TGCORE001_HIDDEN_COMPONENTS

**Document ID:** CASE-TG-CORE-001-HC

**Title:** Hidden Components

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies hidden components within Telegram subsystem.

---

# 2. Hidden Components

## 2.1 HC-001: Graph Generator

### Evidence

> "Queue Schedule Parser → Queue Schedule JSON → Graph Generator → SVG → PNG → Telegram publication" (Architect Context)

### Function

Generates visual graphs from queue schedule data.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

PARTIALLY — SVG/PNG generation is generic, but Telegram image format is specific.

---

## 2.2 HC-002: Text Formatter

### Evidence

> Telegram messages use specific formatting (markdown, HTML).

### Function

Formats text for Telegram display.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

YES — Telegram formatting is specific.

---

## 2.3 HC-003: Message Builder

### Evidence

> Telegram posts are built from publications.

### Function

Constructs complete messages from publication data.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

PARTIALLY — message structure is generic, but Telegram format is specific.

---

## 2.4 HC-004: Technical Message Builder

### Evidence

> "technical update message" (Architect Intent)

### Function

Builds technical system messages.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

PARTIALLY — content is generic, but format is specific.

---

## 2.5 HC-005: Territory Organizer

### Evidence

> "Journal publications are grouped by Starosta Districts." (Architect Intent)

### Function

Organizes publications by territory.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

NO — territory organization is generic.

---

## 2.6 HC-006: Lifecycle Manager

### Evidence

> Publications have states: Generated, Published, Updated, Archived, Removed. (TELEGRAM_PUBLICATION_LIFECYCLE.md)

### Function

Manages publication lifecycle.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

NO — lifecycle management is generic.

---

## 2.7 HC-007: Change Detector

### Evidence

> "Publications MAY be updated only when the normalized dataset changes." (TELEGRAM_PUBLICATION_LIFECYCLE.md)

### Function

Detects when data has changed.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

NO — change detection is generic.

---

## 2.8 HC-008: Expiry Detector

### Evidence

> "Tomorrow information disappears automatically before the end of the current day." (Architect Intent)

### Function

Detects when temporary information should expire.

### Location

Currently inside Telegram subsystem.

### Channel-Specific?

NO — expiry detection is generic.

---

# 3. Hidden Component Summary

| ID | Component | Channel-Specific? | Evidence |
|----|-----------|-------------------|----------|
| HC-001 | Graph Generator | PARTIALLY | Architect Context |
| HC-002 | Text Formatter | YES | Telegram formatting |
| HC-003 | Message Builder | PARTIALLY | Telegram posts |
| HC-004 | Technical Message Builder | PARTIALLY | Architect Intent |
| HC-005 | Territory Organizer | NO | Architect Intent |
| HC-006 | Lifecycle Manager | NO | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| HC-007 | Change Detector | NO | TELEGRAM_PUBLICATION_LIFECYCLE.md |
| HC-008 | Expiry Detector | NO | Architect Intent |

---

# 4. Findings

## 4.1 Finding HC-001

**8 hidden components were identified.**

**Evidence:** Analysis of Telegram subsystem.

**Confidence:** HIGH.

## 4.2 Finding HC-002

**4 components are CHANNEL-INDEPENDENT.**

Territory Organizer, Lifecycle Manager, Change Detector, Expiry Detector.

**Evidence:** Analysis of hidden components.

**Confidence:** HIGH.

## 4.3 Finding HC-003

**4 components are PARTIALLY or FULLY channel-specific.**

Graph Generator, Text Formatter, Message Builder, Technical Message Builder.

**Evidence:** Analysis of hidden components.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| HC-001 | Analysis of Telegram subsystem |
| HC-002 | Analysis of hidden components |
| HC-003 | Analysis of hidden components |

---

**End of Hidden Components**
