# LC001_RESEARCH6_PUBLICATION

**Document ID:** CASE-LC-001-R6

**Title:** Publication Ownership

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document differentiates Information changes, Publication changes, and Representation changes, and determines whether they are independent events.

---

# 2. Change Types

## 2.1 Information Change

### Definition

The underlying factual content changes.

### Examples

- New planned outage is announced
- Emergency outage is updated
- Queue schedule changes

### Source

Official DSO publications.

### Ownership

DSO creates information changes.

Parser detects information changes.

---

## 2.2 Publication Change

### Definition

The prepared message for distribution changes.

### Examples

- Publication is regenerated with new information
- Publication is updated with new data
- Publication is replaced with new version

### Source

Information changes trigger publication changes.

### Ownership

Publisher executes publication changes.

---

## 2.3 Representation Change

### Definition

The visual or textual format changes.

### Examples

- Telegram message is edited
- Facebook post is updated
- PWA display changes

### Source

Publication changes trigger representation changes.

### Ownership

Adapter executes representation changes.

---

# 3. Independence Analysis

## 3.1 Are They Independent?

**NO.**

They are CAUSALLY LINKED:

```
Information Change → Publication Change → Representation Change
```

## 3.2 Can They Occur Independently?

| Scenario | Possible? | Evidence |
|----------|-----------|----------|
| Information change without publication change | YES | Information may not require publication update |
| Publication change without information change | YES | Publication may be reformatted without information change |
| Representation change without publication change | YES | Channel may re-render without publication change |

## 3.3 Conclusion

The three change types are CAUSALLY LINKED but CAN occur independently.

---

# 4. Change Propagation

## 4.1 Information → Publication

```
Information Change detected by Parser
    ↓
Parser notifies Lifecycle
    ↓
Lifecycle determines if Publication update needed
    ↓
Lifecycle notifies Publisher
    ↓
Publisher executes Publication Change
```

## 4.2 Publication → Representation

```
Publication Change executed by Publisher
    ↓
Publisher notifies Adapter
    ↓
Adapter determines if Representation update needed
    ↓
Adapter executes Representation Change
```

---

# 5. Findings

## 5.1 Finding PUB-001

**There are THREE distinct change types.**

Information Change, Publication Change, Representation Change.

**Evidence:** Analysis of change types.

**Confidence:** HIGH.

## 5.2 Finding PUB-002

**The three change types are CAUSALLY LINKED.**

Information Change → Publication Change → Representation Change.

**Evidence:** Analysis of change propagation.

**Confidence:** HIGH.

## 5.3 Finding PUB-003

**The three change types CAN occur independently.**

Publication may change without information change.

Representation may change without publication change.

**Evidence:** Analysis of independence.

**Confidence:** HIGH.

## 5.4 Finding PUB-004

**Each change type has a DIFFERENT OWNER.**

Information Change: DSO/Parser.

Publication Change: Publisher.

Representation Change: Adapter.

**Evidence:** Analysis of ownership.

**Confidence:** HIGH.

---

# 6. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| PUB-001 | Analysis of change types |
| PUB-002 | Analysis of change propagation |
| PUB-003 | Analysis of independence |
| PUB-004 | Analysis of ownership |

---

**End of Publication Ownership**
