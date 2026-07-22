# SYS001_COUPLINGS

**Document ID:** CASE-SYS-001-CPL

**Title:** Hidden Couplings

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document identifies hidden couplings — places where two concepts appear independent but are actually tightly coupled.

---

# 2. Hidden Couplings

## 2.1 COUPLING-001: Parser A and PWA

### Appearance

Parser A produces Queue Schedule.

PWA displays Queue Schedule.

They appear independent.

### Reality

PWA DEPENDS on Parser A for its primary data.

If Parser A fails, PWA has nothing to display.

### Coupling Type

DATA DEPENDENCY.

### Severity

HIGH — PWA cannot function without Parser A.

---

## 2.2 COUPLING-002: Parser B and Journal

### Appearance

Parser B produces Planned and Emergency Outages.

Journal publishes Planned and Emergency Outages.

They appear independent.

### Reality

Journal DEPENDS on Parser B for Domains B and C content.

If Parser B fails, Journal has no outage content.

### Coupling Type

DATA DEPENDENCY.

### Severity

HIGH — Journal cannot publish outage content without Parser B.

---

## 2.3 COUPLING-003: Publisher and Journal

### Appearance

Publisher is a common subsystem.

Journal is a publication service.

They appear independent.

### Reality

Journal USES Publisher for publication.

Publisher IMPLEMENTS Journal publication.

### Coupling Type

SERVICE DEPENDENCY.

### Severity

MEDIUM — Journal depends on Publisher, but Publisher could serve other consumers.

---

## 2.4 COUPLING-004: Adapters and Publisher

### Appearance

Adapters are channel-specific.

Publisher is channel-independent.

They appear independent.

### Reality

Adapters RECEIVE publications from Publisher.

Publisher SENDS publications to Adapters.

### Coupling Type

INTERFACE DEPENDENCY.

### Severity

MEDIUM — Adapters depend on Publisher's output format.

---

## 2.5 COUPLING-005: Queue Schedule and Push Notifications

### Appearance

Queue Schedule is information.

Push Notifications are delivery mechanism.

They appear independent.

### Reality

Push Notifications BELONG ONLY to Queue Schedule.

They are COUPLED by domain.

### Coupling Type

DOMAIN DEPENDENCY.

### Severity

LOW — intentional coupling, not hidden.

---

## 2.6 COUPLING-006: Territory and Journal

### Appearance

Territory is reference data.

Journal is publication service.

They appear independent.

### Reality

Journal ORGANIZES publications by Territory.

Territory DEFINES Journal structure.

### Coupling Type

STRUCTURAL DEPENDENCY.

### Severity

MEDIUM — Journal cannot organize without Territory.

---

# 3. Coupling Matrix

| Coupling | Components | Type | Severity |
|----------|------------|------|----------|
| COUPLING-001 | Parser A ↔ PWA | Data | HIGH |
| COUPLING-002 | Parser B ↔ Journal | Data | HIGH |
| COUPLING-003 | Publisher ↔ Journal | Service | MEDIUM |
| COUPLING-004 | Adapters ↔ Publisher | Interface | MEDIUM |
| COUPLING-005 | Queue Schedule ↔ Notifications | Domain | LOW |
| COUPLING-006 | Territory ↔ Journal | Structural | MEDIUM |

---

# 4. Findings

## 4.1 Finding CPL-001

**Six hidden couplings were identified.**

Two are HIGH severity, three are MEDIUM, one is LOW.

**Evidence:** Analysis of system relationships.

**Confidence:** HIGH.

## 4.2 Finding CPL-002

**The most critical couplings are DATA DEPENDENCIES.**

PWA depends on Parser A.

Journal depends on Parser B.

**Evidence:** Analysis of system relationships.

**Confidence:** HIGH.

## 4.3 Finding CPL-003

**Some couplings are INTENTIONAL.**

Queue Schedule ↔ Notifications is an intentional domain coupling.

**Evidence:** Architect Intent.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| CPL-001 | Analysis of system relationships |
| CPL-002 | Analysis of system relationships |
| CPL-003 | Architect Intent |

---

**End of Hidden Couplings**
