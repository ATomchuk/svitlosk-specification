# REPOSITORY_ROOT_ARCHITECTURE_PRINCIPLE

**Document ID:** TJS-R4.3-A1

**Title:** Repository Root Architecture Principle

**Document Class:** Architectural Principle

**Status:** Stable

**Author:** SvitloSk Project

---

# Purpose

Establish a permanent normative rule governing the Repository Root.

---

# 1. Repository Root Architecture Principle

PR-ROOT-001

The Repository Root exists ONLY as the governance and navigation entry point for the entire repository.

The Repository Root SHALL contain ONLY repository-wide normative governance documents.

Subsystem documents SHALL NEVER be placed in Repository Root.

Working documents SHALL NEVER be placed in Repository Root.

Temporary documents SHALL NEVER be placed in Repository Root.

Subsystem specifications SHALL live inside their subsystem directories.

Repository-wide normative documents MAY remain in Root.

---

# 2. Principle Statement

The repository root is the permanent governance and navigation entry point. It exists to orient visitors, onboard contributors, and present the normative foundation of the project. It SHALL NOT be used as a workspace, archive, or subsystem storage.

---

# 3. Principle Scope

This principle applies to:

* every future document added to the repository;
* every migration decision affecting Root;
* every governance review of repository structure;
* every new subsystem introduced to the repository.

---

# 4. Principle Authority

This principle is normative. Violations SHALL be corrected through the ADR process.

---

**End of Root Architecture Principle**

**Authority:** SvitloSk Certification Pipeline
**Date:** 2026-07-13
**Status:** Stable
