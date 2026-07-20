# PUBLICATION_ENGINE_SEMANTIC_MODEL

**Document ID:** SEM-003

**Title:** Publication Engine Semantic Model

**Document Class:** Semantic Model

**Status:** COMPLETE

**Author:** Independent Architect

---

# 1. Semantic Model

Publication Engine is a **self-contained, deterministic, autonomous processing Component** that:

1. **Receives** pre-processed data from three producers (Parser, Schedule Generator, Graphic Generator)
2. **Transforms** this data into a deterministic Publication Package
3. **Manages** the complete publication lifecycle (creation, distribution, ownership, daily cycle, windows)
4. **Maintains state** through lifecycle states (Generated → Published → Updated → Archived)
5. **Guarantees** deterministic output through Canonical Equality

---

# 2. Why "Engine" Is Correct

The word "Engine" is correct because:

| Engine Property | Publication Engine Evidence |
|----------------|---------------------------|
| Autonomous execution | Operates on its own schedule |
| Deterministic transformation | Same input → identical output (Canonical Equality) |
| Self-contained lifecycle | Owns daily cycle, publication windows |
| Processing authority | Final say over publication output |
| Encapsulation | Hides internal complexity from Parser and Telegram Publisher |

---

# 3. Why It Also Performs Coordination

The Engine ALSO assembles outputs from three producers. This is a secondary responsibility — the PRIMARY responsibility is transformation. A pure Coordinator would only assemble without transforming. Publication Engine does both.

---

# 4. Semantic Verdict

**"Publication Engine" is semantically correct.** The Component is primarily an Engine (transformation + lifecycle + determinism) that also performs coordination (assembly from producers). The name captures the primary responsibility.

---

**End of Semantic Model**

**Auditor:** Independent Architect
**Date:** 2026-07-13
**Status:** COMPLETE
