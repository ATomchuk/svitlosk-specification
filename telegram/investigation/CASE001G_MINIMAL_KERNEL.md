# CASE001G_MINIMAL_KERNEL

**Document ID:** CASE001G-KERNEL

**Title:** Minimal Semantic Kernel of the Telegram Publishing Subsystem

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Minimal Kernel Investigation

---

# Purpose

This document discovers the MINIMAL semantic kernel required for the Telegram Publishing Subsystem to exist.

---

# Part I: Complete Concept Inventory

## Real-World Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 1 | Community | Real-world | GLOSSARY.md §4 |
| 2 | Territory | Real-world | GLOSSARY.md §4 |
| 3 | Administrative Centre | Real-world | GLOSSARY.md §4 |
| 4 | Starosta District | Real-world | GLOSSARY.md §4 |
| 5 | Settlement | Real-world | GLOSSARY.md §4 |
| 6 | Street | Real-world | TERRITORIAL_MODEL.md |
| 7 | Address | Real-world | GLOSSARY.md §4 |
| 8 | Queue | Real-world | GLOSSARY.md §5 |
| 9 | Subqueue | Real-world | GLOSSARY.md §5 |
| 10 | Planned Power Outage | Real-world | GLOSSARY.md §5 |
| 11 | Emergency Power Outage | Real-world | GLOSSARY.md §5 |
| 12 | Open Data | Real-world | GLOSSARY.md §2 |
| 13 | Data Source | Real-world | GLOSSARY.md §2 |
| 14 | DSO | Real-world | GLOSSARY.md §2 |

---

## Business Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 15 | Journal | Business | TJS-000 §4 |
| 16 | Issue | Business | TJS-000 §4 |
| 17 | Publication | Business | GLOSSARY.md §3 |
| 18 | Publication Package | Business | GLOSSARY.md §3 |
| 19 | Editorial Policy | Business | GLOSSARY.md §3 |
| 20 | Resident | Business | GLOSSARY.md §6 |
| 21 | Information Consumer | Business | GLOSSARY.md §6 |

---

## Information Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 22 | Normalized Dataset | Information | TJS-010 §3.3 |
| 23 | Schedule | Information | GLOSSARY.md §5 |
| 24 | Graphic | Information | TJS-022 |
| 25 | Interpretation Result | Information | GLOSSARY.md §2 |
| 26 | Parsed Data | Information | GLOSSARY.md §2 |

---

## Architectural Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 27 | Publication Engine | Architectural | GLOSSARY.md §7 |
| 28 | Parser | Architectural | GLOSSARY.md §7 |
| 29 | Publisher (Role) | Architectural | GLOSSARY.md §7 |
| 30 | Telegram Publisher | Architectural | TJS-010 §3.1 |
| 31 | Schedule Generator | Architectural | TJS-010 §3.1 |
| 32 | Graphic Generator | Architectural | TJS-010 §3.1 |
| 33 | Data Storage | Architectural | TJS-010 §3.1 |
| 34 | Telegram Channel | Architectural | TJS-010 §3.1 |

---

## Representation Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 35 | Telegram Message | Representation | TJS-000A §10 |
| 36 | Repository Object | Representation | TJS-021 §3.1 |
| 37 | Historical Record | Representation | GLOSSARY.md §2 |
| 38 | Daily Snapshot | Representation | DATA_MODEL.md |
| 39 | Analytics Record | Representation | DATA_MODEL.md |

---

## Process Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 40 | Data Retrieval | Process | GLOSSARY.md §2 |
| 41 | Interpretation | Process | GLOSSARY.md §2 |
| 42 | Rendering | Process | GLOSSARY.md §3 |
| 43 | Distribution | Process | GLOSSARY.md §3 |
| 44 | Processing Cycle | Process | GLOSSARY.md §2 |

---

## State Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 45 | Generated | State | TJS-021 §4.1 |
| 46 | Published | State | TJS-021 §4.2 |
| 47 | Updated | State | TJS-021 §4.3 |
| 48 | Archived | State | TJS-021 §4.4 |
| 49 | Removed | State | TJS-021 §4.5 |

---

## Relationship Objects

| # | Concept | Category | Evidence |
|---|---------|----------|----------|
| 50 | Territorial Coverage | Relationship | GLOSSARY.md §4 |
| 51 | Reporting Period | Relationship | GLOSSARY.md §2 |
| 52 | Publication Channel | Relationship | GLOSSARY.md §3 |

---

# Part II: Reduction Experiments

## Experiment 1: Remove Publication

**What disappeared:** The central output concept

**What broke:** Glossary, Data Model, Semantic Model, Lifecycle, Publishing Model, Editorial System, Graphic Model

**What had to be replaced:** Nothing — cannot be replaced

**Can another concept absorb its responsibility?** NO

**Evidence:** CASE-001F proves Publication cannot be removed

---

## Experiment 2: Remove Issue

