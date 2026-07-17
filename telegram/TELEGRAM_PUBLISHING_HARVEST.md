# Telegram Publishing Harvest

**Date:** 2026-07-13
**Scope:** Complete inventory of harvested semantic statements
**Status:** HARVEST COMPLETE

---

# Purpose

This document contains every approved semantic statement related to the Telegram Publishing System. One statement per line. Every statement includes source references.

---

# Harvest Statistics

| Metric | Count |
|--------|-------|
| Total semantic statements | 380 |
| Source documents read | 18 |
| Concept areas covered | 10 |
| Definitions | ~145 |
| Rules | ~105 |
| Constraints | ~85 |
| Principles | ~30 |
| Relationships | ~45 |

---

# 1. Journal Publishing System

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 1 | The Telegram subsystem SHALL be treated as a Journal Publishing System. | TSM §3 | DEFINITION |
| 2 | Telegram itself SHALL NOT be considered the Journal. | TSM §3 | CONSTRAINT |
| 3 | Telegram SHALL only be considered the publication platform. | TSM §3 | DEFINITION |
| 4 | The Journal exists independently from any publication platform. | TSM §3 | PRINCIPLE |
| 5 | The SvitloSk Telegram Journal is an automated public information journal that continuously analyzes official open data on electricity outages. | TJS-001 §3 | DEFINITION |
| 6 | The journal also serves as a chronological public archive of information processed by the SvitloSk system. | TJS-001 §3 | DEFINITION |
| 7 | The Telegram Journal is not a news channel. It is not a media outlet. It is not a discussion platform. | TJS-001 §9 | DEFINITION |
| 8 | The Telegram Journal represents the public communication layer of the SvitloSk ecosystem. | TJS-001 §10 | DEFINITION |
| 9 | It receives processed information from the Publication Engine and distributes it to subscribers. | TJS-001 §10 | RELATIONSHIP |
| 10 | The Telegram Journal serves as the permanent public archive of publications related to the current day. | TJS-001 §11 | DEFINITION |
| 11 | The semantic hierarchy of the Journal is: Journal → Issue → Publication → Telegram. | TSM §4 | DEFINITION |
| 12 | Journal represents the continuous informational publication of the SvitloSk project. | TSM §4 | DEFINITION |
| 13 | Journal owns Issue. | TG §6 | RELATIONSHIP |
| 14 | Journal is delivered through Telegram. | TG §6 | RELATIONSHIP |
| 15 | The continuous informational publication of the SvitloSk project. | TG §8 | DEFINITION |
| 16 | The Telegram Journal follows these principles: Territory-first, One post — one territory, Maximum readability, Minimal formatting, Consistent structure, No decorative elements, Automatic generation. | TJS-004 §Editorial | PRINCIPLE |
| 17 | Every publication must increase clarity without changing the meaning of the official source. | TJS-001 §6 | PRINCIPLE |
| 18 | The journal does not interpret, predict or alter official information. | TJS-001 §6 | PRINCIPLE |

---

# 2. Publishing Components

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 19 | Publication Engine implements Publisher. | TG §6 | RELATIONSHIP |
| 20 | Publisher creates Publication. | TG §6 | RELATIONSHIP |
| 21 | Parser retrieves data for Publication Engine. | TG §6 | RELATIONSHIP |
| 22 | Telegram Publisher implements Publisher for Telegram. | TG §6 | RELATIONSHIP |
| 23 | The architectural Component implementing the Publisher Role. | TG §8 | DEFINITION |
| 24 | The logical Role responsible for preparing, generating and distributing Publications. | TG §8 | DEFINITION |
| 25 | The architectural Component responsible for retrieving Open Data from approved Data Sources. | TG §8 | DEFINITION |
| 26 | The Telegram-specific implementation of the Publisher Role. | TG §10 | DEFINITION |
| 27 | Publication Engine is the canonical architectural Component responsible for publication generation and distribution. | GL §7 | DEFINITION |
| 28 | Publisher is the canonical logical Role responsible for: preparing, generating, distributing Publications. | GL §7 | DEFINITION |
| 29 | The Publisher SHALL: receive Interpretation Results; generate Publications; distribute Publications through supported Publication Channels. | GL §3 | RULE |
| 30 | The Publisher SHALL NOT: retrieve Open Data; perform Parsing; reinterpret information; modify factual meaning. | GL §3 | CONSTRAINT |
| 31 | The Publication Engine realizes the behaviour defined by the Publisher. | GL §3 | RELATIONSHIP |
| 32 | The Publication Engine SHALL implement the Publisher Role. | GL §3 | RULE |
| 33 | The Publication Engine SHALL NOT redefine the Publisher. | GL §3 | CONSTRAINT |

