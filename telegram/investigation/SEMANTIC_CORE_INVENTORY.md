# SEMANTIC_CORE_INVENTORY

**Document ID:** CASE001-002

**Title:** Semantic Core Inventory

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Investigation №001

---

# Purpose

This document classifies every concept identified in the Telegram Publishing Domain into three independent existence groups without evaluation or explanation.

---

# Group A — Exists independently of SvitloSk

These concepts exist in the real domain regardless of whether SvitloSk exists.

| # | Concept | Description |
|---|---------|-------------|
| A-01 | Starokostiantyniv Community | Territorial community served by the project |
| A-02 | Administrative Centre | Principal territorial unit of the Community |
| A-03 | Starosta District | Territorial subdivision of the Community |
| A-04 | Settlement | Populated place belonging to a Territory |
| A-05 | Street | Road name within an address |
| A-06 | Address | Geographical location published by official Data Source |
| A-07 | Distribution System Operator | Official organization operating electricity distribution network |
| A-08 | Planned Power Outage | Officially announced scheduled interruption of electricity supply |
| A-09 | Emergency Power Outage | Unplanned interruption published by official Data Source |
| A-10 | Outage Schedule | Official schedule of planned electricity availability |
| A-11 | Queue | Official electricity distribution queue |
| A-12 | Subqueue | Subdivision of an official Queue |
| A-13 | Electricity Availability | Current availability status of electricity supply |
| A-14 | Availability Window | Continuous time interval during which electricity is available |
| A-15 | Outage Window | Continuous time interval during which electricity is unavailable |
| A-16 | Open Data | Officially published publicly accessible information |
| A-17 | Data Source | Official organization publishing Open Data |
| A-18 | Residents | Persons using SvitloSk to obtain information |
| A-19 | Information Consumers | Any person or system receiving Publications |
| A-20 | Telegram | External communication platform |
| A-21 | Community (territorial) | Territorial community served by the project |
| A-22 | Powered state | Territory NOT currently experiencing outage |
| A-23 | Outage state | Territory currently experiencing outage |

---

# Group B — Exists only because the business process exists

These concepts exist only because SvitloSk decided to perform this specific business process.

| # | Concept | Description |
|---|---------|-------------|
| B-01 | Journal | Continuous informational publication of SvitloSk |
| B-02 | Issue | One editorial edition for a single calendar day |
| B-03 | Publication | One independent publication belonging to an Issue |
| B-04 | Telegram Channel | Communication medium for delivering Publications |
| B-05 | Publication Channel | Communication medium for distribution |
| B-06 | Publication Package | Complete collection of Publications for one Reporting Period |
| B-07 | Editorial Policy | Normative rules for publication presentation |
| B-08 | Reporting Period | Time interval for which Publications are generated |
| B-09 | Archive | Preserved historical Publications |
| B-10 | Territory (publication unit) | Publication unit representing Administrative Centre or Starosta District |
| B-11 | Publisher Role | Logical responsibility for preparing and distributing Publications |
| B-12 | Canonical Templates | Definitive publication templates A, B, C, D |
| B-13 | Source Fidelity | Principle that rendering shall not modify official information |
| B-14 | Traceability | Ability to identify origin of every Publication |
| B-15 | Reliability | Guarantee of non-duplication and order preservation |
| B-16 | Editorial Principles | Foundational editorial principles |
| B-17 | Territory Presentation | Rules for territory display in Publications |
| B-18 | Time Format | Rules for time interval display |
| B-19 | Settlement Formatting | Rules for settlement name display |
| B-20 | Address Formatting | Rules for address display |
| B-21 | Branding | Rules for SvitloSk identity in Publications |
| B-22 | Publication Grammar | Hierarchical structure rules for Publications |
| B-23 | Territory Header | Beginning of Publication with territory name |
| B-24 | Publication Sections | Content sections: Planned and Emergency Outages |
| B-25 | Graphic Clarity | Principle of visual simplicity |
| B-26 | Graphic Branding | Branding elements in graphic Publications |
| B-27 | Graphic Accessibility | Readability across display types |
| B-28 | Graphic Color | Color semantics for state representation |
| B-29 | Daily Publication Cycle | Daily operational cycle of the Telegram Journal |
| B-30 | Formatting Rules | Rules for text presentation in Publications |

---

# Group C — Exists only because software exists

These concepts exist only because software components exist to implement them.

| # | Concept | Description |
|---|---------|-------------|
| C-01 | Publication Engine | Architectural Component implementing Publisher Role |
| C-02 | Parser | Architectural Component retrieving Open Data |
| C-03 | Data Storage | Architectural Component preserving data |
| C-04 | Schedule Generator | Architectural Component producing schedules |
| C-05 | Graphic Generator | Architectural Component producing graphics |
| C-06 | Telegram Publisher | Telegram-specific implementation of Publisher Role |
| C-07 | Publication Lifecycle States | Generated, Published, Updated, Archived, Removed |
| C-08 | Telegram Message ID | Platform identifier for published messages |
| C-09 | Rate Limiting | Telegram API frequency constraints |
| C-10 | Rendering Pipeline | Sequence of processing stages |
| C-11 | Deterministic Rendering | Same input produces identical output |
| C-12 | Non-destructive Channel | Modify only owned Publications |
| C-13 | Non-destructive Update | Modify instead of replace |
| C-14 | Publication Ownership | Model determining component ownership |
| C-15 | Publication Session | One execution producing complete Journal state |
| C-16 | Publication Windows | Time windows for engine operation |
| C-17 | Canonical Equality | Byte-for-byte comparison of identical datasets |
| C-18 | Error Handling | Failure recovery rules |
| C-19 | Validation Rules | Structural requirement verification |
| C-20 | Long Publication Split | Division between complete Settlement blocks |
| C-21 | HTML Rendering Rules | Allowed HTML tags and escaping |
| C-22 | Stable Output Rule | No cosmetic formatting changes |
| C-23 | Empty Block Rule | No empty sections generated |
| C-24 | Editing Rules | Post-publication correction rules |
| C-25 | Graphic Automation | Automatic generation from normalized data |
| C-26 | Graphic Format | PNG and SVG support only |
| C-27 | Graphic Validation | Pre-publication verification |
| C-28 | Graphic Timeline | Proportional 24-hour representation |
| C-29 | Repository Authority | Repository as single source of truth |
| C-30 | Repository State | Current publication state in Repository |
| C-31 | Publication Lifecycle | Complete lifecycle from creation to archival |
| C-32 | Graphic Publication | Visual representation of outage data |
| C-33 | Tomorrow Schedule Graphic | Primary public information card |
| C-34 | Emergency Information Card | Urgent information graphic |
| C-35 | Statistics Card | Generated statistics graphic |
| C-36 | Service Graphic | Internal service messages |

---

# End of Document
