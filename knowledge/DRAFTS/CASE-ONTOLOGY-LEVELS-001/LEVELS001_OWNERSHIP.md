# Ownership

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity ownership.

---

# Ownership

## Publisher-Owned Entities

| Entity | Level | Owner | Why |
|--------|-------|-------|-----|
| Journal Edition | OBJECT | Publisher | Creates and manages |
| Publication Package | OBJECT | Publisher | Creates and manages |
| Emergency Outage Publication | OBJECT | Publisher | Creates and manages |
| Planned Outage Publication | OBJECT | Publisher | Creates and manages |
| Queue Graph Publication | OBJECT | Publisher | Creates and manages |
| Technical Publication | OBJECT | Publisher | Creates and manages |
| Service Publication | OBJECT | Publisher | Creates and manages |
| Publication | ARTIFACT | Publisher | Creates and manages |
| Publication Package | ARTIFACT | Publisher | Creates and manages |
| Publisher Interface | INTERFACE | Publisher | Defines |
| Publisher Boundary | BOUNDARY | Publisher | Defines |

---

## Lifecycle-Owned Entities

| Entity | Level | Owner | Why |
|--------|-------|-------|-----|
| Lifecycle State | STATE | Lifecycle | Governs |
| Lifecycle Transition | STATE | Lifecycle | Governs |

---

## Parser-Owned Entities

| Entity | Level | Owner | Why |
|--------|-------|-------|-----|
| Parsed Data | ARTIFACT | Parser | Creates |
| Normalized Dataset | ARTIFACT | Parser | Creates |

---

## Adapter-Owned Entities

| Entity | Level | Owner | Why |
|--------|-------|-------|-----|
| Representation | ARTIFACT | Adapter | Creates |
| Channel State | STATE | Adapter | Governs |
| Adapter Interface | INTERFACE | Adapter | Defines |

---

## System-Owned Entities

| Entity | Level | Owner | Why |
|--------|-------|-------|-----|
| Journal | SERVICE | System | Operates |
| Publisher | SERVICE | System | Operates |
| Parser | SERVICE | System | Operates |
| Archive | SERVICE | System | Operates |
| Specification | DOCUMENT | System | Maintains |
| Glossary | DOCUMENT | System | Maintains |
| Publisher Boundary | BOUNDARY | System | Defines |
| Channel Boundary | BOUNDARY | System | Defines |
| Domain Boundary | BOUNDARY | System | Defines |

---

# Ownership Summary

| Owner | Entities | Count |
|-------|----------|-------|
| Publisher | 12 | 12 |
| Lifecycle | 2 | 2 |
| Parser | 1 | 1 |
| Adapter | 1 | 1 |
| System | 5 | 5 |
| **Total** | | **21** |

---

# Traceability

| Ownership | Source |
|-----------|--------|
| All ownership | Analysis of entity classification and architectural levels |

---

**End of Ownership**
