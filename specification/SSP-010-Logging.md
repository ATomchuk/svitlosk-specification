# SSP-010 — Logging

Status: Draft (Чернетка)

Specification ID: SSP-010

Component: Logging

Document Class: Normative

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official logging requirements for the SvitloSk system.

Logging provides traceability, diagnostics, auditing and operational visibility across all system components.

This document is normative.

---

# 2. Scope

This specification defines:

- logging principles;
- log levels;
- log format;
- log storage;
- log retention;
- log security;
- audit events.

---

# 3. Principles

Logging SHALL be:

- consistent;
- machine-readable;
- timestamped;
- deterministic;
- searchable;
- secure.

Logs SHALL never alter application behavior.

---

# 4. Objectives

Logging supports:

- troubleshooting;
- monitoring;
- debugging;
- auditing;
- incident investigation;
- performance analysis.

---

# 5. Log Levels

The following levels SHALL be used.

| Level | Purpose |
|--------|---------|
| DEBUG | Development diagnostics |
| INFO | Normal system events |
| WARNING | Recoverable problems |
| ERROR | Service errors |
| CRITICAL | System failure requiring immediate attention |

---

# 6. Log Structure

Every log record SHALL contain:

- Timestamp (UTC)
- Log level
- Service name
- Component
- Event ID
- Message
- Execution time (if applicable)

Example:

```text
2026-07-05T16:59:03Z INFO Parser DATA_FETCH_COMPLETED duration=352ms
```

---

# 7. Service Identification

Every service SHALL identify itself.

Examples:

- Parser
- Storage
- Schedule Generator
- Graphic Generator
- Publication Engine
- Telegram Channel

---

# 8. Event Categories

Typical categories include:

- Startup
- Shutdown
- Data Fetch
- Parsing
- Validation
- Storage
- Schedule Generation
- Graphic Generation
- Publication
- Telegram Delivery
- API
- Security

---

# 9. Error Logging

Every unexpected error SHALL be logged.

Each error record SHOULD include:

- error description;
- affected service;
- operation;
- stack trace (development mode only).

Sensitive information SHALL never be logged.

---

# 10. Log Storage

Logs SHALL be stored outside the application source code.

Recommended directory:

```text
logs/
```

Daily log rotation is recommended.

---

# 11. Retention

Default retention period:

90 days.

Archived logs MAY be compressed.

---

# 12. Privacy

Logs SHALL never contain:

- passwords;
- access tokens;
- API secrets;
- personal user data.

---

# 13. Audit Events

The following events SHALL always be logged:

- service startup;
- service shutdown;
- configuration loading;
- parser execution;
- publication creation;
- Telegram publication;
- configuration changes;
- system failures.

---

# 14. Performance

Logging SHALL not significantly reduce application performance.

Asynchronous logging is recommended.

---

# 15. Future Extensions

Possible future additions:

- centralized logging;
- real-time log streaming;
- structured JSON logging;
- OpenTelemetry integration;
- log dashboards.

These extensions require separate specifications.

---

# References

## Depends on

- GLOSSARY.md — canonical terminology
- ARCHITECTURE.md — system architecture
- EDITORIAL_STANDARDS.md — editorial requirements

## Referenced by

- All services
