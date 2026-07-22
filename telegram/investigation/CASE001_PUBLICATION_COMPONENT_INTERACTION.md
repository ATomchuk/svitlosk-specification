# CASE001_PUBLICATION_COMPONENT_INTERACTION

**Document ID:** CASE001B-COMPONENT

**Title:** Publication — Component Interaction Detail

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Living Domain Object Investigation

---

# Purpose

This document provides detailed analysis of how each Component interacts with Publication.

---

# Detailed Component Analysis

## Parser

**Relationship to Publication:** INDIRECT

**How it interacts:**

1. Parser retrieves Open Data from Data Source
2. Parser validates and normalizes data
3. Parser stores Normalized Dataset in Data Storage
4. Parser does NOT create, modify, read, own, reference, destroy, or archive Publications

**Evidence:**

- TJS-010 §4.2: "Parser — Retrieves Open Data from approved Data Sources"
- TJS-010 §5.2: "Parser → Publication Engine (reinterpretation): ILLEGAL"

**Conclusion:** Parser produces INPUT for Publication creation but never touches Publication directly.

---

## Schedule Generator

**Relationship to Publication:** INDIRECT

**How it interacts:**

1. Schedule Generator receives Normalized Dataset
2. Schedule Generator produces Schedules
3. Schedule Generator stores Schedules in Data Storage
4. Schedule Generator does NOT create, modify, read, own, reference, destroy, or archive Publications

**Evidence:**

- TJS-010 §4.5: "Schedule Generator — Transforms normalized outage data into deterministic schedules"
- TJS-010 §5.1: "Publication Engine → Schedule Generator: Schedule Request"

**Conclusion:** Schedule Generator produces INPUT for Publication creation but never touches Publication directly.

---

## Graphic Generator

**Relationship to Publication:** INDIRECT

**How it interacts:**

1. Graphic Generator receives Normalized Dataset
2. Graphic Generator produces Graphics (images)
3. Graphic Generator stores Graphics in Data Storage
4. Graphic Generator does NOT create, modify, read, own, reference, destroy, or archive Publications

**Evidence:**

- TJS-010 §4.6: "Graphic Generator — Produces visual materials based on normalized outage schedules"
- TJS-010 §5.1: "Publication Engine → Graphic Generator: Graphic Request"
- TJS-022: Graphic Publications are a separate concept

**Conclusion:** Graphic Generator produces INPUT for Publication creation but never touches Publication directly.

---

## Publication Engine

**Relationship to Publication:** PRIMARY

**How it interacts:**

1. **Creates:** Publication Engine generates Publications from Normalized Dataset
2. **Modifies:** Publication Engine updates Publications when data changes
3. **Reads:** Publication Engine reads Publications for Canonical Equality check
4. **Owns:** Publication Engine owns all automatically generated Publications
5. **References:** Publication Engine references Publications in Publication Package
6. **Destroys:** Publication Engine removes temporary Publications
7. **Archives:** Publication Engine archives Publications when reporting period ends

**Evidence:**

- TJS-010 §4.1: "Publication Engine — Transforms normalized dataset into deterministic Publication Package"
- TJS-010 §5.1: All approved interactions involving Publication
- TJS-021: Complete lifecycle management

**Conclusion:** Publication Engine is the PRIMARY actor for Publication. It performs ALL actions.

---

## Telegram Publisher

**Relationship to Publication:** DELIVERY

**How it interacts:**

1. **Creates:** NO — Telegram Publisher delivers, does not create
2. **Modifies:** YES — Telegram Publisher edits Telegram messages
3. **Reads:** YES — Telegram Publisher reads Publications for delivery
4. **Owns:** NO — Publication Engine owns Publications
5. **References:** YES — Telegram Publisher references Publications for delivery
6. **Destroys:** YES — Telegram Publisher deletes temporary Publications from Telegram
7. **Archives:** NO — Telegram Publisher does not archive

**Evidence:**

- TJS-010 §4.4: "Telegram Publisher — Telegram-specific implementation of Publisher Role"
- TJS-010 §5.1: "Telegram Publisher → Telegram Channel: Publication"

**Conclusion:** Telegram Publisher is the DELIVERY mechanism. It delivers Publications to Telegram.

---

## Telegram Channel

**Relationship to Publication:** DISPLAY

**How it interacts:**

