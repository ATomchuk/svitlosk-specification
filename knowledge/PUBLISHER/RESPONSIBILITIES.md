# Publisher Responsibilities

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the responsibilities of Publisher.

---

# Publisher Responsibilities

## Publication Management

| Responsibility | Channel-Independent | Evidence |
|----------------|---------------------|----------|
| Create Publication | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Update Publication | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Replace Publication | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Remove Publication | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

## Content Formatting

| Responsibility | Channel-Independent | Evidence |
|----------------|---------------------|----------|
| Format Emergency Outages | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Format Planned Outages | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Format Tomorrow Outages | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Format Technical Message | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

## Territorial Organization

| Responsibility | Channel-Independent | Evidence |
|----------------|---------------------|----------|
| Group by Territory | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Identify Territory | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

## Lifecycle Execution

| Responsibility | Channel-Independent | Evidence |
|----------------|---------------------|----------|
| Execute Expiry | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Execute Update | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

# What Publisher Does NOT Do

| Responsibility | Owner | Evidence |
|----------------|-------|----------|
| Retrieve Open Data | Parser | GLOSSARY §2 |
| Make Business Decisions | Lifecycle | CASE-PUB-004, CASE-PUB-005 |
| Detect Data Changes | Parser | CASE-TG-CORE-001 |
| Detect Temporal Events | Lifecycle | CASE-LC-001 |
| Channel Delivery | Adapter | CASE-TG-CORE-001 |
| Channel-Specific Formatting | Adapter | CASE-TG-CORE-001 |

---

# Responsibility Summary

| Category | Count | Channel-Independent |
|----------|-------|---------------------|
| Publication Management | 4 | YES |
| Content Formatting | 4 | YES |
| Territorial Organization | 2 | YES |
| Lifecycle Execution | 2 | YES |
| **Total** | **12** | **YES** |

---

# Evidence

| Responsibility | Source |
|----------------|--------|
| Publication Management | CASE-PUB-002, CASE-TG-CORE-001 |
| Content Formatting | CASE-PUB-002, CASE-TG-CORE-001 |
| Territorial Organization | CASE-PUB-002, CASE-TG-CORE-001 |
| Lifecycle Execution | CASE-PUB-002, CASE-TG-CORE-001 |

---

**End of Responsibilities**
