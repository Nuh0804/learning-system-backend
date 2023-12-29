from django.shortcuts import render
from rest_framework import viewsets
from .models import Question, Choice, Answer, Result, Test
from .serializer import QuestionCreateSerializer, MultipleChoiceMakeSerializer, QuestionSerializer, AnswerSerializer, ResultmakeSerializer, TestSerializer
# Create your views here.
#for teacher
class QuestionCreateViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer


class MultipleChoiceMakeViewset(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = MultipleChoiceMakeSerializer

    def get_serializer_context(self):
        return {'question_id': self.kwargs['question_make_pk']}

#for student
class QuestionViewset(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnsweringViewset(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_serializer_context(self):
        return {'question_id': self.kwargs['questions_pk']}
    


class TestViewset(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class ResultViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        course_id = self.kwargs['course_pk']
        return Result.objects.filter()
    serializer_class = ResultmakeSerializer

    def get_serializer_context(self):
        return {'course_id': self.kwargs['course_pk']}