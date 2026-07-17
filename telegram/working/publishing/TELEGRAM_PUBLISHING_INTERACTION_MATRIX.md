# Telegram Publishing Interaction Matrix

**Date:** 2026-07-13
**Scope:** Approved interactions between components
**Status:** HARVEST COMPLETE

---

| Caller | Callee | Transferred Object | Allowed | Reason |
|--------|--------|-------------------|---------|--------|
| Parser | Publication Engine | Normalized Dataset | YES | Parser produces data for Publication Engine (TG §6) |
| Parser | Data Storage | Normalized Dataset | YES | Parser stores normalized data (SSP-002) |
| Publication Engine | Telegram Publisher | Publication Package | YES | Publication Engine produces packages for Telegram delivery |
| Publication Engine | Data Storage | Publication | YES | Publication Engine stores generated publications (SSP-003) |
| Publication Engine | Schedule Generator | Schedule Request | YES | Publication Engine requests schedules (SSP-006) |
| Publication Engine | Graphic Generator | Graphic Request | YES | Publication Engine requests graphics (SSP-007) |
| Telegram Publisher | Telegram Channel | Publication | YES | Telegram Publisher delivers publications to channel |
| Telegram Channel | Subscribers | Publication | YES | Channel delivers publications to readers |
| Administrators | Telegram Channel | Manual Publication | YES | Administrators can create manual publications |
| Administrators | Telegram Channel | Image Publication | YES | Administrators can create image publications |
| Publication Engine | Telegram Channel | Publication (owned) | YES | Engine manages its own publications |
| Publication Engine | Telegram Channel | Manual Publication | NO | Engine SHALL NOT modify manual publications |
| Publication Engine | Telegram Channel | Image Publication | NO | Engine SHALL NOT modify image publications |
| Parser | Publication Engine | Interpretation | NO | Parser SHALL NOT reinterpret data |
| Publication Engine | Parser | — | NO | Engine SHALL NOT retrieve data |
| Publication Engine | Telegram Channel | Other publisher's Publication | NO | Engine SHALL NOT modify others' publications |
| Subscribers | Telegram Channel | Read | YES | Subscribers read publications |
| Administrators | Telegram Channel | Configuration | YES | Administrators configure channel |

---

# Illegal Interactions

| Interaction | Status | Reason |
|-------------|--------|--------|
| Parser → Publication Engine (reinterpretation) | ILLEGAL | Parser SHALL NOT interpret data (GL §3) |
| Publication Engine → Parser | ILLEGAL | Engine SHALL NOT retrieve data (GL §3) |
| Publication Engine → Manual Publications | ILLEGAL | Engine SHALL NOT modify manual publications (TJS-008 §13) |
| Publication Engine → Image Publications | ILLEGAL | Engine SHALL NOT modify image publications (TJS-008 §14) |
| Publication Engine → Other publisher's Publications | ILLEGAL | Engine SHALL NOT modify others' publications (TJS-007 §11) |
| Subscribers → Telegram Channel (write) | ILLEGAL | Subscribers read only |
| Any component → Glossary (modify) | ILLEGAL | Glossary is read-only semantic authority |

---

# Interaction Summary

| Category | Count |
|----------|-------|
| Approved interactions | 11 |
| Illegal interactions | 7 |
| Total interactions analyzed | 18 |

---

**End of Interaction Matrix**

**Harvester:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
