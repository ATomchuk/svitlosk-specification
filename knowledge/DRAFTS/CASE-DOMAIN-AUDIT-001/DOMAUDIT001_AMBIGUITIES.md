# Ambiguities

**Document Class:** Domain Completeness Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document identifies ambiguities in the domain model.

---

# Ambiguities

## AMBIGUITY-001: Journal vs Journal Edition

### Ambiguity

Journal and Journal Edition may be confused.

### Evidence

- Journal is the SERVICE
- Journal Edition is the PRODUCT

### Resolution

Journal is the ONGOING service.

Journal Edition is the DAILY instance.

---

## AMBIGUITY-002: Publication vs Information Product

### Ambiguity

Publication and Information Product may be confused.

### Evidence

- Publication is the ATOMIC UNIT
- Information Product is the SPECIALIZATION

### Resolution

Publication is the atomic unit.

Information Product is a type of Publication.

---

## AMBIGUITY-003: Issue vs Journal Edition

### Ambiguity

Issue and Journal Edition may be synonymous.

### Evidence

- Issue is defined in Telegram context
- Journal Edition is channel-independent

### Resolution

Issue is Telegram-specific.

Journal Edition is channel-independent.

---

## AMBIGUITY-004: Release vs Journal Edition

### Ambiguity

Release and Journal Edition may be synonymous.

### Evidence

- Release is used in CASE-PUB-001
- Journal Edition is used in CASE-JRN-001

### Resolution

Release is not defined in canonical documents.

Journal Edition is the canonical term.

---

## AMBIGUITY-005: Schedule vs Queue Schedule

### Ambiguity

Schedule and Queue Schedule may be confused.

### Evidence

- Schedule is the general concept
- Queue Schedule is the specific implementation

### Resolution

Schedule is the general concept.

Queue Schedule is the specific implementation for Domain A.

---

## AMBIGUITY-006: Graph Publication vs Queue Graph Publication

### Ambiguity

Graph Publication and Queue Graph Publication may be confused.

### Evidence

- Graph Publication is the general concept
- Queue Graph Publication is the specific implementation

### Resolution

Graph Publication is the general concept.

Queue Graph Publication is the specific implementation for Domain A.

---

## AMBIGUITY-007: Text Publication vs Emergency/Planned Publication

### Ambiguity

Text Publication and Emergency/Planned Publication may be confused.

### Evidence

- Text Publication is the general concept
- Emergency/Planned Publication are specific implementations

### Resolution

Text Publication is the general concept.

Emergency/Planned Publication are specific implementations.

---

## AMBIGUITY-008: Technical Publication vs Service Publication

### Ambiguity

Technical Publication and Service Publication may be confused.

### Evidence

- Technical Publication is for system updates
- Service Publication is for future project announcements

### Resolution

Technical Publication is for CURRENT system updates.

Service Publication is for FUTURE project announcements.

---

# Ambiguity Summary

| Ambiguity | Resolution |
|-----------|------------|
| Journal vs Journal Edition | Journal = service, Journal Edition = daily instance |
| Publication vs Information Product | Publication = atomic unit, Information Product = specialization |
| Issue vs Journal Edition | Issue = Telegram-specific, Journal Edition = channel-independent |
| Release vs Journal Edition | Release = undefined, Journal Edition = canonical |
| Schedule vs Queue Schedule | Schedule = general, Queue Schedule = specific |
| Graph Publication vs Queue Graph Publication | Graph Publication = general, Queue Graph Publication = specific |
| Text Publication vs Emergency/Planned | Text Publication = general, Emergency/Planned = specific |
| Technical vs Service Publication | Technical = current updates, Service = future announcements |

---

# Traceability

| Ambiguity | Source |
|-----------|--------|
| All ambiguities | Analysis of entity inventory and domain knowledge |

---

**End of Ambiguities**
