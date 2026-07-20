# ARCHIVE_GOVERNANCE_BOUNDARY

**Document ID:** GA-004

**Title:** Archive Governance Boundary

**Document Class:** Boundary Model

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Can Any Document Exist in Multiple Layers?

**NO.** A document belongs to EXACTLY ONE layer.

---

# 2. Layer Responsibility Rules

| Layer | Responsibility | Lifecycle | Transition Rule |
|-------|---------------|-----------|-----------------|
| Root | Identity + Navigation + Foundation | Permanent | NEVER moves (Foundation is frozen) |
| governance/ | Active governance rules + baselines | Active during use | Moves to archive/ when superseded or historical |
| archive/ | Historical records | Permanent | NEVER moves back |

---

# 3. Document Lifecycle Through Layers

`
Created → governance/ (active) → archive/ (historical)
                    OR
Created → Root (permanent Foundation) → NEVER moves
`

---

# 4. Layer Boundary Violations

| Violation | Rule | Consequence |
|-----------|------|-------------|
| Document in both Root and governance/ | BOUNDARY-R1 | Architectural conflict |
| Document in both governance/ and archive/ | BOUNDARY-R2 | Lifecycle confusion |
| Document in both Root and archive/ | BOUNDARY-R3 | Contradicts permanence |
| Document moved back from archive/ to governance/ | BOUNDARY-R5 violation | Historical records are immutable |

---

**End of Archive Governance Boundary**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
