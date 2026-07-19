# GLOSSARY

Status: Stable (Стабільний)

Document ID: DOC-004

Document Class: Normative

Author: SvitloSk Project

---

# Purpose

This document establishes the canonical terminology of the SvitloSk Project Specification.

Every normative term used throughout the repository SHALL be defined in this document.

All normative documents SHALL use these definitions consistently.

This document is the single authoritative source for terminology used within the SvitloSk Specification Repository.

---

# Why this document matters

Consistent terminology is essential for maintaining a long-lived technical specification.

Using multiple terms for the same concept creates ambiguity, increases maintenance costs, complicates architectural evolution, and may result in inconsistent implementation.

The Glossary guarantees that every approved technical term has exactly one normative meaning.

Whenever terminology conflicts arise, this document SHALL prevail unless superseded by an approved Architecture Decision Record (ADR).

---

# Stable Terminology Principle

Every approved term SHALL have exactly one official definition.

One concept SHALL correspond to one canonical term.

One canonical term SHALL correspond to one concept.

Approved terminology SHALL remain stable throughout the repository.

Once approved, a term SHALL NOT change its meaning.

Changes to existing terminology SHALL be introduced only through the repository governance process.

Every normative document SHALL use the terminology established by this Glossary.

---

# Terminology Governance

The repository distinguishes between:

- terminology;
- architecture;
- implementation.

Terminology defines **what concepts mean**.

Architecture defines **how concepts interact**.

Implementation defines **how concepts are realized**.

A term SHALL NOT be redefined by:

- SSP specifications;
- TJS specifications;
- review reports;
- implementation documentation.

Only this Glossary MAY define normative terminology.

If a new concept is introduced into the repository:

1. the term SHALL first be approved in this Glossary;

2. architectural implications SHALL be documented through an Architecture Decision Record (ADR), when applicable;

3. only then MAY other documents use the new terminology.

---

# Interpretation Priority

When interpreting repository terminology, the following precedence SHALL apply:

1. Approved Architecture Decision Records (ADR);

2. This Glossary;

3. Core Documents;

4. Component Specifications (SSP);

5. Telegram Journal Specifications (TJS);

6. Audit documentation.

No lower-level document MAY redefine terminology established by a higher-level document.

---

# Architecture Decision Records

Architecture Decision Records (ADR) MAY introduce normative interpretation rules.

When an ADR affects terminology, this Glossary SHALL remain the canonical vocabulary.

The ADR SHALL define only the architectural interpretation of that terminology.

This separation preserves the Principle of One Subject — One Document.

Current normative ADR affecting repository terminology:

- ADR-001 — Component vs Role

---

# Scope

This Glossary applies to every normative document maintained within the SvitloSk Specification Repository, including but not limited to:

- Core Documents;
- Architecture Decision Records (ADR);
- System Specification documents (SSP);
- Telegram Journal Specifications (TJS);
- Audit Methodology;
- Repository Governance documentation.

Informative documents SHOULD also follow this terminology whenever possible.

---

# Glossary Structure

Terms are organized into the following categories:

1. Core Concepts

2. Information Model

3. Publication Model

4. Territorial Model

5. Electricity Domain

6. Users

7. Architecture Vocabulary

Each term SHALL belong to exactly one category.

---

# Naming Convention

Canonical terms SHALL:

- use singular form unless plurality is essential;
- use Title Case for defined concepts;
- avoid synonyms;
- remain stable over time;
- be understandable without implementation knowledge.

Abbreviations MAY be introduced only when explicitly defined.

Undefined abbreviations SHALL NOT appear in normative documentation.

---

# 1. Core Concepts

# 1. Core Concepts

## SvitloSk

A public information service that analyses, interprets, archives and distributes officially published information about electricity outages within the Starokostiantyniv Community.

SvitloSk does not create facts.

SvitloSk does not predict events.

SvitloSk interprets officially published information.

SvitloSk SHALL preserve the factual meaning of every official publication.

---

## Specification

