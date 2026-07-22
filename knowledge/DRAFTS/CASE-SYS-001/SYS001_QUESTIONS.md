# SYS001_QUESTIONS

**Document ID:** CASE-SYS-001-Q

**Title:** Open Questions

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document produces Open Questions.

Do not answer them.

---

# 2. Open Questions

## 2.1 OQ-001: System Boundary Definition

**Question:** Where exactly does the SvitloSk system end and the external world begin?

**Evidence:**
- DSO is external
- Residents are external
- Telegram/Facebook are external channels

**Importance:** HIGH — defines system scope.

---

## 2.2 OQ-002: Domain Independence Enforcement

**Question:** How is domain independence enforced architecturally?

**Evidence:**
- Architect Intent: "Queue Schedule, Planned Outages, Emergency Outages are THREE DIFFERENT ONTOLOGICAL OBJECTS. Never merge them."

**Importance:** HIGH — prevents domain coupling.

---

## 2.3 OQ-003: State Management Architecture

**Question:** Where should system state be managed?

**Evidence:**
- Missing concepts: Channel State, Publication State, Information State

**Importance:** HIGH — affects system behavior.

---

## 2.4 OQ-004: Event-Driven vs Cycle-Based

**Question:** Should the system be event-driven or cycle-based?

**Evidence:**
- CASE-LC-001: Event-Driven Model
- GLOSSARY: Processing Cycle

**Importance:** MEDIUM — affects system architecture.

---

## 2.5 OQ-005: Publisher Scope

**Question:** Should Publisher serve only Journal, or also PWA?

**Evidence:**
- Current: Publisher serves Journal
- PWA is independent

**Importance:** MEDIUM — affects Publisher responsibility.

---

## 2.6 OQ-006: Adapter Interface Standardization

**Question:** Should Adapters have a standardized interface?

**Evidence:**
- Telegram and Facebook are peers
- They have different APIs

**Importance:** MEDIUM — affects adapter design.

---

## 2.7 OQ-007: Territorial Scope

**Question:** Should territorial scope be expanded beyond Starokostiantyniv?

**Evidence:**
- CHARTER §5: "primary purpose is to serve Starokostiantyniv"
- Architecture allows adaptation

**Importance:** LOW — future consideration.

---

## 2.8 OQ-008: Historical Archive Scope

**Question:** What should be archived and for how long?

**Evidence:**
- DATA_MODEL.md: "Historical Archive"
- No retention policy defined

**Importance:** LOW — affects storage design.

---

# 3. Question Priority

## 3.1 High Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-001 | System Boundary Definition | Defines system scope |
| OQ-002 | Domain Independence Enforcement | Prevents domain coupling |
| OQ-003 | State Management Architecture | Affects system behavior |

## 3.2 Medium Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-004 | Event-Driven vs Cycle-Based | Affects system architecture |
| OQ-005 | Publisher Scope | Affects Publisher responsibility |
| OQ-006 | Adapter Interface Standardization | Affects adapter design |

## 3.3 Low Priority

| ID | Question | Reason |
|----|----------|--------|
| OQ-007 | Territorial Scope | Future consideration |
| OQ-008 | Historical Archive Scope | Affects storage design |

---

# 4. Findings

## 4.1 Finding OQ-001

**Eight open questions were identified.**

Three are high priority, three are medium priority, two are low priority.

**Evidence:** Analysis of all evidence sources.

**Confidence:** HIGH.

---

# 5. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| OQ-001 | Analysis of all evidence sources |

---

**End of Open Questions**
