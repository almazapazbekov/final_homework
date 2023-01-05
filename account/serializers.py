import datetime

from rest_framework import serializers

from .models import Profile


class IsSenderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

        # read_only_fields = ['is_sender', ]

    def create(self, validated_data):
        new_user = Profile(
            username=validated_data['username'],
            last_login=validated_data['last_login'],
            password=validated_data['password'],
            is_sender=validated_data['is_sender'],

        )
        new_user.is_sender = True
        new_user.last_login = datetime.datetime.now()
        print(new_user.is_sender)

        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user


# оптимизировать
class BuyerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

        # read_only_fields = ['is_sender', ]

    def create(self, validated_data):
        new_user = Profile(
            username=validated_data['username'],
            last_login=validated_data['last_login'],
            password=validated_data['password'],
            is_sender=validated_data['is_sender'],

        )
        new_user.is_sender = False
        new_user.last_login = datetime.datetime.now()
        print(new_user.is_sender)

        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
