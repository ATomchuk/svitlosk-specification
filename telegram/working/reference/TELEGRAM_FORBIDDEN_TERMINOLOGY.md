# Telegram Forbidden Terminology

**Date:** 2026-07-13
**Purpose:** All rejected synonyms — SHALL NOT become canonical
**Source:** TELEGRAM_SEMANTIC_TERM_REVIEW.md

---

# Forbidden Terms

These terms SHALL NOT become canonical in the Telegram Glossary. They are rejected for specific architectural or semantic reasons.

---

## F-001: Message

| Field | Value |
|-------|-------|
| Forbidden Term | Message |
| Alternative | Telegram Message |
| Reason | Hidden synonym for "Publication." The term "Message" is a Telegram platform concept (a message object in Telegram's API), NOT a semantic concept for the Journal. Using "Message" to mean "Publication" conflates platform implementation with semantic model. |
| Recommended Replacement | Publication (for semantic meaning); Telegram Message ID (for platform identifier) |
| Documents Where Found | TJS-007 §10 ("stored Telegram Message ID"), TJS-007 §11 ("Publisher-owned Posts") |
| Severity | MEDIUM |

---

## F-002: Post

| Field | Value |
|-------|-------|
| Forbidden Term | Post |
| Alternative | — |
| Reason | Hidden synonym for "Publication." "Post" is a social media concept (Facebook, Twitter) that conflicts with the Journal's identity as an "official automated public information journal" (TJS-001 §9). Using "Post" trivializes the Journal's mission. |
| Recommended Replacement | Publication |
| Documents Where Found | TJS-003 filename ("Post Structure"), TJS-007 §11 ("Publisher-owned Posts") |
| Severity | MEDIUM |

---

## F-003: Telegram Message

| Field | Value |
|-------|-------|
| Forbidden Term | Telegram Message |
| Alternative | Publication (semantic); Telegram Message ID (platform) |
| Reason | Conflates the semantic concept "Publication" with the platform concept "Telegram Message." These are DIFFERENT abstraction levels. A Publication is a semantic entity; a Telegram Message is a platform delivery mechanism. |
| Recommended Replacement | Publication (for semantic meaning); Telegram Message ID (for platform identifier) |
| Documents Where Found | TJS-007 §10, §12 |
| Severity | MEDIUM |

---

## F-004: Daily Page

| Field | Value |
|-------|-------|
| Forbidden Term | Daily Page |
| Alternative | Issue, Today's Package |
| Reason | Not used in any Telegram document. "Page" is a web/print concept that conflicts with the Journal's identity as a Telegram publication, not a web page. |
| Recommended Replacement | Issue (for semantic concept); Today's Package (for operational concept) |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-005: Publication Set

| Field | Value |
|-------|-------|
| Forbidden Term | Publication Set |
| Alternative | Publication Package, Today's Package |
| Reason | Not used in any Telegram document. "Set" is a mathematical concept that doesn't match the Journal's terminology. The correct term is "Publication Package" (TJS-004 §4) or "Today's Package" (TJS-008 §4). |
| Recommended Replacement | Publication Package |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-006: Feed

| Field | Value |
|-------|-------|
| Forbidden Term | Feed |
| Alternative | Journal |
| Reason | Not used in any Telegram document. "Feed" is a social media concept (Facebook Feed, Twitter Feed) that conflicts with the Journal's identity. The Journal is NOT a feed — it is an "official automated public information journal." |
| Recommended Replacement | Journal |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-007: Page

| Field | Value |
|-------|-------|
| Forbidden Term | Page |
| Alternative | Publication, Issue |
| Reason | Not used as a semantic concept. "Page" is a web/print concept. The Journal is a Telegram publication, not a web page. |
| Recommended Replacement | Publication (for individual items); Issue (for daily editions) |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-008: Coordinator

| Field | Value |
|-------|-------|
| Forbidden Term | Coordinator |
| Alternative | — |
| Reason | NOT USED in any Telegram document. Not part of the Telegram subsystem vocabulary. This term belongs to other system architectures (e.g., microservice coordination) but has no role in the Journal Publishing System. |
| Recommended Replacement | — (do not use) |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-009: Workflow

| Field | Value |
|-------|-------|
| Forbidden Term | Workflow |
| Alternative | Daily Publication Cycle, Processing Flow |
| Reason | NOT USED as a semantic concept in Telegram documents. The Journal has "Daily Publication Cycle" (temporal) and "Processing Flow" (operational) — "Workflow" is a generic term that adds no semantic value. |
| Recommended Replacement | Daily Publication Cycle (for temporal); Processing Flow (for operational) |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-010: Working Repository

| Field | Value |
|-------|-------|
| Forbidden Term | Working Repository |
| Alternative | — |
| Reason | NOT a Telegram semantic concept. This is a Git repository governance concept. The Telegram subsystem operates within a repository but the repository itself is not a Telegram concept. |
| Recommended Replacement | — (do not use in Telegram context) |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-011: Historical Storage

| Field | Value |
|-------|-------|
| Forbidden Term | Historical Storage |
| Alternative | Archive, Historical Archive |
| Reason | NOT USED as a semantic concept in Telegram documents. The correct terms are "Archive" (state) and "Historical Archive" (concept defined in TJS-001 §11). "Historical Storage" is a technical implementation term, not a semantic concept. |
| Recommended Replacement | Archive |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-012: Journal Finality

| Field | Value |
|-------|-------|
| Forbidden Term | Journal Finality |
| Alternative | — |
| Reason | NOT USED in any Telegram document. Not a semantic concept. "Finality" is a distributed systems concept (blockchain finality) that has no meaning in the Journal Publishing System. |
| Recommended Replacement | — (do not use) |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-013: Repository

| Field | Value |
|-------|-------|
| Forbidden Term | Repository |
| Alternative | — |
| Reason | NOT a Telegram semantic concept. This is a Git/version control concept. The Telegram subsystem is DOCUMENTED in a repository but the repository itself is not a Telegram concept. |
| Recommended Replacement | — (do not use in Telegram context) |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-014: History

| Field | Value |
|-------|-------|
| Forbidden Term | History |
| Alternative | Archive, Historical Archive |
| Reason | NOT USED as a semantic concept in Telegram documents. "History" is a generic term that conflicts with the specific "Archive" concept. The Journal has an "Archive" (state) and a "Historical Archive" (concept) — "History" is imprecise. |
| Recommended Replacement | Archive |
| Documents Where Found | Not found |
| Severity | LOW |

---

## F-015: System Publication

| Field | Value |
|-------|-------|
| Forbidden Term | System Publication |
| Alternative | Publication |
| Reason | Redundant qualifier. ALL publications in the Journal are system-generated (TJS-004 §15: "Every publication is generated automatically from structured data"). The "System" qualifier adds no semantic value. |
| Recommended Replacement | Publication |
| Documents Where Found | Not found (implicit concept only) |
| Severity | LOW |

---

## F-016: Starostyn District (misspelling)

| Field | Value |
|-------|-------|
| Forbidden Term | Starostyn District |
| Alternative | Starosta District |
| Reason | Misspelling. The correct term is "Starosta District" (with "a" ending, not "yn"). "Starosta" is the Ukrainian term for the district head. "Starostyn" is an incorrect anglicization. |
| Recommended Replacement | Starosta District |
| Documents Where Found | Audit documents (inconsistent spelling) |
| Severity | LOW |

---

## Summary

| # | Forbidden Term | Severity | Primary Reason |
|---|---------------|----------|---------------|
| F-001 | Message | MEDIUM | Hidden synonym for Publication |
| F-002 | Post | MEDIUM | Social media connotation |
| F-003 | Telegram Message | MEDIUM | Conflates platform and semantic levels |
| F-004 | Daily Page | LOW | Not used |
| F-005 | Publication Set | LOW | Not used |
| F-006 | Feed | LOW | Social media connotation |
| F-007 | Page | LOW | Web/print connotation |
| F-008 | Coordinator | LOW | Not used |
| F-009 | Workflow | LOW | Not used as semantic concept |
| F-010 | Working Repository | LOW | Not Telegram concept |
| F-011 | Historical Storage | LOW | Implementation term, not semantic |
| F-012 | Journal Finality | LOW | Not used |
| F-013 | Repository | LOW | Not Telegram concept |
| F-014 | History | LOW | Imprecise — use Archive |
| F-015 | System Publication | LOW | Redundant qualifier |
| F-016 | Starostyn District | LOW | Misspelling |

**Total Forbidden Terms:** 16

---

**End of Forbidden Terminology**

**Authorizer:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
