from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename='course')
contentrouter = NestedDefaultRouter(router, 'Course', lookup= 'course')
contentrouter.register('content', CourseContentViewSet, basename='content')

urlpatterns = router.urls + contentrouter.urls