# LC001_RESEARCH4_UPDATE

**Document ID:** CASE-LC-001-R4

**Title:** Update Behavior

**Document Class:** Research Draft

**Status:** Draft

**Author:** SvitloSk Project — Architectural Investigation

---

# 1. Purpose

This document investigates update behavior and determines the complete causal chain.

---

# 2. Update Scenario

## 2.1 Scenario

Parser updates today.txt every two hours.

Question: Who decides that an existing Telegram post must be edited?

- Parser?
- Lifecycle?
- Publisher?
- Telegram Adapter?

---

# 3. Causal Chain Analysis

## 3.1 Chain A: Parser-Driven

```
Parser detects new data
    ↓
Parser acquires new data
    ↓
Parser normalizes new data
    ↓
Parser notifies Lifecycle
    ↓
Lifecycle determines update needed
    ↓
Lifecycle notifies Publisher
    ↓
Publisher generates new Publication
    ↓
Publisher notifies Adapter
    ↓
Adapter updates Telegram post
```

### Analysis

Parser is the TRIGGER.

Lifecycle is the DECISION MAKER.

Publisher is the EXECUTOR.

Adapter is the DELIVERER.

---

## 3.2 Chain B: Lifecycle-Driven

```
Lifecycle detects time-based trigger
    ↓
Lifecycle requests data from Parser
    ↓
Parser acquires new data
    ↓
Parser normalizes new data
    ↓
Parser returns data to Lifecycle
    ↓
Lifecycle determines update needed
    ↓
Lifecycle notifies Publisher
    ↓
Publisher generates new Publication
    ↓
Publisher notifies Adapter
    ↓
Adapter updates Telegram post
```

### Analysis

Lifecycle is the TRIGGER.

Parser is the DATA PROVIDER.

Lifecycle is the DECISION MAKER.

Publisher is the EXECUTOR.

Adapter is the DELIVERER.

---

## 3.3 Chain C: Event-Driven

```
Event: "Data changed"
    ↓
Handler: Parser (acquires new data)
    ↓
Event: "Data normalized"
    ↓
Handler: Lifecycle (determines update needed)
    ↓
Event: "Update needed"
    ↓
Handler: Publisher (generates new Publication)
    ↓
Event: "Publication ready"
    ↓
Handler: Adapter (updates Telegram post)
```

### Analysis

Each step is an EVENT.

Each event has a DESIGNATED HANDLER.

No single component owns the entire chain.

---

# 4. Decision Point Analysis

## 4.1 Who DECIDES that an update is needed?

### Candidate: Parser

**Evidence for:**
- Parser detects new data
- Parser knows when data changes

**Evidence against:**
- Parser does NOT know about publication state
- Parser does NOT know about channel state
- Parser only knows about DATA state

**Verdict:** Parser detects DATA CHANGES but does not decide about PUBLICATION UPDATES.

---

### Candidate: Lifecycle

**Evidence for:**
- Lifecycle knows about INFORMATION STATE
- Lifecycle knows about TEMPORAL RULES
- Lifecycle can determine if update is needed

**Evidence against:**
- Lifecycle does not know about PUBLICATION STATE
- Lifecycle does not know about CHANNEL STATE

**Verdict:** Lifecycle determines if UPDATE IS NEEDED based on information state and temporal rules.

---

### Candidate: Publisher

**Evidence for:**
- Publisher knows about PUBLICATION STATE
- Publisher knows about CHANNEL STATE
- Publisher can determine if publication needs update

**Evidence against:**
- Publisher does not know about INFORMATION STATE
- Publisher does not know about TEMPORAL RULES

**Verdict:** Publisher determines if PUBLICATION NEEDS UPDATE based on publication state.

---

### Candidate: Adapter

**Evidence for:**
- Adapter knows about CHANNEL STATE
- Adapter can determine if channel message needs update

**Evidence against:**
- Adapter does not know about INFORMATION STATE
- Adapter does not know about PUBLICATION STATE

**Verdict:** Adapter determines if CHANNEL MESSAGE NEEDS UPDATE based on channel state.

---

# 5. Complete Causal Chain

```
1. Parser detects data change
2. Parser acquires new data
3. Parser normalizes data
4. Parser notifies system of data change
5. Lifecycle determines information has changed
6. Lifecycle determines if update is needed (temporal rules)
7. Lifecycle notifies Publisher of needed update
8. Publisher determines current publication state
9. Publisher determines if publication needs update
10. Publisher generates new/updated Publication
11. Publisher notifies Adapter
12. Adapter determines current channel state
13. Adapter determines if channel message needs update
14. Adapter updates channel message
```

---

# 6. Findings

## 6.1 Finding UPDATE-001

**The update causal chain involves FOUR subsystems.**

Parser, Lifecycle, Publisher, Adapter.

**Evidence:** Analysis of update behavior.

**Confidence:** HIGH.

## 6.2 Finding UPDATE-002

**No single subsystem decides about publication updates.**

The decision is DISTRIBUTED across the chain.

**Evidence:** Analysis of decision points.

**Confidence:** HIGH.

## 6.3 Finding UPDATE-003

**Lifecycle is the INTERMEDIARY between data changes and publication updates.**

It determines if information has changed and if update is needed.

**Evidence:** Analysis of decision points.

**Confidence:** HIGH.

## 6.4 Finding UPDATE-004

**Each subsystem makes decisions based on its OWN STATE.**

Parser knows data state.

Lifecycle knows information state.

Publisher knows publication state.

Adapter knows channel state.

**Evidence:** Analysis of decision points.

**Confidence:** HIGH.

---

# 7. Traceability

| Finding | Evidence Source |
|---------|-----------------|
| UPDATE-001 | Analysis of update behavior |
| UPDATE-002 | Analysis of decision points |
| UPDATE-003 | Analysis of decision points |
| UPDATE-004 | Analysis of decision points |

---

**End of Update Behavior**
