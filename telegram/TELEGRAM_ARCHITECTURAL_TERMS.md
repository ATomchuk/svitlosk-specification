# Telegram Architectural Terms

**Date:** 2026-07-13
**Purpose:** Architectural terminology — SHALL NOT become glossary entries
**Status:** APPROVED — semantic language frozen

---

# Why Architectural Terms Are Not Glossary Entries

Architectural terms describe HOW the system is organized, governed and engineered. They are NOT semantic concepts of the Telegram Publishing System.

The Telegram Glossary SHALL contain only semantic concepts — what the Journal IS and what it DOES. Architectural terms describe how the system is built and governed.

---

## Architectural Terms

### A-001: SSOT (Single Source of Truth)

| Field | Value |
|-------|-------|
| English | SSOT |
| Ukrainian | Єдине джерело правди |
| Status | ARCHITECTURAL |
| Category | Architectural |
| Owner | GLOSSARY |
| Reason | Repository governance principle. Describes how documentation is organized, not what the Journal publishes. |
| Where Used | All audit documents, PROJECT_PRINCIPLES |

---

### A-002: SRP (Single Responsibility Principle)

| Field | Value |
|-------|-------|
| English | SRP |
| Ukrainian | Принцип єдиної відповідальності |
| Status | ARCHITECTURAL |
| Category | Architectural |
| Owner | PROJECT_PRINCIPLES |
| Reason | Engineering principle. Describes how documents are structured, not what the Journal publishes. |
| Where Used | PROJECT_PRINCIPLES, audit documents |

---

### A-003: Separation of Concerns

| Field | Value |
|-------|-------|
| English | Separation of Concerns |
| Ukrainian | Розділення відповідальності |
| Status | ARCHITECTURAL |
| Category | Architectural |
| Owner | ARCHITECTURE |
| Reason | Engineering principle. Describes how responsibilities are divided, not what the Journal publishes. |
| Where Used | ARCHITECTURE, audit documents |

---

### A-004: Semantic Ownership Principle

| Field | Value |
|-------|-------|
| English | Semantic Ownership Principle |
| Ukrainian | Принцип семантичної власності |
| Status | ARCHITECTURAL |
| Category | Architectural |
| Owner | TJS-000 |
| Reason | Governance rule. Describes how terminology is governed, not what the Journal publishes. |
| Where Used | TJS-000 §6 |

---

### A-005: One Document — One Subject

| Field | Value |
|-------|-------|
| English | One Document — One Subject |
| Ukrainian | Один документ — одна тема |
| Status | ARCHITECTURAL |
| Category | Architectural |
| Owner | PROJECT_PRINCIPLES |
| Reason | Engineering principle (P-10). Describes how documents are structured, not what the Journal publishes. |
| Where Used | PROJECT_PRINCIPLES P-10 |

---

### A-006: Dependency Direction

| Field | Value |
|-------|-------|
| English | Dependency Direction |
| Ukrainian | Напрямок залежностей |
| Status | ARCHITECTURAL |
| Category | Architectural |
| Owner | ARCHITECTURE |
| Reason | Governance rule. Describes how document dependencies flow, not what the Journal publishes. |
| Where Used | ARCHITECTURE |

---

### A-007: Metadata Compliance

| Field | Value |
|-------|-------|
| English | Metadata Compliance |
| Ukrainian | Відповідність метаданих |
| Status | ARCHITECTURAL |
| Category | Architectural |
| Owner | ARCHITECTURE |
| Reason | Governance rule. Describes required document metadata, not what the Journal publishes. |
| Where Used | ARCHITECTURE, audit documents |

---

## Summary

| # | Term | Status | Reason Not Glossary |
|---|------|--------|-------------------|
| A-001 | SSOT | ARCHITECTURAL | Governance principle |
| A-002 | SRP | ARCHITECTURAL | Engineering principle |
| A-003 | Separation of Concerns | ARCHITECTURAL | Engineering principle |
| A-004 | Semantic Ownership Principle | ARCHITECTURAL | Governance rule |
| A-005 | One Document — One Subject | ARCHITECTURAL | Engineering principle |
| A-006 | Dependency Direction | ARCHITECTURAL | Governance rule |
| A-007 | Metadata Compliance | ARCHITECTURAL | Governance rule |

**Total Architectural Terms:** 7

---

**End of Architectural Terms**

**Approver:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
