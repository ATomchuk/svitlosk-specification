# Category Definitions

**Document Class:** Meta-Model Validation

**Status:** Complete

**Author:** SvitloSk Project

---

# Purpose

This document defines every category formally.

---

# Category Definitions

## CONCEPT

### Formal Definition

An abstract idea that describes the domain.

### Necessary Properties

- Abstract
- Not directly observable
- Cannot be created or destroyed
- Defines vocabulary

### Sufficient Properties

- Abstract AND
- Not directly observable AND
- Cannot be created or destroyed

### Can Identity Exist?

NO — concepts are abstract.

### Can Lifecycle Exist?

NO — concepts are stable.

### Can Multiple Instances Exist?

YES — many concepts can exist.

### Can Versions Exist?

NO — concepts are stable.

### Can Ownership Exist?

NO — concepts are independent.

### Examples from Software Engineering

- Inheritance
- Polymorphism
- Encapsulation

### Examples from Information Systems

- Entity
- Relationship
- Attribute

### Examples from Our Project

- Journal
- Publisher
- Publication
- Lifecycle
- Territory
- Information
- Knowledge
- Open Data

### Common Mistakes

- Confusing concept with instance
- Confusing concept with object

### Typical Confusion

CONCEPT vs OBJECT — concepts are abstract, objects are concrete.

---

## OBJECT

### Formal Definition

A discrete, identifiable entity that exists in the system.

### Necessary Properties

- Concrete
- Identifiable
- Can be created and destroyed
- Has state

### Sufficient Properties

- Concrete AND
- Identifiable AND
- Can be created AND
- Has state

### Can Identity Exist?

YES — objects have identity.

### Can Lifecycle Exist?

YES — objects can be created and destroyed.

### Can Multiple Instances Exist?

YES — many instances of same type.

### Can Versions Exist?

YES — objects can be versioned.

### Can Ownership Exist?

YES — objects can own other objects.

### Examples from Software Engineering

- Object (OOP)
- Instance
- Record

### Examples from Information Systems

- Entity instance
- Data record
- Document instance

### Examples from Our Project

- Journal Edition
- Publication Package

### Common Mistakes

- Confusing object with concept
- Confusing object with artifact

### Typical Confusion

OBJECT vs ARTIFACT — objects are conceptual, artifacts are physical.

---

## INSTANCE

### Formal Definition

A concrete realization of a type.

### Necessary Properties

- Concrete
- Realization of type
- Has identity
- Has state

### Sufficient Properties

- Concrete AND
- Realization of type AND
- Has identity

### Can Identity Exist?

YES — instances have identity.

### Can Lifecycle Exist?

YES — instances can be created and destroyed.

### Can Multiple Instances Exist?

YES — many instances of same type.

### Can Versions Exist?

YES — instances can be versioned.

### Can Ownership Exist?

YES — instances can own other entities.

### Examples from Software Engineering

- Object instance
- Class instance
- Template instance

### Examples from Our Information Systems

- Database record
- File instance
- Document copy

### Examples from Our Project

- Journal Edition
- Publication Package

### Common Mistakes

- Confusing instance with type
- Confusing instance with object

### Typical Confusion

INSTANCE vs TYPE — instances are concrete, types are abstract.

---

## COLLECTION

### Formal Definition

A group of related entities.

### Necessary Properties

- Contains multiple entities
- Has boundaries
- Can be empty

### Sufficient Properties

- Contains multiple entities AND
- Has boundaries

### Can Identity Exist?

YES — collections have identity.

### Can Lifecycle Exist?

YES — collections can be created and destroyed.

### Can Multiple Instances Exist?

YES — many collections can exist.

### Can Versions Exist?

YES — collections can be versioned.

### Can Ownership Exist?

YES — collections can own other entities.

### Examples from Software Engineering

- List
- Set
- Array

### Examples from Information Systems

- Database table
- File folder
- Document collection

