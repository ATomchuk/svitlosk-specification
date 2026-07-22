# Entity Nature

**Document Class:** Entity Nature Investigation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines what each entity IS.

---

# Entity Nature

## Journal

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | SERVICE | CHARTER §10 |
| Can exist by itself? | YES | Continuous activity |
| Multiple instances? | NO | Single service |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Continuous |
| Can be versioned? | NO | Continuous |
| Can own other entities? | YES | Produces Journal Editions |
| Can another entity own it? | NO | Top-level entity |
| Can exist without Publisher? | YES | Independent service |
| Publisher exist without it? | NO | Publisher serves Journal |

---

## Journal Edition

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | INSTANCE | CASE-JRN-001 |
| Can exist by itself? | YES | Daily instance |
| Multiple instances? | YES | One per day |
| Has identity? | YES | Reporting Period |
| Can change over time? | YES | Daily |
| Can be versioned? | NO | Single version per day |
| Can own other entities? | YES | Contains Publications |
| Can another entity own it? | YES | Journal produces it |
| Can exist without Publisher? | YES | Independent instance |
| Publisher exist without it? | YES | Publisher can exist without specific edition |

---

## Publisher

| Question | Answer | Evidence |
|----------|--------|----------|
| What it is? | SERVICE + ROLE | GLOSSARY §7 |
| Can exist by itself? | YES | Continuous service |
| Multiple instances? | NO | Single service |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Continuous |
| Can be versioned? | NO | Continuous |
| Can own other entities? | YES | Produces Publications |
| Can another entity own it? | NO | Top-level entity |
| Can exist without Journal? | YES | Independent service |
| Journal exist without it? | NO | Journal needs Publisher |

---

## Publication

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | ARTIFACT | GLOSSARY §3 |
| Can exist by itself? | YES | Discrete object |
| Multiple instances? | YES | Many Publications |
| Has identity? | YES | Territory + Time |
| Can change over time? | YES | Updated, Archived |
| Can be versioned? | YES | Publication Version |
| Can own other entities? | NO | Atomic unit |
| Can another entity own it? | YES | Publisher produces it |
| Can exist without Publisher? | YES | Independent artifact |
| Publisher exist without it? | YES | Publisher can exist without specific Publication |

---

## Publication Package

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | COLLECTION | GLOSSARY §3 |
| Can exist by itself? | YES | Collection of Publications |
| Multiple instances? | YES | One per reporting period |
| Has identity? | YES | Reporting Period |
| Can change over time? | YES | Updated daily |
| Can be versioned? | NO | Single version per period |
| Can own other entities? | YES | Contains Publications |
| Can another entity own it? | YES | Publisher produces it |
| Can exist without Publisher? | YES | Independent collection |
| Publisher exist without it? | YES | Publisher can exist without specific package |

---

## Lifecycle

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | PATTERN | CASE-LC-001 |
| Can exist by itself? | YES | Abstract pattern |
| Multiple instances? | NO | Single pattern |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Pattern is stable |
| Can be versioned? | NO | Pattern is stable |
| Can own other entities? | NO | Pattern observes, not owns |
| Can another entity own it? | NO | Pattern is independent |
| Can exist without Publisher? | YES | Independent pattern |
| Publisher exist without it? | NO | Publisher follows lifecycle |

---

## Territory

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | REFERENCE | GLOSSARY §4 |
| Can exist by itself? | YES | Reference data |
| Multiple instances? | YES | Many territories |
| Has identity? | YES | Geographic identity |
| Can change over time? | NO | Reference data is stable |
| Can be versioned? | NO | Reference data is stable |
| Can own other entities? | NO | Reference data |
| Can another entity own it? | NO | Reference data is independent |
| Can exist without Publisher? | YES | Independent reference |
| Publisher exist without it? | YES | Publisher can exist without specific territory |

---

## Information

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | CONCEPT | CASE-INF-001 |
| Can exist by itself? | YES | Abstract concept |
| Multiple instances? | YES | Many information objects |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Concept is stable |
| Can be versioned? | NO | Concept is stable |
| Can own other entities? | NO | Concept observes |
| Can another entity own it? | NO | Concept is independent |
| Can exist without Publisher? | YES | Independent concept |
| Publisher exist without it? | NO | Publisher processes information |

---

## Knowledge

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | CONCEPT | CASE-INF-001 |
| Can exist by itself? | YES | Abstract concept |
| Multiple instances? | YES | Many knowledge objects |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Concept is stable |
| Can be versioned? | NO | Concept is stable |
| Can own other entities? | NO | Concept observes |
| Can another entity own it? | NO | Concept is independent |
| Can exist without Publisher? | YES | Independent concept |
| Publisher exist without it? | YES | Publisher can exist without specific knowledge |

---

## Open Data

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | CONCEPT | GLOSSARY §2 |
| Can exist by itself? | YES | Abstract concept |
| Multiple instances? | YES | Many data objects |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Concept is stable |
| Can be versioned? | NO | Concept is stable |
| Can own other entities? | NO | Concept observes |
| Can another entity own it? | NO | Concept is independent |
| Can exist without Publisher? | YES | Independent concept |
| Publisher exist without it? | YES | Publisher can exist without specific data |

