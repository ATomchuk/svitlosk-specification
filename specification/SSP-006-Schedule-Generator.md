# SSP-006 — Schedule Generator

Status: Draft (Чернетка)

Specification ID: SSP-006

Component: Schedule Generator

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official schedule generation engine used by the SvitloSk system.

The generator transforms normalized outage data into deterministic schedules used by all presentation layers.

This document is normative.

---

# 2. Scope

The schedule generator is responsible for:

- interpreting normalized outage data;
- calculating outage periods;
- generating daily schedules;
- detecting schedule changes;
- producing machine-readable schedule objects.

---

# 3. Design Principles

The generator shall be:

- deterministic;
- predictable;
- reproducible;
- independent from presentation.

The same input shall always produce the same output.

---

# 4. Input

Input consists only of normalized data.

The generator shall not process raw source files.

Required input includes:

- queue identifier;
- subqueue identifier;
- outage intervals;
- publication date;
- source metadata.

---

# 5. Output

The generator produces schedule objects.

Each object contains:

- date;
- queue;
- subqueue;
- outage intervals;
- powered intervals;
- total outage duration;
- total powered duration;
- generation timestamp.

---

# 6. Schedule Rules

Every schedule shall represent one calendar day.

Time range:

00:00–24:00

Intervals shall never overlap.

Intervals shall always be ordered chronologically.

---

# 7. Interval Model

Each interval contains:

- start time;
- end time;
- state.

Possible states:

- Powered
- Outage

No additional states are permitted.

---

# 8. Validation

Before publication every schedule shall be validated.

Validation includes:

- chronological order;
- interval continuity;
- no overlaps;
- complete daily coverage;
- valid queue identifiers.

Invalid schedules shall not be published.

---

# 9. Change Detection

The generator shall compare the newly generated schedule with the previous version.

Detected changes include:

- added interval;
- removed interval;
- modified interval;
- publication timestamp update.

---

# 10. Consumers

Generated schedules are consumed by:

- Publication Engine;
- Telegram Channel;
- Graphic Generator;
- REST API;
- PWA Client;
- Archive subsystem.

---

# 11. Error Handling

Generation errors shall produce structured log records.

Errors shall never generate incomplete schedules.

---

# 12. Performance

The generator should complete processing within a few seconds after normalized data becomes available.

The generator shall support repeated execution without side effects.

---

# 13. Future Extensions

Possible future enhancements:

- multiple-day schedules;
- emergency schedules;
- manual correction layer;
- predictive schedule generation.

These extensions shall remain compatible with this specification.

---

# 14. Compliance

Every SvitloSk component that consumes outage schedules shall use the schedule objects defined by this specification.
