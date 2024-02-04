from rest_framework import serializers
from .models import *
from django.conf import settings
from myusers.serializers import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description','teacher', 'students_enroled']
   

class CourseContentSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url = True)
    quiz = serializers.FileField(use_url = True, required = False, allow_null=True)
    class Meta:
        model = CourseContent
        fields = ['course', 'module', 'description', 'file', 'quiz']

    
    def create(self, validated_data):
        course_id = self._context['course_id']
        return CourseContent.objects.create(course_id = course_id, **validated_data)
    

class EnrolledCourseForStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = ['student', 'course']

    
    def create(self, validated_data):
        student = validated_data['student']
        course_id = validated_data['course']

        #checks whether the student is already enrolled in the course
        is_enrolled = StudentCourse.objects.filter(student = student, course = course_id.id)
        if is_enrolled:
            raise serializers.ValidationError('already enrolled')
        
        return StudentCourse.objects.create(course_id = course_id.id, **validated_data)
    

class TeachersCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseforTeacher
        field = ['teacher', 'course']