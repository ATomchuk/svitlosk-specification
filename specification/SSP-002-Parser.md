# SSP-002 — Parser

Status: Draft

Specification ID: SSP-002

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official requirements for the SvitloSk data parser.

The parser is responsible for collecting official public data, validating it, normalizing it and producing a consistent internal dataset.

The parser is the only component allowed to create the internal data model.

This document is normative.

---

# 2. Scope

This specification applies to:

- data acquisition;
- source validation;
- data normalization;
- metadata generation;
- dataset publishing.

---

# 3. Responsibilities

The parser shall:

- retrieve official public data;
- detect updates;
- validate received data;
- normalize information;
- generate metadata;
- publish a normalized dataset.

The parser shall never modify or interpret official information.

---

# 4. Data Sources

The parser accepts only official publicly available sources.

Examples include:

- planned outage schedules;
- emergency outage notifications;
- official operator publications;
- official public registries.

Unofficial sources are prohibited.

---

# 5. Input Requirements

Each input source shall contain sufficient information to identify:

- publication date;
- affected territory;
- affected settlements;
- outage periods;
- affected addresses.

Incomplete datasets shall be reported.

---

# 6. Normalization

The parser converts all incoming data into the internal data model.

Normalization includes:

- administrative hierarchy;
- settlement names;
- street names;
- house numbers;
- outage intervals;
- metadata.

After normalization all publication modules consume identical data.

---

# 7. Change Detection

The parser shall detect:

- new records;
- modified records;
- removed records.

Each detected change shall be reflected in the generated dataset.

---

# 8. Metadata

Each dataset shall include metadata:

- generation timestamp;
- source identifier;
- parser version;
- dataset identifier;
- processing status.

Metadata shall accompany every publication.

---

# 9. Error Handling

Parser failures shall never generate fictional information.

Possible actions:

- reject dataset;
- report validation errors;
- preserve previous valid dataset;
- log processing details.

---

# 10. Output

The parser produces exactly one normalized dataset.

This dataset becomes the official source for:

- Telegram Publisher;
- PWA application;
- historical archive;
- future public API.

---

# 11. Non-Goals

The parser does not:

- publish messages;
- generate graphics;
- edit Telegram posts;
- calculate analytics;
- send notifications.

These responsibilities belong to downstream components.

---

# 12. References

- SSP-001 — Data Pipeline
- DATA_MODEL.md
- SYSTEM_OVERVIEW.md
- ARCHITECTURE.md

---

End of Specification.
