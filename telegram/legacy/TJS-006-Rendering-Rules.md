# TJS-006 — Telegram Rendering Rules

Status: Draft (Чернетка)
Specification ID: TJS-006
Project: SvitloSk
Class: Normative

---

# 1. Purpose

This specification defines the canonical rendering process used by the Telegram Publisher.

Its purpose is to guarantee that identical input data always produces identical Telegram publications.

---

# 2. Scope

This specification applies to:

- Telegram publication rendering;
- formatting;
- sorting;
- grouping;
- HTML generation;
- publication validation.

---

# 3. Rendering Principles

The Telegram Publisher SHALL follow these principles.

## Deterministic Rendering

The same normalized dataset SHALL always produce identical output.

## Canonical Equality

Two publications generated from identical datasets SHALL be byte-for-byte identical.

## Human Readability

Publications SHALL prioritize readability over compactness.

## Minimal Formatting

Only formatting approved by the Editorial Policy MAY be used.

## Stable Ordering

Every rendered element SHALL follow deterministic ordering rules.

## Source Fidelity

Rendering SHALL NOT modify or reinterpret official information.

---

# 4. Rendering Pipeline

Every publication SHALL be generated using the following pipeline.

```
Normalized Dataset

↓

Validation

↓

Sorting

↓

Grouping

↓

Duplicate Removal

↓

Formatting

↓

HTML Escaping

↓

Length Validation

↓

Telegram HTML
```

---

# 5. Territory Ordering

Publications SHALL be generated in the following order:

1. Administrative Centre;
2. Starosta Districts.

Starosta Districts SHALL be ordered alphabetically.

---

# 6. Time Ordering

Time intervals SHALL always be sorted by their start time.

Example:

```
07:00–18:00

09:00–17:00

12:00–13:00
```

Multi-day intervals SHALL include dates.

Example:

```
🕘 7 July 20:15 – 8 July 16:45
```

Single-day intervals SHALL omit repeated dates.

---

# 7. Settlement Ordering

Settlements SHALL be ordered alphabetically using the Ukrainian alphabet.

---

# 8. Street Ordering

Street entries SHALL be ordered alphabetically using Natural Sort.

Examples:

```
вул. Весела

вул. Залізнична

вул. Молодіжна

пров. Садовий
```

Building numbers SHALL also use Natural Sort.

Example:

```
1

2

3

10

11
```

---

# 9. Duplicate Removal

Duplicate addresses SHALL NOT appear in publications.

If duplicate records are received, only one SHALL be rendered.

---

# 10. Long Publication Split

If a publication exceeds Telegram limits, it SHALL be divided automatically.

Split titles SHALL follow this format.

```
САМЧИКІВСЬКИЙ СО (1/2)

...

САМЧИКІВСЬКИЙ СО (2/2)
```

Publications SHALL only be split between complete Settlement blocks.

Settlement information SHALL NEVER be divided between two publications.

---

# 11. HTML Rendering Rules

Publisher SHALL generate Telegram HTML only.

Allowed tags:

- `<b>`
- `<br>`

All other HTML tags are prohibited unless explicitly approved by future specifications.

Publisher SHALL escape reserved HTML characters.

Publisher SHALL generate UTF-8 encoded output.

Trailing whitespace SHALL NOT be generated.

Empty lines SHALL follow the Editorial Policy.

---

# 12. Stable Output Rule

Publisher SHALL NOT introduce cosmetic formatting changes.

Formatting MAY change only when:

- the normalized dataset changes;
- the rendering specification changes.

---

# 13. Empty Block Rule

Publisher SHALL NOT generate empty sections.

Only sections containing information SHALL be rendered.

---

# 14. Validation Rules

Before publication the Publisher SHALL verify:

- valid HTML;
- closed HTML tags;
- valid UTF-8;
- deterministic ordering;
- no duplicate addresses;
- no empty sections;
- publication length within Telegram limits.

---

# 15. Error Handling

Rendering failures SHALL:

- be logged;
- prevent publication;
- preserve previously published information.

Publisher SHALL NEVER generate incomplete publications.

---

# 16. Future Compatibility

Future Telegram formatting capabilities SHALL NOT modify the canonical rendering behaviour unless approved by a future revision of this specification.

---

# 17. References

Depends on:

- TJS-003 — Editorial Policy
- TJS-005 — Message Templates
- SSP-003 — Publication Engine
- TERRITORIAL_MODEL.md

Referenced by:

- Telegram Publisher

---

End of Specification.
