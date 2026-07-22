# SYS001_BOUNDARIES

**Document ID:** CASE-SYS-001-BND

**Title:** System Boundaries

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies ALL boundaries in the system.

---

# 2. System Boundaries

## 2.1 Information Boundary

### Definition

The boundary between EXTERNAL information (from DSO) and INTERNAL information (managed by SvitloSk).

### Location

At the Parser input.

### Objects Crossing

| Direction | Object |
|-----------|--------|
| In | Official Queue Schedule |
| In | Official Planned Outages |
| In | Official Emergency Outages |

### Rule

SvitloSk SHALL NOT modify the factual meaning of information crossing this boundary.

**Evidence:** CHARTER §7, §8.

---

## 2.2 Parsing Boundary

### Definition

The boundary between raw external data and normalized internal data.

### Location

At the Parser output.

### Objects Crossing

| Direction | Object |
|-----------|--------|
| In | Official data (raw) |
| Out | Queue Schedule Information |
| Out | Planned Outage Information |
| Out | Emergency Outage Information |

### Rule

Parsed data SHALL correspond exactly to retrieved Open Data.

**Evidence:** GLOSSARY §2.

---

## 2.3 Interpretation Boundary

### Definition

The boundary between normalized data and interpreted information (knowledge).

### Location

Between Parser output and Publisher input.

### Objects Crossing

| Direction | Object |
|-----------|--------|
| In | Parsed Data |
| Out | Interpretation Result |

### Rule

Interpretation SHALL improve readability without changing factual meaning.

**Evidence:** GLOSSARY §2.

---

## 2.4 Publication Boundary

### Definition

The boundary between internal information and prepared publications.

### Location

At the Publisher output.

### Objects Crossing

| Direction | Object |
|-----------|--------|
| In | Interpretation Result |
| Out | Publication |

### Rule

Publications SHALL be derived exclusively from Interpretation Results.

**Evidence:** GLOSSARY §3.

---

## 2.5 Presentation Boundary

### Definition

The boundary between publications and channel-specific representations.

### Location

At the Adapter input/output.

### Objects Crossing

| Direction | Object |
|-----------|--------|
| In | Publication |
| Out | Telegram Post |
| Out | Facebook Post |
| Out | PWA Display |

### Rule

Representations SHALL preserve the factual meaning of publications.

**Evidence:** GLOSSARY §3.

---

## 2.6 Storage Boundary

### Definition

The boundary between active information and archived information.

### Location

At the Archive input.

### Objects Crossing

| Direction | Object |
|-----------|--------|
| In | Information, Publications |
| Out | Historical Records |

### Rule

Archived datasets SHALL remain immutable.

**Evidence:** DATA_MODEL.md.

---

## 2.7 Community Boundary

### Definition

The boundary between SvitloSk and the Starokostiantyniv Community.

### Location

At the Channel output.

### Objects Crossing

| Direction | Object |
|-----------|--------|
| Out | Publications, Representations |
| In | Resident interactions (PWA) |

### Rule

SvitloSk serves the Starokostiantyniv Community.

**Evidence:** CHARTER §5.

---

## 2.8 Domain Boundaries

### Definition

The boundaries between the three independent information domains.

### Location

Conceptual separation between Domain A, B, and C.

### Rule

Queue Schedule, Planned Outages, and Emergency Outages are THREE DIFFERENT ONTOLOGICAL OBJECTS. Never merge them.

**Evidence:** Architect Intent.

---

# 3. Boundary Matrix

| Boundary | Location | Objects Crossing | Rule |
|----------|----------|------------------|------|
| Information | Parser Input | External data | No modification |
| Parsing | Parser Output | Raw → Normalized | Exact correspondence |
| Interpretation | Parser → Publisher | Data → Knowledge | No factual change |
| Publication | Publisher Output | Knowledge → Publication | Derived from Interpretation |
| Presentation | Adapter | Publication → Representation | Preserve meaning |
| Storage | Archive Input | Active → Archived | Immutable |
| Community | Channel Output | System → Residents | Service delivery |
| Domain | Conceptual | A, B, C separation | Never merge |

---

# 4. Findings

## 4.1 Finding BND-001

**There are 8 system boundaries.**

Information, Parsing, Interpretation, Publication, Presentation, Storage, Community, Domain.

**Evidence:** Analysis of system structure.

**Confidence:** HIGH.

## 4.2 Finding BND-002

**Each boundary has a SPECIFIC RULE.**

The rules protect information integrity across boundaries.

**Evidence:** CHARTER, GLOSSARY, DATA_MODEL.

**Confidence:** HIGH.

## 4.3 Finding BND-003

**The Information Boundary is the most critical.**

It protects external data from modification by SvitloSk.

**Evidence:** CHARTER §7, §8.

**Confidence:** HIGH.

## 4.4 Finding BND-004

**Domain Boundaries are conceptual, not physical.**

They separate information domains without physical barriers.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| BND-001 | Analysis of system structure |
| BND-002 | CHARTER, GLOSSARY, DATA_MODEL |
| BND-003 | CHARTER §7, §8 |
| BND-004 | Architect Intent |

---

**End of System Boundaries**
