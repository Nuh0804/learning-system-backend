from django.db import models
from django.contrib import admin
from django.conf import settings
from uuid import uuid4
# Create your models here.

class Course(models.Model):
    id = models.CharField(primary_key = True)
    name = models.CharField()
    description = models.TextField()
    students_enroled = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return f'{self.id}'
    

class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.CharField()
    description = models.TextField()
    file = models.FileField(upload_to='content/')
    quiz = models.FileField(blank=True, upload_to='quiz')


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class CourseforTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = 'teacher')

    def __str__(self):
        return f'{self.teacher.user.first_name} {self.teacher.user.last_name}'
    
    @admin.display(ordering='teacher__user__first_name')
    def first_name(self):
        return self.teacher.user.first_name

    @admin.display(ordering='teacher__user__last_name')
    def last_name(self):
        return self.teacher.user.last_name

    class Meta:
        ordering = ['teacher__user__first_name', 'teacher__user__last_name']


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.student.user.first_name} {self.student.user.last_name}'
    
    @admin.display(ordering='student__user__first_name')
    def first_name(self):
        return self.student.user.first_name

    @admin.display(ordering='student__user__last_name')
    def last_name(self):
        return self.student.user.last_name

    class Meta:
        ordering = ['student__user__first_name', 'student__user__last_name']