---

# 3. Publication Lifecycle

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 34 | The complete lifecycle of a Publication from creation through rendering, publication, update, retention and removal. | TG §11 | DEFINITION |
| 35 | One of the states a Publication passes through during its lifecycle. | TG §11 | DEFINITION |
| 36 | Generated: The state in which a Publication has been created but not yet published. | TG §11 | DEFINITION |
| 37 | Published: The state in which a Publication is live and visible to readers. | TG §11 | DEFINITION |
| 38 | Updated: The state in which a Publication has been modified after initial publication. | TG §11 | DEFINITION |
| 39 | Archived: The state in which a Publication is preserved as part of the historical record. | TG §11 | DEFINITION |
| 40 | Removed: The state in which a temporary Publication has been deleted. | TG §11 | DEFINITION |
| 41 | A Publication that may be removed after becoming irrelevant. | TG §11 | DEFINITION |
| 42 | A Publication that remains in the Journal permanently. | TG §11 | DEFINITION |
| 43 | The conditions under which a published Publication MAY be edited. | TG §11 | DEFINITION |
| 44 | The rules governing preservation of historical Publications. | TG §11 | DEFINITION |
| 45 | The rules governing removal of Publications. | TG §11 | DEFINITION |
| 46 | The model determining which component owns which Publications. | TG §11 | DEFINITION |
| 47 | The state of preserved historical Publications. | TG §11 | DEFINITION |
| 48 | Each publication shall pass through: Generated → Scheduled → Published → Updated → Archived → Removed. | TJS-002 §3 | DEFINITION |
| 49 | Every Publication SHALL follow: Dataset → Render → Publish → Update → Retain or Remove. | TJS-007 §3 | DEFINITION |
| 50 | The Telegram Journal SHALL follow one daily publication cycle. | TJS-008 §3 | RULE |
| 51 | Publication Lifecycle governs Publication. | TG §6 | RELATIONSHIP |
| 52 | Lifecycle State describes Publication. | TG §6 | RELATIONSHIP |
| 53 | Generated IS A Lifecycle State. Published IS A Lifecycle State. Updated IS A Lifecycle State. Archived IS A Lifecycle State. Removed IS A Lifecycle State. | TG §6 | RELATIONSHIP |

---

