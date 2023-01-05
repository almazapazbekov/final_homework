from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.views import get_user_model


# User_model = get_user_model()

# class User(AbstractBaseUser):
#     class Meta:
#         fields = "__all__"

class Profile(AbstractBaseUser):
    username = models.CharField(max_length=128)
    is_sender = models.BooleanField()

    def __str__(self):
        return f'{self.username} is sender: {self.is_sender}'
