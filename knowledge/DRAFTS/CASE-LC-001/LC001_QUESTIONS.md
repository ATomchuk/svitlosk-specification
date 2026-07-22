# LC001_QUESTIONS

**Document ID:** CASE-LC-001-Q

**Title:** Open Questions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document lists all unresolved questions from the CASE-LC-001 investigation.

---

# 2. Open Questions

## 2.1 OQ-001: Lifecycle as Pattern

**Question:** If Lifecycle is a pattern, how does it relate to architectural components?

**Evidence:**
- Research 1: "Lifecycle is a PATTERN, not an object, process, or service."
- Patterns are OBSERVED, not OWNED.

**Importance:** HIGH — affects how lifecycle ownership is conceived.

**Dependencies:** None.

---

## 2.2 OQ-002: Lifecycle Engine Necessity

**Question:** Is a separate Lifecycle Engine necessary, or can temporal behavior be distributed?

**Evidence:**
- Research 7: Architecture C proposes Independent Lifecycle Engine
- Research 7: Architecture D proposes Event-Driven Model

**Importance:** HIGH — affects architectural decomposition.

**Dependencies:** OQ-001.

---

## 2.3 OQ-003: Publisher Thickness

**Question:** Should Publisher become thinner, retaining only generation and distribution?

**Evidence:**
- Research 10: Publisher COULD become thinner
- Research 10: Thin Publisher Model has better separation

**Importance:** MEDIUM — affects Publisher responsibilities.

**Dependencies:** None.

---

## 2.4 OQ-004: Event Ownership

**Question:** Who owns event detection and routing?

**Evidence:**
- Research 4: Update causal chain involves four subsystems
- Research 7: Event-Driven Model requires event routing

**Importance:** MEDIUM — affects event-driven architecture.

**Dependencies:** OQ-002.

---

## 2.5 OQ-005: Rendering Ownership

**Question:** Should rendering be owned by Publisher or Adapter?

**Evidence:**
- Research 10: Rendering could be moved to Adapter
- GLOSSARY §3: Rendering is part of Publication Pipeline

**Importance:** MEDIUM — affects rendering responsibility.

**Dependencies:** None.

---

## 2.6 OQ-006: State Management

**Question:** Where should publication state be managed?

**Evidence:**
- Research 4: Publisher knows publication state
- Research 7: Lifecycle Engine could own state management

**Importance:** MEDIUM — affects state ownership.

**Dependencies:** OQ-002.

---

## 2.7 OQ-007: Delete Operation

**Question:** Is Delete truly not an operation in SvitloSk, or should it be?

**Evidence:**
- Research 2: "SvitloSk does NOT delete information."
- CHARTER §7: "SvitloSk does not modify open data."

**Importance:** LOW — confirms archival-only policy.

**Dependencies:** None.

---

## 2.8 OQ-008: Hide/Reveal Operations

**Question:** Should Hide and Reveal be formalized as lifecycle operations?

**Evidence:**
- Research 2: Hide and Reveal are MAYBE intrinsic to Lifecycle
- No evidence in canonical documents

**Importance:** LOW — affects operation inventory.

**Dependencies:** None.

---

# 3. Question Priority

## 3.1 High Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-001 | Lifecycle as Pattern | Affects lifecycle ownership conception |
| OQ-002 | Lifecycle Engine Necessity | Affects architectural decomposition |

## 3.2 Medium Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-003 | Publisher Thickness | Affects Publisher responsibilities |
| OQ-004 | Event Ownership | Affects event-driven architecture |
| OQ-005 | Rendering Ownership | Affects rendering responsibility |
| OQ-006 | State Management | Affects state ownership |

## 3.3 Low Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-007 | Delete Operation | Confirms archival-only policy |
| OQ-008 | Hide/Reveal Operations | Affects operation inventory |

---

# 4. Findings

## 4.1 Finding OQ-001

**Eight open questions were identified.**

Two are high priority, four are medium priority, two are low priority.

**Evidence:** Analysis of all research findings.

**Confidence:** HIGH.

## 4.2 Finding OQ-002

**The highest priority questions relate to Lifecycle as Pattern and Lifecycle Engine necessity.**

These questions affect the fundamental architecture.

**Evidence:** Research 1, Research 7.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OQ-001 | Research 1, Research 7 |
| OQ-002 | Analysis of all research findings |

---

**End of Open Questions**
