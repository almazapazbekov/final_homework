from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Profile, User
from .serializers import IsSenderRegisterSerializer


class IsSenderListCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = IsSenderRegisterSerializer




# class ProfileRegisterAPIView(generics.CreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileRegisterSerializer


# class UserRegisterAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer
