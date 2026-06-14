# student-allocation-ai-assistant

AI-powered Student Course Allocation System and Natural Language SQL Assistant built using **Django**, **Django REST Framework**, **PostgreSQL**, and **Google Gemini AI**.

---

# Overview

This project consists of two modules:

## Task 1 - AI-Powered Student Course Allocation System

A web application that automates student course allocation based on:

* Student marks
* Reservation category
* Application date
* Course preferences

The system also provides dashboard analytics and reporting.

---

## Task 2 - AI SQL Assistant

A generic AI-powered analytics platform that allows users to:

* Upload CSV datasets
* Dynamically create PostgreSQL tables
* Query datasets using natural language
* Convert prompts to SQL using Google Gemini
* Execute validated SQL and display results

---

# Technology Stack

### Frontend

* HTML
* Bootstrap 5
* JavaScript

### Backend

* Python 3
* Django 6
* Django REST Framework

### Database

* PostgreSQL

### AI Integration

* Google Gemini 2.5 Flash

---

# Task 1 - Student Course Allocation System

## Features

### Student Management

* Student Registration
* Marks Tracking
* Category Management
* Application Date Tracking

### Course Management

* Course Creation
* Total Seats Management
* Category-wise Seat Reservation

### Course Preferences

Students can select:

* Priority 1
* Priority 2
* Priority 3

### Allocation Engine

Business rules implemented:

1. Higher marks receive higher priority.
2. Reservation rules are considered.
3. Earlier application date wins if marks are equal.
4. One student can be allocated only one course.
5. If the first preference is unavailable, subsequent preferences are evaluated.

---

## Dashboard

Dashboard displays:

* Total Students
* Total Courses
* Total Allocations
* Course Statistics
* Category-wise Allocation Summary
* Recent Allocations

Additional pages:

* Students
* Courses
* Preferences
* Reservations
* Allocations

---

# Task 2 - AI SQL Assistant

## Features

### Dataset Upload

Supports:

* CSV Upload
* Dynamic schema detection

### Dynamic Table Creation

Uploaded datasets are:

* Parsed using Pandas
* Converted to PostgreSQL tables
* Stored dynamically

### Natural Language to SQL

Example queries:

* Show top 10 customers by revenue
* Count students in each category
* Show average marks
* Which month generated the highest sales?

### AI Integration

Google Gemini is used to:

* Convert natural language into PostgreSQL SQL
* Restrict output to SELECT statements
* Generate safe SQL queries

### Query Validation

The application validates:

* Only SELECT queries are allowed
* Unsafe SQL is rejected

### Query Execution

Validated queries are executed and results are displayed in the UI.

---

# Project Structure

student-allocation-ai-assistant/

├── allocation/

│   ├── models.py

│   ├── views.py

│   ├── serializers.py

│   ├── services.py

│   └── templates/

│       └── allocation/

│           ├── dashboard.html

│           ├── students.html

│           ├── courses.html

│           ├── preferences.html

│           ├── reservations.html

│           └── allocations.html

│

├── ai_assistant/

│   ├── views.py

│   ├── services.py

│   ├── gemini_service.py

│   ├── query_service.py

│   └── templates/

│       └── ai_assistant/

│           └── chat.html

│

├── core/

├── requirements.txt

├── README.md

└── media/

---

# Setup Instructions

Clone repository:

```bash
git clone <repository-url>
```

Create virtual environment:

```bash
python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure `.env`

```text
DB_NAME=

DB_USER=

DB_PASSWORD=

DB_HOST=

DB_PORT=

GEMINI_API_KEY=
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/api/dashboard/
```

---

# Security Considerations

* AI Assistant only allows SELECT queries.
* Unsafe SQL is rejected before execution.
* Dynamic table creation uses validated schemas.
* SQL execution is restricted to safe operations.

---

# Future Improvements

* Authentication and role-based access
* Query history
* Charts and graphs
* Export to Excel/PDF
* Docker deployment
* CI/CD pipeline
