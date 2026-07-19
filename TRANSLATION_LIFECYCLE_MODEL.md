# TRANSLATION_LIFECYCLE_MODEL

**Document ID:** TJS-L2-S5

**Title:** Translation Lifecycle Model

**Document Class:** Lifecycle Model

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Design the lifecycle for translated documents.

---

# 1. Translation Lifecycle

`
English Stable
    ↓
Translation Draft
    ↓
Translation Review
    ↓
Translation Stable
    ↓
Translation Updated
    ↓
Translation Archived
`

---

# 2. Translation Lifecycle States

| State | Description |
|-------|-------------|
| English Stable | English source document is Stable |
| Translation Draft | Ukrainian translation is being created |
| Translation Review | Ukrainian translation is being reviewed |
| Translation Stable | Ukrainian translation is approved and published |
| Translation Updated | Ukrainian translation is updated due to English changes |
| Translation Archived | Ukrainian translation is archived |

---

# 3. Translation Lifecycle Transitions

| Transition | Trigger | Action |
|-----------|---------|--------|
| English Stable → Translation Draft | English source reaches Stable | Begin translation |
| Translation Draft → Translation Review | Draft complete | Begin review |
| Translation Review → Translation Stable | Review approved | Publish translation |
| Translation Stable → Translation Updated | English source updated | Update translation |
| Translation Updated → Translation Stable | Update reviewed | Publish updated translation |
| Translation Stable → Translation Archived | English source archived | Archive translation |

---

# 4. English Modification Propagation

| English Change | Ukrainian Action | Timeline |
|---------------|-----------------|----------|
| Minor wording change | Update translation | Within 1 week |
| Section restructure | Update translation | Within 2 weeks |
| New section added | Translate new section | Within 2 weeks |
| Section removed | Archive translation section | Within 1 week |
| Terminology change | Update glossary translation first, then all specs | Within 1 week |

---

# 5. Translation Lifecycle Summary

| Metric | Value |
|--------|-------|
| States | 6 |
| Transitions | 5 |
| Propagation rules | 4 |
| Independence from PROC-001 | YES — separate lifecycle |

---

**End of Translation Lifecycle Model**

**Modeler:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
