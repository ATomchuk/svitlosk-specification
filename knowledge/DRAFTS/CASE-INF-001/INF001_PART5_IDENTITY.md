# INF001_PART5_IDENTITY

**Document ID:** CASE-INF-001-P5

**Title:** Identity Dimensions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines the identity dimensions of information in SvitloSk.

---

# 2. Identity Dimensions

## 2.1 Time

### Dimension

**Temporal identity** — WHEN information is valid or when it was created.

### Sub-dimensions

| Sub-dimension | Description | Evidence |
|---------------|-------------|----------|
| Reporting Period | The time interval for which information is valid | GLOSSARY §2 |
| Creation Timestamp | When information was created | GLOSSARY §2 |
| Validity Interval | Start and end time of information validity | Architect Intent |
| Hour | Hourly granularity for Queue Schedule | Architect Intent |

### Applicable Information

- Queue Schedule (hourly)
- Planned Outages (validity interval)
- Emergency Outages (creation timestamp)
- Journal Edition (daily)
- Publication (timestamp)

---

## 2.2 Territory

### Dimension

**Spatial identity** — WHERE information applies.

### Sub-dimensions

| Sub-dimension | Description | Evidence |
|---------------|-------------|----------|
| Community | Top-level territorial unit | TERRITORIAL_MODEL |
| Administrative Centre | Principal territorial unit | TERRITORIAL_MODEL |
| Starosta District | Territorial subdivision | TERRITORIAL_MODEL |
| Settlement | Populated place | TERRITORIAL_MODEL |
| Street | Official street or lane | TERRITORIAL_MODEL |
| Address | Smallest territorial unit | TERRITORIAL_MODEL |

### Applicable Information

- Planned Outages (address-based)
- Emergency Outages (address-based)
- Journal Edition (organized by territory)
- Publication (territory reference)

---

## 2.3 Queue

### Dimension

**Queue identity** — WHICH queue information applies to.

### Sub-dimensions

| Sub-dimension | Description | Evidence |
|---------------|-------------|----------|
| Queue Number | Official queue identifier (1-6) | GLOSSARY §5, Architect Intent |
| Subqueue Number | Official subqueue identifier (1.1-6.2) | GLOSSARY §5, Architect Intent |

### Applicable Information

- Queue Schedule
- Queue Information
- Subqueue Information
- Schedule Information
- Tomorrow Queue Graph

---

## 2.4 Source

### Dimension

**Source identity** — WHERE information came from.

### Sub-dimensions

| Sub-dimension | Description | Evidence |
|---------------|-------------|----------|
| Data Source | Official organization publishing Open Data | GLOSSARY §2 |
| DSO | Distribution System Operator | GLOSSARY §2 |
| Processing Cycle | When information was processed | GLOSSARY §2 |

### Applicable Information

- All information (traceability requirement)

---

## 2.5 Domain

### Dimension

**Domain identity** — WHICH information domain information belongs to.

### Sub-dimensions

| Sub-dimension | Description | Evidence |
|---------------|-------------|----------|
| Domain A | Queue Schedule | Architect Intent |
| Domain B | Planned Outages | Architect Intent |
| Domain C | Emergency Outages | Architect Intent |

### Applicable Information

- All information (domain classification)

---

## 2.6 Validity

### Dimension

**Validity identity** — WHETHER information is currently valid.

### Sub-dimensions

| Sub-dimension | Description | Evidence |
|---------------|-------------|----------|
| Active | Information is currently valid | Architect Intent |
| Expired | Information is no longer valid | Architect Intent |
| Temporary | Information will expire | Architect Intent |

### Applicable Information

- Tomorrow's planned outages (temporary)
- Tomorrow's queue graph (temporary)
- Current day's planned outages (active → expired)

---

# 3. Identity Matrix

| Information | Time | Territory | Queue | Source | Domain | Validity |
|-------------|------|-----------|-------|--------|--------|----------|
| Queue Schedule | YES | — | YES | YES | A | Active |
| Tomorrow Queue Graph | YES | — | YES | YES | A | Temporary |
| Planned Outages | YES | YES | — | YES | B | Temporary |
| Emergency Outages | YES | YES | — | YES | C | Active |
| Territory Information | — | YES | — | YES | — | Canonical |
| Journal Edition | YES | YES | — | YES | All | Active |
| Publication | YES | YES | — | YES | All | Active |

---

# 4. Findings

## 4.1 Finding ID-001

**There are SIX identity dimensions.**

Time, Territory, Queue, Source, Domain, Validity.

**Evidence:** Analysis of information characteristics.

**Confidence:** HIGH.

## 4.2 Finding ID-002

**Time has SIX sub-dimensions.**

Reporting Period, Creation Timestamp, Validity Interval, Hour, Date, Timestamp.

**Evidence:** GLOSSARY §2, Architect Intent.

**Confidence:** HIGH.

## 4.3 Finding ID-003

**Territory has SIX sub-dimensions.**

Community, Administrative Centre, Starosta District, Settlement, Street, Address.

**Evidence:** TERRITORIAL_MODEL.

**Confidence:** HIGH.

## 4.4 Finding ID-004

**Queue has TWO sub-dimensions.**

Queue Number (1-6), Subqueue Number (1.1-6.2).

**Evidence:** GLOSSARY §5, Architect Intent.

**Confidence:** HIGH.

## 4.5 Finding ID-005

**Different information types have different identity dimensions.**

Queue Schedule uses Queue identity.

Planned/Emergency Outages use Territory identity.

All use Time and Source identity.

**Evidence:** Analysis of information characteristics.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| ID-001 | Analysis of information characteristics |
| ID-002 | GLOSSARY §2, Architect Intent |
| ID-003 | TERRITORIAL_MODEL |
| ID-004 | GLOSSARY §5, Architect Intent |
| ID-005 | Analysis of information characteristics |

---

**End of Identity Dimensions**
