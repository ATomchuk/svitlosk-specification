# CASEPUB001_LIFECYCLE

**Document ID:** CASE-PUB-001-LC

**Title:** Journal Release Lifecycle Reconstruction

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document reconstructs the complete lifecycle of the Journal Release from first principles.

---

# 2. Evidence Collection

## 2.1 CHARTER.md Evidence

> "SvitloSk continuously analyses officially published open data, transforms it into understandable information and delivers it promptly to the residents."

> "Every day the service analyses officially published information, transforms it into understandable messages, archives the processed information and ensures its timely distribution through supported communication channels."

**Extraction:** The lifecycle involves: analysis → transformation → distribution → archival.

## 2.2 GLOSSARY.md Evidence

> "Processing Cycle: One complete execution of the information pipeline. A Processing Cycle includes: 1. Data Retrieval, 2. Parsing, 3. Data Validation, 4. Interpretation, 5. Publication generation, 6. Publication distribution."

> "Publication Lifecycle: The complete lifecycle of a Publication. The lifecycle consists of: 1. Interpretation Result, 2. Rendering, 3. Publication generation, 4. Distribution, 5. Archival, 6. Expiration (where applicable)."

**Extraction:** The Glossary defines a Processing Cycle and Publication Lifecycle, but these are for individual Publications, not Journal Releases.

## 2.3 DATA_MODEL.md Evidence

> "Data Lifecycle: Collected → Validated → Normalized → Interpreted → Published → Archived."

**Extraction:** The Data Model defines a data lifecycle, but this is for operational data, not the Journal Release.

## 2.4 TELEGRAM_PUBLICATION_LIFECYCLE.md Evidence

> "Publications pass through the following states: Generated, Published, Updated, Archived, Removed."

> "An Issue opens when the first Publication for a calendar day is generated. The Issue represents one editorial edition of the Journal for that day."

> "An Issue closes when: All Publications for the day have been archived, No further updates are expected, The next day's Issue opens."

**Extraction:** The Telegram lifecycle defines states for Publications and an Issue lifecycle (opening/closing).

## 2.5 TELEGRAM_PUBLISHING_CANONICAL_MODEL.md Evidence

> "External Data Sources → Parser → Normalized Dataset → Publication Engine → Publication Package → Telegram Publisher → Telegram Channel → Subscribers."

**Extraction:** The publishing data flow is: Data Source → Parser → Normalized Data → Publication Engine → Publication Package → Channel → Subscribers.

---

# 3. Analysis

## 3.1 Current Lifecycle Models

The project has THREE lifecycle models:

| Model | Scope | Source |
|-------|-------|--------|
| Data Lifecycle | Operational data | DATA_MODEL.md |
| Processing Cycle | Information pipeline | GLOSSARY.md |
| Publication Lifecycle | Individual Publications | GLOSSARY.md |
| Telegram Lifecycle | Telegram Publications | TELEGRAM_PUBLICATION_LIFECYCLE.md |

## 3.2 The Gap

NONE of these models describe the lifecycle of the JOURNAL RELEASE.

- Data Lifecycle: raw data → archived data
- Processing Cycle: data retrieval → publication distribution
- Publication Lifecycle: interpretation → archival
- Telegram Lifecycle: generated → archived/removed

The Journal Release lifecycle is ABSENT.

## 3.3 Why This Matters

The Journal Release is the PRIMARY OBJECT. Its lifecycle must be explicitly defined.

Without a Journal Release lifecycle, the system lacks:
- Clear definition of when a Journal Release begins
- Clear definition of when a Journal Release ends
- Clear definition of Journal Release states
- Clear definition of Journal Release transitions

---

# 4. Journal Release Lifecycle Reconstruction

## 4.1 Lifecycle Chain

```
Reality (Official Open Data)
    ↓
Data Acquisition (Parser)
    ↓
Normalization (Parsing Engine)
    ↓
Interpretation (Interpretation Engine)
    ↓
Journal Release Assembly (Publication Engine)
    ↓
Channel Distribution (Telegram/Facebook/PWA)
    ↓
Recipient (Resident)
```

## 4.2 Detailed Lifecycle States

### State 1: INACTIVE

No Journal Release exists for the current Reporting Period.

The system is waiting for official data to trigger Journal Release creation.

**Transition to:** CREATING (when official data is received)

### State 2: CREATING

Journal Release is being assembled from interpreted data.

Publications are being generated for each Territory.

**Transition to:** ACTIVE (when first Publication is distributed)

### State 3: ACTIVE

Journal Release is live and visible to residents.

Publications may be updated as new data arrives.

The Journal Release is being maintained throughout the Reporting Period.

**Transition to:** FINALIZING (when no more updates are expected)

### State 4: FINALIZING

Journal Release is being finalized.

Temporary Publications (tomorrow information) are being marked for removal.

**Transition to:** ARCHIVED (when Reporting Period ends)

### State 5: ARCHIVED

Journal Release is preserved as part of the historical record.

All Publications are frozen.

The Journal Release is permanently available.

**Terminal state.**

## 4.3 Lifecycle Transitions

