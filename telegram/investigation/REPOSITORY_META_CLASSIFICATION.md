# REPOSITORY_META_CLASSIFICATION

**Document ID:** META002-REPO-CLASS

**Title:** Repository Meta-Classification

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Meta-Ontology Investigation

---

# Purpose

This document reclassifies every repository concept using the reconstructed meta-ontology.

---

# Repository Meta-Classification

## Publication

**Meta-Layer:** 1 + 3 + 4 (Ontological + Semantic + Communicative)

**Primary Category:** Object

**Secondary Categories:** Information, Representation

**Evidence:**

- Has identity (Territory + Date + Template) — Object
- Contains Information (content) — Information
- Is Represented as Telegram Message — Representation

**Reasoning:** Publication is an Object that contains Information and is Represented for Communication.

---

## Issue

**Meta-Layer:** 1 + 5 (Ontological + Structural)

**Primary Category:** Object

**Secondary Categories:** Collection

**Evidence:**

- Has identity (Calendar day) — Object
- Contains Publications — Collection

**Reasoning:** Issue is an Object that contains a Collection of Publications.

---

## Journal

**Meta-Layer:** 1 + 5 (Ontological + Structural)

**Primary Category:** Collection

**Secondary Categories:** Object

**Evidence:**

- Contains Issues — Collection
- Has identity (continuous publication) — Object

**Reasoning:** Journal is a Collection of Issues that also has identity.

---

## Publication Engine

**Meta-Layer:** 1 + 6 (Ontological + Social)

**Primary Category:** Object

**Secondary Categories:** Process, Role

**Evidence:**

- Has identity (component name) — Object
- Performs generation — Process
- Implements Publisher Role — Role

**Reasoning:** Publication Engine is an Object that performs a Process and implements a Role.

---

## Parser

**Meta-Layer:** 1 + 6 (Ontological + Social)

**Primary Category:** Object

**Secondary Categories:** Process, Role

**Evidence:**

- Has identity (component name) — Object
- Performs data retrieval — Process
- Implements Data Retrieval Role — Role

**Reasoning:** Parser is an Object that performs a Process and implements a Role.

---

## Schedule

**Meta-Layer:** 1 + 2 (Ontological + Epistemological)

**Primary Category:** Object

**Secondary Categories:** Information

**Evidence:**

- Has identity (unique per generation) — Object
- Contains Information (outage schedule) — Information

**Reasoning:** Schedule is an Object that contains Information about electricity availability.

---

## Normalized Dataset

**Meta-Layer:** 2 + 4 (Epistemological + Communicative)

**Primary Category:** Information

**Secondary Categories:** Representation

**Evidence:**

- Structured Information — Information
- Machine-readable representation — Representation

**Reasoning:** Normalized Dataset is Information that is Represented in machine-readable form.

---

## Interpretation Result

**Meta-Layer:** 2 + 4 (Epistemological + Communicative)

**Primary Category:** Information

**Secondary Categories:** Representation

**Evidence:**

- Information for residents — Information
- Normalized representation — Representation

**Reasoning:** Interpretation Result is Information Represented for resident consumption.

---

## Telegram Message

**Meta-Layer:** 4 (Communicative)

**Primary Category:** Carrier

**Secondary Categories:** Representation

**Evidence:**

- Medium holding Publication — Carrier
- Portrays Publication content — Representation

**Reasoning:** Telegram Message is a Carrier that holds a Representation of Publication.

---

## Publication Package

**Meta-Layer:** 1 + 5 (Ontological + Structural)

**Primary Category:** Collection

**Secondary Categories:** Object

**Evidence:**

- Contains Publications — Collection
- Has identity (Reporting Period) — Object

**Reasoning:** Publication Package is a Collection of Publications with identity.

---

## Territory

**Meta-Layer:** 1 + 5 (Ontological + Structural)

**Primary Category:** Object

**Secondary Categories:** Boundary

**Evidence:**

- Has identity (administrative name) — Object
- Defines scope — Boundary

**Reasoning:** Territory is an Object that defines geographic scope.

---

## Address

**Meta-Layer:** 1 (Ontological)

**Primary Category:** Object

**Secondary Categories:** —

**Evidence:**

- Has identity (official designation) — Object

**Reasoning:** Address is a simple Object representing a location.

---

## Processing Cycle

**Meta-Layer:** 7 + 1 (Temporal + Ontological)

**Primary Category:** Lifecycle

**Secondary Categories:** Process

**Evidence:**

- Sequence of actions — Process
- One complete execution — temporal

**Reasoning:** Processing Cycle is a Process that represents one execution.

---

## Historical Archive

**Meta-Layer:** 1 + 5 (Ontological + Structural)

**Primary Category:** Collection

**Secondary Categories:** Carrier

**Evidence:**

- Preserves records — Collection
- Stores Information — Carrier

**Reasoning:** Historical Archive is a Collection that acts as Carrier for historical Information.

---

## Open Data

**Meta-Layer:** 2 + 3 (Epistemological + Semantic)

**Primary Category:** Information

**Secondary Categories:** Evidence

**Evidence:**

- Officially published Information — Information
- Provides evidence of Reality — Evidence

**Reasoning:** Open Data is Information that serves as Evidence of Reality.

---

## Role

**Meta-Layer:** 6 (Social)

**Primary Category:** Role

**Secondary Categories:** —

**Evidence:**

- Describes responsibility — Role

**Reasoning:** Role is a pure Social category describing participation.

---

# Meta-Classification Summary

| Meta-Layer | Count | Examples |
|------------|-------|----------|
| 1: Ontological | 12 | Publication, Issue, Territory, Address |
| 2: Epistemological | 3 | Schedule, Normalized Dataset, Interpretation Result |
| 3: Semantic | 1 | Open Data |
| 4: Communicative | 1 | Telegram Message |
| 5: Structural | 4 | Journal, Publication Package, Historical Archive, Territory |
| 6: Social | 1 | Role |
| 7: Temporal | 1 | Processing Cycle |
| Mixed | 14 | Publication Engine, Parser, etc. |

---

# Key Insight

**14 of 36 concepts MIX multiple meta-levels.**

**This confirms that META-001's flat classification was insufficient.**

**The meta-ontology reveals that concepts exist across multiple levels simultaneously.**

---

# End of Repository Meta-Classification
