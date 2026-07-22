# Publisher Operations

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the operations performed by Publisher.

---

# Operations

## Publication Operations

| Operation | Input | Output | Channel-Independent | Evidence |
|-----------|-------|--------|---------------------|----------|
| Create Publication | Interpretation Result, Territory | Publication | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Update Publication | Updated Interpretation Result, Publication ID | Updated Publication | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Replace Publication | New Interpretation Result, Territory | New Publication | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Remove Publication | Publication ID | Void | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

## Content Operations

| Operation | Input | Output | Channel-Independent | Evidence |
|-----------|-------|--------|---------------------|----------|
| Format Emergency Outages | Emergency Outage Information | Formatted Content | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Format Planned Outages | Planned Outage Information | Formatted Content | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Format Tomorrow Outages | Tomorrow Outage Information | Formatted Content | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Format Technical Message | Technical Message Content | Formatted Content | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

## Territorial Operations

| Operation | Input | Output | Channel-Independent | Evidence |
|-----------|-------|--------|---------------------|----------|
| Group by Territory | Publications, Territory Structure | Organized Publications | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Identify Territory | Address, Territory Structure | Territory | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

## Lifecycle Operations

| Operation | Input | Output | Channel-Independent | Evidence |
|-----------|-------|--------|---------------------|----------|
| Execute Expiry | Expired Publications | Publications Removed | YES | CASE-PUB-002, CASE-TG-CORE-001 |
| Execute Update | Updated Publications | Publications Updated | YES | CASE-PUB-002, CASE-TG-CORE-001 |

---

# Operation Flow

```
Interpretation Result
    ↓
Publisher
    ├── Create Publication
    ├── Format Content
    ├── Group by Territory
    └── Execute Lifecycle
    ↓
Publication
    ↓
Adapter (Telegram/Facebook/PWA)
    ↓
Channel
```

---

# Operation Count

| Category | Count | Channel-Independent |
|----------|-------|---------------------|
| Publication | 4 | YES |
| Content | 4 | YES |
| Territorial | 2 | YES |
| Lifecycle | 2 | YES |
| **Total** | **12** | **YES** |

---

# Evidence

| Operation | Source |
|-----------|--------|
| Publication Operations | CASE-PUB-002, CASE-TG-CORE-001 |
| Content Operations | CASE-PUB-002, CASE-TG-CORE-001 |
| Territorial Operations | CASE-PUB-002, CASE-TG-CORE-001 |
| Lifecycle Operations | CASE-PUB-002, CASE-TG-CORE-001 |

---

**End of Operations**