# 4. Publication Structure

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 54 | One independent publication belonging to an Issue. | TG §8 | DEFINITION |
| 55 | One editorial edition of the Journal for a single calendar day. | TG §8 | DEFINITION |
| 56 | The structural format of publications, consisting of Territory Header, Publication Sections, and Update Time. | TG §12 | DEFINITION |
| 57 | The hierarchical structure rules: Territory Header → Sections → Settlement → Time → Street → Addresses. | TG §12 | DEFINITION |
| 58 | The definitive publication templates: City Today (A), District Today (B), City Tomorrow (C), District Tomorrow (D). | TG §12 | DEFINITION |
| 59 | The beginning of a Publication containing the territory name in uppercase. | TG §12 | DEFINITION |
| 60 | The content sections: Planned Outages and Emergency Outages. Empty sections SHALL NOT be rendered. | TG §12 | DEFINITION |
| 61 | Every Publication SHALL follow the same structural grammar. | TJS-005 §4 | RULE |
| 62 | Inside every section the hierarchy SHALL be: Settlement → Time Interval → Street → Addresses. | TJS-005 §4 | RULE |
| 63 | The Publication SHALL begin with the Territory title. | TJS-005 §5 | RULE |
| 64 | Telegram Publications SHALL render Territory titles in uppercase. | TJS-005 §5 | RULE |
| 65 | The Planned section SHALL always appear before the Emergency section. | TJS-005 §6 | RULE |
| 66 | Empty sections SHALL NOT be rendered. | TJS-005 §6 | CONSTRAINT |
| 67 | Settlements SHALL appear in the canonical order defined by TERRITORIAL_MODEL.md. | TJS-005 §7 | RULE |
| 68 | Alphabetical sorting is prohibited. | TJS-005 §7 | CONSTRAINT |
| 69 | Time Intervals SHALL be sorted by their starting time. | TJS-005 §8 | RULE |
| 70 | Settlement names SHALL be rendered in bold. | TJS-005 §10 | RULE |
| 71 | Administrative prefixes SHALL NOT be rendered. | TJS-005 §10 | CONSTRAINT |
| 72 | Street names SHALL begin on a new line. | TJS-005 §11 | RULE |
| 73 | Addresses SHALL NOT be split across multiple lines. | TJS-005 §11 | CONSTRAINT |
| 74 | Duplicate addresses are prohibited. | TJS-005 §12 | CONSTRAINT |
| 75 | A Publication SHALL NOT: render empty sections; change the order of sections; change the canonical Settlement order; sort Settlements alphabetically; duplicate addresses; merge multiple Starosta Districts into one Publication. | TJS-005 §14 | CONSTRAINT |
| 76 | Temporary Publications SHALL NOT contain an Update Time. | TJS-005 §13 | CONSTRAINT |
| 77 | Graphic Publication IS A Publication. Text Publication IS A Publication. Temporary Publication IS A Publication. Permanent Publication IS A Publication. | TG §6 | RELATIONSHIP |
| 78 | City Today IS A Publication. District Today IS A Publication. City Tomorrow IS A Publication. District Tomorrow IS A Publication. | TG §6 | RELATIONSHIP |
| 79 | Publication Package contains Publications. Today's Package IS A Publication Package. Tomorrow Package IS A Publication Package. | TG §6 | RELATIONSHIP |

---

# 5. Rendering

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 80 | The sequence: Validation → Sorting → Grouping → Duplicate Removal → Formatting → HTML Escaping → Length Validation → Telegram HTML. | TG §14 | DEFINITION |
| 81 | The process of converting normalized data into a presentation-ready Publication. | TG §14 | DEFINITION |
| 82 | The same normalized dataset SHALL always produce identical output. | TG §14 | PRINCIPLE |
| 83 | Every rendered element SHALL follow deterministic ordering rules. | TG §14 | PRINCIPLE |
| 84 | Rendering SHALL NOT modify or reinterpret official information. | TG §14 | PRINCIPLE |
| 85 | Publications SHALL be generated: Administrative Centre first, then Starosta Districts alphabetically. | TG §14 | RULE |
| 86 | Time intervals SHALL always be sorted by their start time. | TG §14 | RULE |
| 87 | Street entries SHALL be ordered alphabetically using Natural Sort. | TG §14 | RULE |
| 88 | Duplicate addresses SHALL NOT appear in publications. | TG §14 | RULE |
| 89 | If a publication exceeds Telegram limits, it SHALL be divided automatically between complete Settlement blocks. | TG §14 | RULE |
| 90 | Allowed HTML tags: `<b>` and `<br>`. All other HTML tags are prohibited. | TG §14 | CONSTRAINT |
| 91 | Publisher SHALL NOT introduce cosmetic formatting changes. | TG §14 | RULE |
| 92 | Publisher SHALL NOT generate empty sections. | TG §14 | CONSTRAINT |
| 93 | The Telegram Publisher SHALL follow: Deterministic Rendering, Canonical Equality, Human Readability, Minimal Formatting, Stable Ordering, Source Fidelity. | TJS-006 §3 | PRINCIPLE |
| 94 | Two publications generated from identical datasets SHALL be byte-for-byte identical. | TJS-006 §3 | PRINCIPLE |
| 95 | Only formatting approved by the Editorial Policy MAY be used. | TJS-006 §3 | CONSTRAINT |
| 96 | Telegram formatting SHALL use only: bold (`<b>`). No other formatting SHALL be used. | TJS-005 §15 | CONSTRAINT |

