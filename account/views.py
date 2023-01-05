from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Profile
from .serializers import IsSenderRegisterSerializer, BuyerRegisterSerializer


class IsSenderProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = IsSenderRegisterSerializer


class BuyerProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = BuyerRegisterSerializer

