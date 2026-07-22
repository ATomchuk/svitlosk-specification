# CASE001G_REDUCTION_EXPERIMENTS

**Document ID:** CASE001G-REDUCTIONS

**Title:** Reduction Experiments

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Minimal Kernel Investigation

---

# Purpose

This document performs multiple reduction approaches to find the minimal kernel.

---

# Reduction A: Business-First Ontology

## Focus

What does the business need?

## Business Requirements

1. Residents need information about power outages
2. Information must be organized by territory
3. Information must be timely
4. Information must be accurate
5. Information must be accessible

## Minimal Concepts

| # | Concept | Reason |
|---|---------|--------|
| 1 | Publication | Business output |
| 2 | Territory | Geographic organization |
| 3 | Address | Location detail |
| 4 | Schedule | Outage information |
| 5 | Time Interval | Timing information |
| 6 | Resident | Business beneficiary |
| 7 | Open Data | Business source |

## Kernel Size: 7 concepts

---

# Reduction B: Information-First Ontology

## Focus

What information must exist?

## Information Requirements

1. Source data must exist
2. Data must be processed
3. Information must be structured
4. Information must be delivered
5. Information must be preserved

## Minimal Concepts

| # | Concept | Reason |
|---|---------|--------|
| 1 | Open Data | Source information |
| 2 | Data Source | Information origin |
| 3 | Publication | Processed information |
| 4 | Schedule | Domain information |
| 5 | Address | Location information |
| 6 | Time Interval | Timing information |
| 7 | Normalized Dataset | Processed data |

## Kernel Size: 7 concepts

---

# Reduction C: DDD-First Ontology

## Focus

What are the domain aggregates?

## DDD Analysis

| # | Concept | DDD Role |
|---|---------|----------|
| 1 | Publication | Aggregate Root |
| 2 | Territory | Value Object |
| 3 | Address | Value Object |
| 4 | Schedule | Entity |
| 5 | Time Interval | Value Object |
| 6 | Open Data | External concept |
| 7 | Data Source | External concept |

## Minimal Concepts

| # | Concept | Reason |
|---|---------|--------|
| 1 | Publication | Aggregate Root |
| 2 | Territory | Value Object |
| 3 | Address | Value Object |
| 4 | Schedule | Entity |
| 5 | Time Interval | Value Object |
| 6 | Open Data | External input |
| 7 | Data Source | External origin |

## Kernel Size: 7 concepts

---

# Reduction D: Event-First Ontology

## Focus

What events occur?

## Events

1. Data is retrieved
2. Data is processed
3. Publication is generated
4. Publication is delivered
5. Publication is archived

## Minimal Concepts

| # | Concept | Reason |
|---|---------|--------|
| 1 | Publication | Event output |
| 2 | Data Retrieval | Event trigger |
| 3 | Processing Cycle | Event sequence |
| 4 | Schedule | Event data |
| 5 | Address | Event location |
| 6 | Time Interval | Event timing |
| 7 | Open Data | Event source |

## Kernel Size: 7 concepts

---

# Reduction E: Communication-First Ontology

## Focus

What communication must occur?

## Communication Requirements

1. System must communicate with Data Source
2. System must process information
3. System must communicate with residents
4. System must preserve history

## Minimal Concepts

| # | Concept | Reason |
|---|---------|--------|
| 1 | Publication | Communication output |
| 2 | Parser | Communication with Data Source |
| 3 | Publication Engine | Communication processing |
| 4 | Telegram Channel | Communication with residents |
| 5 | Schedule | Communication content |
| 6 | Address | Communication location |
| 7 | Time Interval | Communication timing |

## Kernel Size: 7 concepts

---

# Reduction Comparison

| Reduction | Kernel Size | Concepts |
|-----------|-------------|----------|
| A: Business-first | 7 | Publication, Territory, Address, Schedule, Time Interval, Resident, Open Data |
| B: Information-first | 7 | Open Data, Data Source, Publication, Schedule, Address, Time Interval, Normalized Dataset |
| C: DDD-first | 7 | Publication, Territory, Address, Schedule, Time Interval, Open Data, Data Source |
| D: Event-first | 7 | Publication, Data Retrieval, Processing Cycle, Schedule, Address, Time Interval, Open Data |
| E: Communication-first | 7 | Publication, Parser, Publication Engine, Telegram Channel, Schedule, Address, Time Interval |

---

# End of Reduction Experiments
