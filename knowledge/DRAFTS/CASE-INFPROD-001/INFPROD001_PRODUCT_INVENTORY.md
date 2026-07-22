# INFPROD001_PRODUCT_INVENTORY

**Document ID:** CASE-INFPROD-001-PI

**Title:** Information Product Inventory

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies every information product produced by SvitloSk.

---

# 2. Information Products

## 2.1 Emergency Outage Publication

### Identity

**Name:** Emergency Outage Publication

**Domain:** C — Emergency Outages

**Evidence:** Architect Intent, GLOSSARY §5

### Purpose

To inform residents about unexpected electricity outages.

### Content

- Address (Settlement, Street, House)
- Emergency event description
- Source (DSO)

### Lifetime

- Created: When emergency outage is published by DSO
- Active: Until replaced or archived
- Archived: Permanently

### Owner

- Parser B (acquires data)
- Publisher (generates publication)
- Telegram/Facebook Adapter (delivers)

### Update Behaviour

- Updated when emergency outage information changes
- May be replaced if structure changes significantly

### Expiration Behaviour

- Does NOT expire (permanent record)

### Channel Independence

**YES** — same information for Telegram and Facebook.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- Organized by Territory

---

## 2.2 Planned Outage Publication (Today)

### Identity

**Name:** Planned Outage Publication (Today)

**Domain:** B — Planned Outages

**Evidence:** Architect Intent, GLOSSARY §5

### Purpose

To inform residents about today's planned maintenance.

### Content

- Address (Settlement, Street, House)
- Planned time interval
- Source (DSO)

### Lifetime

- Created: When planned outage is published by DSO
- Active: Until end of current day
- Archived: Permanently

### Owner

- Parser B (acquires data)
- Publisher (generates publication)
- Telegram/Facebook Adapter (delivers)

### Update Behaviour

- Updated when planned outage information changes
- May be replaced if structure changes significantly

### Expiration Behaviour

- Expires at end of current day
- Becomes historical record

### Channel Independence

**YES** — same information for Telegram and Facebook.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- Organized by Territory

---

## 2.3 Planned Outage Publication (Tomorrow)

### Identity

**Name:** Planned Outage Publication (Tomorrow)

**Domain:** B — Planned Outages

**Evidence:** Architect Intent, GLOSSARY §3

### Purpose

To inform residents about tomorrow's planned maintenance.

### Content

- Address (Settlement, Street, House)
- Planned time interval
- Source (DSO)

### Lifetime

- Created: When tomorrow's planned outage is published by DSO
- Active: Until end of current day
- Removed: When current day ends

### Owner

- Parser B (acquires data)
- Publisher (generates publication)
- Telegram/Facebook Adapter (delivers)

### Update Behaviour

- Updated when tomorrow's planned outage information changes
- May be replaced if structure changes significantly

### Expiration Behaviour

- Expires at end of current day
- Disappears automatically

### Channel Independence

**YES** — same information for Telegram and Facebook.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- Organized by Territory
- TEMPORARY — disappears after current day

---

## 2.4 Queue Graph Publication (Tomorrow)

### Identity

**Name:** Queue Graph Publication (Tomorrow)

**Domain:** A — Queue Schedule

**Evidence:** Architect Intent

### Purpose

To visualize tomorrow's queue schedule.

### Content

- Visual graph of 12 subqueues
- Tomorrow's date
- Planned availability

### Lifetime

- Created: When tomorrow's queue schedule is available
- Active: Until end of current day
- Replaced: When new graph is generated
- Removed: When current day ends

### Owner

- Parser A (acquires data)
- Publisher (coordinates generation)
- Telegram/Facebook Adapter (delivers)

### Update Behaviour

- Replaced when new graph data arrives
- May be updated if schedule changes

### Expiration Behaviour

- Expires at end of current day
- Disappears automatically

### Channel Independence

**PARTIALLY** — graph format may differ between channels.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- NOT organized by Territory (queue-based)

---

## 2.5 Technical Publication

