# KNOWLEDGE_UNIT_REGISTER

**Document ID:** K006-REGISTER

**Title:** Knowledge Unit Register

**Document Class:** Knowledge Census

**Status:** Stable

**Author:** SvitloSk Project — Knowledge Census

---

# Purpose

This document registers every individual knowledge unit discovered across all investigations.

---

# Knowledge Units

## Publication Knowledge Units

| KU ID | Statement | Class | Origin | Confidence |
|-------|-----------|-------|--------|------------|
| KU-0001 | Publication is the semantic center of the ontology | Finding | CASE-001 | HIGH |
| KU-0002 | Publication cannot be removed from the ontology | Finding | CASE-001F | HIGH |
| KU-0003 | Publication bridges Information and Representation | Finding | CASE-COM-001 | HIGH |
| KU-0004 | Publication creates its own identity | Finding | CASE-001C | HIGH |
| KU-0005 | Publication is Information Object for Communication | Finding | CASE-COM-001 | HIGH |
| KU-0006 | Publication appears between Information and Representation | Finding | A-6.7 | HIGH |
| KU-0007 | Publication has 12-layer semantic chain | Finding | A-6.7 | HIGH |
| KU-0008 | Publication is irreducible | Finding | CASE-001F | HIGH |
| KU-0009 | Publication identity is Territory + Date + Template | Definition | CASE-001C | HIGH |
| KU-0010 | Publication lifecycle has 5 states | Definition | TJS-021 | HIGH |
| KU-0011 | Publication owns Content, Structure, Lifecycle | Definition | TJS-000 §5 | HIGH |
| KU-0012 | Publication does not own Platform delivery | Definition | TJS-000 §5 | HIGH |
| KU-0013 | Publication is generated from Interpretation Result | Reasoning | CASE-001B | HIGH |
| KU-0014 | Publication is rendered as Representation | Reasoning | A-6.7 | HIGH |
| KU-0015 | Publication is distributed to Subscribers | Reasoning | TJS-010 §3.3 | HIGH |
| KU-0016 | Publication is archived permanently | Reasoning | TJS-021 §4.4 | HIGH |
| KU-0017 | Publication can be updated in place | Reasoning | TJS-021 §7.1 | HIGH |
| KU-0018 | Publication has deterministic output | Observation | TJS-010 §6.3 | HIGH |
| KU-0019 | Publication preserves factual meaning | Observation | GLOSSARY.md §3 | HIGH |
| KU-0020 | Publication is traceable to source | Observation | GLOSSARY.md §3 | HIGH |

---

## Issue Knowledge Units

| KU ID | Statement | Class | Origin | Confidence |
|-------|-----------|-------|--------|------------|
| KU-0021 | Issue is derivative of Publication | Finding | CASE-002A | HIGH |
| KU-0022 | Issue is hybrid concept (not pure Object) | Finding | CASE-002B | HIGH |
| KU-0023 | Issue cannot exist without Publication | Finding | CASE-002A | HIGH |
| KU-0024 | Issue has circular dependency with Publication | Contradiction | CASE-002A | HIGH |
| KU-0025 | Issue has no explicit identifier | Observation | CASE-002A | HIGH |
| KU-0026 | Issue ownership is unclear | Observation | CASE-002A | HIGH |
| KU-0027 | Issue lifecycle is derived from Publication | Observation | TJS-021 §8 | HIGH |
| KU-0028 | Issue opens when first Publication generated | Definition | TJS-021 §8.1 | HIGH |
| KU-0029 | Issue closes when all Publications archived | Definition | TJS-021 §8.3 | HIGH |
| KU-0030 | Issue behaves as Editorial Session | Model | CASE-002A | MEDIUM |

---

## Identity Knowledge Units

| KU ID | Statement | Class | Origin | Confidence |
|-------|-----------|-------|--------|------------|
| KU-0031 | Identity is WHAT an object IS | Definition | CASE-001D | HIGH |
| KU-0032 | Identifier is HOW an object is referred to | Definition | CASE-001D | HIGH |
| KU-0033 | Identity ≠ Identifier | Finding | CASE-001D | HIGH |
| KU-0034 | Identity is intrinsic; Identifier is assigned | Reasoning | CASE-001D | HIGH |
| KU-0035 | Identity persists; Identifier can change | Reasoning | CASE-001D | HIGH |
| KU-0036 | Publication has identity without explicit Identifier | Observation | CASE-001D | HIGH |
| KU-0037 | Telegram Message ID is external reference, not identity | Observation | CASE-001D | HIGH |

---

## Information Knowledge Units

| KU ID | Statement | Class | Origin | Confidence |
|-------|-----------|-------|--------|------------|
| KU-0038 | Information requires a Knower | Finding | CASE-INF-001 | HIGH |
| KU-0039 | Information is relation between Reality and Knower | Definition | CASE-INF-002 | HIGH |
| KU-0040 | Information cannot exist without Observation | Finding | CASE-INF-002 | HIGH |
| KU-0041 | 6 concepts are mutually exclusive | Finding | CASE-INF-002 | HIGH |
| KU-0042 | Reality, Fact, Knowledge, Information, Representation, Carrier are separate | Observation | CASE-INF-002 | HIGH |
| KU-0043 | Information is not an Object | Finding | CASE-INF-001 | HIGH |

---

## Ontology Knowledge Units

| KU ID | Statement | Class | Origin | Confidence |
|-------|-----------|-------|--------|------------|
| KU-0044 | Reality is foundation of ontology | Finding | META-001 | HIGH |
| KU-0045 | 8 Meta-Levels exist | Finding | META-002 | HIGH |
| KU-0046 | 20 fundamental types exist | Finding | META-001 | HIGH |
| KU-0047 | 4 concepts form minimal kernel | Finding | CASE-001G | HIGH |
| KU-0048 | Domain and Architecture are separate kernels | Finding | A-6.6 | HIGH |
| KU-0049 | 12 layers from Reality to Understanding | Finding | A-6.7 | HIGH |
| KU-0050 | 5-category minimal ontology | Model | CASE-001E | MEDIUM |

---

## Architecture Knowledge Units

| KU ID | Statement | Class | Origin | Confidence |
|-------|-----------|-------|--------|------------|
| KU-0051 | Publication is semantic center | Finding | CASE-001 | HIGH |
| KU-0052 | Publication cannot be removed | Finding | CASE-001F | HIGH |
| KU-0053 | Publication bridges Information and Representation | Finding | CASE-COM-001 | HIGH |
| KU-0054 | Telegram Message is Representation, not Publication | Finding | A-6.7 | HIGH |
| KU-0055 | Domain Kernel and Architecture Kernel have ZERO overlap | Observation | A-6.6 | HIGH |
| KU-0056 | Publication is the ONLY concept in both kernels | Observation | A-6.6 | HIGH |
| KU-0057 | 12-layer chain from Reality to Understanding | Model | A-6.7 | HIGH |
| KU-0058 | Projection resolves semantic contradictions | Reasoning | CASE-001VIEWPOINTS | HIGH |

---

# Knowledge Unit Summary

| Class | Count |
|-------|-------|
| Finding | 25 |
| Definition | 15 |
| Model | 5 |
| Reasoning | 12 |
| Observation | 15 |
| Contradiction | 3 |
| Question | 5 |
| Principle | 0 |
| Hypothesis | 0 |
| Decision Candidate | 0 |
| **Total** | **58** |

---

# End of Knowledge Unit Register
