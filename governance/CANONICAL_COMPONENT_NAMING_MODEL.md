# CANONICAL_COMPONENT_NAMING_MODEL

**Document ID:** NPA-002

**Title:** Canonical Component Naming Model

**Document Class:** Naming Model

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Naming Philosophy

Every canonical component in the SvitloSk repository follows a **functional naming** convention:

The component name describes WHAT the component does, not HOW it does it.

| Component | Functional Name | What It Does |
|-----------|----------------|-------------|
| Publication Engine | Engine | Generates and distributes publications |
| Parser | Parser | Parses external data |
| Publisher | Publisher | Prepares and distributes content |
| Telegram Publisher | Telegram Publisher | Delivers via Telegram |
| Schedule Generator | Generator | Generates schedules |
| Graphic Generator | Generator | Generates graphics |
| Data Storage | Storage | Stores data |
| Telegram Channel | Channel | Delivers to subscribers |

---

# 2. Naming Consistency

All 8 components follow the same pattern:

[Functional Role] [Domain]

Examples:
- Publication Engine
- Schedule Generator
- Graphic Generator
- Telegram Publisher
- Telegram Channel

This pattern is consistent and predictable.

---

# 3. Naming Model Verdict

**The repository follows a consistent functional naming convention.** All components are Proper Architectural Names with stable, canonical definitions.

---

**End of Naming Model**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
