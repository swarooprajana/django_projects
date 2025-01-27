from rest_framework import serializers
from .models import ForgetModels


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgetModels
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgetModels
        fields = ["password"]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgetModels
        fields = ["username", "password"]