### Identity

**Name:** Technical Publication

**Domain:** System

**Evidence:** Architect Intent

### Purpose

To communicate system updates and technical information.

### Content

- Technical message content
- Timestamp
- Category

### Lifetime

- Created: When technical update is needed
- Active: Until replaced by newer message
- Archived: Permanently

### Owner

- System (generates content)
- Publisher (formats and distributes)
- Telegram/Facebook Adapter (delivers)

### Update Behaviour

- Updated when new technical information is available
- Previous message may be edited or replaced

### Expiration Behaviour

- Does NOT expire (permanent record)
- May be replaced by newer message

### Channel Independence

**YES** — same information for Telegram and Facebook.

### Relationship to Journal Edition

- Included in Journal Edition
- NOT organized by Territory

---

## 2.6 Service Publication (Future)

### Identity

**Name:** Service Publication (Future)

**Domain:** System

**Evidence:** Architect Intent — "future project announcements"

### Purpose

To communicate future project developments.

### Content

- Announcement content
- Timestamp
- Category

### Lifetime

- Created: When future announcement is needed
- Active: Until replaced or archived
- Archived: Permanently

### Owner

- System (generates content)
- Publisher (formats and distributes)
- Telegram/Facebook Adapter (delivers)

### Update Behaviour

- Updated when announcement changes
- May be replaced if content changes significantly

### Expiration Behaviour

- Does NOT expire (permanent record)

### Channel Independence

**YES** — same information for Telegram and Facebook.

### Relationship to Journal Edition

- Included in Journal Edition
- NOT organized by Territory

---

# 3. Product Inventory Summary

| Product | Domain | Atomic? | Temporary? | Channel-Independent? | For Facebook? |
|---------|--------|---------|------------|---------------------|---------------|
| Emergency Outage Publication | C | YES | NO | YES | YES |
| Planned Outage Publication (Today) | B | YES | YES (expires end of day) | YES | YES |
| Planned Outage Publication (Tomorrow) | B | YES | YES (disappears end of day) | YES | YES |
| Queue Graph Publication (Tomorrow) | A | NO (composite) | YES (disappears end of day) | PARTIALLY | YES |
| Technical Publication | System | YES | NO | YES | YES |
| Service Publication (Future) | System | YES | NO | YES | YES |

---

# 4. Findings

## 4.1 Finding PI-001

**There are 6 information products.**

Across 3 domains: Emergency Outages, Planned Outages, Queue Schedule, System.

**Evidence:** Analysis of Architect Intent, GLOSSARY.

**Confidence:** HIGH.

## 4.2 Finding PI-002

**5 products are atomic.**

Emergency Outage, Planned Outage (Today), Planned Outage (Tomorrow), Technical, Service.

**Evidence:** Analysis of product characteristics.

**Confidence:** HIGH.

## 4.3 Finding PI-003

**1 product is composite.**

Queue Graph Publication ( Tomorrow) contains multiple subqueue graphs.

**Evidence:** Analysis of product characteristics.

**Confidence:** HIGH.

## 4.4 Finding PI-004

**3 products are temporary.**

Planned Outage (Today), Planned Outage (Tomorrow), Queue Graph (Tomorrow).

**Evidence:** Analysis of product characteristics.

**Confidence:** HIGH.

## 4.5 Finding PI-005

**5 products are channel-independent.**

Emergency Outage, Planned Outage (Today), Planned Outage (Tomorrow), Technical, Service.

**Evidence:** Analysis of product characteristics.

**Confidence:** HIGH.

## 4.6 Finding PI-006

**All 6 products will exist for Facebook.**

**Evidence:** Analysis of product characteristics.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| PI-001 | Architect Intent, GLOSSARY |
| PI-002 | Analysis of product characteristics |
| PI-003 | Analysis of product characteristics |
| PI-004 | Analysis of product characteristics |
| PI-005 | Analysis of product characteristics |
| PI-006 | Analysis of product characteristics |

---

**End of Information Product Inventory**
