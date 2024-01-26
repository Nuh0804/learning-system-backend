from django.contrib import admin
from .models import CourseforTeacher, StudentCourse
# Register your models here.

@admin.register(CourseforTeacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name']
    ordering = ['teacher__user__first_name', 'teacher__user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.register(StudentCourse)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'course']
    ordering = ['student__user__first_name', 'student__user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']