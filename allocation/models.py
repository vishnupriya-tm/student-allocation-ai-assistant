from django.db import models




class Student(models.Model):
    CATEGORY_CHOICES = [
        ('GENERAL', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
    ]

    student_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    application_date = models.DateField()
    def __str__(self):
        return f"{self.student_id} - {self.name}"


class Course(models.Model):
    course_name = models.CharField(max_length=255, unique=True)
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name


class SeatReservation(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='seat_reservations'
    )

    category = models.CharField(max_length=20)
    reserved_seats = models.PositiveIntegerField()

    class Meta:
        unique_together = ('course', 'category')


class CoursePreference(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='preferences'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    priority = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('student', 'priority')
        ordering = ['priority']


class Allocation(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    allocated_priority = models.PositiveSmallIntegerField()

    allocated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} -> {self.course.course_name}"
    
class RejectedAllocation(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    reason = models.TextField()

    rejected_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.name} - Rejected"