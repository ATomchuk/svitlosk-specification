# Category Properties

**Document Class:** Meta-Model Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document determines properties for every category.

---

# Category Properties

## CONCEPT

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Abstract idea | Analysis |
| Necessary Properties | Abstract, not observable, cannot be created | Analysis |
| Sufficient Properties | Abstract AND not observable | Analysis |
| Can Identity Exist? | NO | Abstract |
| Can Lifecycle Exist? | NO | Stable |
| Can Multiple Instances Exist? | YES | Many concepts |
| Can Versions Exist? | NO | Stable |
| Can Ownership Exist? | NO | Independent |
| Examples (Software) | Inheritance, Polymorphism | Analysis |
| Examples (Information) | Entity, Relationship | Analysis |
| Examples (Project) | Journal, Publisher, Publication | Analysis |
| Common Mistakes | Concept vs Object | Analysis |
| Typical Confusion | CONCEPT vs OBJECT | Analysis |

---

## OBJECT

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Discrete entity | Analysis |
| Necessary Properties | Concrete, identifiable, has state | Analysis |
| Sufficient Properties | Concrete AND identifiable | Analysis |
| Can Identity Exist? | YES | Objects have identity |
| Can Lifecycle Exist? | YES | Objects can be created/destroyed |
| Can Multiple Instances Exist? | YES | Many instances |
| Can Versions Exist? | YES | Objects can be versioned |
| Can Ownership Exist? | YES | Objects can own |
| Examples (Software) | Object (OOP), Instance | Analysis |
| Examples (Information) | Entity instance, Record | Analysis |
| Examples (Project) | Journal Edition, Publication Package | Analysis |
| Common Mistakes | Object vs Concept | Analysis |
| Typical Confusion | OBJECT vs CONCEPT | Analysis |

---

## INSTANCE

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Concrete realization | Analysis |
| Necessary Properties | Concrete, realization of type, has identity | Analysis |
| Sufficient Properties | Concrete AND realization | Analysis |
| Can Identity Exist? | YES | Instances have identity |
| Can Lifecycle Exist? | YES | Instances can be created/destroyed |
| Can Multiple Instances Exist? | YES | Many instances |
| Can Versions Exist? | YES | Instances can be versioned |
| Can Ownership Exist? | YES | Instances can own |
| Examples (Software) | Object instance, Class instance | Analysis |
| Examples (Information) | Database record, File instance | Analysis |
| Examples (Project) | Journal Edition, Publication Package | Analysis |
| Common Mistakes | Instance vs Type | Analysis |
| Typical Confusion | INSTANCE vs TYPE | Analysis |

---

## COLLECTION

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Group of entities | Analysis |
| Necessary Properties | Contains multiple, has boundaries | Analysis |
| Sufficient Properties | Contains multiple AND has boundaries | Analysis |
| Can Identity Exist? | YES | Collections have identity |
| Can Lifecycle Exist? | YES | Collections can be created/destroyed |
| Can Multiple Instances Exist? | YES | Many collections |
| Can Versions Exist? | YES | Collections can be versioned |
| Can Ownership Exist? | YES | Collections can own |
| Examples (Software) | List, Set, Array | Analysis |
| Examples (Information) | Database table, File folder | Analysis |
| Examples (Project) | Publication Package | Analysis |
| Common Mistakes | Collection vs Object | Analysis |
| Typical Confusion | COLLECTION vs OBJECT | Analysis |

---

## PROCESS

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Data transformation | Analysis |
| Necessary Properties | Transforms, has input/output, repeatable | Analysis |
| Sufficient Properties | Transforms AND has input/output | Analysis |
| Can Identity Exist? | NO | Processes are activities |
| Can Lifecycle Exist? | NO | Processes are transient |
| Can Multiple Instances Exist? | YES | Processes can run concurrently |
| Can Versions Exist? | NO | Processes are activities |
| Can Ownership Exist? | NO | Processes are activities |
| Examples (Software) | Function, Method, Algorithm | Analysis |
| Examples (Information) | ETL process, Data transformation | Analysis |
| Examples (Project) | Parsing, Interpretation, Rendering | Analysis |
| Common Mistakes | Process vs Service | Analysis |
| Typical Confusion | PROCESS vs SERVICE | Analysis |

---

## SERVICE

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Continuous activity | Analysis |
| Necessary Properties | Continuous, provides capabilities, has interfaces | Analysis |
| Sufficient Properties | Continuous AND provides capabilities | Analysis |
| Can Identity Exist? | YES | Services have identity |
| Can Lifecycle Exist? | YES | Services can be started/stopped |
| Can Multiple Instances Exist? | YES | Multiple services |
| Can Versions Exist? | YES | Services can be versioned |
| Can Ownership Exist? | YES | Services can own |
| Examples (Software) | Web service, API, Microservice | Analysis |
| Examples (Information) | Database service, File service | Analysis |
| Examples (Project) | Journal, Publisher, Parser | Analysis |
| Common Mistakes | Service vs Process | Analysis |
| Typical Confusion | SERVICE vs PROCESS | Analysis |

