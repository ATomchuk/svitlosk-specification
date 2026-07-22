# OBJECT_IDENTITY_MATRIX

**Document ID:** CASE001D-OBJECT-MATRIX

**Title:** Object — Identity Matrix

**Document Class:** Investigation Artifact

**Status:** Stable

**Author:** SvitloSk Project — Identity vs Identifier Investigation

---

# Purpose

This document provides a complete inventory of every domain object and its Identity characteristics.

---

# Object Identity Matrix

| # | Object | Has Identity? | Identity Source | Identity Created | Identity Persistent | Identity Survives Identifier Changes |
|---|--------|---------------|-----------------|------------------|--------------------|---------------------------------------|
| 1 | Publication | YES | Territory + Date + Template | At creation | YES | YES |
| 2 | Issue | YES | Calendar day | When first Publication generated | YES | YES |
| 3 | Journal | YES | Continuous publication | At project start | YES | YES |
| 4 | Territory | YES | Administrative name | Before SvitloSk | YES | YES |
| 5 | Address | YES | Official designation | Before SvitloSk | YES | YES |
| 6 | Street | YES | Official name | Before SvitloSk | YES | YES |
| 7 | Settlement | YES | Official name | Before SvitloSk | YES | YES |
| 8 | Community | YES | Administrative boundaries | Before SvitloSk | YES | YES |
| 9 | Queue | YES | Official queue identifier | Before SvitloSk | YES | YES |
| 10 | Subqueue | YES | Official subqueue identifier | Before SvitloSk | YES | YES |
| 11 | Normalized Dataset | YES | Unique per retrieval | At parsing | NO | YES |
| 12 | Schedule | YES | Unique per generation | At schedule generation | NO | YES |
| 13 | Graphic | YES | Unique per generation | At graphic generation | NO | YES |
| 14 | Publication Package | NO | Borrows from Reporting Period | At generation | NO | YES |
| 15 | Telegram Message | NO | Borrows from Publication | At delivery | NO | NO |
| 16 | Historical Record | NO | Borrows from Publication | At archival | YES | YES |
| 17 | Database Record | NO | Borrows from Publication | At storage | NO | YES |
| 18 | Publication Window | YES | Time window | At configuration | YES | YES |
| 19 | Publication Session | YES | One execution | At execution | NO | YES |
| 20 | Publication Cycle | YES | Daily cycle | At cycle start | YES | YES |

---

# Identity Characteristics

## Objects with Intrinsic Identity

| Object | Identity Criteria | Immutable? | Stable? |
|--------|-------------------|------------|---------|
| Publication | Territory + Date + Template | YES | YES |
| Issue | Calendar day | YES | YES |
| Journal | Continuous publication | YES | YES |
| Territory | Administrative name | YES | YES |
| Address | Official designation | YES | YES |
| Street | Official name | YES | YES |
| Settlement | Official name | YES | YES |
| Community | Administrative boundaries | YES | YES |
| Queue | Official queue identifier | YES | YES |
| Subqueue | Official subqueue identifier | YES | YES |
| Publication Window | Time window | YES | YES |
| Publication Cycle | Daily cycle | YES | YES |

## Objects with Borrowed Identity

| Object | Borrows From | Identity Source |
|--------|--------------|-----------------|
| Publication Package | Reporting Period | Reporting Period |
| Telegram Message | Publication | Publication Identity |
| Historical Record | Publication | Publication Identity |
| Database Record | Publication | Publication Identity |

## Objects with Temporary Identity

| Object | Identity Duration | Identity消失 |
|--------|-------------------|--------------|
| Normalized Dataset | One retrieval cycle | Consumed by Publication Engine |
| Schedule | One generation cycle | Regenerated |
| Graphic | One generation cycle | Regenerated |
| Publication Session | One execution | Ends after execution |

---

# Key Insight

**12 of 20 objects have INTRINSIC Identity.**

**4 objects have BORROWED Identity.**

**4 objects have TEMPORARY Identity.**

**This confirms that Identity is a fundamental property of most domain objects.**

---

# End of Object Identity Matrix