---

## Parser

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | SERVICE | GLOSSARY §2 |
| Can exist by itself? | YES | Continuous service |
| Multiple instances? | NO | Single service |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Continuous |
| Can be versioned? | NO | Continuous |
| Can own other entities? | YES | Produces Parsed Data |
| Can another entity own it? | NO | Top-level entity |
| Can exist without Publisher? | YES | Independent service |
| Publisher exist without it? | NO | Publisher needs Parser data |

---

## Archive

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | SERVICE | GLOSSARY §2 |
| Can exist by itself? | YES | Continuous service |
| Multiple instances? | NO | Single service |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Continuous |
| Can be versioned? | NO | Continuous |
| Can own other entities? | YES | Stores Publications |
| Can another entity own it? | NO | Top-level entity |
| Can exist without Publisher? | YES | Independent service |
| Publisher exist without it? | YES | Publisher can exist without Archive |

---

## Representation

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | ARTIFACT | CASE-INF-001 |
| Can exist by itself? | YES | Discrete object |
| Multiple instances? | YES | Many representations |
| Has identity? | YES | Channel + Time |
| Can change over time? | YES | Updated |
| Can be versioned? | NO | Single version |
| Can own other entities? | NO | Atomic unit |
| Can another entity own it? | YES | Adapter produces it |
| Can exist without Publisher? | YES | Independent artifact |
| Publisher exist without it? | YES | Publisher can exist without specific representation |

---

## Channel

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | SERVICE | GLOSSARY §3 |
| Can exist by itself? | YES | Continuous service |
| Multiple instances? | YES | Many channels |
| Has identity? | YES | Channel identity |
| Can change over time? | NO | Continuous |
| Can be versioned? | NO | Continuous |
| Can own other entities? | YES | Delivers Representations |
| Can another entity own it? | NO | Top-level entity |
| Can exist without Publisher? | YES | Independent service |
| Publisher exist without it? | YES | Publisher can exist without specific channel |

---

## Adapter

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | SERVICE + ROLE | CASE-SVT-ONTOLOGY-001 |
| Can exist by itself? | YES | Continuous service |
| Multiple instances? | YES | Many adapters |
| Has identity? | YES | Channel identity |
| Can change over time? | NO | Continuous |
| Can be versioned? | NO | Continuous |
| Can own other entities? | YES | Produces Representations |
| Can another entity own it? | NO | Top-level entity |
| Can exist without Publisher? | YES | Independent service |
| Publisher exist without it? | YES | Publisher can exist without specific adapter |

---

## Archive

| Question | Answer | Evidence |
|----------|--------|----------|
| What is it? | SERVICE | GLOSSARY §2 |
| Can exist by itself? | YES | Continuous service |
| Multiple instances? | NO | Single service |
| Has identity? | NO | Abstract concept |
| Can change over time? | NO | Continuous |
| Can be versioned? | NO | Continuous |
| Can own other entities? | YES | Stores Publications |
| Can another entity own it? | NO | Top-level entity |
| Can exist without Publisher? | YES | Independent service |
| Publisher exist without it? | YES | Publisher can exist without Archive |

---

# Entity Nature Summary

| Entity | Nature | Can Exist Alone | Multiple Instances | Has Identity | Can Change | Can Version | Can Own | Can Be Owned | Without Publisher | Publisher Without It |
|--------|--------|-----------------|-------------------|--------------|------------|-------------|---------|--------------|-------------------|---------------------|
| Journal | SERVICE | YES | NO | NO | NO | NO | YES | NO | YES | NO |
| Journal Edition | INSTANCE | YES | YES | YES | YES | NO | YES | YES | YES | YES |
| Publisher | SERVICE + ROLE | YES | NO | NO | NO | NO | YES | NO | YES | NO |
| Publication | ARTIFACT | YES | YES | YES | YES | YES | NO | YES | YES | YES |
| Publication Package | COLLECTION | YES | YES | YES | YES | NO | YES | YES | YES | YES |
| Lifecycle | PATTERN | YES | NO | NO | NO | NO | NO | NO | YES | NO |
| Territory | REFERENCE | YES | YES | YES | NO | NO | NO | NO | YES | YES |
| Information | CONCEPT | YES | YES | NO | NO | NO | NO | NO | YES | NO |
| Knowledge | CONCEPT | YES | YES | NO | NO | NO | NO | NO | YES | YES |
| Open Data | CONCEPT | YES | YES | NO | NO | NO | NO | NO | YES | YES |
| Parser | SERVICE | YES | NO | NO | NO | NO | YES | NO | YES | NO |
| Archive | SERVICE | YES | NO | NO | NO | NO | YES | NO | YES | YES |
| Representation | ARTIFACT | YES | YES | YES | YES | NO | NO | YES | YES | YES |
| Channel | SERVICE | YES | YES | YES | NO | NO | YES | NO | YES | YES |
| Adapter | SERVICE + ROLE | YES | YES | YES | NO | NO | YES | NO | YES | YES |

---

# Traceability

| Entity | Source |
|--------|--------|
| All entities | Analysis of entity inventory and domain knowledge |

---

**End of Entity Nature**
