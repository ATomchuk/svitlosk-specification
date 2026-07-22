# INFPROD001_PRODUCT_ANALYSIS

**Document ID:** CASE-INFPROD-001-PA

**Title:** Product Analysis

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document analyzes every information product in detail.

---

# 2. Product Analysis

## 2.1 Emergency Outage Publication

### Identity

**ID:** Emergency-Outage-{Territory}-{Timestamp}

**Type:** Atomic

**Domain:** C

### Purpose

Inform residents about unexpected electricity outages in their area.

### Lifetime

| Stage | Duration | Trigger |
|-------|----------|---------|
| Created | Instant | DSO publishes emergency |
| Active | Until replaced/archived | — |
| Archived | Permanent | End of reporting period |

### Owner

| Responsibility | Owner |
|----------------|-------|
| Data acquisition | Parser B |
| Publication generation | Publisher |
| Channel delivery | Adapter |

### Update Behaviour

- Triggered by: DSO data change
- Action: Edit existing publication
- Frequency: When data changes

### Expiration Behaviour

- Does NOT expire
- Becomes historical record
- Permanent archive

### Channel Independence

**YES**

Telegram: Text message with address and event.

Facebook: Post with address and event.

Same information, different representation.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- Organized by Territory
- Permanent record

---

## 2.2 Planned Outage Publication (Today)

### Identity

**ID:** Planned-Outage-Today-{Territory}-{Timestamp}

**Type:** Atomic

**Domain:** B

### Purpose

Inform residents about today's planned maintenance.

### Lifetime

| Stage | Duration | Trigger |
|-------|----------|---------|
| Created | Instant | DSO publishes planned outage |
| Active | Until end of day | — |
| Archived | Permanent | End of reporting period |

### Owner

| Responsibility | Owner |
|----------------|-------|
| Data acquisition | Parser B |
| Publication generation | Publisher |
| Channel delivery | Adapter |

### Update Behaviour

- Triggered by: DSO data change
- Action: Edit existing publication
- Frequency: When data changes

### Expiration Behaviour

- Expires at end of current day
- Becomes historical record
- Permanent archive

### Channel Independence

**YES**

Telegram: Text message with address and time.

Facebook: Post with address and time.

Same information, different representation.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- Organized by Territory
- Temporary during day, permanent after

---

## 2.3 Planned Outage Publication (Tomorrow)

### Identity

**ID:** Planned-Outage-Tomorrow-{Territory}-{Timestamp}

**Type:** Atomic

**Domain:** B

### Purpose

Inform residents about tomorrow's planned maintenance.

### Lifetime

| Stage | Duration | Trigger |
|-------|----------|---------|
| Created | Instant | DSO publishes tomorrow's outage |
| Active | Until end of day | — |
| Removed | Instant | End of current day |

### Owner

| Responsibility | Owner |
|----------------|-------|
| Data acquisition | Parser B |
| Publication generation | Publisher |
| Channel delivery | Adapter |

### Update Behaviour

- Triggered by: DSO data change
- Action: Edit existing publication
- Frequency: When data changes

### Expiration Behaviour

- Expires at end of current day
- Disappears automatically
- NOT archived (temporary)

### Channel Independence

**YES**

Telegram: Text message with address and time.

Facebook: Post with address and time.

Same information, different representation.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- Organized by Territory
- TEMPORARY — disappears after current day

---

## 2.4 Queue Graph Publication (Tomorrow)

### Identity

**ID:** Queue-Graph-Tomorrow-{Timestamp}

**Type:** Composite

**Domain:** A

### Purpose

Visualize tomorrow's queue schedule for all 12 subqueues.

### Lifetime

| Stage | Duration | Trigger |
|-------|----------|---------|
| Created | Instant | Tomorrow's schedule available |
| Active | Until new graph or end of day | — |
| Replaced | Instant | New graph data arrives |
| Removed | Instant | End of current day |

### Owner

| Responsibility | Owner |
|----------------|-------|
| Data acquisition | Parser A |
| Graph generation | Publisher/Adapter |
| Channel delivery | Adapter |

### Update Behaviour

- Triggered by: New schedule data
- Action: Replace entire graph
- Frequency: When schedule changes

### Expiration Behaviour

- Expires at end of current day
- Disappears automatically
- NOT archived (temporary)

### Channel Independence

**PARTIALLY**

Telegram: Image format specific to Telegram.

Facebook: Image format specific to Facebook.

Same data, different image format.

### Relationship to Journal Edition

- Included in Journal Edition for current day
- NOT organized by Territory (queue-based)
- TEMPORARY — disappears after current day

---

## 2.5 Technical Publication

### Identity

**ID:** Technical-{Category}-{Timestamp}

**Type:** Atomic

**Domain:** System

### Purpose

Communicate system updates and technical information.

### Lifetime

| Stage | Duration | Trigger |
|-------|----------|---------|
| Created | Instant | Technical update needed |
| Active | Until replaced | — |
| Archived | Permanent | End of reporting period |

### Owner

| Responsibility | Owner |
|----------------|-------|
| Content generation | System |
| Publication formatting | Publisher |
| Channel delivery | Adapter |

### Update Behaviour

- Triggered by: New technical information
- Action: Edit or replace publication
- Frequency: When updates available

### Expiration Behaviour

- Does NOT expire
- May be replaced by newer message
- Permanent archive

### Channel Independence

**YES**

Telegram: Text message.

Facebook: Post.

Same information, different representation.

### Relationship to Journal Edition

- Included in Journal Edition
- NOT organized by Territory
- Permanent record

---

## 2.6 Service Publication (Future)

### Identity

**ID:** Service-{Category}-{Timestamp}

**Type:** Atomic

**Domain:** System

### Purpose

Communicate future project developments.

### Lifetime

| Stage | Duration | Trigger |
|-------|----------|---------|
| Created | Instant | Announcement needed |
| Active | Until replaced | — |
| Archived | Permanent | End of reporting period |

### Owner

| Responsibility | Owner |
|----------------|-------|
| Content generation | System |
| Publication formatting | Publisher |
| Channel delivery | Adapter |

### Update Behaviour

- Triggered by: Announcement change
- Action: Edit or replace publication
- Frequency: When changes occur

### Expiration Behaviour

- Does NOT expire
- May be replaced by newer announcement
- Permanent archive

### Channel Independence

**YES**

Telegram: Text message.

Facebook: Post.

Same information, different representation.

### Relationship to Journal Edition

- Included in Journal Edition
- NOT organized by Territory
- Permanent record

---

# 3. Findings

## 3.1 Finding PA-001

**All products have CLEAR IDENTITY.**

Each product has a unique ID pattern.

**Evidence:** Analysis of product identity.

**Confidence:** HIGH.

## 3.2 Finding PA-002

**All products have DEFINED PURPOSE.**

Each product serves a specific informational need.

**Evidence:** Analysis of product purpose.

**Confidence:** HIGH.

## 3.3 Finding PA-003

**Product lifetimes VARY SIGNIFICANTLY.**

Some are permanent, some are temporary, some disappear.

**Evidence:** Analysis of product lifetime.

**Confidence:** HIGH.

## 3.4 Finding PA-004

**All products are CHANNEL-INDEPENDENT (except Queue Graph).**

Same information, different representation.

**Evidence:** Analysis of channel independence.

**Confidence:** HIGH.

---

# 4. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| PA-001 | Analysis of product identity |
| PA-002 | Analysis of product purpose |
| PA-003 | Analysis of product lifetime |
| PA-004 | Analysis of channel independence |

---

**End of Product Analysis**