### Examples from Our Project

- Publication Package

### Common Mistakes

- Confusing collection with object
- Confusing collection with group

### Typical Confusion

COLLECTION vs OBJECT — collections contain objects, objects are contained.

---

## PROCESS

### Formal Definition

A discrete activity that transforms data.

### Necessary Properties

- Transforms data
- Has input and output
- Can be triggered
- Is repeatable

### Sufficient Properties

- Transforms data AND
- Has input and output

### Can Identity Exist?

NO — processes are activities, not entities.

### Can Lifecycle Exist?

NO — processes are transient.

### Can Multiple Instances Exist?

YES — processes can run concurrently.

### Can Versions Exist?

NO — processes are activities.

### Can Ownership Exist?

NO — processes are activities.

### Examples from Software Engineering

- Function
- Method
- Algorithm

### Examples from Information Systems

- ETL process
- Data transformation
- Report generation

### Examples from Our Project

- Parsing
- Interpretation
- Rendering
- Distribution

### Common Mistakes

- Confusing process with service
- Confusing process with event

### Typical Confusion

PROCESS vs SERVICE — processes are transient, services are continuous.

---

## SERVICE

### Formal Definition

A continuous activity performed by the system.

### Necessary Properties

- Continuous
- Provides capabilities
- Is invoked by other entities
- Has defined interfaces

### Sufficient Properties

- Continuous AND
- Provides capabilities

### Can Identity Exist?

YES — services have identity.

### Can Lifecycle Exist?

YES — services can be started and stopped.

### Can Multiple Instances Exist?

YES — multiple services can exist.

### Can Versions Exist?

YES — services can be versioned.

### Can Ownership Exist?

YES — services can own other entities.

### Examples from Software Engineering

- Web service
- API
- Microservice

### Examples from Information Systems

- Database service
- File service
- Email service

### Examples from Our Project

- Journal
- Publisher
- Parser
- Archive
- Channel
- Adapter

### Common Mistakes

- Confusing service with process
- Confusing service with role

### Typical Confusion

SERVICE vs PROCESS — services are continuous, processes are transient.

---

## ROLE

### Formal Definition

A logical responsibility performed within the system.

### Necessary Properties

- Logical
- Describes behavior
- Independent of implementation
- Can be implemented by different components

### Sufficient Properties

- Logical AND
- Describes behavior

### Can Identity Exist?

NO — roles are abstract responsibilities.

### Can Lifecycle Exist?

NO — roles are abstract.

### Can Multiple Instances Exist?

NO — roles are singular.

### Can Versions Exist?

NO — roles are abstract.

### Can Ownership Exist?

NO — roles are abstract.

### Examples from Software Engineering

- Interface
- Abstract class
- Protocol

### Examples from Information Systems

- User role
- Admin role
- Reader role

### Examples from Our Project

- Publisher
- Interpreter
- Adapter

### Common Mistakes

- Confusing role with service
- Confusing role with component

### Typical Confusion

ROLE vs SERVICE — roles are abstract responsibilities, services are concrete activities.

---

## ARTIFACT

### Formal Definition

A physical or digital object produced by the system.

### Necessary Properties

- Physical or digital
- Produced by system
- Can be stored
- Can be distributed

### Sufficient Properties

- Physical or digital AND
- Produced by system

### Can Identity Exist?

YES — artifacts have identity.

### Can Lifecycle Exist?

YES — artifacts can be created and destroyed.

### Can Multiple Instances Exist?

YES — many artifacts can exist.

### Can Versions Exist?

YES — artifacts can be versioned.

### Can Ownership Exist?

YES — artifacts can own other entities.

### Examples from Software Engineering

- File
- Binary
- Document

### Examples from Information Systems

- Report
- Export
- Backup

### Examples from Our Project

- Publication
- Publication Package
- Representation

### Common Mistakes

- Confusing artifact with object
- Confusing artifact with document

### Typical Confusion

