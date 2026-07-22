# SEMANTIC_KERNEL_COMPARISON

**Document ID:** CASE001G-COMPARISON

**Title:** Semantic Kernel Comparison

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Minimal Kernel Investigation

---

# Purpose

This document compares all reduction kernels to find stable and unstable concepts.

---

# All Kernels

## Kernel A: Business-first

| # | Concept |
|---|---------|
| 1 | Publication |
| 2 | Territory |
| 3 | Address |
| 4 | Schedule |
| 5 | Time Interval |
| 6 | Resident |
| 7 | Open Data |

---

## Kernel B: Information-first

| # | Concept |
|---|---------|
| 1 | Open Data |
| 2 | Data Source |
| 3 | Publication |
| 4 | Schedule |
| 5 | Address |
| 6 | Time Interval |
| 7 | Normalized Dataset |

---

## Kernel C: DDD-first

| # | Concept |
|---|---------|
| 1 | Publication |
| 2 | Territory |
| 3 | Address |
| 4 | Schedule |
| 5 | Time Interval |
| 6 | Open Data |
| 7 | Data Source |

---

## Kernel D: Event-first

| # | Concept |
|---|---------|
| 1 | Publication |
| 2 | Data Retrieval |
| 3 | Processing Cycle |
| 4 | Schedule |
| 5 | Address |
| 6 | Time Interval |
| 7 | Open Data |

---

## Kernel E: Communication-first

| # | Concept |
|---|---------|
| 1 | Publication |
| 2 | Parser |
| 3 | Publication Engine |
| 4 | Telegram Channel |
| 5 | Schedule |
| 6 | Address |
| 7 | Time Interval |

---

# Comparison Matrix

| Concept | Kernel A | Kernel B | Kernel C | Kernel D | Kernel E | In ALL? |
|---------|----------|----------|----------|----------|----------|---------|
| Publication | YES | YES | YES | YES | YES | YES |
| Territory | YES | NO | YES | NO | NO | NO |
| Address | YES | YES | YES | YES | YES | YES |
| Schedule | YES | YES | YES | YES | YES | YES |
| Time Interval | YES | YES | YES | YES | YES | YES |
| Resident | YES | NO | NO | NO | NO | NO |
| Open Data | YES | YES | YES | YES | NO | NO |
| Data Source | NO | YES | YES | NO | NO | NO |
| Normalized Dataset | NO | YES | NO | NO | NO | NO |
| Data Retrieval | NO | NO | NO | YES | NO | NO |
| Processing Cycle | NO | NO | NO | YES | NO | NO |
| Parser | NO | NO | NO | NO | YES | NO |
| Publication Engine | NO | NO | NO | NO | YES | NO |
| Telegram Channel | NO | NO | NO | NO | YES | NO |

---

# Stable Concepts (In ALL Kernels)

| # | Concept | Kernels |
|---|---------|---------|
| 1 | Publication | A, B, C, D, E |
| 2 | Address | A, B, C, D, E |
| 3 | Schedule | A, B, C, D, E |
| 4 | Time Interval | A, B, C, D, E |

---

# Unstable Concepts (In SOME Kernels)

| # | Concept | Kernels | Absent From |
|---|---------|---------|-------------|
| 1 | Territory | A, C | B, D, E |
| 2 | Open Data | A, B, C, D | E |
| 3 | Data Source | B, C | A, D, E |
| 4 | Resident | A | B, C, D, E |
| 5 | Normalized Dataset | B | A, C, D, E |
| 6 | Data Retrieval | D | A, B, C, E |
| 7 | Processing Cycle | D | A, B, C, E |
| 8 | Parser | E | A, B, C, D |
| 9 | Publication Engine | E | A, B, C, D |
| 10 | Telegram Channel | E | A, B, C, D |

---

# Candidate Concepts for Future Removal

| # | Concept | Reason |
|---|---------|--------|
| 1 | Territory | Not in all kernels; can be replaced by Address |
| 2 | Open Data | Not in Kernel E; could be implicit |
| 3 | Data Source | Not in all kernels; could be implicit |
| 4 | Resident | Only in Kernel A; could be implicit |
| 5 | Normalized Dataset | Only in Kernel B; implementation detail |
| 6 | Data Retrieval | Only in Kernel D; could be implicit |
| 7 | Processing Cycle | Only in Kernel D; could be implicit |
| 8 | Parser | Only in Kernel E; could be implicit |
| 9 | Publication Engine | Only in Kernel E; could be implicit |
| 10 | Telegram Channel | Only in Kernel E; could be implicit |

---

# Key Insight

**4 concepts appear in ALL kernels:**

1. Publication
2. Address
3. Schedule
4. Time Interval

**These 4 concepts form the ABSOLUTE MINIMAL KERNEL.**

**Every reduction approach independently arrives at these 4 concepts.**

---

# End of Semantic Kernel Comparison
