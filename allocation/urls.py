from django.urls import path

from .views import (
    StudentListCreateView,
    CourseListCreateView,
    SeatReservationListCreateView,
    CoursePreferenceListCreateView,
    AllocationListView,AllocationProcessView,
)

from .views import allocation_dashboard,students_page,courses_page,allocations_page,preferences_page,reservations_page



urlpatterns = [
    path(
        "students/",
        StudentListCreateView.as_view(),
        name="student-list-create"
    ),

    path(
        "courses/",
        CourseListCreateView.as_view(),
        name="course-list-create"
    ),

    path(
        "reservations/",
        SeatReservationListCreateView.as_view(),
        name="reservation-list-create"  
    ),

    path(
        "preferences/",
        CoursePreferenceListCreateView.as_view(),
        name="preference-list-create"
    ),

    path(
        "allocations/",
        AllocationListView.as_view(),
        name="allocation-list"
    ),
    path(
    "allocate/",
    AllocationProcessView.as_view(),
    name="allocate"
    ),
    path(
    "dashboard/",
    allocation_dashboard,
    name="allocation-dashboard"
    ),
    path(
    "students-page/",
    students_page,
    name="students-page"
    ),
    path(
    "courses-page/",
    courses_page,
    name="courses-page"
    ),
    path(

    "allocations-page/",
    allocations_page,
    name="allocations-page"),
    path(
    "preferences-page/",
    preferences_page,
    name="preferences-page"
    ),

    path(
        "reservations-page/",
        reservations_page,
        name="reservations-page"
    ),


]