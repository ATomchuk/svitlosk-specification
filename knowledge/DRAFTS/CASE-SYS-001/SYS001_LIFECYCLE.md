# SYS001_LIFECYCLE

**Document ID:** CASE-SYS-001-LC

**Title:** Lifecycle Placement

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document determines where Lifecycle belongs.

---

# 2. Lifecycle Analysis

## 2.1 What is Lifecycle?

From CASE-LC-001:

> "Lifecycle is a PATTERN, not an object, process, or service."

> "It is a domain-specific pattern describing how information flows through the system."

## 2.2 Can a Pattern Be "Owned"?

**NO.**

Patterns are OBSERVED, not OWNED.

A pattern describes behavior — it does not have an owner.

---

# 3. Where Does Lifecycle Belong?

## 3.1 Option A: Inside Publisher

**Evidence For:**
- Publisher handles publication lifecycle

**Evidence Against:**
- Lifecycle spans MORE than publication
- Lifecycle includes information acquisition and archival
- Lifecycle is a SYSTEM-WIDE pattern, not a Publisher pattern

**Verdict:** WEAK. Lifecycle is too broad for Publisher.

---

## 3.2 Option B: Inside Information

**Evidence For:**
- Lifecycle describes information flow

**Evidence Against:**
- Lifecycle includes publication and delivery
- Lifecycle is not just about information

**Verdict:** WEAK. Lifecycle is too broad for Information.

---

## 3.3 Option C: Inside Journal

**Evidence For:**
- Journal is the publication service

**Evidence Against:**
- Lifecycle includes information acquisition (before Journal)
- Lifecycle includes PWA (separate from Journal)

**Verdict:** WEAK. Lifecycle is too broad for Journal.

---

## 3.4 Option D: Inside Publication

**Evidence For:**
- Publication has its own lifecycle

**Evidence Against:**
- Lifecycle includes information (before Publication)
- Lifecycle includes archival (after Publication)

**Verdict:** WEAK. Lifecycle is too narrow for Publication.

---

## 3.5 Option E: Entire System

**Evidence For:**
- Lifecycle spans the ENTIRE system
- Lifecycle includes all stages from ORIGIN to ARCHIVAL
- Lifecycle is a SYSTEM-WIDE pattern

**Evidence Against:**
- "Entire System" is not a component that can "own" something

**Verdict:** STRONG. Lifecycle belongs to the ENTIRE SYSTEM.

---

## 3.6 Option F: Nowhere (Pattern)

**Evidence For:**
- Lifecycle is a PATTERN
- Patterns are OBSERVED, not OWNED
- Lifecycle cannot be "owned" by any component

**Evidence Against:**
- Patterns still need to be IMPLEMENTED somewhere

**Verdict:** STRONG. Lifecycle is a pattern that is OBSERVED across the system.

---

# 4. Lifecycle Placement Conclusion

## 4.1 Primary Conclusion

**Lifecycle is a SYSTEM-WIDE PATTERN.**

It cannot be "owned" by any single component.

It is OBSERVED across the entire system.

## 4.2 Implementation Implication

Lifecycle behavior must be DISTRIBUTED across multiple components.

No single component can implement the entire lifecycle.

---

# 5. Findings

## 5.1 Finding LC-001

**Lifecycle belongs to the ENTIRE SYSTEM.**

It is a system-wide pattern, not a component-specific pattern.

**Evidence:** CASE-LC-001, analysis of placement options.

**Confidence:** HIGH.

## 5.2 Finding LC-002

**Lifecycle cannot be "owned" by any single component.**

It is a PATTERN that is OBSERVED, not OWNED.

**Evidence:** CASE-LC-001.

**Confidence:** HIGH.

## 5.3 Finding LC-003

**Lifecycle behavior must be DISTRIBUTED.**

No single component can implement the entire lifecycle.

**Evidence:** Analysis of placement options.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| LC-001 | CASE-LC-001, analysis of placement options |
| LC-002 | CASE-LC-001 |
| LC-003 | Analysis of placement options |

---

**End of Lifecycle Placement**
