from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, StudentUser
from .serializers import *
from myusers.serializers import UserCreaterSerializer
from .models import *

# Create your views here.

class CourseViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class CourseContentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = CourseContent.objects.all()
    serializer_class = CourseContentSerializer
    def get_serializer_context(self):
        return {
        'request': self.request,
        'course_id': self.kwargs['course_pk']
    }


class StudentEnrollingViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            message = {'false': 'you are not authenticated'}
            return StudentCourse.objects.none() 
        student = Student.objects.get(user = user) 
        return StudentCourse.objects.filter(student = student)
    
    def get_serializer_class(self):
        user = self.request.user
        if self.request.method =='POST':
            if user.is_anonymous:
                 return UserCreaterSerializer
            return EnrolledCourseForStudentSerializer
        return EnrolledCourseForStudentSerializer
    
    def get_serializer_context(self):
        return {'course_id': self.kwargs['course_pk']}
    



