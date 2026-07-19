# ADR-001 — Component vs Role

Status: Accepted (Прийнятий)

Document Class: Architecture Decision Record

ADR ID: ADR-001

Author: SvitloSk Project

---

# Purpose

This Architecture Decision Record defines the distinction between an architectural component and a logical role within the SvitloSk repository.

Its purpose is to ensure consistent naming across Core Documents, System Specifications (SSP), and future reviews.

---

# Context

During the review of SSP-003, ambiguity arose regarding the use of the following names:

- Publication Engine
- Publisher

The review process treated these names as interchangeable terminology.

However, repository architecture distinguishes between:

- architectural components;
- logical roles.

This distinction had not previously been defined explicitly.

---

# Decision

The field:

```text
Component:
```

in every SSP specification SHALL identify the **architectural component** implemented by the system.

The value of **Component** SHALL NOT be interpreted as a glossary term unless explicitly defined as such.

Architectural component names and glossary terms MAY differ when they represent different abstraction levels.

---

# Definitions

## Architectural Component

An architectural component is a structural element of the system architecture.

It represents a deployable or conceptual subsystem responsible for implementing one or more logical roles.

Examples:

- Data Pipeline
- Parser
- Publication Engine
- Graphic Generator
- Schedule Generator

---

## Logical Role

A logical role represents a responsibility, behaviour, or function performed within the system.

Logical roles are defined by the project glossary.

Examples:

- Publisher
- Parser
- Consumer

---

# Relationship

An architectural component MAY implement one or more logical roles.

A logical role MAY be implemented by exactly one architectural component.

Example:

| Architectural Component | Logical Role |
|--------------------------|--------------|
| Publication Engine | Publisher |
| Parser | Parser |

The two concepts SHALL NOT be considered synonymous.

---

# Review Implications

Reviewers SHALL distinguish between:

- architectural component names;
- glossary terminology.

An architectural component name SHALL NOT be classified as a terminology violation solely because its name differs from a glossary term.

Terminology findings SHALL only apply when glossary terms are used incorrectly within descriptive text.

Metadata fields identifying architectural components SHALL be evaluated independently.

---

# Consequences

The following repository elements remain valid:

```
Component: Publication Engine
```

while descriptive text MAY correctly refer to:

```
Publisher
```

Both forms are correct because they represent different abstraction levels.

No repository-wide renaming is required.

Future SSP reviews SHALL apply this decision.

---

# Affected Documents

This decision affects the interpretation of:

- ARCHITECTURE.md
- SYSTEM_OVERVIEW.md
- GLOSSARY.md
- EDITORIAL_STANDARDS.md
- SSP_REVIEW_PROTOCOL.md
- All SSP specifications

---

# References

## Depends on

- ARCHITECTURE.md
- GLOSSARY.md
- EDITORIAL_STANDARDS.md

## Referenced by

- SSP_REVIEW_PROTOCOL.md
- Future SSP Review Reports

---

**End of Document**