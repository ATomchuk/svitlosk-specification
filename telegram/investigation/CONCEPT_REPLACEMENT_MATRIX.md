# CONCEPT_REPLACEMENT_MATRIX

**Document ID:** CASE001G-REPLACEMENT

**Title:** Concept Replacement Matrix

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Minimal Kernel Investigation

---

# Purpose

This document shows what can replace each reducible concept.

---

# Replacement Matrix

## Issue

**Can be replaced by:** Reporting Period

**How:**

- Reporting Period defines temporal scope (one calendar day)
- Reporting Period groups Publications temporally
- Reporting Period is already defined in GLOSSARY.md §2

**Consequences:**

- Loss of "editorial edition" meaning
- Loss of "daily edition" meaning
- Simpler concept, less semantic richness

---

## Journal

**Can be replaced by:** Publication Package (continuous)

**How:**

- Publication Package can be extended to be continuous
- Publication Package can accumulate over time
- Publication Package is already defined in GLOSSARY.md §3

**Consequences:**

- Loss of "continuous publication" meaning
- Loss of editorial identity
- Simpler concept, less semantic richness

---

## Publication Package

**Can be replaced by:** Individual Publication delivery

**How:**

- Publications can be delivered one by one
- No need for batching
- Telegram Publisher can handle individual Publications

**Consequences:**

- Loss of batching efficiency
- Loss of internal consistency guarantee
- Simpler delivery model

---

## Telegram Channel

**Can be replaced by:** Other publication channels

**How:**

- GLOSSARY.md §3 defines Publication Channel as generic
- Future mobile application, web interface could be used
- Channel is implementation detail, not domain concept

**Consequences:**

- Platform independence maintained
- Multiple channels supported
- More flexible architecture

---

## Normalized Dataset

**Can be replaced by:** Parsed Data

**How:**

- Parser produces Parsed Data
- Parsed Data can be used directly by Publication Engine
- Normalization can be done inside Parser

**Consequences:**

- Loss of normalization step
- Parser becomes more complex
- Simpler data flow

---

## Graphic

**Can be replaced by:** Text-only Publications

**How:**

- Publications can be text-only
- Graphics are optional enhancement
- Schedule information can be presented in text

**Consequences:**

- Loss of visual representation
- Simpler generation
- Less information density

---

## Territory

**Can be replaced by:** Address (direct)

**How:**

- Publications can be organized by Address directly
- No need for Territory grouping
- Address is the fundamental location unit

**Consequences:**

- Loss of geographic grouping
- More granular organization
- Simpler territorial model

---

## Community

**Can be replaced by:** Territory (implies scope)

**How:**

- Territory implies geographic scope
- Community is the top-level Territory
- No need for separate Community concept

**Consequences:**

- Loss of explicit scope definition
- Territory becomes top-level
- Simpler hierarchy

---

## Settlement

**Can be replaced by:** Address (direct)

**How:**

- Addresses can be used directly
- No need for Settlement grouping
- Address contains settlement information

**Consequences:**

- Loss of settlement grouping
- More granular organization
- Simpler geographic model

---

## Street

**Can be replaced by:** Address (direct)

**How:**

- Addresses can be used directly
- No need for Street grouping
- Address contains street information

**Consequences:**

- Loss of street grouping
- More granular organization
- Simpler geographic model

---

# Replacement Summary

| Concept | Replacement | Consequences |
|---------|-------------|--------------|
| Issue | Reporting Period | Loss of editorial meaning |
| Journal | Publication Package (continuous) | Loss of editorial identity |
| Publication Package | Individual delivery | Loss of batching |
| Telegram Channel | Other channels | More flexible |
| Normalized Dataset | Parsed Data | Simpler data flow |
| Graphic | Text-only | Loss of visual |
| Territory | Address direct | Loss of grouping |
| Community | Territory implies | Simpler hierarchy |
| Settlement | Address direct | Loss of grouping |
| Street | Address direct | Loss of grouping |

---

# End of Replacement Matrix
