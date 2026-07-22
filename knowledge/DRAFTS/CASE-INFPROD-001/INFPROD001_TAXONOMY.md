# INFPROD001_TAXONOMY

**Document ID:** CASE-INFPROD-001-TX

**Title:** Product Taxonomy

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs the product taxonomy.

---

# 2. Product Taxonomy

## 2.1 By Domain

```
Information Products
    │
    ├── Domain A: Queue Schedule
    │   └── Queue Graph Publication (Tomorrow)
    │
    ├── Domain B: Planned Outages
    │   ├── Planned Outage Publication (Today)
    │   └── Planned Outage Publication (Tomorrow)
    │
    ├── Domain C: Emergency Outages
    │   └── Emergency Outage Publication
    │
    └── Domain D: System
        ├── Technical Publication
        └── Service Publication (Future)
```

---

## 2.2 By Atomicity

```
Information Products
    │
    ├── Atomic Products
    │   ├── Emergency Outage Publication
    │   ├── Planned Outage Publication (Today)
    │   ├── Planned Outage Publication (Tomorrow)
    │   ├── Technical Publication
    │   └── Service Publication (Future)
    │
    └── Composite Products
        └── Queue Graph Publication (Tomorrow)
```

---

## 2.3 By Persistence

```
Information Products
    │
    ├── Permanent Products
    │   ├── Emergency Outage Publication
    │   ├── Technical Publication
    │   └── Service Publication (Future)
    │
    ├── Temporary Products (expire end of day)
    │   ├── Planned Outage Publication (Today)
    │   └── Queue Graph Publication (Tomorrow)
    │
    └── Transient Products (disappear end of day)
        └── Planned Outage Publication (Tomorrow)
```

---

## 2.4 By Channel Independence

```
Information Products
    │
    ├── Channel-Independent Products
    │   ├── Emergency Outage Publication
    │   ├── Planned Outage Publication (Today)
    │   ├── Planned Outage Publication (Tomorrow)
    │   ├── Technical Publication
    │   └── Service Publication (Future)
    │
    └── Partially Channel-Independent Products
        └── Queue Graph Publication (Tomorrow)
```

---

## 2.5 By Territory Organization

```
Information Products
    │
    ├── Territory-Organized Products
    │   ├── Emergency Outage Publication
    │   ├── Planned Outage Publication (Today)
    │   └── Planned Outage Publication (Tomorrow)
    │
    └── Non-Territory-Organized Products
        ├── Queue Graph Publication (Tomorrow)
        ├── Technical Publication
        └── Service Publication (Future)
```

---

# 3. Taxonomy Summary

| Classification | Categories | Products |
|----------------|------------|----------|
| By Domain | 4 | Queue, Planned, Emergency, System |
| By Atomicity | 2 | Atomic (5), Composite (1) |
| By Persistence | 3 | Permanent (3), Temporary (1), Transient (1) |
| By Channel Independence | 2 | Channel-Independent (5), Partial (1) |
| By Territory Organization | 2 | Territory-Organized (3), Non-Territory (3) |

---

# 4. Findings

## 4.1 Finding TX-001

**Products can be classified by 5 dimensions.**

Domain, Atomicity, Persistence, Channel Independence, Territory Organization.

**Evidence:** Analysis of product characteristics.

**Confidence:** HIGH.

## 4.2 Finding TX-002

**Most products are ATOMIC and CHANNEL-INDEPENDENT.**

5 out of 6 products.

**Evidence:** Analysis of taxonomy.

**Confidence:** HIGH.

## 4.3 Finding TX-003

**Only Queue Graph is COMPOSITE and PARTIALLY channel-independent.**

**Evidence:** Analysis of taxonomy.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| TX-001 | Analysis of product characteristics |
| TX-002 | Analysis of taxonomy |
| TX-003 | Analysis of taxonomy |

---

**End of Product Taxonomy**
