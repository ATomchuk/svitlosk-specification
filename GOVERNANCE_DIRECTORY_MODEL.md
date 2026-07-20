# GOVERNANCE_DIRECTORY_MODEL

**Document ID:** GA-002

**Title:** Governance Directory Model

**Document Class:** Directory Model

**Status:** COMPLETE

**Author:** SvitloSk Project

---

# 1. Governance Directory Model

`
governance/
    baselines/        (permanent — grows with each version)
    translation/      (active — may become historical)
`

---

# 2. Layer Responsibility Table

| Layer | Responsibility | Contains | Does NOT contain |
|-------|---------------|----------|------------------|
| Root | Identity + Navigation + Governance foundation | 13 Foundation docs + README | Anything non-Foundation |
| governance/ | Active governance rules + baselines | Baselines, translation rules, future governance areas | Historical records, identity documents |
| archive/ | Historical records | Completed work, reviews, migration artifacts | Active documents, governance rules |
| telegram/ | Telegram subsystem | Foundation, specs, working, legacy, archive | Non-Telegram documents |
| specification/ | SSP | SSP-001 through SSP-013 | Non-SSP documents |
| adr/ | Architecture decisions | ADR documents | Non-ADR documents |

---

# 3. Strict Boundary Rules

| Rule | Statement |
|------|-----------|
| BOUNDARY-R1 | A document SHALL NOT exist in both Root and governance/ |
| BOUNDARY-R2 | A document SHALL NOT exist in both governance/ and archive/ |
| BOUNDARY-R3 | A document SHALL NOT exist in both Root and archive/ |
| BOUNDARY-R4 | A document belongs to exactly one layer |
| BOUNDARY-R5 | When a governance document becomes historical, it moves to archive/ |

---

# 4. Growth Prediction

| Scenario | Root | governance/ | archive/ |
|----------|------|-------------|----------|
| Baseline v4.0 | 13 | +1 file in baselines/ | +1 old baseline if replaced |
| Translation complete | 13 | translation/ becomes historical | +6 files from translation/ |
| Future subsystem | 13 | no change | no change |
| Future review | 13 | no change | +N files |

**Root ALWAYS stays at 13 files.** Governance grows slowly. Archive grows with completed work.

---

**End of Governance Directory Model**

**Modeler:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** COMPLETE
