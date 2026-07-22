# ATOMIC_KNOWLEDGE_REGISTER

**Document ID:** K007-REGISTER

**Title:** Atomic Knowledge Register

**Document Class:** Knowledge Atomization

**Status:** Stable

**Author:** SvitloSk Project — Knowledge Atomization Sprint

---

# Purpose

This document registers every Atomic Knowledge Unit (AKU) decomposed from composite Knowledge Units.

---

# Atomic Knowledge Units

## Publication AKUs

| AKU ID | Statement | Source KU | Origin | Confidence |
|--------|-----------|-----------|--------|------------|
| AKU-0001 | Publication exists | KU-0001 | CASE-001 | HIGH |
| AKU-0002 | Publication is the semantic center | KU-0001 | CASE-001 | HIGH |
| AKU-0003 | Publication cannot be removed | KU-0002 | CASE-001F | HIGH |
| AKU-0004 | Publication bridges Information | KU-0003 | CASE-COM-001 | HIGH |
| AKU-0005 | Publication bridges Representation | KU-0003 | CASE-COM-001 | HIGH |
| AKU-0006 | Publication creates its own identity | KU-0004 | CASE-001C | HIGH |
| AKU-0007 | Publication is Information Object | KU-0005 | CASE-COM-001 | HIGH |
| AKU-0008 | Publication is for Communication | KU-0005 | CASE-COM-001 | HIGH |
| AKU-0009 | Publication appears after Information | KU-0006 | A-6.7 | HIGH |
| AKU-0010 | Publication appears before Representation | KU-0006 | A-6.7 | HIGH |
| AKU-0011 | Publication has 12-layer chain | KU-0007 | A-6.7 | HIGH |
| AKU-0012 | Publication is irreducible | KU-0008 | CASE-001F | HIGH |
| AKU-0013 | Publication identity is Territory | KU-0009 | CASE-001C | HIGH |
| AKU-0014 | Publication identity is Date | KU-0009 | CASE-001C | HIGH |
| AKU-0015 | Publication identity is Template | KU-0009 | CASE-001C | HIGH |
| AKU-0016 | Publication lifecycle has Generated state | KU-0010 | TJS-021 | HIGH |
| AKU-0017 | Publication lifecycle has Published state | KU-0010 | TJS-021 | HIGH |
| AKU-0018 | Publication lifecycle has Updated state | KU-0010 | TJS-021 | HIGH |
| AKU-0019 | Publication lifecycle has Archived state | KU-0010 | TJS-021 | HIGH |
| AKU-0020 | Publication lifecycle has Removed state | KU-0010 | TJS-021 | HIGH |
| AKU-0021 | Publication owns Content | KU-0011 | TJS-000 §5 | HIGH |
| AKU-0022 | Publication owns Structure | KU-0011 | TJS-000 §5 | HIGH |
| AKU-0023 | Publication owns Lifecycle | KU-0011 | TJS-000 §5 | HIGH |
| AKU-0024 | Publication does not own Platform delivery | KU-0012 | TJS-000 §5 | HIGH |
| AKU-0025 | Publication is generated from Interpretation Result | KU-0013 | CASE-001B | HIGH |
| AKU-0026 | Publication is rendered as Representation | KU-0014 | A-6.7 | HIGH |
| AKU-0027 | Publication is distributed to Subscribers | KU-0015 | TJS-010 §3.3 | HIGH |
| AKU-0028 | Publication is archived permanently | KU-0016 | TJS-021 §4.4 | HIGH |
| AKU-0029 | Publication can be updated in place | KU-0017 | TJS-021 §7.1 | HIGH |
| AKU-0030 | Publication has deterministic output | KU-0018 | TJS-010 §6.3 | HIGH |
| AKU-0031 | Publication preserves factual meaning | KU-0019 | GLOSSARY.md §3 | HIGH |
| AKU-0032 | Publication is traceable to source | KU-0020 | GLOSSARY.md §3 | HIGH |

---

## Issue AKUs

| AKU ID | Statement | Source KU | Origin | Confidence |
|--------|-----------|-----------|--------|------------|
| AKU-0033 | Issue is derivative of Publication | KU-0021 | CASE-002A | HIGH |
| AKU-0034 | Issue is hybrid concept | KU-0022 | CASE-002B | HIGH |
| AKU-0035 | Issue cannot exist without Publication | KU-0023 | CASE-002A | HIGH |
| AKU-0036 | Issue has circular dependency with Publication | KU-0024 | CASE-002A | HIGH |
| AKU-0037 | Issue has no explicit identifier | KU-0025 | CASE-002A | HIGH |
| AKU-0038 | Issue ownership is unclear | KU-0026 | CASE-002A | HIGH |
| AKU-0039 | Issue lifecycle is derived from Publication | KU-0027 | TJS-021 §8 | HIGH |
| AKU-0040 | Issue opens when first Publication generated | KU-0028 | TJS-021 §8.1 | HIGH |
| AKU-0041 | Issue closes when all Publications archived | KU-0029 | TJS-021 §8.3 | HIGH |
| AKU-0042 | Issue behaves as Editorial Session | KU-0030 | CASE-002A | MEDIUM |

