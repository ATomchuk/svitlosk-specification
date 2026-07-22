# LC001_RESEARCH2_OPERATIONS

**Document ID:** CASE-LC-001-R2

**Title:** Lifecycle Operations

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every lifecycle operation and determines whether it is intrinsic to Lifecycle or belongs elsewhere.

---

# 2. Lifecycle Operations

## 2.1 Create

### Definition

New information enters the system.

### Intrinsic to Lifecycle?

**YES.**

Create is the ENTRY POINT of the lifecycle.

Without Create, no information exists in the system.

### Evidence

> "Data Retrieval: The process of obtaining Open Data from an approved Data Source." (GLOSSARY §2)

### Owner

Parser (acquires information from DSO).

---

## 2.2 Update

### Definition

Existing information is modified with new data.

### Intrinsic to Lifecycle?

**YES.**

Update is a CORE OPERATION of the lifecycle.

Information changes over time and must be updated.

### Evidence

> Parser updates today.txt every two hours (Architect Intent scenario).

### Owner

Parser (acquires new data), Lifecycle (determines update needed), Publisher (propagates update).

---

## 2.3 Replace

### Definition

Existing information is entirely replaced with new information.

### Intrinsic to Lifecycle?

**YES.**

Replace is a VARIATION of Update where the entire content changes.

### Evidence

> "Tomorrow Publications SHALL be automatically replaced by current publications." (GLOSSARY §3)

### Owner

Lifecycle (determines replacement needed), Publisher (executes replacement).

---

## 2.4 Merge

### Definition

Multiple pieces of information are combined into one.

### Intrinsic to Lifecycle?

**YES.**

Merge is a COMPOSITION OPERATION.

Multiple data points may need to be merged into a single information object.

### Evidence

> Queue Timetable = multiple Schedules merged.

### Owner

Lifecycle (determines merge needed), Parser (performs merge).

---

## 2.5 Republish

### Definition

Existing information is distributed again without content change.

### Intrinsic to Lifecycle?

**NO.**

Republish is a DISTRIBUTION operation, not a lifecycle operation.

It belongs to the Publishing domain.

### Evidence

> "Distribution: The process of delivering Publications to one or more Publication Channels." (GLOSSARY §3)

### Owner

Publisher (executes distribution).

---

## 2.6 Expire

### Definition

Information ceases to be valid and is removed from active view.

### Intrinsic to Lifecycle?

**YES.**

Expire is a TEMPORAL OPERATION.

Information has a validity period and must expire when that period ends.

### Evidence

> "Tomorrow Publications SHALL expire after the reporting period ends." (GLOSSARY §3)

### Owner

Lifecycle (determines expiry), Publisher (removes expired information).

---

## 2.7 Archive

### Definition

Information is preserved as historical record.

### Intrinsic to Lifecycle?

**YES.**

Archive is the TERMINAL OPERATION of the lifecycle.

Information moves from active to historical.

### Evidence

> "Historical Archive: The persistent storage of historical Interpretation Results and Publications." (GLOSSARY §2)

### Owner

Lifecycle (determines archival), Storage (executes archival).

---

## 2.8 Hide

### Definition

Information is removed from view but not deleted.

### Intrinsic to Lifecycle?

**MAYBE.**

Hide is a PRESENTATION operation, not a core lifecycle operation.

It may belong to the Publishing domain.

### Evidence

> No direct evidence in canonical documents.

### Owner

Publisher (executes hiding).

---

## 2.9 Reveal

### Definition

Hidden information is made visible again.

### Intrinsic to Lifecycle?

**MAYBE.**

Reveal is a PRESENTATION operation, not a core lifecycle operation.

It may belong to the Publishing domain.

### Evidence

> No direct evidence in canonical documents.

### Owner

Publisher (executes revealing).

---

## 2.10 Delete

### Definition

Information is permanently removed from the system.

### Intrinsic to Lifecycle?

**NO.**

SvitloSk does NOT delete information.

Information is archived, not deleted.

### Evidence

> "Archived datasets SHALL remain immutable." (DATA_MODEL.md)

> "SvitloSk SHALL NOT modify open data." (CHARTER §7)

### Owner

None. Delete is NOT an operation in SvitloSk.

---

## 2.11 Suspend

### Definition

Information processing is temporarily halted.

### Intrinsic to Lifecycle?

**NO.**

SvitloSk does NOT suspend information processing.

Information flows continuously.

### Evidence

> No evidence of suspension in canonical documents.

### Owner

None. Suspend is NOT an operation in SvitloSk.

---

## 2.12 Resume

### Definition

Suspended information processing is restarted.

### Intrinsic to Lifecycle?

**NO.**

SvitloSk does NOT resume suspended processing.

Information flows continuously.

### Evidence

> No evidence of resumption in canonical documents.

### Owner

None. Resume is NOT an operation in SvitloSk.

---

# 3. Operations Matrix

| Operation | Intrinsic? | Owner | Evidence |
|-----------|------------|-------|----------|
| Create | YES | Parser | GLOSSARY §2 |
| Update | YES | Parser, Lifecycle, Publisher | Architect Intent |
| Replace | YES | Lifecycle, Publisher | GLOSSARY §3 |
| Merge | YES | Lifecycle, Parser | Architect Intent |
| Republish | NO | Publisher | GLOSSARY §3 |
| Expire | YES | Lifecycle, Publisher | GLOSSARY §3 |
| Archive | YES | Lifecycle, Storage | GLOSSARY §2 |
| Hide | MAYBE | Publisher | No evidence |
| Reveal | MAYBE | Publisher | No evidence |
| Delete | NO | None | CHARTER §7, DATA_MODEL.md |
| Suspend | NO | None | No evidence |
| Resume | NO | None | No evidence |

---

# 4. Findings

## 4.1 Finding OPS-001

**Seven operations are intrinsic to Lifecycle.**

Create, Update, Replace, Merge, Expire, Archive, and possibly Hide/Reveal.

**Evidence:** Analysis of lifecycle operations.

**Confidence:** HIGH.

## 4.2 Finding OPS-002

**Three operations are NOT part of SvitloSk.**

Delete, Suspend, Resume are not operations in the system.

**Evidence:** CHARTER §7, DATA_MODEL.md.

**Confidence:** HIGH.

## 4.3 Finding OPS-003

**Republish is a DISTRIBUTION operation, not a lifecycle operation.**

It belongs to the Publishing domain.

**Evidence:** GLOSSARY §3.

**Confidence:** HIGH.

## 4.4 Finding OPS-004

**Multiple subsystems may own the same operation.**

Update may involve Parser, Lifecycle, and Publisher.

**Evidence:** Analysis of operation ownership.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OPS-001 | Analysis of lifecycle operations |
| OPS-002 | CHARTER §7, DATA_MODEL.md |
| OPS-003 | GLOSSARY §3 |
| OPS-004 | Analysis of operation ownership |

---

**End of Lifecycle Operations**
