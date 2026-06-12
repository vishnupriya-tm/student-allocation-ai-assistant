
# Register your models here.
from django.contrib import admin
from .models import (
    Student,
    Course,
    SeatReservation,
    CoursePreference,
    Allocation,RejectedAllocation
)

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(SeatReservation)
admin.site.register(CoursePreference)
admin.site.register(Allocation)
admin.site.register(RejectedAllocation)
