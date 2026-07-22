# SRC001_HEARING

**Document ID:** CASE-SRC-001

**Title:** Source Audit for Publisher Knowledge Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-SRC-001: Source Audit for Publisher Knowledge.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The SOURCES OF KNOWLEDGE about Publisher — where knowledge exists, how trustworthy each source is, whether hidden knowledge exists outside current specifications.

## 2.2 What This Case Does NOT Investigate

- Publisher design
- Publisher implementation
- Specification modification
- Architecture decisions

## 2.3 Investigation Constraint

This is a SOURCE AUDIT.

We are NOT designing Publisher.

We are NOT modifying specifications.

We are auditing SOURCES OF KNOWLEDGE.

---

# 3. Context

## 3.1 Previous Investigations

- CASE-PUB-001: Publication architecture
- CASE-PUB-002: Telegram Publisher reverse engineering
- CASE-JRN-001: Journal ontology
- CASE-INF-001: Information ontology
- CASE-LC-001: Information lifecycle ontology
- CASE-SYS-001: System composition

## 3.2 Architect Confirmation

The Architect confirms:

- Telegram implementation contains the largest amount of practical Publisher knowledge
- Existing specifications contain only fragments
- Historical project versions may contain additional architectural knowledge
- Current operational artifacts describe Publisher inputs but NOT Publisher itself

## 3.3 Implication

Before reconstructing Publisher, we must determine WHICH SOURCES are authoritative.

---

# 4. Research Tasks

## Research 1 — Source Inventory

Identify every source that may contain Publisher knowledge.

## Research 2 — Source Classification

Classify every source: Canonical, Secondary, Historical, Operational, Derived, Unknown.

## Research 3 — Knowledge Distribution

Determine which Publisher concepts exist in which source.

## Research 4 — Hidden Knowledge

Search for Publisher knowledge that exists ONLY in Telegram implementation, archived files, or historical documentation.

## Research 5 — Missing Knowledge

Identify Publisher concepts that exist NOWHERE.

## Research 6 — Historical Value

Evaluate archived project versions.

## Research 7 — Source Reliability

Rank every source by reliability.

## Research 8 — Evidence Map

Construct evidence graph.

## Research 9 — Readiness Assessment

Determine if we are ready to reconstruct Publisher ontology.

## Research 10 — Audit

Verify completeness.

---

# 5. Deliverables

| Document | Purpose |
|----------|---------|
| SRC001_HEARING.md | Case scope and research questions |
| SRC001_SOURCE_INVENTORY.md | Source inventory |
| SRC001_SOURCE_CLASSIFICATION.md | Source classification |
| SRC001_KNOWLEDGE_DISTRIBUTION.md | Knowledge distribution matrix |
| SRC001_HIDDEN_KNOWLEDGE.md | Hidden knowledge |
| SRC001_MISSING_KNOWLEDGE.md | Missing knowledge |
| SRC001_ARCHIVE_VALUE.md | Archive value analysis |
| SRC001_SOURCE_RELIABILITY.md | Source reliability matrix |
| SRC001_EVIDENCE_GRAPH.md | Evidence graph |
| SRC001_READINESS.md | Readiness assessment |
| SRC001_AUDIT.md | Audit certificate |

---

# 6. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
