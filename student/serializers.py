from rest_framework import serializers
from student.models import *
from datetime import date
from rest_framework.validators import ValidationError

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ["fullname", "score", "courses"]

    def get_courses(self, obj):
        return obj.courses.values()


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
    
    def create(self, validated_data):
        # validated_data["title"] = validated_data["title"] + "1404"
        my_instance = super().create(validated_data)
        my_instance.start_date = date.today()
        my_instance.save()
        return my_instance
    
    # def update(self, instance, validated_data):
    #     request = self.context.get("request")
    #     print(request.user.id)
    #     print(instance.teacher.profile.user.id)
    #     if request.user.id == instance.teacher.profile.user.id:
    #         return super().update(instance, validated_data)
    #     else:
    #         raise ValidationError("Access Error")