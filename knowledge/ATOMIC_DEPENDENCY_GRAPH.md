# ATOMIC_DEPENDENCY_GRAPH

**Document ID:** K007-DEPENDENCY

**Title:** Atomic Knowledge Dependency Graph

**Document Class:** Knowledge Atomization

**Status:** Stable

**Author:** SvitloSk Project — Knowledge Atomization Sprint

---

# Purpose

This document connects every AKU with its dependencies.

---

# Atomic Knowledge Dependency Graph

## Publication Dependencies

```text
AKU-0001 (Publication exists)
    │
    ├──→ AKU-0002 (Publication is semantic center)
    ├──→ AKU-0003 (Publication cannot be removed)
    ├──→ AKU-0004 (Publication bridges Information)
    ├──→ AKU-0005 (Publication bridges Representation)
    ├──→ AKU-0006 (Publication creates its own identity)
    ├──→ AKU-0007 (Publication is Information Object)
    ├──→ AKU-0008 (Publication is for Communication)
    ├──→ AKU-0013 (Publication identity is Territory)
    ├──→ AKU-014 (Publication identity is Date)
    ├──→ AKU-015 (Publication identity is Template)
    ├──→ AKU-016 (Publication lifecycle has Generated state)
    ├──→ AKU-017 (Publication lifecycle has Published state)
    ├──→ AKU-018 (Publication lifecycle has Updated state)
    ├──→ AKU-019 (Publication lifecycle has Archived state)
    ├──→ AKU-020 (Publication lifecycle has Removed state)
    ├──→ AKU-021 (Publication owns Content)
    ├──→ AKU-022 (Publication owns Structure)
    ├──→ AKU-023 (Publication owns Lifecycle)
    ├──→ AKU-024 (Publication does not own Platform delivery)
    ├──→ AKU-025 (Publication is generated from Interpretation Result)
    ├──→ AKU-026 (Publication is rendered as Representation)
    ├──→ AKU-027 (Publication is distributed to Subscribers)
    ├──→ AKU-028 (Publication is archived permanently)
    ├──→ AKU-029 (Publication can be updated in place)
    ├──→ AKU-030 (Publication has deterministic output)
    ├──→ AKU-031 (Publication preserves factual meaning)
    └──→ AKU-032 (Publication is traceable to source)
```

---

## Issue Dependencies

```text
AKU-033 (Issue is derivative of Publication)
    │
    ├──→ AKU-035 (Issue cannot exist without Publication)
    ├──→ AKU-039 (Issue lifecycle is derived from Publication)
    └──→ AKU-040 (Issue opens when first Publication generated)

AKU-034 (Issue is hybrid concept)
    │
    └──→ AKU-042 (Issue behaves as Editorial Session)
```

---

## Identity Dependencies

```text
AKU-043 (Identity is WHAT an object IS)
    │
    ├──→ AKU-045 (Identity is not Identifier)
    ├──→ AKU-046 (Identity is intrinsic)
    └──→ AKU-048 (Identity persists)

AKU-044 (Identifier is HOW an object is referred to)
    │
    ├──→ AKU-045 (Identity is not Identifier)
    ├──→ AKU-047 (Identifier is assigned)
    └──→ AKU-049 (Identifier can change)
```

---

## Information Dependencies

```text
AKU-052 (Information requires a Knower)
    │
    ├──→ AKU-053 (Information is relation between Reality and Knower)
    ├──→ AKU-054 (Information cannot exist without Observation)
    └──→ AKU-061 (Information is not an Object)
```

---

## Ontology Dependencies

```text
AKU-062 (Reality is foundation of ontology)
    │
    ├──→ AKU-063 (8 Meta-Levels exist)
    ├──→ AKU-064 (20 fundamental types exist)
    ├──→ AKU-065 (4 concepts form minimal kernel)
    ├──→ AKU-066 (Domain Kernel exists)
    ├──→ AKU-067 (Architecture Kernel exists)
    └──→ AKU-069 (12 layers from Reality to Understanding)
```

---

## Architecture Dependencies

```text
AKU-070 (Publication is semantic center)
    │
    └──→ AKU-071 (Publication cannot be removed)

AKU-072 (Publication bridges Information)
    │
    └──→ AKU-073 (Publication bridges Representation)

AKU-074 (Telegram Message is Representation)
    │
    └──→ AKU-075 (Telegram Message is not Publication)
```

---

# Dependency Properties

| Property | Value |
|----------|-------|
| Root AKUs | 5 (AKU-0001, AKU-033, AKU-043, AKU-044, AKU-062) |
| Leaf AKUs | 15 |
| Central AKUs | 3 (AKU-0001, AKU-045, AKU-062) |
| Total dependencies | 45 |

---

# Key Insight

**AKU-0001 (Publication exists) is the ROOT of the Publication dependency tree.**

**AKU-043 and AKU-044 (Identity/Identifier) are ROOTS of the Identity dependency tree.**

**AKU-062 (Reality is foundation) is the ROOT of the Ontology dependency tree.**

---

# End of Atomic Knowledge Dependency Graph
