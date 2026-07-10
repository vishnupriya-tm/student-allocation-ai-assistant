from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import run_allocation

from .models import (
    Student,
    Course,
    SeatReservation,
    CoursePreference,
    Allocation
)

from .serializers import (
    StudentSerializer,
    CourseSerializer,
    SeatReservationSerializer,
    CoursePreferenceSerializer,
    AllocationSerializer
)


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SeatReservationListCreateView(generics.ListCreateAPIView):
    queryset = SeatReservation.objects.all()
    serializer_class = SeatReservationSerializer


class CoursePreferenceListCreateView(generics.ListCreateAPIView):
    queryset = CoursePreference.objects.all()
    serializer_class = CoursePreferenceSerializer


class AllocationListView(generics.ListAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

class AllocationProcessView(APIView):

    def post(self, request):

        run_allocation()

        return Response({
            "message": "Allocation completed successfully"
        })
from django.shortcuts import render


from django.shortcuts import render
from django.db.models import Count

from .models import (
    Student,
    Course,
    Allocation
)


def allocation_dashboard(request):

    student_count = Student.objects.count()

    course_count = Course.objects.count()

    allocation_count = Allocation.objects.count()


    allocations = Allocation.objects.select_related(

        "student",

        "course"

    ).order_by(

        "-allocated_at"

    )


    # Category summary

    category_summary = (

        Allocation.objects

        .values(

            "student__category"

        )

        .annotate(

            count=Count("id")

        )

    )


    # Course statistics

    course_stats = []

    for course in Course.objects.all():

        allocated = Allocation.objects.filter(

            course=course

        ).count()

        available = (

            course.total_seats

            -

            allocated

        )

        course_stats.append(

            {

                "course_name":

                course.course_name,

                "total":

                course.total_seats,

                "allocated":

                allocated,

                "available":

                available

            }

        )


    return render(

        request,

        "allocation/dashboard.html",

        {

            "student_count":

            student_count,

            "course_count":

            course_count,

            "allocation_count":

            allocation_count,

            "allocations":

            allocations,

            "category_summary":

            category_summary,

            "course_stats":

            course_stats

        }

    )
def students_page(request):

    students = Student.objects.all().order_by(
        "id"
    )

    return render(

        request,

        "allocation/students.html",

        {

            "students": students

        }

    )
def courses_page(request):

    courses = Course.objects.all()

    return render(

        request,

        "allocation/courses.html",

        {

            "courses": courses

        }

    )
def allocations_page(request):

    allocations = Allocation.objects.select_related(
        "student",
        "course"
    ).order_by(
        "-allocated_at"
    )

    return render(

        request,

        "allocation/allocations.html",

        {

            "allocations": allocations,

            "allocation_count": allocations.count()

        }

    )


from django.contrib import messages

def preferences_page(request):

    if request.method == "POST":
        student = request.POST.get("student")
        course = request.POST.get("course")
        priority = request.POST.get("priority")

        # Get existing record with same priority
        existing_priority = CoursePreference.objects.filter(
            student_id=student,
            priority=priority
        ).first()

        # Get existing record with same course
        existing_course = CoursePreference.objects.filter(
            student_id=student,
            course_id=course
        ).first()

        # Case 1: Exact same record
        if existing_course and existing_course.priority == int(priority):

            messages.info(
                request,
                "This preference already exists."
            )

        # Case 2: Same course already exists with another priority
        elif existing_course:

            messages.error(
                request,
                "This course is already selected by the student."
            )

        # Case 3: Same priority exists -> Update (acts like edit)
        elif existing_priority:

            existing_priority.course_id = course
            existing_priority.save()

            messages.success(
                request,
                "Preference updated successfully."
            )

        # Case 4: New preference
        else:

            CoursePreference.objects.create(
                student_id=student,
                course_id=course,
                priority=priority
            )

            messages.success(
                request,
                "Preference added successfully."
            )

        return redirect("/api/preferences-page/")
    return render(
        request,
        "allocation/preferences.html",
        {
            "students": Student.objects.all(),
            "courses": Course.objects.all(),
            "preferences": CoursePreference.objects.select_related(
                "student",
                "course"
            ).order_by(
                "student",
                "priority"
            )
        }
    )
   
def reservations_page(request):

    if request.method == "POST":

        SeatReservation.objects.create(

            course_id=request.POST.get("course"),

            category=request.POST.get("category"),

            reserved_seats=request.POST.get("reserved_seats")

        )

        return redirect("/api/reservations-page/")


    return render(

        request,

        "allocation/reservations.html",

        {

            "courses": Course.objects.all(),

            "reservations": SeatReservation.objects.select_related(
                "course"
            )

        }

    )

