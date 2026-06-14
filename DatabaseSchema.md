# Database Schema

## Student

| Field            | Type         |
| ---------------- | ------------ |
| id               | Integer      |
| student_id       | CharField    |
| name             | CharField    |
| marks            | DecimalField |
| category         | CharField    |
| application_date | DateField    |

---

## Course

| Field       | Type      |
| ----------- | --------- |
| id          | Integer   |
| course_name | CharField |
| total_seats | Integer   |

---

## SeatReservation

| Field          | Type               |
| -------------- | ------------------ |
| id             | Integer            |
| course         | ForeignKey(Course) |
| category       | CharField          |
| reserved_seats | Integer            |

---

## CoursePreference

| Field    | Type                |
| -------- | ------------------- |
| id       | Integer             |
| student  | ForeignKey(Student) |
| course   | ForeignKey(Course)  |
| priority | Integer             |

---

## Allocation

| Field              | Type               |
| ------------------ | ------------------ |
| id                 | Integer            |
| student            | OneToOne(Student)  |
| course             | ForeignKey(Course) |
| allocated_priority | Integer            |
| allocated_at       | DateTime           |

---

## RejectedAllocation

| Field   | Type                |
| ------- | ------------------- |
| id      | Integer             |
| student | ForeignKey(Student) |
| reason  | TextField           |
