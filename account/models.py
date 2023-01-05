from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import get_user_model

User = get_user_model()


class Profile(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sender = models.BooleanField()

    def __str__(self):
        return f'{AbstractUser.username} is sender: {self.is_sender}'
