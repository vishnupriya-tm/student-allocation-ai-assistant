# Architecture Design

Frontend

HTML + Bootstrap + JavaScript

↓

Django Views + Django REST Framework APIs

↓

Business Layer

* Allocation Engine
* AI SQL Engine

↓

PostgreSQL Database

↓

Google Gemini API

# Database Design Decisions

The database is normalized into:

* Student
* Course
* CoursePreference
* SeatReservation
* Allocation
* RejectedAllocation
* Dataset

Relationships are implemented using Django ORM Foreign Keys and OneToOne Fields.

# AI Integration Approach

Google Gemini 2.5 Flash is used to:

1. Convert natural language to PostgreSQL SQL.
2. Restrict output to SELECT queries.
3. Execute validated SQL on uploaded datasets.

# Security Considerations

* Only SELECT statements are allowed.
* Unsafe SQL is rejected.
* Dynamic table creation validates schema before execution.

# Challenges Faced

### Allocation Logic

Challenge:

Handling preference ordering and seat availability correctly.

Solution:

Implemented priority-based allocation considering marks, reservations, and application dates.

### Natural Language to SQL

Challenge:

Generating executable SQL safely.

Solution:

Integrated Gemini with SQL validation and execution restrictions.

### Dynamic Table Creation

Challenge:

Creating PostgreSQL tables from arbitrary CSV files.

Solution:

Used Pandas schema inference and dynamic SQL generation.
