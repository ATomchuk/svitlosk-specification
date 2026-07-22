# Version Requirement

**Document Class:** Entity Nature Investigation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines version requirement for each entity.

---

# Version Requirement

## Entities That Can Be Versioned

| Entity | Nature | Version Requirement | Evidence |
|--------|--------|---------------------|----------|
| Publication | ARTIFACT | YES | GLOSSARY §3 |

---

## Entities That Cannot Be Versioned

| Entity | Nature | Why No Versioning |
|--------|--------|-------------------|
| Journal | SERVICE | Continuous |
| Journal Edition | INSTANCE | Single version per day |
| Publisher | SERVICE + ROLE | Continuous |
| Publication Package | COLLECTION | Single version per period |
| Lifecycle | PATTERN | Pattern is stable |
| Territory | REFERENCE | Reference data is stable |
| Information | CONCEPT | Abstract concept |
| Knowledge | CONCEPT | Abstract concept |
| Open Data | CONCEPT | Abstract concept |
| Parser | SERVICE | Continuous |
| Archive | SERVICE | Continuous |
| Representation | ARTIFACT | Single version |
| Channel | SERVICE | Continuous |
| Adapter | SERVICE + ROLE | Continuous |

---

# Version Requirement Summary

| Requirement | Entities | Count |
|-------------|----------|-------|
| Can Be Versioned | Publication | 1 |
| Cannot Be Versioned | Journal, Journal Edition, Publisher, Publication Package, Lifecycle, Territory, Information, Knowledge, Open Data, Parser, Archive, Representation, Channel, Adapter | 14 |

---

# Traceability

| Version Requirement | Source |
|---------------------|--------|
| All version requirements | Analysis of entity nature and domain knowledge |

---

**End of Version Requirement**
