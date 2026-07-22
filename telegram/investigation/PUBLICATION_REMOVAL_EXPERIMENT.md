# PUBLICATION_REMOVAL_EXPERIMENT

**Document ID:** CASE001F-REMOVAL

**Title:** Publication Removal Experiment

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Publication Existence Investigation

---

# Purpose

This document attempts to remove Publication and documents the consequences.

---

# Experiment: Remove Publication

## Step 1: Remove Publication from Glossary

**Action:** Remove "Publication" definition from GLOSSARY.md §3

**Consequence:**

- GLOSSARY.md loses its central concept
- Publication Package has no parent concept
- Publisher has no output concept
- Publication Channel has no content concept
- All references to Publication become broken

**Evidence:** GLOSSARY.md §3 defines Publication, Publication Package, Tomorrow Publication, Telegram Journal, Editorial Policy, Publication Channel, Publisher, Publication Engine, Publisher Role, Publication Pipeline, Rendering, Distribution, Publication Lifecycle

---

## Step 2: Remove Publication from Data Model

**Action:** Remove "Publication" from DATA_MODEL.md

**Consequence:**

- DATA_MODEL.md loses "Publication Entities" category
- Publication Package has no element concept
- Data flow has no output concept
- Traceability has no target concept

**Evidence:** DATA_MODEL.md defines Publication as "Logical representation of interpreted information prepared for public distribution"

---

## Step 3: Remove Publication from Semantic Model

**Action:** Remove "Publication" from TJS-000 §4

**Consequence:**

- Semantic hierarchy becomes Journal → Issue → Telegram (no Publication)
- Issue has no child concept
- Journal has no content concept
- Telegram has no input concept

**Evidence:** TJS-000 §4 defines hierarchy: Journal → Issue → Publication → Telegram

---

## Step 4: Remove Publication from Lifecycle

**Action:** Remove Publication lifecycle from TJS-021

**Consequence:**

- TJS-021 loses its primary subject
- Lifecycle states (Generated, Published, Updated, Archived, Removed) have no subject
- Lifecycle transitions have no subject
- Issue lifecycle has no related lifecycle

**Evidence:** TJS-021 §4 defines lifecycle states for Publication

---

## Step 5: Remove Publication from Publishing Model

**Action:** Remove Publication from TJS-010

**Consequence:**

- Data flow has no output
- Publication Engine has no product
- Telegram Publisher has nothing to deliver
- Subscribers receive nothing

**Evidence:** TJS-010 §3.3 defines data flow ending at Subscribers

---

## Step 6: Remove Publication from Editorial System

**Action:** Remove Publication from TJS-020

**Consequence:**

- Editorial principles have no subject
- Editorial integrity has no target
- Editorial behaviour has no output

**Evidence:** TJS-020 §4.5 defines "Issue Integrity" for daily publications

---

## Step 7: Remove Publication from Graphic Model

**Action:** Remove Publication from TJS-022

**Consequence:**

- Graphic publications have no parent concept
- Graphic taxonomy has no root
- Graphic invariants have no subject

**Evidence:** TJS-022 defines "Graphic publications transform normalized outage data"

---

## Step 8: Repair Architecture

**Action:** Try to repair the architecture without Publication

**Attempt 1: Replace with "Message"**

- Problem: "Message" is platform-specific (Telegram)
- Problem: "Message" has no territorial identity
- Problem: "Message" is not mentioned in any specification

**Attempt 2: Replace with "Content"**

- Problem: "Content" is too generic
- Problem: "Content" has no lifecycle
- Problem: "Content" has no ownership

**Attempt 3: Replace with "Output"**

- Problem: "Output" is too generic
- Problem: "Output" has no identity
- Problem: "Output" has no integrity requirements

**Result:** IMPOSSIBLE to repair without Publication

---

# Conclusion

**Publication CANNOT be removed.**

**Removing Publication breaks:**

1. Glossary
2. Data Model
3. Semantic Model
4. Lifecycle
5. Publishing Model
6. Editorial System
7. Graphic Model
8. Data flow
9. Identity model
10. Ownership model

---

# End of Removal Experiment
