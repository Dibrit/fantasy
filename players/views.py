from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from random import randint

from utils import messages, tools
from .models import User


class GameSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        email = self.validated_data["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist as error:
            return {"message": str(error)}
        money = user.money
        power = user.power
        powerbot = randint(power-10, power+10)
        if powerbot + power < power:
            money += 1000000
        else:
            money -= 1000000
        user.set_money(money)
        user.save()


class BuySerializer(serializers.ModelSerializer):



class SellSerializer(serializers.ModelSerializer):