The complete collection of normative and informative documentation maintained within the SvitloSk Specification Repository.

The Specification defines the project architecture, governance, terminology, component behaviour and documentation standards.

---

## Repository

The official GitHub repository containing the canonical SvitloSk Project Specification.

The Repository is the authoritative engineering source for every approved project document.

---

## Canonical Documentation

The English normative documentation representing the authoritative source of the SvitloSk Project Specification.

Official translations SHALL preserve the meaning of the Canonical Documentation.

Whenever inconsistencies arise, the Canonical Documentation SHALL prevail.

---

## Canonical Repository

The approved collection of normative project documentation.

Temporary materials, working notes, experimental drafts and intermediate audit artefacts SHALL NOT be considered part of the Canonical Repository.

---

## Core Documents

The highest-level normative documents governing the repository.

Core Documents define:

- repository governance;
- editorial standards;
- terminology;
- architecture;
- information model;
- territorial model;
- repository lifecycle.

Every lower-level document SHALL comply with the Core Documents.

---

## Architecture Decision Record (ADR)

A normative document recording an approved architectural decision affecting the long-term evolution of the project.

An ADR SHALL explain architectural intent.

An ADR SHALL NOT redefine repository terminology.

Architectural interpretation SHALL complement, but never replace, the definitions established by this Glossary.

---

## Architecture

The approved structural organization of the SvitloSk system.

Architecture defines:

- Components;
- relationships;
- responsibilities;
- data flow;
- dependency rules.

Architecture SHALL NOT redefine terminology.

---

## Normative Document

A document defining mandatory project requirements.

Normative Documents SHALL use RFC 2119 terminology where applicable.

Compliance with a Normative Document is mandatory.

---

## Informative Document

A document providing explanation, rationale, examples or supporting information.

Informative Documents SHALL NOT introduce mandatory requirements.

---

## Repository Governance

The collection of rules governing:

- document lifecycle;
- terminology;
- architecture;
- editorial quality;
- review methodology;
- approval procedures.

Repository Governance is established exclusively through the Core Documents and approved ADRs.

---

## Document Class

The normative classification assigned to every repository document.

Every document SHALL declare exactly one Document Class.

Current approved classes include:

- Normative
- Informative
- Audit Methodology
- Architecture Decision Record

Additional classes SHALL require repository-wide approval.

---

## Metadata

The standardized information describing a repository document.

Canonical metadata currently includes:

- Status
- Document ID (when applicable)
- Document Class
- Author

Metadata SHALL remain consistent across the entire repository.

---

## RFC

Request for Comments.

A document proposing modifications to the Project Specification.

Approved RFCs MAY result in updates to the Core Documents or Architecture Decision Records.

---

## Review

The structured process of evaluating repository documentation against the approved normative baseline.

Reviews SHALL follow the SSP Review Methodology.

Reviews SHALL assess compliance rather than redesign documents.

---

## Validation Review

A review performed after corrections have been implemented.

Its purpose is to verify that every approved finding has been resolved without introducing inconsistencies.

Validation Review SHALL NOT introduce new findings unless new evidence is discovered.

---

## Canonical Specification

A System Specification that has successfully completed:

- Assessment;
- Correction Phase;
- Validation Review;

and received the final verdict:

PASS.

A Canonical Specification MAY serve as a reference model for future specifications of the same class.

---

## Reference Model

An approved document used as an implementation and review example.

A Reference Model illustrates repository conventions but SHALL NOT override the Core Documents.

If a conflict exists, the Core Documents SHALL prevail.

# 2. Information Model

## Open Data

Officially published information that is publicly accessible without authentication or special permission.

Open Data SHALL remain the authoritative source of factual information.

SvitloSk SHALL NOT modify the factual meaning of Open Data.

---

## Data Source

The official organization publishing Open Data.

A Data Source is the authoritative origin of information consumed by SvitloSk.

Examples include:

- Distribution System Operator (DSO)
- Local government
- Official public registries

Only approved Data Sources MAY be used by the system.

---

