# IDENTITY_IDENTIFIER_MODELS

**Document ID:** CASE001D-MODELS

**Title:** Identity / Identifier — Relationship Models

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity vs Identifier Investigation

---

# Purpose

This document constructs ALL possible relationship models between Identity and Identifier.

---

# Model A: Identity Creates Identifier

## Description

Identity exists first, then Identifier is created to reference it.

## Diagram

```text
Identity ──creates──► Identifier
   │                      │
   │                      ▼
   └──────────────► Object
```

## Evidence

- Publication (Identity) exists in Generated state before Telegram Message ID (Identifier) is assigned
- Territory (Identity) exists before SvitloSk assigns any Identifier

## Fit

PARTIAL — fits Publication, Territory, Address, but not Telegram Message.

---

# Model B: Identifier Creates Identity

## Description

Identifier exists first, then Identity is created around it.

## Diagram

```text
Identifier ──creates──► Identity
   │                      │
   │                      ▼
   └──────────────► Object
```

## Evidence

- Telegram Message — Identity IS defined by Telegram Message ID
- Document — Identity IS defined by Document ID

## Fit

PARTIAL — fits Telegram Message, Document, but not Publication, Territory.

---

# Model C: Identity Independent from Identifier

## Description

Identity exists independently of any Identifier.

## Diagram

```text
Identity ──────────────► Object
   │
   │ (independent)
   │
Identifier ─────────────► Reference
```

## Evidence

- Publication exists before Telegram Message ID
- Territory exists before SvitloSk
- Address exists before any system

## Fit

GOOD — fits most objects.

---

# Model D: Identifier Is Only a Projection

## Description

Identifier is one projection of Identity, not Identity itself.

## Diagram

```text
Identity
   │
   ├──► Projection 1 (with Identifier 1)
   ├──► Projection 2 (with Identifier 2)
   └──► Projection 3 (with Identifier 3)
```

## Evidence

- Publication has multiple projections: Telegram Message (Telegram Message ID), Repository Object (Database ID), Historical Record (Archive reference)
- Each projection has its own Identifier, but all share one Identity

## Fit

GOOD — fits most objects.

---

# Model E: Identity Equals Identifier

## Description

Identity and Identifier are the same thing.

## Diagram

```text
Identity = Identifier ──► Object
```

## Evidence

- Telegram Message — Identity IS the Telegram Message ID
- Session — Identity IS the Session ID

## Fit

POOR — does not fit Publication, Territory, Address, Issue, Journal.

---

# Model F: Identity Precedes Object

## Description

Identity exists before the Object is created.

## Diagram

```text
Identity ──► Object ──► Identifier
```

## Evidence

- Territory Identity exists before any Publication is created for that Territory
- Address Identity exists before any system references it

## Fit

PARTIAL — fits real-world objects, not system-created objects.

---

# Model Comparison

| Model | Description | Fits Publication | Fits Territory | Fits Telegram Message | Fits Document |
|-------|-------------|------------------|----------------|----------------------|---------------|
| A | Identity creates Identifier | YES | YES | NO | NO |
| B | Identifier creates Identity | NO | NO | YES | YES |
| C | Identity independent | YES | YES | NO | NO |
| D | Identifier is projection | YES | YES | YES | YES |
| E | Identity equals Identifier | NO | NO | YES | YES |
| F | Identity precedes Object | YES | YES | NO | NO |

---

# Key Insight

**No single model fits all objects.**

**Different objects have different Identity/Identifier relationships.**

**The most universal model is Model D: Identifier is a projection of Identity.**

---

# End of Identity / Identifier Models
