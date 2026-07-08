# TJS-007 — Publication Lifecycle

**Status:** Draft (Проєкт)

**Specification ID:** TJS-007

**Author:** SvitloSk Project

---

# 1. Purpose

This specification defines the complete lifecycle of Publications within the SvitloSk Telegram Journal.

It specifies how Publications are created, updated, retained and removed while preserving deterministic behaviour, publication integrity and channel stability.

This document is normative.

---

# 2. Scope

This specification applies to:

- Publication creation;
- Publication updates;
- Publication ownership;
- Publication ordering;
- Publication removal;
- Publication retention;
- Telegram Journal lifecycle management.

---

# 3. Publication Lifecycle

Every Publication SHALL follow the same lifecycle.

```text
Dataset

↓

Render

↓

Publish

↓

Update (if required)

↓

Retain or Remove
```

Publications SHALL only change when permitted by this specification.

---

# 4. Publication Creation

The Publisher SHALL create Publications from the normalized dataset produced by the Parser.

Every Publication SHALL:

- represent exactly one Territory;
- use one Canonical Template;
- be rendered using the Canonical Rendering Rules;
- receive a Telegram Message ID after publication.

---

# 5. Publication Updates

A Publication MAY be updated only when:

- the normalized dataset changes; or
- the rendering rules change.

Updates SHALL be performed by editing the existing Telegram Message.

A new Publication SHALL NOT be created if an existing Publication can be updated.

---

# 6. Canonical Equality

Before updating a Publication, the Publisher SHALL compare:

- the current rendered Publication;
- the newly rendered Publication.

If both Canonical Renderings are identical, no Telegram update SHALL be performed.

Equivalent Publications SHALL NOT generate Telegram edits.

---

# 7. Publication Ordering

The order of Publications SHALL remain deterministic.

The canonical order is:

1. Administrative Centre;
2. Starosta Districts in alphabetical order.

Missing Territories SHALL be skipped.

The order of remaining Publications SHALL NOT change.

---

# 8. Temporary Publications

Tomorrow Publications are temporary.

The Publisher SHALL remove Tomorrow Publications after the reporting period ends.

Only Tomorrow Publications MAY be removed automatically.

---

# 9. Permanent Publications

Current-day Publications SHALL remain in the Telegram Journal.

The Publisher SHALL NOT remove historical Publications generated for the current reporting day.

The Telegram Journal serves as the historical record of daily Publications.

---

# 10. Publication Ownership

Every Publication created by the Publisher becomes owned by the Publisher.

Ownership SHALL be determined by the stored Telegram Message ID.

Only owned Publications MAY be updated or removed.

Manual Publications SHALL never become owned Publications.

---

# 11. Non-destructive Channel Principle

The Telegram Journal SHALL be treated as a long-lived public information journal.

The Publisher SHALL modify only Publications that it owns.

The Publisher SHALL NOT modify, delete or reorder Publications created by other publishers or administrators.

The Publisher SHALL NOT interfere with manually published content, including but not limited to:

- announcements;
- application news;
- promotional publications;
- graphical publications not managed by the Publisher;
- administrator-created information.

The Publisher SHALL operate only on Telegram Message IDs belonging to its own Publication Package.

---

# 12. Publication Lifecycle Diagram

```text
                  +--------------------+
                  |      Parser        |
                  +--------------------+
                            │
                            ▼
               Normalized Dataset (immutable)
                            │
                            ▼
                 Publication Engine
                            │
                            ▼
                  Telegram Publisher
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
     Create              Update            Delete
  Publications       Changed Posts      Tomorrow Posts
        │                   │                   │
        └───────────────┬───┴───────────────────┘
                        │
                        ▼
              Telegram Journal Channel
                        │
        ┌───────────────┴────────────────┐
        │                                │
        ▼                                ▼
 Publisher-owned Posts            Administrator Posts
 (managed automatically)          (never modified)
```

---

# 13. Error Handling

Publication lifecycle failures SHALL:

- never corrupt existing Publications;
- never delete permanent Publications;
- never modify administrator-created Publications;
- be recoverable after the next successful synchronization.

---

# 14. References

Depends on:

- TERRITORIAL_MODEL.md
- DATA_MODEL.md
- SSP-002 — Parser
- SSP-003 — Publication Engine
- TJS-005 — Message Templates
- TJS-006 — Rendering Rules

Referenced by:

- Telegram Publisher implementation

---

End of Specification.