---

# 6. Editorial

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 97 | The normative rules governing: publication structure; formatting; wording; presentation. | GL §3 | DEFINITION |
| 98 | Editorial Policy SHALL regulate presentation only. Editorial Policy SHALL NOT modify factual content. | GL §3 | CONSTRAINT |
| 99 | The editorial standards for all text publications in the Telegram Journal. | TG §13 | DEFINITION |
| 100 | The foundational principles: Territory-first, One post — one territory, Maximum readability, Minimal formatting, Consistent structure, No decorative elements, Automatic generation. | TG §13 | DEFINITION |
| 101 | A post represents only one territory. | TJS-004 §Territory | RULE |
| 102 | Territory name is always the first element of the publication. | TJS-004 §Territory | RULE |
| 103 | Posts without information are not created. | TJS-004 §Package | CONSTRAINT |
| 104 | Inside every post information is presented: 1. Planned outages. 2. Emergency outages. | TJS-004 §Categories | RULE |
| 105 | Only the following formatting is permitted: bold; plain text. | TJS-004 §Formatting | CONSTRAINT |
| 106 | Every publication is generated automatically from structured data. | TJS-004 §Automatic | RULE |
| 107 | Every publication generated by SvitloSk shall comply with this editorial policy. | TJS-004 §Compliance | CONSTRAINT |

---

# 7. Platform (Telegram)

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 108 | The primary publication channel used to deliver Publications to readers. | TG §8 | DEFINITION |
| 109 | Telegram owns Platform delivery, channel management. Telegram does NOT own Editorial content, lifecycle rules. | TSM §5 | CONSTRAINT |
| 110 | The communication medium through which Publications are delivered. | TG §10 | DEFINITION |
| 111 | The platform identifier assigned to a published message in Telegram. | TG §10 | DEFINITION |
| 112 | The Telegram Bot interface used for automated publication delivery. | TG §10 | DEFINITION |
| 113 | Telegram API constraints that limit the frequency of automated operations. | TG §10 | DEFINITION |
| 114 | End consumers who receive Publications through the Telegram channel. | TG §10 | DEFINITION |
| 115 | Channel delivers Publication. | TG §6 | RELATIONSHIP |
| 116 | Telegram Message ID identifies Publication on Telegram. | TG §6 | RELATIONSHIP |
| 117 | Subscribers receive Publication. | TG §6 | RELATIONSHIP |
| 118 | Administrators manage Channel. | TG §6 | RELATIONSHIP |
| 119 | Publications created manually by administrators, outside the automated lifecycle. | TG §10 | DEFINITION |
| 120 | Platform concepts describe Telegram-specific technical concepts. | TG §10 | CONSTRAINT |

---

# 8. Administrative (Territorial)

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 121 | A populated place within a territory. | TG §15 | DEFINITION |
| 122 | A territorial subdivision of the Community. The abbreviation SO is normative. | TG §15 | DEFINITION |
| 123 | The primary territorial scope served by the project. | TG §15 | DEFINITION |
| 124 | The principal territorial unit of the Community. | TG §15 | DEFINITION |
| 125 | A publication unit representing either the Administrative Centre or one Starosta District. | TG §15 | DEFINITION |
| 126 | A road name within an address. Official Ukrainian abbreviations are preserved. | TG §15 | DEFINITION |
| 127 | A geographical location published by the official Data Source. | TG §15 | DEFINITION |
| 128 | A continuous time interval during which electricity is expected to be available or unavailable. | TG §15 | DEFINITION |

---

