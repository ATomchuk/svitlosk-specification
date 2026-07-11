# SSP-004 — Telegram Channel

Status: Draft (Чернетка)

Specification ID: SSP-004

Component: Telegram Channel

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official rules governing the SvitloSk Telegram channel.

The Telegram channel is the primary public information journal of the project.

This document is normative.

---

# 2. Mission

The Telegram channel provides residents of the Starokostiantyniv Territorial Community with timely, accurate and understandable information about power outages based exclusively on official public data.

The channel does not produce news.

The channel publishes structured public information.

---

# 3. Principles

The Telegram channel shall operate according to the following principles:

- Official information only.
- Automation first.
- Clear structure.
- Deterministic publications.
- Minimal editorial intervention.
- Respect for public data.
- Complete publication history.

---

# 4. Publication Categories

The official publication categories are:

1. Planned outages.
2. Emergency outages.
3. Tomorrow schedule.
4. Tomorrow outage chart.
5. Service announcements.
6. Technical information.

---

# 5. Daily Publication Cycle

## 05:00

Publication package for the current day is generated automatically.

The package includes:

- planned outages;
- emergency outages.

---

## During the day

The Publication Engine monitors official data.

If changes are detected:

- existing publications are edited;
- unchanged publications remain untouched.

---

## End of day

The publication history reflects the final official state for that day.

---

# 6. Tomorrow Schedule

If official information for the following day becomes available:

- a temporary publication shall be created;
- the publication may be updated throughout the current day;
- the publication shall be removed before it becomes obsolete.

Tomorrow publications are informational only.

They are not part of the permanent archive.

---

# 7. Tomorrow Outage Chart

The outage chart is the flagship publication of SvitloSk.

It shall:

- present the official outage schedule visually;
- be generated automatically;
- include generation timestamp;
- include the SvitloSk identity;
- use the official project design system.

The chart shall never be edited manually.

---

# 8. Administrative Structure

Publications shall follow the official administrative hierarchy.

The order is:

- Starokostiantyniv;
- Starosta districts;
- Settlements.

Every Starosta district shall be visually distinguishable.

---

# 9. Publication Integrity

Every publication represents the official state at the time of generation.

Historical publications shall preserve the final official state.

---

# 10. Editorial Policy

The Publication Engine shall never:

- rewrite official information;
- simplify addresses;
- remove official records;
- introduce assumptions.

---

# 11. Future Channels

The Publication Engine may support additional channels in the future.

Telegram remains the reference implementation.

---

# 12. References

- SSP-001 — Data Pipeline
- SSP-002 — Parser
- SSP-003 — Publication Engine
- ARCHITECTURE.md
- SYSTEM_OVERVIEW.md

---

End of Specification.
