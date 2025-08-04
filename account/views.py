from django.shortcuts import render
from rest_framework import generics

from account.models import CustomUser
from account.serializers import CustomUserSerializer


# Create your views here.


class CustomUserRegisterAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

