# SSP-003 — Publication Engine

Status: Draft

Specification ID: SSP-003

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the Publication Engine of the SvitloSk system.

The Publication Engine transforms normalized data into public information products while preserving accuracy, consistency and traceability.

This document is normative.

---

# 2. Scope

This specification applies to:

- Telegram publications;
- PWA data delivery;
- publication updates;
- publication history;
- future publication channels.

---

# 3. Responsibilities

The Publication Engine shall:

- consume only normalized datasets;
- generate publications;
- detect publication changes;
- update existing publications;
- preserve publication consistency;
- maintain publication metadata.

The Publication Engine shall never modify the source dataset.

---

# 4. Input

The only accepted input is the normalized dataset produced by the Parser.

Direct access to external data sources is prohibited.

---

# 5. Publication Types

The engine supports:

- Planned outages;
- Emergency outages;
- Tomorrow schedule;
- Tomorrow outage chart;
- Service announcements;
- Technical notifications.

New publication types may be introduced by future specifications.

---

# 6. Publication Rules

Every publication shall:

- contain only official information;
- be generated automatically;
- have deterministic content;
- include generation timestamp when required.

Publications shall never contain manually added information.

---

# 7. Update Policy

Publications may be:

- created;
- updated;
- removed.

Updates shall occur only when the normalized dataset changes.

Unchanged publications shall remain untouched.

---

# 8. Telegram Behaviour

Telegram is the official publication journal of SvitloSk.

The Publication Engine shall:

- publish daily information;
- edit publications when official data changes;
- preserve historical publications for the current day;
- remove temporary "Tomorrow" publications after they become obsolete.

---

# 9. Publication Categories

The official publication order is:

1. Planned outages.
2. Emergency outages.
3. Tomorrow schedule.
4. Tomorrow outage chart.
5. Service information.

---

# 10. Publication Integrity

Every publication shall represent the current official state at the time of generation.

No publication may contain speculative information.

---

# 11. Error Handling

Publication failures shall:

- be logged;
- be retryable;
- never corrupt previous publications.

---

# 12. References

- SSP-001 — Data Pipeline
- SSP-002 — Parser
- SYSTEM_OVERVIEW.md
- ARCHITECTURE.md

---

End of Specification.
