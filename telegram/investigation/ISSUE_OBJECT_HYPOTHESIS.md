# ISSUE_OBJECT_HYPOTHESIS

**Document ID:** CASE002B-H1

**Title:** Issue Object Hypothesis

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Issue Ontology Investigation

---

# Purpose

This document investigates Hypothesis H1: Issue IS an Object.

---

# Hypothesis H1: Issue IS an Object

**Definition:** Issue is a thing that exists, has identity, has properties, and has lifecycle.

---

# Supporting Evidence

## Evidence 1: Issue Has Existence

**Source:** TJS-000 §4

**Quote:** "Issue represents one editorial edition of the Journal for a single calendar day"

**Analysis:** Issue is defined as a concept that exists in the semantic hierarchy.

---

## Evidence 2: Issue Has Identity

**Source:** TJS-000 §4

**Quote:** "Issue represents one editorial edition... for a single calendar day"

**Analysis:** Identity is Calendar day — unique, stable, immutable.

---

## Evidence 3: Issue Has Properties

**Source:** TJS-000 §5

**Quote:** "Issue — Owns: Daily edition, date scope"

**Analysis:** Issue has properties (daily edition, date scope) that can be described.

---

## Evidence 4: Issue Has Lifecycle

**Source:** TJS-021 §8

**Quote:** "An Issue opens when... An Issue is maintained through... An Issue closes when..."

**Analysis:** Issue has a defined lifecycle (Opens → Maintained → Closes → Historical).

---

## Evidence 5: Issue Has Boundaries

**Source:** TJS-000 §4

**Quote:** "for a single calendar day"

**Analysis:** Issue has clear temporal boundaries (one calendar day).

---

## Evidence 6: Issue Is Treated as Thing

**Source:** TJS-000 §4 (hierarchy)

**Quote:** "Journal → Issue → Publication"

**Analysis:** Issue is positioned as a thing in the semantic hierarchy, between Journal and Publication.

---

# Contradicting Evidence

## Contradiction 1: Issue Has No Explicit Identifier

**Source:** No specification

**Analysis:** DATA_MODEL.md requires unique identification, but no Issue ID is defined.

---

## Contradiction 2: Issue Ownership Is Unclear

**Source:** TJS-000 §5, TJS-010 §4.1

**Analysis:** TJS-000 §5 says Issue "Owns: Daily edition, date scope" but doesn't say who owns Issue. TJS-010 §4.1 says Publication Engine owns Publications, not Issue.

---

## Contradiction 3: Issue Lifecycle Is Derived

**Source:** TJS-021 §8

**Analysis:** Issue lifecycle is defined in terms of Publication lifecycle (opens when first Publication generated, closes when all Publications archived). It is not independent.

---

## Contradiction 4: Issue Is Triggered, Not Created

**Source:** TJS-021 §8.1

**Quote:** "An Issue opens when the first Publication... is generated"

**Analysis:** Issue is triggered by an external event (Publication generation), not created independently like an Object.

---

## Contradiction 5: Issue Cannot Exist Without Publications

**Source:** TJS-021 §8.1

**Analysis:** Issue requires at least one Publication to exist. Objects typically can exist independently.

---

# Verdict

**H1 is PARTIALLY SUPPORTED.**

Issue exhibits some Object properties (existence, identity, properties, lifecycle, boundaries) but contradicts others (no explicit identifier, unclear ownership, derived lifecycle, triggered creation, dependency on Publications).

---

# End of Object Hypothesis
