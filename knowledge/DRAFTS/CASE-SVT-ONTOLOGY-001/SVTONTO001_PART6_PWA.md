# SVTONTO001_PART6_PWA

**Document ID:** CASE-SVT-ONTOLOGY-001-P6

**Title:** PWA Ontology

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines the ontology of Screen, Timeline, Tomorrow Graph, Push Notification, Address Lookup, and Personal Cabinet.

---

# 2. Concept Analysis

## 2.1 Screen

### Repository Evidence

> "Progressive Web Application (PWA)" (ARCHITECTURE.md §Layer 6)

### Architect Intent Evidence

> "Current screens: Main, Archive, Address Lookup, Personal Cabinet"

### Ontological Status

**Screen is a REPRESENTATION.**

It is a user interface component displaying information.

### Evidence

- Architect Intent explicitly mentions screens
- Screens are how residents interact with the PWA
- Each screen displays different information

---

## 2.2 Timeline

### Repository Evidence

> "Outage Timeline: A visual representation of electricity availability during one Reporting Period." (GLOSSARY.md §5)

### Architect Intent Evidence

> "Timeline" is a screen component displaying Queue Schedule

### Ontological Status

**Timeline is a COMPOSITE REPRESENTATION.**

It displays multiple Schedules over time for one Subqueue.

### Evidence

- GLOSSARY defines it as "a visual representation"
- It contains multiple schedules
- It is a key component of the Main screen

---

## 2.3 Tomorrow Graph

### Repository Evidence

No direct definition in canonical documents.

### Architect Intent Evidence

> "Tomorrow graph" is a screen component

> Displays Queue Schedule for tomorrow

### Ontological Status

**Tomorrow Graph is a COMPOSITE REPRESENTATION.**

It displays Schedules for all 12 Subqueues for tomorrow.

### Evidence

- Architect Intent mentions it as a screen component
- It contains schedules for all subqueues
- It is a key component of the Main screen

---

## 2.4 Push Notification

### Repository Evidence

> "Notification Services" (ARCHITECTURE.md §Layer 8)

### Architect Intent Evidence

> "Push notifications belong ONLY to Queue Schedule."

> "They notify about: electricity loss, electricity restoration"

> "for the selected subqueue."

> "NOT about planned outages."

> "NOT about emergency outages."

### Ontological Status

**Push Notification is an ATOMIC REPRESENTATION.**

It is a discrete notification about electricity state change for one Subqueue.

### Evidence

- Architect Intent explicitly defines its scope
- It is atomic (one notification per event)
- It belongs ONLY to Queue Schedule domain

---

## 2.5 Address Lookup

### Repository Evidence

No direct definition in canonical documents.

### Architect Intent Evidence

> "Address Lookup: Allows resident to determine which subqueue serves their address."

> "Search by: Settlement, Street, House"

### Ontological Status

**Address Lookup is a PROCESS.**

It is a search function that maps addresses to subqueues.

### Evidence

- Architect Intent defines it as a search function
- It is a process that takes address and returns subqueue
- It bridges Domain A (Queue Schedule) and Domain B/C (Address-based)

---

## 2.6 Personal Cabinet

### Repository Evidence

No direct definition in canonical documents.

### Architect Intent Evidence

> "Personal Cabinet: Allows configuration of: Two independent locations, Push notifications, Silence mode, Future schedule notifications, About, Feedback, Sharing"

### Ontological Status

**Personal Cabinet is a COMPOSITE OBJECT.**

It contains multiple configuration items for the resident.

### Evidence

- Architect Intent defines it as a configuration area
- It contains multiple independent settings
- It is personalized to each resident

---

# 3. Ontological Relationships

```
PWA Application
    ↓ contains
Screen (Main, Archive, Address Lookup, Personal Cabinet)
    ↓ Main Screen contains
    ├── Timeline (Composite Representation)
    ├── Tomorrow Graph (Composite Representation)
    └── Push Notification (Atomic Representation, separate)
    ↓ Address Lookup Screen contains
    └── Address → Subqueue mapping (Process)
    ↓ Personal Cabinet contains
    └── Configuration items (Composite Object)
```

---

# 4. Screen Independence

## 4.1 Main Screen

Main Screen is:
- Primary screen for Queue Schedule display
- Contains Timeline and Tomorrow Graph
- Displays current Queue Schedule for one selected subqueue
- Independent from other screens

## 4.2 Archive Screen

Archive Screen is:
- Historical Queue Schedule display
- Contains Calendar and Historical Timelines
- Displays past Queue Schedules
- Independent from other screens

## 4.3 Address Lookup Screen

Address Lookup Screen is:
- Search function for address → subqueue mapping
- Takes Settlement, Street, House as input
- Returns subqueue assignment
- Independent from other screens

## 4.4 Personal Cabinet Screen

Personal Cabinet Screen is:
- Configuration area for resident preferences
- Contains two independent locations
- Contains push notification settings
- Independent from other screens

---

# 5. Push Notification Scope

## 5.1 Push Notification belongs to Queue Schedule ONLY

Push notifications:
- Notify about electricity loss
- Notify about electricity restoration
- Are for the selected subqueue
- Do NOT notify about planned outages
- Do NOT notify about emergency outages

## 5.2 Push Notification independence

Push notifications:
- Are independent from Journal
- Are independent from Telegram/Facebook
- Belong exclusively to PWA Queue Schedule domain

---

# 6. Findings

## 6.1 Finding PWA-001

**Screen is a REPRESENTATION.**

It is a user interface component displaying information.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 6.2 Finding PWA-002

**Timeline and Tomorrow Graph are COMPOSITE REPRESENTATIONS.**

They display multiple Schedules over time.

**Evidence:** GLOSSARY.md §5, Architect Intent.

**Confidence:** HIGH.

## 6.3 Finding PWA-003

**Push Notification is an ATOMIC REPRESENTATION.**

It is a discrete notification about electricity state change for one Subqueue.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 6.4 Finding PWA-004

**Address Lookup is a PROCESS.**

It maps addresses to subqueues.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 6.5 Finding PWA-005

**Personal Cabinet is a COMPOSITE OBJECT.**

It contains multiple configuration items for the resident.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 6.6 Finding PWA-006

**Push Notifications belong ONLY to Queue Schedule.**

They do NOT notify about planned or emergency outages.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 7. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| PWA-001 | Architect Intent |
| PWA-002 | GLOSSARY.md §5, Architect Intent |
| PWA-003 | Architect Intent |
| PWA-004 | Architect Intent |
| PWA-005 | Architect Intent |
| PWA-006 | Architect Intent |

---

**End of PWA Ontology**
