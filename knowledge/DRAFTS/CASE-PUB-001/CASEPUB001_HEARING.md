# CASEPUB001_HEARING

**Document ID:** CASE-PUB-001

**Title:** Publication Architecture Hearing

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document establishes the scope, context and research questions for CASE-PUB-001: the complete reconstruction of the publication architecture from first principles.

---

# 2. Case Scope

## 2.1 What This Case Investigates

The publication architecture of the SvitloSk Project, reconstructed from first principles without Telegram-centric assumptions.

## 2.2 What This Case Does NOT Investigate

- Telegram-specific implementation
- Facebook-specific implementation
- Software implementation details
- Infrastructure decisions
- Existing specification validity

## 2.3 Investigation Constraint

This investigation MUST ignore previous Telegram-centric assumptions. Everything must be proven from the project's mission and domain reality.

---

# 3. Context

## 3.1 Previous Architecture

During previous investigations the project was unconsciously centered around Telegram.

The architectural decomposition assumed Telegram as the primary publication channel.

## 3.2 Recognition

After completing the research methodology (Research Method V1.0) the Architect recognized that:

- The real subject of the project is NOT Telegram publication
- The real subject is publication of the SvitloSk Public Information Journal
- Telegram is only ONE possible communication channel
- Facebook will become ANOTHER communication channel
- The project may later support ADDITIONAL publication channels

## 3.3 Implication

The previous architectural decomposition may be incorrect.

The investigation must reconstruct the publication architecture from first principles.

---

# 4. Research Questions

## 4.1 Primary Object

What is actually the primary object produced by the project?

Candidates:
- Journal
- Publication
- Issue
- Release
- Edition
- Information Package
- Something else

**Requirement:** Prove the answer.

## 4.2 Lifecycle

What is the lifecycle of this primary object?

Construct the complete chain:

```
Reality
    ↓
...
    ↓
Recipient
```

## 4.3 Identity

Does this primary object have identity?

If yes — what creates it?
- Date?
- Territory?
- Content?
- Sequence?
- Version?
- Combination?

## 4.4 Irreducible Parts

What are the irreducible parts of one Journal Release?

Classify each part:
- Mandatory
- Optional
- Temporary

## 4.5 Telegram Consumption

Does Telegram consume this object?

Or create another one?

## 4.6 Facebook Consumption

Does Facebook consume exactly the same object?

Or another representation?

## 4.7 Domain Separation

What belongs to the publication domain?

What belongs to communication channels?

Separate them rigorously.

## 4.8 Publisher Existence

Does a Publisher actually exist?

Or is it merely an abstraction over several processes?

## 4.9 Publishing Kernel

Is there a Publishing Kernel?

If yes — define it.

## 4.10 Questionable Concepts

Which current project concepts become questionable after this reframing?

Candidates:
- Publication
- Issue
- Journal
- Publisher
- Publication Engine
- Telegram Publisher
- Telegram Message
- Facebook Post
- Release
- Archive
- Representation

Identify all candidates.

## 4.11 Disappearing Concepts

Which concepts may disappear completely?

## 4.12 New Concepts

Which new concepts appear naturally?

Only if unavoidable. Never invent terminology.

---

# 5. Evidence Sources

This investigation draws evidence from:

| Document | Relevance |
|----------|-----------|
| CHARTER.md | Project mission, product definition |
| GLOSSARY.md | Canonical terminology |
| ARCHITECTURE.md | Current architectural model |
| DATA_MODEL.md | Logical data entities |
| TELEGRAM_PUBLISHING_CANONICAL_MODEL.md | Current Telegram-centric model |
| TELEGRAM_PUBLICATION_LIFECYCLE.md | Current lifecycle model |
| TELEGRAM_EDITORIAL_SYSTEM_CANONICAL_MODEL.md | Current editorial model |
| TERRITORIAL_MODEL.md | Territorial structure |

---

# 6. Research Rules

This investigation follows Research Method V1.0 (METH-V1-001).

Research Principles applied:
- Evidence Before Conclusion
- Multiple Models Before Selection
- Cross-Examination Before Acceptance
- Contradiction Search Before Acceptance
- No Recommendations During Research

---

# 7. Deliverables

| Document | Purpose |
|----------|---------|
| CASEPUB001_HEARING.md | Case scope and research questions |
| CASEPUB001_OBJECT_RECONSTRUCTION.md | Primary object identification and proof |
| CASEPUB001_LIFECYCLE.md | Complete lifecycle chain |
| CASEPUB001_COMPETING_MODELS.md | Multiple architectural models |
| CASEPUB001_CONTRADICTIONS.md | Contradictions between models |
| CASEPUB001_KERNEL_ANALYSIS.md | Publishing Kernel analysis |
| CASEPUB001_TERMINOLOGY_REVIEW.md | Terminology review |
| CASEPUB001_OPEN_QUESTIONS.md | Unresolved questions |
| CASEPUB001_CERTIFICATE.md | Investigation certificate |

---

# 8. Governance

This document is a Research Draft.

This document is NOT a specification.

This document is NOT canonical.

Findings from this investigation MAY be promoted to canonical knowledge through the approved governance process.

---

**End of Hearing**
