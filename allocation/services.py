from django.db import transaction

from .models import (
    Student,
    CoursePreference,
    Allocation,
    SeatReservation,
    RejectedAllocation
)



def get_available_seats(course, category):

    # Total course capacity check

    total_allocated = Allocation.objects.filter(

        course=course

    ).count()

    total_remaining = (

        course.total_seats

        - total_allocated

    )

    if total_remaining <= 0:

        return 0


    reservation = SeatReservation.objects.filter(

        course=course,

        category=category

    ).first()


    if reservation:

        category_allocated = Allocation.objects.filter(

            course=course,

            student__category=category

        ).count()


        reserved_remaining = (

            reservation.reserved_seats

            - category_allocated

        )

        return min(

            total_remaining,

            reserved_remaining

        )


    return 0


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

        preferences = student.preferences.all().order_by("priority")
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