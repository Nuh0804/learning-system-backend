from django.db import models
from django.conf import settings
from uuid import uuid4
# Create your models here.

class Course(models.Model):
    id = models.CharField(primary_key = True)
    name = models.CharField()
    description = models.TextField()
    enrollment_key = models.CharField()
    students_enroled = models.IntegerField(default = 0)
    

class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.CharField()
    description = models.TextField()
    file = models.FileField(upload_to='content/')
    quiz = models.FileField(blank=True, upload_to='quiz')

class Teacher(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = 'teacher')


class Student(models.Model):
    reg_no = models.CharField(primary_key = True, unique = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, blank = True)