**What disappeared:** Daily grouping concept

**What broke:** Semantic hierarchy, Journal structure, daily organization

**What had to be replaced:** Nothing — Journal can exist without Issues (but loses daily structure)

**Can another concept absorb its responsibility?** PARTIALLY — Reporting Period could absorb temporal grouping

**Evidence:** CASE-002A shows Issue depends on Publication

---

## Experiment 3: Remove Journal

**What disappeared:** Continuous publication concept

**What broke:** Ultimate container, long-term storage, editorial identity

**What had to be replaced:** Nothing — system could exist without Journal concept

**Can another concept absorb its responsibility?** PARTIALLY — Publication Package could absorb collection role

**Evidence:** Journal is a high-level abstraction

---

## Experiment 4: Remove Publication Package

**What disappeared:** Collection concept

**What broke:** Grouping mechanism, delivery batching

**What had to be replaced:** Nothing — Publications could be delivered individually

**Can another concept absorb its responsibility?** YES — Publications could be delivered one by one

**Evidence:** Publication Package is a convenience abstraction

---

## Experiment 5: Remove Parser

**What disappeared:** Data retrieval component

**What broke:** Data flow — no data enters system

**What had to be replaced:** Nothing — cannot function without data retrieval

**Can another concept absorb its responsibility?** NO — data retrieval is essential

**Evidence:** Parser is the only entry point for external data

---

## Experiment 6: Remove Publication Engine

**What disappeared:** Core processing component

**What broke:** Data flow — no Publications generated

**What had to be replaced:** Nothing — cannot function without generation

**Can another concept absorb its responsibility?** NO — generation is essential

**Evidence:** Publication Engine is the only component that generates Publications

---

## Experiment 7: Remove Schedule Generator

**What disappeared:** Schedule generation

**What broke:** Schedule data not produced

**What had to be replaced:** Nothing — Publications could be generated without schedules

**Can another concept absorb its responsibility?** PARTIALLY — Publication Engine could generate schedules internally

**Evidence:** Schedule Generator is a specialized component

---

## Experiment 8: Remove Graphic Generator

**What disappeared:** Graphic generation

**What broke:** Visual materials not produced

**What had to be replaced:** Nothing — Publications could be text-only

**Can another concept absorb its responsibility?** PARTIALLY — Publication Engine could generate graphics internally

**Evidence:** Graphic Generator is a specialized component

---

## Experiment 9: Remove Telegram Publisher

**What disappeared:** Telegram delivery

**What broke:** Publications not delivered to Telegram

**What had to be replaced:** Nothing — Publications could be stored without delivery

**Can another concept absorb its responsibility?** PARTIALLY — Publication Engine could deliver directly

**Evidence:** Telegram Publisher is platform-specific

---

## Experiment 10: Remove Telegram Channel

**What disappeared:** Publication channel

**What broke:** Publications not visible to readers

**What had to be replaced:** Nothing — Publications could exist without channel

**Can another concept absorb its responsibility?** YES — other channels could be used

**Evidence:** Telegram Channel is one of many possible channels

---

## Experiment 11: Remove Normalized Dataset

**What disappeared:** Intermediate data format

**What broke:** Data flow between Parser and Publication Engine

**What had to be replaced:** Nothing — Parser could feed directly to Engine

**Can another concept absorb its responsibility?** YES — Parsed Data could be used directly

**Evidence:** Normalized Dataset is an implementation detail

---

## Experiment 12: Remove Schedule

**What disappeared:** Electricity availability information

**What broke:** Schedule-based Publications not generated

**What had to be replaced:** Nothing — Publications could be generated without schedules

**Can another concept absorb its responsibility?** NO — schedule information is essential for outage Publications

**Evidence:** Schedule contains essential domain information

---

## Experiment 13: Remove Graphic

**What disappeared:** Visual materials

**What broke:** Visual Publications not generated

**What had to be replaced:** Nothing — Publications could be text-only

**Can another concept absorb its responsibility?** NO — graphics are distinct from text

**Evidence:** Graphics are a different format

---

## Experiment 14: Remove Time Interval

**What disappeared:** Time representation

**What broke:** Outage timing not representable

**What had to be replaced:** Nothing — cannot represent outages without time

**Can another concept absorb its responsibility?** NO — time is essential

**Evidence:** Time intervals are fundamental to outage information

---

## Experiment 15: Remove Address

**What disappeared:** Location representation

**What broke:** Outage locations not representable

**What had to be replaced:** Nothing — cannot represent outages without location

**Can another concept absorb its responsibility?** NO — location is essential

**Evidence:** Addresses are fundamental to outage information

---

## Experiment 16: Remove Territory

**What disappeared:** Publication unit

**What broke:** Territorial organization lost

**What had to be replaced:** Nothing — Publications could be unorganized

**Can another concept absorb its responsibility?** PARTIALLY — Address could be used directly

