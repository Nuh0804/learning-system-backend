from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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
    http_method_names = ['post']
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    # creates multiple objects at the same time in the api
    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = AnswerSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class TestViewset(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class ResultViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        course_id = self.kwargs['course_pk']
        user = self.request.user
        if user.is_staff:
            return Result.objects.all()
        return Result.objects.filter(user = user)
    
    
    serializer_class = ResultmakeSerializer        




    def get_serializer_context(self):
        return {'course_id': self.kwargs['course_pk']}