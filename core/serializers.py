from rest_framework import serializers
from .models import Department, Employee, Attendance, PerformanceReview

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    attendances = AttendanceSerializer(many=True, read_only=True)
    reviews = PerformanceReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
