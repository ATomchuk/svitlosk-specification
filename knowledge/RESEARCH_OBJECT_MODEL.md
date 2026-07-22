# RESEARCH_OBJECT_MODEL

**Document ID:** META005-OBJECT-MODEL

**Title:** Research Object Model

**Document Class:** Research Architecture

**Status:** Stable

**Author:** SvitloSk Project — Chief Research Architect

---

# Purpose

This document defines every object participating in architectural research.

---

# Research Object Model

## Object: Question

**Definition:** An inquiry requiring investigation.

**Properties:**

- Has text (the question itself)
- Has origin (who asked)
- Has importance (HIGH/MEDIUM/LOW)
- Has status (Open/Answered/Superseded)
- Has dependencies (other questions)

---

## Object: Investigation

**Definition:** A systematic inquiry into a subject.

**Properties:**

- Has identifier (CASE-XXX)
- Has subject (what is being investigated)
- Has phases (research, models, hearing, decision)
- Has status (In Progress/Complete)
- Has outputs (findings, models, contradictions)

---

## Object: Evidence

**Definition:** Proof supporting or contradicting a claim.

**Properties:**

- Has source (document, section, paragraph)
- Has content (what it proves)
- Has strength (STRONG/WEAK)
- Has type (supporting/contradicting)

---

## Object: Finding

**Definition:** A validated conclusion from investigation.

**Properties:**

- Has statement (what was found)
- Has evidence (what supports it)
- Has confidence (HIGH/MEDIUM/LOW)
- Has origin (which investigation)
- Has status (Draft/Validated/Canonical)

---

## Object: Knowledge Unit

**Definition:** An atomic piece of architectural knowledge.

**Properties:**

- Has statement (what is known)
- Has class (Finding/Definition/Model/etc.)
- Has origin (which investigation)
- Has confidence (HIGH/MEDIUM/LOW)
- Has status (Draft/Validated/Canonical)

---

## Object: Contradiction

**Definition:** A conflict between two statements.

**Properties:**

- Has statement A
- Has statement B
- Has origin (which investigation found it)
- Has severity (HIGH/MEDIUM/LOW)
- Has status (Open/Resolved/Superseded)

---

## Object: Principle

**Definition:** An architectural truth that applies across contexts.

**Properties:**

- Has statement (what is true)
- Has evidence (what supports it)
- Has source (which investigation derived it)
- Has applications (where it applies)

---

# Key Insight

**Research objects have clear properties that can be measured and tracked.**

**This enables objective assessment of research completeness.**

---

# End of Research Object Model
