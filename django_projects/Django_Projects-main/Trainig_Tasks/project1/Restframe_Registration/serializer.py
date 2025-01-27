from rest_framework import serializers
from.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = "__all__"

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ('username', 'password')


