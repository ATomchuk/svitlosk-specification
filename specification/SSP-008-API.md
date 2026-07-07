# SSP-008 — API Specification

Status: Draft

Specification ID: SSP-008

Version: SSP-0.1

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official internal API of the SvitloSk system.

The API is intended exclusively for communication between internal services.

Public API is outside the scope of this specification.

This document is normative.

---

# 2. Scope

This specification covers:

• service communication

• request structure

• response structure

• versioning

• error handling

• authentication

---

# 3. Principles

The API shall be:

- deterministic;
- stateless;
- versioned;
- documented;
- machine-readable.

---

# 4. Services

The following services exchange data through the API.

Parser

↓

Storage

↓

Schedule Generator

↓

Graphic Generator

↓

Publication Engine

↓

Telegram Channel

---

# 5. Request Format

JSON shall be the default format.

UTF-8 encoding is mandatory.

Example

```json
{
    "community":"Starokostiantyniv",
    "queue":"3.1",
    "date":"2026-07-05"
}
```

---

# 6. Response Format

Successful response

```json
{
    "status":"ok",
    "generated":"2026-07-05T16:59:00Z"
}
```

---

# 7. Errors

Standard HTTP status codes shall be used.

Examples

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

500 Internal Server Error

---

# 8. Versioning

API versions shall follow semantic versioning.

Example

/api/v1/

Future versions

/api/v2/

---

# 9. Authentication

Internal services shall authenticate before exchanging data.

Authentication method is implementation-specific.

---

# 10. Logging

Every API request shall be logged.

Logs shall include:

- timestamp

- service

- endpoint

- execution time

- status code

---

# 11. Reliability

Services shall retry transient failures.

Retry strategy shall use exponential backoff.

---

# 12. Security

The API shall:

- validate every request;

- reject malformed data;

- sanitize input;

- never expose internal secrets.

---

# 13. Future Extensions

Possible future additions:

- Web API

- Public API

- Municipality integration API

- Monitoring API

- Webhooks

These additions require separate specifications.
