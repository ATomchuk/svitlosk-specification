# IDENTIFIER_MATRIX

**Document ID:** CASE001D-IDENTIFIER-MATRIX

**Title:** Identifier — Complete Matrix

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity vs Identifier Investigation

---

# Purpose

This document provides a complete inventory of every Identifier in the repository.

---

# Identifier Matrix

| # | Identifier | Owner | Immutable? | Platform-Dependent? | Represents Identity? |
|---|------------|-------|------------|---------------------|---------------------|
| 1 | Telegram Message ID | Telegram platform | YES | YES | NO — references Publication |
| 2 | Document ID (DOC-XXX) | Repository governance | YES | NO | NO — references document |
| 3 | ADR ID (ADR-XXX) | Repository governance | YES | NO | NO — references ADR |
| 4 | TJS ID (TJS-XXX) | Repository governance | YES | NO | NO — references TJS document |
| 5 | SSP ID (SSP-XXX) | Repository governance | YES | NO | NO — references SSP document |
| 6 | Session ID | Publication Engine | YES | NO | NO — references session |
| 7 | Database ID (implied) | Data Storage | YES | NO | NO — references database record |
| 8 | Queue identifier | DSO | YES | NO | NO — references queue |
| 9 | Subqueue identifier | DSO | YES | NO | NO — references subqueue |
| 10 | Address (official) | Government | YES | NO | NO — references location |

---

# Identifier Characteristics

## Technical Identifiers

| Identifier | Purpose | Lifecycle | Stability |
|------------|---------|-----------|-----------|
| Telegram Message ID | Reference Telegram message | Created at delivery, released at deletion | UNSTABLE |
| Database ID (implied) | Reference database record | Created at storage, released at deletion | STABLE |
| Session ID | Reference execution session | Created at start, released at end | TEMPORARY |

## Governance Identifiers

| Identifier | Purpose | Lifecycle | Stability |
|------------|---------|-----------|-----------|
| Document ID (DOC-XXX) | Reference normative document | Created at registration, permanent | STABLE |
| ADR ID (ADR-XXX) | Reference architecture decision | Created at creation, permanent | STABLE |
| TJS ID (TJS-XXX) | Reference TJS specification | Created at registration, permanent | STABLE |
| SSP ID (SSP-XXX) | Reference SSP specification | Created at registration, permanent | STABLE |

## Domain Identifiers

| Identifier | Purpose | Lifecycle | Stability |
|------------|---------|-----------|-----------|
| Queue identifier | Reference electricity queue | Official designation, permanent | STABLE |
| Subqueue identifier | Reference electricity subqueue | Official designation, permanent | STABLE |
| Address (official) | Reference geographical location | Official designation, permanent | STABLE |

---

# Identifier vs Identity

| Identifier | Represents Identity? | Reason |
|------------|---------------------|--------|
| Telegram Message ID | NO | References Publication, does not define it |
| Document ID | NO | References document, does not define it |
| ADR ID | NO | References ADR, does not define it |
| TJS ID | NO | References TJS document, does not define it |
| SSP ID | NO | References SSP document, does not define it |
| Session ID | NO | References session, does not define it |
| Database ID | NO | References database record, does not define it |
| Queue identifier | NO | References queue, does not define it |
| Subqueue identifier | NO | References subqueue, does not define it |
| Address (official) | NO | References location, does not define it |

---

# Key Insight

**All Identifiers are REFERENCES, not Identity.**

**No Identifier defines what an object IS.**

**All Identifiers point to objects that have their own Identity.**

---

# End of Identifier Matrix
