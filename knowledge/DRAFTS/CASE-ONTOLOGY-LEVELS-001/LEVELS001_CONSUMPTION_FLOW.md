# Consumption Flow

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document maps consumption flow.

---

# Consumption Flow

## Consumption Chain

```
DSO
    ↓ provides
Open Data
    ↓ consumed by
Parser
    ↓ produces
Parsed Data
    ↓ consumed by
Interpreter
    ↓ produces
Interpretation Result
    ↓ consumed by
Publisher
    ↓ produces
Publication
    ↓ consumed by
Adapter
    ↓ produces
Representation
    ↓ consumed by
Channel
    ↓ consumed by
Residents
```

---

## Consumption by Level

### Level 1: CONCEPT

| Entity | Consumed By | How |
|--------|-------------|-----|
| Journal | Residents | Through channels |
| Publisher | Channels | Through adapters |
| Publication | Channels | Through adapters |
| Lifecycle | System | Governs behavior |
| Territory | Publisher | Organizes publications |
| Information | Publisher | Interpreted |
| Knowledge | Channels | Distributed |
| Open Data | Parser | Retrieved |

---

### Level 2: OBJECT

| Entity | Consumed By | How |
|--------|-------------|-----|
| Journal Edition | Residents | Through channels |
| Publication Package | Channels | Through adapters |
| Emergency Outage Publication | Residents | Through channels |
| Planned Outage Publication | Residents | Through channels |
| Queue Graph Publication | Residents | Through channels |
| Technical Publication | Residents | Through channels |
| Service Publication | Residents | Through channels |

---

### Level 3: PROCESS

| Entity | Consumed By | How |
|--------|-------------|-----|
| Parsing | System | Triggered |
| Interpretation | System | Triggered |
| Rendering | System | Triggered |
| Distribution | System | Triggered |

---

### Level 4: SERVICE

| Entity | Consumed By | How |
|--------|-------------|-----|
| Journal | Residents | Through channels |
| Publisher | Channels | Through adapters |
| Parser | System | Invoked |
| Archive | System | Invoked |

---

### Level 5: ROLE

| Entity | Consumed By | How |
|--------|-------------|-----|
| Publisher | System | Implemented |
| Interpreter | System | Implemented |
| Adapter | System | Implemented |

---

### Level 6: ARTIFACT

| Entity | Consumed By | How |
|--------|-------------|-----|
| Publication | Channels | Through adapters |
| Publication Package | Channels | Through adapters |
| Representation | Residents | Through channels |

---

### Level 7: DOCUMENT

| Entity | Consumed By | How |
|--------|-------------|-----|
| Specification | System | Referenced |
| Glossary | System | Referenced |

---

### Level 8: STATE

| Entity | Consumed By | How |
|--------|-------------|-----|
| Publication State | System | Observed |
| Lifecycle State | System | Observed |
| Channel State | Adapter | Observed |

---

### Level 9: EVENT

| Entity | Consumed By | How |
|--------|-------------|-----|
| Data Changed | Lifecycle | Detected |
| Publication Expired | Publisher | Detected |
| Channel Connected | Adapter | Detected |

---

# Consumption Flow Summary

| Consumer | Consumes | Count |
|----------|----------|-------|
| Residents | Journal, Journal Edition, Emergency Outage Publication, Planned Outage Publication, Queue Graph Publication, Technical Publication, Service Publication, Representation | 8 |
| Channels | Publisher, Publication, Publication Package, Knowledge | 4 |
| System | Parser, Archive, Specification, Glossary, Publication State, Lifecycle State, Channel State, Data Changed, Publication Expired, Channel Connected | 10 |
| Lifecycle | Publication Expired | 1 |
| **Total** | | **15** |

---

# Traceability

| Consumption Flow | Source |
|------------------|--------|
| All consumption flows | Analysis of entity classification and architectural levels |

---

**End of Consumption Flow**
