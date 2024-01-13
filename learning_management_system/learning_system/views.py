from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.permissions imp
from .permissions import IsAdminOrReadOnly
from .serializers import *
from .models import *

# Create your views here.

class CourseViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class CourseContentViewSet(viewsets.ModelViewSet):
    queryset = CourseContent.objects.all()
    serializer_class = CourseContentSerializer
    def get_serializer_context(self):
        return {
        'request': self.request,
        'course_id': self.kwargs['course_pk']
    }