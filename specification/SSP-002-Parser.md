# SSP-002 — Parser

**Status:** Stable (Стабільний)

**Specification ID:** SSP-002

**Component:** Parser

**Class:** Normative

**Maintainer:** SvitloSk Project

---

# 1. Purpose

This specification defines the normative requirements for the SvitloSk Parser.

The Parser is responsible for collecting Official Open Data, validating it, normalizing it and producing a canonical Normalized Dataset for downstream system components.

The Parser is the only component authorized to transform external Official Open Data into the internal logical representation defined by `DATA_MODEL.md`.

The Parser SHALL NOT interpret information, generate publications or modify official facts.

---

# 2. Scope

This specification applies to:

- data acquisition;
- source validation;
- change detection;
- normalization;
- territorial resolution;
- metadata generation;
- dataset production.

---

# 3. Design Principles

The Parser SHALL operate according to the following principles:

- determinism;
- reproducibility;
- traceability;
- source transparency;
- fail-safe processing.

The same input SHALL always produce the same output.

Execution environment, locale or execution time SHALL NOT affect the generated dataset.

---

# 4. Responsibilities

The Parser SHALL:

- retrieve Official Open Data;
- validate received information;
- detect dataset changes;
- normalize all operational data;
- resolve territorial entities;
- generate processing metadata;
- produce one canonical Normalized Dataset.

The Parser SHALL NOT:

- interpret operational information;
- generate publications;
- apply editorial formatting;
- calculate analytics;
- modify official facts.

---

# 5. Official Data Sources

The Parser SHALL accept only Official Open Data.

Typical sources include:

- planned power outage schedules;
- emergency power outage notifications;
- official Distribution System Operator publications;
- official public registries.

Unofficial sources SHALL NOT be processed.

---

# 6. Input Requirements

Each accepted dataset SHALL contain sufficient information to identify, where applicable:

- publication date;
- publication time;
- affected Territory;
- affected Settlement;
- affected Address;
- outage interval;
- official source.

Incomplete or invalid datasets SHALL be rejected or reported.

---

# 7. Normalization

The Parser SHALL transform incoming data into entities conforming to `DATA_MODEL.md`.

Territorial entities SHALL conform to `TERRITORIAL_MODEL.md`.

Normalization MAY include:

- canonical settlement names;
- canonical street names;
- building numbers;
- outage intervals;
- queue identifiers;
- subqueue identifiers;
- metadata enrichment.

Normalization SHALL preserve the meaning of the original Official Open Data.

---

# 8. Territorial Resolution

The Parser SHALL resolve every affected Address to the official territorial hierarchy defined by `TERRITORIAL_MODEL.md`.

The Parser SHALL NOT define or modify territorial relationships.

---

# 9. Change Detection

The Parser SHALL detect:

- new records;
- modified records;
- removed records.

Every detected change SHALL be reflected in the produced dataset.

The generated metadata SHOULD include a dataset version identifier.

---

# 10. Metadata

Each Normalized Dataset SHALL contain metadata including:

- generation timestamp;
- source identifier;
- source publication timestamp (when available);
- parser version;
- dataset identifier;
- dataset version;
- processing status.

Metadata SHALL accompany every generated dataset.

---

# 11. Artificial Intelligence

The Parser MAY use AI-assisted processing techniques as implementation details.

AI MAY be used for:

- document structure recognition;
- extraction from semi-structured sources;
- anomaly detection;
- normalization assistance.

Regardless of implementation, the produced Normalized Dataset SHALL remain deterministic.

AI SHALL NOT:

- create operational facts;
- modify official information;
- infer missing operational data;
- replace the Official Open Data source.

Official Open Data SHALL remain the only operational source of truth.

---

# 12. Error Handling

Parser failures SHALL NEVER generate fictional information.

The Parser SHALL fail safely.

Possible actions include:

- rejecting the dataset;
- reporting validation errors;
- preserving the previous valid dataset;
- logging processing details.

---

# 13. Processing Pipeline

Every successful execution SHALL follow the logical processing pipeline.

```text
Retrieve Official Open Data

↓

Validate

↓

Normalize

↓

Resolve Territory

↓

Generate Metadata

↓

Produce Normalized Dataset
```

---

# 14. Output

Each successful execution SHALL produce exactly one immutable Normalized Dataset.

The produced dataset SHALL conform to `DATA_MODEL.md`.

The dataset becomes the canonical input for:

- Publication Engine;
- Telegram Journal;
- PWA application;
- Historical Archive;
- future Public API.

---

# 15. Non-Goals

The Parser SHALL NOT:

- publish Telegram messages;
- generate graphics;
- determine editorial presentation;
- send notifications;
- archive publications;
- calculate analytics.

These responsibilities belong to downstream system components.

---

# 16. Repository Rule

Normative documents SHALL reference the Parser as the only component responsible for producing the canonical Normalized Dataset.

No downstream component MAY modify operational data received from the Parser.

---

# 17. References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- GLOSSARY.md
- TERRITORIAL_MODEL.md
- DATA_MODEL.md
- SSP-001 — Data Pipeline

## Referenced by

- SSP-003 — Publication Engine
- SSP-005 — Data Storage
- Telegram Journal Specification

---

# End of Specification