## Distribution System Operator (DSO)

The official organization responsible for operating the electricity distribution network.

Within the SvitloSk Project, the DSO is the primary publisher of official electricity outage information.

The DSO SHALL be treated as the authoritative source for planned and emergency outage data.

---

## Data Retrieval

The process of obtaining Open Data from an approved Data Source.

Data Retrieval SHALL preserve the integrity of the original information.

The retrieval process SHALL NOT interpret, modify or enrich the received data.

---

## Parser

A software Component responsible for retrieving Open Data from approved Data Sources.

The Parser SHALL:

- retrieve data;
- validate data format;
- preserve data integrity.

The Parser SHALL NOT:

- interpret information;
- modify official data;
- generate publications;
- create business logic.

---

## Parsed Data

The direct machine-readable representation of information produced by the Parser.

Parsed Data SHALL correspond exactly to the retrieved Open Data.

Parsed Data SHALL remain traceable to its originating Data Source.

---

## Data Model

The structured internal representation of Parsed Data used by SvitloSk.

The Data Model SHALL be derived exclusively from Open Data.

The Data Model SHALL preserve semantic equivalence with the source information.

The Data Model SHALL NOT introduce additional facts.

---

## Interpretation

The process of transforming structured information into information understandable for residents.

Interpretation SHALL improve readability without changing factual meaning.

Interpretation SHALL NOT:

- create facts;
- predict events;
- modify official information;
- infer missing information.

Interpretation is a logical Role within the system architecture.

Its architectural realization is defined separately from this Glossary.

---

## Interpretation Result

The normalized information produced by the Interpretation process.

Interpretation Results SHALL remain:

- factually correct;
- traceable;
- reproducible.

Interpretation Results become input for Publication generation.

---

## Historical Archive

The persistent storage of historical Interpretation Results and Publications.

The Historical Archive SHALL preserve historical records without altering their original content.

Historical records SHALL remain traceable to their originating Open Data.

---

## Traceability

The ability to identify the origin of every piece of information managed by the system.

Every Interpretation Result and every Publication SHALL be traceable to:

- the originating Open Data;
- the originating Data Source;
- the corresponding processing cycle.

Traceability SHALL be preserved throughout the complete information lifecycle.

---

## Reporting Period

The time interval for which Publications are generated.

A Reporting Period MAY correspond to:

- a calendar day;
- an update cycle;
- another officially defined reporting interval.

The exact Reporting Period is defined by the corresponding specification.

---

## Processing Cycle

One complete execution of the information pipeline.

A Processing Cycle includes:

1. Data Retrieval

2. Parsing

3. Data Validation

4. Interpretation

5. Publication generation

6. Publication distribution

A Processing Cycle SHALL preserve information traceability from beginning to end.

# 3. Publication Model

## Publication

A public information message generated by the SvitloSk system for distribution through one or more supported communication channels.

Every Publication SHALL:

- be derived exclusively from an Interpretation Result;
- preserve the factual meaning of the originating Open Data;
- remain traceable to its originating Processing Cycle.

A Publication SHALL NOT introduce new facts.

---

## Publication Package

The complete collection of Publications generated during one Reporting Period.

A Publication Package MAY contain:

- planned outage publications;
- emergency outage publications;
- tomorrow publications;
- graphical publications;
- service announcements.

Every Publication Package SHALL remain internally consistent.

---

## Tomorrow Publication

A Publication containing officially announced planned outages for the following calendar day.

Tomorrow Publications SHALL:

- contain only officially published information;
- expire after the reporting period ends;
- be automatically replaced by current publications.

---

## Telegram Journal

The official public communication channel operated by the SvitloSk Project.

The Telegram Journal publishes Publications generated by the Publisher.

The Telegram Journal SHALL NOT create Publications independently.

---

## Editorial Policy

The normative rules governing:

- publication structure;
- formatting;
- wording;
- presentation.

Editorial Policy SHALL regulate presentation only.

Editorial Policy SHALL NOT modify factual content.

---

## Publication Channel