| From | To | Trigger |
|------|----|---------|
| INACTIVE | CREATING | Official data received |
| CREATING | ACTIVE | First Publication distributed |
| ACTIVE | ACTIVE | Data update received |
| ACTIVE | FINALIZING | No more updates expected |
| FINALIZING | ARCHIVED | Reporting Period ends |

---

# 5. Journal Release vs Publication Lifecycle

## 5.1 Scope Comparison

| Aspect | Journal Release Lifecycle | Publication Lifecycle |
|--------|--------------------------|----------------------|
| Scope | Complete daily edition | Single message |
| States | INACTIVE → CREATING → ACTIVE → FINALIZING → ARCHIVED | Generated → Published → Updated → Archived/Removed |
| Identity | Reporting Period + Territory Set | Territory + Content |
| Duration | One Reporting Period | Until Archived/Removed |

## 5.2 Relationship

The Journal Release lifecycle CONTAINS multiple Publication lifecycles.

Each Publication within a Journal Release follows its own lifecycle (Generated → Published → Updated → Archived/Removed).

The Journal Release lifecycle governs the OVERALL lifecycle of the daily edition.

## 5.3 Independence

The Journal Release lifecycle is INDEPENDENT of any specific channel.

The Publication lifecycle may be CHANNEL-SPECIFIC (e.g., Telegram Publications have different constraints than Facebook Posts).

---

# 6. Channel Distribution Analysis

## 6.1 The Distribution Question

Does the Journal Release go to channels, or do Publications go to channels?

## 6.2 Evidence

From TELEGRAM_PUBLISHING_CANONICAL_MODEL.md:
> "Publication Engine → Telegram Publisher → Telegram Channel → Subscribers."

From TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md:
> "The Journal serves as a chronological public archive of information processed by the SvitloSk system."

## 6.3 Analysis

The current model sends PUBLICATIONS to channels.

But the JOURNAL RELEASE is what residents consume.

The Journal Release is ASSEMBLED, then DISTRIBUTED to channels.

Each channel receives a REPRESENTATION of the Journal Release, not the Journal Release itself.

## 6.4 Finding

**The Journal Release is channel-independent.**

**Channels receive REPRESENTATIONS of the Journal Release.**

**The Journal Release exists independently of any channel.**

---

# 7. Cross-Examination

## 7.1 Model A: Channel-Specific Lifecycle

**Claim:** Each channel has its own Journal Release lifecycle.

**Attack:**
- This duplicates logic across channels
- This violates DRY principle
- This makes maintenance difficult
- This contradicts CHARTER.md: "SvitloSk is not defined by a particular technology, platform or communication channel"

**Verdict:** REJECTED.

## 7.2 Model B: Unified Lifecycle with Channel Distribution

**Claim:** One Journal Release lifecycle, with channel-specific distribution.

**Attack:**
- This is consistent with CHARTER.md
- This separates concerns (lifecycle vs distribution)
- This allows multiple channels without duplicating lifecycle logic

**Verdict:** ACCEPTED.

---

# 8. Findings

## 8.1 Finding LC-001

**The Journal Release lifecycle is: INACTIVE → CREATING → ACTIVE → FINALIZING → ARCHIVED.**

This lifecycle is INDEPENDENT of any specific channel.

**Evidence:** CHARTER.md, GLOSSARY.md, TELEGRAM_PUBLICATION_LIFECYCLE.md (adapted).

**Confidence:** HIGH.

## 8.2 Finding LC-002

**The Journal Release lifecycle CONTAINS multiple Publication lifecycles.**

Each Publication follows its own lifecycle within the Journal Release.

**Evidence:** GLOSSARY.md (Publication Lifecycle), TELEGRAM_PUBLICATION_LIFECYCLE.md.

**Confidence:** HIGH.

## 8.3 Finding LC-003

**Channels receive REPRESENTATIONS of the Journal Release, not the Journal Release itself.**

The Journal Release is channel-independent.

**Evidence:** CHARTER.md ("not defined by a particular technology"), TELEGRAM_PUBLISHING_CANONICAL_MODEL.md (data flow).

**Confidence:** HIGH.

## 8.4 Finding LC-004

**The current project lacks an explicit Journal Release lifecycle.**

This is a gap in the architectural documentation.

**Evidence:** Analysis of DATA_MODEL.md, GLOSSARY.md, TELEGRAM_PUBLICATION_LIFECYCLE.md.

**Confidence:** HIGH.

---

# 9. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| LC-001 | CHARTER.md §6, GLOSSARY.md §2, TELEGRAM_PUBLICATION_LIFECYCLE.md §4 |
| LC-002 | GLOSSARY.md §3 (Publication Lifecycle), TELEGRAM_PUBLICATION_LIFECYCLE.md §4 |
| LC-003 | CHARTER.md §1 ("not defined by technology"), TELEGRAM_PUBLISHING_CANONICAL_MODEL.md §3.3 |
| LC-004 | Analysis of DATA_MODEL.md, GLOSSARY.md, TELEGRAM_PUBLICATION_LIFECYCLE.md |

---

**End of Lifecycle Reconstruction**
