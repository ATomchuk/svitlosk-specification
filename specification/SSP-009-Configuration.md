# SSP-009 — Configuration

Status: Draft

Specification ID: SSP-009

Version: SSP-0.1

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official configuration model of the SvitloSk system.

Configuration controls the behavior of all services without requiring source code modifications.

This document is normative.

---

# 2. Scope

This specification defines:

- configuration architecture;
- configuration files;
- environment variables;
- secrets management;
- validation;
- configuration lifecycle.

---

# 3. Principles

Configuration shall be:

- centralized;
- deterministic;
- documented;
- version-controlled;
- reproducible;
- environment-independent.

No configuration shall be hardcoded.

---

# 4. Configuration Levels

The system uses three configuration levels.

## Global

System-wide configuration.

Examples:

- project name
- timezone
- locale
- logging level

---

## Service

Configuration specific to one service.

Examples:

- Parser
- Publication Engine
- Graphic Generator

---

## Runtime

Temporary values generated during execution.

Runtime configuration shall never modify permanent configuration.

---

# 5. Configuration Sources

Configuration may originate from:

- YAML files
- JSON files
- environment variables
- secret storage

Priority (highest first):

1. Environment variables
2. Secret storage
3. Local configuration files
4. Default values

---

# 6. Directory Structure

Example:

```text
config/
    default.yaml
    production.yaml
    development.yaml
    telegram.yaml
    parser.yaml
    graphics.yaml
```

---

# 7. Environment Variables

Environment variables shall use the prefix:

```
SVITLOSK_
```

Examples:

```
SVITLOSK_ENV

SVITLOSK_TIMEZONE

SVITLOSK_LOG_LEVEL

SVITLOSK_DATA_PATH
```

---

# 8. Secrets

Secrets shall never be stored inside the repository.

Examples:

- Telegram Bot Token
- API Keys
- SMTP Passwords

Secrets shall be provided externally.

---

# 9. Validation

Configuration shall be validated before startup.

Startup shall fail if:

- required fields are missing;
- invalid values are detected;
- unsupported configuration is found.

---

# 10. Default Values

Every optional parameter shall have a documented default value.

Hidden defaults are prohibited.

---

# 11. Configuration Changes

Configuration changes shall:

- be documented;
- be traceable;
- require commit history;
- preserve backward compatibility whenever possible.

---

# 12. Backup

Configuration shall be backed up together with the system.

Secrets are backed up separately.

---

# 13. Future Extensions

Possible future additions:

- Remote configuration
- Web configuration interface
- Live configuration reload
- Configuration profiles
- Municipality-specific configuration

These extensions require separate specifications.
