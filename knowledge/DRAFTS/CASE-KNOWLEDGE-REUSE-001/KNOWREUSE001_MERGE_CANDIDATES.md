# Merge Candidates

**Document Class:** Knowledge Reuse Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document identifies knowledge items that can be merged.

---

# Merge Candidates

## MERGE-001: Publisher Definition

### Sources

- CASE-PUB-001: Publisher as Role
- CASE-PUB-002: Publisher responsibilities
- CASE-PUB-003: Publisher in glossary
- CASE-PUB-004: Publisher as executor
- CASE-PUB-005: Publisher rules

### Merge Target

PUBLISHER_CONCEPTS.md

### Rationale

All sources describe the same concept from different angles.

Merging creates a comprehensive definition.

---

## MERGE-002: Publication Definition

### Sources

- CASE-PUB-001: Publication as atomic
- CASE-PUB-002: Publication operations
- CASE-PUB-005: Publication rules
- CASE-INF-001: Information model
- CASE-INFPROD-001: Publication as product
- CASE-TG-CORE-001: Publication operations

### Merge Target

PUBLISHER_CONCEPTS.md

### Rationale

All sources describe the same concept.

Merging creates a comprehensive definition.

---

## MERGE-003: Lifecycle Definition

### Sources

- CASE-PUB-004: Lifecycle is not owned
- CASE-PUB-005: Lifecycle operations
- CASE-INF-001: Information lifecycle
- CASE-LC-001: Lifecycle as pattern

### Merge Target

LIFECYCLE_PATTERN.md

### Rationale

All sources describe the same concept.

Merging creates a comprehensive definition.

---

## MERGE-004: Publisher Responsibilities

### Sources

- CASE-PUB-002: 12 responsibilities
- CASE-PUB-005: Responsibilities in rules
- CASE-TG-CORE-001: Responsibilities identified

### Merge Target

PUBLISHER_RESPONSIBILITIES.md

### Rationale

All sources describe the same responsibilities.

Merging creates a comprehensive inventory.

---

## MERGE-005: Publisher Operations

### Sources

- CASE-PUB-002: Operations identified
- CASE-PUB-005: Operations in rules
- CASE-TG-CORE-001: Operations identified

### Merge Target

PUBLISHER_OPERATIONS.md

### Rationale

All sources describe the same operations.

Merging creates a comprehensive inventory.

---

## MERGE-006: Business Rules

### Sources

- CASE-PUB-004: Decision model
- CASE-PUB-005: 17 rules

### Merge Target

PUBLISHER_RULES.md

### Rationale

Decision model and rules are complementary.

Merging creates a comprehensive rules document.

---

# Merge Candidates Summary

| Merge ID | Sources | Target |
|----------|---------|--------|
| MERGE-001 | CASE-PUB-001, 002, 003, 004, 005 | PUBLISHER_CONCEPTS.md |
| MERGE-002 | CASE-PUB-001, 002, 005, INF-001, INFPROD-001, TG-CORE-001 | PUBLISHER_CONCEPTS.md |
| MERGE-003 | CASE-PUB-004, 005, INF-001, LC-001 | LIFECYCLE_PATTERN.md |
| MERGE-004 | CASE-PUB-002, 005, TG-CORE-001 | PUBLISHER_RESPONSIBILITIES.md |
| MERGE-005 | CASE-PUB-002, 005, TG-CORE-001 | PUBLISHER_OPERATIONS.md |
| MERGE-006 | CASE-PUB-004, 005 | PUBLISHER_RULES.md |

---

# Traceability

| Merge | Source |
|-------|--------|
| All merges | CASE-PUB-001 through CASE-TG-CORE-001 |

---

**End of Merge Candidates**
