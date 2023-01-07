import datetime

from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Profile, User


class SenderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'is_sender', ]
        read_only_fields = ['is_sender', ]

    def create(self, validated_data):
        new_user = Profile(
            username=validated_data['username'],
        )
        new_user.is_sender = True
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user


class BuyerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'is_sender', ]
        read_only_fields = ['is_sender', ]

    def create(self, validated_data):
        new_user = Profile(
            username=validated_data['username'],
        )
        new_user.is_sender = False
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user



