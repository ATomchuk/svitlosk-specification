# Confidence Matrix

**Document Class:** Ontology Falsification

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document produces the confidence matrix.

---

# Confidence Matrix

## Category Confidence

| Category | Original Confidence | Falsification Attempts | Survived? | Final Confidence |
|----------|---------------------|------------------------|-----------|------------------|
| CONCEPT | MEDIUM | 3 | YES | HIGH |
| OBJECT | MEDIUM | 3 | YES | HIGH |
| INSTANCE | MEDIUM | 3 | YES | HIGH |
| COLLECTION | MEDIUM | 3 | YES | HIGH |
| PROCESS | MEDIUM | 3 | YES | HIGH |
| SERVICE | MEDIUM | 3 | YES | HIGH |
| ROLE | MEDIUM | 3 | YES | HIGH |
| ARTIFACT | MEDIUM | 3 | YES | HIGH |
| DOCUMENT | MEDIUM | 3 | YES | HIGH |
| STATE | MEDIUM | 3 | YES | HIGH |
| EVENT | MEDIUM | 3 | YES | HIGH |
| INTERFACE | MEDIUM | 3 | YES | HIGH |
| BOUNDARY | MEDIUM | 3 | YES | HIGH |
| RELATION | MEDIUM | 3 | YES | HIGH |

---

## Pairwise Confidence

| Pair | Falsification Attempted | Distinction Accepted | Confidence |
|------|------------------------|---------------------|------------|
| CONCEPT vs OBJECT | YES | YES | HIGH |
| OBJECT vs INSTANCE | YES | YES | HIGH |
| SERVICE vs ROLE | YES | YES | HIGH |
| ARTIFACT vs DOCUMENT | YES | YES | HIGH |
| PROCESS vs EVENT | YES | YES | HIGH |
| SERVICE vs PROCESS | YES | YES | HIGH |
| STATE vs EVENT | YES | YES | HIGH |
| COLLECTION vs OBJECT | YES | YES | HIGH |

---

## Confidence Summary

| Confidence Level | Categories | Pairs |
|------------------|------------|-------|
| HIGH | 14 | 8 |
| MEDIUM | 0 | 0 |
| LOW | 0 | 0 |

---

# Traceability

| Confidence | Source |
|-------------|--------|
| All confidence | Analysis of counterexamples and pairwise falsification |

---

**End of Confidence Matrix**
