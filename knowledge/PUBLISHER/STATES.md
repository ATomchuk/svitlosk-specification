# Publisher States

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the states of Publisher and its products.

---

# Publication States

## Generated

**Definition:** Publication has been created from normalized data but not yet published.

**Characteristics:**
- Exists in Repository
- Not yet visible to readers
- Ready for distribution

**Evidence:** TELEGRAM_LIFECYCLE.md §4.1

---

## Published

**Definition:** Publication is live and visible to readers.

**Characteristics:**
- Delivered to channel
- Visible to residents
- Can be updated

**Evidence:** TELEGRAM_LIFECYCLE.md §4.2

---

## Updated

**Definition:** Publication has been modified.

**Characteristics:**
- Modified in place
- Original meaning preserved
- Returns to Published state

**Evidence:** TELEGRAM_LIFECYCLE.md §4.3

---

## Archived

**Definition:** Publication is preserved as historical record.

**Characteristics:**
- Permanent preservation
- Immutable
- Traceable to source

**Evidence:** TELEGRAM_LIFECYCLE.md §4.4

---

## Removed

**Definition:** Publication has been deleted from channel.

**Characteristics:**
- Only temporary Publications can be removed
- Not visible to readers
- Terminal state

**Evidence:** TELEGRAM_LIFECYCLE.md §4.5

---

# Journal Release States

## INACTIVE

**Definition:** No Journal Release exists for current Reporting Period.

**Characteristics:**
- Waiting for data
- No Publications

**Evidence:** CASE-INF-001

---

## CREATING

**Definition:** Journal Release is being assembled.

**Characteristics:**
- Publications being generated
- Not yet visible

**Evidence:** CASE-INF-001

---

## ACTIVE

**Definition:** Journal Release is live and visible.

**Characteristics:**
- Publications distributed
- Can be updated
- Visible to residents

**Evidence:** CASE-INF-001

---

## FINALIZING

**Definition:** Journal Release is being finalized.

**Characteristics:**
- Temporary Publications being removed
- Preparing for archival

**Evidence:** CASE-INF-001

---

## ARCHIVED

**Definition:** Journal Release is preserved permanently.

**Characteristics:**
- Immutable
- Historical record
- Terminal state

**Evidence:** CASE-INF-001

---

# State Summary

| Entity | States | Count |
|--------|--------|-------|
| Publication | Generated, Published, Updated, Archived, Removed | 5 |
| Journal Release | INACTIVE, CREATING, ACTIVE, FINALIZING, ARCHIVED | 5 |

---

# Evidence

| State | Source |
|-------|--------|
| Publication States | TELEGRAM_LIFECYCLE.md §4 |
| Journal Release States | CASE-INF-001 |

---

**End of States**
