from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from random import randint

from utils import messages, tools
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailFieldField()

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["email", "token"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        #create_team_for_user.delay(user.id)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=8)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)

        user = authenticate(username=email)

        if user is None:
            raise ValidationError(messages.INCORRECT_EMAIL_OR_USER)

        if not user.is_active:
            raise ValidationError(messages.NONE_ACTIVE_USER)

        return {"email": user.email, "token": user.token}

    def create(self, validated_data):
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
        )