**Evidence:** Territory is a grouping abstraction

---

## Experiment 17: Remove Community

**What disappeared:** Top-level territorial scope

**What broke:** Geographic scope undefined

**What had to be replaced:** Nothing — system could operate without explicit scope

**Can another concept absorb its responsibility?** YES — Territory could imply scope

**Evidence:** Community is a high-level abstraction

---

## Experiment 18: Remove Settlement

**What disappeared:** Populated place

**What broke:** Settlement-level organization lost

**What had to be replaced:** Nothing — Addresses could be used directly

**Can another concept absorb its responsibility?** YES — Address could be used directly

**Evidence:** Settlement is a grouping abstraction

---

## Experiment 19: Remove Street

**What disappeared:** Road name

**What broke:** Street-level organization lost

**What had to be replaced:** Nothing — Addresses could be used directly

**Can another concept absorb its responsibility?** YES — Address could be used directly

**Evidence:** Street is a grouping abstraction

---

# Part III: Reduction Results Summary

| Concept | Removed? | Replaced? | Absorbed? | Essential? |
|---------|----------|-----------|-----------|------------|
| Publication | NO | NO | NO | YES |
| Issue | PARTIALLY | PARTIALLY | Reporting Period | NO |
| Journal | PARTIALLY | NO | Publication Package | NO |
| Publication Package | YES | NO | Individual delivery | NO |
| Parser | NO | NO | NO | YES |
| Publication Engine | NO | NO | NO | YES |
| Schedule Generator | PARTIALLY | NO | Engine internal | NO |
| Graphic Generator | PARTIALLY | NO | Engine internal | NO |
| Telegram Publisher | PARTIALLY | NO | Engine direct | NO |
| Telegram Channel | YES | NO | Other channels | NO |
| Normalized Dataset | YES | NO | Parsed Data | NO |
| Schedule | NO | NO | NO | YES |
| Graphic | YES | NO | Text-only | NO |
| Time Interval | NO | NO | NO | YES |
| Address | NO | NO | NO | YES |
| Territory | PARTIALLY | NO | Address direct | NO |
| Community | YES | NO | Territory implies | NO |
| Settlement | YES | NO | Address direct | NO |
| Street | YES | NO | Address direct | NO |

---

# Part IV: Minimal Kernel

## Concepts That Satisfy ALL Conditions

1. Cannot be removed
2. Cannot be derived
3. Cannot be replaced
4. Cannot be merged
5. Required in every possible architecture

| # | Concept | Evidence |
|---|---------|----------|
| 1 | Publication | CASE-001F proves cannot be removed |
| 2 | Parser | Only entry point for external data |
| 3 | Publication Engine | Only component that generates Publications |
| 4 | Schedule | Contains essential domain information |
| 5 | Time Interval | Fundamental to outage information |
| 6 | Address | Fundamental to outage information |
| 7 | Open Data | Source of all information |
| 8 | Data Source | Origin of all information |

---

# Part V: Supporting Layer

## Derived Concepts

| # | Concept | Derived From |
|---|---------|--------------|
| 1 | Publication Package | Collection of Publications |
| 2 | Interpretation Result | Output of Interpretation |
| 3 | Parsed Data | Output of Parser |
| 4 | Normalized Dataset | Normalized Parsed Data |
| 5 | Graphic | Visual representation of Schedule |
| 6 | Daily Snapshot | Archived operational data |
| 7 | Analytics Record | Derived from Historical Data |

---

## Projection Concepts

| # | Concept | Projects From |
|---|---------|---------------|
| 1 | Telegram Message | Publication on Telegram |
| 2 | Repository Object | Publication in storage |
| 3 | Historical Record | Publication in archive |

---

## Representation Concepts

| # | Concept | Represents |
|---|---------|------------|
| 1 | Telegram Message | Publication on platform |
| 2 | Repository Object | Publication in database |
| 3 | Historical Record | Publication in history |
| 4 | Daily Snapshot | Operational data in archive |

---

## Implementation Concepts

| # | Concept | Implementation Of |
|---|---------|-------------------|
| 1 | Publication Engine | Publisher Role |
| 2 | Parser | Data Retrieval Role |
| 3 | Telegram Publisher | Publisher Role (Telegram) |
| 4 | Schedule Generator | Schedule generation |
| 5 | Graphic Generator | Graphic generation |
| 6 | Data Storage | Persistent storage |
| 7 | Telegram Channel | Publication channel |

---

## Convenience Abstractions

| # | Concept | Abstraction Of |
|---|---------|----------------|
| 1 | Publication Package | Grouping of Publications |
| 2 | Issue | Daily grouping |
| 3 | Journal | Continuous publication |
| 4 | Territory | Geographic grouping |
| 5 | Community | Top-level scope |
| 6 | Settlement | Geographic grouping |
| 7 | Street | Geographic grouping |

---

# End of Minimal Kernel
