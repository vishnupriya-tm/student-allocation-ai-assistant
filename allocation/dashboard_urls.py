from django.urls import path
from .dashboard_views import *

urlpatterns = [

    path(
        'dashboard/allocated/',
        AllocatedStudentsView.as_view()
    ),

    path(
        'dashboard/category-summary/',
        CategorySummaryView.as_view()
    ),

    path(
        'dashboard/course-stats/',
        CourseStatisticsView.as_view()
    ),

    path(
        'dashboard/seats/',
        AvailableSeatsView.as_view()
    ),
]