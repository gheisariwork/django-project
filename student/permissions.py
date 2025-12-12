from rest_framework.permissions import BasePermission
from django.db import models

class IsStudent(BasePermission):

    def has_permission(self, request, view):
        return request.user.profile.is_student
    
class IsTeacher(BasePermission):

    def has_permission(self, request, view):
        return not request.user.profile.is_student
    

class IsActiveCourse(BasePermission):
    message = "اجازه ندارد"
    def has_object_permission(self, request, view, obj):
        return obj.is_active
    
class ModifyCourse(BasePermission):
    message = "اجازه ندارد"
    def has_object_permission(self, request, view, obj):
        return obj.teacher.profile.user.id == request.user.idپ
    
class PermissionModels(models.Model):
    class Meta:
        permissions = (
            ("can_drive", "Can drive"),
            ("can_vote", "Can vote in elections"),
            ("can_drink", "Can drink alcohol"),
        )