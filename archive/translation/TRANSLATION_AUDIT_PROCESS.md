# TRANSLATION_AUDIT_PROCESS

**Document_ID:** TJS-L3.1-F3

**Title:** Translation Audit Process

**Document Class:** Audit Process

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Define the mandatory Translation Audit process.

---

# 1. Translation Audit Process

`
English specification changes
    ↓
Translation Audit
    ↓
If identical
    → Official Translation remains
    Else
    → Translation Requires Synchronization
        ↓
    Translation Update
        ↓
    Translation Review
        ↓
    Official Translation
`

---

# 2. Translation Audit Steps

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | English specification is updated | English author |
| 2 | Translation Audit triggered | Maintainer |
| 3 | Compare English against Ukrainian | Reviewer |
| 4 | If identical, status remains Official Translation | Reviewer |
| 5 | If different, status changes to Translation Requires Synchronization | Reviewer |
| 6 | Translator updates Ukrainian translation | Translator |
| 7 | Reviewer reviews updated translation | Reviewer |
| 8 | After approval, status becomes Official Translation | Maintainer |

---

# 3. Translation Audit Rules

| Rule | Statement |
|------|-----------|
| TA-001 | Translation Audit SHALL be triggered after every English source update |
| TA-002 | Translation Audit SHALL compare English against Ukrainian |
| TA-003 | If identical, Official Translation status is preserved |
| TA-004 | If different, Translation Requires Synchronization status is set |
| TA-005 | Translation Update SHALL be completed within 2 weeks |
| TA-006 | Translation Review SHALL be completed within 1 week |
| TA-007 | After approval, status becomes Official Translation |

---

# 4. Translation Audit Process Summary

| Metric | Value |
|--------|-------|
| Steps | 8 |
| Rules | 7 |
| Responsible roles | 3 (Maintainer, Reviewer, Translator) |

---

**End of Translation Audit Process**

**Definer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
