# SSP-005 — Data Storage

Status: Draft (Чернетка)

Specification ID: SSP-005

Component: Data Storage

Document Class: Normative

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official data storage architecture used by the SvitloSk system.

The storage layer is responsible for preserving normalized data, generated publications, schedules, historical records, and system metadata.

This document is normative.

---

# 2. Scope

This specification applies to every component that stores or retrieves persistent information.

It defines:

- storage architecture;
- supported storage formats;
- retention rules;
- historical archive;
- cache strategy;
- backup requirements.

---

# 3. Design Principles

The storage subsystem SHALL be:

- deterministic;
- lightweight;
- transparent;
- recoverable;
- platform independent.

Data SHALL never depend on proprietary software.

---

# 4. Storage Layers

The system consists of several logical layers.

## Layer 1 — Source Data

Raw official files.

Characteristics:

- immutable;
- timestamped;
- archived.

---

## Layer 2 — Parsed Data

Structured representation of official information.

Format:

JSON

Purpose:

Internal processing.

---

## Layer 3 — Normalized Data

Unified representation used by every subsystem.

Purpose:

Single source of truth.

---

## Layer 4 — Generated Content

Automatically generated:

- Telegram publications;
- graphics;
- reports;
- API responses.

---

## Layer 5 — Archive

Historical copies.

Never modified.

Only appended.

---

# 5. Storage Formats

Preferred formats:

| Type | Format |
|-------|--------|
| Structured data | JSON |
| Configuration | YAML |
| Metadata | JSON |
| Images | PNG |
| Vector graphics | SVG |
| Documents | Markdown |

No binary proprietary document formats SHALL be used internally.

---

# 6. Directory Structure

Example:

```
storage/

raw/

normalized/

generated/

graphics/

archive/

cache/

logs/
```

Directory names SHALL remain stable.

---

# 7. Data Integrity

Every stored object SHOULD contain:

- generation timestamp;
- source identifier;
- checksum (when applicable);
- schema version.

---

# 8. Historical Archive

Historical records SHALL never be overwritten.

Every publication remains reproducible.

Archive retention:

Unlimited unless configured otherwise.

---

# 9. Cache

Cache is optional.

Rules:

- disposable;
- automatically regenerated;
- never treated as source data.

Deleting cache SHALL never affect correctness.

---

# 10. Backup Strategy

Recommended:

- daily backups;
- compressed archive;
- off-device copy;
- integrity verification.

---

# 11. Recovery

The system SHALL support recovery from:

- raw source files;
- normalized data;
- archived publications.

No manual reconstruction SHOULD be required.

---

# 12. Security

Stored data SHALL be:

- read-only where possible;
- protected from accidental modification;
- validated before loading.

---

# 13. Future Extensions

Possible future additions:

- SQLite index;
- PostgreSQL backend;
- object storage;
- distributed archive.

These extensions SHALL not change the logical storage model.

---

# 14. Compliance

Every SvitloSk component that stores persistent information SHALL comply with this specification.

---

# 15. References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- GLOSSARY.md
- ARCHITECTURE.md
- DATA_MODEL.md
- SSP-001 — Data Pipeline

## Referenced by

- SSP-003 — Publication Engine
