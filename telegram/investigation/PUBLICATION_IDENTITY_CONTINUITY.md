# PUBLICATION_IDENTITY_CONTINUITY

**Document ID:** CASE001-PUB-IDENTITY

**Title:** Publication — Identity Continuity Analysis

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Viewpoint Audit №001

---

# Purpose

This document determines whether the identity of Publication remains the same while crossing layers, or whether a new object appears.

---

# Identity Across Layers

| Layer | Identity Mechanism | Identity Value | Same Publication? |
|-------|-------------------|----------------|-------------------|
| Reality | Content | The outage information | YES |
| Business | Territory + Date + Purpose | "Outage info for Starokostiantyniv on 2026-07-21" | YES |
| Domain | Internal ID | pub-2026-07-21-starokostiantyniv-001 | YES |
| DDD | Internal ID | pub-2026-07-21-starokostiantyniv-001 | YES |
| Editorial | Territory + Date + Template | "Starokostiantyniv + 2026-07-21 + Template A" | YES |
| Publication | Territory + Date + Template | "Starokostiantyniv + 2026-07-21 + Template A" | YES |
| Integration | Telegram Message ID | 123456789 | YES |
| Telegram | Telegram Message ID | 123456789 | YES |
| Persistence | Internal ID + DB Key | pub-2026-07-21-starokostiantyniv-001 / row-42 | YES |
| Repository | Document ID | GLOSSARY.md §3 | NO — this is the SPECIFICATION |
| Documentation | Term name | "Publication" | NO — this is the DEFINITION |

---

# Identity Continuity Analysis

## Phase 1: Reality → Business

**Transition:** DSO publishes outage data → SvitloSk creates business artifact

**Identity change:** Content-based → Territory + Date + Purpose

**Same Publication?** YES

**Reason:** The information is the same; only the framing changes.

---

## Phase 2: Business → Domain

**Transition:** Business artifact → Domain entity

**Identity change:** Territory + Date + Purpose → Internal ID

**Same Publication?** YES

**Reason:** The internal ID IDENTIFIES the same business artifact.

---

## Phase 3: Domain → DDD

**Transition:** Domain entity → Aggregate Root

**Identity change:** Internal ID → Internal ID (no change)

**Same Publication?** YES

**Reason:** DDD classification does not change identity.

---

## Phase 4: DDD → Editorial

**Transition:** Aggregate Root → Editorial product

**Identity change:** Internal ID → Territory + Date + Template

**Same Publication?** YES

**Reason:** The editorial description DESCRIBES the same entity.

---

## Phase 5: Editorial → Publication

**Transition:** Editorial product → Deterministic information unit

**Identity change:** Territory + Date + Template → Territory + Date + Template (no change)

**Same Publication?** YES

**Reason:** Same identity mechanism.

---

## Phase 6: Publication → Integration

**Transition:** Information unit → Telegram message

**Identity change:** Territory + Date + Template → Telegram Message ID

**Same Publication?** YES

**Reason:** Telegram Message ID REFERENCES the same information unit.

---

## Phase 7: Integration → Telegram

**Transition:** Telegram message → Channel message

**Identity change:** Telegram Message ID → Telegram Message ID (no change)

**Same Publication?** YES

**Reason:** Same identity mechanism.

---

## Phase 8: Telegram → Persistence

**Transition:** Channel message → Database record

**Identity change:** Telegram Message ID → Internal ID + DB Key

**Same Publication?** YES

**Reason:** The database record STORES the same channel message.

---

## Phase 9: Persistence → Repository

**Transition:** Database record → Specification artifact

**Identity change:** Internal ID + DB Key → Document ID

**Same Publication?** NO

**Reason:** The repository document is the SPECIFICATION of Publication, not Publication itself.

---

## Phase 10: Repository → Documentation

**Transition:** Specification artifact → Normative definition

**Identity change:** Document ID → Term name

**Same Publication?** NO

**Reason:** The documentation is the DEFINITION of Publication, not Publication itself.

---

# Identity Continuity Verdict

## One Object or Multiple Objects?

**ONE OBJECT.**

**Evidence:**

1. **Phases 1-8 maintain identity** — the same Publication flows through Reality, Business, Domain, DDD, Editorial, Publication, Integration, Telegram, and Persistence layers.

2. **Phases 9-10 describe the SPECIFICATION** — Repository and Documentation layers describe Publication, they do not contain Publication.

3. **Identity mechanisms change, but identity persists:**

| Phase | Old Identity | New Identity | Same Publication? |
|-------|-------------|--------------|-------------------|
| 1→2 | Content | Territory + Date + Purpose | YES |
| 2→3 | Territory + Date + Purpose | Internal ID | YES |
| 3→4 | Internal ID | Internal ID | YES |
| 4→5 | Internal ID | Territory + Date + Template | YES |
| 5→6 | Territory + Date + Template | Territory + Date + Template | YES |
| 6→7 | Territory + Date + Template | Telegram Message ID | YES |
| 7→8 | Telegram Message ID | Telegram Message ID | YES |
| 8→9 | Telegram Message ID | Internal ID + DB Key | YES |

4. **What does NOT change:**

| Property | Evidence |
|----------|----------|
| Information content | Same outage information |
| Territorial scope | Same Territory |
| Temporal scope | Same Date |
| Business purpose | Same resident service |
| Editorial standards | Same formatting rules |

---

## Example: Four-Layer Trace

```text
Business Publication
    │
    │ "Outage info for Starokostiantyniv on 2026-07-21"
    │
    ▼
Domain Entity
    │
    │ pub-2026-07-21-starokostiantyniv-001
    │
    ▼
Telegram Message
    │
    │ Telegram Message ID: 123456789
    │
    ▼
Repository Record
    │
    │ row-42 in publications table
    │
    ▼
SAME PUBLICATION
```

**Is this one object or four different objects?**

**ONE OBJECT.**

**Reason:**

1. Same information content
2. Same territorial scope
3. Same temporal scope
4. Same business purpose
5. Identity mechanisms are REFERENCES to the same object, not different objects

---

# End of Identity Continuity