ARTIFACT vs OBJECT — artifacts are physical/digital, objects are conceptual.

---

## DOCUMENT

### Formal Definition

Written or recorded information.

### Necessary Properties

- Written or recorded
- Has content
- Can be read
- Has format

### Sufficient Properties

- Written or recorded AND
- Has content

### Can Identity Exist?

YES — documents have identity.

### Can Lifecycle Exist?

YES — documents can be created and destroyed.

### Can Multiple Instances Exist?

YES — many documents can exist.

### Can Versions Exist?

YES — documents can be versioned.

### Can Ownership Exist?

YES — documents can own other entities.

### Examples from Software Engineering

- Specification
- Design document
- README

### Examples from Information Systems

- Policy
- Procedure
- Manual

### Examples from Our Project

- Specification
- Glossary

### Common Mistakes

- Confusing document with artifact
- Confusing document with object

### Typical Confusion

DOCUMENT vs ARTIFACT — documents are written information, artifacts are physical/digital objects.

---

## STATE

### Formal Definition

A condition or mode of existence.

### Necessary Properties

- Condition or mode
- Can change over time
- Is observed, not created
- Is transient or persistent

### Sufficient Properties

- Condition or mode AND
- Can change over time

### Can Identity Exist?

NO — states are conditions, not entities.

### Can Lifecycle Exist?

NO — states are transient.

### Can Multiple Instances Exist?

YES — multiple states can exist.

### Can Versions Exist?

NO — states are conditions.

### Can Ownership Exist?

NO — states are conditions.

### Examples from Software Engineering

- Object state
- Connection state
- Transaction state

### Examples from Information Systems

- Account status
- Order status
- Document status

### Examples from Our Project

- Publication State
- Lifecycle State
- Channel State

### Common Mistakes

- Confusing state with entity
- Confusing state with event

### Typical Confusion

STATE vs EVENT — states are conditions, events are occurrences.

---

## EVENT

### Formal Definition

An occurrence that happens at a specific time.

### Necessary Properties

- Instantaneous
- Has causes and effects
- Triggers transitions
- Is observed

### Sufficient Properties

- Instantaneous AND
- Has causes and effects

### Can Identity Exist?

NO — events are occurrences, not entities.

### Can Lifecycle Exist?

NO — events are instantaneous.

### Can Multiple Instances Exist?

YES — multiple events can occur.

### Can Versions Exist?

NO — events are occurrences.

### Can Ownership Exist?

NO — events are occurrences.

### Examples from Software Engineering

- Mouse click
- HTTP request
- Database transaction

### Examples from Information Systems

- Account created
- Order placed
- Document uploaded

### Examples from Our Project

- Data Changed
- Publication Expired
- Channel Connected

### Common Mistakes

- Confusing event with state
- Confusing event with process

### Typical Confusion

EVENT vs STATE — events are occurrences, states are conditions.

---

# 5. Category Definition Summary

| Category | Definition | Key Properties |
|----------|------------|----------------|
| CONCEPT | Abstract idea | Abstract, not observable, cannot be created |
| OBJECT | Discrete entity | Concrete, identifiable, has state |
| INSTANCE | Concrete realization | Concrete, realization of type, has identity |
| COLLECTION | Group of entities | Contains multiple, has boundaries |
| PROCESS | Data transformation | Transforms, has input/output, repeatable |
| SERVICE | Continuous activity | Continuous, provides capabilities |
| ROLE | Logical responsibility | Logical, describes behavior, abstract |
| ARTIFACT | Physical/digital object | Physical/digital, produced by system |
| DOCUMENT | Written information | Written, has content, readable |
| STATE | Condition/mode | Condition, can change, observed |
| EVENT | Occurrence | Instantaneous, has causes/effects |

---

# Traceability

| Category | Source |
|----------|--------|
| All categories | Analysis of ontological patterns and domain knowledge |

---

**End of Category Definitions**
