# Telegram Forbidden Terms

**Date:** 2026-07-13
**Purpose:** Every rejected synonym — SHALL NOT be used in specifications
**Status:** APPROVED — semantic language frozen

---

# Forbidden Terms

These terms are REJECTED from the Telegram semantic language. They SHALL NOT be used in any Telegram specification. Each forbidden term has a canonical replacement.

---

## F-001: Message

| Field | Value |
|-------|-------|
| Forbidden Term | Message |
| Replacement | Publication (for semantic meaning); Telegram Message ID (for platform identifier) |
| Reason | Hidden synonym for "Publication." The term "Message" is a Telegram platform concept (a message object in Telegram's API), NOT a semantic concept for the Journal. Using "Message" to mean "Publication" conflates platform implementation with semantic model. |
| Documents Where Found | TJS-007 §10 ("stored Telegram Message ID"), TJS-007 §11 ("Publisher-owned Posts") |

---

## F-002: Post

| Field | Value |
|-------|-------|
| Forbidden Term | Post |
| Replacement | Publication |
| Reason | Hidden synonym for "Publication." "Post" is a social media concept (Facebook, Twitter) that conflicts with the Journal's identity as an "official automated public information journal" (TJS-001 §9). Using "Post" trivializes the Journal's mission. |
| Documents Where Found | TJS-003 filename ("Post Structure"), TJS-007 §11 ("Publisher-owned Posts") |

---

## F-003: Telegram Message

| Field | Value |
|-------|-------|
| Forbidden Term | Telegram Message |
| Replacement | Publication (for semantic meaning); Telegram Message ID (for platform identifier) |
| Reason | Conflates the semantic concept "Publication" with the platform concept "Telegram Message." These are DIFFERENT abstraction levels. A Publication is a semantic entity; a Telegram Message is a platform delivery mechanism. |
| Documents Where Found | TJS-007 §10, §12 |

---

## F-004: Daily Page

| Field | Value |
|-------|-------|
| Forbidden Term | Daily Page |
| Replacement | Issue (for semantic concept); Today's Package (for operational concept) |
| Reason | Not used in any Telegram document. "Page" is a web/print concept that conflicts with the Journal's identity as a Telegram publication, not a web page. |
| Documents Where Found | Not found |

---

## F-005: Publication Set

| Field | Value |
|-------|-------|
| Forbidden Term | Publication Set |
| Replacement | Publication Package |
| Reason | Not used in any Telegram document. "Set" is a mathematical concept that doesn't match the Journal's terminology. The correct term is "Publication Package" (TJS-004 §4) or "Today's Package" (TJS-008 §4). |
| Documents Where Found | Not found |

---

## F-006: Feed

| Field | Value |
|-------|-------|
| Forbidden Term | Feed |
| Replacement | Journal |
| Reason | Not used in any Telegram document. "Feed" is a social media concept (Facebook Feed, Twitter Feed) that conflicts with the Journal's identity. The Journal is NOT a feed — it is an "official automated public information journal." |
| Documents Where Found | Not found |

---

## F-007: Page

| Field | Value |
|-------|-------|
| Forbidden Term | Page |
| Replacement | Publication (for individual items); Issue (for daily editions) |
| Reason | Not used as a semantic concept. "Page" is a web/print concept. The Journal is a Telegram publication, not a web page. |
| Documents Where Found | Not found |

---

## F-008: Coordinator

| Field | Value |
|-------|-------|
| Forbidden Term | Coordinator |
| Replacement | — (do not use) |
| Reason | NOT USED in any Telegram document. Not part of the Telegram subsystem vocabulary. This term belongs to other system architectures (e.g., microservice coordination) but has no role in the Journal Publishing System. |
| Documents Where Found | Not found |

---

## F-009: Workflow

| Field | Value |
|-------|-------|
| Forbidden Term | Workflow |
| Replacement | Daily Publication Cycle (for temporal); Processing Flow (for operational) |
| Reason | NOT USED as a semantic concept in Telegram documents. The Journal has "Daily Publication Cycle" (temporal) and "Processing Flow" (operational) — "Workflow" is a generic term that adds no semantic value. |
| Documents Where Found | Not found |

---

## F-010: Working Repository

| Field | Value |
|-------|-------|
| Forbidden Term | Working Repository |
| Replacement | — (do not use in Telegram context) |
| Reason | NOT a Telegram semantic concept. This is a Git repository governance concept. The Telegram subsystem operates within a repository but the repository itself is not a Telegram concept. |
| Documents Where Found | Not found |

---

## F-011: Historical Storage

| Field | Value |
|-------|-------|
| Forbidden Term | Historical Storage |
| Replacement | Archive |
| Reason | NOT USED as a semantic concept in Telegram documents. The correct terms are "Archive" (state) and "Historical Archive" (concept defined in TJS-001 §11). "Historical Storage" is a technical implementation term, not a semantic concept. |
| Documents Where Found | Not found |

---

## F-012: Journal Finality

| Field | Value |
|-------|-------|
| Forbidden Term | Journal Finality |
| Replacement | — (do not use) |
| Reason | NOT USED in any Telegram document. Not a semantic concept. "Finality" is a distributed systems concept (blockchain finality) that has no meaning in the Journal Publishing System. |
| Documents Where Found | Not found |

---

## F-013: Repository

| Field | Value |
|-------|-------|
| Forbidden Term | Repository |
| Replacement | — (do not use in Telegram context) |
| Reason | NOT a Telegram semantic concept. This is a Git/version control concept. The Telegram subsystem is DOCUMENTED in a repository but the repository itself is not a Telegram concept. |
| Documents Where Found | Not found |

---

## F-014: History

| Field | Value |
|-------|-------|
| Forbidden Term | History |
| Replacement | Archive |
| Reason | NOT USED as a semantic concept in Telegram documents. "History" is a generic term that conflicts with the specific "Archive" concept. The Journal has an "Archive" (state) and a "Historical Archive" (concept) — "History" is imprecise. |
| Documents Where Found | Not found |

---

## F-015: System Publication

| Field | Value |
|-------|-------|
| Forbidden Term | System Publication |
| Replacement | Publication |
| Reason | Redundant qualifier. ALL publications in the Journal are system-generated (TJS-004 §15: "Every publication is generated automatically from structured data"). The "System" qualifier adds no semantic value. |
| Documents Where Found | Not found (implicit concept only) |

---

## F-016: Starostyn District

| Field | Value |
|-------|-------|
| Forbidden Term | Starostyn District |
| Replacement | Starosta District |
| Reason | Misspelling. The correct term is "Starosta District" (with "a" ending, not "yn"). "Starosta" is the Ukrainian term for the district head. "Starostyn" is an incorrect anglicization. |
| Documents Where Found | Audit documents (inconsistent spelling) |

---

## Summary

| # | Forbidden Term | Replacement | Reason |
|---|---------------|-------------|--------|
| F-001 | Message | Publication / Telegram Message ID | Hidden synonym |
| F-002 | Post | Publication | Social media connotation |
| F-003 | Telegram Message | Publication / Telegram Message ID | Conflates levels |
| F-004 | Daily Page | Issue / Today's Package | Not used |
| F-005 | Publication Set | Publication Package | Not used |
| F-006 | Feed | Journal | Social media connotation |
| F-007 | Page | Publication / Issue | Web/print connotation |
| F-008 | Coordinator | — | Not used |
| F-009 | Workflow | Daily Publication Cycle | Not used |
| F-010 | Working Repository | — | Not Telegram concept |
| F-011 | Historical Storage | Archive | Implementation term |
| F-012 | Journal Finality | — | Not used |
| F-013 | Repository | — | Not Telegram concept |
| F-014 | History | Archive | Imprecise |
| F-015 | System Publication | Publication | Redundant qualifier |
| F-016 | Starostyn District | Starosta District | Misspelling |

**Total Forbidden Terms:** 16

---

**End of Forbidden Terms**

**Approver:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
