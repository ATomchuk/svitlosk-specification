# CASE001_PUBLICATION_LIFECYCLE

**Document ID:** CASE001-PUB-003

**Title:** Publication — Lifecycle Reconstruction

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Semantic Investigation №001

---

# Purpose

This document reconstructs the complete lifecycle of Publication WITHOUT assuming repository correctness.

---

# Lifecycle States Found

## Current Canonical States (TJS-021)

1. Generated
2. Published
3. Updated
4. Archived
5. Removed

## Legacy States (TJS-002)

1. Generated
2. Scheduled
3. Published
4. Updated
5. Archived
6. Removed

**Note:** "Scheduled" state exists in legacy but not in current canonical model.

## Legacy Lifecycle (TJS-007)

```
Dataset → Render → Publish → Update (if required) → Retain or Remove
```

**Note:** Uses different terminology than current model.

## Legacy Lifecycle (TJS-008)

```
Generate Today's Package → Publish Today's Posts → Monitor Dataset → Update changed Posts → Generate Tomorrow Package → Publish Tomorrow Posts → Delete obsolete Tomorrow Posts
```

**Note:** Describes operational cycle, not state machine.

---

# Reconstructed Lifecycle

## Phase 1: Creation

**Trigger:** Normalized Dataset becomes available

**Actor:** Publication Engine (implements Publisher Role)

**Process:**

1. Parser retrieves Open Data from Data Source
2. Parser validates and normalizes data
3. Normalized Dataset is stored in Data Storage
4. Publication Engine receives Normalized Dataset
5. Publication Engine applies Canonical Templates
6. Publication Engine renders Publication using Rendering Rules
7. Publication enters Generated state

**Evidence:** TJS-010 §3.3, TJS-021 §4.1, Legacy TJS-007 §4

---

## Phase 2: Delivery

**Trigger:** Publication is generated

**Actor:** Telegram Publisher

**Process:**

1. Publication Engine packages Publications into Publication Package
2. Publication Package is sent to Telegram Publisher
3. Telegram Publisher delivers to Telegram Channel
4. Telegram assigns Telegram Message ID
5. Publication transitions from Generated to Published
6. Publication becomes visible to readers

**Evidence:** TJS-010 §3.3, TJS-021 §5.1, Legacy TJS-007 §4

---

## Phase 3: Update (Conditional)

**Trigger:** Normalized Dataset changes OR Rendering Rules change

**Actor:** Publication Engine

**Process:**

1. Publication Engine detects dataset change
2. Publication Engine re-renders affected Publications
3. Canonical Equality check performed
4. If different: Telegram Publisher edits existing Telegram message
5. Publication transitions from Published to Updated
6. Publication transitions from Updated back to Published

**Constraints:**

- Updates SHOULD modify in place (TJS-021 §7.1)
- Replacing is last resort (TJS-021 §7.2)
- Original meaning preserved (TJS-021 §6.2)

**Evidence:** TJS-021 §5.2, §5.3, §6.2, Legacy TJS-007 §5, §6

---

## Phase 4: Archival

**Trigger:** Reporting period ends

**Actor:** Publication Engine (automated)

**Process:**

1. Reporting period ends (next day approximately 05:00)
2. All current-day Publications are archived
3. Publications remain in Telegram Journal permanently
4. Publications transition from Published to Archived
5. Archived Publications SHALL NOT be deleted

**Exception:** Temporary Publications (Tomorrow) are removed, not archived.

**Evidence:** TJS-021 §5.4, §6.3, Legacy TJS-007 §9

---

## Phase 5: Removal (Conditional)

**Trigger:** Publication is temporary AND no longer relevant

**Actor:** Publication Engine (automated)

**Process:**

1. Only Tomorrow Publications are temporary
2. Next day approximately 05:00
3. Obsolete Tomorrow Publications are deleted
4. Publications transition from Published to Removed
5. Removed Publications are no longer visible

**Constraints:**

- Only temporary Publications MAY be removed (TJS-021 §5.5)
- Permanent Publications SHALL NOT be removed (TJS-021 §5.6)
- Manual Publications SHALL NOT be removed (Legacy TJS-007 §11)

**Evidence:** TJS-021 §5.5, §5.6, §6.4, Legacy TJS-007 §8, TJS-008 §12

---

# Lifecycle Diagram

```
                    ┌─────────────────┐
                    │   Normalized    │
                    │    Dataset      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Generated     │
                    │   (Repository   │
                    │    only)        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
            ┌──────│    Published    │──────┐
            │      │   (Visible on   │      │
            │      │    Telegram)    │      │
            │      └────────┬────────┘      │
            │               │               │
            │               ▼               │
            │      ┌─────────────────┐      │
            │      │    Updated      │      │
            │      │  (Modified in   │      │
            │      │    place)       │      │
            │      └────────┬────────┘      │
            │               │               │
            │               ▼               │
            │      ┌─────────────────┐      │
            └─────►│    Published    │◄─────┘
                   │   (Back to      │
                   │    Published)   │
                   └────────┬────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
     ┌─────────────────┐        ┌─────────────────┐
     │    Archived     │        │    Removed      │
     │  (Permanent     │        │  (Temporary     │
     │   record)       │        │   only)         │
     └─────────────────┘        └─────────────────┘
```

---

# Lifecycle Anomalies

## Anomaly L-001: Missing "Scheduled" State

Legacy TJS-002 defines "Scheduled" as a state. Current TJS-021 does not include it.

**Impact:** Unclear whether Publications can be "scheduled" before generation.

---

## Anomaly L-002: Updated → Published Transition

TJS-021 §5.3 defines Updated → Published as a transition. This means Updated is a temporary state that always returns to Published.

**Question:** Is Updated a real state or just a transient marker?

---

## Anomaly L-003: Archival vs Removal Timing

Archival occurs when "reporting period ends." Removal occurs when "Publication is no longer relevant."

**Question:** Are these the same trigger or different triggers?

---

## Anomaly L-004: Manual Publication Lifecycle

Manual Publications are explicitly excluded from automatic lifecycle management.

**Question:** Do Manual Publications have their own lifecycle? Who manages it?

---

## Anomaly L-005: Graphic Publication Lifecycle

TJS-022 defines Graphic Publications but does not specify their lifecycle.

**Question:** Do Graphic Publications follow the same lifecycle as Text Publications?

---

# End of Document
