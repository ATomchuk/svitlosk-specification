# Publisher Interfaces

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the interfaces of Publisher.

---

# Publisher Interfaces

## Interface 1: Create Publication

**Input:** Interpretation Result, Territory

**Output:** Publication

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 2: Update Publication

**Input:** Updated Interpretation Result, Publication ID

**Output:** Updated Publication

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 3: Replace Publication

**Input:** New Interpretation Result, Territory

**Output:** New Publication

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 4: Remove Publication

**Input:** Publication ID

**Output:** Void

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 5: Format Emergency Outages

**Input:** Emergency Outage Information

**Output:** Formatted Content

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 6: Format Planned Outages

**Input:** Planned Outage Information

**Output:** Formatted Content

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 7: Format Tomorrow Outages

**Input:** Tomorrow Outage Information

**Output:** Formatted Content

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 8: Format Technical Message

**Input:** Technical Message Content

**Output:** Formatted Content

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 9: Group by Territory

**Input:** Publications, Territory Structure

**Output:** Organized Publications

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 10: Identify Territory

**Input:** Address, Territory Structure

**Output:** Territory

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 11: Execute Expiry

**Input:** Expired Publications

**Output:** Publications Removed

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

## Interface 12: Execute Update

**Input:** Updated Publications

**Output:** Publications Updated

**Channel-Independent:** YES

**Evidence:** CASE-PUB-002, CASE-TG-CORE-001

---

# Interface Count

| Category | Count | Channel-Independent |
|----------|-------|---------------------|
| Publication | 4 | YES |
| Content | 4 | YES |
| Territorial | 2 | YES |
| Lifecycle | 2 | YES |
| **Total** | **12** | **YES** |

---

# Evidence

| Interface | Source |
|-----------|--------|
| All Interfaces | CASE-PUB-002, CASE-TG-CORE-001 |

---

**End of Interfaces**
