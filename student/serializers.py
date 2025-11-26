from rest_framework import serializers
from student.models import *
1
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["fullname", "score"]

class TeacherSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ["fullname", "score"]


class CourseSerializer(serializers.ModelSerializer):
    # students = serializers.ListField(write_only=True, required=False)
    # students = StudentSerializer(many=True, read_only=True)
    students = serializers.SerializerMethodField()
    teacher = TeacherSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = "__all__"

    def get_students(self, obj):
        result = obj.students.values("fullname", "score")
        return result