# CASE001_PUBLICATION_LIFECYCLE_RECONSTRUCTION

**Document ID:** CASE001B-LIFECYCLE

**Title:** Publication — Complete Lifecycle Reconstruction

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document reconstructs the complete life of one Publication from the moment it does not exist until it permanently disappears.

---

# The Life of One Publication

## Phase 0: Non-Existence

**State:** Publication does not exist.

**What exists:**

- DSO publishes outage data (Open Data)
- Parser retrieves and normalizes data
- Normalized Dataset is stored in Data Storage
- Schedule Generator produces schedules
- Graphic Generator produces graphics

**Evidence:** TJS-010 §3.3, GLOSSARY.md §2

---

## Phase 1: Creation

**Trigger:** Normalized Dataset becomes available for a Territory.

**Actor:** Publication Engine (implements Publisher Role).

**Process:**

1. Publication Engine receives Normalized Dataset
2. Publication Engine selects Canonical Template (A, B, C, or D)
3. Publication Engine applies Rendering Rules
4. Publication Engine renders Publication as Telegram HTML
5. Publication enters **Generated** state

**What changes:**

- Publication comes into existence
- Territory is assigned
- Template is assigned
- Content is rendered
- Lifecycle state = Generated

**What never changes:**

- Territory (fixed at creation)
- Template (fixed at creation)
- Source data (traceable to original)

**Identity continuity:** Publication is identified by Territory + Date + Template.

**Evidence:** TJS-021 §6.1, TJS-010 §4.1, Legacy TJS-007 §4

---

## Phase 2: Delivery

**Trigger:** Publication is Generated.

**Actor:** Telegram Publisher.

**Process:**

1. Publication Engine packages Publications into Publication Package
2. Publication Package is sent to Telegram Publisher
3. Telegram Publisher delivers to Telegram Channel
4. Telegram assigns **Telegram Message ID**
5. Publication transitions from Generated to **Published**
6. Publication becomes visible to Subscribers

**What changes:**

- Telegram Message ID is assigned
- Lifecycle state = Published
- Publication becomes visible

**What never changes:**

- Territory
- Template
- Content (unless data changes)
- Source data

**Identity continuity:** Telegram Message ID is added as external reference.

**Evidence:** TJS-021 §5.1, TJS-010 §3.3, Legacy TJS-007 §4

---

## Phase 3: Active Life (Conditional Updates)

**Trigger:** Normalized Dataset changes OR Rendering Rules change.

**Actor:** Publication Engine.

**Process:**

1. Publication Engine detects dataset change
2. Publication Engine re-renders affected Publications
3. Canonical Equality check performed
4. If different: Telegram Publisher edits existing Telegram message
5. Publication transitions from Published to **Updated**
6. Publication transitions from Updated back to **Published**

**What changes:**

- Content (if data changed)
- Lifecycle state = Updated → Published
- Telegram message is edited

**What never changes:**

- Territory
- Template
- Telegram Message ID
- Source data (traceable to original)

**Identity continuity:** Same Territory + Date + Template + Telegram Message ID.

**Constraints:**

- Updates SHOULD modify in place (TJS-021 §7.1)
- Replacing is last resort (TJS-021 §7.2)
- Original meaning preserved (TJS-021 §6.2)

**Evidence:** TJS-021 §5.2, §5.3, §6.2, Legacy TJS-007 §5, §6

---

## Phase 4: Archival

**Trigger:** Reporting period ends (next day approximately 05:00).

**Actor:** Publication Engine (automated).

**Process:**

1. Reporting period ends
2. All current-day Publications are archived
3. Publications remain in Telegram Journal permanently
4. Publications transition from Published to **Archived**
5. Archived Publications SHALL NOT be deleted

**What changes:**

- Lifecycle state = Archived
- Publication becomes historical record

**What never changes:**

- Territory
- Template
- Content
- Telegram Message ID
- Source data

**Identity continuity:** Same Territory + Date + Template + Telegram Message ID. Now permanently archived.

**Evidence:** TJS-021 §5.4, §6.3, Legacy TJS-007 §9

---

## Phase 4b: Removal (Conditional — Temporary Publications Only)

**Trigger:** Publication is temporary AND no longer relevant.

**Actor:** Publication Engine (automated).

**Process:**

1. Only Tomorrow Publications are temporary
2. Next day approximately 05:00
3. Obsolete Tomorrow Publications are deleted
4. Publications transition from Published to **Removed**
5. Removed Publications are no longer visible

**What changes:**

- Lifecycle state = Removed
- Publication disappears from Telegram

**What never changes:**

- Territory
- Template
- Content (until deletion)

**Identity continuity:** Telegram Message ID is released. Publication ceases to exist.

**Constraints:**

- Only temporary Publications MAY be removed (TJS-021 §5.5)
- Permanent Publications SHALL NOT be removed (TJS-021 §5.6)
- Manual Publications SHALL NOT be removed (Legacy TJS-007 §11)

**Evidence:** TJS-021 §5.5, §5.6, §6.4, Legacy TJS-007 §8, TJS-008 §12

---

## Phase 5: Permanent Existence (Archived Publications)

**State:** Publication exists permanently in Archive.

**What exists:**

- Historical record in Telegram Journal
- Data in Data Storage
- Traceable to source data

**What never changes:**

- Territory
- Template
- Content
- Telegram Message ID
- Source data

**Identity continuity:** Publication is permanently identified and preserved.

**Evidence:** TJS-021 §4.4, GLOSSARY.md §3

---

# Complete Lifecycle Diagram

```text
                    ┌─────────────────┐
                    │   Non-Existence  │
                    │  (Phase 0)       │
                    └────────┬────────┘
                             │
                             │ Trigger: Normalized Dataset available
                             │ Actor: Publication Engine
                             ▼
                    ┌─────────────────┐
                    │    Generated     │
                    │  (Phase 1)       │
                    │  Repository only │
                    └────────┬────────┘
                             │
                             │ Trigger: Delivery to Telegram
                             │ Actor: Telegram Publisher
                             ▼
                    ┌─────────────────┐
            ┌──────│    Published     │──────┐
            │      │  (Phase 2)       │      │
            │      │  Visible on      │      │
            │      │  Telegram        │      │
            │      └────────┬────────┘      │
            │               │               │
            │               ▼               │
            │      ┌─────────────────┐      │
            │      │    Updated      │      │
            │      │  (Phase 3)       │      │
            │      │  Modified in     │      │
            │      │  place           │      │
            │      └────────┬────────┘      │
            │               │               │
            │               ▼               │
            │      ┌─────────────────┐      │
            └─────►│    Published    │◄─────┘
                   │  (Back to       │
                   │   Published)    │
                   └────────┬────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
     ┌─────────────────┐        ┌─────────────────┐
     │    Archived     │        │    Removed      │
     │  (Phase 4)       │        │  (Phase 4b)     │
     │  Permanent       │        │  Temporary only │
     │  record          │        │  No longer      │
     └─────────────────┘        │  visible        │
                                └─────────────────┘
```

---

# Lifecycle States Summary

| State | Description | Duration | Visibility |
|-------|-------------|----------|------------|
| Generated | Created from normalized data | Momentary | Repository only |
| Published | Live on Telegram | Until next update or archival | Subscribers |
| Updated | Modified after initial publication | Momentary | Subscribers |
| Archived | Preserved as historical record | Permanent | Subscribers (historical) |
| Removed | Deleted from Telegram | Permanent | None |

---

# End of Lifecycle Reconstruction
