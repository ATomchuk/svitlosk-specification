# TELEGRAM_DIRECTORY_HISTORY_POLICY

**Document ID:** TJS-F1.2-R6

**Title:** Telegram Directory History Policy

**Document Class:** History Policy

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Define where governance records live: certificates, audits, validations, scorecards, reviews, compilation reports.

---

# 1. Document Types

| Document Type | Count | Recommended Location | Justification |
|--------------|-------|---------------------|---------------|
| Certificates | 10 | archive/ | Permanent governance records |
| Audit reports | 12 | archive/ | Permanent governance records |
| Validation reports | 15 | archive/ | Permanent governance records |
| Scorecards | 3 | archive/ | Permanent governance records |
| Review reports | 10 | archive/ | Permanent governance records |
| Compilation reports | 5 | archive/ | Permanent governance records |

---

# 2. Why archive/?

| Criterion | Assessment |
|-----------|-----------|
| These documents are permanent | YES |
| These documents are governance records | YES |
| These documents are NOT active specifications | YES |
| These documents are NOT working materials | YES |
| These documents are NOT legacy | YES |
| "archive/" is the standard term | YES |

---

# 3. Policy Statement

All governance records (certificates, audits, validations, scorecards, reviews, compilation reports) SHALL live in archive/. These documents are permanent governance records that document the architectural evolution of the Telegram subsystem.

---

# 4. What NOT to Put in archive/

| Document Type | Correct Location | Reason |
|--------------|-----------------|--------|
| Canonical specifications | specs/ | Active specifications |
| Foundation documents | foundation/ | Permanent platform knowledge |
| Working materials | working/ | Temporary materials |
| Legacy documents | legacy/ | Historical knowledge sources |

---

**End of History Policy**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
