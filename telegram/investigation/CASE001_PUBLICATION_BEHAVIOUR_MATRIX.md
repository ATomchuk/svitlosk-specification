# CASE001_PUBLICATION_BEHAVIOUR_MATRIX

**Document ID:** CASE001B-BEHAVIOUR

**Title:** Publication — Component Interaction Matrix

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document determines what every repository Component does with Publication.

---

# Component Interaction Matrix

## Parser

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Parser retrieves data, does not create Publications |
| Modify Publication? | NO | Parser does not interact with Publications |
| Read Publication? | NO | Parser does not read Publications |
| Own Publication? | NO | Parser owns Normalized Dataset, not Publications |
| Reference Publication? | NO | Parser produces data for Publication Engine |
| Destroy Publication? | NO | Parser does not interact with Publications |
| Archive Publication? | NO | Parser does not interact with Publications |
| Ignore Publication? | YES | Parser is unaware of Publications |

**Summary:** Parser produces Normalized Dataset which becomes input for Publication creation. Parser never touches Publication directly.

**Evidence:** TJS-010 §4.2, §5.2

---

## Schedule Generator

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Schedule Generator produces schedules, not Publications |
| Modify Publication? | NO | Schedule Generator does not interact with Publications |
| Read Publication? | NO | Schedule Generator does not read Publications |
| Own Publication? | NO | Schedule Generator owns Schedules |
| Reference Publication? | NO | Schedule Generator feeds into Publication Engine |
| Destroy Publication? | NO | Schedule Generator does not interact with Publications |
| Archive Publication? | NO | Schedule Generator does not interact with Publications |
| Ignore Publication? | YES | Schedule Generator is unaware of Publications |

**Summary:** Schedule Generator produces Schedules which become input for Publication creation. Schedule Generator never touches Publication directly.

**Evidence:** TJS-010 §4.5, §5.1

---

## Graphic Generator

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Graphic Generator produces Graphics, not Publications |
| Modify Publication? | NO | Graphic Generator does not interact with Publications |
| Read Publication? | NO | Graphic Generator does not read Publications |
| Own Publication? | NO | Graphic Generator owns Graphics |
| Reference Publication? | NO | Graphic Generator feeds into Publication Engine |
| Destroy Publication? | NO | Graphic Generator does not interact with Publications |
| Archive Publication? | NO | Graphic Generator does not interact with Publications |
| Ignore Publication? | YES | Graphic Generator is unaware of Publications |

**Summary:** Graphic Generator produces Graphics which become input for Publication creation. Graphic Generator never touches Publication directly.

**Evidence:** TJS-010 §4.6, §5.1, TJS-022

---

## Publication Engine

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | **YES** | Publication Engine generates Publications from Normalized Dataset |
| Modify Publication? | **YES** | Publication Engine updates Publications when data changes |
| Read Publication? | **YES** | Publication Engine reads Publications for Canonical Equality check |
| Own Publication? | **YES** | Publication Engine owns all automatically generated Publications |
| Reference Publication? | **YES** | Publication Engine references Publications in Publication Package |
| Destroy Publication? | **YES** | Publication Engine removes temporary Publications |
| Archive Publication? | **YES** | Publication Engine archives Publications when reporting period ends |
| Ignore Publication? | NO | Publication Engine is the primary manager of Publications |

**Summary:** Publication Engine is the primary actor for Publication. It creates, modifies, reads, owns, references, destroys, and archives Publications.

**Evidence:** TJS-010 §4.1, §5.1, TJS-021, Legacy TJS-007

---

## Telegram Publisher

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Telegram Publisher delivers, does not create |
| Modify Publication? | **YES** | Telegram Publisher edits Telegram messages |
| Read Publication? | **YES** | Telegram Publisher reads Publications for delivery |
| Own Publication? | NO | Publication Engine owns Publications |
| Reference Publication? | **YES** | Telegram Publisher references Publications for delivery |
| Destroy Publication? | **YES** | Telegram Publisher deletes temporary Publications from Telegram |
| Archive Publication? | NO | Telegram Publisher does not archive |
| Ignore Publication? | NO | Telegram Publisher is the delivery mechanism |

**Summary:** Telegram Publisher is the delivery mechanism. It delivers Publications to Telegram, edits messages, and deletes temporary Publications.

