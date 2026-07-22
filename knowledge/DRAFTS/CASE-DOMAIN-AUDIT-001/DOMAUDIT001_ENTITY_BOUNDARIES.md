# Entity Boundaries

**Document Class:** Domain Completeness Audit

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines entity boundaries.

---

# Entity Boundaries

## Journal Boundary

### What Belongs

- Journal
- Journal Edition

### What Does NOT Belong

- Publication (separate domain)
- Channel (separate domain)
- Adapter (separate domain)

### Boundary Rule

Journal is the SERVICE that produces Journal Editions.

Journal Edition is the PRODUCT that contains Publications.

---

## Publisher Boundary

### What Belongs

- Publisher
- Publication Engine
- Publication Package

### What Does NOT Belong

- Parser (separate domain)
- Channel (separate domain)
- Adapter (separate domain)

### Boundary Rule

Publisher PREPARES and DISTRIBUTES Publications.

Publisher does NOT retrieve data or deliver to channels.

---

## Publication Boundary

### What Belongs

- Publication
- Publication State
- Publication Version
- Publication History
- Publication Identity
- Publication Context

### What Does NOT Belong

- Journal (separate domain)
- Publisher (separate domain)
- Channel (separate domain)

### Boundary Rule

Publication is the ATOMIC UNIT of information.

Publication has lifecycle, identity, and context.

---

## Information Product Boundary

### What Belongs

- Information Product
- Emergency Outage Publication
- Planned Outage Publication
- Queue Graph Publication
- Technical Publication
- Service Publication

### What Does NOT Belong

- Publication (separate domain)
- Publisher (separate domain)

### Boundary Rule

Information Product is a SPECIALIZATION of Publication.

Each product type has specific content and lifetime.

---

## Lifecycle Boundary

### What Belongs

- Lifecycle
- Lifecycle State
- Lifecycle Transition

### What Does NOT Belong

- Publication (separate domain)
- Publisher (separate domain)

### Boundary Rule

Lifecycle is a PATTERN, not an owned component.

Lifecycle governs temporal behavior of all entities.

---

## Parser Boundary

### What Belongs

- Parser
- Parsed Data
- Normalized Dataset

### What Does NOT Belong

- Publisher (separate domain)
- Channel (separate domain)

### Boundary Rule

Parser RETRIEVES and NORMALIZES data.

Parser does NOT interpret or publish.

---

## Territory Boundary

### What Belongs

- Territory
- Administrative Centre
- Starosta District
- Settlement
- Street
- Address

### What Does NOT Belong

- Publication (separate domain)
- Publisher (separate domain)

### Boundary Rule

Territory is REFERENCE DATA for geographic organization.

Territory does NOT contain publications.

---

## Information Boundary

### What Belongs

- Information
- Knowledge
- Open Data

### What Does NOT Belong

- Publication (separate domain)
- Publisher (separate domain)

### Boundary Rule

Information is FACTUAL CONTENT from official sources.

Knowledge is INTERPRETED information.

---

## Schedule Boundary

### What Belongs

- Schedule
- Queue
- Subqueue
- Graph Publication
- Text Publication
- Technical Publication

### What Does NOT Belong

- Publisher (separate domain)
- Channel (separate domain)

### Boundary Rule

Schedule is ELECTRICITY AVAILABILITY data.

Schedule is NOT address-based.

---

## Representation Boundary

### What Belongs

- Representation
- Rendering

### What Does NOT Belong

- Publication (separate domain)
- Publisher (separate domain)

### Boundary Rule

Representation is CHANNEL-SPECIFIC output.

Rendering is CONVERSION process.

---

## Channel Boundary

### What Belongs

- Channel
- Adapter
- Telegram Adapter
- Facebook Adapter

### What Does NOT Belong

- Publisher (separate domain)
- Publication (separate domain)

### Boundary Rule

Channel DELIVERS information to residents.

Adapter IMPLEMENTS channel-specific behavior.

---

## Archive Boundary

### What Belongs

- Archive
- Historical Record

### What Does NOT Belong

- Publication (separate domain)
- Publisher (separate domain)

### Boundary Rule

Archive PRESERVES historical information.

Archive is PERMANENT storage.

---

# Traceability

| Boundary | Source |
|----------|--------|
| All boundaries | Analysis of entity inventory and domain knowledge |

---

**End of Entity Boundaries**
