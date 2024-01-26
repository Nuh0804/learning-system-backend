from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register('Course', CourseViewset, basename='course')
contentrouter = NestedDefaultRouter(router, 'Course', lookup= 'course')
contentrouter.register('content', CourseContentViewSet, basename='content')

enrolling_router = NestedDefaultRouter(router, 'Course', lookup = 'course')
enrolling_router.register('enroll', StudentEnrollingViewset, basename='student')
# router.register('Student', StudentProfileViewset, basename='student')
urlpatterns = router.urls + contentrouter.urls + enrolling_router.urls