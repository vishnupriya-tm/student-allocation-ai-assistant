from django.db import transaction

from .models import (
    Student,
    CoursePreference,
    Allocation,
    SeatReservation,
    RejectedAllocation
)



def get_available_seats(course, category):
    reservation = SeatReservation.objects.filter(
        course=course,
        category=category
    ).first()

    if not reservation:
        return 0

    allocated_count = Allocation.objects.filter(
        course=course,
        student__category=category
    ).count()

    return reservation.reserved_seats - allocated_count


@transaction.atomic
def run_allocation():

    Allocation.objects.all().delete()
    RejectedAllocation.objects.all().delete()

    students = Student.objects.order_by(
        '-marks',
        'application_date'
    )

    for student in students:

        allocated = False

        preferences = student.preferences.all()

        for preference in preferences:

            course = preference.course

            available_seats = get_available_seats(
                course,
                student.category
            )

            if available_seats > 0:

                Allocation.objects.create(
                    student=student,
                    course=course,
                    allocated_priority=preference.priority
                )

                allocated = True
                break

        if not allocated:

            RejectedAllocation.objects.create(
                student=student,
                reason="No seats available in preferred courses"
            )