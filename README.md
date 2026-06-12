# student-allocation-ai-assistant
AI-powered Student Course Allocation System and Natural Language SQL Assistant built using Django, DRF, PostgreSQL and OpenAI.

# AI-Powered Student Course Allocation System

## Overview

A Django REST Framework application that automates student course allocation based on:

- Marks
- Reservation category
- Application date
- Course preferences

The system also provides AI-assisted reporting and analytics.

---

## Tech Stack

- Python 3
- Django 6
- Django REST Framework
- PostgreSQL
- GitHub

---

## Features

### Student Management

- Student Registration
- Category Management
- Marks Tracking
- Application Date Tracking

### Course Management

- Course Creation
- Seat Reservation by Category

### Allocation Engine

Rules:

1. Higher marks receive priority
2. Reservation rules are respected
3. Earlier application date wins when marks are equal
4. One student can receive only one course
5. Preference order is respected

### Dashboard APIs

- Allocated Students
- Available Seats
- Course Statistics
- Category-wise Allocation

### AI Assistant

Supports:

- How many students were allocated to each course?
- Which students did not receive their first preference?
- Which course had the highest rejection rate?
- Show category-wise allocation summary.

---

## Setup

```bash
git clone <repo-url>

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Configure PostgreSQL database.

Run:

```bash
python manage.py migrate

python manage.py runserver
```

---

## API Endpoints

### Students

```text
/api/students/
```

### Courses

```text
/api/courses/
```

### Allocation

```text
/api/allocate/
```

### Dashboard

```text
/api/dashboard/allocated/

/api/dashboard/seats/

/api/dashboard/course-stats/

/api/dashboard/category-summary/
```

### AI Assistant

```text
/api/assistant/
```

---
