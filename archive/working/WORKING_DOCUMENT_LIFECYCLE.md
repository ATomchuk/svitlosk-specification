# WORKING_DOCUMENT_LIFECYCLE

**Document ID:** F-1.99-W2

**Title:** Working Document Lifecycle

**Document Class:** Document Lifecycle

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Define lifecycle for working documents.

---

# 1. Working Document States

| State | Description | Location |
|-------|-------------|----------|
| Draft | Document is being created | working/[subsystem]/ |
| Active | Document is being developed or supports active development | working/[subsystem]/ |
| Frozen | Document content is finalized but still in working/ | working/[subsystem]/ |
| Archived | Document is no longer part of active development | archive/[category]/ |
| Legacy | Document is historical knowledge | legacy/ |
| Removed | Document is no longer needed | DELETED (rare) |

---

# 2. State Transitions

```
Draft
  ↓ (content finalized)
Active
  ↓ (development complete)
Frozen
  ↓ (moved to archive)
Archived
  ↓ (historical only, rare)
Legacy
```

---

# 3. Transition Rules

| Transition | Trigger | Action |
|-----------|---------|--------|
| Draft → Active | Document begins active development | No action needed |
| Active → Frozen | Document content is finalized | Mark as frozen |
| Frozen → Archived | Document is no longer part of active development | Move to archive/ |
| Archived → Legacy | Document becomes purely historical | Move to legacy/ (rare) |
| Any → Removed | Document is no longer needed | Delete (very rare) |

---

# 4. Lifecycle Rules

| Rule | Statement |
|------|-----------|
| WL-001 | Every document in working/ SHALL be in exactly one state |
| WL-002 | Documents SHALL NOT skip states |
| WL-003 | Archived documents SHALL NOT return to working/ |
| WL-004 | Legacy documents SHALL NOT return to working/ |
| WL-005 | Removed documents SHALL NOT be restored without approval |

---

# 5. Lifecycle Summary

| State | Typical Duration | Documents |
|-------|-----------------|-----------|
| Draft | Days to weeks | New specifications |
| Active | Weeks to months | Active development |
| Frozen | Months | Finalized but not yet archived |
| Archived | Permanent | Completed governance records |
| Legacy | Permanent | Historical knowledge |
| Removed | Permanent | Deleted (rare) |

---

**End of Document Lifecycle**

**Designer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
