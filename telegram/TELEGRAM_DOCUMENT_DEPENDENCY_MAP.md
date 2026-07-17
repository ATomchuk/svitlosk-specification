# Telegram Document Dependency Map

**Date:** 2026-07-09
**Scope:** Dependencies between all Telegram documents and cross-references to repository documents

---

## Declared Dependencies

| Document | Depends on (declared) | Referenced by (declared) |
|----------|----------------------|------------------------|
| TJS-001 | None | All other TJS (as foundation) |
| TJS-002 | None | None |
| TJS-003 | None | None |
| TJS-004 | None | TJS-005 |
| TJS-005 | TJS-004, TERRITORIAL_MODEL.md, SSP-003 | TJS-006, TJS-007, TJS-008 |
| TJS-006 | TJS-003 (labeled "Editorial Policy" — WRONG), TJS-005, SSP-003, TERRITORIAL_MODEL.md | TJS-007, TJS-008 |
| TJS-007 | TERRITORIAL_MODEL.md, DATA_MODEL.md, SSP-002, SSP-003, TJS-005, TJS-006 | TJS-008 (labeled "Channel Management" — WRONG) |
| TJS-008 | SSP-002, SSP-003, TJS-005, TJS-006, TJS-007 (labeled "Channel Management" — WRONG), DATA_MODEL.md, TERRITORIAL_MODEL.md | future Scheduler, future Telegram Publisher |

---

## Implicit Dependencies (not declared but exist)

| Document | Implicit Dependency | Reason |
|----------|-------------------|--------|
| TJS-002 | TJS-001 | Lifecycle concepts derive from journal identity |
| TJS-002 | TJS-004 | Editorial rules affect lifecycle decisions |
| TJS-003 | TJS-001 | Post structure derives from journal concept |
| TJS-003 | TJS-004 | Structure follows editorial policy |
| TJS-004 | TJS-001 | Editorial policy derives from journal principles |
| TJS-004 | TERRITORIAL_MODEL.md | Territory presentation rules |
| TJS-007 | TJS-001 | Lifecycle derives from journal concept |
| TJS-007 | TJS-004 | Editorial rules affect lifecycle |
| TJS-008 | TJS-001 | Daily cycle derives from journal concept |
| TJS-008 | TJS-004 | Editorial rules affect daily cycle |

---

## Incorrect Cross-References

| Source | Declared Reference | Actual Target | Correct? |
|--------|-------------------|---------------|----------|
| TJS-006 §17 | "TJS-003 — Editorial Policy" | TJS-003 is "Post Structure" | **NO** — should be "TJS-004 — Editorial Policy" |
| TJS-008 §18 | "TJS-007 — Channel Management" | TJS-007 is "Publication Lifecycle" | **NO** — TJS-007 has no "Channel Management" title |

---

## Dependency Graph

```text
TJS-001 (Journal Concept)
    │
    ├──→ TJS-002 (Publication Lifecycle) [implicit]
    ├──→ TJS-003 (Post Structure) [implicit]
    ├──→ TJS-004 (Editorial Policy) [implicit]
    │        │
    │        └──→ TJS-005 (Message Templates) [declared]
    │                 │
    │                 ├──→ TJS-006 (Rendering Rules) [declared]
    │                 │        │
    │                 │        ├──→ TJS-007 (Publication Lifecycle) [declared]
    │                 │        │        │
    │                 │        │        └──→ TJS-008 (Publication Lifecycle) [declared]
    │                 │        │
    │                 │        └──→ (external: SSP-002, SSP-003, TERRITORIAL_MODEL, DATA_MODEL)
    │                 │
    │                 └──→ TJS-007, TJS-008 [declared]
    │
    └──→ TJS-002, TJS-007, TJS-008 [implicit — all depend on journal concept]
```

---

## Circular Dependency Check

| Check | Result |
|-------|--------|
| TJS-002 → TJS-007 → TJS-008 → TJS-007 | NO circular dependency (TJS-008 depends on TJS-007, not reverse) |
| TJS-005 → TJS-004 → TJS-005 | NO (TJS-004 does not depend on TJS-005) |
| TJS-006 → TJS-005 → TJS-006 | NO (TJS-005 does not depend on TJS-006) |

**Result: NO circular dependencies detected.**

---

## Orphan Document Check

| Document | Has incoming references? | Orphan? |
|----------|------------------------|---------|
| TJS-001 | YES (all TJS depend on it implicitly) | NO |
| TJS-002 | NO (not referenced by any TJS) | YES — isolated |
| TJS-003 | YES (TJS-006 references it, though incorrectly) | PARTIAL |
| TJS-004 | YES (TJS-005 references it) | NO |
| TJS-005 | YES (TJS-006, TJS-007, TJS-008 reference it) | NO |
| TJS-006 | YES (TJS-007, TJS-008 reference it) | NO |
| TJS-007 | YES (TJS-008 references it) | NO |
| TJS-008 | NO (not referenced by any TJS) | YES — terminal |

---

**Mapper:** SvitloSk Certification Pipeline
