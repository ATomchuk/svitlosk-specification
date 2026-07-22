# Ownership

**Document Class:** Entity Nature Investigation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity ownership.

---

# Ownership

## Entities That Can Own

| Entity | Nature | Can Own | What It Owns | Evidence |
|--------|--------|---------|--------------|----------|
| Journal | SERVICE | YES | Journal Editions | CHARTER §10 |
| Journal Edition | INSTANCE | YES | Publications | CASE-JRN-001 |
| Publisher | SERVICE + ROLE | YES | Publications | GLOSSARY §7 |
| Publication Package | COLLECTION | YES | Publications | GLOSSARY §3 |
| Parser | SERVICE | YES | Parsed Data | GLOSSARY §2 |
| Archive | SERVICE | YES | Publications | GLOSSARY §2 |
| Channel | SERVICE | YES | Representations | GLOSSARY §3 |
| Adapter | SERVICE + ROLE | YES | Representations | CASE-SVT-ONTOLOGY-001 |

---

## Entities That Can Be Owned

| Entity | Nature | Can Be Owned | Owned By | Evidence |
|--------|--------|--------------|----------|----------|
| Journal Edition | INSTANCE | YES | Journal | CASE-JRN-001 |
| Publication | ARTIFACT | YES | Publisher, Journal Edition, Publication Package | GLOSSARY §3 |
| Publication Package | COLLECTION | YES | Publisher | GLOSSARY §3 |
| Parsed Data | ARTIFACT | YES | Parser | GLOSSARY §2 |
| Representation | ARTIFACT | YES | Adapter | CASE-INF-001 |

---

## Ownership Summary

| Category | Entities | Count |
|----------|----------|-------|
| Can Own | Journal, Journal Edition, Publisher, Publication Package, Parser, Archive, Channel, Adapter | 8 |
| Can Be Owned | Journal Edition, Publication, Publication Package, Parsed Data, Representation | 5 |

---

# Traceability

| Ownership | Source |
|-----------|--------|
| All ownership | Analysis of entity nature and domain knowledge |

---

**End of Ownership**