A communication medium through which Publications are distributed.

Examples include:

- Telegram Journal;
- future mobile application;
- future web interface.

A Publication MAY be distributed through multiple Publication Channels.

---

## Publisher

The logical Role responsible for preparing and distributing Publications.

The Publisher SHALL:

- receive Interpretation Results;
- generate Publications;
- distribute Publications through supported Publication Channels.

The Publisher SHALL NOT:

- retrieve Open Data;
- perform Parsing;
- reinterpret information;
- modify factual meaning.

The Publisher represents a logical responsibility within the system.

The architectural realization of this responsibility is performed by one or more Components.

---

## Publication Engine

A software Component implementing the Publisher Role.

Publication Engine is the canonical architectural Component responsible for publication generation and distribution.

The Publication Engine realizes the behaviour defined by the Publisher.

The Publication Engine SHALL implement the Publisher Role.

The Publication Engine SHALL NOT redefine the Publisher.

---

## Publisher Role

The logical responsibility of creating and distributing Publications.

A Publisher Role MAY be implemented by different software Components.

Within the current SvitloSk architecture, the Publisher Role is implemented by the Publication Engine.

---

## Publication Pipeline

The sequence of processing stages transforming Interpretation Results into Publications.

The Publication Pipeline begins after Interpretation has completed.

Typical stages include:

1. Publication preparation;

2. Publication rendering;

3. Publication packaging;

4. Publication distribution.

The exact implementation is architecture-dependent.

---

## Rendering

The process of converting an Interpretation Result into a presentation-ready Publication.

Rendering MAY include:

- formatting;
- template application;
- image generation;
- message composition.

Rendering SHALL NOT alter factual content.

---

## Distribution

The process of delivering Publications to one or more Publication Channels.

Distribution SHALL preserve the generated Publication without semantic modification.

Distribution SHALL remain traceable.

---

## Publication Lifecycle

The complete lifecycle of a Publication.

The lifecycle consists of:

1. Interpretation Result;

2. Rendering;

3. Publication generation;

4. Distribution;

5. Archival;

6. Expiration (where applicable).

Every Publication SHALL follow the defined Publication Lifecycle.

# 4. Territorial Model

## Community

The territorial community served by SvitloSk.

The Community represents the complete territorial scope of the project.

Its canonical structure is defined in:

- TERRITORIAL_MODEL.md

---

## Territory

A publication unit representing either:

- the Administrative Centre;
- one Starosta District.

A Territory is a logical publication entity rather than an administrative classification.

Territorial relationships SHALL follow TERRITORIAL_MODEL.md.

---

## Administrative Centre

The principal territorial unit of the Community.

The Administrative Centre represents the primary settlement within the Community.

Its administrative responsibilities are outside the scope of this Glossary.

---

## Starosta District (SO)

A territorial subdivision of the Community.

The abbreviation **SO** is normative.

Every Starosta District SHALL belong to exactly one Community.

The internal composition of a Starosta District is defined in TERRITORIAL_MODEL.md.

---

## Settlement

A populated place belonging to the Community.

Every Settlement SHALL belong to exactly one Territory.

Settlement relationships SHALL remain consistent with TERRITORIAL_MODEL.md.

---

## Address

A geographical location published by the official Data Source.

Addresses SHALL be treated exactly as officially published.

SvitloSk SHALL NOT normalize, rename or reinterpret official addresses.

---

## Territorial Coverage

The collection of Territories served by the project.

Territorial Coverage SHALL remain explicitly defined.

Expansion of Territorial Coverage SHALL require repository-wide approval.

# 5. Electricity Domain

## Planned Power Outage

An officially announced scheduled interruption of electricity supply.

Planned Power Outages originate exclusively from an approved Data Source.

---

## Emergency Power Outage

An unplanned interruption of electricity supply published by the official Data Source.

Emergency Power Outages SHALL be treated as authoritative immediately after publication.

---

## Electricity Availability

The current availability status of electricity supply.

Electricity Availability is derived from official information.

