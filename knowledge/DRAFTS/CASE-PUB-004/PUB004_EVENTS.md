# PUB004_EVENTS

**Document ID:** CASE-PUB-004-EV

**Title:** Event Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every event that can occur inside Publisher.

---

# 2. Event Inventory

## 2.1 Data Events

### EV-001: New Information Appears

**Trigger:** Parser produces new data.

**Example:** New emergency outage is published by DSO.

**Source:** Architect Intent — "new information appears"

---

### EV-002: Information Changes

**Trigger:** Parser detects data change.

**Example:** Emergency outage information is updated.

**Source:** Architect Intent — "information changes"

---

### EV-003: Information Disappears

**Trigger:** DSO removes information.

**Example:** Emergency outage is resolved.

**Source:** Architect Intent — "information disappears"

---

## 2.2 Publication Events

### EV-004: Publication Expires

**Trigger:** Time-based expiry.

**Example:** Tomorrow's planned outage publication expires at end of day.

**Source:** Architect Intent — "publication expires"

---

### EV-005: Publication Becomes Obsolete

**Trigger:** New data makes publication irrelevant.

**Example:** Planned outage is cancelled.

**Source:** Architect Intent — "publication becomes obsolete"

---

### EV-006: Publication Needs Update

**Trigger:** Data change affects existing publication.

**Example:** Emergency outage time changes.

**Source:** CASE-TG-CORE-001 — change detection

---

## 2.3 Graph Events

### EV-007: Graph Changes

**Trigger:** Queue schedule data changes.

**Example:** Tomorrow's queue schedule is updated.

**Source:** Architect Intent — "graph changes"

---

### EV-008: Graph Becomes Available

**Trigger:** Tomorrow's schedule is published.

**Example:** Tomorrow's queue graph can be generated.

**Source:** Architect Intent — queue graph availability

---

### EV-009: Graph Expires

**Trigger:** End of current day.

**Example:** Tomorrow's queue graph is no longer relevant.

**Source:** Architect Intent — temporary nature

---

## 2.4 Technical Events

### EV-010: Technical Message Changes

**Trigger:** System status update.

**Example:** System maintenance scheduled.

**Source:** Architect Intent — "technical message changes"

---

### EV-011: Service Announcement Published

**Trigger:** New service announcement.

**Example:** Future project feature announced.

**Source:** Architect Intent — service publications

---

## 2.5 Lifecycle Events

### EV-012: Reporting Period Ends

**Trigger:** End of day.

**Example:** Current day's publications should be archived.

**Source:** GLOSSARY §2 — Reporting Period

---

### EV-013: New Reporting Period Begins

**Trigger:** Start of new day.

**Example:** New Journal Edition should be created.

**Source:** Architect Intent — daily cycle

---

### EV-014: Publication State Change

**Trigger:** Lifecycle transition.

**Example:** Publication moves from Generated to Published.

**Source:** TELEGRAM_LIFECYCLE.md

---

## 2.6 Channel Events

### EV-015: Channel Becomes Available

**Trigger:** Channel connection established.

**Example:** Telegram bot connects.

**Source:** CASE-TG-CORE-001

---

### EV-016: Channel Becomes Unavailable

**Trigger:** Channel connection lost.

**Example:** Telegram API unreachable.

**Source:** CASE-TG-CORE-001

---

### EV-017: Channel Message Delivered

**Trigger:** Message successfully sent.

**Example:** Telegram post published.

**Source:** CASE-TG-CORE-001

---

### EV-018: Channel Message Failed

**Trigger:** Message delivery failed.

**Example:** Telegram API error.

**Source:** CASE-TG-CORE-001

---

# 3. Event Classification

| ID | Event | Category | Trigger Type |
|----|-------|----------|--------------|
| EV-001 | New Information Appears | Data | External |
| EV-002 | Information Changes | Data | External |
| EV-003 | Information Disappears | Data | External |
| EV-004 | Publication Expires | Publication | Time |
| EV-005 | Publication Becomes Obsolete | Publication | Data |
| EV-006 | Publication Needs Update | Publication | Data |
| EV-007 | Graph Changes | Graph | Data |
| EV-008 | Graph Becomes Available | Graph | Data |
| EV-009 | Graph Expires | Graph | Time |
| EV-010 | Technical Message Changes | Technical | Data |
| EV-011 | Service Announcement Published | Technical | External |
| EV-012 | Reporting Period Ends | Lifecycle | Time |
| EV-013 | New Reporting Period Begins | Lifecycle | Time |
| EV-014 | Publication State Change | Lifecycle | Internal |
| EV-015 | Channel Becomes Available | Channel | External |
| EV-016 | Channel Becomes Unavailable | Channel | External |
| EV-017 | Channel Message Delivered | Channel | External |
| EV-018 | Channel Message Failed | Channel | External |

---

# 4. Findings

## 4.1 Finding EV-001

**There are 18 events.**

Across 6 categories: Data (3), Publication (3), Graph (3), Technical (2), Lifecycle (3), Channel (4).

**Evidence:** Analysis of all sources.

**Confidence:** HIGH.

## 4.2 Finding EV-002

**Events are triggered by 4 types.**

External (7), Time (4), Data (5), Internal (1).

**Evidence:** Analysis of event classification.

**Confidence:** HIGH.

## 4.3 Finding EV-003

**Data events are the MOST COMMON.**

7 events triggered by data changes.

**Evidence:** Analysis of event classification.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| EV-001 | Analysis of all sources |
| EV-002 | Analysis of event classification |
| EV-003 | Analysis of event classification |

---

**End of Event Inventory**
