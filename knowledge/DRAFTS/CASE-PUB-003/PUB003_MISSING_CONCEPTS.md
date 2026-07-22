# PUB003_MISSING_CONCEPTS

**Document ID:** CASE-PUB-003-MC

**Title:** Missing Concepts

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document finds missing concepts that repeatedly appear but have no stable name.

---

# 2. Missing Concepts

## 2.1 MC-001: Information Change

### What It Would Be

The event when information changes.

### Evidence

> "Publications MAY be updated only when the normalized dataset changes." (TELEGRAM_PUBLICATION_LIFECYCLE.md)

### Current Term

"Data change" or "information change" — used informally.

### Status

MISSING — no stable name.

---

## 2.2 MC-002: Publication Change

### What It Would Be

The event when a publication is modified.

### Evidence

> "Updates SHALL be performed by editing the existing Telegram message." (TELEGRAM_PUBLICATION_LIFECYCLE.md)

### Current Term

"Update" — used informally.

### Status

MISSING — no stable name.

---

## 2.3 MC-003: Representation Change

### What It Would Be

The event when a channel-specific output changes.

### Evidence

> "Telegram and Facebook DO NOT own information." (Architect Intent)

### Current Term

No term used.

### Status

MISSING — no stable name.

---

## 2.4 MC-004: Publication Identity

### What It Would Be

The unique identifier for a publication.

### Evidence

> CASE-INFPROD-001: Publication has composite identity.

### Current Term

No formal term in GLOSSARY.

### Status

MISSING — no stable name.

---

## 2.5 MC-005: Graph Rendering

### What It Would Be

The process of generating a graph from data.

### Evidence

> "Graph Generator → SVG → PNG" (Architect Context)

### Current Term

"Graph generation" — used informally.

### Status

MISSING — no stable name.

---

## 2.6 MC-006: Temporary Product

### What It Would Be

A product that expires at end of day.

### Evidence

> "Tomorrow information disappears automatically." (Architect Intent)

### Current Term

"Temporary" — used informally.

### Status

MISSING — no stable name.

---

## 2.7 MC-007: Persistent Product

### What It Would Be

A product that is archived permanently.

### Evidence

> "Emergency outages SHALL remain available as part of the historical record." (TELEGRAM_EDITORIAL)

### Current Term

"Permanent" — used informally.

### Status

MISSING — no stable name.

---

## 2.8 MC-008: Channel Adapter

### What It Would Be

A channel-specific implementation of publishing.

### Evidence

> "Telegram and Facebook are PEER adapters." (Architect Intent)

### Current Term

"Adapter" — used informally.

### Status

MISSING — no stable name.

---

# 3. Missing Concepts Summary

| ID | Concept | Current Term | Status |
|----|---------|--------------|--------|
| MC-001 | Information Change | Data change | MISSING |
| MC-002 | Publication Change | Update | MISSING |
| MC-003 | Representation Change | No term | MISSING |
| MC-004 | Publication Identity | No formal term | MISSING |
| MC-005 | Graph Rendering | Graph generation | MISSING |
| MC-006 | Temporary Product | Temporary | MISSING |
| MC-007 | Persistent Product | Permanent | MISSING |
| MC-008 | Channel Adapter | Adapter | MISSING |

---

# 4. Findings

## 4.1 Finding MC-001

**8 missing concepts were identified.**

All repeatedly appear but have no stable name.

**Evidence:** Analysis of missing concepts.

**Confidence:** HIGH.

## 4.2 Finding MC-002

**Most missing concepts relate to EVENTS.**

Information Change, Publication Change, Representation Change.

**Evidence:** Analysis of missing concepts.

**Confidence:** HIGH.

## 4.3 Finding MC-003

**Some missing concepts relate to ATTRIBUTES.**

Publication Identity, Temporary Product, Persistent Product.

**Evidence:** Analysis of missing concepts.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| MC-001 | Analysis of missing concepts |
| MC-002 | Analysis of missing concepts |
| MC-003 | Analysis of missing concepts |

---

**End of Missing Concepts**
