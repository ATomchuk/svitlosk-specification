# Publisher Channel Boundary

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the boundary between Publisher (generic) and Channel (specific).

---

# Channel Boundary

## Generic Core (Publisher)

| Component | Channel-Independent | Evidence |
|-----------|---------------------|----------|
| Data Acquisition | YES | CASE-TG-CORE-001 |
| Data Processing | YES | CASE-TG-CORE-001 |
| Publication Generation | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Lifecycle Management | YES | CASE-LC-001, CASE-PUB-005 |
| Content Formatting | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Territorial Organization | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

## Channel-Specific (Adapter)

| Component | Channel-Specific | Evidence |
|-----------|------------------|----------|
| Graph Generation | PARTIALLY | CASE-TG-CORE-001 |
| Text Formatting | YES | CASE-TG-CORE-001 |
| Message Building | PARTIALLY | CASE-TG-CORE-001 |
| Channel Delivery | YES | CASE-TG-CORE-001 |
| Message Editing | YES | CASE-TG-CORE-001 |
| Message Deletion | YES | CASE-TG-CORE-001 |
| Channel State | YES | CASE-TG-CORE-001 |

---

# Boundary Visualization

```
┌─────────────────────────────────────────────────────────────┐
│                    GENERIC CORE                              │
├─────────────────────────────────────────────────────────────┤
│ Data Acquisition                                            │
│ Data Processing                                             │
│ Publication Generation                                      │
│ Lifecycle Management                                        │
│ Content Formatting                                          │
│ Territorial Organization                                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                CHANNEL-SPECIFIC                             │
├─────────────────────────────────────────────────────────────┤
│ Graph Generation (format)                                   │
│ Text Formatting (format)                                    │
│ Message Building (format)                                   │
│ Channel Delivery (API)                                      │
│ Message Editing (API)                                       │
│ Message Deletion (API)                                      │
│ Channel State (API)                                         │
└─────────────────────────────────────────────────────────────┘
```

---

# Boundary Analysis

## What Could Be Extracted to Publisher

| Component | Evidence |
|-----------|----------|
| Data Acquisition | Generic |
| Data Processing | Generic |
| Publication Generation | Generic |
| Lifecycle Management | Generic |
| Content Formatting | Generic |
| Territorial Organization | Generic |

## What Must Stay in Adapter

| Component | Evidence |
|-----------|----------|
| Graph Generation (format) | Channel-specific |
| Text Formatting (format) | Channel-specific |
| Message Building (format) | Channel-specific |
| Channel Delivery (API) | Channel-specific |
| Message Editing (API) | Channel-specific |
| Message Deletion (API) | Channel-specific |
| Channel State (API) | Channel-specific |

---

# Evidence

| Boundary | Source |
|----------|--------|
| Generic Core | CASE-TG-CORE-001 |
| Channel-Specific | CASE-TG-CORE-001 |

---

**End of Channel Boundary**
