# Publisher Lifecycle

**Document Class:** Knowledge Base

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

This document defines the lifecycle of Publisher and its products.

---

# Journal Release Lifecycle

## States

| State | Description | Evidence |
|-------|-------------|----------|
| INACTIVE | No Journal Release exists | CASE-INF-001 |
| CREATING | Journal Release is being assembled | CASE-INF-001 |
| ACTIVE | Journal Release is live and visible | CASE-INF-001 |
| FINALIZING | Journal Release is being finalized | CASE-INF-001 |
| ARCHIVED | Journal Release is preserved permanently | CASE-INF-001 |

## Transitions

| From | To | Trigger |
|------|----|---------|
| INACTIVE | CREATING | Official data received |
| CREATING | ACTIVE | First Publication distributed |
| ACTIVE | ACTIVE | Data update received |
| ACTIVE | FINALIZING | No more updates expected |
| FINALIZING | ARCHIVED | Reporting Period ends |

---

# Publication Lifecycle

## States

| State | Description | Evidence |
|-------|-------------|----------|
| Generated | Publication created from data | TELEGRAM_LIFECYCLE.md |
| Published | Publication delivered to channel | TELEGRAM_LIFECYCLE.md |
| Updated | Publication modified | TELEGRAM_LIFECYCLE.md |
| Archived | Publication preserved permanently | TELEGRAM_LIFECYCLE.md |
| Removed | Publication deleted (temporary only) | TELEGRAM_LIFECYCLE.md |

## Transitions

| From | To | Trigger |
|------|----|---------|
| Generated | Published | Delivery to channel |
| Published | Updated | Data change |
| Updated | Published | Update delivered |
| Published | Archived | Reporting Period ends |
| Published | Removed | Expiry (temporary only) |

---

# Lifecycle Pattern

**Statement:** Lifecycle is a PATTERN, not an owned component.

**Evidence:** CASE-LC-001, CASE-PUB-004

**Implication:** Lifecycle cannot be "owned" by Publisher. Lifecycle is OBSERVED across the system.

---

# Lifecycle Operations

| Operation | Owner | Evidence |
|-----------|-------|----------|
| Detect Expiry | Lifecycle | CASE-LC-001 |
| Detect Update | Lifecycle | CASE-LC-001 |
| Execute Expiry | Publisher | CASE-PUB-005 |
| Execute Update | Publisher | CASE-PUB-005 |
| Archive Publication | Publisher | CASE-PUB-005 |

---

# Evidence

| Concept | Source |
|---------|--------|
| Journal Release Lifecycle | CASE-INF-001 |
| Publication Lifecycle | TELEGRAM_LIFECYCLE.md |
| Lifecycle Pattern | CASE-LC-001, CASE-PUB-004 |
| Lifecycle Operations | CASE-LC-001, CASE-PUB-005 |

---

**End of Lifecycle**