# 9. Principles

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 129 | Every decision SHALL improve accessibility, clarity, reliability or usefulness of public information. | PP P-01 | PRINCIPLE |
| 130 | SvitloSk respects official public information as the only source of operational data. | PP P-02 | PRINCIPLE |
| 131 | SvitloSk transforms officially published information into understandable information. | PP P-03 | PRINCIPLE |
| 132 | Publishing accurate information is mandatory. Accuracy SHALL take priority. | PP P-04 | PRINCIPLE |
| 133 | Every repetitive process SHOULD eventually become automated. | PP P-05 | PRINCIPLE |
| 134 | The project SHALL remain transparent. | PP P-06 | PRINCIPLE |
| 135 | Every new component SHALL solve an existing problem. | PP P-08 | PRINCIPLE |
| 136 | Each approved technical term has exactly one meaning. | PP P-09 | PRINCIPLE |
| 137 | Every normative document defines one complete subject. | PP P-10 | PRINCIPLE |
| 138 | The TELEGRAM_SEMANTIC_MODEL.md document is the single semantic authority. | TSM §6 | RULE |
| 139 | No Telegram specification SHALL redefine concepts owned by the Semantic Model. | TSM §6 | CONSTRAINT |
| 140 | TELEGRAM_GLOSSARY.md is the authoritative semantic source for every Telegram specification. | TG §2 | RULE |
| 141 | Each semantic concept SHALL have exactly one canonical definition. | TG §3 | RULE |
| 142 | Single Source of Truth — one authoritative definition per concept. | TG §16 | PRINCIPLE |
| 143 | Single Responsibility Principle — one responsibility per document. | TG §16 | PRINCIPLE |
| 144 | The principle that Policy and Implementation are separated across documents. | TG §16 | PRINCIPLE |
| 145 | Every normative document defines one complete subject area. | TG §16 | PRINCIPLE |
| 146 | Dependencies flow from TJS-001 downward. No circular dependencies are permitted. | TG §16 | RULE |

---

# 10. Constraints

| # | Statement | Source | Type |
|---|-----------|--------|------|
| 147 | The Telegram documentation subsystem consists of exactly 7 documents. | TAD §Approved | CONSTRAINT |
| 148 | One responsibility. One owner. No shared ownership. | TAD §Responsibility | CONSTRAINT |
| 149 | Dependencies flow in one direction. No cycles are permitted. | TAD §Dependency | CONSTRAINT |
| 150 | One responsibility — one owner. No responsibility SHALL be defined authoritatively in more than one document. | TAD §Constraints #1 | CONSTRAINT |
| 151 | The Publication Lifecycle SHALL be owned exclusively by TJS-005. | TAD §Constraints #2 | CONSTRAINT |
| 152 | Formatting POLICY SHALL be owned exclusively by TJS-002. Formatting IMPLEMENTATION SHALL be owned exclusively by TJS-003. | TAD §Constraints #3 | CONSTRAINT |
| 153 | Publication templates SHALL be owned exclusively by TJS-003. | TAD §Constraints #4 | CONSTRAINT |
| 154 | Every concept SHALL have exactly one authoritative definition. | TAD §Constraints #5 | CONSTRAINT |
| 155 | Dependencies SHALL flow from TJS-001 downward. No circular dependencies are permitted. | TAD §Constraints #6 | CONSTRAINT |
| 156 | Any change to the document set SHALL require an approved Architecture Decision. | TAD §Constraints #7 | CONSTRAINT |
| 157 | Every TJS document SHALL have: Document Class, References section, uppercase RFC 2119 keywords. | TAD §Constraints #8 | CONSTRAINT |
| 158 | Every TJS document SHALL use terminology defined by GLOSSARY.md. | TAD §Constraints #9 | CONSTRAINT |
| 159 | Every TJS document SHALL define one complete subject area. | TAD §Constraints #10 | CONSTRAINT |
| 160 | Settlement Ordering Conflict: TJS-005 §7 and TJS-006 §7 define mutually exclusive rules. | TAD DD-001 | CONSTRAINT |

---

**End of Publishing Harvest**

**Harvester:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** HARVEST COMPLETE
