# SEMANTIC_EXISTENCE_GRAPH

**Document ID:** CASE001-003

**Title:** Semantic Existence Graph

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Investigation №001

---

# Purpose

This document draws the dependency graph showing how concepts depend on each other in the Telegram Publishing Domain. Only Concept → Concept dependencies are shown. No Component → Component dependencies.

---

# Dependency Graph

## Foundation Layer — Physical Reality

```text
Starokostiantyniv Community
    ├── Administrative Centre
    ├── Starosta District
    │     └── Settlement
    │           └── Street
    │                 └── Address
    └── Community (territorial)
```

## Electricity Domain Layer

```text
Distribution System Operator
    ├── Planned Power Outage
    ├── Emergency Power Outage
    ├── Outage Schedule
    │     ├── Queue
    │     │     └── Subqueue
    │     ├── Availability Window
    │     └── Outage Window
    └── Electricity Availability

Electricity Availability
    ├── Powered state
    └── Outage state
```

## Data Domain Layer

```text
Open Data
    └── Data Source

Data Source
    └── Distribution System Operator
```

## Publication Domain Layer

```text
Journal
    └── Issue
          └── Publication
                ├── Text Publication
                ├── Graphic Publication
                ├── City Today
                ├── District Today
                ├── City Tomorrow
                ├── District Tomorrow
                └── Publication Package

Publication Channel
    └── Telegram Channel

Telegram Channel
    └── Subscribers
```

## Editorial Domain Layer

```text
Editorial Policy
    ├── Editorial Principles
    ├── Territory Presentation
    ├── Time Format
    ├── Settlement Formatting
    ├── Address Formatting
    └── Branding

Canonical Templates
    └── Publication Grammar
          ├── Territory Header
          └── Publication Sections

Formatting Rules
    └── Rendering Rules
```

## Lifecycle Domain Layer

```text
Publication Lifecycle
    ├── Generated
    ├── Published
    ├── Updated
    ├── Archived
    └── Removed

Publication Lifecycle
    ├── Update Rules
    ├── Archive Policy
    └── Deletion Policy

Repository Authority
    └── Repository State
```

## Quality Domain Layer

```text
Traceability
    └── Reliability

Source Fidelity
    └── Deterministic Rendering

Non-destructive Channel
    └── Publication Ownership

Non-destructive Update
    └── Canonical Equality
```

## Graphic Domain Layer

```text
Graphic Publication
    ├── Tomorrow Schedule Graphic
    ├── Emergency Information Card
    ├── Information Card
    ├── Statistics Card
    └── Service Graphic

Graphic Principles
    ├── Graphic Automation
    ├── Graphic Clarity
    ├── Graphic Branding
    ├── Graphic Accessibility
    └── Graphic Color
```

---

# Cross-Layer Dependencies

```text
Starokostiantyniv Community → Journal (geographic scope)
Distribution System Operator → Open Data (source)
Open Data → Data Source (origin)
Data Source → Parser (retrieval)
Parser → Publication Engine (data flow)
Publication Engine → Publication (generation)
Publication → Telegram Channel (delivery)
Telegram Channel → Subscribers (distribution)
Editorial Policy → Publication (governance)
Publication Lifecycle → Publication (management)
Territory (publication unit) → Starosta District (mapping)
Territory (publication unit) → Administrative Centre (mapping)
Reporting Period → Issue (temporal scope)
Archive → Publication (preservation)
Publication Package → Publication (aggregation)
```

---

# Complete Dependency Chains

## Chain 1: Physical Reality → Publication

```text
Starokostiantyniv Community
    → Administrative Centre / Starosta District
        → Settlement
            → Street
                → Address
                    → Publication (contains address information)
```

## Chain 2: Electricity Domain → Publication

```text
Distribution System Operator
    → Outage Schedule
        → Queue → Subqueue
            → Availability Window / Outage Window
                → Publication (contains schedule information)
```

## Chain 3: Data Flow → Publication

```text
Open Data
    → Data Source
        → Parser (retrieval)
            → Publication Engine (transformation)
                → Publication (generation)
                    → Telegram Channel (delivery)
                        → Subscribers (consumption)
```

## Chain 4: Editorial Governance → Publication

```text
Editorial Policy
    → Editorial Principles
        → Territory Presentation
        → Time Format
        → Settlement Formatting
        → Address Formatting
        → Branding
            → Publication (formatting rules)
```

## Chain 5: Lifecycle Management → Publication

```text
Publication Lifecycle
    → Generated → Published → Updated → Archived → Removed
        → Publication (state transitions)
            → Repository Authority (truth source)
```

## Chain 6: Graphic Domain → Publication

```text
Graphic Principles
    → Graphic Automation
    → Graphic Clarity
        → Graphic Publication (visual output)
            → Telegram Channel (delivery)
```

---

# End of Document
