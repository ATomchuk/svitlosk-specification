# Creation Flow

**Document Class:** Architectural Level Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document maps creation flow.

---

# Creation Flow

## Creation Chain

```
DSO
    ↓ creates
Open Data
    ↓ acquired by
Parser
    ↓ creates
Parsed Data
    ↓ normalizes to
Normalized Dataset
    ↓ interpreted by
Interpreter
    ↓ creates
Interpretation Result
    ↓ processed by
Publisher
    ↓ creates
Publication
    ↓ rendered by
Adapter
    ↓ creates
Representation
    ↓ delivered to
Channel
    ↓ received by
Residents
```

---

## Creation by Level

### Level 1: CONCEPT

| Entity | Created By | How |
|--------|------------|-----|
| Journal | System | Defined by mission |
| Publisher | System | Defined by role |
| Publication | System | Defined by concept |
| Lifecycle | System | Defined by pattern |
| Territory | System | Defined by geography |
| Information | DSO | Officially published |
| Knowledge | Interpreter | Derived from information |
| Open Data | DSO | Officially published |

---

### Level 2: OBJECT

| Entity | Created By | How |
|--------|------------|-----|
| Journal Edition | Publisher | Generated daily |
| Publication Package | Publisher | Assembled daily |
| Emergency Outage Publication | Publisher | Generated from emergency data |
| Planned Outage Publication | Publisher | Generated from planned data |
| Queue Graph Publication | Publisher | Generated from schedule data |
| Technical Publication | Publisher | Generated from system status |
| Service Publication | Publisher | Generated from announcements |

---

### Level 3: PROCESS

| Entity | Created By | How |
|--------|------------|-----|
| Parsing | Parser | Triggered by data |
| Interpretation | Interpreter | Triggered by parsed data |
| Rendering | Adapter | Triggered by publication |
| Distribution | Publisher | Triggered by publication |

---

### Level 4: SERVICE

| Entity | Created By | How |
|--------|------------|-----|
| Journal | System | Deployed |
| Publisher | System | Deployed |
| Parser | System | Deployed |
| Archive | System | Deployed |

---

### Level 5: ROLE

| Entity | Created By | How |
|--------|------------|-----|
| Publisher | System | Defined |
| Interpreter | System | Defined |
| Adapter | System | Defined |

---

### Level 6: ARTIFACT

| Entity | Created By | How |
|--------|------------|-----|
| Publication | Publisher | Generated |
| Publication Package | Publisher | Assembled |
| Representation | Adapter | Rendered |

---

### Level 7: DOCUMENT

| Entity | Created By | How |
|--------|------------|-----|
| Specification | System | Authored |
| Glossary | System | Authored |

---

### Level 8: STATE

| Entity | Created By | How |
|--------|------------|-----|
| Publication State | System | Assigned |
| Lifecycle State | System | Assigned |
| Channel State | Adapter | Assigned |

---

### Level 9: EVENT

| Entity | Created By | How |
|--------|------------|-----|
| Data Changed | Parser | Detected |
| Publication Expired | Lifecycle | Detected |
| Channel Connected | Adapter | Detected |

---

# Creation Flow Summary

| Creator | Creates | Count |
|---------|---------|-------|
| DSO | Open Data, Information, Knowledge, Open Data | 4 |
| Parser | Parsed Data, Normalized Dataset | 2 |
| Interpreter | Interpretation Result | 1 |
| Publisher | Journal Edition, Publication Package, Emergency Outage Publication, Planned Outage Publication, Queue Graph Publication, Technical Publication, Service Publication, Publication, Publication Package | 9 |
| Adapter | Representation | 1 |
| System | Journal, Publisher, Parser, Archive, Specification, Glossary, Publication State, Lifecycle State, Channel State | 9 |
| Lifecycle | Publication Expired | 1 |
| **Total** | | **18** |

---

# Traceability

| Creation Flow | Source |
|---------------|--------|
| All creation flows | Analysis of entity classification and architectural levels |

---

**End of Creation Flow**
