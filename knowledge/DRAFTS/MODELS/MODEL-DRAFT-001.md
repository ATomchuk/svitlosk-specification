# MODEL-DRAFT-001_Publication_As_Message

**Document ID:** MODEL-DRAFT-001

**Title:** Publication as Message

**Status:** Draft

---

# Model Description

Publication IS a discrete unit of information transmitted from sender to receiver through a communication channel.

---

# Advantages

- Simple, intuitive model
- Matches common understanding of "publication"
- Explains why Telegram Message ID is part of identity
- Explains why deletions are meaningful
- Matches the forbidden terms (Message, Post)

---

# Weaknesses

- Messages are typically transient; Publications are archived permanently
- Messages are typically not updated in place; Publications are
- Messages don't have territorial grammar; Publications do
- Messages are typically one-way; Publications have complex lifecycle
- Contradicts platform independence (TJS-000)

---

# Evidence

**Supporting:**

- GLOSSARY.md: "A public information message"
- TJS-000A §17: Forbidden terms include "Message", "Post"
- Legacy TJS-003: Structure similar to message formatting

**Contradicting:**

- TJS-021: Complex lifecycle (Generated → Archived)
- TJS-000: Platform independence
- TJS-005: Territorial grammar
- Legacy TJS-007 §6: Canonical Equality

---

# Rejected Assumptions

- Publication is just a message (rejected: Publications have lifecycle, identity, ownership)
- Messages are the same as Publications (rejected: Telegram Glossary forbids this)

---

# Open Questions

1. Is "message" useful as a metaphor even if not literally accurate?
2. Does the "message" model explain too little or too much?

---

# Architect Decision

*(currently empty)*

---

# Cross References

**Origin Investigations:**

- CASE-001A
- CASE-COM-001

**Related Findings:**

- KF-003 (Publication Bridges Information and Representation)
- KF-010 (Publication Is Information Object)

---

# End of Draft Model
