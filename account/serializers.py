from rest_framework import serializers

from .models import Profile


class IsSenderRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ['is_sender', ]

    def create(self, validated_data):
        new_user = Profile(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
