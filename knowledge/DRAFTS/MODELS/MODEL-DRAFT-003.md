# MODEL-DRAFT-003_Publication_Identity_Model

**Document ID:** MODEL-DRAFT-003

**Title:** Publication Identity Model

**Status:** Draft

---

# Model Description

Publication has intrinsic identity composed of Territory + Date + Template. This identity is created at birth and never changes.

---

# Advantages

- Explains what makes Publication the same over time
- Explains why Publication is more than Information
- Explains why Publication can be updated without losing identity
- Explains why Telegram Message ID is not identity

---

# Weaknesses

- Identity is not explicitly defined in any specification
- Identity criteria are reconstructed, not documented
- No formal identity model exists in repository

---

# Evidence

**Supporting:**

- CASE-001C: "Publication identity is Territory + Date + Template"
- CASE-001D: "Publication creates its own identity"
- CASE-COM-001: "Publication CREATES its own identity"
- TJS-005, TJS-006: Imply identity through templates and rendering

**Contradicting:**

- No explicit identity definition in GLOSSARY.md
- DATA_MODEL.md requires "uniquely identifiable" but no ID exists

---

# Rejected Assumptions

- Telegram Message ID is identity (rejected: assigned after creation, platform-specific)
- Identity is composite Identifier (rejected: Identity persists when Identifier changes)
- Identity is inherited from Information (rejected: Information has no identity)

---

# Open Questions

1. Should GLOSSARY.md explicitly define Publication identity?
2. Is Territory + Date + Template sufficient, or is more needed?
3. How does this identity model apply to Manual Publications?

---

# Architect Decision

*(currently empty)*

---

# Cross References

**Origin Investigations:**

- CASE-001C
- CASE-001D
- CASE-COM-001

**Related Findings:**

- KF-001 (Publication Creates Identity)
- KF-002 (Identity ≠ Identifier)

---

# End of Draft Model
