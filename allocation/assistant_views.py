from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Allocation,
    CoursePreference,
    RejectedAllocation
)

class AssistantAPIView(APIView):

    def post(self, request):

        question = request.data.get(
            "question",
            ""
        ).lower()

        if "allocated to each course" in question:

            data = Allocation.objects.values(
                'course__course_name'
            ).annotate(
                total=Count('id')
            )

            return Response({
                "answer": list(data)
            })


        elif "first preference" in question:

            result = []

            allocations = Allocation.objects.select_related(
                'student',
                'course'
            )

            for allocation in allocations:

                first_preference = CoursePreference.objects.filter(
                    student=allocation.student,
                    priority=1
                ).first()

                if (
                    first_preference and
                    first_preference.course != allocation.course
                ):

                    result.append({
                        "student": allocation.student.name,
                        "allocated_course":
                            allocation.course.course_name,
                        "first_preference":
                            first_preference.course.course_name
                    })

            return Response({
                "answer": result
            })


        elif "highest rejection rate" in question:

            total_rejections = RejectedAllocation.objects.count()

            return Response({
                "answer":
                    f"Total rejections: {total_rejections}"
            })


        elif "category-wise" in question:

            data = Allocation.objects.values(
                'student__category'
            ).annotate(
                total=Count('id')
            )

            return Response({
                "answer": list(data)
            })

        return Response({
            "answer":
                "Question not supported."
        })