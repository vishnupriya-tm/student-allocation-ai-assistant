from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Allocation,
    Course,
    SeatReservation
)



class AllocatedStudentsView(APIView):

    def get(self, request):

        allocations = Allocation.objects.select_related(
            'student',
            'course'
        )

        data = []

        for allocation in allocations:

            data.append({
                "student": allocation.student.name,
                "course": allocation.course.course_name,
                "priority": allocation.allocated_priority
            })

        return Response(data)
    
class CategorySummaryView(APIView):

    def get(self, request):

        data = Allocation.objects.values(
            'student__category'
        ).annotate(
            total=Count('id')
        )

        return Response(data)
    

class CourseStatisticsView(APIView):

    def get(self, request):

        stats = Allocation.objects.values(
            'course__course_name'
        ).annotate(
            allocated=Count('id')
        )

        return Response(stats)
    

class AvailableSeatsView(APIView):

    def get(self, request):

        result = []

        reservations = SeatReservation.objects.select_related(
            'course'
        )

        for reservation in reservations:

            allocated = Allocation.objects.filter(
                course=reservation.course,
                student__category=reservation.category
            ).count()

            result.append({
                "course": reservation.course.course_name,
                "category": reservation.category,
                "available_seats":
                    reservation.reserved_seats - allocated
            })

        return Response(result)