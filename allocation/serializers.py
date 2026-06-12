from rest_framework import serializers

from .models import (
    Student,
    Course,
    SeatReservation,
    CoursePreference,
    Allocation
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SeatReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatReservation
        fields = "__all__"


class CoursePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePreference
        fields = "__all__"


class AllocationSerializer(serializers.ModelSerializer):

    student_name = serializers.CharField(
        source='student.name',
        read_only=True
    )

    course_name = serializers.CharField(
        source='course.course_name',
        read_only=True
    )

    class Meta:
        model = Allocation
        fields = '__all__'