# DOMAIN_EXISTENCE_MATRIX

**Document ID:** CASE001-001

**Title:** Domain Existence Matrix

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Architectural Investigation №001

---

# Purpose

This document maps every concept identified in the Telegram Publishing Domain against its independent existence, observability, human describability, creator, and consumer.

---

# Investigation Scope

All normative documentation: CHARTER, PROJECT_PRINCIPLES, GLOSSARY, TJS-000, TJS-010, TJS-020, TJS-021, TJS-022, ADR-001, DOCUMENT_INDEX, TERRITORIAL_MODEL.

---

# Existence Matrix

| Concept | Exists without SvitloSk | Observable in reality | Human can describe without software | Creator | Consumer |
|---------|------------------------|----------------------|-------------------------------------|---------|----------|
| Starokostiantyniv Community | YES | YES | YES | Political/administrative process | Residents, government, utilities |
| Administrative Centre | YES | YES | YES | Political/administrative process | Residents, government |
| Starosta District | YES | YES | YES | Political/administrative process | Residents, government |
| Settlement | YES | YES | YES | Historical growth | Residents, government |
| Street | YES | YES | YES | Urban planning | Residents, postal services |
| Address | YES | YES | YES | Urban planning, cadastral registry | Residents, postal services, utilities |
| Distribution System Operator | YES | YES | YES | Energy regulation | Residents, government, industry |
| Planned Power Outage | YES | YES | YES | DSO operational planning | Residents, businesses |
| Emergency Power Outage | YES | YES | YES | DSO emergency response | Residents, businesses |
| Outage Schedule | YES | YES | YES | DSO scheduling department | Residents, businesses |
| Queue | YES | YES | YES | DSO load management | Residents, businesses |
| Subqueue | YES | YES | YES | DSO load management | Residents, businesses |
| Electricity Availability | YES | YES | YES | Physical grid state | Residents, businesses |
| Availability Window | YES | YES | YES | DSO scheduling | Residents, businesses |
| Outage Window | YES | YES | YES | DSO scheduling | Residents, businesses |
| Open Data | YES | YES | YES | Government transparency policy | Public, media, civil society |
| Data Source | YES | YES | YES | Government/institutional mandate | Public, media, civil society |
| Residents | YES | YES | YES | Community membership | SvitloSk, government |
| Information Consumers | YES | YES | YES | Need for information | SvitloSk, government |
| Journal | NO | PARTIALLY | YES | SvitloSk editorial decision | Residents |
| Issue | NO | PARTIALLY | YES | SvitloSk editorial decision | Residents |
| Publication | NO | PARTIALLY | YES | SvitloSk editorial decision | Residents |
| Telegram | YES | YES | YES | Telegram company | Global users |
| Telegram Channel | NO | YES | YES | SvitloSk administrators | Residents |
| Publication Channel | NO | PARTIALLY | YES | SvitloSk project design | Residents |
| Publication Package | NO | NO | YES | SvitloSk editorial design | Residents |
| Editorial Policy | NO | NO | YES | SvitloSk editorial decision | Residents, SvitloSk team |
| Reporting Period | NO | PARTIALLY | YES | SvitloSk editorial decision | SvitloSk team |
| Publication Lifecycle | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Archive | NO | PARTIALLY | YES | SvitloSk editorial decision | Residents, researchers |
| Territory (publication unit) | NO | PARTIALLY | YES | SvitloSk publication design | Residents |
| Community (territorial) | YES | YES | YES | Political/administrative process | Residents, government |
| Publication Engine | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Parser | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Publisher Role | NO | NO | YES | SvitloSk system design | SvitloSk team |
| Data Storage | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Schedule Generator | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Graphic Generator | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Telegram Publisher | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Publication Lifecycle States | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Telegram Message ID | NO | NO | NO | Telegram platform | SvitloSk team |
| Rate Limiting | NO | NO | NO | Telegram platform | SvitloSk team |
| Canonical Templates | NO | NO | YES | SvitloSk editorial design | Residents |
| Rendering Pipeline | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Deterministic Rendering | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Source Fidelity | NO | NO | YES | SvitloSk editorial principle | Residents |
| Non-destructive Channel | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Non-destructive Update | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Publication Ownership | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Publication Session | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Daily Publication Cycle | NO | PARTIALLY | YES | SvitloSk operational design | Residents, SvitloSk team |
| Publication Windows | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Traceability | NO | NO | YES | SvitloSk quality principle | Residents, auditors |
| Reliability | NO | NO | YES | SvitloSk quality principle | Residents |
| Canonical Equality | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Error Handling | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Graphic Publication | NO | NO | NO | SvitloSk software design | Residents |
| Tomorrow Schedule Graphic | NO | NO | NO | SvitloSk software design | Residents |
| Emergency Information Card | NO | NO | NO | SvitloSk software design | Residents |
| Statistics Card | NO | NO | NO | SvitloSk software design | Residents |
| Service Graphic | NO | NO | NO | SvitloSk software design | SvitloSk team |
| Powered state | NO | YES | YES | Physical grid state | Residents |
| Outage state | NO | YES | YES | Physical grid state | Residents |
| Publication Grammar | NO | NO | YES | SvitloSk editorial design | Residents |
| Territory Header | NO | NO | YES | SvitloSk editorial design | Residents |
| Publication Sections | NO | NO | YES | SvitloSk editorial design | Residents |
| Validation Rules | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Formatting Rules | NO | NO | YES | SvitloSk editorial decision | Residents |
| Editorial Principles | NO | NO | YES | SvitloSk editorial decision | Residents, SvitloSk team |
| Territory Presentation | NO | NO | YES | SvitloSk editorial decision | Residents |
| Time Format | NO | NO | YES | SvitloSk editorial decision | Residents |
| Settlement Formatting | NO | NO | YES | SvitloSk editorial decision | Residents |
| Address Formatting | NO | NO | YES | SvitloSk editorial decision | Residents |
| Branding | NO | NO | YES | SvitloSk identity decision | Residents |
| Editing Rules | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Long Publication Split | NO | NO | NO | SvitloSk system design | SvitloSk team |
| HTML Rendering Rules | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Stable Output Rule | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Empty Block Rule | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Graphic Automation | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Graphic Clarity | NO | NO | YES | SvitloSk editorial principle | Residents |
| Graphic Branding | NO | NO | YES | SvitloSk identity decision | Residents |
| Graphic Accessibility | NO | NO | YES | SvitloSk accessibility principle | Residents |
| Graphic Color | NO | NO | YES | SvitloSk visual design | Residents |
| Graphic Format | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Graphic Validation | NO | NO | NO | SvitloSk system design | SvitloSk team |
| Graphic Timeline | NO | NO | NO | SvitloSk system design | Residents |
| Repository Authority | NO | NO | NO | SvitloSk governance | SvitloSk team |
| Repository State | NO | NO | NO | SvitloSk governance | SvitloSk team |

---

# End of Document