**Evidence:** TJS-010 §4.4, §5.1

---

## Telegram Channel

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Telegram Channel receives, does not create |
| Modify Publication? | NO | Telegram Channel displays, does not modify |
| Read Publication? | **YES** | Telegram Channel displays Publications to Subscribers |
| Own Publication? | NO | Publication Engine owns Publications |
| Reference Publication? | **YES** | Telegram Channel references Publications for display |
| Destroy Publication? | NO | Telegram Channel does not destroy |
| Archive Publication? | NO | Telegram Channel does not archive |
| Ignore Publication? | NO | Telegram Channel is the display mechanism |

**Summary:** Telegram Channel is the display mechanism. It displays Publications to Subscribers.

**Evidence:** TJS-010 §4.8, §5.1

---

## Data Storage

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Data Storage stores, does not create |
| Modify Publication? | **YES** | Data Storage persists Publication updates |
| Read Publication? | **YES** | Data Storage retrieves Publications |
| Own Publication? | NO | Publication Engine owns Publications |
| Reference Publication? | **YES** | Data Storage references Publications by ID |
| Destroy Publication? | NO | Data Storage does not destroy |
| Archive Publication? | **YES** | Data Storage preserves archived Publications |
| Ignore Publication? | NO | Data Storage is the persistence mechanism |

**Summary:** Data Storage is the persistence mechanism. It stores, retrieves, and preserves Publications.

**Evidence:** TJS-010 §4.7, §5.1

---

## Issue

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Issue does not create Publications |
| Modify Publication? | NO | Issue does not modify Publications |
| Read Publication? | NO | Issue does not read Publications |
| Own Publication? | NO | Publication Engine owns Publications |
| Reference Publication? | **YES** | Issue contains Publications for one day |
| Destroy Publication? | NO | Issue does not destroy Publications |
| Archive Publication? | NO | Issue does not archive Publications |
| Ignore Publication? | NO | Issue is the temporal container |

**Summary:** Issue is the temporal container for Publications. It contains Publications for one calendar day.

**Evidence:** TJS-000 §4, TJS-021 §8

---

## Journal

| Action | Performs? | Evidence |
|--------|-----------|----------|
| Create Publication? | NO | Journal does not create Publications |
| Modify Publication? | NO | Journal does not modify Publications |
| Read Publication? | NO | Journal does not read Publications |
| Own Publication? | NO | Publication Engine owns Publications |
| Reference Publication? | **YES** | Journal contains Issues which contain Publications |
| Destroy Publication? | NO | Journal does not destroy Publications |
| Archive Publication? | NO | Journal does not archive Publications |
| Ignore Publication? | NO | Journal is the ultimate container |

**Summary:** Journal is the ultimate container. It contains Issues which contain Publications.

**Evidence:** TJS-000 §4, GLOSSARY.md §3

---

# Component Interaction Summary

| Component | Creates | Modifies | Reads | Owns | References | Destroys | Archives | Ignores |
|-----------|---------|----------|-------|------|------------|----------|----------|---------|
| Parser | NO | NO | NO | NO | NO | NO | NO | YES |
| Schedule Generator | NO | NO | NO | NO | NO | NO | NO | YES |
| Graphic Generator | NO | NO | NO | NO | NO | NO | NO | YES |
| Publication Engine | YES | YES | YES | YES | YES | YES | YES | NO |
| Telegram Publisher | NO | YES | YES | NO | YES | YES | NO | NO |
| Telegram Channel | NO | NO | YES | NO | YES | NO | NO | NO |
| Data Storage | NO | YES | YES | NO | YES | NO | YES | NO |
| Issue | NO | NO | NO | NO | YES | NO | NO | NO |
| Journal | NO | NO | NO | NO | YES | NO | NO | NO |

---

# Key Insight

**Publication Engine is the ONLY Component that performs ALL actions on Publication.**

**All other Components either:**

- Produce input for Publication creation (Parser, Schedule Generator, Graphic Generator)
- Deliver Publication to Telegram (Telegram Publisher)
- Display Publication to Subscribers (Telegram Channel)
- Store Publication persistently (Data Storage)
- Contain Publication temporally (Issue, Journal)

**No other Component can create, modify, own, or destroy Publications.**

**Evidence:** TJS-010 §5.2 (Illegal Interactions)

---

# End of Component Interaction Matrix
