# TELEGRAM_GRAPHIC_PUBLICATION_TYPES

**Document ID:** TJS-G1.0-B3

**Title:** Graphic Publication Types

**Document Class:** Publication Taxonomy

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# Purpose

Canonical publication taxonomy for graphic publications. Based on actual SvitloSk publications, not generic types.

---

# 1. Publication Families

## 1.1 Primary Family: Scheduled Graphics

Graphics generated automatically from normalized outage data as part of the daily publication cycle.

| # | Type | Ukrainian | Source | Description |
|---|------|-----------|--------|-------------|
| T-001 | Tomorrow Schedule Graphic | Графік знеструмлень на завтра | SSP-007 §6 (Tomorrow Schedule) | Primary public information card showing tomorrow's planned outages for one territory |
| T-002 | Today Schedule Graphic | Графік знеструмлень сьогодні | Derived from T-001 + Lifecycle §4 | Today's outage schedule for one territory |

## 1.2 Secondary Family: Informational Graphics

Graphics containing non-schedule information.

| # | Type | Ukrainian | Source | Description |
|---|------|-----------|--------|-------------|
| T-003 | Emergency Information Card | Картка аварійного повідомлення | SSP-007 §6 (Emergency Card) | Urgent information card with priority over scheduled publications |
| T-004 | Information Card | Інформаційна картка | SSP-007 §6 (Information Card) | General informational messages without schedule timeline |

## 1.3 Tertiary Family: Statistical Graphics

Graphics containing aggregated data.

| # | Type | Ukrainian | Source | Description |
|---|------|-----------|--------|-------------|
| T-005 | Statistics Card | Картка статистики | SSP-007 §6 (Statistics Card) | Generated statistics (powered percentage, outage percentage, total outage duration) |

## 1.4 Administrative Family: Service Graphics

Graphics for internal use or special purposes.

| # | Type | Ukrainian | Source | Description |
|---|------|-----------|--------|-------------|
| T-006 | Service Graphic | Службова графіка | Derived from SSP-007 §13 (Future Extensions) | Internal service graphics (announcements, promotional, administrative) |

---

# 2. Publication Type Properties

## T-001: Tomorrow Schedule Graphic

| Property | Value |
|----------|-------|
| Family | Scheduled |
| Trigger | Automatic (after schedule generation) |
| Territory | One territory per graphic |
| Contains | Date, queues, subqueues, outage intervals, powered intervals, timestamp, branding |
| Timeline | 00:00–24:00, proportional |
| Colors | Powered=Orange, Outage=Dark Gray |
| Update | When data changes |
| Archive | When reporting period ends |

## T-002: Today Schedule Graphic

| Property | Value |
|----------|-------|
| Family | Scheduled |
| Trigger | Automatic (after data update) |
| Territory | One territory per graphic |
| Contains | Date, queues, subqueues, outage intervals, powered intervals, timestamp, branding |
| Timeline | 00:00–current time, proportional |
| Colors | Powered=Orange, Outage=Dark Gray |
| Update | When data changes |
| Archive | At end of day |

## T-003: Emergency Information Card

| Property | Value |
|----------|-------|
| Family | Informational |
| Trigger | Emergency event |
| Territory | One territory per card |
| Contains | Emergency message, territory, timestamp, branding |
| Timeline | None |
| Colors | Emergency-specific |
| Update | When emergency status changes |
| Archive | When emergency resolved |

## T-004: Information Card

| Property | Value |
|----------|-------|
| Family | Informational |
| Trigger | Administrative decision |
| Territory | One territory per card |
| Contains | Informational message, territory, timestamp, branding |
| Timeline | None |
| Colors | Standard |
| Update | When information changes |
| Archive | Permanent |

## T-005: Statistics Card

| Property | Value |
|----------|-------|
| Family | Statistical |
| Trigger | Automatic (daily/periodic) |
| Territory | One territory or community-wide |
| Contains | Powered percentage, outage percentage, total outage duration, timestamp, branding |
| Timeline | None |
| Colors | Standard |
| Update | When statistics change |
| Archive | Permanent |

## T-006: Service Graphic

| Property | Value |
|----------|-------|
| Family | Administrative |
| Trigger | Manual |
| Territory | Variable |
| Contains | Service message, timestamp, branding |
| Timeline | None |
| Colors | Standard |
| Update | When service message changes |
| Archive | Permanent |

---

# 3. Type Classification Rules

| Rule | Statement |
|------|-----------|
| TR-001 | Every graphic publication SHALL belong to exactly one family |
| TR-002 | Every graphic publication SHALL belong to exactly one type |
| TR-003 | Type determines content structure |
| TR-004 | Type determines update behaviour |
| TR-005 | Type determines archive behaviour |
| TR-006 | New types MAY be added through ADR |

---

# 4. Taxonomy Summary

| Family | Types | Count |
|--------|-------|-------|
| Scheduled | T-001, T-002 | 2 |
| Informational | T-003, T-004 | 2 |
| Statistical | T-005 | 1 |
| Administrative | T-006 | 1 |
| **Total** | | **6** |

---

**End of Publication Types**

**Taxonomist:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