It SHALL NOT be inferred.

---

## Queue

An official electricity distribution queue published by the Distribution System Operator.

Queue identifiers SHALL preserve their official representation.

---

## Subqueue

A subdivision of an official Queue.

Subqueue identifiers SHALL preserve their official representation.

The current SvitloSk implementation supports twelve Subqueues.

Support for additional Subqueues SHALL require specification updates.

---

## Outage Schedule

The official schedule of planned electricity availability published by the Distribution System Operator.

The Outage Schedule SHALL remain the authoritative planning source.

---

## Outage Timeline

A visual representation of electricity availability during one Reporting Period.

The Outage Timeline is an informational representation only.

It SHALL preserve the meaning of the originating Outage Schedule.

---

## Availability Window

A continuous time interval during which electricity is expected to be available.

Availability Windows SHALL be derived exclusively from official schedules.

---

## Outage Window

A continuous time interval during which electricity is expected to be unavailable.

Outage Windows SHALL be derived exclusively from official schedules.

---

# 6. Users

## Resident

A person using SvitloSk to obtain official information about electricity outages within the Community.

Residents are the primary beneficiaries of the project.

---

## Information Consumer

Any person or software system receiving Publications generated by SvitloSk.

An Information Consumer MAY use any supported Publication Channel.

---

## Stakeholder

Any organization or individual having legitimate interest in the project.

Stakeholders MAY include:

- residents;
- local authorities;
- infrastructure operators;
- project maintainers.

# 7. Architecture Vocabulary

This section establishes the canonical distinction between architectural Components and logical Roles.

The rules defined in this section SHALL be interpreted together with:

- ADR-001 — Component vs Role

Whenever ambiguity exists regarding architectural naming, this section SHALL prevail.

---

## Component

A Component is a concrete architectural building block of the system.

A Component represents an implementation unit.

Components are defined by the approved system architecture.

A Component SHALL:

- have a stable architectural identity;
- have clearly defined responsibilities;
- participate in the system architecture;
- expose well-defined interfaces where applicable.

A Component MAY implement one or more Roles.

A Component SHALL NOT be considered a business concept.

---

## Role

A Role is a logical responsibility performed within the system.

A Role describes **what is performed**, not **how it is implemented**.

A Role is independent of implementation technology.

A Role MAY be implemented by:

- one Component;
- multiple Components;
- different Components in future architectural revisions.

A Role SHALL remain implementation-independent.

---

## Component Name

The official architectural name assigned to a Component.

Component Names SHALL remain stable across repository documentation.

Component Names SHALL be used when:

- describing architecture;
- describing system structure;
- identifying implementation units;
- defining dependencies between Components.

Component Names SHALL NOT be replaced by Role Names.

---

## Role Name

The official logical name assigned to a Role.

Role Names SHALL be used when describing:

- behaviour;
- responsibilities;
- business logic;
- processing activities.

Role Names SHALL NOT replace Component Names inside architectural descriptions.

---

## Component Metadata

The metadata field:

```text
Component:
```

declares the architectural Component described by an SSP document.

The value of the Component field SHALL always contain a Component Name.

The Component field SHALL NEVER contain a Role Name.

---

## Publication Engine

Publication Engine is the canonical architectural Component responsible for publication generation and distribution.

Publication Engine is an implementation unit.

Publication Engine implements the Publisher Role.

The architectural identity of Publication Engine SHALL remain stable throughout the repository.

---

## Publisher

Publisher is the canonical logical Role responsible for:

- preparing Publications;
- generating Publications;
- distributing Publications.

Publisher is NOT an architectural Component.

Publisher SHALL describe responsibility only.

---

## Parser

Parser is the canonical architectural Component responsible for retrieving Open Data.

Parser implements the Data Retrieval Role.

Parser SHALL be treated as a Component throughout repository documentation.

---

## Interpreter

Interpreter is the canonical logical Role responsible for transforming structured information into information understandable for residents.

Interpreter describes behaviour.

