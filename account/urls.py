from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/sender', views.SenderProfileCreateAPIView.as_view()),
    path('register/buyer', views.BuyerProfileCreateAPIView.as_view()),
    path('token/', obtain_auth_token),
]


