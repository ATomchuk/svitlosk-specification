# INFPROD001_IDENTITY

**Document ID:** CASE-INFPROD-001-ID

**Title:** Product Identity Model

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document constructs the product identity model.

---

# 2. Identity Dimensions

## 2.1 Product Type

### Definition

The category of information product.

### Values

- Emergency Outage Publication
- Planned Outage Publication (Today)
- Planned Outage Publication (Tomorrow)
- Queue Graph Publication (Tomorrow)
- Technical Publication
- Service Publication (Future)

### Evidence

Analysis of product inventory.

---

## 2.2 Territory

### Definition

The geographic area the product covers.

### Values

- Administrative Centre
- Starosta District (SO)

### Evidence

TERRITORIAL_MODEL, Architect Intent.

### Applicable Products

- Emergency Outage Publication
- Planned Outage Publication (Today)
- Planned Outage Publication (Tomorrow)

### Not Applicable

- Queue Graph Publication (Tomorrow) — queue-based, not territory-based
- Technical Publication — system-wide
- Service Publication (Future) — system-wide

---

## 2.3 Reporting Period

### Definition

The time interval the product covers.

### Values

- Current day
- Tomorrow
- System-wide (not time-specific)

### Evidence

GLOSSARY §2.

### Applicable Products

- All products

---

## 2.4 Source Timestamp

### Definition

When the product was created or last updated.

### Values

- ISO 8601 timestamp

### Evidence

GLOSSARY §2.

### Applicable Products

- All products

---

## 2.5 Content Hash

### Definition

Hash of the product content for change detection.

### Values

- SHA-256 hash

### Evidence

Change detection requirement.

### Applicable Products

- All products

---

# 3. Identity Patterns

## 3.1 Emergency Outage Publication

```
Emergency-Outage-{Territory}-{ReportingPeriod}-{SourceTimestamp}
```

## 3.2 Planned Outage Publication (Today)

```
Planned-Outage-Today-{Territory}-{ReportingPeriod}-{SourceTimestamp}
```

## 3.3 Planned Outage Publication (Tomorrow)

```
Planned-Outage-Tomorrow-{Territory}-{ReportingPeriod}-{SourceTimestamp}
```

## 3.4 Queue Graph Publication (Tomorrow)

```
Queue-Graph-Tomorrow-{ReportingPeriod}-{SourceTimestamp}
```

## 3.5 Technical Publication

```
Technical-{Category}-{ReportingPeriod}-{SourceTimestamp}
```

## 3.6 Service Publication (Future)

```
Service-{Category}-{ReportingPeriod}-{SourceTimestamp}
```

---

# 4. Identity Matrix

| Product | Type | Territory | Reporting Period | Timestamp | Hash |
|---------|------|-----------|------------------|-----------|------|
| Emergency Outage | YES | YES | Current day | YES | YES |
| Planned Outage (Today) | YES | YES | Current day | YES | YES |
| Planned Outage (Tomorrow) | YES | YES | Tomorrow | YES | YES |
| Queue Graph (Tomorrow) | YES | NO | Tomorrow | YES | YES |
| Technical | YES | NO | System | YES | YES |
| Service (Future) | YES | NO | System | YES | YES |

---

# 5. Findings

## 5.1 Finding ID-001

**All products have COMPOSITE identity.**

Type + Territory (optional) + Reporting Period + Timestamp + Hash.

**Evidence:** Analysis of identity patterns.

**Confidence:** HIGH.

## 5.2 Finding ID-002

**Territory is OPTIONAL for some products.**

Queue Graph, Technical, Service are not territory-organized.

**Evidence:** Analysis of identity matrix.

**Confidence:** HIGH.

## 5.3 Finding ID-003

**Content Hash enables CHANGE DETECTION.**

Same content = same hash = no update needed.

**Evidence:** Analysis of identity model.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| ID-001 | Analysis of identity patterns |
| ID-002 | Analysis of identity matrix |
| ID-003 | Analysis of identity model |

---

**End of Product Identity Model**
