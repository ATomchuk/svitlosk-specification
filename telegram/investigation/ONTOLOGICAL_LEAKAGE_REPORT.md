# ONTOLOGICAL_LEAKAGE_REPORT

**Document ID:** A66-LEAKAGE

**Title:** Ontological Leakage Report

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Dual Kernel Investigation

---

# Purpose

This document identifies every place where Architecture appears inside Domain or Domain appears inside Architecture.

---

# Leakage Type 1: Architecture Inside Domain

## Leakage 1-001: Publication Engine in GLOSSARY.md

**Location:** GLOSSARY.md §7

**Evidence:** "Publication Engine — A software Component responsible for publication generation and distribution"

**Is Architecture?** YES — Component is architectural concept

**Is in Domain?** YES — GLOSSARY.md defines domain terminology

**Intentional?** UNCLEAR — GLOSSARY.md §7 explicitly defines "Architecture Vocabulary"

**Harmful?** NO — clearly separated in §7

**Improves Understanding?** YES — provides architectural context

---

## Leakage 1-002: Parser in GLOSSARY.md

**Location:** GLOSSARY.md §2

**Evidence:** "Parser — A software Component responsible for retrieving Open Data"

**Is Architecture?** YES — Component is architectural concept

**Is in Domain?** YES — GLOSSARY.md defines domain terminology

**Intentional?** UNCLEAR — Parser is used in domain context (data retrieval)

**Harmful?** PARTIALLY — Parser is both architectural Component and domain concept (Data Retrieval)

**Improves Understanding?** PARTIALLY — creates ambiguity

---

## Leakage 1-003: Telegram Message in Semantic Model

**Location:** TJS-000 §4

**Evidence:** "Telegram is the primary publication channel used to deliver Publications"

**Is Architecture?** YES — Telegram is platform-specific

**Is in Domain?** YES — TJS-000 defines semantic model

**Intentional?** YES — TJS-000 §3 explicitly states "Telegram itself SHALL NOT be considered the Journal"

**Harmful?** NO — clearly positioned as platform, not domain

**Improves Understanding?** YES — provides delivery context

---

## Leakage 1-004: Publication Package in GLOSSARY.md

**Location:** GLOSSARY.md §3

**Evidence:** "Publication Package — The complete collection of Publications generated during one Reporting Period"

**Is Architecture?** PARTIALLY — collection is architectural pattern

**Is in Domain?** YES — GLOSSARY.md defines domain terminology

**Intentional?** UNCLEAR — Publication Package is used in domain context

**Harmful?** PARTIALLY — creates ambiguity about whether Package is domain or architecture

**Improves Understanding?** YES — provides grouping context

---

## Leakage 1-005: Processing Cycle in GLOSSARY.md

**Location:** GLOSSARY.md §2

**Evidence:** "Processing Cycle — One complete execution of the information pipeline"

**Is Architecture?** YES — pipeline is architectural concept

**Is in Domain?** YES — GLOSSARY.md defines domain terminology

**Intentional?** UNCLEAR — Processing Cycle is used in domain context (traceability)

**Harmful?** PARTIALLY — creates ambiguity about whether cycle is domain or architecture

**Improves Understanding?** YES — provides processing context

---

# Leakage Type 2: Domain Inside Architecture

## Leakage 2-001: Publication in Data Flow

**Location:** TJS-010 §3.3

**Evidence:** "External Data Sources → Parser → Normalized Dataset → Publication Engine → Publication Package → Telegram Publisher → Telegram Channel → Subscribers"

**Is Domain?** YES — Publication is domain concept

**Is in Architecture?** YES — Data Flow is architectural concept

**Intentional?** YES — Architecture implements Domain

**Harmful?** NO — this is the correct relationship

**Improves Understanding?** YES — shows how Architecture implements Domain

---

## Leakage 2-002: Schedule in Component Responsibilities

**Location:** TJS-010 §4.5

**Evidence:** "Schedule Generator — Owns: Schedule generation, outage period calculation"

**Is Domain?** YES — Schedule is domain concept

**Is in Architecture?** YES — Component Responsibilities is architectural concept

**Intentional?** YES — Architecture implements Domain

**Harmful?** NO — this is the correct relationship

**Improves Understanding?** YES — shows how Architecture implements Domain

---

## Leakage 2-003: Address in Data Model

**Location:** DATA_MODEL.md § "Core Logical Entities"

**Evidence:** "Address — Logical reference to a physical location served by the project"

**Is Domain?** YES — Address is domain concept

**Is in Architecture?** YES — Data Model is architectural concept

**Intentional?** YES — Architecture models Domain

**Harmful?** NO — this is the correct relationship

**Improves Understanding?** YES — shows how Architecture models Domain

---

## Leakage 2-004: Territory in Territorial Model

**Location:** TERRITORIAL_MODEL.md

**Evidence:** "Territory — A publication unit representing either the Administrative Centre or one Starosta District"

**Is Domain?** YES — Territory is domain concept (geographic)

**Is in Architecture?** PARTIALLY — "publication unit" is architectural framing

**Intentional?** PARTIALLY — Territory is defined as "logical publication entity"

**Harmful?** PARTIALLY — "publication unit" blurs domain/architecture boundary

**Improves Understanding?** YES — provides publication context

---

## Leakage 2-005: Resident in Users Section

**Location:** GLOSSARY.md §6

**Evidence:** "Resident — A person using SvitloSk to obtain official information"

**Is Domain?** YES — Resident is domain concept (person)

**Is in Architecture?** NO — Users section is domain-focused

**Intentional?** YES — Residents are domain stakeholders

**Harmful?** NO — correctly positioned in domain

**Improves Understanding?** YES — provides user context

---

# Leakage Summary

| Type | Count | Examples |
|------|-------|----------|
| Architecture inside Domain | 5 | Publication Engine, Parser, Telegram, Publication Package, Processing Cycle |
| Domain inside Architecture | 5 | Publication, Schedule, Address, Territory, Resident |
| **Total** | **10** | |

---

# Leakage Assessment

| Assessment | Count |
|------------|-------|
| Intentional | 5 |
| Harmful | 0 |
| Improves Understanding | 8 |
| Unclear Intent | 3 |

---

# Key Insight

**Ontological leakage exists but is largely intentional and harmless.**

**Architecture concepts appear in Domain context to provide implementation context.**

**Domain concepts appear in Architecture context to show what Architecture implements.**

**No harmful leakage was found.**

---

# End of Ontological Leakage Report
