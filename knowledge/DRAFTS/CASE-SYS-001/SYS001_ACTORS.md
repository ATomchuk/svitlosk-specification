# SYS001_ACTORS

**Document ID:** CASE-SYS-001-ACT

**Title:** System Actors

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies ALL actors in the system.

---

# 2. Actor Analysis

## 2.1 External Actors

### DSO (Distribution System Operator)

**Type:** External Actor

**Role:** Publishes official Open Data

**Evidence:** GLOSSARY §2

**Actor?** YES — external entity that interacts with the system.

---

### Resident

**Type:** External Actor

**Role:** Uses SvitloSk to obtain information

**Evidence:** GLOSSARY §6

**Actor?** YES — human actor that interacts with the system.

---

### Architect

**Type:** External Actor

**Role:** Makes architectural decisions

**Evidence:** Research methodology

**Actor?** YES — human actor that governs the system.

---

## 2.2 System Actors (Components)

### Parser A

**Type:** System Actor

**Role:** Acquires Queue Schedule from DSO

**Evidence:** Architect Intent

**Actor?** BORDERLINE — active component, but not an autonomous actor.

---

### Parser B

**Type:** System Actor

**Role:** Acquires Planned and Emergency Outages from DSO

**Evidence:** Architect Intent

**Actor?** BORDERLINE — active component, but not an autonomous actor.

---

### Publisher

**Type:** System Actor

**Role:** Coordinates publication

**Evidence:** Architect Intent, GLOSSARY §3

**Actor?** BORDERLINE — active component with coordination responsibility.

---

### Telegram Adapter

**Type:** System Actor

**Role:** Publishes to Telegram

**Evidence:** Architect Intent

**Actor?** BORDERLINE — active component, but follows Publisher instructions.

---

### Facebook Adapter

**Type:** System Actor

**Role:** Publishes to Facebook

**Evidence:** Architect Intent

**Actor?** BORDERLINE — active component, but follows Publisher instructions.

---

### PWA

**Type:** System Actor

**Role:** Visualizes Queue Schedule

**Evidence:** Architect Intent

**Actor?** BORDERLINE — active application, but passive display.

---

### Archive

**Type:** System Actor

**Role:** Preserves historical information

**Evidence:** GLOSSARY §2

**Actor?** BORDERLINE — passive storage, not an active actor.

---

## 2.3 Conceptual Actors

### Journal

**Type:** Conceptual Actor

**Role:** Ongoing publication service

**Evidence:** CHARTER §10

**Actor?** NO — Journal is a SERVICE, not an actor.

---

### Lifecycle

**Type:** Conceptual Actor

**Role:** Pattern describing information flow

**Evidence:** CASE-LC-001

**Actor?** NO — Lifecycle is a PATTERN, not an actor.

---

# 3. Actor Classification

## 3.1 True Actors

| Actor | Type | Evidence |
|-------|------|----------|
| DSO | External | GLOSSARY §2 |
| Resident | External | GLOSSARY §6 |
| Architect | External | Research methodology |

## 3.2 System Components (Not True Actors)

| Component | Type | Evidence |
|-----------|------|----------|
| Parser A | System | Architect Intent |
| Parser B | System | Architect Intent |
| Publisher | System | GLOSSARY §3 |
| Telegram Adapter | System | Architect Intent |
| Facebook Adapter | System | Architect Intent |
| PWA | System | Architect Intent |
| Archive | System | GLOSSARY §2 |

## 3.3 Conceptual Entities (Not Actors)

| Entity | Type | Evidence |
|--------|------|----------|
| Journal | Service | CHARTER §10 |
| Lifecycle | Pattern | CASE-LC-001 |

---

# 4. Findings

## 4.1 Finding ACT-001

**There are 3 TRUE ACTORS.**

DSO, Resident, Architect.

**Evidence:** Analysis of actor characteristics.

**Confidence:** HIGH.

## 4.2 Finding ACT-002

**There are 7 SYSTEM COMPONENTS.**

Parser A, Parser B, Publisher, Telegram Adapter, Facebook Adapter, PWA, Archive.

These are NOT true actors — they are components that perform specific functions.

**Evidence:** Analysis of actor characteristics.

**Confidence:** HIGH.

## 4.3 Finding ACT-003

**There are 2 CONCEPTUAL ENTITIES.**

Journal and Lifecycle are NOT actors — they are concepts.

**Evidence:** Analysis of actor characteristics.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| ACT-001 | Analysis of actor characteristics |
| ACT-002 | Analysis of actor characteristics |
| ACT-003 | Analysis of actor characteristics |

---

**End of System Actors**
