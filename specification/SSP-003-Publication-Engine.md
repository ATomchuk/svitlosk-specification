# SSP-003 — Publication Engine

**Status:** Stable (Стабільний)

**Specification ID:** SSP-003

**Component:** Publication Engine

**Class:** Normative

**Maintainer:** SvitloSk Project

---

# 1. Purpose

This specification defines the normative requirements for the SvitloSk Publication Engine.

The Publication Engine transforms the canonical Normalized Dataset into a deterministic Publication Package.

Each Publication represents exactly one Territory and is rendered according to the Telegram Journal Specification.

The Publication Engine SHALL NOT modify operational data produced by the Parser.

---

# 2. Scope

This specification applies to:

- publication generation;
- territorial grouping;
- publication ordering;
- publication updates;
- publication lifecycle;
- publication metadata;
- multi-channel publication preparation.

---

# 3. Design Principles

The Publication Engine SHALL operate according to the following principles:

- determinism;
- reproducibility;
- traceability;
- territorial consistency;
- editorial independence;
- fail-safe processing.

The same Normalized Dataset SHALL always produce the same Publication Package.

---

# 4. Responsibilities

The Publication Engine SHALL:

- consume the canonical Normalized Dataset;
- group operational data by Territory;
- generate Publications;
- assemble Publication Packages;
- maintain publication order;
- detect publication changes;
- update existing Publications;
- generate publication metadata.

The Publication Engine SHALL NOT:

- retrieve Official Open Data;
- modify operational data;
- interpret official information;
- perform data normalization;
- calculate analytics.

---

# 5. Input

The only accepted input SHALL be the Normalized Dataset produced by the Parser.

Direct access to Official Open Data sources SHALL NOT be permitted.

The input dataset SHALL conform to `DATA_MODEL.md`.

---

# 6. Territorial Processing

Publications SHALL be generated according to the territorial hierarchy defined in `TERRITORIAL_MODEL.md`.

Each Publication SHALL represent exactly one Territory.

A Territory SHALL be one of:

- the Administrative Centre;
- one Starosta District.

Operational data SHALL be grouped by Territory before publication generation begins.

---

# 7. Publication

A Publication is the smallest independently published information unit.

Each Publication SHALL:

- represent one Territory;
- contain only Official Open Data;
- be generated automatically;
- preserve source accuracy;
- remain deterministic.

The Publication Engine SHALL NOT merge multiple Territories into one Publication.

---

# 8. Publication Package

A Publication Package represents the complete set of Publications generated for one reporting day.

A Publication Package SHALL contain zero or more Publications.

The number of Publications depends entirely on the availability of Official Open Data.

Every Publication SHALL belong to exactly one Publication Package.

---

# 9. Publication Order

Within a Publication Package, Publications SHALL appear in the following order:

1. Administrative Centre
2. Starosta Districts
3. Tomorrow Publications

The order of Starosta Districts SHALL remain stable between executions.

Temporary Tomorrow Publications SHALL always appear after current-day Publications.

---

# 10. Publication Content

The Publication Engine defines WHAT information is published.

The Telegram Journal Specification defines HOW the information is presented.

Publication formatting SHALL NOT be defined by this specification.

---

# 11. Canonical Templates

Every Publication SHALL be rendered using a Canonical Template defined by the Telegram Journal Specification.

The Publication Engine SHALL select the appropriate template based on:

- Territory;
- publication purpose;
- reporting day.

---

# 12. Publication Lifecycle

A Publication MAY be:

- created;
- updated;
- removed.

Publications SHALL only change when the underlying Normalized Dataset changes.

Unchanged Publications SHALL remain unchanged.

Temporary Tomorrow Publications SHALL be removed after the reporting period ends.

Historical Publications SHALL remain preserved according to project policy.

---

# 13. Metadata

Each Publication SHALL contain metadata including:

- Publication ID;
- Package ID;
- Territory ID;
- dataset version;
- generation timestamp;
- publication status.

Metadata SHALL accompany every Publication.

---

# 14. Idempotency

Publication generation SHALL be idempotent.

Generating Publications multiple times from an identical Normalized Dataset SHALL always produce identical output.

---

# 15. Error Handling

Publication failures SHALL NEVER modify previously published information.

Possible actions include:

- logging processing errors;
- retrying publication;
- preserving previous Publications;
- reporting publication failures.

Partial publication SHALL NOT corrupt an existing Publication Package.

---

# 16. Artificial Intelligence

The Publication Engine MAY use AI-assisted techniques as implementation details.

AI MAY assist with:

- publication optimization;
- layout preparation;
- template selection;
- quality validation.

AI SHALL NOT:

- generate operational facts;
- modify Official Open Data;
- change territorial grouping;
- alter editorial rules.

All generated Publications SHALL remain fully deterministic.

---

# 17. Multi-Channel Publishing

The Publication Engine SHALL remain independent of any specific publication platform.

Telegram Journal is the current primary publication channel.

Future publication channels MAY include:

- PWA;
- Web Portal;
- Public API;
- Push Notifications.

Publication generation SHALL remain channel-independent.

---

# 18. Non-Goals

The Publication Engine SHALL NOT:

- collect Official Open Data;
- normalize datasets;
- archive datasets;
- calculate analytics;
- modify territorial relationships.

These responsibilities belong to other system components.

---

# 19. Repository Rule

Normative documents SHALL reference the Publication Engine as the only component responsible for generating Publications from the Normalized Dataset.

Editorial presentation SHALL be defined exclusively by the Telegram Journal Specification.

---

# 20. References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- GLOSSARY.md
- TERRITORIAL_MODEL.md
- DATA_MODEL.md
- SSP-001 — Data Pipeline
- SSP-002 — Parser

## Referenced by

- Telegram Journal Specification
- SSP-005 — Data Storage
- Future Publication Channels

---

# End of Specification
