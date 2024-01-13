from rest_framework import serializers
from .models import *
from django.conf import settings

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'enrollment_key']



class CourseContentSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url = True)
    quiz = serializers.FileField(use_url = True, required = False, allow_null=True)
    class Meta:
        model = CourseContent
        fields = ['course', 'module', 'description', 'file', 'quiz']

    
    def create(self, validated_data):
        course_id = self._context['course_id']
        return CourseContent.objects.create(course_id = course_id, **validated_data)