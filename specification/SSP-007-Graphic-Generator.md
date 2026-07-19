# SSP-007 — Graphic Generator

Status: Draft (Чернетка)

Specification ID: SSP-007

Component: Graphic Generator

Document Class: Normative

Author: SvitloSk Project

---

# 1. Purpose

This specification defines the official graphic generation subsystem of the SvitloSk platform.

The subsystem automatically produces visual materials based on normalized outage schedules.

This document is normative.

---

# 2. Scope

The Graphic Generator produces:

- Tomorrow Outage Schedule;
- Emergency notifications;
- Information cards;
- Service announcements;
- Public statistics;
- Visual reports.

Every graphic SHALL be generated automatically.

---

# 3. Design Principles

Graphics SHALL be:

- clear;
- minimalistic;
- readable;
- accessible;
- deterministic;
- brand consistent.

The same input SHALL always produce identical output.

---

# 4. Branding

Every generated graphic SHALL contain official SvitloSk branding.

Mandatory elements:

- SvitloSk logo;
- project name;
- publication date;
- generation timestamp.

Brand colors:

Primary Orange

```
#EE7221
```

Primary Gray

```
#374151
```

Typography:

Inter

---

# 5. Supported Formats

The generator SHALL support:

PNG

SVG

Future support:

PDF

---

# 6. Graphic Types

## Tomorrow Schedule

Primary public information card.

Contains:

- date;
- six queues;
- twelve subqueues;
- outage intervals;
- powered intervals;
- generation timestamp;
- project branding.

---

## Emergency Card

Contains urgent information.

Priority over scheduled publications.

---

## Information Card

Contains informational messages.

No schedule timeline.

---

## Statistics Card

Contains generated statistics.

Examples:

- powered percentage;
- outage percentage;
- total outage duration.

---

# 7. Timeline Representation

Timeline represents:

00:00–24:00

States:

Powered

Outage

Intervals SHALL always be proportional to time.

---

# 8. Visual Rules

Colors SHALL always represent state.

Powered

Orange

Outage

Dark Gray

No additional semantic colors SHALL NOT be introduced.

---

# 9. Layout

Graphics SHALL be optimized for:

Telegram

Mobile devices

Desktop viewing

Printing (future)

---

# 10. Automation

Graphics SHALL be generated without manual editing.

Generation SHALL be triggered automatically after successful schedule generation.

---

# 11. Validation

Before publication every generated graphic SHALL be validated.

Validation includes:

- date;
- timeline consistency;
- branding;
- queue count;
- subqueue count;
- image dimensions.

Invalid graphics SHALL never be published.

---

# 12. Accessibility

Graphics SHALL remain readable on:

light displays;

dark displays;

small mobile screens.

---

# 13. Future Extensions

Future versions MAY include:

animated graphics;

interactive SVG;

multi-language graphics;

regional themes.

These extensions SHALL remain compatible with this specification.

---

# 14. Compliance

Every public graphic published by SvitloSk SHALL comply with this specification.

---

# References

## Depends on

- GLOSSARY.md — canonical terminology
- ARCHITECTURE.md — system architecture
- EDITORIAL_STANDARDS.md — editorial requirements

## Referenced by

- SSP-008 (Internal API) — exposes graphic data
- SSP-003 (Publication Engine) — consumes graphics
- SSP-004 (Telegram Channel) — delivers graphics
