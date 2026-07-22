# ISSUE_LIFECYCLE

**Document ID:** CASE002A-LIFECYCLE

**Title:** Issue — Lifecycle

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Investigation

---

# Purpose

This document reconstructs the complete lifecycle of Issue.

---

# Issue Lifecycle

## Phase 0: Non-Existence

**State:** Issue does not exist.

**What exists:**

- Journal exists (continuous publication)
- Calendar day exists
- No Publications yet

**Evidence:** TJS-000 §4, TJS-021 §8.1

---

## Phase 1: Opening

**Trigger:** First Publication for a calendar day is generated.

**Actor:** Publication Engine.

**Process:**

1. Publication Engine generates first Publication for a calendar day
2. Issue is created (opened)
3. Issue represents one editorial edition for that day

**What changes:**

- Issue comes into existence
- Issue has Identity (Calendar day)
- Issue has temporal scope (one day)

**Evidence:** TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated"

---

## Phase 2: Maintenance

**Trigger:** Publication Engine continues generating/updating Publications.

**Actor:** Publication Engine.

**Process:**

1. Publication creation for new territories
2. Publication updates when data changes
3. Publication replacement when necessary
4. Publication removal for temporary publications

**What changes:**

- Issue accumulates Publications
- Issue content changes (Publications added/updated/removed)
- Issue state remains "Maintained"

**Evidence:** TJS-021 §8.2: "An Issue is maintained through: Publication creation, updates, replacement, removal"

---

## Phase 3: Closing

**Trigger:** All Publications for the day have been archived, no further updates expected, next day's Issue opens.

**Actor:** Publication Engine (automated).

**Process:**

1. All Publications for the day are archived
2. No further updates are expected
3. Next day's Issue opens
4. Current Issue closes

**What changes:**

- Issue state changes to "Closed"
- Issue becomes historical record
- Issue is preserved permanently

**Evidence:** TJS-021 §8.3: "An Issue closes when: All Publications for the day have been archived, no further updates are expected, the next day's Issue opens"

---

## Phase 4: Historical

**State:** Issue exists permanently as historical record.

**What exists:**

- Preserved Issue with all Publications
- Available for public accountability
- Available for historical reference

**Evidence:** TJS-021 §8.3: "The Issue remains available as part of the historical record after closing"

---

# Lifecycle Diagram

```text
                    ┌─────────────────┐
                    │   Non-Existence  │
                    │  (Phase 0)       │
                    └────────┬────────┘
                             │
                             │ Trigger: First Publication generated
                             │ Actor: Publication Engine
                             ▼
                    ┌─────────────────┐
                    │     Open        │
                    │  (Phase 1)       │
                    │  Created        │
                    └────────┬────────┘
                             │
                             │ Activity: Publication creation, updates
                             │ Actor: Publication Engine
                             ▼
                    ┌─────────────────┐
                    │   Maintained    │
                    │  (Phase 2)       │
                    │  Publications   │
                    │  accumulated    │
                    └────────┬────────┘
                             │
                             │ Trigger: All archived, no updates expected
                             │ Actor: Publication Engine
                             ▼
                    ┌─────────────────┐
                    │    Closed       │
                    │  (Phase 3)       │
                    │  Historical     │
                    │  record         │
                    └────────┬────────┘
                             │
                             │ State: Permanent
                             ▼
                    ┌─────────────────┐
                    │   Historical    │
                    │  (Phase 4)       │
                    │  Preserved      │
                    │  permanently    │
                    └─────────────────┘
```

---

# Lifecycle States Summary

| State | Description | Duration | Reversible? |
|-------|-------------|----------|-------------|
| Non-Existence | Issue does not exist | Until first Publication | N/A |
| Open | Issue created | Momentary | NO |
| Maintained | Publications accumulated | Until closing | NO |
| Closed | Historical record created | Momentary | NO |
| Historical | Preserved permanently | Permanent | NO |

---

# Key Insight

**Issue lifecycle is triggered by Publication lifecycle.**

**Issue opens when first Publication is generated.**

**Issue closes when all Publications are archived.**

**Issue becomes historical after closing.**

**Issue lifecycle is DERIVED from Publication lifecycle.**

---

# End of Issue Lifecycle
