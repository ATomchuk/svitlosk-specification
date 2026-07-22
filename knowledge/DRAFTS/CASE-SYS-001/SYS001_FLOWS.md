# SYS001_FLOWS

**Document ID:** CASE-SYS-001-FLW

**Title:** System Flows

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document reconstructs ALL flows in the system.

Do NOT merge them.

---

# 2. System Flows

## 2.1 Information Flow

### Definition

The flow of information from external sources into the system.

### Path

```
DSO → Parser A → Queue Schedule Information
DSO → Parser B → Planned Outage Information
DSO → Parser B → Emergency Outage Information
```

### Characteristics

- Information originates EXTERNALLY
- SvitloSk does NOT create information
- Information is PRESERVED exactly as published

**Evidence:** CHARTER §7, §8.

---

## 2.2 Knowledge Flow

### Definition

The flow of interpreted information (knowledge) from parsing to publication.

### Path

```
Queue Schedule Information → Interpretation → Queue Knowledge
Planned Outage Information → Interpretation → Planned Outage Knowledge
Emergency Outage Information → Interpretation → Emergency Outage Knowledge
```

### Characteristics

- Knowledge is CREATED by interpretation
- Knowledge IMPROVES understanding
- Knowledge does NOT change factual meaning

**Evidence:** GLOSSARY §2.

---

## 2.3 Publication Flow

### Definition

The flow of prepared publications from Publisher to channels.

### Path

```
Publisher → Telegram Adapter → Telegram Posts
Publisher → Facebook Adapter → Facebook Posts
Publisher → PWA → PWA Display
```

### Characteristics

- Publications are DERIVED from Interpretation Results
- Publications are CHANNEL-INDEPENDENT
- Adapters RENDER publications for specific channels

**Evidence:** GLOSSARY §3, Architect Intent.

---

## 2.4 Representation Flow

### Definition

The flow of channel-specific representations to residents.

### Path

```
Telegram Posts → Residents
Facebook Posts → Residents
PWA Display → Residents
Push Notifications → Residents
```

### Characteristics

- Representations are CHANNEL-SPECIFIC
- Representations PRESERVE factual meaning
- Residents INTERACT with representations

**Evidence:** Architect Intent.

---

## 2.5 Update Flow

### Definition

The flow of updates when information changes.

### Path

```
DSO changes data
    → Parser detects change
    → Parser acquires new data
    → Lifecycle determines update needed
    → Publisher generates updated Publication
    → Adapter updates channel
```

### Characteristics

- Updates are EVENT-DRIVEN
- Updates involve MULTIPLE subsystems
- Updates preserve information integrity

**Evidence:** CASE-LC-001.

---

## 2.6 Temporal Flow

### Definition

The flow of time-based events (expiry, replacement).

### Path

```
Lifecycle detects temporal event
    → Lifecycle determines action needed
    → Publisher executes action
    → Adapter updates channel
```

### Characteristics

- Temporal events are DETECTED by Lifecycle
- Temporal actions are EXECUTED by Publisher
- Temporal behavior is SEPARATED from data acquisition

**Evidence:** CASE-LC-001.

---

## 2.7 Notification Flow

### Definition

The flow of push notifications to residents.

### Path

```
Queue Schedule change detected
    → Push Notification generated
    → Resident receives notification
```

### Characteristics

- Notifications belong ONLY to Queue Schedule
- Notifications do NOT belong to planned or emergency outages
- Notifications are CONFIGURABLE by residents

**Evidence:** Architect Intent.

---

# 3. Flow Matrix

| Flow | Source | Destination | Owner |
|------|--------|-------------|-------|
| Information | DSO | Parser | Parser |
| Knowledge | Parser | Publisher | Lifecycle |
| Publication | Publisher | Adapter | Publisher |
| Representation | Adapter | Resident | Adapter |
| Update | DSO | Channel | Lifecycle + Publisher |
| Temporal | Lifecycle | Channel | Lifecycle + Publisher |
| Notification | Queue Schedule | Resident | Publisher |

---

# 4. Findings

## 4.1 Finding FLW-001

**There are 7 distinct flows.**

Information, Knowledge, Publication, Representation, Update, Temporal, Notification.

**Evidence:** Analysis of system flows.

**Confidence:** HIGH.

## 4.2 Finding FLW-002

**Flows are CAUSALLY LINKED but DISTINCT.**

Information Flow → Knowledge Flow → Publication Flow → Representation Flow.

**Evidence:** Analysis of flow relationships.

**Confidence:** HIGH.

## 4.3 Finding FLW-003

**Update and Temporal flows are CROSS-CUTTING.**

They affect multiple other flows.

**Evidence:** Analysis of flow characteristics.

**Confidence:** HIGH.

## 4.4 Finding FLW-004

**Notification Flow is DOMAIN-SPECIFIC.**

It belongs ONLY to Queue Schedule (Domain A).

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| FLW-001 | Analysis of system flows |
| FLW-002 | Analysis of flow relationships |
| FLW-003 | Analysis of flow characteristics |
| FLW-004 | Architect Intent |

---

**End of System Flows**
