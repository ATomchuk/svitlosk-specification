# DRAFT-F-002_Identity_Distinction

**Document ID:** DRAFT-F-002

**Title:** Identity ≠ Identifier

**Status:** Draft

---

# Statement

Identity is WHAT an object IS; Identifier is HOW it is referred to. They are fundamentally different concepts.

---

# Reasoning

The distinction between Identity and Identifier was discovered through systematic investigation of Publication's identity model:

**Observation 1: Publication Has Identity Without Identifier**

- Publication has Territory + Date + Template identity
- Publication has NO explicit Identifier defined in any specification
- DATA_MODEL.md requires "uniquely identifiable" but no Publication ID exists
- This proves Identity and Identifier are separable

**Observation 2: Telegram Message ID Is External Reference**

- Telegram Message ID is assigned AFTER Publication is created
- Publication exists in Generated state BEFORE Telegram Message ID
- Telegram Message ID is platform-specific, not intrinsic
- This proves Identifier is not Identity

**Observation 3: Identity Persists, Identifier Can Change**

- Publication identity (Territory + Date + Template) never changes
- Telegram Message ID can be released (when Publication is removed)
- If Publication is re-published, it gets a new Telegram Message ID
- This proves Identity persists while Identifier can change

**Observation 4: Two Publications Can Share Identifier Pattern**

- Two Publications for same Territory on same Date would have same Identity pattern
- But they would have different Telegram Message IDs
- This proves Identity and Identifier are independent

---

# Evidence

- CASE-001D: "Identity is WHAT an object IS; Identifier is HOW it is referred to"
- CASE-001D: "Publication has identity (Territory + Date + Template) but no explicit Identifier"
- CASE-001C: "Identity is Territory + Date + Template"
- CASE-001C: "Telegram Message ID is external reference, not identity"

---

# Origin Investigations

- CASE-001D (Identity vs Identifier)
- CASE-001C (Identity Investigation)

---

# Confidence

HIGH — 4 independent investigations reached same conclusion.

---

# Possible Alternatives

**Alternative A:** Identity and Identifier are the same thing.

**Why rejected:** Publication has Identity (Territory + Date + Template) but no Identifier. Telegram Message ID is assigned after creation, proving it is not Identity.

**Alternative B:** Identity is just a composite Identifier.

**Why rejected:** Identity persists when Identifier changes. Identity exists before Identifier is assigned. They have different lifecycles.

---

# Questions Still Open

1. Does every Object in the repository have this distinction?
2. Is there a formal definition of Identity that could be added to GLOSSARY.md?
3. How does this distinction affect DDD Entity vs Value Object classification?

---

# Cross References

**Origin Investigations:**

- CASE-001D
- CASE-001C

**Related Findings:**

- KF-002 (Identity ≠ Identifier) — canonical version
- KF-001 (Publication Creates Identity)
- KF-009 (Publication creates own identity)

**Related Models:**

- KM-001 (Publication Identity Model)

---

# End of Draft Finding
