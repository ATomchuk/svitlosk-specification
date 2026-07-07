# SYSTEM OVERVIEW

**Status:** Stable  
**Version:** 1.0.0  
**Owner:** SvitloSK Project  
**Last updated:** 2026-07-07

---

## Purpose

SvitloSK is an automated open data processing system designed to provide residents of the Starokostiantyniv Territorial Community with clear, timely and reliable information about planned and emergency power outages, outage schedules and related events.

The system continuously collects publicly available information, transforms it into structured data and publishes it through multiple public information channels.

---

## Scope

The current scope of the project is limited to the territory of the Starokostiantyniv Territorial Community.

Although the system architecture allows future adaptation for other communities, all current design decisions, data models and publications are optimized exclusively for the needs of the Starokostiantyniv community.

---

## Target Audience

SvitloSK is intended for:

- residents of the Starokostiantyniv Territorial Community;
- local government representatives;
- community institutions;
- businesses operating within the community;
- anyone requiring reliable information about power outages.

---

## Data Sources

SvitloSK operates exclusively on publicly available information.

The primary source of operational data is the official website of Khmelnytskyioblenergo.

Additional public sources may be integrated in the future if they satisfy the project principles and quality requirements.

---

## Core Components

The system consists of several independent but interconnected components.

### Open Data Parser

Retrieves and validates official public information.

### Data Processing Engine

Normalizes, aggregates and structures collected information.

### Publisher

Generates public information for supported communication channels.

### Telegram Journal

Publishes operational information and maintains a historical public archive.

### PWA Application

Provides residents with a simple and user-friendly interface for accessing current information.

### Analytics Module

Produces statistical summaries and analytical reports based on collected historical data.

---

## Information Flow

The information lifecycle consists of the following stages:

1. Retrieve official public data.
2. Validate collected information.
3. Normalize and structure data.
4. Detect changes.
5. Generate publications.
6. Update previously published information if required.
7. Archive the final state of the day.
8. Produce analytical datasets.

---

## Public Information Channels

Current public communication channels include:

- Progressive Web Application (PWA);
- Telegram Public Information Journal.

Additional channels may be added in the future without changing the system architecture.

---

## Data Storage

Operational data are stored for a limited period required for system operation.

Historical public information is preserved through the Telegram Journal.

The project prioritizes reproducibility rather than long-term storage of raw operational datasets.

---

## Automation

The entire publication workflow is designed for maximum automation.

The system is capable of:

- retrieving official data;
- detecting updates;
- regenerating publications;
- editing Telegram posts during the current day;
- generating graphical outage schedules;
- producing analytical reports.

Human intervention should only be required for maintenance or exceptional situations.

---

## Design Principles

The system is built according to the following principles:

- Open Data First
- Automation First
- Human-Centered Information
- Transparency
- Simplicity
- Reliability
- Reproducibility

---

## Current Limitations

Current implementation is optimized for:

- Starokostiantyniv Territorial Community;
- official public data sources;
- electricity-related operational information.

The project intentionally avoids collecting personal or confidential information.

---

## Future Evolution

Future development may include:

- support for additional public information channels;
- integration of new open data sources;
- improved analytical capabilities;
- reusable architecture for other territorial communities.

Such expansion shall never compromise the project's primary mission: serving the residents of the Starokostiantyniv Territorial Community.

---

## Related Documents

- CHARTER.md
- PROJECT_PRINCIPLES.md
- ARCHITECTURE.md
- GLOSSARY.md
- RFC_PROCESS.md
- DOCUMENT_INDEX.md
