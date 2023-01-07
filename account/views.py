from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Profile
from .serializers import SenderRegisterSerializer, BuyerRegisterSerializer


class SenderProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = SenderRegisterSerializer


class BuyerProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = BuyerRegisterSerializer

