# IDENTITY_TIMELINE

**Document ID:** CASE001C-TIMELINE

**Title:** Identity — Timeline Analysis

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity Investigation

---

# Purpose

This document follows one Publication from birth to archive, identifying identity at every transition.

---

# Publication Identity Timeline

## Phase 0: Pre-Creation

**State:** Publication does not exist.

**Identity:** None

**Evidence:** No Publication exists yet.

---

## Phase 1: Creation (Generated)

**Trigger:** Normalized Dataset becomes available for a Territory.

**Actor:** Publication Engine.

**Identity Before:** None

**Identity After:** Territory + Date + Template

**Changed?** YES — identity created.

**External identifiers added?** NO

**Internal identifiers added?** YES — Territory + Date + Template assigned.

**Historical identifiers added?** NO

**Evidence:** TJS-021 §6.1: "Publications are created automatically from normalized data. Every Publication SHALL represent exactly one Territory, use one Canonical Template"

---

## Phase 2: Delivery (Published)

**Trigger:** Publication is delivered to Telegram.

**Actor:** Telegram Publisher.

**Identity Before:** Territory + Date + Template

**Identity After:** Territory + Date + Template + Telegram Message ID

**Changed?** YES — external reference added.

**External identifiers added?** YES — Telegram Message ID assigned.

**Internal identifiers added?** NO

**Historical identifiers added?** NO

**Evidence:** TJS-021 §5.1: "A Generated Publication becomes Published when it is delivered to the Telegram channel"

---

## Phase 3: Active Life (Updated → Published)

**Trigger:** Normalized Dataset changes.

**Actor:** Publication Engine.

**Identity Before:** Territory + Date + Template + Telegram Message ID

**Identity After:** Territory + Date + Template + Telegram Message ID

**Changed?** NO — identity unchanged.

**External identifiers added?** NO

**Internal identifiers added?** NO

**Historical identifiers added?** NO

**Evidence:** TJS-021 §5.2: "A Published Publication becomes Updated when the normalized dataset changes"

---

## Phase 4: Archival (Archived)

**Trigger:** Reporting period ends.

**Actor:** Publication Engine (automated).

**Identity Before:** Territory + Date + Template + Telegram Message ID

**Identity After:** Territory + Date + Template + Telegram Message ID + Historical Record

**Changed?** YES — historical status added.

**External identifiers added?** NO

**Internal identifiers added?** NO

**Historical identifiers added?** YES — becomes historical record.

**Evidence:** TJS-021 §5.4: "A Published Publication becomes Archived when the reporting period ends"

---

## Phase 4b: Removal (Removed) — Temporary Publications Only

**Trigger:** Publication is temporary AND no longer relevant.

**Actor:** Publication Engine (automated).

**Identity Before:** Territory + Date + Template + Telegram Message ID

**Identity After:** Territory + Date + Template (Telegram Message ID released)

**Changed?** YES — external reference released.

**External identifiers added?** NO

**Internal identifiers added?** NO

**Historical identifiers added?** NO

**Evidence:** TJS-021 §5.5: "A Published Publication becomes Removed only if it is a temporary Publication"

---

# Identity Timeline Summary

| Phase | State | Identity | External Added | Internal Added | Historical Added |
|-------|-------|----------|----------------|----------------|------------------|
| 0 | Non-Existence | None | - | - | - |
| 1 | Generated | Territory + Date + Template | NO | YES | NO |
| 2 | Published | Territory + Date + Template + Telegram Message ID | YES | NO | NO |
| 3 | Updated | Territory + Date + Template + Telegram Message ID | NO | NO | NO |
| 4 | Archived | Territory + Date + Template + Telegram Message ID + Historical Record | NO | NO | YES |
| 4b | Removed | Territory + Date + Template | NO | NO | NO |

---

# Key Insight

**Identity (Territory + Date + Template) is created at birth and NEVER changes.**

**External references (Telegram Message ID) are added and released.**

**Historical status is added at archival but does not change identity.**

**Identity persists across all lifecycle states.**

---

# End of Identity Timeline
