# PUBLICATION_ENGINE_ARCHITECTURE_ANALYSIS

**Document ID:** TEA-003

**Title:** Publication Engine Architecture Analysis

**Document Class:** Architecture Analysis

**Status:** COMPLETE

**Author:** Independent Terminology Auditor

---

# 1. What is "Publication Engine"?

Publication Engine is:

- **An Architectural Component** — one of 8 primary components
- **NOT a Service** — it does not run as a standalone service
- **NOT a Module** — it is not a generic building block
- **NOT a Mechanism** — it is not a generic process
- **NOT a Pipeline** — it is a single component, not a sequence
- **An Engine** — a processing core that transforms input into output

The Glossary definition is explicit:

> "The architectural Component implementing the Publisher Role."

The word "Engine" is the **proper name** of this Component. It describes WHAT the component does (generates publications) and HOW (as a processing engine).

---

# 2. Why "Engine" Not "Component"?

The Glossary distinguishes between the Component classification and the Engine name:

- **Component** = architectural classification (what it IS)
- **Engine** = functional name (what it DOES)

Every Component has a functional name:

| Component | Functional Name |
|-----------|----------------|
| Publication Engine | Engine (generates publications) |
| Parser | Parser (parses data) |
| Schedule Generator | Generator (generates schedules) |
| Graphic Generator | Generator (generates graphics) |
| Data Storage | Storage (stores data) |

"Engine" is the functional name — it is NOT the architectural classification.

---

# 3. Architectural Verdict

"Publication Engine" is a **proper architectural name** for a specific Component. The Ukrainian translation should preserve the functional name's identity while being natural in Ukrainian.

---

**End of Architecture Analysis**

**Auditor:** Independent Terminology Auditor
**Date:** 2026-07-13
**Status:** COMPLETE