---

## ROLE

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Logical responsibility | Analysis |
| Necessary Properties | Logical, describes behavior, abstract | Analysis |
| Sufficient Properties | Logical AND describes behavior | Analysis |
| Can Identity Exist? | NO | Roles are abstract |
| Can Lifecycle Exist? | NO | Roles are abstract |
| Can Multiple Instances Exist? | NO | Roles are singular |
| Can Versions Exist? | NO | Roles are abstract |
| Can Ownership Exist? | NO | Roles are abstract |
| Examples (Software) | Interface, Abstract class | Analysis |
| Examples (Information) | User role, Admin role | Analysis |
| Examples (Project) | Publisher, Interpreter, Adapter | Analysis |
| Common Mistakes | Role vs Service | Analysis |
| Typical Confusion | ROLE vs SERVICE | Analysis |

---

## ARTIFACT

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Physical/digital object | Analysis |
| Necessary Properties | Physical/digital, produced by system | Analysis |
| Sufficient Properties | Physical/digital AND produced by system | Analysis |
| Can Identity Exist? | YES | Artifacts have identity |
| Can Lifecycle Exist? | YES | Artifacts can be created/destroyed |
| Can Multiple Instances Exist? | YES | Many artifacts |
| Can Versions Exist? | YES | Artifacts can be versioned |
| Can Ownership Exist? | YES | Artifacts can own |
| Examples (Software) | File, Binary, Document | Analysis |
| Examples (Information) | Report, Export, Backup | Analysis |
| Examples (Project) | Publication, Publication Package | Analysis |
| Common Mistakes | Artifact vs Object | Analysis |
| Typical Confusion | ARTIFACT vs OBJECT | Analysis |

---

## DOCUMENT

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Written information | Analysis |
| Necessary Properties | Written, has content, readable | Analysis |
| Sufficient Properties | Written AND has content | Analysis |
| Can Identity Exist? | YES | Documents have identity |
| Can Lifecycle Exist? | YES | Documents can be created/destroyed |
| Can Multiple Instances Exist? | YES | Many documents |
| Can Versions Exist? | YES | Documents can be versioned |
| Can Ownership Exist? | YES | Documents can own |
| Examples (Software) | Specification, Design document | Analysis |
| Examples (Information) | Policy, Procedure | Analysis |
| Examples (Project) | Specification, Glossary | Analysis |
| Common Mistakes | Document vs Artifact | Analysis |
| Typical Confusion | DOCUMENT vs ARTIFACT | Analysis |

---

## STATE

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Condition/mode | Analysis |
| Necessary Properties | Condition, can change, observed | Analysis |
| Sufficient Properties | Condition AND can change | Analysis |
| Can Identity Exist? | NO | States are conditions |
| Can Lifecycle Exist? | NO | States are transient |
| Can Multiple Instances Exist? | YES | Multiple states |
| Can Versions Exist? | NO | States are conditions |
| Can Ownership Exist? | NO | States are conditions |
| Examples (Software) | Object state, Connection state | Analysis |
| Examples (Information) | Account status, Order status | Analysis |
| Examples (Project) | Publication State, Channel State | Analysis |
| Common Mistakes | State vs Event | Analysis |
| Typical Confusion | STATE vs EVENT | Analysis |

---

## EVENT

| Property | Value | Evidence |
|----------|-------|----------|
| Formal Definition | Occurrence | Analysis |
| Necessary Properties | Instantaneous, has causes/effects | Analysis |
| Sufficient Properties | Instantaneous AND has causes/effects | Analysis |
| Can Identity Exist? | NO | Events are occurrences |
| Can Lifecycle Exist? | NO | Events are instantaneous |
| Can Multiple Instances Exist? | YES | Multiple events |
| Can Versions Exist? | NO | Events are occurrences |
| Can Ownership Exist? | NO | Events are occurrences |
| Examples (Software) | Mouse click, HTTP request | Analysis |
| Examples (Information) | Account created, Order placed | Analysis |
| Examples (Project) | Data Changed, Publication Expired | Analysis |
| Common Mistakes | Event vs State | Analysis |
| Typical Confusion | EVENT vs STATE | Analysis |

---

# Traceability

| Category | Source |
|----------|--------|
| All properties | Analysis of ontological patterns and domain knowledge |

---

**End of Category Properties**
