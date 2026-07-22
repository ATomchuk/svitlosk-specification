# LC001_GLOSSARY

**Document ID:** CASE-LC-001-GL

**Title:** Candidate Glossary

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document produces a candidate glossary from the lifecycle ontology investigation.

---

# 2. Candidate Glossary

## 2.1 Core Concepts

### Information Lifecycle

A domain-specific PATTERN describing how information flows through the system.

Stages: ORIGIN → ACQUISITION → NORMALIZATION → INTERPRETATION → PRESENTATION → DELIVERY → ARCHIVAL.

**Source:** CASE-INF-001, this investigation

---

### Publication Lifecycle

The lifecycle of a Publication from creation to archival.

Stages: Interpretation Result → Rendering → Publication generation → Distribution → Archival → Expiration.

**Source:** GLOSSARY §3

---

### Lifecycle Pattern

A reusable solution describing how information behaves over time.

Cannot be "owned" by a component — it is OBSERVED, not OWNED.

**Source:** This investigation (Research 1)

---

## 2.2 Lifecycle Operations

### Create

New information enters the system.

Intrinsic to Lifecycle. Owned by Parser.

**Source:** This investigation (Research 2)

---

### Update

Existing information is modified with new data.

Intrinsic to Lifecycle. Owned by Parser, Lifecycle, Publisher.

**Source:** This investigation (Research 2)

---

### Replace

Existing information is entirely replaced with new information.

Intrinsic to Lifecycle. Owned by Lifecycle, Publisher.

**Source:** This investigation (Research 2)

---

### Merge

Multiple pieces of information are combined into one.

Intrinsic to Lifecycle. Owned by Lifecycle, Parser.

**Source:** This investigation (Research 2)

---

### Expire

Information ceases to be valid and is removed from active view.

Intrinsic to Lifecycle. Owned by Lifecycle, Publisher.

**Source:** This investigation (Research 2)

---

### Archive

Information is preserved as historical record.

Intrinsic to Lifecycle. Owned by Lifecycle, Storage.

**Source:** This investigation (Research 2)

---

## 2.3 Change Types

### Information Change

The underlying factual content changes.

Source: Official DSO publications.

**Source:** This investigation (Research 6)

---

### Publication Change

The prepared message for distribution changes.

Source: Information changes trigger publication changes.

**Source:** This investigation (Research 6)

---

### Representation Change

The visual or textual format changes.

Source: Publication changes trigger representation changes.

**Source:** This investigation (Research 6)

---

## 2.4 Architecture Concepts

### Lifecycle Engine

A component that manages temporal rules, state management, and expiry logic.

Independent from Publisher.

**Source:** This investigation (Research 7)

---

### Thin Publisher

A Publisher focused only on publication generation and distribution coordination.

Does not own temporal rules, state management, or rendering.

**Source:** This investigation (Research 10)

---

### Thick Publisher

A Publisher with many responsibilities including temporal rules, state management, and rendering.

**Source:** This investigation (Research 10)

---

# 3. Candidate Status

This glossary candidate is:

- A RESEARCH ARTIFACT
- NOT canonical
- NOT promoted
- Subject to Architect decision

---

**End of Candidate Glossary**
