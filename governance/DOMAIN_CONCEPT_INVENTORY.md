# DOMAIN_CONCEPT_INVENTORY

**Document ID:** DOA-002

**Title:** Domain Concept Inventory

**Document Class:** Concept Inventory

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Business Domain Concepts (12)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | Journal | TJS-000 | Continuous informational publication |
| 2 | Issue | TJS-000 | One editorial edition for a single day |
| 3 | Publication | TJS-000 | One independent publication belonging to an Issue |
| 4 | Publication Package | TJS-000 | Collection of publications for a territory |
| 5 | Territory | TJS-022 | Publication unit: Administrative Centre or Starosta District |
| 6 | Settlement | TJS-022 | Populated place within a territory |
| 7 | Street | TJS-022 | Road name within an address |
| 8 | Address | TJS-022 | Geographical location from official Data Source |
| 9 | Time Interval | TJS-022 | Continuous time for electricity availability |
| 10 | Community | TJS-022 | Primary territorial scope |
| 11 | Starosta District | TJS-022 | Territorial subdivision |
| 12 | Administrative Centre | TJS-022 | Principal territorial unit |

---

# 2. Architecture Concepts (10)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | Publication Engine | TJS-010 | Canonical Component for generating Publications |
| 2 | Parser | TJS-010 | Component for retrieving Open Data |
| 3 | Publisher (Role) | TJS-010 | Logical role for preparation/distribution |
| 4 | Telegram Publisher | TJS-010 | Telegram-specific Publisher implementation |
| 5 | Schedule Generator | TJS-010 | Generates deterministic schedules |
| 6 | Graphic Generator | TJS-010 | Produces visual materials |
| 7 | Data Storage | TJS-010 | Preserves data and records |
| 8 | Telegram Channel | TJS-010 | Delivers Publications to subscribers |
| 9 | SvitloSk | TJS-000 | Project name |
| 10 | Telegram | TJS-000 | Primary publication channel |

---

# 3. Lifecycle Concepts (12)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | Publication Lifecycle | TJS-021 | Complete lifecycle of a Publication |
| 2 | Lifecycle State | TJS-021 | One of the states a Publication passes through |
| 3 | Generated | TJS-021 | Created but not yet published |
| 4 | Published | TJS-021 | Live and visible to readers |
| 5 | Updated | TJS-021 | Modified after initial publication |
| 6 | Archived | TJS-021 | Preserved as historical record |
| 7 | Removed | TJS-021 | Temporary Publication deleted |
| 8 | Publication Session | TJS-021 | One execution producing a Journal state |
| 9 | Daily Publication Cycle | TJS-021 | Daily operational cycle |
| 10 | Publication Windows | TJS-021 | Time windows for Engine operation |
| 11 | Temporary Publication | TJS-021 | May be removed after becoming irrelevant |
| 12 | Permanent Publication | TJS-021 | Remains in Journal permanently |

---

# 4. Editorial Concepts (14)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | Editorial Policy | TJS-020 | Editorial standards for text publications |
| 2 | Editorial Principles | TJS-020 | Foundational principles |
| 3 | Territory Presentation | TJS-020 | Territory display rules |
| 4 | Message Categories | TJS-020 | Content categories |
| 5 | Time Format | TJS-020 | Time display rules |
| 6 | Settlement Formatting | TJS-020 | Settlement name display |
| 7 | Address Formatting | TJS-020 | Address display |
| 8 | Branding | TJS-020 | Publication branding rules |
| 9 | Editing Rules | TJS-020 | Post-publication corrections |
| 10 | Formatting | TJS-020 | Text presentation rules |
| 11 | Formatting Rules | TJS-020 | Text presentation rules |
| 12 | Validation Rules | TJS-022 | Structural conformance |
| 13 | Publication Structure | TJS-022 | Structural format |
| 14 | Publication Grammar | TJS-022 | Hierarchical structure rules |

---

# 5. Rendering Concepts (14)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | Rendering Pipeline | TJS-022 | Processing stages sequence |
| 2 | Rendering | TJS-022 | Converting data to presentation-ready Publication |
| 3 | Deterministic Rendering | TJS-022 | Same input produces identical output |
| 4 | Stable Ordering | TJS-022 | Deterministic ordering rules |
| 5 | Source Fidelity | TJS-022 | Rendering does not modify official info |
| 6 | Territory Ordering | TJS-022 | Territory generation order |
| 7 | Time Ordering | TJS-022 | Time interval sorting |
| 8 | Settlement Ordering | TJS-022 | Settlement alphabetical order |
| 9 | Street Ordering | TJS-022 | Street alphabetical order |
| 10 | Duplicate Removal | TJS-022 | Duplicate address removal |
| 11 | Long Publication Split | TJS-022 | Split oversized publications |
| 12 | HTML Rendering Rules | TJS-022 | Allowed HTML tags |
| 13 | Stable Output Rule | TJS-022 | No cosmetic changes |
| 14 | Empty Block Rule | TJS-022 | No empty sections |

---

# 6. Platform Concepts (11)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | Channel | TJS-010 | Communication medium |
| 2 | Telegram Message ID | TJS-010 | Platform message identifier |
| 3 | Telegram Bot API | TJS-010 | Bot interface |
| 4 | Rate Limiting | TJS-010 | API constraints |
| 5 | Message Editing | TJS-010 | Post-publication modification |
| 6 | Channel Administration | TJS-010 | Channel management |
| 7 | Subscribers | TJS-010 | End consumers |
| 8 | Administrators | TJS-010 | Channel managers |
| 9 | Manual Publications | TJS-010 | Administrator-created |
| 10 | Image Publications | TJS-010 | Visual publications |
| 11 | Telegram Publisher | TJS-010 | Telegram-specific Publisher |

---

# 7. Quality Concepts (8)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | Traceability | TJS-010 | Origin identification |
| 2 | Reliability | TJS-010 | Non-duplication, order preservation |
| 3 | Canonical Equality | TJS-010 | Byte-for-byte identical output |
| 4 | Error Handling | TJS-010 | Failure recovery rules |
| 5 | Powered | TJS-022 | No outage state |
| 6 | Archive | TJS-010 | Historical preservation |
| 7 | Publication Ownership | TJS-010 | Component ownership model |
| 8 | Non-destructive principles | TJS-010 | Channel and Update principles |

---

# 8. Architectural Principles (7)

| # | Concept | Owner | Definition |
|---|---------|-------|-----------|
| 1 | SSOT | TJS-000 | Single Source of Truth |
| 2 | SRP | TJS-000 | Single Responsibility Principle |
| 3 | Separation of Concerns | TJS-000 | Policy vs Implementation |
| 4 | Semantic Ownership Principle | TJS-000 | Semantic Model owns terminology |
| 5 | One Document — One Subject | TJS-000 | One subject per document |
| 6 | Dependency Direction | TJS-000 | Unidirectional dependencies |
| 7 | Metadata Compliance | TJS-000 | Required metadata fields |

---

# 9. Concept Summary

| Layer | Count |
|-------|-------|
| Business Domain | 12 |
| Architecture | 10 |
| Lifecycle | 12 |
| Editorial | 14 |
| Rendering | 14 |
| Platform | 11 |
| Quality | 8 |
| Architectural Principles | 7 |
| **Total** | **88 canonical concepts** |

---

**End of Concept Inventory**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