Interpreter SHALL NOT be interpreted as an architectural Component unless explicitly defined by future architecture.

---

## Component vs Role

A Component and a Role SHALL NOT be considered interchangeable.

The same concept MAY be expressed through:

Component → implementation

Role → responsibility

Example:

Role:

Publisher

↓

implemented by

↓

Component:

Publication Engine

This relationship SHALL remain valid unless superseded by a future approved ADR.

---

## Naming Rule

When writing repository documentation:

Architectural documents SHALL use Component Names.

Behavioural descriptions SHALL use Role Names.

Editorial wording SHALL preserve this distinction.

---

## SSP Rule

Every SSP specification SHALL declare:

```text
Component:
```

using the canonical Component Name.

The body of the specification MAY refer to Roles when describing responsibilities.

Example:

Metadata

```text
Component:
Publication Engine
```

Body

```text
The Publication Engine implements the Publisher Role.
```

This is the preferred canonical formulation.

---

## Review Rule

During repository reviews:

Using a Role instead of a Component inside metadata SHALL be treated as a repository inconsistency.

Using a Component instead of a Role inside behavioural descriptions SHOULD be evaluated according to context.

Reviewers SHALL distinguish between architectural naming and logical naming before classifying findings.

The existence of both names SHALL NOT be interpreted as contradictory when they describe different abstraction levels.

---

## Architectural Consistency

Different abstraction levels SHALL NOT be treated as inconsistencies.

The reviewer SHALL verify:

- whether the correct abstraction level is used;
- whether terminology remains consistent;
- whether Component and Role names preserve their defined meanings.

Only explicit conflicts SHALL be classified as findings.

# Repository Rule

No normative document SHALL define terminology independently.

Every normative term SHALL first be introduced into this Glossary.

If architectural interpretation is required, the corresponding Architecture Decision Record (ADR) SHALL be created or updated.

Lower-level documents SHALL reference existing terminology rather than redefine it.

Repository terminology SHALL evolve only through the approved repository governance process.

---

# Repository Consistency Rule

All repository documentation SHALL use terminology consistently.

Every defined term SHALL preserve:

- its meaning;
- its abstraction level;
- its architectural interpretation.

Documents SHALL distinguish between:

- terminology;
- architecture;
- implementation.

Repository-wide terminology inconsistencies SHOULD be resolved before introducing new documentation.

---

# Reviewer Guidance

Reviewers SHALL evaluate terminology using this Glossary before classifying findings.

The reviewer SHALL distinguish between:

- missing terminology;
- incorrect terminology;
- architectural naming;
- logical naming.

Different abstraction levels SHALL NOT be interpreted as contradictions.

When uncertainty exists, the reviewer SHALL consult the applicable Architecture Decision Record (ADR).

---

# Change Management

New terminology SHALL be introduced only when:

- an existing term cannot accurately describe the concept; and
- repository-wide approval has been obtained.

Existing terminology SHALL NOT be replaced by synonyms.

Deprecating an approved term SHALL require:

1. an approved Architecture Decision Record (ADR), where applicable;

2. an update to this Glossary;

3. repository-wide consistency verification.

---

# Glossary Maintenance

The Glossary SHALL be reviewed whenever:

- new Core Documents are introduced;
- a new ADR affects terminology;
- repository-wide terminology changes are approved.

The Glossary SHOULD remain the smallest possible complete vocabulary of the project.

Duplicate definitions SHALL NOT exist.

---

# References

## Depends on

- CHARTER.md
- PROJECT_PRINCIPLES.md
- DOCUMENT_INDEX.md
- EDITORIAL_STANDARDS.md
- TERRITORIAL_MODEL.md
- ADR-001-Component-vs-Role.md

## Referenced by

This Glossary is referenced by every normative repository document, including:

- ARCHITECTURE.md
- DATA_MODEL.md
- SYSTEM_OVERVIEW.md
- RFC_PROCESS.md
- all SSP specifications
- all TJS specifications
- SSP Review Methodology
- Repository Governance documents

---

**End of Document**