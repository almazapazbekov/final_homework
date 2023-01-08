from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Profile(User):
    is_sender = models.BooleanField()


