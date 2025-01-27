from rest_framework import serializers
from.models import Encrypt

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encrypt
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encrypt
        fields = ["username", "password"]
