
# Register your models here.
from django.contrib import admin
from .models import (
    Student,
    Course,
    SeatReservation,
    CoursePreference,
    Allocation
)

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(SeatReservation)
admin.site.register(CoursePreference)
admin.site.register(Allocation)
#admin password:Admin@123