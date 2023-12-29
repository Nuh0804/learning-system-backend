from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
#for teacher
router.register('course', TestViewset,basename='course')
result_router = routers.NestedDefaultRouter(router, 'course', lookup = 'course')
result_router.register('results', ResultViewset, basename='results')
router.register('question_make', QuestionCreateViewset, basename = 'question')

#nested routers
question_make_router = routers.NestedDefaultRouter(router, 'question_make', lookup='question_make')
question_make_router.register('choices', MultipleChoiceMakeViewset, basename='choices')


#for student
router.register('questions', QuestionViewset, basename='questions')

#nested routers
answering_router = routers.NestedDefaultRouter(router, 'questions', lookup = 'questions')
answering_router.register('answers', AnsweringViewset, basename='answers')



urlpatterns = router.urls + question_make_router.urls + answering_router.urls + result_router.urls