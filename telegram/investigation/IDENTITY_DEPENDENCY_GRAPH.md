# IDENTITY_DEPENDENCY_GRAPH

**Document ID:** CASE001C-DEPENDENCIES

**Title:** Identity — Dependency Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity Investigation

---

# Purpose

This document determines whether any identity depends upon external factors.

---

# Identity Dependencies

## Publication Identity

**Identity:** Territory + Date + Template

**Dependencies:**

| Dependency | Depends On | Stable? | Evidence |
|------------|------------|---------|----------|
| Territory | Administrative boundaries | YES | TERRITORIAL_MODEL.md: "All project components SHALL derive territorial information exclusively from this model" |
| Date | Calendar system | YES | Calendar is stable |
| Template | Editorial design | YES | TJS-005: Canonical Templates are stable |

**Conclusion:** Publication identity depends on stable factors. Identity is STABLE.

---

## Telegram Message ID

**Identity:** Platform identifier

**Dependencies:**

| Dependency | Depends On | Stable? | Evidence |
|------------|------------|---------|----------|
| Telegram Message ID | Telegram platform | NO | Platform-specific |
| Telegram Message ID | Message delivery | NO | Assigned at delivery |
| Telegram Message ID | Message existence | NO | Released at deletion |

**Conclusion:** Telegram Message ID depends on unstable factors. Reference is UNSTABLE.

---

## Issue Identity

**Identity:** Calendar day

**Dependencies:**

| Dependency | Depends On | Stable? | Evidence |
|------------|------------|---------|----------|
| Issue | Calendar day | YES | Calendar is stable |
| Issue | Publication existence | NO | TJS-021 §8.1: "An Issue opens when the first Publication for a calendar day is generated" |

**Conclusion:** Issue identity depends on stable calendar but unstable Publication existence. Identity is PARTIALLY STABLE.

---

## Journal Identity

**Identity:** Continuous publication

**Dependencies:**

| Dependency | Depends On | Stable? | Evidence |
|------------|------------|---------|----------|
| Journal | Continuous publication | YES | Journal is permanent |
| Journal | Issue existence | YES | Issues accumulate |

**Conclusion:** Journal identity depends on stable factors. Identity is STABLE.

---

## Territory Identity

**Identity:** Administrative name

**Dependencies:**

| Dependency | Depends On | Stable? | Evidence |
|------------|------------|---------|----------|
| Territory | Administrative boundaries | YES | Boundaries are stable |
| Territory | Government decisions | NO | Boundaries can change |

**Conclusion:** Territory identity depends on mostly stable factors. Identity is MOSTLY STABLE.

---

## Address Identity

**Identity:** Official designation

**Dependencies:**

| Dependency | Depends On | Stable? | Evidence |
|------------|------------|---------|----------|
| Address | Official designation | YES | GLOSSARY.md §4: "Addresses SHALL be treated exactly as officially published" |
| Address | Government decisions | NO | Addresses can change |

**Conclusion:** Address identity depends on official designation. Identity is STABLE as long as designation exists.

---

# Identity Dependency Graph

```text
Publication Identity (Territory + Date + Template)
    │
    ├──→ Territory (Administrative boundaries) ──→ STABLE
    ├──→ Date (Calendar system) ──→ STABLE
    └──→ Template (Editorial design) ──→ STABLE

Telegram Message ID
    │
    ├──→ Telegram Platform ──→ UNSTABLE
    ├──→ Message Delivery ──→ UNSTABLE
    └──→ Message Existence ──→ UNSTABLE

Issue Identity (Calendar day)
    │
    ├──→ Calendar System ──→ STABLE
    └──→ Publication Existence ──→ UNSTABLE

Journal Identity (Continuous publication)
    │
    └──→ Continuous Publication ──→ STABLE

Territory Identity (Administrative name)
    │
    ├──→ Administrative Boundaries ──→ STABLE
    └──→ Government Decisions ──→ UNSTABLE

Address Identity (Official designation)
    │
    └──→ Official Designation ──→ STABLE
```

---

# Identity Stability Summary

| Identity | Stable? | Reason |
|----------|---------|--------|
| Publication | YES | Depends on stable factors (Territory, Date, Template) |
| Telegram Message ID | NO | Depends on unstable platform |
| Issue | PARTIALLY | Depends on stable calendar but unstable Publication |
| Journal | YES | Depends on stable continuous publication |
| Territory | MOSTLY | Depends on mostly stable boundaries |
| Address | YES | Depends on official designation |

---

# Key Insight

**Publication identity is STABLE because it depends only on stable factors.**

**Telegram Message ID is UNSTABLE because it depends on platform-specific factors.**

**This confirms that Telegram Message ID is an external reference, not intrinsic identity.**

---

# End of Identity Dependency Graph
