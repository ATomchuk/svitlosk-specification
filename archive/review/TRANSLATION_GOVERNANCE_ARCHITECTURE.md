# TRANSLATION_GOVERNANCE_ARCHITECTURE

**Document ID:** RA-004

**Title:** Translation Governance Architecture

**Document Class:** Architecture Review

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Should Translation Governance Remain in Root?

**NO.**

Translation governance is a specialized subset of repository governance. It serves a specific function (translation) and a specific audience (translators). It does not define the project identity or serve as navigation.

---

# 2. Root Impact of 6 Translation Documents

If 6 translation documents remain in Root:
- Root grows from 13 to 20 files
- Root becomes cluttered with specialized governance
- Future subsystems (PWA, Power Outage Engine) would expect similar treatment
- Root would grow indefinitely as new governance areas emerge

---

# 3. Alternative Locations

| Location | Advantages | Disadvantages |
|----------|-----------|---------------|
| governance/translation/ | Clean separation, organized by type | One more directory level |
| translation/ | Maximum separation | Loses governance context |
| governance/language/ | Generic language area | "Translation" is more precise |

---

# 4. Recommended Location

**governance/translation/**

Rationale:
- Translation governance is governance — it belongs under governance/
- "translation/" is more precise than "language/"
- This pattern can be replicated for future governance areas (e.g., governance/accessibility/)
- Root stays at 13 files regardless of how many governance areas grow

---

# 5. Verdict

All 6 translation governance documents SHALL be moved to governance/translation/.

---

**End of Translation Governance Architecture**

**Reviewer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