1. **Creates:** NO — Telegram Channel receives, does not create
2. **Modifies:** NO — Telegram Channel displays, does not modify
3. **Reads:** YES — Telegram Channel displays Publications to Subscribers
4. **Owns:** NO — Publication Engine owns Publications
5. **References:** YES — Telegram Channel references Publications for display
6. **Destroys:** NO — Telegram Channel does not destroy
7. **Archives:** NO — Telegram Channel does not archive

**Evidence:**

- TJS-010 §4.8: "Telegram Channel — Primary public information journal delivering Publications"
- TJS-010 §5.1: "Telegram Channel → Subscribers: Publication"

**Conclusion:** Telegram Channel is the DISPLAY mechanism. It displays Publications to Subscribers.

---

## Data Storage

**Relationship to Publication:** PERSISTENCE

**How it interacts:**

1. **Creates:** NO — Data Storage stores, does not create
2. **Modifies:** YES — Data Storage persists Publication updates
3. **Reads:** YES — Data Storage retrieves Publications
4. **Owns:** NO — Publication Engine owns Publications
5. **References:** YES — Data Storage references Publications by ID
6. **Destroys:** NO — Data Storage does not destroy
7. **Archives:** YES — Data Storage preserves archived Publications

**Evidence:**

- TJS-010 §4.7: "Data Storage — Preserving normalized data, publications, schedules, and historical records"
- TJS-010 §5.1: "Publication Engine → Data Storage: Publication"

**Conclusion:** Data Storage is the PERSISTENCE mechanism. It stores, retrieves, and preserves Publications.

---

## Issue

**Relationship to Publication:** CONTAINER

**How it interacts:**

1. **Creates:** NO — Issue does not create Publications
2. **Modifies:** NO — Issue does not modify Publications
3. **Reads:** NO — Issue does not read Publications
4. **Owns:** NO — Publication Engine owns Publications
5. **References:** YES — Issue contains Publications for one day
6. **Destroys:** NO — Issue does not destroy Publications
7. **Archives:** NO — Issue does not archive Publications

**Evidence:**

- TJS-000 §4: "Issue represents one editorial edition of the Journal for a single calendar day"
- TJS-021 §8: "An Issue opens when the first Publication for a calendar day is generated"

**Conclusion:** Issue is the TEMPORAL CONTAINER. It contains Publications for one calendar day.

---

## Journal

**Relationship to Publication:** ULTIMATE CONTAINER

**How it interacts:**

1. **Creates:** NO — Journal does not create Publications
2. **Modifies:** NO — Journal does not modify Publications
3. **Reads:** NO — Journal does not read Publications
4. **Owns:** NO — Publication Engine owns Publications
5. **References:** YES — Journal contains Issues which contain Publications
6. **Destroys:** NO — Journal does not destroy Publications
7. **Archives:** NO — Journal does not archive Publications

**Evidence:**

- TJS-000 §4: "Journal represents the continuous informational publication"
- GLOSSARY.md §3: "The Telegram Journal publishes Publications generated by the Publisher"

**Conclusion:** Journal is the ULTIMATE CONTAINER. It contains Issues which contain Publications.

---

# Component Interaction Summary Table

| Component | Creates | Modifies | Reads | Owns | References | Destroys | Archives |
|-----------|---------|----------|-------|------|------------|----------|----------|
| Parser | - | - | - | - | - | - | - |
| Schedule Generator | - | - | - | - | - | - | - |
| Graphic Generator | - | - | - | - | - | - | - |
| Publication Engine | YES | YES | YES | YES | YES | YES | YES |
| Telegram Publisher | - | YES | YES | - | YES | YES | - |
| Telegram Channel | - | - | YES | - | YES | - | - |
| Data Storage | - | YES | YES | - | YES | - | YES |
| Issue | - | - | - | - | YES | - | - |
| Journal | - | - | - | - | YES | - | - |

---

# Key Insight

**Publication Engine is the ONLY Component that performs ALL actions on Publication.**

**No other Component can create, modify, own, or destroy Publications.**

**All other Components either:**

- Produce input for Publication creation (Parser, Schedule Generator, Graphic Generator)
- Deliver Publication to Telegram (Telegram Publisher)
- Display Publication to Subscribers (Telegram Channel)
- Store Publication persistently (Data Storage)
- Contain Publication temporally (Issue, Journal)

**This confirms Publication Engine as the Aggregate Root for Publication.**

---

# End of Component Interaction Detail