---

## Identity AKUs

| AKU ID | Statement | Source KU | Origin | Confidence |
|--------|-----------|-----------|--------|------------|
| AKU-0043 | Identity is WHAT an object IS | KU-0031 | CASE-001D | HIGH |
| AKU-0044 | Identifier is HOW an object is referred to | KU-0032 | CASE-001D | HIGH |
| AKU-0045 | Identity is not Identifier | KU-0033 | CASE-001D | HIGH |
| AKU-0046 | Identity is intrinsic | KU-0034 | CASE-001D | HIGH |
| AKU-0047 | Identifier is assigned | KU-0034 | CASE-001D | HIGH |
| AKU-0048 | Identity persists | KU-0035 | CASE-001D | HIGH |
| AKU-0049 | Identifier can change | KU-0035 | CASE-001D | HIGH |
| AKU-0050 | Publication has identity without explicit Identifier | KU-0036 | CASE-001D | HIGH |
| AKU-0051 | Telegram Message ID is external reference | KU-0037 | CASE-001D | HIGH |

---

## Information AKUs

| AKU ID | Statement | Source KU | Origin | Confidence |
|--------|-----------|-----------|--------|------------|
| AKU-0052 | Information requires a Knower | KU-0038 | CASE-INF-001 | HIGH |
| AKU-0053 | Information is relation between Reality and Knower | KU-0039 | CASE-INF-002 | HIGH |
| AKU-0054 | Information cannot exist without Observation | KU-0040 | CASE-INF-002 | HIGH |
| AKU-0055 | 6 concepts are mutually exclusive | KU-0041 | CASE-INF-002 | HIGH |
| AKU-0056 | Reality is separate from Fact | KU-0042 | CASE-INF-002 | HIGH |
| AKU-0057 | Reality is separate from Knowledge | KU-0042 | CASE-INF-002 | HIGH |
| AKU-0058 | Reality is separate from Information | KU-0042 | CASE-INF-002 | HIGH |
| AKU-0059 | Reality is separate from Representation | KU-0042 | CASE-INF-002 | HIGH |
| AKU-0060 | Reality is separate from Carrier | KU-0042 | CASE-INF-002 | HIGH |
| AKU-0061 | Information is not an Object | KU-0043 | CASE-INF-001 | HIGH |

---

## Ontology AKUs

| AKU ID | Statement | Source KU | Origin | Confidence |
|--------|-----------|-----------|--------|------------|
| AKU-0062 | Reality is foundation of ontology | KU-0044 | META-001 | HIGH |
| AKU-0063 | 8 Meta-Levels exist | KU-0045 | META-002 | HIGH |
| AKU-0064 | 20 fundamental types exist | KU-0046 | META-001 | HIGH |
| AKU-0065 | 4 concepts form minimal kernel | KU-0047 | CASE-001G | HIGH |
| AKU-0066 | Domain Kernel exists | KU-0048 | A-6.6 | HIGH |
| AKU-0067 | Architecture Kernel exists | KU-0048 | A-6.6 | HIGH |
| AKU-0068 | Domain and Architecture are separate | KU-0048 | A-6.6 | HIGH |
| AKU-0069 | 12 layers from Reality to Understanding | KU-0049 | A-6.7 | HIGH |

---

## Architecture AKUs

| AKU ID | Statement | Source KU | Origin | Confidence |
|--------|-----------|-----------|--------|------------|
| AKU-0070 | Publication is semantic center | KU-0051 | CASE-001 | HIGH |
| AKU-0071 | Publication cannot be removed | KU-0052 | CASE-001F | HIGH |
| AKU-0072 | Publication bridges Information | KU-0053 | CASE-COM-001 | HIGH |
| AKU-0073 | Publication bridges Representation | KU-0053 | CASE-COM-001 | HIGH |
| AKU-0074 | Telegram Message is Representation | KU-0054 | A-6.7 | HIGH |
| AKU-0075 | Telegram Message is not Publication | KU-0054 | A-6.7 | HIGH |
| AKU-0076 | Domain Kernel has no overlap with Architecture Kernel | KU-0055 | A-6.6 | HIGH |
| AKU-0077 | Publication is the ONLY concept in both kernels | KU-0056 | A-6.6 | HIGH |
| AKU-0078 | 12-layer chain exists | KU-0057 | A-6.7 | HIGH |
| AKU-0079 | Projection resolves semantic contradictions | KU-0058 | CASE-001VIEWPOINTS | HIGH |

---

# Atomic Knowledge Summary

| Category | Count |
|----------|-------|
| Publication AKUs | 32 |
| Issue AKUs | 10 |
| Identity AKUs | 9 |
| Information AKUs | 10 |
| Ontology AKUs | 8 |
| Architecture AKUs | 10 |
| **Total** | **79** |

---

# End of Atomic Knowledge Register
