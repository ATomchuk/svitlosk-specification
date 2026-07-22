# SYS001_PLACEMENT

**Document ID:** CASE-SYS-001-PLC

**Title:** Component Placement

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines where Journal, Publisher, and PWA begin and end, and whether they overlap.

---

# 2. Component Boundaries

## 2.1 Journal

### Begins

When the first Publication for a day is generated.

### Ends

When all Publications for the day have been archived.

### Scope

- Contains information from Domains A, B, and C
- Organized by Territory (Starosta Districts)
- Published via Telegram and Facebook

### Does NOT Include

- PWA (separate application)
- Queue Schedule visualization (PWA domain)
- Push Notifications (PWA domain)

### Evidence

> "The SvitloSk Public Information Journal is the primary public communication channel of the project." (CHARTER §10)

> "One journal edition may include: planned outages (today), emergency outages (today)..." (Architect Intent)

---

## 2.2 Publisher

### Begins

When Interpretation Results are available.

### Ends

When Publications are delivered to Adapters.

### Scope

- Coordinates publication across channels
- Manages publication state
- Generates Publications from Interpretation Results

### Does NOT Include

- Data acquisition (Parser domain)
- Interpretation (Parser/Lifecycle domain)
- Channel delivery (Adapter domain)
- Temporal behavior (Lifecycle domain)

### Evidence

> "Publisher: The logical Role responsible for preparing and distributing Publications." (GLOSSARY §3)

> "Publisher is intended to become a common subsystem." (Architect Intent)

---

## 2.3 PWA

### Begins

When the PWA application is loaded.

### Ends

When the resident closes the application.

### Scope

- Visualizes Queue Schedule (Domain A)
- Provides Address Lookup
- Provides Push Notification configuration
- Provides Archive
- Provides Personal Cabinet

### Does NOT Include

- Journal publications (Journal domain)
- Planned Outages display (Journal domain)
- Emergency Outages display (Journal domain)
- Telegram/Facebook publishing (Publisher domain)

### Evidence

> "PWA remains centered around Queue Schedule." (Architect Intent)

> "Push notifications belong ONLY to Queue Schedule." (Architect Intent)

---

# 3. Overlap Analysis

## 3.1 Journal vs Publisher

### Overlap?

**MINIMAL.**

Journal is the SERVICE.

Publisher is the COMPONENT that implements Journal publication.

Journal includes publications from all channels.

Publisher coordinates publication to specific channels.

### Relationship

Journal USES Publisher for publication.

Publisher IMPLEMENTS part of Journal.

---

## 3.2 Journal vs PWA

### Overlap?

**NO OVERLAP.**

Journal publishes via Telegram and Facebook.

PWA is a separate application for Queue Schedule.

They serve DIFFERENT purposes.

### Relationship

Journal and PWA are INDEPENDENT products.

They share information domains (Domain A) but not publication channels.

---

## 3.3 Publisher vs PWA

### Overlap?

**NO OVERLAP.**

Publisher coordinates publication to channels.

PWA is a standalone application.

They serve DIFFERENT purposes.

### Relationship

Publisher and PWA are INDEPENDENT.

PWA does not use Publisher for its display.

---

# 4. Placement Matrix

| Component | Begins | Ends | Scope | Overlaps |
|-----------|--------|------|-------|----------|
| Journal | First Publication | All archived | Domains A,B,C via Telegram/Facebook | Minimal with Publisher |
| Publisher | Interpretation Results | Adapter delivery | Publication coordination | None with PWA |
| PWA | App loaded | App closed | Queue Schedule visualization | None with Journal |

---

# 5. Findings

## 5.1 Finding PLC-001

**Journal, Publisher, and PWA have DISTINCT boundaries.**

They serve different purposes and have minimal overlap.

**Evidence:** Analysis of component boundaries.

**Confidence:** HIGH.

## 5.2 Finding PLC-002

**Journal and PWA are INDEPENDENT products.**

They share information domains but not publication channels.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

## 5.3 Finding PLC-003

**Publisher IMPLEMENTS part of Journal.**

Publisher coordinates publication for Journal.

**Evidence:** GLOSSARY §3, Architect Intent.

**Confidence:** HIGH.

## 5.4 Finding PLC-004

**PWA does NOT use Publisher.**

PWA is a standalone application that visualizes Queue Schedule directly.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| PLC-001 | Analysis of component boundaries |
| PLC-002 | Architect Intent |
| PLC-003 | GLOSSARY §3, Architect Intent |
| PLC-004 | Architect Intent |

---

**End of Component Placement**
