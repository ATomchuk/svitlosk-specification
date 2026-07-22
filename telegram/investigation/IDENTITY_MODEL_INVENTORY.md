# IDENTITY_MODEL_INVENTORY

**Document ID:** CASE001C-INVENTORY

**Title:** Identity — Model Inventory

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity Investigation

---

# Purpose

This document provides a complete inventory of all identity models found in the repository.

---

# Identity Models Found

## Model 1: Technical Identity

**Definition:** Identity assigned by the technical system.

**Examples in repository:**

- Telegram Message ID (TJS-000A §10)
- Database primary key (implied)
- Session ID (Legacy TJS-008 §15)

**Characteristics:**

- Assigned by system
- Immutable
- Unique
- Platform-specific

---

## Model 2: Business Identity

**Definition:** Identity determined by business meaning.

**Examples in repository:**

- Territory (GLOSSARY.md §4)
- Address (GLOSSARY.md §4)
- Queue (GLOSSARY.md §5)
- Subqueue (GLOSSARY.md §5)
- Settlement (TERRITORIAL_MODEL.md)
- Street (TERRITORIAL_MODEL.md)

**Characteristics:**

- Determined by real-world existence
- Stable
- Meaningful
- Traceable to official sources

---

## Model 3: Editorial Identity

**Definition:** Identity determined by editorial purpose.

**Examples in repository:**

- Issue (TJS-000 §4)
- Publication (TJS-000 §4)
- Publication Package (GLOSSARY.md §3)
- Journal (TJS-000 §4)

**Characteristics:**

- Determined by editorial decision
- Stable within editorial context
- Meaningful for readers
- Part of Journal hierarchy

---

## Model 4: Repository Identity

**Definition:** Identity determined by repository governance.

**Examples in repository:**

- Document IDs (DOC-000 through DOC-010)
- ADR IDs (ADR-001)
- TJS IDs (TJS-000 through TJS-022)
- SSP IDs (SSP-001 through SSP-013)

**Characteristics:**

- Assigned by governance
- Immutable
- Unique across repository
- Traceable to governing document

---

## Model 5: Historical Identity

**Definition:** Identity determined by temporal position.

**Examples in repository:**

- Daily Snapshot (DATA_MODEL.md)
- Historical Archive (GLOSSARY.md §2)
- Reporting Period (GLOSSARY.md §2)
- Processing Cycle (GLOSSARY.md §2)

**Characteristics:**

- Fixed in time
- Immutable
- Unique per time period
- Permanent

---

## Model 6: Platform Identity

**Definition:** Identity determined by platform (Telegram).

**Examples in repository:**

- Telegram Message ID (TJS-000A §10)
- Telegram Channel (TJS-000A §10)
- Subscribers (TJS-000A §10)

**Characteristics:**

- Assigned by platform
- Platform-specific
- Immutable while on platform
- Released on deletion

---

## Model 7: Lifecycle Identity

**Definition:** Identity determined by lifecycle state.

**Examples in repository:**

- Generated Publication (TJS-021 §4.1)
- Published Publication (TJS-021 §4.2)
- Updated Publication (TJS-021 §4.3)
- Archived Publication (TJS-021 §4.4)
- Removed Publication (TJS-021 §4.5)

**Characteristics:**

- Changes through transitions
- Tracks object state
- Part of object history
- Temporary

---

# Model Comparison Matrix

| Model | Creates Identity | Preserves Identity | Destroys Identity | Changes? | Migrates? |
|-------|------------------|--------------------|--------------------|----------|-----------|
| Technical | System assignment | Storage persistence | Storage deletion | NO | YES |
| Business | Real-world existence | Real-world continuity | Real-world cessation | NO | NO |
| Editorial | Editorial decision | Editorial consistency | Editorial removal | NO | NO |
| Repository | Governance registration | Repository persistence | Repository removal | NO | YES |
| Historical | Temporal position | Historical persistence | Historical erasure | NO | NO |
| Platform | Platform assignment | Platform persistence | Platform deletion | NO | NO |
| Lifecycle | State assignment | Lifecycle continuity | Lifecycle termination | YES | NO |

---

# Model Relationships

```text
Business Identity ( Territory, Address, Queue )
    │
    ▼
Editorial Identity ( Issue, Publication, Package )
    │
    ▼
Technical Identity ( Telegram Message ID, Database ID )
    │
    ▼
Platform Identity ( Telegram Channel, Subscribers )
    │
    ▼
Historical Identity ( Daily Snapshot, Archive )
    │
    ▼
Lifecycle Identity ( Generated → Published → Archived )
```

---

# End of Model Inventory
