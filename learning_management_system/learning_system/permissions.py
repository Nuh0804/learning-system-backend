from rest_framework import permissions
from .models import CourseContent

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    

class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj:CourseContent):
        if not request.user.is_authenticated:  # Deny access if not authenticated
            return False
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.course.teacher.user == request.user
    
