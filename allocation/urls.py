from django.urls import path

from .views import (
    StudentListCreateView,
    CourseListCreateView,
    SeatReservationListCreateView,
    CoursePreferenceListCreateView,
    AllocationListView,AllocationProcessView
)





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
]