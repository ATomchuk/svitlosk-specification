# TERRITORIAL_MODEL

Status: Stable (Стабільний)

Document ID: DOC-009

Document Class: Normative

Author: SvitloSk Project

---

# Purpose

This document defines the canonical territorial hierarchy used throughout the SvitloSk Project.

The Territorial Model establishes a single authoritative representation of geographical entities and their relationships.

All project components SHALL derive territorial information exclusively from this model.

This document is normative.

---

# Why this document exists

Territorial information is used by multiple independent components:

- Parser
- Data Model
- Publication Engine
- Telegram Publisher
- Graphic Generator
- API
- Future Web Interface
- Future Interactive Map

Without a unified territorial model, each component would implement its own interpretation of territorial relationships, resulting in inconsistent behaviour.

This specification establishes a single source of truth.

---

# Design Principles

The Territorial Model SHALL satisfy the following principles.

## Single Source of Truth

Territorial relationships SHALL be defined only once.

Presentation components SHALL NOT redefine territorial hierarchy.

---

## Hierarchical Structure

Every territorial entity SHALL belong to exactly one parent entity.

The hierarchy SHALL form a tree.

Cycles SHALL NOT exist.

---

## Separation of Concerns

The Territorial Model describes geographical relationships only.

It SHALL NOT contain:

- publication logic;
- parser logic;
- presentation rules;
- Telegram formatting.

---

## Future Compatibility

The hierarchy SHALL support future territorial levels without changing existing components.

New entity types MAY be introduced without breaking compatibility.

---

# Canonical Territorial Hierarchy

```
Community
│
├── Administrative Centre
│     └── Urban Area
│            └── Street
│                  └── Address
│
└── Starosta District
      └── Settlement
            └── Street
                  └── Address
```

This hierarchy is canonical.

All project components SHALL follow this structure.

---

# Territorial Entities

## Community

Top-level territorial unit.

Example:

Starokostiantyniv Community.

---

## Administrative Centre

The administrative capital of the Community.

Example:

Starokostiantyniv.

---

## Urban Area

An urban subdivision used inside the Administrative Centre.

Current implementation:

Urban Area = entire city.

Future implementations MAY include:

- Microdistrict
- Neighbourhood
- Residential Area
- Industrial Zone

Existing software SHALL remain compatible.

---

## Starosta District

Administrative subdivision of the Community.

A Starosta District contains one or more settlements.

---

## Settlement

A populated locality belonging to one Starosta District.

Examples:

- Velyki Matsevychi
- Samchyky
- Radkivtsi

---

## Street

Official street or lane.

Examples:

- вул.
- пров.
- площа
- проспект

The official designation SHALL be preserved.

---

## Address

Smallest territorial unit.

Examples:

- вул. Козацька 5
- пров. Садовий 3

---

# Containment Rules

Each entity SHALL belong to exactly one parent.

Example:

Address

↓

Street

↓

Settlement

↓

Starosta District

↓

Community

The Administrative Centre follows an equivalent structure.

---

# Presentation Independence

Presentation components SHALL NOT determine territorial relationships.

Examples include:

- Telegram Publisher
- Graphic Generator
- Future Web UI

These components SHALL consume the Territorial Model without modification.

---

# Future Extensions

The following entity types MAY be introduced in future versions:

- Microdistrict
- Quarter
- Residential Complex
- Building Group
- Geographic Zone

Existing hierarchy SHALL remain valid.

---

# Example

```
Community

└── Administrative Centre

      └── Starokostiantyniv

            └── вул. Острозького

                    └── 15

Community

└── Starosta District

      └── Samchyky

            └── Samchyky

                  └── вул. Центральна

                        └── 18
```

---

# Repository Rule

No project component MAY introduce its own territorial hierarchy.

All territorial relationships SHALL originate from the Territorial Model.

---

# References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- GLOSSARY.md

## Referenced by

- DATA_MODEL.md
- SSP-002 Parser
- SSP-003 Publication Engine
- SSP-004 Telegram Channel
- SSP-007 Graphic Generator
- TJS-005 Message Templates
- Future Web UI
- Future Map Module
