# CANONICAL_COMPONENT_IDENTITY

**Document ID:** ARM-005

**Title:** Canonical Component Identity

**Document Class:** Identity Review

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Component Identity Review

| # | Component | Why This Identifier? | Why Not Alternatives? | Why Stable? |
|---|-----------|---------------------|----------------------|-------------|
| 1 | Parser | Describes exact function: parses external data | "DataRetriever" too generic; "Extractor" implies extraction not parsing | Used across all specs, Glossary-defined, 149+ occurrences |
| 2 | Publication Engine | Describes primary responsibility: generates publications through deterministic transformation | "Coordinator" misses transformation; "Processor" too generic | Used across all specs, Glossary-defined, 149+ occurrences |
| 3 | Publisher | Describes logical role: prepares, generates, distributes | "Generator" too narrow; "Manager" implies administration | Abstract Role, implementation-independent |
| 4 | Telegram Publisher | Describes platform-specific implementation | "TelegramBot" too technical; "DeliveryService" too generic | Platform-specific, Glossary-defined |
| 5 | Schedule Generator | Describes exact function: generates schedules | "ScheduleProcessor" too generic; "TimelineEngine" misleading | Used across all specs, Glossary-defined |
| 6 | Graphic Generator | Describes exact function: generates graphics | "ImageRenderer" too narrow; "VisualEngine" too broad | Used across all specs, Glossary-defined |
| 7 | Data Storage | Describes exact function: stores data persistently | "Database" implementation-specific; "Repository" too broad | Used across all specs, Glossary-defined |
| 8 | Telegram Channel | Describes platform-specific delivery medium | "TelegramChat" too narrow; "DistributionChannel" too generic | Platform-specific, Glossary-defined |

---

# 2. Identity Verdict

**All 8 canonical identifiers are justified.** Each captures the primary responsibility uniquely. No alternative identifier would be stronger.

---

**End of Canonical Component Identity**

**Author:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
