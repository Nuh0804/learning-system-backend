from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,generics
from .models import User
from . serializers import RegisterUserSerializer
from rest_framework import status



# Create your views here.
class RegisterUserGet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

class RegisterUserPost(APIView):
    def post(self, request):
         #queryset = User.objects.get()
         serializer = RegisterUserSerializer(data= request.data)
         if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
         return Response(status, status= status.HTTP_400_BAD_REQUEST)



    