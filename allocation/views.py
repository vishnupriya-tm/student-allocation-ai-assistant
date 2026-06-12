from django.shortcuts import render
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


