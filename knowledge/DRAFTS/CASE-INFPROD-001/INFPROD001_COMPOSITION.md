# INFPROD001_COMPOSITION

**Document ID:** CASE-INFPROD-001-CM

**Title:** Product Composition Model

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs the product composition model.

---

# 2. Product Composition

## 2.1 Journal Edition Composition

### Definition

A Journal Edition is the CONTAINER for all products for one day.

### Composition

```
Journal Edition
    │
    ├── Emergency Outage Publications (per Territory)
    │   ├── Emergency Outage Publication (Territory 1)
    │   ├── Emergency Outage Publication (Territory 2)
    │   └── ...
    │
    ├── Planned Outage Publications (Today, per Territory)
    │   ├── Planned Outage Publication Today (Territory 1)
    │   ├── Planned Outage Publication Today (Territory 2)
    │   └── ...
    │
    ├── Planned Outage Publications (Tomorrow, per Territory)
    │   ├── Planned Outage Publication Tomorrow (Territory 1)
    │   ├── Planned Outage Publication Tomorrow (Territory 2)
    │   └── ...
    │
    ├── Queue Graph Publication (Tomorrow)
    │   └── Queue Graph (single, not per Territory)
    │
    ├── Technical Publication(s)
    │   ├── Technical Publication 1
    │   └── ...
    │
    └── Service Publication(s)
        ├── Service Publication 1
        └── ...
```

---

## 2.2 Product Composition Rules

### Rule 1: Territory-Based Products

Emergency Outage, Planned Outage (Today), Planned Outage (Tomorrow) are organized by Territory.

Each Territory has its OWN publication.

### Rule 2: Queue-Based Products

Queue Graph is NOT organized by Territory.

It is a SINGLE product for all Territories.

### Rule 3: System Products

Technical and Service Publications are NOT organized by Territory.

They are SYSTEM-WIDE products.

### Rule 4: Temporary Products

Planned Outage (Tomorrow) and Queue Graph (Tomorrow) are TEMPORARY.

They disappear at end of current day.

---

## 2.3 Composition Matrix

| Product | Per Territory? | Temporary? | Count per Day |
|---------|----------------|------------|---------------|
| Emergency Outage | YES | NO | 1 per Territory with outages |
| Planned Outage (Today) | YES | YES | 1 per Territory with outages |
| Planned Outage (Tomorrow) | YES | YES | 1 per Territory with outages |
| Queue Graph (Tomorrow) | NO | YES | 1 total |
| Technical | NO | NO | 0 or more |
| Service (Future) | NO | NO | 0 or more |

---

# 3. Composition Example

## 3.1 Example: Starokostiantyniv Community

### Territories

- Administrative Centre
- SO 1
- SO 2
- SO 3
- SO 4
- SO 5
- SO 6

### Journal Edition Composition

```
Journal Edition (2026-07-22)
    │
    ├── Emergency Outages
    │   ├── Emergency Outage (Administrative Centre)
    │   ├── Emergency Outage (SO 2)
    │   └── Emergency Outage (SO 5)
    │
    ├── Planned Outages (Today)
    │   ├── Planned Outage Today (Administrative Centre)
    │   ├── Planned Outage Today (SO 1)
    │   ├── Planned Outage Today (SO 3)
    │   └── Planned Outage Today (SO 6)
    │
    ├── Planned Outages (Tomorrow)
    │   ├── Planned Outage Tomorrow (Administrative Centre)
    │   └── Planned Outage Tomorrow (SO 4)
    │
    ├── Queue Graph (Tomorrow)
    │   └── Queue Graph (12 subqueues)
    │
    ├── Technical Publication
    │   └── "System maintenance scheduled for 2026-07-23"
    │
    └── Service Publication
        └── "New feature coming soon"
```

---

# 4. Findings

## 4.1 Finding CM-001

**Journal Edition is the COMPOSITION ROOT.**

All products are composed within Journal Edition.

**Evidence:** Analysis of product composition.

**Confidence:** HIGH.

## 4.2 Finding CM-002

**Products are organized by 3 patterns.**

Territory-based, Queue-based, System-wide.

**Evidence:** Analysis of composition rules.

**Confidence:** HIGH.

## 4.3 Finding CM-003

**Composition is DYNAMIC.**

Number of products varies based on available data.

**Evidence:** Analysis of composition matrix.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| CM-001 | Analysis of product composition |
| CM-002 | Analysis of composition rules |
| CM-003 | Analysis of composition matrix |

---

**End of Product Composition Model**
